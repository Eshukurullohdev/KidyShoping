from django.db import models

class Main_Kiyim(models.Model):
    YOSH_CHOICES = [
        ('1', '1 oylik'),
        ('2', '2 oylik'),
        ('3', '3 oylik'),
        ('4', '4 oylik'),
        ('5', '5 oylik'),
        ('6', '6 oylik'),
        ('7', '7 oylik'),
        ('8', '8 oylik'),
        ('9', '9 oylik'),
    ]
    yoshi = models.CharField(
        max_length=2,
        choices=YOSH_CHOICES,
        blank=True,
        null=True,
        verbose_name="Bolalar yoshi"
    )
    GENDER_CHOICES = [
        ('qiz', 'Qiz bola'),
        ('ogil', 'O‘g‘il bola'),
    ]

    jinsi = models.CharField(
        max_length=5,
        choices=GENDER_CHOICES,
        default='qiz',
        verbose_name="Jinsi",
        help_text="Qiz bola yoki o‘g‘il bola uchun"
    )

    # ... boshqa barcha fieldlar xuddi oldingidek ...
    main_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    birinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    ikkinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    tavsifi = models.CharField(max_length=100)
    narhi = models.PositiveIntegerField()
    skidkasi = models.PositiveIntegerField(
    blank=True,
    null=True,
    verbose_name="Chegirma (%)",
    help_text="Chegirma foizi, agar yo'q bo‘lsa bo‘sh qoldiring"
    )
    balandligi = models.CharField(max_length=200, null=True, blank=True)
    kilogrami = models.CharField(max_length=50, null=True, blank=True)
    kiyim_haqida = models.TextField(null=True, blank=True)

    # xususiyatlar
    birinchi_xususiyati = models.CharField(max_length=50, null=True, blank=True)
    ikkinchi_xususiyati = models.CharField(max_length=50, null=True, blank=True)
    uchunchi_xususiyati = models.CharField(max_length=50, null=True, blank=True)
    tortinchi_xususiyati = models.CharField(max_length=50, null=True, blank=True)
    beshinchi_xususiyati = models.CharField(max_length=50, null=True, blank=True)
    oltinchi_xususiyati = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Asosiy kiyim"
        verbose_name_plural = "Asosiy kiyimlar"
        ordering = ['-id']

    def __str__(self):
        return f"{self.tavsifi} ({self.get_jinsi_display()})"

    
    @property
    def chegirma_foizi(self):
        if self.narhi and self.skidkasi and self.skidkasi > self.narhi:
            return round(((self.skidkasi - self.narhi) / self.skidkasi) * 100)
        return 0