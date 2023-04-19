# Generated by Django 4.2 on 2023-04-18 09:27

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('small_description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=1000)),
                ('original_price', models.FloatField(max_length=50000000000)),
                ('selling_price', models.FloatField(max_length=50000000000)),
                ('status', models.BooleanField(default=False, help_text='0-default,1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-Trending')),
                ('tag', models.CharField(max_length=100)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.TextField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
