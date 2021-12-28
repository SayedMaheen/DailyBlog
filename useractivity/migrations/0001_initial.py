# Generated by Django 4.0 on 2021-12-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogpost', '0001_initial'),
        ('bloguser', '0002_bloguser'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, max_length=2)),
                ('like_activity', models.DateTimeField(auto_now=True)),
                ('liked_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bloguser.bloguser')),
                ('liked_post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blogpost.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='CommentOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='No Comments', max_length=255)),
                ('comment_activity', models.DateTimeField(auto_now=True)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogpost.blogpost')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloguser.bloguser')),
            ],
        ),
    ]
