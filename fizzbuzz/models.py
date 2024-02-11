from django.db import models
from django.utils import timezone

class Fizzbuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True)  # AutoField for automatic id generation
    creation_date = models.DateTimeField(default=timezone.now)  # Automatically set the field when object is created
    useragent = models.CharField(max_length=255)  # Assuming it's a string representing the user agent
    message = models.TextField()  # Text field for potentially long messages

    def __str__(self):
        return f"Fizzbuzz {self.fizzbuzz_id}: {self.message[:20]}..."
