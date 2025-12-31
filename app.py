from openai import OpenAI
from prompt import TEST_CASE_PROMPT
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(requirement: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior QA engineer."},
            {"role": "user", "content": TEST_CASE_PROMPT.format(requirement=requirement)}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    with open("sample_input.txt", "r") as f:
        requirement = f.read()

    test_cases = generate_test_cases(requirement)
    print("\nGenerated Test Cases:\n")
    print(test_cases)
