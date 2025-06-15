from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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"
)

def  chat_with_ai(ques):
    completion = client.chat.completions.create(
    model="meta-llama/llama-3.3-8b-instruct:free",
    messages=[
        {
        "role": "user",
        "content": ques
        }
    ]
    )
    return completion.choices[0].message.content


# This part is for the chatbot without GUI 
#while True:
    #usermsg = input("You :")
    #if usermsg.lower() in ["quit","bye","thank you","thanks","see you"]:
        #print("Quint: Bye and See you again soon!")
        #break 
      
    #response = chat_with_ai(usermsg)
    #print("Quint: ", response) 
    



    