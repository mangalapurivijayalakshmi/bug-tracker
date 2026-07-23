from django.db import models
from django.contrib.auth.models import User

# Bug Model (this creates a "bugs" table in database)
class Bug(models.Model):

    # Priority choices
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    # Status choices
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    title       = models.CharField(max_length=200)        # Bug title
    description = models.TextField()                       # Bug details
    priority    = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_by  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='reported_bugs') 
    assigned_to  = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_bugs'
    )  # Who is fixing the bug
    created_at  = models.DateTimeField(auto_now_add=True)  # Auto date/time
    updated_at   = models.DateTimeField(auto_now=True)        # Auto updates every save

    class Meta:
        ordering = ['-created_at']   # Latest bugs show first
    def __str__(self):
        return self.title
