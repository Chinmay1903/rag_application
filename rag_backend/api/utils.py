import openai

openai.api_key = "your_openai_api_key"

def generate_answer(question, document_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Based on the following document:\n\n{document_text}\n\nAnswer the question: {question}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
