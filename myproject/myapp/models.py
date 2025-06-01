from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Race(models.Model):
    race_id = models.CharField(max_length=50, primary_key=True)
    date = models.DateField()
    race_name = models.CharField(max_length=100)
    race_class = models.CharField(max_length=50)
    race_number = models.IntegerField()
    horse_age = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    weather = models.CharField(max_length=50)
    ground = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    in_out = models.CharField(max_length=50)
    distance = models.IntegerField()
    num_horses = models.IntegerField()
    num_front_runners = models.IntegerField()
    num_pace_makers = models.IntegerField()
    num_mid_runners = models.IntegerField()
    num_closers = models.IntegerField()
    top3_front_runners = models.IntegerField()
    top3_pace_makers = models.IntegerField()
    top3_mid_runners = models.IntegerField()
    top3_closers = models.IntegerField()
    expected_style_1 = models.CharField(max_length=50)
    expected_style_2 = models.CharField(max_length=50)
    expected_style_3 = models.CharField(max_length=50)
    actual_style_1 = models.CharField(max_length=50)
    actual_style_2 = models.CharField(max_length=50)
    actual_style_3 = models.CharField(max_length=50)
    track_condition = models.CharField(max_length=50)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'race'

class RaceDetail(models.Model):
    race = models.ForeignKey('Race', on_delete=models.CASCADE, db_column='race_id')
    horse_id = models.CharField(max_length=50)
    rank = models.IntegerField()
    frame_number = models.IntegerField()
    horse_number = models.IntegerField()
    sex_age = models.CharField(max_length=10)
    load_weight = models.FloatField()
    jockey_name = models.CharField(max_length=50)
    time = models.CharField(max_length=20)
    time_index = models.IntegerField()
    passing_order = models.CharField(max_length=50)
    last_time = models.FloatField()
    odds = models.FloatField()
    popularity = models.IntegerField()
    horse_weight = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    trainer_comment = models.TextField(blank=True, null=True)
    avg_recent_rank = models.FloatField()
    avg_recent_time_index1 = models.FloatField()
    best_time_index1 = models.IntegerField()
    best_time_index2 = models.IntegerField()
    running_style = models.CharField(max_length=20)
    num_front_run = models.IntegerField()
    num_pace_run = models.IntegerField()
    num_mid_run = models.IntegerField()
    num_closing_run = models.IntegerField()
    development_prediction = models.TextField(blank=True, null=True)
    check_target = models.BooleanField(default=False)
    check_result = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'race_detail'
        unique_together = ('race', 'horse_number')  # 複合主キーの代用

    def __str__(self):
        return f"{self.race.race_id} - 馬番 {self.horse_number}"

class Jockey(models.Model):
    jockey_id = models.CharField(primary_key=True, max_length=20)
    year = models.IntegerField()
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    first_place = models.IntegerField()
    second_place = models.IntegerField()
    third_place = models.IntegerField()
    unplaced = models.IntegerField()
    graded_race_runs = models.IntegerField()
    graded_race_wins = models.IntegerField()
    special_race_runs = models.IntegerField()
    special_race_wins = models.IntegerField()
    normal_race_runs = models.IntegerField()
    normal_race_wins = models.IntegerField()
    turf_runs = models.IntegerField()
    turf_wins = models.IntegerField()
    dirt_runs = models.IntegerField()
    dirt_wins = models.IntegerField()
    win_rate = models.FloatField()
    place_rate_2 = models.FloatField()
    place_rate_3 = models.FloatField()
    total_runs = models.IntegerField()
    total_place_3 = models.IntegerField()
    cumulative_runs = models.IntegerField()
    cumulative_place_3 = models.IntegerField()
    cumulative_place_rate_3 = models.FloatField()

    class Meta:
        db_table = 'jockey'

    def __str__(self):
        return f"{self.jockey_id} - {self.name}"

class Horse(models.Model):
    horse_id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        db_table = 'horse'

    def __str__(self):
        return self.horse_id