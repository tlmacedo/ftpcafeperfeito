# Generated by Django 2.1.3 on 2018-11-21 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=80)),
                ('apelido', models.CharField(max_length=30)),
                ('ctps', models.CharField(max_length=30)),
                ('dataadmisao', models.DateTimeField(blank=True, db_column='dataAdmisao', null=True)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=19)),
                ('ativo', models.IntegerField()),
            ],
            options={
                'db_table': 'colaborador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.IntegerField()),
                ('cnpjcpf', models.CharField(db_column='cnpjCpf', max_length=14)),
                ('isisento', models.TextField(db_column='isIsento')),
                ('ierg', models.CharField(db_column='ieRg', max_length=14)),
                ('razao', models.CharField(max_length=80)),
                ('fantasia', models.CharField(max_length=80)),
                ('islojasistema', models.TextField(db_column='isLojaSistema')),
                ('iscliente', models.TextField(db_column='isCliente')),
                ('isfornecedor', models.TextField(db_column='isFornecedor')),
                ('istransportadora', models.TextField(db_column='isTransportadora')),
                ('situacao', models.IntegerField()),
                ('datacadastro', models.DateTimeField(blank=True, db_column='dataCadastro', null=True)),
                ('dataatualizacao', models.DateTimeField(blank=True, db_column='dataAtualizacao', null=True)),
                ('dataabetura', models.DateTimeField(blank=True, db_column='dataAbetura', null=True)),
                ('naturezajuridica', models.CharField(db_column='naturezaJuridica', max_length=150)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpresaEndereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'empresa_endereco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.IntegerField(blank=True)),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=80)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=80)),
                ('bairro', models.CharField(max_length=50)),
                ('prox', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'endereco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuPrincipal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('menu', models.CharField(max_length=45)),
                ('menulabel', models.CharField(db_column='menuLabel', max_length=45)),
                ('icomenu', models.CharField(db_column='icoMenu', max_length=80, null=True)),
                ('istabpane', models.BooleanField(db_column='isTabPane')),
                ('teclaatalho', models.CharField(db_column='teclaAtalho', max_length=45)),
            ],
            options={
                'db_table': 'menuPrincipal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=80)),
                ('iscapital', models.TextField(db_column='isCapital')),
                ('ibge_codigo', models.CharField(max_length=7)),
                ('ddd', models.IntegerField()),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'telefone',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Telefoneoperadora',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=30)),
                ('tipo', models.IntegerField()),
                ('ddd', models.IntegerField()),
                ('codwsportabiliadadeceluar',
                 models.CharField(blank=True, db_column='codWsPortabiliadadeCeluar', max_length=30, null=True)),
            ],
            options={
                'db_table': 'telefoneOperadora',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'uf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id',
                 models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True,
                                      serialize=False, to='cafeperfeito.Colaborador')),
                ('situacao', models.IntegerField(blank=True, null=True)),
                ('senha', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
