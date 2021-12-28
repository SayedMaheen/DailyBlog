# Generated by Django 4.0 on 2021-12-28 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloguser', '0003_bloguser_username'),
        ('blogpost', '0003_alter_blogpost_content'),
        ('useractivity', '0003_alter_likedpost_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_status', models.BooleanField(default=False)),
                ('user_activity', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(default='No Comments', max_length=255)),
                ('current_post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blogpost.blogpost')),
                ('current_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bloguser.bloguser')),
            ],
        ),
        migrations.RemoveField(
            model_name='likedpost',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='likedpost',
            name='liked_post',
        ),
        migrations.DeleteModel(
            name='CommentOn',
        ),
        migrations.DeleteModel(
            name='LikedPost',
        ),
    ]
