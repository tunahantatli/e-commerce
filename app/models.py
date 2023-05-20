from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
    ('AD', 'Adana'),
    ('ADI', 'Adıyaman'),
    ('AF', 'Afyonkarahisar'),
    ('AG', 'Ağrı'),
    ('AKS', 'Aksaray'),
    ('AM', 'Amasya'),
    ('ANK', 'Ankara'),
    ('ANT', 'Antalya'),
    ('ARD', 'Ardahan'),
    ('ART', 'Artvin'),
    ('AYI', 'Aydın'),
    ('BAL', 'Balıkesir'),
    ('BAR', 'Bartın'),
    ('BAT', 'Batman'),
    ('BAY', 'Bayburt'),
    ('BIL', 'Bilecik'),
    ('BIN', 'Bingöl'),
    ('BIT', 'Bitlis'),
    ('BOL', 'Bolu'),
    ('BRD', 'Burdur'),
    ('BRS', 'Bursa'),
    ('ÇAN', 'Çanakkale'),
    ('ÇAN', 'Çankırı'),
    ('ÇOR', 'Çorum'),
    ('DEN', 'Denizli'),
    ('DIY', 'Diyarbakır'),
    ('DÜZ', 'Düzce'),
    ('ED', 'Edirne'),
    ('ELA', 'Elazığ'),
    ('ERZ', 'Erzincan'),
    ('ERZ', 'Erzurum'),
    ('ESK', 'Eskişehir'),
    ('GAZ', 'Gaziantep'),
    ('GIR', 'Giresun'),
    ('GMS', 'Gümüşhane'),
    ('HAK', 'Hakkari'),
    ('HAT', 'Hatay'),
    ('IGD', 'Iğdır'),
    ('ISPA', 'Isparta'),
    ('IST', 'Istanbul'),
    ('IZM', 'Izmir'),
    ('KAHR', 'Kahramanmaraş'),
    ('KARA', 'Karabük'),
    ('KARAM', 'Karaman'),
    ('KARS', 'Kars'),
    ('KAS', 'Kastamonu'),
    ('KAY', 'Kayseri'),
    ('KIL', 'Kilis'),
    ('KIRIK', 'Kırıkkale'),
    ('KIRKL', 'Kırklareli'),
    ('KIRSE', 'Kırşehir'),
    ('KOC', 'Kocaeli'),
    ('KON', 'Konya'),
    ('KÜTA', 'Kütahya'),
    ('MAL', 'Malatya'),
    ('MAN', 'Manisa'),
    ('MARD', 'Mardin'),
    ('MERS', 'Mersin'),
    ('MUĞ', 'Muğla'),
    ('MUŞ', 'Muş'),
    ('NEVŞ', 'Nevşehir'),
    ('NİĞD', 'Niğde'),
    ('ORDU', 'Ordu'),
    ('OSM', 'Osmaniye'),
    ('RIZ', 'Rize'),
    ('SAKA', 'Sakarya'),
    ('SAM', 'Samsun'),
    ('SİIR', 'Siirt'),
    ('SİNA', 'Sinop'),
    ('ŞIRN', 'Şırnak'),
    ('SİV', 'Sivas'),
    ('TEK', 'Tekirdağ'),
    ('TOK', 'Tokat'),
    ('TRA', 'Trabzon'),
    ('TUN', 'Tunceli'),
    ('URF', 'Urfa'),
    ('UŞA', 'Uşak'),
    ('VAN', 'Van'),
    ('YAL', 'Yalova'),
    ('YOZ', 'Yozgat'),
    ('ZON', 'Zonguldak'),
    )

# Create your models here.
CATEGORY_CHOISES=(
    ('WD','Web Development'),
    ('DS','Data Science'),
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

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)

    def __str__(self):
        return self.first_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price