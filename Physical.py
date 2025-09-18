from shared import responses
def physical_sympotoms():
    questions = [
        "Do you experience rapid heartbeat or palpitations? ",
        "Do you have sweating, trembling, or shaking? ",
        "Do you feel trouble catching your breath or dizziness? ",
        "Do you have nausea or abdominal distress? ",
        "Do you often have muscle tension? "
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
