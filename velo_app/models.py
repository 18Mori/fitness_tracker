from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    date = models.DateField()
    duration = models.DurationField()
    calories_burned = models.PositiveIntegerField()
    workout_details = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"WorkoutSession({self.user.username}, {self.date})"
    
class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"WeightEntry({self.user.username}, {self.date})"
    
class BodyMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"BodyMetric({self.user.username}, {self.date})"
    
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    target_date = models.DateField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Goal({self.user.username}, {self.description})"
    
    

class Challenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_scores = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    session_details = models.JSONField(default=list)

    def __str__(self):
        return f"Challenge({self.title}, {self.user.username})"
    
class ChallengeParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    joined_at = models.DateTimeField(auto_now_add=True)

class MinuteTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"MinuteTracker({self.user.username}, {self.date})"

class CalorieTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.PositiveIntegerField()
    total_calories = models.PositiveIntegerField(default=0)
    meal_details = models.JSONField(default=list)

    def __str__(self):
        return f"CalorieTracker({self.user.username}, {self.date})"