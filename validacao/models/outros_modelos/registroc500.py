from django.db import models
from validacao.models.participantes.participantes import Participantes
from cadastro.models.empresa import Empresa


class RegistroEnergiaC500(models.Model):

    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa", blank=True, null=True
    )
    reg = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        default="C500",
        verbose_name="Código do Registro",
    )
    data_inicio_sped = models.DateField(
        blank=True, null=True, verbose_name="Data inicio sped"
    )
    data_final_sped = models.DateField(
        blank=True, null=True, verbose_name="Data final sped"
    )
    mes_referencia = models.CharField(
        "Mês referencia", max_length=9, null=True, blank=True
    )
    ind_oper = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        verbose_name="Indicador do Tipo de Operação",
    )
    ind_emit = models.CharField(
        max_length=1, blank=True, null=True, verbose_name="Indicador do Emitente"
    )
    cod_part = models.ForeignKey(
        Participantes,
        on_delete=models.CASCADE,
        max_length=60,
        blank=True,
        null=True,
        verbose_name="Código do Participante",
    )
    cod_mod = models.CharField(
        max_length=2, blank=True, null=True, verbose_name="Modelo do Documento"
    )
    cod_sit = models.CharField(
        max_length=2, blank=True, null=True, verbose_name="Código da Situação"
    )
    ser = models.CharField(max_length=4, blank=True, null=True, verbose_name="Série")
    sub = models.CharField(max_length=7, blank=True, null=True, verbose_name="Subsérie")
    cod_cons = models.CharField(
        max_length=2, blank=True, null=True, verbose_name="Classe de Consumo"
    )
    num_doc = models.IntegerField(
        blank=True, null=True, verbose_name="Número do Documento"
    )
    dt_doc = models.DateField(blank=True, null=True, verbose_name="Data de Emissão")
    dt_e_s = models.DateField(
        blank=True, null=True, verbose_name="Data de Entrada/Saída"
    )
    vl_doc = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor Total do Documento",
    )
    vl_desc = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor Total do Desconto",
    )
    vl_forn = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor Fornecido/Consumido",
    )
    vl_serv_nt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor Serviços Não Tributados",
    )
    vl_terc = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor Cobrado de Terceiros",
    )
    vl_da = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor Despesas Acessórias",
    )
    vl_bc_icms = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Base de Cálculo do ICMS",
    )
    vl_icms = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, verbose_name="Valor do ICMS"
    )
    vl_bc_icms_st = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        verbose_name="Base de Cálculo do ICMS-ST",
    )
    vl_icms_st = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, verbose_name="Valor do ICMS-ST"
    )
    cod_inf = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Código da Informação Complementar",
    )
    vl_pis = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, verbose_name="Valor do PIS"
    )
    vl_cofins = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, verbose_name="Valor da COFINS"
    )
    tp_ligacao = models.CharField(
        max_length=1, blank=True, null=True, verbose_name="Tipo de Ligação"
    )
    cod_grupo_tensao = models.CharField(
        max_length=2, blank=True, null=True, verbose_name="Grupo de Tensão"
    )
    chv_doce = models.CharField(
        max_length=44,
        blank=True,
        null=True,
        verbose_name="Chave do Documento Eletrônico",
    )
    fin_doce = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        verbose_name="Finalidade do Documento Eletrônico",
    )
    chv_doce_ref = models.CharField(
        max_length=44,
        blank=True,
        null=True,
        verbose_name="Chave do Documento Eletrônico Referenciado",
    )
    ind_dest = models.CharField(
        max_length=1, blank=True, null=True, verbose_name="Indicador do Destinatário"
    )
    cod_mun_dest = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Código IBGE do Município do Destinatário",
    )
    cod_cta = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Conta Contábil"
    )
    cod_mod_doc_ref = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        verbose_name="Modelo do Documento Referenciado",
    )
    hash_doc_ref = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Hash do Documento Referenciado",
    )
    ser_doc_ref = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        verbose_name="Série do Documento Referenciado",
    )
    num_doc_ref = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        verbose_name="Número do Documento Referenciado",
    )
    mes_doc_ref = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        verbose_name="Mês/Ano do Documento Referenciado",
    )
    ener_injet = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, verbose_name="Energia Injetada"
    )
    outras_ded = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, verbose_name="Outras Deduções"
    )

    class Meta:
        verbose_name = "Registro C500"
        verbose_name_plural = "Registros C500"

    def __str__(self):
        return f"C500 - Doc {self.num_doc}"
