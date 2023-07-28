# Generated by Django 4.1.1 on 2022-09-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('участок', 'участок'), ('улица', 'улица'), ('первый_дом', 'первый_дом'), ('баня', 'баня'), ('второй_дом', 'второй_дом')], default='улица', max_length=15)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]