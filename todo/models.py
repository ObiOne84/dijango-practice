from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # null and blank equal false, is to prevent creating item without name,
    # null prevents from creating items without name programmatically,
    # blank=False, make the field required on forms
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """
        To overwrite default Django naming object, we add function that
        returns the name of the added items. To add items you must go admin
        panel, click on the items and click add
        """
        return self.name
