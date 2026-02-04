# chat/services/rag_service.py
from .gemini_service import GeminiProvider
from database.models import Plano, Documento

def get_planos_contexto() -> str:
    planos = Plano.objects.all()

    if not planos.exists():
        return "Nenhum plano cadastrado."

    texto = ""
    for plano in planos:
        texto += (
            f"Plano {plano.nome}: "
            f"{plano.descricao}. "
            f"Valor mensal: R$ {plano.preco}.\n\n"
        )

    return texto.strip()


def handle_chat(pergunta: str) -> str:
    provider = GeminiProvider()
    
    dados = get_planos_contexto()
    
    contexto = "Documentos institucionais não carregados."

    prompt = f"""
    
Você é um assistente virtual da Prever Marília especializado em planos de saúde.

=== REGRAS IMPORTANTES ===
1. Use APENAS as informações fornecidas abaixo
2. NÃO use markdown (**, *, #, etc.)
3. NÃO use listas com bullet points (•, -, *)
4. Use APENAS texto simples
5. Seja conciso: máximo 3-6 linhas por resposta
6. Use quebras de linha duplas para separar informações
7. Se não tiver informação, diga claramente

=== ESTRUTURA DA RESPOSTA ===
- Linhas seguintes: Resposta direta e objetiva
- Última linha: Pergunta se quer mais detalhes (opcional)


=== INFORMAÇÕES DISPONÍVEIS ===

PLANOS:
{dados}

DOCUMENTOS:
{contexto}

=== PERGUNTA DO USUÁRIO ===
{pergunta}

=== SUA RESPOSTA (SIGA AS REGRAS ACIMA) ===
    """

    return provider.gerar(prompt)
