# Generated by Django 3.1.5 on 2021-01-14 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(related_name='get_post', to='blog.Categoria'),
        ),
    ]