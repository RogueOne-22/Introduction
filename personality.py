import requests

# Uso de un API_KEY para interconectarnos con el API de DeepSeek
API_URL = 'https://api.deepseek.com/v1/chat/completions'
API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e'  # Reemplaza con tu API key

def enviar_mensaje(mensaje, modelo='deepseek-chat', personalidad=None):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Definir el mensaje de sistema para la personalidad
    messages = []
    if personalidad:
        messages.append({'role': 'system', 'content': personalidad})
    messages.append({'role': 'user', 'content': mensaje})

    data = {
        'model': modelo,
        'messages': messages
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Comprueba si existe un posible error en HTTP
        return response.json()['choices'][0]['message']['content']
    
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err.response.text}"
    except Exception as e:
        return f"Error Inesperado: {e}"

def main():
    print("Bienvenido al chatbot de DeepSeek. Si usted desea salir escriba 'salir' para terminar")

    # Definir la personalidad del chatbot
    personalidad = "Eres un chatbot existencialista guiado por la filosofia de Kant y divertido. Responde siempre con un toque de humor y simpatía."

    while True:
        mensaje_usuario = input("Tú: ")

        if mensaje_usuario.lower() == 'salir':
            print("Chatbot: Hasta luego!")
            break 

        respuesta = enviar_mensaje(mensaje_usuario, personalidad=personalidad)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    main()
