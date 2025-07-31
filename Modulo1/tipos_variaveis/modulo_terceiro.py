
# request contem série de instruções e funções que ajudam a fazer requisições HTTP, requisições em websites.

print("\nImportação e uso de um módulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")

