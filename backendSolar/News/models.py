from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class news(models.Model):
    titel = models.CharField(("Titel"), max_length=50)
    content = RichTextUploadingField()
    tag = models.ManyToManyField('TagAndComment.tag', related_name='tagsNews', verbose_name = ("tagnews") ,blank=True)
    createTime = models.DateField(("Date"), auto_now=False, auto_now_add=False)
    imagecontent =models.ImageField(("iamge"), upload_to=None, height_field=None, width_field=None, max_length=None) 

    class Meta:
        verbose_name = ("news")
        verbose_name_plural = ("news")

    def __str__(self):
        return self.titel
        

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})

