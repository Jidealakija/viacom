from django.db import models

CONTACT_TYPE = (
    ('Inquiry', 'Inquiry'),
    ('Complaint', 'Complaint')
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(help_text= 'Insert a valid email')
    type = models.CharField(max_length=10, choices=CONTACT_TYPE)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name