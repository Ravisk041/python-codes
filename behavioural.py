from shared import responses
def Behavioral_Symptoms():
    questions = [
        "Do you find it hard to relax or be still? ",
        "Do you struggle to let go of worries? ",
        "Do you avoid things that cause anxiety? "
    ]
    for q in questions:
        choice = input(q + "(often/sometimes/no): ")
        if choice.lower() == "often":
            responses.append(10)
        elif choice.lower() == "sometimes":
            responses.append(7)
        elif choice.lower() == "no":
            responses.append(5)
        else:
            print("Invalid choice. Answer skipped.")