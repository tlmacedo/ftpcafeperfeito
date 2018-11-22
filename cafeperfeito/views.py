# import xml.etree.ElementTree as ET
import bcrypt
from django.shortcuts import render

from cafeperfeito.models import *


def senhaEncrypt(senha):
    return bcrypt.hashpw(senha, bcrypt.gensalt(10))


def senhaValida(senha, senha_db):
    return bcrypt.checkpw(senha, senha_db)


def index(request):
    # tree = ET.parse('cafeperfeito/static/cafeperfeito/xml/configSistema.xml')
    # root = tree.getroot()
    # print('tag: {}, attrib: {}'.format(root.tag, root.attrib))
    # for child in root:
    #     if len(child.getchildren()) == 1:
    #         print('\t{} [{}]'.format(child.tag, child.text))
    #     else:
    #         print('\t{} [{}]'.format(child.tag, child.text))
    #         filhos1 = child.getchildren()
    #         for filho1 in filhos1:
    #             if len(filho1.getchildren()) == 1:
    #                 print('\t\t{} [{}]'.format(filho1.tag, filho1.text))
    #             else:
    #                 print('\t\t{} [{}]'.format(filho1.tag, filho1.text))
    #                 filhos2 = filho1.getchildren()
    #                 for filho2 in filhos2:
    #                     print('\t\t\t{} [{}]'.format(filho2.tag, filho2.text))

    # print('tree.getroot()', root.tag)
    # print('tag=%s, attrib=%s' % (root.tag, root.attrib))
    # print("-" * 40)
    # print("Iterating using getchildren()")
    # print("-" * 40)
    # print('copyright: ', root)
    # users = root.getchildren()
    # for user in users:
    #     user_children = user.getchildren()
    #     for user_child in user_children:
    #         print("%s=%s" % (user_child.tag, user_child.text))
    #         user_childrenss = user_child.getchildren()
    #         for user_childrens in user_childrenss:
    #             print("%s=%s" % (user_childrens.tag, user_childrens.text))

    # if request.user.is_authenticated():
    #     return redirect('admin_page')

    # doc = minidom.parse('/Volumes/150GB-Development/__ftp/ftpcafeperfeito/cafeperfeito/static/cafeperfeito/xml/configSistema.xml')
    # print(doc.nodeName)
    # print(doc.firstChild.tagName)
    # itemList = doc.getElementsByTagName('connect_DB')
    # for s in itemList:
    #     print(s.getAttribute())

    # x = minidom.parse(
    #     '/Volumes/150GB-Development/__ftp/ftpcafeperfeito/cafeperfeito/static/cafeperfeito/xml/configSistema.xml')
    # nos = x.documentElement
    # print("1|-> %s" % nos.nodeName)
    # filhos1 = [no for no in nos.childNodes if no.nodeType == x.ELEMENT_NODE]
    # for pai in filhos1:
    #     print("2|--> %s" % pai.nodeName)
    #     filhos2 = [no for no in pai.childNodes if no.nodeType == x.ELEMENT_NODE]
    #     for filho in filhos2:
    #         print("3|---> %s" % filho.nodeName)
    #         filhos3  = [no for no in filho.childNodes if no.nodeType == x.ELEMENT_NODE]
    #         for filho in filhos3:
    #             print("4|-----> %s" % filho.getAttribute.value)
    #         # print("5|-----> %s" % filho.getAttribute)

    if request.method == 'POST':
        nusuario = request.POST.get('usuarios')
        nsenha = request.POST.get('senha')

        # usuario = Tabcolaborador.autentica_login('', nusuario)
        usuario = Usuario.get_Usuario_Senha('', nusuario)
        print('usuario::', usuario[0])
        print('senha::', usuario[1])
        if usuario is None:
            print('Usuario não existe')
        else:
            if bcrypt.checkpw(str(nsenha).encode(), str(usuario[1]).encode()) is True:
                print('Senha Validade com sucesso!!!!!!!!!!!!!!!!!!!!!!!!')
                menu_itens = MenuPrincipal.objects.all()
                return render(request, 'cafeperfeito/navigation.html', {'menu_itens': menu_itens})
            else:
                print('Senha inválida')

    # else:
    #     messages.error(request, 'Error wrong username/password')
    usuarios = Colaborador.objects.all()
    return render(request, 'cafeperfeito/index.html', {'usuarios': usuarios})

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
