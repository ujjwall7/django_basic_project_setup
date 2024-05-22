from django.db import models
from django.utils.text import slugify





def rename_file(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

# class Section(models.Model):
#     section_type = models.CharField(max_length=50)
#     show = models.BooleanField(default=True)
