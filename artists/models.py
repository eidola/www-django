from django.db import models

class Artist(models.Model):   
    def upload_to(self, filename):
        return 'artists/%s/img/%s' % (self.name, filename)
   
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
