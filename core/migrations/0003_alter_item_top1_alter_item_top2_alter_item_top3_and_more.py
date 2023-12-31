# Generated by Django 4.2.2 on 2023-06-29 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_store_description_alter_item_top1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='top1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top1', to='core.store'),
        ),
        migrations.AlterField(
            model_name='item',
            name='top2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top2', to='core.store'),
        ),
        migrations.AlterField(
            model_name='item',
            name='top3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top3', to='core.store'),
        ),
        migrations.AlterField(
            model_name='item',
            name='top4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top4', to='core.store'),
        ),
        migrations.AlterField(
            model_name='item',
            name='top5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top5', to='core.store'),
        ),
    ]
