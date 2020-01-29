from django.contrib.auth.models import AbstractUser ,UserManager
from django.db import models
import logging
logger = logging.getLogger(__name__)

class TreeManeger(UserManager):
    """ Пагинатор """
    def get_childrens(self,perent):
        q=self.filter(root=perent)
        return q

    def get_parent(self,children):
        if children.level and  getattr(children,'root')==None:
            return None
        return children.root

    def search_users_via_atr(self,user,atr,value):
        if   getattr(user,atr) == value:
            return user
        elif user.level == 0:
            return 'None'
        else:
            q= self.search_users_via_atr(self.get_parent(user),atr,value)
            return q
        logger.warn(msg=f"lol  { self } Non correct ")
        return None


# ABS MODEL
# class Tree(models.Model):
#     object=models.Manager()
#     objectTree=TreeManeger()
#     id = models.AutoField(primary_key=True)
#     root = models.ForeignKey('Tree', related_name='+',on_delete=models.CASCADE,blank=True,null=True)
#     level= models.IntegerField(default=0,blank=False,null=False)
#     name = models.CharField(default="test",max_length=12)
#
#     def save(self, force_insert=False, force_update=False, using=None,
#              update_fields=None) -> None:
#         """ This f modifite  level and save date to datebase  """
#         if getattr(self,'root') ==None:
#             self.level=0
#         else:
#             self.level=abs(self.root.level) +1
#         super().save()

class CustomUser(AbstractUser):

    objects= TreeManeger()
    level= models.IntegerField(default=0,blank=False,null=False)
    root = models.ForeignKey('CustomUser', related_name='+',on_delete=models.CASCADE,blank=True,null=True)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None) -> None:
        """ This f modifite  level and save date to datebase  """
        if getattr(self,'root') ==None:
            self.level=0
        else:
            self.level=abs(self.root.level) +1
        super().save()