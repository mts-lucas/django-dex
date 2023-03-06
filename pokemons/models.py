from django.db import models

# Create your models here.


class PkmType(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class PkmAbility(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Evolutions(models.Model):
    number = models.IntegerField()
    first_form = models.CharField(max_length=65)

    def __str__(self):

        return self.first_form


class Generation(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):

        return self.name


class Pokemon(models.Model):

    number = models.IntegerField()
    name = models.CharField(max_length=65)
    picture = models.URLField()
    evolution_chain_number = models.ForeignKey(
        Evolutions,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        default=None,)
    #  physical attributes
    height = models.IntegerField()
    weight = models.IntegerField()
    #  status base
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    #  pokemon types
    pkm_types = models.ManyToManyField(PkmType)
    color_type = models.CharField(max_length=35)

    abilities = models.ManyToManyField(PkmAbility)

    generation = models.ForeignKey(
        Generation,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        default=None,)

    def __str__(self):

        infos = str(self.number) + ' - ' + self.name

        return infos
