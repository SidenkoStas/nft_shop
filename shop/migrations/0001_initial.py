# Generated by Django 4.0.6 on 2023-03-15 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Категории')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Коллекция')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='nft/%Y/%m/%d/', verbose_name='NFT')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='artist', to=settings.AUTH_USER_MODEL, verbose_name='Художник')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категория')),
                ('collections', models.ManyToManyField(blank=True, to='shop.collections', verbose_name='Коллекции')),
            ],
            options={
                'verbose_name': 'NFT token',
                'verbose_name_plural': 'NFT tokens',
                'ordering': ['-creation_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='OwnerNFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ManyToManyField(to='shop.item', verbose_name='NFT токен')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владельцы',
            },
        ),
    ]