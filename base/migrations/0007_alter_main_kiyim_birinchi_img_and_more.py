# Generated by Django 5.0.4 on 2025-06-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_main_kiyim_birinchi_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_kiyim',
            name='birinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='main_kiyim',
            name='ikkinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='main_kiyim',
            name='ikkinchi_varianat_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='main_kiyim',
            name='main_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='main_kiyim',
            name='varianat_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
