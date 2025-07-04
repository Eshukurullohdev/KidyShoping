# Generated by Django 5.0.4 on 2025-06-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_main_kiyim_m3_balandligi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_kiyim',
            name='balandligi',
        ),
        migrations.RemoveField(
            model_name='main_kiyim',
            name='kilogrami',
        ),
        migrations.AddField(
            model_name='main_kiyim',
            name='beshinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='kiyimlar/'),
        ),
        migrations.AddField(
            model_name='main_kiyim',
            name='oltinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='kiyimlar/'),
        ),
        migrations.AddField(
            model_name='main_kiyim',
            name='sakizinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='kiyimlar/'),
        ),
        migrations.AddField(
            model_name='main_kiyim',
            name='tortinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='kiyimlar/'),
        ),
        migrations.AddField(
            model_name='main_kiyim',
            name='uchinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='kiyimlar/'),
        ),
        migrations.AddField(
            model_name='main_kiyim',
            name='yetinchi_img',
            field=models.ImageField(blank=True, null=True, upload_to='kiyimlar/'),
        ),
    ]
