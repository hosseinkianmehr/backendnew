from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class blog(models.Model):
    titel = models.TextField(("minetitel"))
    tag = models.ManyToManyField('TagAndComment.tag', related_name='tagsBlog', verbose_name = ("tagblog") ,blank=True)
    createTime = models.DateField('date', auto_now=False, auto_now_add=False)
    
    content = RichTextUploadingField()
    iamge1 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    class Meta:
        verbose_name = ("blog")
        verbose_name_plural = ("blogs")

    def __str__(self):
        return self.minetitel

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

