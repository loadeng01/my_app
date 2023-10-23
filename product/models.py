from django.db import models as m


class Product(m.Model):
    title = m.CharField(max_length=120)
    description = m.TextField(null=True, blank=True)
    price = m.DecimalField(max_digits=10, decimal_places=2, default=100)
    created_at = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'Test'
    #     verbose_name_plural = 'Tests'


