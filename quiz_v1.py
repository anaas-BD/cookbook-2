import json
import random
import tkinter as tk
from tkinter import StringVar

with open('quiz.json', 'r') as file:
        data = json.load(file)


def afficher_question_aleatoire():
    
    # Sélectionne une question aléatoire
    question_aleatoire = random.choice(data)

    # Affiche la question
    print("Question:", question_aleatoire["questions-cap"])
    
    # Affiche les options de réponse
    print("Options de réponse:")
    for i, option in enumerate(question_aleatoire["choix_reponses-cap"], start=1):
        print(f"{i}. {option}")

# Exemple d'utilisation
afficher_question_aleatoire()
