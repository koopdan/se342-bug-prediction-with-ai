import cohere
import google.generativeai as palm
import openai

from dotenv import load_dotenv
import os

load_dotenv()


def get_cohere_response(query):
    cohere_test_api_key = os.getenv("COHERE_TEST_API_KEY")
    co = cohere.Client(cohere_test_api_key)  # This is your trial API key
    response = co.chat(
        model="command",
        message=query,
        temperature=0.3,
        chat_history=[],
        prompt_truncation="auto",
        stream=False,
        citation_quality="accurate",
        connectors=[{"id": "web-search"}],
        documents=[],
    )

    print("Cohere finished responding")
    return response.text


def get_palm_response(query):
    palm_api_key = os.getenv("PALM_API_KEY")
    palm.configure(api_key=palm_api_key)
    defaults = {
        "model": "models/text-bison-001",
        "temperature": 0.7,
        "candidate_count": 1,
        "top_k": 40,
        "top_p": 0.95,
        "max_output_tokens": 1024,
        "stop_sequences": [],
        "safety_settings": [
            {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
            {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
            {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
            {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
            {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
            {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2},
        ],
    }
    prompt = query

    response = palm.generate_text(**defaults, prompt=prompt)
    print("PALM finished responding")
    return response.result


def get_openai_response(query):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print("OpenAI finished responding")
    return response.choices[0].message.content


def get_model_responses(query):
    cohere_response = get_cohere_response(query)
    openai_response = get_openai_response(query)
    palm_response = get_palm_response(query)

    model_responses = {
        "cohere": cohere_response,
        "openai": openai_response,
        "palm": palm_response,
    }

    return model_responses


print(get_model_responses("Who is Spiderman?"))
