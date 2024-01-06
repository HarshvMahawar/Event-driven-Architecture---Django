# Generated by Django 4.1.3 on 2024-01-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoogleSheetIntegration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleSheetIntegrationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('answer_1', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('answer_2', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('answer_3', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
