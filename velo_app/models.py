from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    current_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    target_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fitness_level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Challenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=[('steps', 'Steps'), ('distance', 'Distance covered'), ('calories', 'Calories Burned'), ('minutes', 'Active Minutes'), ('workouts', 'Workout Sessions')], null=True)
    target = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    total_scores = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Challenge({self.title}, {self.user.username})"
    
class ChallengeParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    joined_at = models.DateTimeField(auto_now_add=True)

class ActivityTrackerLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    activity_type = models.CharField(max_length=50, choices=[('workout', 'Workout'), ('steps', 'Steps')], null=True)
    duration = models.DurationField()
    calories_burned = models.PositiveIntegerField()
    steps = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"ActivityTracker({self.user.username}, {self.date}, {self.activity_type})"