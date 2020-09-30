# Generated by Django 3.1.1 on 2020-09-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_result_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dump',
            name='operating_system',
            field=models.CharField(choices=[('Linux', 'Linux'), ('Windows', 'Windows'), ('Mac', 'Mac'), ('Other', 'Other')], default='Linux', max_length=10),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='operating_system',
            field=models.PositiveSmallIntegerField(choices=[('Linux', 'Linux'), ('Windows', 'Windows'), ('Mac', 'Mac'), ('Other', 'Other')], default=1),
        ),
    ]