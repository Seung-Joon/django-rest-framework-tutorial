from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style'] # set fields 
        #fields = '__all__'  # set all fields
        #exclude = 'title' # except fields
        #read_only_fields = 'title' # set readonly field



