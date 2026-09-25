from cadastro.models.produtos import Cadastro_itens_sped
from cadastro.models.empresa import Empresa
from django.db import IntegrityError
from cadastro.utils.normalizadores import NormalizadoresUtils


class CadastroManualServices:

    def __init__(self, data_job):
        self.data_job = data_job

    def cadatro_manual(self):
        try:
            empresa_id = self.data_job.get('empresa_id')
            if not empresa_id:
                return {'success': False, 'error': 'Selecione a empresa.'}

            empresa = Empresa.objects.get(id=empresa_id)
            data_inicio = self.data_job.get('data_inicio_sped') or None
            print(f'data_inicio: {data_inicio}')
            ano_sped = data_inicio[:4] if data_inicio and len(data_inicio) >= 4 else None
            print(f'ano sped: {ano_sped}')

            saldo_inicial = NormalizadoresUtils(
                self.data_job.get('saldo_inicial_produto')
            ).normalizador_decimal()
            saldo_final = NormalizadoresUtils(
                self.data_job.get('saldo_final_produto')
            ).normalizador_decimal()

            Cadastro_itens_sped.objects.create(
                empresa=empresa,
                data_inicio_sped=data_inicio,
                codigo_prod=self.data_job.get('codigo_prod') or None,
                descricao_prod=self.data_job.get('descricao_prod') or None,
                unidade=self.data_job.get('unidade') or None,
                tipo_item=self.data_job.get('tipo_item') or None,
                genero=self.data_job.get('genero') or None,
                ncm=self.data_job.get('ncm') or None,
                cest=self.data_job.get('cest') or None,
                mes_ref=self.data_job.get('mes_ref') or None,
                ano_sped=ano_sped,
                saldo_inicial_produto=saldo_inicial,
                saldo_final_produto=saldo_final,
            )

            return {'success': True}
        except Empresa.DoesNotExist:
            return {'success': False, 'error': 'Empresa não encontrada.'}
        except IntegrityError:
            return {'success': False, 'error': 'Já existe um produto com este código para a empresa selecionada.'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
