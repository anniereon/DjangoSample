# Generated by Django 5.2.1 on 2025-06-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_horse_jockey_race_racedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jockey',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='cumulative_place_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='cumulative_place_rate_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='cumulative_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='dirt_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='dirt_wins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='first_place',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='graded_race_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='graded_race_wins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='normal_race_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='normal_race_wins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='place_rate_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='place_rate_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='second_place',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='special_race_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='special_race_wins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='third_place',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='total_place_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='total_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='turf_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='turf_wins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='unplaced',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='win_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jockey',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='actual_style_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='actual_style_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='actual_style_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='direction',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='distance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='expected_style_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='expected_style_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='expected_style_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='ground',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='horse_age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='in_out',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='num_closers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='num_front_runners',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='num_horses',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='num_mid_runners',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='num_pace_makers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='top3_closers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='top3_front_runners',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='top3_mid_runners',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='top3_pace_makers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='track_condition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='venue',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='weather',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='avg_recent_rank',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='avg_recent_time_index1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='best_time_index1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='best_time_index2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='frame_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='horse_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='horse_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='horse_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='jockey_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='last_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='load_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='num_closing_run',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='num_front_run',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='num_mid_run',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='num_pace_run',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='odds',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='passing_order',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='popularity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='running_style',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='sex_age',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='racedetail',
            name='time_index',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
