from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Activity model
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

# Workout model
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')

    def __str__(self):
        return self.name

# Leaderboard model
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - Rank {self.rank}"
