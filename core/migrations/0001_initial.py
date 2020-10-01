# Generated by Django 3.1.1 on 2020-10-01 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.IntegerField()),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('senha', models.CharField(max_length=10)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.contato')),
                ('favorito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.favorito')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('subCategoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.subcategoria')),
            ],
        ),
        migrations.AddField(
            model_name='favorito',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servico'),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('palavrasChaves', models.CharField(max_length=50)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.contato')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.endereco')),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.feedback')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servico')),
            ],
        ),
    ]