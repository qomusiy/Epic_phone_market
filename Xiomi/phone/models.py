from django.db import models

# Create your models here.
class Phone(models.Model):
    maker = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='phone_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.maker}, {self.model}, {self.created_at}"