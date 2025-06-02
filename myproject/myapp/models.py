from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user_name

class Race(models.Model):
    race_id = models.CharField(max_length=50, primary_key=True)
    date = models.DateField(null=True, blank=True)
    race_name = models.CharField(max_length=100, null=True, blank=True)
    race_class = models.CharField(max_length=50, null=True, blank=True)
    race_number = models.IntegerField(null=True, blank=True)
    horse_age = models.CharField(max_length=50, null=True, blank=True)
    venue = models.CharField(max_length=50, null=True, blank=True)
    weather = models.CharField(max_length=50, null=True, blank=True)
    ground = models.CharField(max_length=50, null=True, blank=True)
    direction = models.CharField(max_length=50, null=True, blank=True)
    in_out = models.CharField(max_length=50, null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    num_horses = models.IntegerField(null=True, blank=True)
    num_front_runners = models.IntegerField(null=True, blank=True)
    num_pace_makers = models.IntegerField(null=True, blank=True)
    num_mid_runners = models.IntegerField(null=True, blank=True)
    num_closers = models.IntegerField(null=True, blank=True)
    top3_front_runners = models.IntegerField(null=True, blank=True)
    top3_pace_makers = models.IntegerField(null=True, blank=True)
    top3_mid_runners = models.IntegerField(null=True, blank=True)
    top3_closers = models.IntegerField(null=True, blank=True)
    expected_style_1 = models.CharField(max_length=50, null=True, blank=True)
    expected_style_2 = models.CharField(max_length=50, null=True, blank=True)
    expected_style_3 = models.CharField(max_length=50, null=True, blank=True)
    actual_style_1 = models.CharField(max_length=50, null=True, blank=True)
    actual_style_2 = models.CharField(max_length=50, null=True, blank=True)
    actual_style_3 = models.CharField(max_length=50, null=True, blank=True)
    track_condition = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'race'

class RaceDetail(models.Model):
    race = models.ForeignKey('Race', on_delete=models.CASCADE, db_column='race_id')
    horse_id = models.CharField(max_length=50, null=True, blank=True)
    rank = models.CharField(max_length=50, null=True, blank=True)
    frame_number = models.IntegerField(null=True, blank=True)
    horse_number = models.IntegerField(null=True, blank=True)
    sex_age = models.CharField(max_length=10, null=True, blank=True)
    load_weight = models.FloatField(null=True, blank=True)
    jockey_name = models.CharField(max_length=50, null=True, blank=True)
    time = models.CharField(max_length=20, null=True, blank=True)
    time_index = models.IntegerField(null=True, blank=True)
    passing_order = models.CharField(max_length=50, null=True, blank=True)
    last_time = models.FloatField(null=True, blank=True)
    odds = models.CharField(max_length=20, null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    horse_weight = models.TextField(null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    trainer_comment = models.TextField(blank=True, null=True)
    avg_recent_rank = models.FloatField(null=True, blank=True)
    avg_recent_time_index1 = models.FloatField(null=True, blank=True)
    best_time_index1 = models.IntegerField(null=True, blank=True)
    best_time_index2 = models.IntegerField(null=True, blank=True)
    running_style = models.CharField(max_length=20, null=True, blank=True)
    num_front_run = models.IntegerField(null=True, blank=True)
    num_pace_run = models.IntegerField(null=True, blank=True)
    num_mid_run = models.IntegerField(null=True, blank=True)
    num_closing_run = models.IntegerField(null=True, blank=True)
    development_prediction = models.TextField(blank=True, null=True)
    check_target = models.BooleanField(blank=True, null=True)
    check_result = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'race_detail'
        unique_together = ('race', 'horse_number')

    def __str__(self):
        return f"{self.race.race_id} - 馬番 {self.horse_number}"

class Jockey(models.Model):
    jockey_id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        db_table = 'jockey'

    def __str__(self):
        return self.jockey_id

class Horse(models.Model):
    horse_id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        db_table = 'horse'

    def __str__(self):
        return self.horse_id
