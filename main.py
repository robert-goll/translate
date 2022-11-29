import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

print("Translate to Spanish, es, Translate to English, en")
userinput = input("Enter your choice: ")
if userinput == "es":
    print("Enter your sentence: ")
    sentence = input()
    esresponse = openai.Completion.create(
        engine="davinci",
        prompt="Translate the following sentence from English to Spanish:\n" + sentence + "\n\n", 
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        # stop=["\n",]
    )
    print(esresponse["choices"][0]["text"])
elif userinput == "en":
    print("Enter your sentence: ")
    sentence = input()
    enresponse = openai.Completion.create(
        engine="davinci",
        prompt="Translate the following sentence from Spanish to English:\n" + sentence + "\n\n",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        # stop=["\n", " Translation:"]
    )
    print(enresponse["choices"][0]["text"])
else:
    print("Invalid input")
    break
