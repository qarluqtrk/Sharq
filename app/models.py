from django.db import models


class MainInfo(models.Model):
    title = models.CharField(max_length=255)
    logo_light = models.ImageField(upload_to='logos/')
    logo_dark = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Main Info'
        verbose_name_plural = 'Main Info'

class Banner(models.Model):
    title_part1 = models.CharField(max_length=255)
    title_part2 = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, default="Request A Visit")
    button_link = models.URLField(default="#")

    def __str__(self):
        return self.title_part1

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class Counter(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class LocationBenefits(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Location Benefits'
        verbose_name_plural = 'Location Benefits'

class Apartments(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    floor_plan = models.ImageField(upload_to='floor_plans/')
    text = models.TextField()
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    rooms = models.PositiveIntegerField(null=True, blank=True)
    area = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Apartment'
        verbose_name_plural = 'Apartments'

class AboutImages(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Images'
        verbose_name_plural = 'About Images'


class Prospecs(models.Model):
    icon = models.ImageField(upload_to='icons/')
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Prospects'
        verbose_name_plural = 'Prospects'
