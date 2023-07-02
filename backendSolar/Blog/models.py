from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class blog(models.Model):
    main_titel = models.CharField(("titel"), max_length=50 , default="null")
    tag = models.ManyToManyField('TagAndComment.tag', related_name='tagsBlog', verbose_name = ("tagblog") ,blank=True)
    createTime = models.DateField('date', auto_now=False, auto_now_add=False)
    
    titel1 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content1 = RichTextUploadingField(blank=True,null=True,  max_length=200 )
    iamge1 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge11 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    
    titel2 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content2 = RichTextUploadingField(blank=True,null=True)
    iamge2 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge22 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    
    titel3 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content3 = RichTextUploadingField(blank=True,null=True)
    iamge3 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge33 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content4 = RichTextUploadingField(blank=True,null=True)
    iamge4 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge44 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel1 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content5 = RichTextUploadingField(blank=True,null=True)
    iamge5 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge55 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel1 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content6 = RichTextUploadingField(blank=True,null=True)
    iamge6 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge66 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel1 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content7 = RichTextUploadingField(blank=True,null=True)
    iamge7 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge77 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel1 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content8 = RichTextUploadingField(blank=True,null=True)
    iamge8 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge88 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel1 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content9 = RichTextUploadingField(blank=True,null=True)
    iamge9 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge99 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    titel1 =models.CharField(("titel"), max_length=50,null = True ,blank=True)
    content10 = RichTextUploadingField(blank=True,null=True)
    iamge10 = models.ImageField(("image"), upload_to=None,blank=True,null=True)
    iamge1010 = models.ImageField(("image"), upload_to=None,blank=True,null=True)

    class Meta:
        verbose_name = ("blog")
        verbose_name_plural = ("blogs")

    def __str__(self):
        return self.main_titel

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

