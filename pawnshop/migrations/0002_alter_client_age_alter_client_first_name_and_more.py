# Generated by Django 4.0.4 on 2022-05-06 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='age',
            field=models.IntegerField(verbose_name='Вік'),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name="И'мя"),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport_num',
            field=models.CharField(max_length=8, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='item',
            name='amount_pledged',
            field=models.IntegerField(verbose_name='Сума, винная під заставу'),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_make',
            field=models.DateField(auto_now_add=True, verbose_name='Дата сдачи'),
        ),
        migrations.AlterField(
            model_name='item',
            name='estimated_cost',
            field=models.IntegerField(verbose_name='Оціночна вартість'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Найменування'),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pawnshop.client', verbose_name='Власник'),
        ),
        migrations.AlterField(
            model_name='item',
            name='save_until',
            field=models.DateField(verbose_name='Зберігати до'),
        ),
    ]
