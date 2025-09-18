from shared import responses
def Cognitive_Symptoms():
    question=[ 
        "Do you experience persistent and excessive worry about everyday things? ",
        "Do you often feel tense, restless, or on edge? ",
        "Do you feel a sense of impending danger, panic, or doom? ",
        "Do you find it difficult to concentrate or make decisions? ",
        "Do you overthink and imagine worst-case scenarios? "
        ]
    for q in question:
        choice = input(q + "(often/sometimes/no): ")
        if choice.lower() == "often":
            responses.append(10)
        elif choice.lower() == "sometimes":
            responses.append(7)
        elif choice.lower() == "no":
            responses.append(5)
        else:
            print("Invalid choice. Answer skipped.")





    