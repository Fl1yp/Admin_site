# Generated by Django 5.0.2 on 2024-03-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_alter_myhistory_options_myhistory_img_2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myhistory',
            options={'verbose_name': 'История', 'verbose_name_plural': 'История'},
        ),
        migrations.AddField(
            model_name='card',
            name='address',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт'),
        ),
    ]
