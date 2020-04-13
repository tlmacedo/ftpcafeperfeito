# Tracking file by folder pattern:  migrations
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from base64 import b64encode, b64decode

from django.db import models

from cafeperfeito.enums import UNIDADE_COMERCIAL, SITUACAO_NO_SISTEMA


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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


class Bancos(models.Model):
    id = models.BigAutoField(primary_key=True)
    banco = models.CharField(max_length=80)
    codigo = models.CharField(unique=True, max_length=3)
    site = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bancos'


class Cargo(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'cargo'


class Colaborador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=120)
    apelido = models.CharField(unique=True, max_length=30)
    ctps = models.CharField(unique=True, max_length=30)
    dtadmisao = models.DateTimeField(db_column='dtAdmisao')  # Field name made lowercase.
    salario = models.DecimalField(max_digits=19, decimal_places=4)
    situacao = models.IntegerField(blank=True, null=True)
    imagem = models.BinaryField(blank=True, null=True)
    lojaativo = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='lojaAtivo_id', blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'colaborador'

    def get_colaborador_imagem(self):
        return b64encode(b64decode(self.imagem)).decode()

    def __str__(self):
        return self.nome

    def getApelido(self):
        return self.apelido

    def getColaborador(self):
        return {'id': self.id, 'nome': self.nome, 'apelido': self.apelido, 'situacao': self.situacao,
                'imagem': self.imagem}


class ContasAReceber(models.Model):
    id = models.BigAutoField(primary_key=True)
    saidaproduto = models.ForeignKey('SaidaProduto', models.DO_NOTHING, db_column='saidaProduto_id', blank=True,
                                     null=True)  # Field name made lowercase.
    dtvencimento = models.DateField(db_column='dtVencimento')  # Field name made lowercase.
    valor = models.DecimalField(max_digits=19, decimal_places=4)
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCadastro_id', blank=True,
                                        null=True)  # Field name made lowercase.
    dtcadastro = models.DateTimeField(db_column='dtCadastro')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contas_a_receber'


class Contato(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=40)
    cargo = models.ForeignKey(Cargo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contato'


class ContatoEmailHomePage(models.Model):
    contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')  # Field name made lowercase.
    emailhomepagelist = models.OneToOneField('EmailHomePage', models.DO_NOTHING,
                                             db_column='emailHomePageList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contato_email_home_page'


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato, models.DO_NOTHING, db_column='Contato_id')  # Field name made lowercase.
    telefonelist = models.OneToOneField('Telefone', models.DO_NOTHING,
                                        db_column='telefoneList_id')  # Field name made lowercase.

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


class EmailHomePage(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=150)
    tipoemailhomepage = models.IntegerField(db_column='tipoEmailHomePage', blank=True,
                                            null=True)  # Field name made lowercase.
    principal = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'email_home_page'


class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    loja = models.TextField()  # This field type is a guess.
    pessoajuridica = models.TextField(
        db_column='pessoaJuridica')  # Field name made lowercase. This field type is a guess.
    situacao = models.IntegerField()
    cnpj = models.CharField(max_length=14)
    ie = models.CharField(max_length=14, blank=True, null=True)
    razao = models.CharField(max_length=80)
    fantasia = models.CharField(max_length=80)
    cliente = models.TextField()  # This field type is a guess.
    fornecedor = models.TextField()  # This field type is a guess.
    transportadora = models.TextField()  # This field type is a guess.
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCadastro_id',
                                        blank=True, null=True,
                                        related_name='usuariocadastroempresa')  # Field name made lowercase.
    dtcadastro = models.DateTimeField(db_column='dtCadastro')  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioAtualizacao_id',
                                           blank=True, null=True,
                                           related_name='usuarioatualizacaoempresa')  # Field name made lowercase.
    dtatualizacao = models.DateTimeField(db_column='dtAtualizacao', blank=True, null=True)  # Field name made lowercase.
    observacoes = models.CharField(max_length=1500, blank=True, null=True)
    limite = models.DecimalField(max_digits=19, decimal_places=4)
    prazo = models.IntegerField()
    prazodiautil = models.TextField(db_column='prazoDiaUtil')  # Field name made lowercase. This field type is a guess.
    imunicpipal = models.CharField(db_column='iMunicpipal', max_length=15, blank=True,
                                   null=True)  # Field name made lowercase.
    isuframa = models.CharField(db_column='iSuframa', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class EmpresaCondicoes(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    produto = models.ForeignKey('Produto', models.DO_NOTHING, blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=4)
    qtdminima = models.IntegerField(db_column='qtdMinima')  # Field name made lowercase.
    prazo = models.IntegerField()
    bonificacao = models.IntegerField()
    retirada = models.IntegerField()
    desconto = models.DecimalField(max_digits=19, decimal_places=4)
    validade = models.DateField()

    class Meta:
        managed = False
        db_table = 'empresa_condicoes'


class EmpresaContato(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    contatolist = models.OneToOneField(Contato, models.DO_NOTHING,
                                       db_column='contatoList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_contato'


class EmpresaEmailHomePage(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    emailhomepagelist = models.OneToOneField(EmailHomePage, models.DO_NOTHING,
                                             db_column='emailHomePageList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_email_home_page'


class EmpresaEmpresaProdutoValor(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    empresaprodutovalorlist = models.OneToOneField('EmpresaProdutoValor', models.DO_NOTHING,
                                                   db_column='empresaProdutoValorList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_empresa_produto_valor'


class EmpresaEndereco(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    enderecolist = models.OneToOneField('Endereco', models.DO_NOTHING,
                                        db_column='enderecoList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_endereco'


class EmpresaInfoReceitaFederal(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    inforeceitafederallist = models.OneToOneField('InfoReceitaFederal', models.DO_NOTHING,
                                                  db_column='infoReceitaFederalList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_info_receita_federal'


class EmpresaInformacaoBancaria(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    informacaobancarialist = models.OneToOneField('InformacaoBancaria', models.DO_NOTHING,
                                                  db_column='informacaoBancariaList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_informacao_bancaria'


class EmpresaProdutoValor(models.Model):
    id = models.BigAutoField(primary_key=True)
    bonificacao = models.IntegerField()
    desconto = models.DecimalField(max_digits=19, decimal_places=2)
    dias = models.IntegerField()
    qtdminima = models.IntegerField(db_column='qtdMinima')  # Field name made lowercase.
    validadedesconto = models.DateField(db_column='validadeDesconto')  # Field name made lowercase.
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    produto = models.ForeignKey('Produto', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa_produto_valor'


class EmpresaTelefone(models.Model):
    empresa_id = models.IntegerField(blank=True, null=True)
    telefonelist_id = models.IntegerField(db_column='telefoneList_id', unique=True, blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_telefone'


class Endereco(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField()
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=120)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=80, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    pontoreferencia = models.CharField(db_column='pontoReferencia', max_length=80, blank=True,
                                       null=True)  # Field name made lowercase.
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco'


class Energia(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.DateTimeField()
    leitura = models.IntegerField(unique=True)
    fechamento = models.IntegerField(blank=True, null=True)
    kwh = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energia'


class EntradaCte(models.Model):
    id = models.BigAutoField(primary_key=True)
    entradaproduto = models.ForeignKey('EntradaProduto', models.DO_NOTHING, db_column='entradaProduto_id', blank=True,
                                       null=True)  # Field name made lowercase.
    chave = models.CharField(unique=True, max_length=44)
    tomadorservico = models.IntegerField(db_column='tomadorServico', blank=True,
                                         null=True)  # Field name made lowercase.
    numero = models.CharField(max_length=9)
    serie = models.CharField(max_length=3)
    modelo = models.IntegerField(blank=True, null=True)
    dtemissao = models.DateField(db_column='dtEmissao', blank=True, null=True)  # Field name made lowercase.
    transportadora = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    situacaotributaria = models.ForeignKey('FiscalFreteSituacaoTributaria', models.DO_NOTHING,
                                           db_column='situacaoTributaria_id', blank=True,
                                           null=True)  # Field name made lowercase.
    vlrcte = models.DecimalField(db_column='vlrCte', max_digits=19, decimal_places=4)  # Field name made lowercase.
    qtdvolume = models.IntegerField(db_column='qtdVolume')  # Field name made lowercase.
    pesobruto = models.DecimalField(db_column='pesoBruto', max_digits=19,
                                    decimal_places=4)  # Field name made lowercase.
    vlrfretebruto = models.DecimalField(db_column='vlrFreteBruto', max_digits=19,
                                        decimal_places=4)  # Field name made lowercase.
    vlrtaxas = models.DecimalField(db_column='vlrTaxas', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlrcoleta = models.DecimalField(db_column='vlrColeta', max_digits=19,
                                    decimal_places=4)  # Field name made lowercase.
    vlrimpostofrete = models.DecimalField(db_column='vlrImpostoFrete', max_digits=19,
                                          decimal_places=4)  # Field name made lowercase.
    entradafiscal = models.ForeignKey('EntradaFiscal', models.DO_NOTHING, db_column='entradaFiscal_id', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entrada_cte'


class EntradaFiscal(models.Model):
    id = models.BigAutoField(primary_key=True)
    controle = models.CharField(max_length=13)
    origem = models.CharField(max_length=12)
    tributossefazam = models.ForeignKey('FiscalTributosSefazAm', models.DO_NOTHING, db_column='tributosSefazAm_id',
                                        blank=True, null=True)  # Field name made lowercase.
    vlrdocumento = models.DecimalField(db_column='vlrDocumento', max_digits=19,
                                       decimal_places=4)  # Field name made lowercase.
    vlrtributo = models.DecimalField(db_column='vlrTributo', max_digits=19,
                                     decimal_places=4)  # Field name made lowercase.
    vlrmulta = models.DecimalField(db_column='vlrMulta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlrjuros = models.DecimalField(db_column='vlrJuros', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlrtaxa = models.DecimalField(db_column='vlrTaxa', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entrada_fiscal'


class EntradaNfe(models.Model):
    id = models.BigAutoField(primary_key=True)
    entradaproduto = models.ForeignKey('EntradaProduto', models.DO_NOTHING, db_column='entradaProduto_id', blank=True,
                                       null=True)  # Field name made lowercase.
    chave = models.CharField(unique=True, max_length=44)
    numero = models.CharField(max_length=9)
    serie = models.CharField(max_length=3)
    modelo = models.IntegerField(blank=True, null=True)
    fornecedor = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    dtemissao = models.DateField(db_column='dtEmissao', blank=True, null=True)  # Field name made lowercase.
    dtentrada = models.DateField(db_column='dtEntrada', blank=True, null=True)  # Field name made lowercase.
    entradafiscal = models.ForeignKey(EntradaFiscal, models.DO_NOTHING, db_column='entradaFiscal_id', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entrada_nfe'


class EntradaProduto(models.Model):
    id = models.BigAutoField(primary_key=True)
    situacao = models.IntegerField(blank=True, null=True)
    loja = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCadastro_id', blank=True,
                                        null=True)  # Field name made lowercase.
    dtcadastro = models.DateTimeField(db_column='dtCadastro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entrada_produto'


class EntradaProdutoProduto(models.Model):
    id = models.BigAutoField(primary_key=True)
    entradaproduto = models.ForeignKey(EntradaProduto, models.DO_NOTHING, db_column='entradaProduto_id', blank=True,
                                       null=True)  # Field name made lowercase.
    produto = models.ForeignKey('Produto', models.DO_NOTHING, blank=True, null=True)
    codigo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=120)
    codigocfop = models.IntegerField(db_column='codigoCFOP', blank=True, null=True)  # Field name made lowercase.
    lote = models.CharField(max_length=15)
    dtvalidade = models.DateField(db_column='dtValidade', blank=True, null=True)  # Field name made lowercase.
    qtd = models.IntegerField()
    vlrunitario = models.DecimalField(db_column='vlrUnitario', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.
    vlrbruto = models.DecimalField(db_column='vlrBruto', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlrdesconto = models.DecimalField(db_column='vlrDesconto', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.
    vlrfrete = models.DecimalField(db_column='vlrFrete', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlrimposto = models.DecimalField(db_column='vlrImposto', max_digits=19,
                                     decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entrada_produto_produto'


class FichaKardex(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey('Produto', models.DO_NOTHING, blank=True, null=True)
    dtmovimento = models.DateTimeField(db_column='dtMovimento', blank=True, null=True)  # Field name made lowercase.
    documento = models.CharField(max_length=44)
    detalhe = models.CharField(max_length=20)
    qtd = models.IntegerField()
    vlrunitario = models.DecimalField(db_column='vlrUnitario', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.
    qtdentrada = models.IntegerField(db_column='qtdEntrada')  # Field name made lowercase.
    vlrentrada = models.DecimalField(db_column='vlrEntrada', max_digits=19,
                                     decimal_places=4)  # Field name made lowercase.
    qtdsaida = models.IntegerField(db_column='qtdSaida')  # Field name made lowercase.
    vlrsaida = models.DecimalField(db_column='vlrSaida', max_digits=19, decimal_places=4)  # Field name made lowercase.
    saldo = models.IntegerField()
    vlrsaldo = models.DecimalField(db_column='vlrSaldo', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ficha_kardex'


class FiscalCestNcm(models.Model):
    id = models.BigAutoField(primary_key=True)
    segmento = models.CharField(max_length=100)
    descricao = models.CharField(max_length=600)
    cest = models.CharField(max_length=7)
    ncm = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'fiscal_cest_ncm'


class FiscalCstOrigem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=180)

    class Meta:
        managed = False
        db_table = 'fiscal_cst_origem'


class FiscalFreteSituacaoTributaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'fiscal_frete_situacao_tributaria'


class FiscalIcms(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscal_icms'


class FiscalPisCofins(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscal_pis_cofins'


class FiscalTributosSefazAm(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'fiscal_tributos_sefaz_am'


class InfoReceitaFederal(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=70)
    text = models.CharField(max_length=500)
    tipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'info_receita_federal'


class InformacaoBancaria(models.Model):
    id = models.BigAutoField(primary_key=True)
    agencia = models.CharField(max_length=4)
    agenciadv = models.CharField(db_column='agenciaDV', max_length=2, blank=True,
                                 null=True)  # Field name made lowercase.
    conta = models.CharField(max_length=13)
    contadv = models.CharField(db_column='contaDV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoconta = models.IntegerField(db_column='tipoConta')  # Field name made lowercase.
    titularcnpjcpf = models.CharField(db_column='titularCnpjCpf', max_length=14)  # Field name made lowercase.
    titularnome = models.CharField(db_column='titularNome', max_length=80)  # Field name made lowercase.
    bancos = models.ForeignKey(Bancos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informacao_bancaria'


class MenuPrincipal(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu = models.CharField(max_length=45)
    menulabel = models.CharField(db_column='menuLabel', max_length=45)  # Field name made lowercase.
    menupai_id = models.IntegerField(db_column='menuPai_id')  # Field name made lowercase.
    icomenu = models.CharField(db_column='icoMenu', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tabpane = models.TextField(db_column='tabPane')  # Field name made lowercase. This field type is a guess.
    teclaatalho = models.CharField(db_column='teclaAtalho', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu_principal'


class Municipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    capital = models.TextField()  # This field type is a guess.
    ibge_codigo = models.CharField(max_length=7)
    ddd = models.IntegerField()
    uf = models.ForeignKey('Uf', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'municipio'


class OrcamentoEntrada(models.Model):
    id = models.BigAutoField(primary_key=True)
    orcamento = models.TextField()

    class Meta:
        managed = False
        db_table = 'orcamento_entrada'


class OrcamentoSaida(models.Model):
    id = models.BigAutoField(primary_key=True)
    orcamento = models.TextField()

    class Meta:
        managed = False
        db_table = 'orcamento_saida'


class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=15)
    descricao = models.CharField(max_length=120)
    peso = models.DecimalField(max_digits=19, decimal_places=3)
    unidadecomercial = models.IntegerField(db_column='unidadeComercial', choices=UNIDADE_COMERCIAL.choices(),
                                           verbose_name=u'Und Comercial')  # Field name made lowercase.
    situacao = models.IntegerField(choices=SITUACAO_NO_SISTEMA.choices(), verbose_name=u'Situação')
    precocompra = models.DecimalField(db_column='precoCompra', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.
    precovenda = models.DecimalField(db_column='precoVenda', max_digits=19,
                                     decimal_places=4)  # Field name made lowercase.
    varejo = models.IntegerField()
    ultimpostosefaz = models.DecimalField(db_column='ultImpostoSefaz', max_digits=19,
                                          decimal_places=4)  # Field name made lowercase.
    ultfrete = models.DecimalField(db_column='ultFrete', max_digits=19, decimal_places=4)  # Field name made lowercase.
    comissao = models.DecimalField(max_digits=19, decimal_places=4)
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCadastro_id',
                                        blank=True, null=True,
                                        related_name='usuariocadastroproduto')  # Field name made lowercase.
    dtcadastro = models.DateTimeField(db_column='dtCadastro')  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioAtualizacao_id',
                                           blank=True, null=True,
                                           related_name='usuarioatualizacaoproduto')  # Field name made lowercase.
    dtatualizacao = models.DateTimeField(db_column='dtAtualizacao', blank=True, null=True)  # Field name made lowercase.
    nfegenero = models.CharField(db_column='nfeGenero', max_length=2)  # Field name made lowercase.
    ncm = models.CharField(max_length=8, blank=True, null=True)
    cest = models.CharField(max_length=7, blank=True, null=True)
    fiscalcstorigem = models.ForeignKey(FiscalCstOrigem, models.DO_NOTHING, db_column='fiscalCstOrigem_id', blank=True,
                                        null=True)  # Field name made lowercase.
    fiscalicms = models.ForeignKey(FiscalIcms, models.DO_NOTHING, db_column='fiscalIcms_id', blank=True,
                                   null=True)  # Field name made lowercase.
    fiscalpis = models.ForeignKey(FiscalPisCofins, models.DO_NOTHING, db_column='fiscalPis_id',
                                  blank=True, null=True, related_name='fiscalpisproduto')  # Field name made lowercase.
    fiscalcofins = models.ForeignKey(FiscalPisCofins, models.DO_NOTHING, db_column='fiscalCofins_id',
                                     blank=True, null=True,
                                     related_name='fiscalcofinsproduto')  # Field name made lowercase.
    imgproduto = models.TextField(db_column='imgProduto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produto'


class ProdutoCodigoBarra(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigobarra = models.CharField(db_column='codigoBarra', unique=True, max_length=18)  # Field name made lowercase.
    imgcodigobarra = models.TextField(db_column='imgCodigoBarra', blank=True, null=True)  # Field name made lowercase.
    produto = models.ForeignKey(Produto, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produto_codigo_barra'


class ProdutoEstoque(models.Model):
    id = models.BigAutoField(primary_key=True)
    produto = models.ForeignKey(Produto, models.DO_NOTHING, blank=True, null=True)
    qtd = models.IntegerField()
    lote = models.CharField(max_length=15)
    dtvalidade = models.DateField(db_column='dtValidade', blank=True, null=True)  # Field name made lowercase.
    vlrunitario = models.DecimalField(db_column='vlrUnitario', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.
    vlrdesconto = models.DecimalField(db_column='vlrDesconto', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.
    vlrfrete = models.DecimalField(db_column='vlrFrete', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlrimposto = models.DecimalField(db_column='vlrImposto', max_digits=19,
                                     decimal_places=4)  # Field name made lowercase.
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCadastro_id', blank=True,
                                        null=True)  # Field name made lowercase.
    dtcadastro = models.DateTimeField(db_column='dtCadastro')  # Field name made lowercase.
    docentrada = models.CharField(db_column='docEntrada', max_length=15)  # Field name made lowercase.
    docentradachavenfe = models.CharField(db_column='docEntradaChaveNFe', max_length=44)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produto_estoque'


class ProdutoProdutoCodigoBarra(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='Produto_id')  # Field name made lowercase.
    produtocodigobarralist = models.OneToOneField(ProdutoCodigoBarra, models.DO_NOTHING,
                                                  db_column='produtoCodigoBarraList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produto_produto_codigo_barra'


class ProdutoProdutoEstoque(models.Model):
    produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='Produto_id')  # Field name made lowercase.
    produtoestoquelist = models.OneToOneField(ProdutoEstoque, models.DO_NOTHING,
                                              db_column='produtoEstoqueList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produto_produto_estoque'


class Recebimento(models.Model):
    id = models.BigAutoField(primary_key=True)
    contasareceber = models.ForeignKey(ContasAReceber, models.DO_NOTHING, db_column='contasAReceber_id', blank=True,
                                       null=True)  # Field name made lowercase.
    pagamentosituacao = models.IntegerField(db_column='pagamentoSituacao', blank=True,
                                            null=True)  # Field name made lowercase.
    documento = models.CharField(max_length=18)
    pagamentomodalidade = models.IntegerField(db_column='pagamentoModalidade', blank=True,
                                              null=True)  # Field name made lowercase.
    valor = models.DecimalField(max_digits=19, decimal_places=4)
    usuariopagamento = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioPagamento_id',
                                         blank=True, null=True,
                                         related_name='usuariopagamentorecebimento')  # Field name made lowercase.
    dtpagamento = models.DateField(db_column='dtPagamento', blank=True, null=True)  # Field name made lowercase.
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCadastro_id',
                                        blank=True, null=True,
                                        related_name='usuariocadastrorecebimento')  # Field name made lowercase.
    dtcadastro = models.DateTimeField(db_column='dtCadastro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recebimento'


class SaidaProduto(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Empresa, models.DO_NOTHING)
    vendedor = models.ForeignKey('Usuario', models.DO_NOTHING)
    dtcadastro = models.DateTimeField(db_column='dtCadastro', blank=True, null=True)  # Field name made lowercase.
    dtsaida = models.DateField(db_column='dtSaida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saida_produto'


class SaidaProdutoNfe(models.Model):
    id = models.BigAutoField(primary_key=True)
    cancelada = models.TextField()  # This field type is a guess.
    saidaproduto = models.ForeignKey(SaidaProduto, models.DO_NOTHING, db_column='saidaProduto_id', blank=True,
                                     null=True)  # Field name made lowercase.
    chave = models.CharField(unique=True, max_length=47)
    statussefaz = models.IntegerField(db_column='statusSefaz', blank=True, null=True)  # Field name made lowercase.
    naturezaoperacao = models.IntegerField(db_column='naturezaOperacao', blank=True,
                                           null=True)  # Field name made lowercase.
    modelo = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField()
    numero = models.IntegerField()
    dthoraemissao = models.DateTimeField(db_column='dtHoraEmissao')  # Field name made lowercase.
    dthorasaida = models.DateTimeField(db_column='dtHoraSaida')  # Field name made lowercase.
    destinooperacao = models.IntegerField(db_column='destinoOperacao', blank=True,
                                          null=True)  # Field name made lowercase.
    impressaotpimp = models.IntegerField(db_column='impressaoTpImp', blank=True,
                                         null=True)  # Field name made lowercase.
    impressaotpemis = models.IntegerField(db_column='impressaoTpEmis', blank=True,
                                          null=True)  # Field name made lowercase.
    impressaofinnfe = models.IntegerField(db_column='impressaoFinNFe', blank=True,
                                          null=True)  # Field name made lowercase.
    consumidorfinal = models.IntegerField(db_column='consumidorFinal', blank=True,
                                          null=True)  # Field name made lowercase.
    indicadorpresenca = models.IntegerField(db_column='indicadorPresenca', blank=True,
                                            null=True)  # Field name made lowercase.
    modfrete = models.IntegerField(db_column='modFrete', blank=True, null=True)  # Field name made lowercase.
    transportador = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)
    cobrancanumero = models.CharField(db_column='cobrancaNumero', max_length=10)  # Field name made lowercase.
    pagamentoindicador = models.IntegerField(db_column='pagamentoIndicador', blank=True,
                                             null=True)  # Field name made lowercase.
    pagamentomeio = models.IntegerField(db_column='pagamentoMeio', blank=True, null=True)  # Field name made lowercase.
    informacaoadicional = models.CharField(db_column='informacaoAdicional',
                                           max_length=5000)  # Field name made lowercase.
    digval = models.CharField(db_column='digVal', unique=True, max_length=28, blank=True,
                              null=True)  # Field name made lowercase.
    xmlassinatura = models.TextField(db_column='xmlAssinatura', blank=True, null=True)  # Field name made lowercase.
    xmlprotnfe = models.TextField(db_column='xmlProtNfe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saida_produto_nfe'


class SaidaProdutoProduto(models.Model):
    id = models.BigAutoField(primary_key=True)
    saidaproduto = models.ForeignKey(SaidaProduto, models.DO_NOTHING, db_column='saidaProduto_id', blank=True,
                                     null=True)  # Field name made lowercase.
    produto = models.ForeignKey(Produto, models.DO_NOTHING, blank=True, null=True)
    codigo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=120)
    codigocfop = models.IntegerField(db_column='codigoCFOP', blank=True, null=True)  # Field name made lowercase.
    lote = models.CharField(max_length=15, blank=True, null=True)
    dtvalidade = models.DateField(db_column='dtValidade', blank=True, null=True)  # Field name made lowercase.
    qtd = models.IntegerField()
    vlrentrada = models.DecimalField(db_column='vlrEntrada', max_digits=19,
                                     decimal_places=4)  # Field name made lowercase.
    vlrentradabruto = models.DecimalField(db_column='vlrEntradaBruto', max_digits=19,
                                          decimal_places=4)  # Field name made lowercase.
    vlrunitario = models.DecimalField(db_column='vlrUnitario', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.
    vlrbruto = models.DecimalField(db_column='vlrBruto', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vlrdesconto = models.DecimalField(db_column='vlrDesconto', max_digits=19,
                                      decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saida_produto_produto'


class Telefone(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=11)
    telefoneoperadora = models.ForeignKey('TelefoneOperadora', models.DO_NOTHING, db_column='telefoneOperadora_id',
                                          blank=True, null=True)  # Field name made lowercase.
    principal = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'telefone'


class TelefoneOperadora(models.Model):
    id = models.BigAutoField(primary_key=True)
    codwsportabilidade = models.CharField(db_column='codWSPortabilidade', max_length=5, blank=True,
                                          null=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'telefone_operadora'


class Uf(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'uf'


class Usuario(models.Model):
    id = models.OneToOneField(Colaborador, models.DO_NOTHING, db_column='id', primary_key=True)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=128)
    accessguest = models.IntegerField(db_column='accessGuest')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
