# import openai
# import os
# from dotenv import load_dotenv

# # Load .env
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# system_prompt = """
# Your name is Brady, a knowledgeable and practical code assistant. You provide clear, concise explanations of programming concepts, avoiding unnecessary jargon. Focus on breaking down complex ideas into simple, actionable steps. Use relevant, real-world code examples to help users understand how things work in practice. When appropriate, offer best practices and common pitfalls to watch out for.
# """

# def ask_question(question, model="gpt-4o"):
#     response = openai.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": question}
#         ],
#         stream=True
#     )

#     markdown_output = ""
#     for chunk in response:
#         if chunk.choices[0].delta.content:
#             markdown_output += chunk.choices[0].delta.content

#     return markdown_output

# if __name__ == "__main__":
#     user_input = input("Ask your coding question: ")
#     result = ask_question(user_input)
#     print("\n\n" + result)

import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = """
Your name is Brady, a knowledgeable and practical code assistant. You provide clear, concise explanations of programming concepts, avoiding unnecessary jargon. Focus on breaking down complex ideas into simple, actionable steps. Use relevant, real-world code examples to help users understand how things work in practice. When appropriate, offer best practices and common pitfalls to watch out for.
"""

def ask_question(question, model="gpt-4o"):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        stream=True
    )

    markdown_output = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            markdown_output += chunk.choices[0].delta.content

    return markdown_output

if __name__ == "__main__":
    user_input = input("Ask your coding question: ")
    result = ask_question(user_input)

    # Print the full Markdown output
    print("\n\n" + result)

    # Save to a file
    with open("output.md", "w") as f:
        f.write(result)
