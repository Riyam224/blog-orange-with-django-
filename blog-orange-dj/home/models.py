from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse 



class Customer(models.Model):
    name = models.CharField(_("name"), max_length=50)
    content = models.TextField(_("content"))
    job = models.CharField(_("job title"), max_length=50)

    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name



class Post(models.Model):
    name  = models.CharField(_("name"), max_length=50)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    image = models.ImageField(_("image"), upload_to='posts')
    slug = models.SlugField(_("slug") , blank=True , null=True)

    

    class Meta:
        ordering = ('name',)
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
    
    def __str__(self):
        return self.name
    
    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Post , self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("home:post_detail", kwargs={"slug": self.slug})





class Recent_Post(models.Model):
    """Model definition for Recent_Post."""
    post = models.ForeignKey(Post, verbose_name=_("post"), on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='recents' , blank=True , null=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Recent_Post."""

        verbose_name = 'Recent_Post'
        verbose_name_plural = 'Recent_Posts'

    def __str__(self):
        """Unicode representation of Recent_Post."""
        return str(self.post.name )




class Comment(models.Model):
    name = models.CharField(_("name"), max_length=50)
    content = models.TextField(_("content"))
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
  

    

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.name





class Category(models.Model):
    title = models.CharField(_("title"), max_length=50)

    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.title


FOOD_AT = (
    ('7:30 AM' , '7:30 AM'),
    ('1:30 PM' , '1:30 PM'),
    ('8:30 PM', '8:30 PM')
)



class About(models.Model):
    """Model definition for About."""
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    serving_time = models.CharField(_("serving time"), choices=FOOD_AT , max_length=10)
    image = models.ImageField(_("image "), upload_to='serving', blank=True  , null=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.category.title




class Team(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("team image"), upload_to='team', blank=True , null=True)
    job_title = models.CharField(_("job title"), max_length=50)

    

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name





class Contact(models.Model):
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    subject = models.CharField(_("subject"), max_length=50)
    message = models.TextField(_("message"))
    phone_number = models.IntegerField(_("phone number"))
    place = models.CharField(_("place"), max_length=50)

    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name