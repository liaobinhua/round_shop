# Generated by Django 2.0.6 on 2018-07-17 08:11

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_sn', models.CharField(default='', max_length=50, verbose_name='商品货码')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('sold_num', models.IntegerField(default=0, verbose_name='销售量')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('goods_num', models.IntegerField(default=0, verbose_name='库存数')),
                ('marke_price', models.FloatField(default=0, verbose_name='市场价格')),
                ('shop_price', models.FloatField(default=0, verbose_name='本店价格')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='商品简短描述')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('ship_fee', models.BooleanField(default=True, verbose_name='是否免运费')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='CommodityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='分类名称', max_length=60, verbose_name='分类名称')),
                ('code', models.CharField(default='', help_text='分类code', max_length=30, verbose_name='分类code')),
                ('desc', models.TextField(default='', help_text='分类描述', verbose_name='分类描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类'), (2, '二级类'), (3, '三级类')], help_text='分类级别', verbose_name='分类级别')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父类级别', null=True, on_delete=django.db.models.deletion.CASCADE, to='commodity.CommodityCategory', verbose_name='父类级别')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
            },
        ),
        migrations.CreateModel(
            name='CommodityCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='品牌名', max_length=30, verbose_name='品牌名')),
                ('desc', models.TextField(default='', help_text='品牌描述', max_length=200, verbose_name='品牌描述')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='commodity.CommodityCategory', verbose_name='商品类')),
            ],
            options={
                'verbose_name': '品牌名',
                'verbose_name_plural': '品牌名',
                'db_table': 'commodity_commoditybrand',
            },
        ),
        migrations.CreateModel(
            name='CommodityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='commodity.Commodity', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='commodity.CommodityCategory', verbose_name='商品类')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity', to='commodity.Commodity')),
            ],
            options={
                'verbose_name': '首页商品类广告',
                'verbose_name_plural': '首页商品类广告',
            },
        ),
        migrations.AddField(
            model_name='commodity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.CommodityCategory', verbose_name='商品分类'),
        ),
    ]
