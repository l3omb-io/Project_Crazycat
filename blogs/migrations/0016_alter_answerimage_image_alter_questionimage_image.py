# Generated by Django 4.0.2 on 2022-02-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_documentimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='answer_image/'),
        ),
        migrations.AlterField(
            model_name='questionimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_image/'),
        ),
    ]