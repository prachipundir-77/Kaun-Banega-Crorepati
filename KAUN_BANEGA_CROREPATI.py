import random
print("WELCOME TO KAUN BANEGA CROREPATI SEASON 2")

print("Rules for Quiz")
print("1. Money will increase with the question")
print("2. You can quit anytime and take the money won so far")
print("3. Every question has four options")

Money_Ladder={
    1:1000,
    2:2000,
    3:3000,
    4:5000,
    5:10000,
    6:20000,
    7:40000,
    8:80000,
    9:160000,
    10:320000,
    11:640000,
    12:1250000,
    13:2500000,
    14:5000000,
    15:10000000
}
lifelines ={
    "50-50":True,
    "audience poll":True,
    "phone a friend":True
}


questions= [{
        "question": "Which language is primarily used for web page structure?",
        "options": {"A": "HTML", "B": "CSS", "C": "Python", "D": "SQL"},
        "answer": "A",
        "category": "Technology",
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": {"A": "list", "B": "tuple", "C": "map", "D": "set"},
        "answer": "C",
        "category": "Python",
    },
    {
        "question": "Who is known as the 'Father of the Nation' in India?",
        "options": {"A": "Sardar Patel", "B": "Mahatma Gandhi", "C": "B. R. Ambedkar", "D": "Jawaharlal Nehru"},
        "answer": "B",
        "category": "GK - India",
    },
    {
        "question": "What does CPU stand for?",
        "options": {"A": "Central Process Unit", "B": "Central Processing Unit", "C": "Computer Personal Unit", "D": "Central Power Unit"},
        "answer": "B",
        "category": "Technology",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {"A": "Venus", "B": "Mars", "C": "Jupiter", "D": "Mercury"},
        "answer": "B",
        "category": "Space",
    },
    {
        "question": "In Python, what is the output of: len({1,1,2,3}) ?",
        "options": {"A": "4", "B": "3", "C": "2", "D": "Error"},
        "answer": "B",
        "category": "Python",
    },
    {
        "question": "The Pythagorean theorem applies to which type of triangle?",
        "options": {"A": "Equilateral", "B": "Isosceles", "C": "Right-angled", "D": "Scalene"},
        "answer": "C",
        "category": "Maths",
    },
    {
        "question": "Which data structure uses FIFO (First In, First Out)?",
        "options": {"A": "Stack", "B": "Queue", "C": "Tree", "D": "Graph"},
        "answer": "B",
        "category": "DS",
    },
    {
        "question": "Which of these is a mammal?",
        "options": {"A": "Shark", "B": "Frog", "C": "Dolphin", "D": "Eagle"},
        "answer": "C",
        "category": "Biology",
    },
    {
        "question": "Which country hosts the city of Varanasi?",
        "options": {"A": "Nepal", "B": "India", "C": "Sri Lanka", "D": "Bangladesh"},
        "answer": "B",
        "category": "GK - India",
    },
    {
        "question": "What is the keyword to define a function in Python?",
        "options": {"A": "func", "B": "define", "C": "def", "D": "lambda"},
        "answer": "C",
        "category": "Python",
    },
    {
        "question": "Which river is the longest in the world?",
        "options": {"A": "Nile", "B": "Amazon", "C": "Yangtze", "D": "Ganga"},
        "answer": "A",
        "category": "Geography",
    },
    {
        "question": "Which file format is used to store images with lossless compression?",
        "options": {"A": "JPEG", "B": "PNG", "C": "MP3", "D": "GIF"},
        "answer": "B",
        "category": "Technology",
    },
    {
        "question": "Which of the following is immutable in Python?",
        "options": {"A": "List", "B": "Set", "C": "Dictionary", "D": "Tuple"},
        "answer": "D",
        "category": "Python",
    },
    {
        "question": "India’s national animal is?",
        "options": {"A": "Lion", "B": "Tiger", "C": "Elephant", "D": "Peacock"},
        "answer": "B",
        "category": "GK - India",
    },
]
random.shuffle(questions)
money=0
def lifeline_50_50(q):
    correct=q["answer"]
    options=list(q["options"].keys())
    options.remove(correct)
    remove=random.sample(options,2)
    print("\n 50-50 Lifeline Applied! Remaining options:")
    for key,value in q["options"].items():
        if key not in remove:
            print(f"{key}.{value}")

def lifeline_phoneFriend(q):
    print("\n📞Your friend suggest the correct answer is",q["answer"])
def Aud_Poll(q):
    print("\n📊 Audience Poll Results:")
    correct=q["answer"]
    votes={k:random.randint(0,30) for k in q["options"].keys()}
    votes[correct] += random.randint(40,60)
    for k,v in votes.items():
        print(f"{k}: {v}%")


for i, q in enumerate(questions,start=1):
    print(f"\nQ{i}:{q['question']}")
    for key,value in q["options"].items():
        print(f"{key}.{value}")

    while True:
        ans =input("Choose your answers from options (A/B/C/D), L for Lifeline, or Q for quit:  ").upper()
        if ans =="L":
            if lifelines["50-50"] and lifelines["phone a friend"] and lifelines["audience poll"]==False:
                print("all Lifeline have used..")
            print("\nAvailable Lifelines:")
            for name,available in lifelines.items():
                if available:
                    print(f"- {name}")
            choice=input("choose a lifeline: ").lower()
            if choice=="50-50" and lifelines["50-50"]:
                lifeline_50_50(q)
                lifelines["50-50"]=False
            elif choice=="phone a friend" and lifelines["phone a friend"]:
                lifeline_phoneFriend(q)
                lifelines["phone a friend"]=False
            elif choice=="audience poll" and lifelines["audience poll"]:
                Aud_Poll(q)
                lifelines["audience poll"]=False
            else:
                print("❌Invalid choice or Lifeline already used.")
            continue
        if ans=="Q":
            print("you Quit the game with money :",money)
            exit()
        if ans==q["answer"]:
            print("✅ Correct Answer!")
            money=Money_Ladder[i]
            print(f"You won  ₹{money}")
            break
        else:
            print("❌ You choose the wrong answer! Game Over")
            print(f"You have Won ₹{money}")
            exit()





