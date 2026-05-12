import ollama

def get_ai_response(user_input):

    response = ollama.chat(
        model='tinyllama',
        messages=[
            {
                'role': 'user',
                'content': user_input
            }
        ]
    )

    return response['message']['content']