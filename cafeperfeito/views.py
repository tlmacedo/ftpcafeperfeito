# import xml.etree.ElementTree as ET
import datetime

import bcrypt
from django.shortcuts import render

from cafeperfeito.models import *

now = datetime.datetime.now()


def senhaEncrypt(senha):
    return bcrypt.hashpw(senha, bcrypt.gensalt(10))


def senhaValida(senha, senha_db):
    return bcrypt.checkpw(senha, senha_db)


def index(request):
    mailusuario = 'tl.macedo@hotmail.com'
    context = {'now': now,
               'usuario': Usuario.objects.get(email=mailusuario)
               }
    return render(request, 'cafeperfeito/index.html', context)


def produto(request):
    mailusuario = 'tl.macedo@hotmail.com'
    context = {'now': now,
               'usuario': Usuario.objects.get(email=mailusuario)
               }
    return render(request, 'cafeperfeito/produto.html', context)


def empresa(request):
    mailusuario = 'tl.macedo@hotmail.com'
    context = {'now': now,
               'usuario': Usuario.objects.get(email=mailusuario)
               }
    return render(request, 'cafeperfeito/empresa.html', context)

# def index(request):
#     if request.method == 'POST':
#         mailusuario = request.POST.get('loginEmail')
#         nsenha = request.POST.get('loginSenha')
#
#         usuario = Usuario.objects.get(email=mailusuario)
#         if usuario is None:
#             print('Usuario não existe')
#         else:
#             context = {
#                 'now': now,
#                 'usuario': usuario,
#                 'menu_itens': Menuprincipal.objects.all(),
#             }
#             if bcrypt.checkpw(str(nsenha).encode(), str(usuario.senha).encode()) is True:
#                 return render(request, 'cafeperfeito/index.html', context=context)
#             else:
#                 print('Senha inválida')
#     return render(request, 'cafeperfeito/login.html', context={'now': now, })

# def index(request):
#     usuario = Usuario.objects.get(email='tl.macedo@hotmail.com')
#     context = {
#         'now': now,
#         'usuario': usuario,
#         'menu_itens': Menuprincipal.objects.all(),
#     }
#     return render(request, 'cafeperfeito/index.html', context=context)


# def produto(request):
#     context = {
#         'now': now,
#         'usuario': usuario,
#         'menu_itens': Menuprincipal.objects.all(),
#     }
#     return render(request, 'cafeperfeito/produto.html')

# colaboradores = Colaborador.objects.select_related('cargo').all()
# print('colaboradores.count {}'.format(colaboradores.count()))
# for colaborador in colaboradores:
#     print('colaborador.cargo {}'.format(colaborador.cargo))
#

# usuarios = Usuario.objects.filter(colaborador__id=2)
# for user in usuarios:
#     #     telefonesColab = Telefone.objects.filter(colaboradortelefone__colaboradorvo__id=user.id.id)
#     #     print('telefonesColab: [{}]'.format(telefonesColab.model.descricao))
#     # telefones = []
#     # for tel in user.colaborador.colaboradortelefone_set.all():
#     #     print('tel: {}'.format(tel))
#     #     telefones.insert(tel)
#     print('users: ', 'id:{}'
#                      '\n    nome: {}'
#                      '\n    cargo: {}'
#                      '\n    senha; {}'
#                      # '\n    telefone: {}'
#           .format(user.colaborador.id,
#                   user.colaborador.nome,
#                   user.colaborador.cargo.descricao,
#                   user.senha
#                   # user.colaborador.colaboradortelefone_set.all()
#                   # telefones
#                   )
#           )

# cargos = Cargo.objects.all()
# for cargo in cargos:
#     print('cargo: '
#           ' id: {:>2}'
#           ' descrição: {}'
#         .format(
#         cargo.id,
#         cargo.descricao
#     )
#     )

# x = {"name": "John",
#      "age": 30,
#      "married": True,
#      "divorced": False,
#      "children": ("Ann", "Billy"),
#      "pets": None,
#      "cars": [
#          {"model": "BMW 230", "mpg": 27.5},
#          {"model": "Ford Edge", "mpg": 24.1}
#      ]}

# use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))

# usuarios = Usuario.objects.select_related()
# print(serializers.serialize('json', usuarios, indent=4))

# colaboradores = Colaborador.objects.select_related()
# print(colaboradores.values())
# json.loads(colaboradores)
# cjson.decode(colaboradores)
# print(json.loads(colaboradores))
# data = serializers.serialize('json', colaboradores, indent=4)
# print(json.dumps(context, indent=4))
# for colaborador in colaboradores:
#     print(colaborador)

# colaboradores = Colaborador.objects.select_related().values()
# print(json.dumps(colaboradores, indent=4))

# cargos = Cargo.objects.select_related()
# for cargo in cargos:
#     print(cargo)
#
# print(json.dumps({'Cargos': list(cargos)}, indent=4))

# usuarios = Usuario.objects.select_related()
# print(json.dumps({'Usuarioss': list(usuarios.values())}, indent=2))

# empresas = {'Empresa': Empresa.objects.filter(id=1)}
# print(json.dumps(empresas, indent=4))

# empresas = Empresa.objects.filter(id=1)
# for empresa in empresas:
#     print('users: [{}]'.format(empresa))
#     # print(
#     #     '\tid: {:>2}'
#     #     '\n\tnome: {}'
#     #     '\n\tapelido: {}'
#     #     '\n\tcargo: {}'
#     #     '\n\tsenha: [{}]'
#     #     '\n\tsituacao: {}'
#     #     '\n\n'
#     #     .format(
#     #         usuario.id,
#     #         usuario.nome,
#     #         usuario.apelido,
#     #         usuario.cargo,
#     #         usuario.usuario.senha,
#     #         usuario.usuario.getSituacao()
#     #     )
#     # )

# usuarios = Usuario.objects.select_related()
#
# print('[{}] - numero de conexões no banco'.format(len(connection.queries)))
# return render(request, 'cafeperfeito/login.html', )
