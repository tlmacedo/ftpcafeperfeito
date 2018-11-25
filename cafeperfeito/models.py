# -*- coding: utf-8 -*-

# import OpenSSL

from django.db import models


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
    ativo = models.IntegerField()
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


class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField()
    cnpjcpf = models.CharField(db_column='cnpjCpf', max_length=14)  # Field name made lowercase.
    isisento = models.TextField(db_column='isIsento')  # Field name made lowercase. This field type is a guess.
    ierg = models.CharField(db_column='ieRg', max_length=14)  # Field name made lowercase.
    razao = models.CharField(max_length=80)
    fantasia = models.CharField(max_length=80)
    islojasistema = models.TextField(
        db_column='isLojaSistema')  # Field name made lowercase. This field type is a guess.
    iscliente = models.TextField(db_column='isCliente')  # Field name made lowercase. This field type is a guess.
    isfornecedor = models.TextField(db_column='isFornecedor')  # Field name made lowercase. This field type is a guess.
    istransportadora = models.TextField(
        db_column='isTransportadora')  # Field name made lowercase. This field type is a guess.
    situacao = models.IntegerField()
    usuariocadastro = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioCadastro_id',
                                        db_column='usuarioCadastro_id', blank=True,
                                        null=True)  # Field name made lowercase.
    datacadastro = models.DateTimeField(db_column='dataCadastro', blank=True, null=True)  # Field name made lowercase.
    usuarioatualizacao = models.ForeignKey('Usuario', models.DO_NOTHING, related_name='usuarioAtualizacao_id',
                                           db_column='usuarioAtualizacao_id', blank=True,
                                           null=True)  # Field name made lowercase.
    dataatualizacao = models.DateTimeField(db_column='dataAtualizacao', blank=True,
                                           null=True)  # Field name made lowercase.
    dataabetura = models.DateTimeField(db_column='dataAbetura', blank=True, null=True)  # Field name made lowercase.
    naturezajuridica = models.CharField(db_column='naturezaJuridica', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class EmpresaEndereco(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    endereco = models.OneToOneField('Endereco', models.DO_NOTHING, db_column='endereco_id', unique=True)

    class Meta:
        managed = False
        db_table = 'empresa_endereco'


class Endereco(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField(blank=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING, blank=True, null=True)
    prox = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'endereco'


class MenuPrincipal(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu = models.CharField(max_length=45)
    menulabel = models.CharField(max_length=45, db_column='menuLabel')
    icomenu = models.CharField(max_length=80, db_column='icoMenu', null=True)
    istabpane = models.BooleanField(db_column='isTabPane')
    teclaatalho = models.CharField(max_length=45, db_column='teclaAtalho')

    class Meta:
        managed = False
        db_table = 'menuPrincipal'


class Municipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=80)
    uf = models.ForeignKey('Uf', models.DO_NOTHING)
    iscapital = models.TextField(db_column='isCapital')  # Field name made lowercase. This field type is a guess.
    ibge_codigo = models.CharField(max_length=7)
    ddd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'municipio'


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
    codwsportabiliadadeceluar = models.CharField(db_column='codWsPortabiliadadeCeluar', max_length=30, blank=True,
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
    senha = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=120, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'usuario'

    def get_Usuario_Senha(self, mailusuario):
        return Usuario.objects.values_list('email', 'senha').get(email=mailusuario)
