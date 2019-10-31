# Generated by Django 2.2.6 on 2019-10-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome Cliente')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=4, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('uf', models.CharField(choices=[('SP', 'São Paulo'), ('PI', 'Piauí'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais')], default='', max_length=2, verbose_name='UF')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Item')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Tema')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor do Aluguel')),
                ('cor', models.CharField(choices=[('1', 'Vermelho'), ('2', 'Verde'), ('3', 'Amarelo'), ('4', 'Azul'), ('5', 'Rosa'), ('6', 'Laranja')], default='', max_length=1, verbose_name='Cor da mesa')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacoes.Item')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_festa', models.DateField(verbose_name='Data da Festa')),
                ('horai', models.TimeField(verbose_name='Hora Inicial')),
                ('horat', models.TimeField(verbose_name='Hora Término')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor Cobrado')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacoes.Cliente')),
                ('endereco', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacoes.Endereco')),
                ('tema', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacoes.Tema')),
            ],
            options={
                'verbose_name': 'Aluguel',
                'verbose_name_plural': 'Alugueis',
            },
        ),
    ]