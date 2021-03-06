# Generated by Django 2.2.3 on 2020-01-03 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitchUser',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=255, unique=True)),
                ('display_name', models.CharField(max_length=255)),
                ('profile_image_url', models.URLField()),
                ('offline_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UpdateSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeChannel',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('priority', models.IntegerField(choices=[(-1, 'None'), (0, 'Low'), (1, 'Medium'), (2, 'High')], default=1)),
                ('thumbnail', models.URLField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('playlist_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('publication', models.DateTimeField()),
                ('gathering', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.URLField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifpy.YoutubeChannel')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addition', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=-1)),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifpy.Playlist')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifpy.YoutubeVideo')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='rules',
            field=models.ManyToManyField(blank=True, to='notifpy.YoutubeChannel'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='videos',
            field=models.ManyToManyField(blank=True, through='notifpy.PlaylistMembership', to='notifpy.YoutubeVideo'),
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regex', models.CharField(default='.*', max_length=255)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifpy.YoutubeChannel')),
            ],
        ),
    ]
