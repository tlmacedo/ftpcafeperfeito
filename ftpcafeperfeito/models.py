from base64 import b64encode

from django.db import models

from cafeperfeito.enums import UNIDADE_COMERCIAL, SITUACAO_NO_SISTEMA


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cargo'

    # def __str__(self):
    #     return str('[{:0>2}] {}'.format(self.id, self.descricao))


class Colaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    apelido = models.CharField(max_length=30)
    ctps = models.CharField(max_length=30)
    dataadmisao = models.DateTimeField(db_column='dataAdmisao', blank=True, null=True)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    ativo = models.TextField()
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING, blank=True, null=True)
    imgcolaborador = models.BinaryField(db_column='imgColaborador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colaborador'

    def get_colaborador_imagem(self):
        return b64encode(self.imgcolaborador).decode('ascii')

    class Meta:
        managed = False
        db_table = 'colaborador'

    def __str__(self):
        return self.nome

    def getColaborador(self):
        return {'id': self.id, 'nome': self.nome, 'apelido': self.apelido, 'ativo': self.ativo, 'cargo': self.cargo}


class Contato(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=40, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contato'


class ContatoEmailhomepage(models.Model):
    contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')
    emailhomepagelist = models.OneToOneField('Emailhomepage', models.DO_NOTHING, db_column='emailHomePageList_id',
                                             unique=True)

    class Meta:
        managed = False
        db_table = 'contato_emailHomePage'


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')
    telefonelist = models.OneToOneField('Telefone', models.DO_NOTHING, db_column='telefoneList_id',
                                        unique=True)

    class Meta:
        managed = False
        db_table = 'contato_telefone'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emailhomepage(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    tipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emailHomePage'


class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    lojasistema = models.TextField(db_column='lojaSistema')
    classifjuridica = models.IntegerField(db_column='classifJuridica')
    cnpj = models.CharField(max_length=14)
    ieisento = models.TextField(db_column='ieIsento')
    ie = models.CharField(max_length=14)
    razao = models.CharField(max_length=80)
    fantasia = models.CharField(max_length=80)
    cliente = models.TextField()
    fornecedor = models.TextField()
    transportadora = models.TextField()
    situacao = models.IntegerField()
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuariocadastroempresa',
                                        db_column='usuarioCadastro_id', blank=True,
                                        null=True)
    datacadastro = models.DateTimeField(auto_now_add=True, db_column='dataCadastro', blank=True, null=True)
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioatualizacaoempresa',
                                           db_column='usuarioAtualizacao_id', blank=True,
                                           null=True)
    dataatualizacao = models.DateTimeField(auto_now=True, db_column='dataAtualizacao', blank=True,
                                           null=True)
    dataabetura = models.DateTimeField(db_column='dataAbetura', blank=True, null=True)
    naturezajuridica = models.CharField(db_column='naturezaJuridica', max_length=150)
    observacoes = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class EmpresaContato(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
    contatolist = models.OneToOneField(Contato, models.DO_NOTHING, db_column='contatoList_id',
                                       unique=True)

    class Meta:
        managed = False
        db_table = 'empresa_contato'


class EmpresaEmailhomepage(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
    emailhomepagelist = models.OneToOneField(Emailhomepage, models.DO_NOTHING, db_column='emailHomePageList_id',
                                             unique=True)

    class Meta:
        managed = False
        db_table = 'empresa_emailHomePage'


class EmpresaEndereco(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
    enderecolist = models.OneToOneField('Endereco', models.DO_NOTHING, db_column='enderecoList_id',
                                        unique=True)

    class Meta:
        managed = False
        db_table = 'empresa_endereco'


class EmpresaInforeceitafederal(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
    inforeceitafederallist = models.OneToOneField('Inforeceitafederal', models.DO_NOTHING,
                                                  db_column='infoReceitaFederalList_id',
                                                  unique=True)

    class Meta:
        managed = False
        db_table = 'empresa_infoReceitaFederal'


class EmpresaTelefone(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
    telefonelist = models.OneToOneField('Telefone', models.DO_NOTHING, db_column='telefoneList_id',
                                        unique=True)

    class Meta:
        managed = False
        db_table = 'empresa_telefone'


class Endereco(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField(blank=True, null=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    prox = models.CharField(max_length=80)
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'endereco'


class Fiscalcestncm(models.Model):
    id = models.BigAutoField(primary_key=True)
    segmento = models.CharField(max_length=100)
    descricao = models.CharField(max_length=600)
    cest = models.CharField(max_length=7)
    ncm = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'fiscalCestNcm'


class Fiscalcstorigem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=180)

    class Meta:
        managed = False
        db_table = 'fiscalCstOrigem'


class Fiscalfretesituacaotributaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'fiscalFreteSituacaoTributaria'


class Fiscalicms(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscalIcms'


class Fiscalpiscofins(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscalPisCofins'


class Fiscaltributossefazam(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscalTributosSefazAm'


class Inforeceitafederal(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField()
    code = models.CharField(max_length=70)
    text = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'infoReceitaFederal'


class Menuprincipal(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu = models.CharField(max_length=45)
    menulabel = models.CharField(db_column='menuLabel', max_length=45)
    menupai_id = models.IntegerField(db_column='menuPai_id')
    tabpane = models.TextField(db_column='tabPane')
    icomenu = models.CharField(db_column='icoMenu', max_length=80, blank=True, null=True)
    teclaatalho = models.CharField(db_column='teclaAtalho', max_length=45, blank=True,
                                   null=True)
    dropdown = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menuPrincipal'


class Municipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    ibge_codigo = models.CharField(max_length=7)
    ddd = models.IntegerField()
    uf = models.ForeignKey('Uf', models.DO_NOTHING)
    capital = models.TextField()

    class Meta:
        managed = False
        db_table = 'municipio'


class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=15)
    descricao = models.CharField(max_length=120)
    peso = models.DecimalField(max_digits=19, decimal_places=3)
    unidadecomercial = models.IntegerField(db_column='unidadeComercial',
                                           choices=UNIDADE_COMERCIAL.choices())
    situacao = models.IntegerField(choices=SITUACAO_NO_SISTEMA.choices())
    precofabrica = models.DecimalField(db_column='precoFabrica', max_digits=19,
                                       decimal_places=2)
    precoconsumidor = models.DecimalField(db_column='precoConsumidor', max_digits=19,
                                          decimal_places=2)
    varejo = models.IntegerField()
    ultimpostosefaz = models.DecimalField(db_column='ultImpostoSefaz', max_digits=19,
                                          decimal_places=2)
    ultfrete = models.DecimalField(db_column='ultFrete', max_digits=19, decimal_places=2)
    comissao = models.DecimalField(max_digits=19, decimal_places=2)
    ncm = models.CharField(max_length=8, blank=True, null=True)
    cest = models.CharField(max_length=7, blank=True, null=True)
    fiscalcstorigem = models.ForeignKey('Fiscalcstorigem', models.DO_NOTHING, db_column='fiscalCstOrigem_id',
                                        blank=True, null=True)
    fiscalicms = models.ForeignKey('Fiscalicms', models.DO_NOTHING, db_column='fiscalIcms_id', blank=True,
                                   null=True)
    fiscalpis = models.ForeignKey('Fiscalpiscofins', models.DO_NOTHING, related_name='fiscalpis',
                                  db_column='fiscalPis_id', blank=True,
                                  null=True)
    fiscalcofins = models.ForeignKey('Fiscalpiscofins', models.DO_NOTHING, related_name='fiscalcofins',
                                     db_column='fiscalCofins_id', blank=True,
                                     null=True)
    nfegenero = models.CharField(db_column='nfeGenero', max_length=255, blank=True,
                                 null=True)
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuariocadastroproduto',
                                        db_column='usuarioCadastro_id', blank=True,
                                        null=True)
    datacadastro = models.DateTimeField(auto_now_add=True, db_column='dataCadastro')
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioatualizacaoproduto',
                                           db_column='usuarioAtualizacao_id', blank=True,
                                           null=True)
    dataatualizacao = models.DateTimeField(auto_now=True, db_column='dataAtualizacao', blank=True,
                                           null=True)
    imgproduto = models.BinaryField(db_column='imgProduto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produto'


class Produtocodigobarra(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigobarra = models.CharField(db_column='codigoBarra', unique=True, max_length=13)
    imgcogigobarra = models.BinaryField(db_column='imgCogigoBarra', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtoCodigoBarra'


class ProdutoProdutocodigobarra(models.Model):
    produto = models.OneToOneField('Produto', models.DO_NOTHING, db_column='Produto_id')
    produtocodigobarralist = models.OneToOneField('Produtocodigobarra', models.DO_NOTHING,
                                                  db_column='produtoCodigoBarraList_id',
                                                  unique=True)

    class Meta:
        managed = False
        db_table = 'produto_produtoCodigoBarra'


class Telefone(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=11)
    telefoneoperadora = models.ForeignKey('Telefoneoperadora', models.DO_NOTHING, db_column='telefoneOperadora_id',
                                          blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefone'


class Telefoneoperadora(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=30)
    tipo = models.IntegerField()
    ddd = models.IntegerField()
    codwsportabilidade = models.CharField(db_column='codWsPortabilidade', max_length=30, blank=True,
                                          null=True)

    class Meta:
        managed = False
        db_table = 'telefoneOperadora'


class Uf(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'uf'


class Usuario(models.Model):
    id = models.OneToOneField('Colaborador', models.DO_NOTHING, db_column='id', primary_key=True)
    email = models.CharField(max_length=254)
    senha = models.CharField(max_length=128)
    imagem = models.TextField(blank=True, null=True)
    userativo = models.IntegerField(db_column='userAtivo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

    def get_id00(self):
        return "{:0>2}".format(self.id.id)

    def get_usuario_apelido(self):
        return self.id.apelido

    def get_colaborador_imagem(self):
        return b64encode(self.id.imgcolaborador).decode('ascii')

    def __str__(self):
        return self.id.apelido

# from base64 import b64encode
#
# from django.db import models
#
# from cafeperfeito.enums import UNIDADE_COMERCIAL, SITUACAO_NO_SISTEMA
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class Cargo(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     descricao = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'cargo'
#
#     def __str__(self):
#         return str('\n\t\tid : {:0>2}' \
#                    '\n\t\tdescricao : {}' \
#             .format(
#             self.id,
#             self.descricao
#         ))
#
#
# class Colaborador(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nome = models.CharField(max_length=80)
#     apelido = models.CharField(max_length=30)
#     ctps = models.CharField(max_length=30)
#     dataadmisao = models.DateTimeField(db_column='dataAdmisao', blank=True, null=True)
#     salario = models.DecimalField(max_digits=19, decimal_places=2)
#     ativo = models.TextField()
#     empresa = models.ForeignKey('Empresa', models.DO_NOTHING, blank=True, null=True)
#     cargo = models.ForeignKey(Cargo, db_column='cargo_id', models.DO_NOTHING, blank=True, null=True)
#     imgcolaborador = models.BinaryField(db_column='imgColaborador', blank=True, null=True)
#
#     def get_colaborador_imagem(self):
#         return b64encode(self.imgcolaborador).decode('ascii')
#
#     class Meta:
#         managed = False
#         db_table = 'colaborador'
#
#     def __str__(self):
#         return self.nome
#
#     def getColaborador(self):
#         return {'id': self.id, 'nome': self.nome, 'apelido': self.apelido, 'ativo': self.ativo, 'cargo': self.cargo}
#
#
# class Contato(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     descricao = models.CharField(max_length=40, blank=True, null=True)
#     cargo = models.ForeignKey(Cargo, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'contato'
#
#
# class ContatoEmailhomepage(models.Model):
#     contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')
#     emailhomepagelist = models.OneToOneField('Emailhomepage', models.DO_NOTHING, db_column='emailHomePageList_id',
#                                              unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'contato_emailHomePage'
#
#
# class ContatoTelefone(models.Model):
#     contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')
#     telefonelist = models.OneToOneField('Telefone', models.DO_NOTHING, db_column='telefoneList_id',
#                                         unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'contato_telefone'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class Emailhomepage(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     descricao = models.CharField(max_length=80)
#     tipo = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'emailHomePage'
#
#
# class Empresa(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     lojasistema = models.TextField(db_column='lojaSistema') This field type is a guess.
#     classifjuridica = models.IntegerField(db_column='classifJuridica')
#     cnpj = models.CharField(max_length=14)
#     ieisento = models.TextField(db_column='ieIsento') This field type is a guess.
#     ie = models.CharField(max_length=14)
#     razao = models.CharField(max_length=80)
#     fantasia = models.CharField(max_length=80)
#     cliente = models.TextField()
#     fornecedor = models.TextField()
#     transportadora = models.TextField()
#     situacao = models.IntegerField()
#     usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuariocadastroempresa',
#                                         db_column='usuarioCadastro_id', blank=True,
#                                         null=True)
#     datacadastro = models.DateTimeField(db_column='dataCadastro', blank=True, null=True)
#     usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioatualizacaoempresa',
#                                            db_column='usuarioAtualizacao_id', blank=True,
#                                            null=True)
#     dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
#                                            null=True)
#     dataabetura = models.DateTimeField(db_column='dataAbetura', blank=True, null=True)
#     naturezajuridica = models.CharField(db_column='naturezaJuridica', max_length=150)
#     observacoes = models.CharField(max_length=1500, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'empresa'
#
#
# class EmpresaContato(models.Model):
#     empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
#     contatolist = models.OneToOneField(Contato, models.DO_NOTHING, db_column='contatoList_id',
#                                        unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'empresa_contato'
#
#
# class EmpresaEmailhomepage(models.Model):
#     empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
#     emailhomepagelist = models.OneToOneField(Emailhomepage, models.DO_NOTHING, db_column='emailHomePageList_id',
#                                              unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'empresa_emailHomePage'
#
#
# class EmpresaEndereco(models.Model):
#     empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
#     enderecolist = models.OneToOneField('Endereco', models.DO_NOTHING, db_column='enderecoList_id',
#                                         unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'empresa_endereco'
#
#
# class EmpresaInforeceitafederal(models.Model):
#     empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
#     inforeceitafederallist = models.OneToOneField('Inforeceitafederal', models.DO_NOTHING,
#                                                   db_column='infoReceitaFederalList_id',
#                                                   unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'empresa_infoReceitaFederal'
#
#
# class EmpresaTelefone(models.Model):
#     empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')
#     telefonelist = models.OneToOneField('Telefone', models.DO_NOTHING, db_column='telefoneList_id',
#                                         unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'empresa_telefone'
#
#
# class Endereco(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     tipo = models.IntegerField(blank=True, null=True)
#     cep = models.CharField(max_length=8)
#     logradouro = models.CharField(max_length=80)
#     numero = models.CharField(max_length=10)
#     complemento = models.CharField(max_length=80)
#     bairro = models.CharField(max_length=50)
#     prox = models.CharField(max_length=80)
#     municipio = models.ForeignKey('Municipio', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'endereco'
#
#
# class Fiscalcestncm(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     segmento = models.CharField(max_length=100)
#     descricao = models.CharField(max_length=600)
#     cest = models.CharField(max_length=7)
#     ncm = models.CharField(max_length=8)
#
#     class Meta:
#         managed = False
#         db_table = 'fiscalCestNcm'
#
#
# class Fiscalcstorigem(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     descricao = models.CharField(max_length=180)
#
#     def __str__(self):
#         return self.descricao
#
#     class Meta:
#         managed = False
#         db_table = 'fiscalCstOrigem'
#
#
# class Fiscalfretesituacaotributaria(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     descricao = models.CharField(max_length=60)
#
#     class Meta:
#         managed = False
#         db_table = 'fiscalFreteSituacaoTributaria'
#
#
# class Fiscalicms(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     descricao = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'fiscalIcms'
#
#
# class Fiscalpiscofins(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     descricao = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'fiscalPisCofins'
#
#
# class Fiscaltributossefazam(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     descricao = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'fiscalTributosSefazAm'
#
#
# class HibernateSequence(models.Model):
#     next_val = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hibernate_sequence'
#
#
# class Inforeceitafederal(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     tipo = models.IntegerField()
#     code = models.CharField(max_length=70)
#     text = models.CharField(max_length=500)
#
#     class Meta:
#         managed = False
#         db_table = 'infoReceitaFederal'
#
#
# class Menuprincipal(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     menu = models.CharField(max_length=45)
#     menulabel = models.CharField(db_column='menuLabel', max_length=45)
#     menupai_id = models.IntegerField(db_column='menuPai_id')
#     tabpane = models.TextField(db_column='tabPane') This field type is a guess.
#     icomenu = models.CharField(db_column='icoMenu', max_length=80, blank=True, null=True)
#     teclaatalho = models.CharField(db_column='teclaAtalho', max_length=45, blank=True,
#                                    null=True)
#
#     # def __str__(self):
#     #     return self.menu
#
#     class Meta:
#         managed = False
#         db_table = 'menuPrincipal'
#
#
# class Municipio(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     descricao = models.CharField(max_length=80)
#     ibge_codigo = models.CharField(max_length=7)
#     ddd = models.IntegerField()
#     uf = models.ForeignKey('Uf', models.DO_NOTHING)
#     capital = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'municipio'
#
#
# class Produto(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     codigo = models.CharField(unique=True, max_length=15)
#     descricao = models.CharField(max_length=120)
#     peso = models.DecimalField(max_digits=19, decimal_places=3)
#     unidadecomercial = models.IntegerField(db_column='unidadeComercial',
#                                            choices=UNIDADE_COMERCIAL.choices())
#     situacao = models.IntegerField(choices=SITUACAO_NO_SISTEMA.choices())
#     precofabrica = models.DecimalField(db_column='precoFabrica', max_digits=19,
#                                        decimal_places=2)
#     precoconsumidor = models.DecimalField(db_column='precoConsumidor', max_digits=19,
#                                           decimal_places=2)
#     varejo = models.IntegerField()
#     ultimpostosefaz = models.DecimalField(db_column='ultImpostoSefaz', max_digits=19,
#                                           decimal_places=2)
#     ultfrete = models.DecimalField(db_column='ultFrete', max_digits=19, decimal_places=2)
#     comissao = models.DecimalField(max_digits=19, decimal_places=2)
#     ncm = models.CharField(max_length=8, blank=True, null=True)
#     cest = models.CharField(max_length=7, blank=True, null=True)
#     fiscalcstorigem = models.ForeignKey(Fiscalcstorigem, models.DO_NOTHING, db_column='fiscalCstOrigem_id', blank=True,
#                                         null=True)
#     fiscalicms = models.ForeignKey(Fiscalicms, models.DO_NOTHING, db_column='fiscalIcms_id', blank=True,
#                                    null=True)
#     fiscalpis = models.ForeignKey(Fiscalpiscofins, models.DO_NOTHING, related_name='fiscalpis',
#                                   db_column='fiscalPis_id', blank=True,
#                                   null=True)
#     fiscalcofins = models.ForeignKey(Fiscalpiscofins, models.DO_NOTHING, related_name='fiscalcofins',
#                                      db_column='fiscalCofins_id', blank=True,
#                                      null=True)
#     nfegenero = models.CharField(db_column='nfeGenero', max_length=255, blank=True,
#                                  null=True)
#     usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuariocadastroproduto',
#                                         db_column='usuarioCadastro_id', blank=True,
#                                         null=True)
#     datacadastro = models.DateTimeField(db_column='dataCadastro', auto_now_add=True)
#     usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioatualizacaoproduto',
#                                            db_column='usuarioAtualizacao_id', blank=True,
#                                            null=True)
#     dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
#                                            null=True, auto_now=True)
#     imgproduto = models.BinaryField(db_column='imgProduto', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto'
#
#
# class Produtocodigobarra(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     codigobarra = models.CharField(db_column='codigoBarra', unique=True, max_length=13)
#     imgcogigobarra = models.TextField(db_column='imgCogigoBarra', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produtoCodigoBarra'
#
#
# class ProdutoProdutocodigobarra(models.Model):
#     produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='Produto_id')
#     produtocodigobarralist = models.OneToOneField(Produtocodigobarra, models.DO_NOTHING,
#                                                   db_column='produtoCodigoBarraList_id',
#                                                   unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto_produtoCodigoBarra'
#
#
# class Telefone(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     descricao = models.CharField(max_length=11)
#     telefoneoperadora = models.ForeignKey('Telefoneoperadora', models.DO_NOTHING, db_column='telefoneOperadora_id',
#                                           blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'telefone'
#
#
# class Telefoneoperadora(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     descricao = models.CharField(max_length=30)
#     tipo = models.IntegerField()
#     ddd = models.IntegerField()
#     codwsportabilidade = models.CharField(db_column='codWsPortabilidade', max_length=30, blank=True,
#                                           null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'telefoneOperadora'
#
#
# class Uf(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     descricao = models.CharField(max_length=50)
#     sigla = models.CharField(max_length=2)
#
#     class Meta:
#         managed = False
#         db_table = 'uf'
#
#
# class Usuario(models.Model):
#     id = models.OneToOneField('Colaborador', models.DO_NOTHING, db_column='id', primary_key=True)
#     email = models.CharField(max_length=120, blank=False, null=False)
#     senha = models.CharField(max_length=60, blank=False, null=False)
#     imagem = models.BinaryField(blank=True, null=True)
#     userativo = models.IntegerField(db_column='userAtivo', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'usuario'
#
#     def get_id00(self):
#         return "{:0>2}".format(self.id.id)
#
#     def get_usuario_apelido(self):
#         return self.id.apelido
#
#     def get_colaborador_imagem(self):
#         return b64encode(self.id.imgcolaborador).decode('ascii')
#
#     def __str__(self):
#         return self.id.apelido
#
