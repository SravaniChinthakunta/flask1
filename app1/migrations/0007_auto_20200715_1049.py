# Generated by Django 3.0.7 on 2020-07-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20200715_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolleddetails',
            name='idno',
            field=models.AutoField(default=False, primary_key=True, serialize=False),
        ),
    ]
