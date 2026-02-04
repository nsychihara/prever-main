from rest_framework import serializers


class ChatRequestSerializer(serializers.Serializer):
    """Serializer para validar a mensagem enviada pelo usuário"""
    mensagem = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=1000,
        error_messages={
            'required': 'O campo mensagem é obrigatório.',
            'blank': 'A mensagem não pode estar vazia.',
            'max_length': 'A mensagem não pode ter mais de 1000 caracteres.'
        }
    )


class ChatResponseSerializer(serializers.Serializer):
    """Serializer para formatar a resposta da IA"""
    resposta = serializers.CharField()
    status = serializers.CharField()
    timestamp = serializers.DateTimeField()