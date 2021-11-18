from django.db import models

class Movie(models.Model):
    name= models.CharField(max_length=255,unique=True)
    description = models.TextField(default='Description...',null=True)
    likes = models.IntegerField(default=0,null=True)
    watch_count = models.IntegerField(default=0,null=True)
    rate = models.PositiveIntegerField(default=0,null=True)
    prod_date= models.DateField(null=True, blank=True)
    creation_date= models.DateField(auto_now_add=True)
    mod_date= models.DateField(auto_now=True)
    actors= models.ManyToManyField('Actor')
    poster= models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=200, default='Name...')

    def __str__(self):
        return  self.name
        
    class Meta:
        ordering= ('name',)

class Review(models.Model):
    review = models.TextField(default='Leave your review here')
    creation_date= models.DateField(auto_now_add=True)
    movie= models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.review
