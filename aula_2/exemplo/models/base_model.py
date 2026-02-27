from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True # ela nao vai existir persistida no banco de dados, tornando-a um modelo abstrato.
        app_label = 'exemplo' # toda a model que for criada irá representar pertencer ao pacote "exemplo"

