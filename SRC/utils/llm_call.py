from openai import OpenAI


def create_prompt_company_news(row):
    return (
        "You are an expert in financial sentiment analysis.\n\n"
        "Analyze the following news article and respond with only:\n"
        "- 1 if the sentiment is clearly positive\n"
        "- 0 in all other cases (negative, neutral, or unclear)\n\n"
        "Do not explain your answer. Do not add any comments. Only respond with 1 or 0.\n\n"
        f"Date: {row['publishedAt']}\n"
        f"Source: {row['source']}\n"
        f"Title: {row['headline']}\n"
        f"Summary: {row['summary']}"
    )


def get_news_sentiment(prompt):
    """Client == wsl host client"""
    client = OpenAI(
        api_key="EMPTY",  # vLLM ne vérifie pas la clé
        base_url="http://172.29.96.59:8000/v1",  # ton endpoint vLLM
    )
    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct-AWQ",  # modèle chargé dans vLLM
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=1,
        )
        content = response.choices[0].message.content.strip()
        return int(content) if content in ["0", "1"] else None
    except Exception as e:
        print(f"Erreur : {e}")
        return None
