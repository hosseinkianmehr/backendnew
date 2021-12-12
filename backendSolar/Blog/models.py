from django.db import models


class blog(models.Model):
    minetitel = models.TextField(("minetitel"))
    tag = models.ManyToManyField('TagAndComment.tag', related_name='tagsBlog', verbose_name = ("tagblog") ,blank=True)
    createTime = models.DateField()
    updateTime = models.DateField()

    titel1 =models.TextField(("Text"),blank=True,null=True)
    contentblog1 = models.TextField(("content"),blank=True,null=True)
    iamge1 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel2 =models.TextField(("Text"),blank=True,null=True)
    contentblog2 = models.TextField(("content"),blank=True,null=True)
    iamge2 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel3 =models.TextField(("Text"),blank=True,null=True)
    contentblog3 = models.TextField(("content"),blank=True,null=True)
    iamge3 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel4 =models.TextField(("Text"),blank=True,null=True)
    contentblog4 = models.TextField(("content"),blank=True,null=True)
    iamge4 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    
    class Meta:
        verbose_name = ("blog")
        verbose_name_plural = ("blogs")

    def __str__(self):
        return self.minetitel

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

