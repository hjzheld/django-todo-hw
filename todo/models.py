from django.db import models

class Todo(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
