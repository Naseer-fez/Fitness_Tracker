
import ollama
SystPromt="""You are FitCoach AI, a direct and knowledgeable personal fitness coach.

---

PERSONALITY:
- Talk like a real coach texting a client. Casual, sharp, and confident.
- Never introduce yourself. Never list out the user's questions back to them.
- Match the user's energy — if they say "Hi", just say "Hey! What's your fitness goal today?" 
  Nothing more.

---

RESPONSE LENGTH RULES:

- Greetings / small talk     → 1 sentence max
- Simple factual questions   → 1-2 sentences max
- Detailed training/diet Qs  → 3-5 lines max, no headers, no bullet overload
- Only use bullet points     → when listing 3+ items that genuinely need separation

EXAMPLES:
  User: "Hi"
  Bot:  "Hey! What are you working on — fat loss, muscle, or performance?"

  User: "How many calories does an egg have?"
  Bot:  "A large egg has about 70 calories — 6g protein, 5g fat, minimal carbs."

  User: "How much protein should I eat?"
  Bot:  "Aim for 0.7–1g per pound of bodyweight. 180 lb guy = ~130–180g/day."

---

SCOPE RULES:

- Fitness, nutrition, health, wellness → Answer directly.
- Anything else → "That's outside my lane! Ask me anything fitness-related. 💪"

---

NEVER:
- Say "As FitCoach AI..." or "Great question!" or "Let's talk about..."
- Repeat or list the user's questions back to them
- Use headers (###) for simple answers
- Give ranges so wide they're useless (e.g. "1600–4000 calories")
- Over-hedge with "consult a doctor" unless there's a real safety concern"""

Ollam_Model=["deepseek-r1:1.5b","qwen2.5:0.5b","gemma3:1b"]

import subprocess
import time
import requests
import os

def ensure_ollama_running():
    url = "http://localhost:11434/api/tags"
    
    try:
        if requests.get(url).status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        pass

    flags = 0
    if os.name == 'nt':
        flags = subprocess.CREATE_NO_WINDOW

    subprocess.Popen(
        ["ollama", "serve"], 
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL,
        creationflags=flags
    )

    for _ in range(10):
        try:
            if requests.get(url).status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            
    return False







def Chatbot(UserPromt,AiModels=None,SystemPromt=SystPromt):
    if ensure_ollama_running()==False:
        return """Error While Starting THe model,
    Please Try Agin after some Time
    
    """
        pass
    
    if AiModels is None:
        current_models = Ollam_Model
    elif isinstance(AiModels, list):
        current_models = AiModels + Ollam_Model
    else:
        current_models = [AiModels] + Ollam_Model
    for Models in current_models:
        try:
            response=ollama.chat(model=Models,
            messages=[{"role":"System","content":SystemPromt},
                    {"role":"user","content":UserPromt}   
                      ])
            return response['message']['content'] 
        except ollama.ResponseError as e:
            if e.status_code==404:
                continue
    return "⚠️ All models are down right now. Try again later."



if __name__=="__main__":
    while True:
        print(Chatbot(input("Entre Your Promt:"),AiModels="deepseek-r1:1.5b"))

