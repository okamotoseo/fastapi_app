import requests

url = "https://api.sysplayer.com.br/api/v1/generate-description"

payloads = [
    {
        "input_code": "def add(a, b):\n    return a + b",
        "expected_keywords": ["function called add", "two numbers", "returns the sum"]
    },
    {
        "input_code": "def greet(name):\n    return f'Hello, {name}!'",
        "expected_keywords": ["function greet", "string argument", "returns a greeting", "f-string syntax"]
    }
]

for payload in payloads:
    try:
        response = requests.post(url, json={"input_code": payload["input_code"]}, verify=False)
        response.raise_for_status()  # Raises an error for 4xx/5xx responses
        result = response.json()
        print(f"Response: {result}")
        description = result.get('description', 'No description available')
        print(f"Código de entrada: {payload['input_code']}")
        print(f"Descrição: {description}")
        test_passed = all(keyword in description for keyword in payload['expected_keywords'])
        print(f"Teste Passou: {test_passed}\n")
    except requests.exceptions.HTTPError as err:
        print(f"Erro na solicitação: {err}")
        print(f"Código de entrada: {payload['input_code']}")
        print("Teste Passou: False\n")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        print(f"Código de entrada: {payload['input_code']}")
        print("Teste Passou: False\n")

