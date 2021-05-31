from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TODO, Project


class TODOModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = TODO
       fields = ['email', 'title', 'text']

class ProjectModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = Project
       fields = ['email', 'title', 'description']