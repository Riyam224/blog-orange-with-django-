from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name



class Product(models.Model):
    """Model definition for Product."""
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='products',blank=True , null=True)
    name = models.CharField(_("name"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    slug = models.SlugField(_("slug") ,blank=True , null=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Product , self).save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
