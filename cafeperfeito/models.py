# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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

    def __str__(self):
        return str('\n\t\tid : {:0>2}' \
                   '\n\t\tdescricao : {}' \
            .format(
            self.id,
            self.descricao
        ))


class Colaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    apelido = models.CharField(max_length=30)
    ctps = models.CharField(max_length=30)
    dataadmisao = models.DateTimeField(db_column='dataAdmisao', blank=True, null=True)  # Field name made lowercase.
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    ativo = models.TextField()  # This field type is a guess.
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colaborador'

    def __str__(self):
        return self.nome

    def getColaborador(self):
        return {'id': self.id, 'nome': self.nome, 'apelido': self.apelido, 'ativo': self.ativo, 'cargo': self.cargo}
        # return str('\n\tid : {:0>2}' \
        #        '\n\tnome : {}' \
        #        '\n\tapelido : {}' \
        #        '\n\tativo : {}' \
        #        '\n\tcargo : {}' \
        #        '\n' \
        #     .format(
        #     self.id,
        #     self.nome,
        #     self.apelido,
        #     SituacaoNoSistema(self.ativo).name,
        #     self.cargo
        # ))


class Contato(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=40, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contato'


class ContatoEmailhomepage(models.Model):
    contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')  # Field name made lowercase.
    emailhomepagelist = models.OneToOneField('Emailhomepage', models.DO_NOTHING, db_column='emailHomePageList_id',
                                             unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contato_emailHomePage'


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')  # Field name made lowercase.
    telefonelist = models.OneToOneField('Telefone', models.DO_NOTHING, db_column='telefoneList_id',
                                        unique=True)  # Field name made lowercase.

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
    lojasistema = models.TextField(db_column='lojaSistema')  # Field name made lowercase. This field type is a guess.
    classifjuridica = models.IntegerField(db_column='classifJuridica')  # Field name made lowercase.
    cnpj = models.CharField(max_length=14)
    ieisento = models.TextField(db_column='ieIsento')  # Field name made lowercase. This field type is a guess.
    ie = models.CharField(max_length=14)
    razao = models.CharField(max_length=80)
    fantasia = models.CharField(max_length=80)
    cliente = models.TextField()  # This field type is a guess.
    fornecedor = models.TextField()  # This field type is a guess.
    transportadora = models.TextField()  # This field type is a guess.
    situacao = models.IntegerField()
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuariocadastroempresa',
                                        db_column='usuarioCadastro_id', blank=True,
                                        null=True)  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='dataCadastro', blank=True, null=True)  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioatualizacaoempresa',
                                           db_column='usuarioAtualizacao_id', blank=True,
                                           null=True)
    dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
                                           null=True)  # Field name made lowercase.
    dataabetura = models.DateTimeField(db_column='dataAbetura', blank=True, null=True)  # Field name made lowercase.
    naturezajuridica = models.CharField(db_column='naturezaJuridica', max_length=150)  # Field name made lowercase.
    observacoes = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class EmpresaContato(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    contatolist = models.OneToOneField(Contato, models.DO_NOTHING, db_column='contatoList_id',
                                       unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_contato'


class EmpresaEmailhomepage(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    emailhomepagelist = models.OneToOneField(Emailhomepage, models.DO_NOTHING, db_column='emailHomePageList_id',
                                             unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_emailHomePage'


class EmpresaEndereco(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    enderecolist = models.OneToOneField('Endereco', models.DO_NOTHING, db_column='enderecoList_id',
                                        unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_endereco'


class EmpresaInforeceitafederal(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    inforeceitafederallist = models.OneToOneField('Inforeceitafederal', models.DO_NOTHING,
                                                  db_column='infoReceitaFederalList_id',
                                                  unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_infoReceitaFederal'


class EmpresaTelefone(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    telefonelist = models.OneToOneField('Telefone', models.DO_NOTHING, db_column='telefoneList_id',
                                        unique=True)  # Field name made lowercase.

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


class HibernateSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hibernate_sequence'


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
    menulabel = models.CharField(db_column='menuLabel', max_length=45)  # Field name made lowercase.
    menupai_id = models.IntegerField(db_column='menuPai_id')  # Field name made lowercase.
    tabpane = models.TextField(db_column='tabPane')  # Field name made lowercase. This field type is a guess.
    icomenu = models.CharField(db_column='icoMenu', max_length=80, blank=True, null=True)  # Field name made lowercase.
    teclaatalho = models.CharField(db_column='teclaAtalho', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menuPrincipal'


class Municipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    ibge_codigo = models.CharField(max_length=7)
    ddd = models.IntegerField()
    uf = models.ForeignKey('Uf', models.DO_NOTHING)
    capital = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'municipio'


class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=15)
    descricao = models.CharField(max_length=120)
    peso = models.DecimalField(max_digits=19, decimal_places=3)
    unidadecomercial = models.IntegerField(db_column='unidadeComercial')  # Field name made lowercase.
    situacao = models.IntegerField()
    precofabrica = models.DecimalField(db_column='precoFabrica', max_digits=19,
                                       decimal_places=2)  # Field name made lowercase.
    precoconsumidor = models.DecimalField(db_column='precoConsumidor', max_digits=19,
                                          decimal_places=2)  # Field name made lowercase.
    varejo = models.IntegerField()
    ultimpostosefaz = models.DecimalField(db_column='ultImpostoSefaz', max_digits=19,
                                          decimal_places=2)  # Field name made lowercase.
    ultfrete = models.DecimalField(db_column='ultFrete', max_digits=19, decimal_places=2)  # Field name made lowercase.
    comissao = models.DecimalField(max_digits=19, decimal_places=2)
    ncm = models.CharField(max_length=8, blank=True, null=True)
    cest = models.CharField(max_length=7, blank=True, null=True)
    fiscalcstorigem = models.ForeignKey(Fiscalcstorigem, models.DO_NOTHING, db_column='fiscalCstOrigem_id', blank=True,
                                        null=True)  # Field name made lowercase.
    fiscalicms = models.ForeignKey(Fiscalicms, models.DO_NOTHING, db_column='fiscalIcms_id', blank=True,
                                   null=True)  # Field name made lowercase.
    fiscalpis = models.ForeignKey(Fiscalpiscofins, models.DO_NOTHING, related_name='fiscalpis',
                                  db_column='fiscalPis_id', blank=True,
                                  null=True)  # Field name made lowercase.
    fiscalcofins = models.ForeignKey(Fiscalpiscofins, models.DO_NOTHING, related_name='fiscalcofins',
                                     db_column='fiscalCofins_id', blank=True,
                                     null=True)  # Field name made lowercase.
    nfegenero = models.CharField(db_column='nfeGenero', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuariocadastroproduto',
                                        db_column='usuarioCadastro_id', blank=True,
                                        null=True)  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='dataCadastro')  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioatualizacaoproduto',
                                           db_column='usuarioAtualizacao_id', blank=True,
                                           null=True)  # Field name made lowercase.
    dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
                                           null=True)  # Field name made lowercase.
    imgproduto = models.TextField(db_column='imgProduto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produto'


class Produtocodigobarra(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigobarra = models.CharField(db_column='codigoBarra', unique=True, max_length=13)  # Field name made lowercase.
    imgcogigobarra = models.TextField(db_column='imgCogigoBarra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtoCodigoBarra'


class ProdutoProdutocodigobarra(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='Produto_id')  # Field name made lowercase.
    produtocodigobarralist = models.OneToOneField(Produtocodigobarra, models.DO_NOTHING,
                                                  db_column='produtoCodigoBarraList_id',
                                                  unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produto_produtoCodigoBarra'


class Telefone(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=11)
    telefoneoperadora = models.ForeignKey('Telefoneoperadora', models.DO_NOTHING, db_column='telefoneOperadora_id',
                                          blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telefone'


class Telefoneoperadora(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=30)
    tipo = models.IntegerField()
    ddd = models.IntegerField()
    codwsportabilidade = models.CharField(db_column='codWsPortabilidade', max_length=30, blank=True,
                                          null=True)  # Field name made lowercase.

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
    id = models.OneToOneField(Colaborador, models.DO_NOTHING, db_column='id', primary_key=True)
    email = models.CharField(max_length=120)
    senha = models.CharField(max_length=60)
    imagem = models.TextField(blank=True, null=True)
    userativo = models.IntegerField(db_column='userAtivo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'

    def get_Usuario_Senha(self, mailusuario):
        return Usuario.objects.values_list('email', 'senha').get(email=mailusuario)

    def get_usuario_apelido(self):
        return self.id.apelido

    def __str__(self):
        return self.id.apelido
