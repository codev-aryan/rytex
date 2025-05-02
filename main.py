from dotenv import load_dotenv
import os
import google.generativeai as genai
import json
import datetime

def interpret_command_with_gpt(command):
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    response = model.generate_content([


        "input: Hello, how are you?",
        "output: {"
            "\n    \"kind\": \"general_chat\","
            "\n    \"parameters\": {"
            "\n        \"response\": \"I'm doing great, thank you! How can I assist you today?\""
            "\n    }"
            "\n}",


        "input: Can you write a Python program to add two numbers?",
        "output: {"
            "\n    \"kind\": \"generate_code\","
            "\n    \"parameters\": {"
            "\n        \"task\": \"add two numbers\","
            "\n        \"code\": \"def add_two_numbers(num1, num2):\\n\\n"
            "\n                    return num1 + num2\\n\\n"
            "\n                    number1 = float(input(\\\"Enter the first number: \\\"))\\n"
            "\n                    number2 = float(input(\\\"Enter the second number: \\\"))\\n\\n"
            "\n                    result = add_two_numbers(number1, number2)\\n\\n"
            "\n                    print(\\\"The sum of\\\", number1, \\\" and \\\",number2,\\\" is \\\",result)\\n\","
            "\n        \"language\": \"Python\""
            "\n    }"
            "\n}",


        "input: What is the current date?",
        "output: {"
            "\n    \"kind\": \"date_time\","
            "\n    \"parameters\": {"
            "\n        \"response\": \"The current date is: {{current_date}}\""
            "\n    }"
            "\n}",


        "input: 3+5",
        "output: {"
            "\n    \"kind\": \"mathematics\","
            "\n    \"parameters\": {"
            "\n        \"result\": \"3+5 is 8\""
            "\n    }"
            "\n}",


        f"input: {command}",
        "output: "
    ])

    return response.text

def process_interpreted_command(interpreted_command):

    command_data = json.loads(interpreted_command)
    kind = command_data["kind"]
    parameters = command_data["parameters"]

    if kind == "generate_code":
        # Handle the generation of code
        code = parameters.get("code", "")
        return code

    elif kind == "general_chat":
        # Handle a general chat response
        response = parameters.get("response", "No response provided.")
        return response

    elif kind == "mathematics":
        # Handle a math expression
        result = parameters.get("result","Sorry, there was an error in evaluating the expression.")
        return result


    elif kind == "date_time":
        # Handle date and time requests
        response = parameters.get("response", "")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.datetime.now().strftime("%H:%M")
        response = response.replace("{{current_date}}", current_date)
        response = response.replace("{{current_time}}", current_time)
        return response

    else:
        # Handle unknown actions
        return "I couldn't quite understand that. Please try another prompt."

def main():
    a = ""
    while True:
        a = f"Previous chat context: {a}\n\nCurrent message: " + str(input("Enter Your prompt: "))

        b = interpret_command_with_gpt(a)
        result = process_interpreted_command(b)
        print(result)
        a += "\n"

main()  #calling the main funtion