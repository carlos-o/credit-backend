# Generated by Django 4.1.7 on 2023-03-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bank_type', models.CharField(choices=[('Private', 'Private'), ('Government', 'Government')], max_length=30, verbose_name='Type')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]