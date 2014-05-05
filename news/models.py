from django.db import models

class Article(models.Model):
    def upload_image_to(self, filename):
        return 'news/%s/image/%s' %(self.title, filename)

    title = models.CharField(max_length=250)
    text = models.TextField('Description body as HTML', blank=True, null=True)
    text_markdown = models.TextField('Description', help_text='Use Markdown syntax.', blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to=upload_image_to)

    def __str__(self):
        return self.title

    def save(self):
        import markdown
        self.text = markdown.markdown(self.text_markdown)
        super(Article, self).save() # Call the "real" save() method.
