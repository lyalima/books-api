from rest_framework import serializers
from .models import Author, Book
from datetime import date


class AuthorModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['id', 'name']
    

class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'owner', 
                  'resume', 'creation_date', 'update_date']

    def validate(self, data):
        current_date = date.today()
        creation_date = data.get('creation_date')
        update_date = data.get('update_date')

        if creation_date and creation_date > current_date:
            raise serializers.ValidationError(
                'A data de criação do livro não pode ser superior à data atual.')        
        if update_date and update_date < creation_date:
            raise serializers.ValidationError(
                'A data de atualização do livro não pode ser anterior à data de criação.')
        return data
