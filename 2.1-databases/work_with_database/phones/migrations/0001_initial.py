# Generated by Django 3.2.16 on 2023-01-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.TextField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.CharField(max_length=5)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
    ]
