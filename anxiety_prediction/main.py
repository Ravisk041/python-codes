from shared import responses
from modules import Cognitive_Symptoms
from Physical import physical_sympotoms
from behavioural import Behavioral_Symptoms

Cognitive_Symptoms()
physical_sympotoms()
Behavioral_Symptoms()
score = sum(responses)
count= len(responses)
total_score=score/count # calculate total score
print("Total score:", total_score)

if 8 <= total_score <= 10:
    print("High anxiety")
elif 5 <= total_score <= 8:
    print("Moderate anxiety")
else:
    print("Low anxiety")
