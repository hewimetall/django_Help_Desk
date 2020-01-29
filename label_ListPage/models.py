from django.db import models

from login.models import CustomUser

# Create your models here.
class dashBourdManeger(models.Manager):
    def get_group_article_user(self,user):
        top_user=CustomUser.objects.search_users_via_atr(user=user,atr="groups",value=user.groups)
        q=Types.objects.filter(meneger=top_user)
        summ_q=[ dashBourdBd.objects.filter(types=i) for i in q]
        return summ_q

    def get_article_user_autor(self,user):
        q=dashBourdBd.objects.filter(autors=user)
        return q

    def get_article_user_maneger(self,user):
        q=dashBourdBd.objects.filter(manager_a=user)
        return q

class Types(models.Model):
    objects=models.Manager()
    id=models.AutoField(primary_key=True)

    Types=models.CharField(max_length=120,unique=True)
    meneger = models.ForeignKey(CustomUser, related_name='menegerTypes', on_delete=models.DO_NOTHING, )  # Автор обращения

    date_created=models.DateTimeField(auto_created=True,auto_now_add=True)

    def __str__(self):
        return self.Types

class dashBourdBd(models.Model):
    objects = dashBourdManeger()

    Priority = [
        (1, "Низкий"),
        (2, "Нормальный"),
        (3, "Срочный"),
    ]

    STATUS = [
        (1, "В обработке"),
        (2, "Отправленно на доработку"),
        (3, "В работе"),
        (4, "Выполнена"),
        (5, "Закрыта"),
    ]

    title = models.CharField(max_length=50)  # Названия заявки
    content = models.TextField()  # Текст обращения

    autors = models.ForeignKey(CustomUser, related_name='autorsCr', on_delete=models.DO_NOTHING, )  # Автор обращения
    manager_a = models.ForeignKey(CustomUser, related_name='manager_aCr', on_delete=models.DO_NOTHING, blank=True,
                                  null=True)  # Ответственный

    priority = models.IntegerField(choices=Priority, default=Priority[0][0], blank=True, null=True)  # Приоритет заявки
    types= models.ForeignKey(Types, related_name='typesTicket',on_delete=models.DO_NOTHING,)  # Тип заявки

    status = models.IntegerField(choices=STATUS, default=STATUS[0][0])  # Статус заявки
    data = models.DateField(auto_created=True, auto_now_add=True, db_index=True)  # Дата на момент создания
    File = models.FileField(blank=True, null=True, default=None)  # file Name

    def search_tuple(self, tups, elem):
        return [a for i, a in (filter(lambda tup: elem in tup, tups))]

    def getPriority(self):
        return self.search_tuple(self.Priority, self.priority)[0]

    def getTypes(self):
        return self.search_tuple(self.TYPE, self.types)[0]

    def getStatus(self):
        return self.search_tuple(self.STATUS, self.status)[0]

    def getUrl(self):
        return 0


class ticketChat(models.Model):
    post = models.ForeignKey(dashBourdBd, related_name='comments', on_delete=models.CASCADE, db_column='pk',blank=False,null=True)
    name = models.ForeignKey(CustomUser, related_name='userCreated', on_delete=models.DO_NOTHING, db_column='username')
    file = models.FileField(blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    class Options:
        userField = ['comments', 'id', 'data', 'title', 'content', 'autors', 'priority', 'types', 'status', 'File']
        manegerField = ['comments', 'id', 'data', 'title', 'content', 'autors', 'priority', 'types', 'status', 'File']
        tableField = ['comments', 'id', 'data', 'title', 'content', 'autors', 'priority', 'types', 'status', 'File']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
