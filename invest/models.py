from django.db import models


class InvestPost(models.Model):
    projectNumber = models.CharField(max_length=150, verbose_name='Наименование проекта', db_index=True)
    status_list = (
        ('active', 'Активный'),
        ('completed', 'Завершенный')
    )
    statusProject = models.CharField(verbose_name='Статус проекта', max_length=250, choices=status_list)
    category = models.CharField(max_length=150, verbose_name='Категория долга:', db_index=True)
    amountDebts = models.IntegerField(verbose_name='Номинал долга:', db_index=True)
    amountRecovery = models.IntegerField(verbose_name='Плановая сумма взыскания:', db_index=True)
    amountBye = models.IntegerField(verbose_name='Сумма покупки:', db_index=True)
    amountCosts = models.IntegerField(verbose_name='Плановая сумма расходов:', db_index=True)
    expectedReturn = models.IntegerField(verbose_name='Ожидаемая годовая доходность:', db_index=True)
    amountInvestment = models.IntegerField(verbose_name='Сумма инвестиций:', db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.statusProject

    class Meta:
        verbose_name = """Проект"""
        verbose_name_plural = """Проекты"""

