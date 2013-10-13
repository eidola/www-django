from django.db import models

class Release(models.Model):
    def upload_cover_to(self, filename):
        return 'releases/%s/cover/%s' %(self.title, filename)

    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    artists = models.ManyToManyField('artists.Artist')
    release_license = models.ForeignKey('ReleaseLicense')
    description = models.TextField()
    coverimage = models.ImageField(upload_to=upload_cover_to)
    

    def __str__(self):
        return self.title
   
class Track(models.Model):
    def upload_to(self, filename):
        return 'releases/%s/tracks/%s' % (self.id, self.sequence)

    release = models.ForeignKey('Release')
    title = models.CharField(max_length=250)
    sndFile = models.FileField(upload_to=upload_to)
    sequence = models.IntegerField()

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['sequence']

class ReleaseLicense(models.Model):
    title = models.CharField(max_length=250)
    summary = models.TextField()
    description = models.TextField()
    legal = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
