# Generated by Django 2.0.7 on 2018-07-22 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0003_auto_20180719_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commoditycategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父类级别', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='commodity.CommodityCategory', verbose_name='父类级别'),
        ),
    ]