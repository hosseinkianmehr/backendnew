from distutils import text_file
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import URLField


class youtube(models.Model):
    title = models.CharField(max_length=120)
    Summary = RichTextUploadingField(blank=True,null=True)
    utls_youtube = models.URLField(("utls_youtube"), max_length=200 , null=True)
    utls_aparat = models.URLField(("utls_aparat"), max_length=200 , null=True)
    content = RichTextUploadingField()
    imagecontent = models.ImageField(("image"), upload_to=None, height_field=None, width_field=None, max_length=None)
    createTime = models.TimeField(("Time"), auto_now=False, auto_now_add=False)
    tag = models.ManyToManyField('TagAndComment.tag', related_name='tagsYoutube', verbose_name = ("tagyoutube") ,blank=True)

    class Meta:
        verbose_name = ("youtube")
        verbose_name_plural = ("youtubes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("youtube_detail", kwargs={"pk": self.pk})