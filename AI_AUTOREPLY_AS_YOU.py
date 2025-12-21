import pyttsx3
from openai import OpenAI
import os

# Speaking Function
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()
    
speak("Enter Your API(Application Programming Interface)..........")
api_key = input("Enter Your API(Application Programming Interface) : ")

#=============Enter=Your=Role=============#
speak("Enter Your Role From These 4 Options....")
print("Select a role:")
print("1. system")
print("2. user")
print("3. assistant")
print("4. tool")
speak("Enter role number")
choice = input("Enter Role Number From Option : ")


roles = {
    "1": "system",
    "2": "user",
    "3": "assistant",
    "4": "tool"
}
role = roles[choice]
if choice in roles:
    print("Selected role: ", roles[choice])
    speak(f"Your selected Role Is {choice}")
else:
    speak("Invalid choice")
    print("❌ Invalid choice")
#=========================================#

#Tell me here what your name is and what you do, 
# what your profession is, and what you would like a reply as.
speak("Enter Who Are You")
whoareyou = input("Enter Who Are You : ")

def aiprocess(command):
    client = OpenAI(api_key=f"{api_key}")

    stream = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": f"{role}",
                "content": (
                    f"{whoareyou}"
                )
            },
            {
                "role": "user",
                "content": command   
            }
        ],
        stream=True,
    )

    full_response = ""

    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)
            full_response += event.delta

    print()
    return full_response

# This is made to tell the response.
def aitalk(text):
    speak(text)

# ---------- RUN ----------
# Tell me what your Question will be here.
#repeat The Commands Section
while True :
    speak("Enter Your Command.....")
    command = input("Enter Your Command(Massage) : ")

    response = aiprocess(f"{command}")
    aitalk(response)
