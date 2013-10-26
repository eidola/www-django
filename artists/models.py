from django.db import models

class Artist(models.Model):   
    def upload_to(self, filename):
        return 'artists/%s/img/%s' % (self.name, filename)
   
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to)
    pub_date = models.DateTimeField('date published')
    links = models.ManyToManyField('Link', null=True, blank=True)

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    def upload_to(self, filename):
        return 'img/%s/%s' % (self.name, filename)

    name = models.CharField(max_length=200)
    baseurl = models.URLField()
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.name

class Link(models.Model):   
    name = models.CharField(max_length=200)
    url = models.URLField()
    userId = models.CharField(max_length=200, null=True, blank=True)
    linkType = models.ForeignKey('SocialLink', null=True, blank=True)
    
    def __str__(self):
        return self.name

