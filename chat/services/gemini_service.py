import requests
from django.conf import settings


class GeminiProvider:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.api_url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            "models/gemini-2.5-flash:generateContent"
        )

    def gerar(self, prompt: str) -> str:
        """
        Gera resposta usando Gemini AI
        """
        try:
            request_body = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 1000,
                    "topP": 0.95,
                    "topK": 40
                }
            }

            url = f"{self.api_url}?key={self.api_key}"

            response = requests.post(
                url,
                json=request_body,
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            if response.status_code != 200:
                return f"Erro na API Gemini: {response.text}"

            data = response.json()

            if "candidates" not in data or not data["candidates"]:
                return "Não foi possível gerar uma resposta."

            return data["candidates"][0]["content"]["parts"][0]["text"]

        except requests.exceptions.Timeout:
            return "Tempo limite excedido. Tente novamente."
        except Exception as e:
            return f"Erro ao consultar Gemini: {str(e)}"
