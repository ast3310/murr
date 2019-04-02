# Generated by Django 2.1.7 on 2019-04-02 12:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default_murren_img.jpg', upload_to='murren_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Murr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=78)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('featured', models.BooleanField(default=True)),
                ('cover', models.ImageField(blank=True, upload_to='murren_pics')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Murr_card.Author')),
                ('categories', models.ManyToManyField(blank=True, to='Murr_card.Category')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Murr_card.Murr'),
        ),
    ]
