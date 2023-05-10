from django.db import models

# Create your models here.
CATEGORY_CHOISES=(
    ('WD','Web Development'),
    ('DS','Data Secience'),
    ('AI', 'Artificial Intelligence'),
    ('GM', 'Game® Development')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOISES, max_length=100)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title