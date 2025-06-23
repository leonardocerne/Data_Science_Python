import openai

client = openai.OpenAI(api_key="sk-")  # nova forma de criar o cliente

def gera_texto(mensagens):
    response = client.chat.completions.create(
        model="gpt-4o",  # ou "gpt-3.5-turbo"
        messages=mensagens,
        temperature=0.8,
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

def main():
    print("\nBem-vindo ao chatbot do projeto 3!")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    mensagens = [{"role": "system", "content": "Você é um assistente amigável e útil."}]

    while True:
        user_message = input("\nVocê: ")
        if user_message.lower() == "sair":
            break

        mensagens.append({"role": "user", "content": user_message})
        resposta = gera_texto(mensagens)
        print(f"\nChatbot: {resposta}")
        mensagens.append({"role": "assistant", "content": resposta})

if __name__ == "__main__":
    main()