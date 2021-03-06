# Generated by Django 3.2.9 on 2021-12-06 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_rename_keywords_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AddField(
            model_name='coursename',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AddField(
            model_name='juryinfo',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AddField(
            model_name='semester',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AddField(
            model_name='summary',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AddField(
            model_name='title',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.document'),
        ),
        migrations.AlterField(
            model_name='author',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
        migrations.AlterField(
            model_name='coursename',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
        migrations.AlterField(
            model_name='juryinfo',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
        migrations.AlterField(
            model_name='mentorinfo',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
        migrations.AlterField(
            model_name='title',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.user'),
        ),
    ]
