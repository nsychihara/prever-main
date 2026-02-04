# test_gemini.py
# Script para testar se a API Key do Gemini está funcionando
# Execute: python test_gemini.py

import os
import sys
import django
from dotenv import load_dotenv

# Carregar .env
load_dotenv('.env')

print("=" * 60)
print("🔍 TESTE DA API KEY DO GEMINI")
print("=" * 60)

# Verificar se a chave está no .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("\n❌ ERRO: GEMINI_API_KEY não encontrada no arquivo .env")
    print("\n📝 Solução:")
    print("   1. Crie um arquivo .env na raiz do projeto")
    print("   2. Adicione: GEMINI_API_KEY=sua_chave_aqui")
    print("   3. Obtenha sua chave em: https://aistudio.google.com/apikey")
    sys.exit(1)

print(f"\n✅ API Key encontrada: {api_key[:20]}...")

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Testar a API
print("\n🧪 Testando conexão com Gemini...")

from chat.services.gemini_service import GeminiProvider

try:
    provider = GeminiProvider()
    resposta = provider.gerar("Responda apenas: OK")
    
    if "Erro" in resposta:
        print(f"\n❌ ERRO na API: {resposta}")
        print("\n📝 Verifique:")
        print("   1. A chave está correta?")
        print("   2. A chave tem permissões ativas?")
        print("   3. Teste em: https://aistudio.google.com/")
    else:
        print(f"\n✅ SUCESSO! Resposta do Gemini: {resposta}")
        print("\n🎉 Tudo funcionando! Pode testar no Insomnia agora.")
        
except Exception as e:
    print(f"\n❌ ERRO: {e}")
    print("\n📝 Verifique se instalou todas as dependências:")
    print("   pip install requests python-dotenv")

print("\n" + "=" * 60)