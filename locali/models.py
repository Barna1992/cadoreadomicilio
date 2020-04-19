from django.db import models

GIORNI_SETTIMANA = [
    ('AP', 'Sempre Aperto'),
    ('LU', 'Lunedi'),
    ('MA', 'Martedi'),
    ('ME', 'Mercoledi'),
    ('GI', 'Giovedi'),
    ('VE', 'Venerdi'),
    ('SA', 'Sabato'),
    ('DO', 'Domenica')
]


CATEGORIE = [
    ('AB', 'Abbigliamento'),
    ('AL', 'Alimentari'),
    ('AN', 'Articoli per animali'),
    ('BA', 'Bar'),
    ('CA', 'Cambio Gomme'),
    ('ED', 'Edicola'),
    ('FI', 'Fioreria'),
    ('FE', 'Ferramenta e materiali edili'),
    ('FV', 'Frutta e verdura'),
    ('GE', 'Gelateria'),
    ('MA', 'Macelleria'),
    ('PA', 'Panificio'),
    ('PI', 'Pizzeria'),
    ('PS', 'Pasticceria'),
    ('RI', 'Ristorante'),
]


COMUNI = [
('1', 'Auronzo di Cadore (BL)'),
('2', 'Borca di Cadore (BL)'),
('3', 'Calalzo di Cadore (BL)'),
('4', 'Cibiana di Cadore (BL)'),
('5', 'Danta di Cadore (BL)'),
('6', 'Domegge di Cadore (BL)'),
('7', 'Lorenzago di Cadore (BL)'),
('8', 'Lozzo di Cadore (BL)'),
('9', 'Ospitale di Cadore (BL)'),
('10', 'Perarolo di Cadore (BL)'),
('11', 'Pieve di Cadore (BL)'),
('12', 'San Pietro di Cadore (BL)'),
('13', 'San Vito di Cadore (BL)'),
('14', 'Santo Stefano di Cadore (BL)'),
('15', 'Selva di Cadore (BL)'),
('16', 'Valle di Cadore (BL)'),
('17', 'Vigo di Cadore (BL)'),
('18', 'Vodo Cadore (BL)'),
('19', 'Zoppè di Cadore (BL)'),
]

class ComuneConsegna(models.Model):
    COMUNI = COMUNI
    comune = models.CharField(
        max_length=2,
        choices=COMUNI,
        default='1',
    )

    def __str__(self):
        return '{}'.format(self.get_comune_display())

class Locale(models.Model):
    GIORNI_SETTIMANA = GIORNI_SETTIMANA
    CATEGORIE = CATEGORIE
    COMUNI = COMUNI
    name = models.CharField(max_length=100)
    comune = models.CharField(
        max_length=2,
        choices=COMUNI,
        default='1',
    )
    email = models.EmailField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    sito = models.URLField(blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    come_funziona = models.CharField(max_length=2000, blank=True, null=True)
    note = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pranzo = models.BooleanField()
    cena = models.BooleanField()
    chiusura = models.CharField(
        max_length=2,
        choices=GIORNI_SETTIMANA,
        default='DO',
    )
    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIE,
        default='AL',
    )
    orario_mattina = models.CharField(max_length=50, blank=True, null=True)
    orario_pomeriggio = models.CharField(max_length=50, blank=True, null=True)
    consegno_a = models.ManyToManyField(ComuneConsegna)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{} - {}'.format(self.name, self.get_comune_display())
