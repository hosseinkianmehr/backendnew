from django.db import models


class youtube(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
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