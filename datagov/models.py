from django.db import models
from django.utils.translation import gettext as _

class PersonHouse(models.Model):
    house_code = models.IntegerField(_("House code"))
    house_addr = models.CharField(_("House addr"),max_length=50)


    class Meta:
        verbose_name = _("PersonHouse")
        verbose_name_plural = _("PersonHouses")

    def __str__(self):
        return str(self.house_code)

    def get_absolute_url(self):
        return reverse("PersonHouse_detail", kwargs={"pk": self.pk})
# ฐานข้อมูลบุคคลที่มีบัตรสวัสดิการแห่งรัฐ 2560
class PersonGov60(models.Model):
    
    nnid = models.CharField(_("nnid"), max_length=50)
    title = models.CharField(_("Title"), max_length=100)
    f_name = models.CharField(_("Firstname"), max_length=200)
    l_name = models.CharField(_("Lastname"), max_length=200)
    birth_date = models.DateField(_("Birthday"),blank=True, null=True)
    sex = models.CharField(_("Sex"), max_length=50,null=True)
    body_code = models.CharField(_("Body_code"), max_length=2,null=True)	
    house_code = models.ForeignKey(PersonHouse, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("PersonGov60")
        verbose_name_plural = _("PersonGov60s")

    def __str__(self):
        return str(self.title)+str(self.f_name)+" "+str(self.l_name)

    def get_absolute_url(self):
        return reverse("PersonGov60_detail", kwargs={"pk": self.pk})

   

