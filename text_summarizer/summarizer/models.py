from django.db import models

class UploadedText(models.Model):
    text = models.TextField()
    summarized_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"UploadedText {self.id}"