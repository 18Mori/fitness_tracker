from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    


class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    date = models.DateField()
    workout_type = models.CharField(max_length=50, choices=[('cardio', 'Cardio'), ('strength', 'Strength Training'), ('flexibility', 'Flexibility'), ('balance', 'Balance Training'), ('pilates', 'Pilates'), ('yoga', 'Yoga'), ('running', 'Running'), ('walking', 'Walking'), ('cycling', 'Cycling'), ('swimming', 'Swimming'), ('hiking', 'Hiking'), ('gym', 'Gym Workout')], null=True)
    duration = models.DurationField()
    calories_burned = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"WorkoutSession({self.user.username}, {self.date})"

class TrainingPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    description = models.TextField()
    duration = models.DurationField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TrainingPlan({self.name}, {self.user.username})"

class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"WeightEntry({self.user.username}, {self.date})"

    
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

class MinuteTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"MinuteTracker({self.user.username}, {self.date})"

class MealTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=50, choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')])
    protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fats = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    calories = models.PositiveIntegerField()
    total_calories = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"MealTracker({self.user.username}, {self.date})"

class ActivityTrackerLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    activity_type = models.CharField(max_length=50, choices=[('workout', 'Workout'), ('steps', 'Steps')], null=True)
    duration = models.DurationField()
    calories_burned = models.PositiveIntegerField()
    steps = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"ActivityTracker({self.user.username}, {self.date}, {self.activity_type})"