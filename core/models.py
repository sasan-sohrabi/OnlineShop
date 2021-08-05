# This part is used for import relevant libraries or some class or functions form other files in this project.

from django.db import models

# Create your models here.

# Create BaseManager to use it for overriding some methods.
class BaseManager(models.Manager):

    # Override all queries for ignoring records that is logically deleted.
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    # Archive is used for all data include logical deleted data.
    def archive(self):
        return super().get_queryset()



# Create BaseModel to use it for all of others models in this project.
class BaseModel(models.Model):

    # Deleted attribute is used for logical delete.
    deleted = models.BooleanField(default=False)


    objects = BaseManager()

    class Meta:
        abstract = True

# This class is  just used for test BaseModel.
class TestModel(BaseModel):
    pass


# Create TimeStampMixin to add date of create, modify and delete from database.
class TimeStampMixin(BaseModel):

    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
