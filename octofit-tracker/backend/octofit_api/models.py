from django.db import models


class Activity(models.Model):
    user_name = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.user_name} - {self.activity_type} ({self.duration_minutes} min)"
