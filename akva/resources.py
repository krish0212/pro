from import_export import resources
from akva.models import User
 
class UserResource(resources.ModelResource):
    class Meta:
        model = User