from django.http import JsonResponse
from cadastro.models.empresa import Empresa
from django.shortcuts import render
from cadastro.services.produto.cadastro_manualmente import CadastroManualServices
from django.views import View
from django.urls import reverse


class CadastroItensManual(View):

    def get(self, request):
        empresas = Empresa.objects.all().order_by('razao_social')

        return render(request, 'produtos/lista_produtosSped.html', {
            'empresas': empresas
        })

    def post(self, request):
        try:
            services = CadastroManualServices(request.POST)
            processamento = services.cadatro_manual()
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e) or 'Erro ao cadastrar produto.',
            }, status=500)

        if processamento.get('success'):
            return JsonResponse({
                'success': True,
                'message': 'Produto cadastrado com sucesso',
                'redirect_url': reverse('lista_produtos_sped'),
            })

        erro = processamento.get('error')
        return JsonResponse({
            'success': False,
            'message': str(erro) if erro else 'Erro ao cadastrar produto',
            'redirect_url': reverse('lista_produtos_sped'),
        }, status=400)
