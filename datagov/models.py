from django.db import models
from django.utils.translation import gettext as _
class  gov_nid (models.Model):
    nnid = models.CharField(_("nnid"),max_length = 20,null=False)
    title = models.CharField(_("title"), max_length=50,null=False)
    f_name = models.CharField(_("f_name"), max_length=100,null=False)
    l_name = models.CharField(_("l_name"),max_length=100, null=False)
    birth_date = models.CharField(_("birth_date"),max_length=100, null=True)
    sex = models.CharField(_("sex"), max_length=50,null=True)
    body_code = models.CharField(_("body_code"), max_length=2,null=True)	
    house_code = models.CharField(_("house_code"), max_length=20,null=True)
    class Meta:
        ordering = ['-house_code']
        db_table = 'gov_nid'
    
    def __str__(self):
        return self.nnid,self.f_name,self.l_name




    

    class Meta:
        verbose_name = _("gov_addr")
        verbose_name_plural = _("gov_addrs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gov_addr_detail", kwargs={"pk": self.pk})


    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

