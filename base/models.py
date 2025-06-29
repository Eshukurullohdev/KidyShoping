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
        ('9', '9 oylik'),
        ('10', '10 oylik'),             # ✅ Qo‘shildi
        ('11', '11 oylik'),             # ✅ Qo‘shildi
        ('12', '12 oylik'),             # ✅ Qo‘shildi
        ('13', '1 yosh'),               # ✅
        ('14', '2 yosh'),               # ✅
        ('15', '3 yosh'),
        ('16', '4 yosh'),
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
    BALAND_CHOICES = [
    ('40', '40 sm'),
    ('45', '45 sm'),
    ('50', '50 sm'),
    ('55', '55 sm'),
    ('60', '60 sm'),
    ('65', '65 sm'),
    ('70', '70 sm'),
]

# Kilogram variantlari
    KG_CHOICES = [
    ('2', '2 kg'),
    ('2.5', '2.5 kg'),
    ('3', '3 kg'),
    ('3.5', '3.5 kg'),
    ('4', '4 kg'),
    ('4.5', '4.5 kg'),
    ('5', '5 kg'),
    ]   
    pre_balandligi = models.CharField("PRE balandligi", max_length=50,     choices=BALAND_CHOICES, blank=True, null=True)
    pre_kilogrami = models.CharField("PRE kilogrami", max_length=50, choices=KG_CHOICES,    blank=True, null=True)

    nb_balandligi = models.CharField("NB balandligi", max_length=50, choices=BALAND_CHOICES,    blank=True, null=True)
    nb_kilogrami = models.CharField("NB kilogrami", max_length=50, choices=KG_CHOICES,  blank=True, null=True)

    m3_balandligi = models.CharField("3M balandligi", max_length=50, choices=BALAND_CHOICES,    blank=True, null=True)
    m3_kilogrami = models.CharField("3M kilogrami", max_length=50, choices=KG_CHOICES,  blank=True, null=True)

    m6_balandligi = models.CharField("6M balandligi", max_length=50, choices=BALAND_CHOICES,    blank=True, null=True)
    m6_kilogrami = models.CharField("6M kilogrami", max_length=50, choices=KG_CHOICES,  blank=True, null=True)

    m9_balandligi = models.CharField("9M balandligi", max_length=50, choices=BALAND_CHOICES,    blank=True, null=True)
    m9_kilogrami = models.CharField("9M kilogrami", max_length=50, choices=KG_CHOICES,  blank=True, null=True)
    # ... boshqa barcha fieldlar xuddi oldingidek ...
    main_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    birinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    ikkinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    uchinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    tortinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    beshinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
    oltinchi_img = models.ImageField(upload_to='kiyimlar/', blank=True, null=True)
  
    tavsifi = models.CharField(max_length=100)
    narhi = models.PositiveIntegerField()
    skidkasi = models.PositiveIntegerField(
    blank=True,
    null=True,
    verbose_name="Chegirma (%)",
    help_text="Chegirma foizi, agar yo'q bo‘lsa bo‘sh qoldiring"
    )

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