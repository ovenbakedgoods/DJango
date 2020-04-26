# Generated by Django 3.0.5 on 2020-04-25 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_items', '0003_auto_20200424_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=65)),
                ('summary', models.TextField()),
                ('daily_space', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]
