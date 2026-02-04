from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .serializers import ChatRequestSerializer, ChatResponseSerializer
from .services.rag_service import handle_chat


@api_view(['POST'])
def chat_message(request):
    """
    Endpoint para enviar mensagem ao chatbot
    
    POST /api/chat/
    Body: {"mensagem": "Quais planos vocês têm?"}
    
    Retorna a resposta da IA
    """
    # Valida a requisição
    serializer = ChatRequestSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(
            {
                'erro': 'Dados inválidos',
                'detalhes': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Pega a mensagem validada
    mensagem = serializer.validated_data['mensagem']
    
    try:
        # Processa com a IA
        resposta_ia = handle_chat(mensagem)
        
        # Formata a resposta
        response_data = {
            'resposta': resposta_ia,
            'status': 'success',
            'timestamp': timezone.now()
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {
                'erro': 'Erro ao processar mensagem',
                'detalhes': str(e),
                'status': 'error',
                'timestamp': timezone.now()
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def health_check(request):
    """
    Endpoint para verificar se a API está funcionando
    
    GET /api/health/
    """
    return Response(
        {
            'status': 'online',
            'message': 'API do Chatbot Prever está funcionando!',
            'timestamp': timezone.now()
        },
        status=status.HTTP_200_OK
    )