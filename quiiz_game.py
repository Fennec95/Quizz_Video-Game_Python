import unicodedata

def normaliser_texte(texte):
    """Convertit un texte en minuscule et enlève les accents"""
    texte = texte.lower()
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(c for c in texte if unicodedata.category(c) != 'Mn')
    return texte

def poser_question(question, reponse_attendue):
    """Pose une question avec un maximum de 3 essais """
    tentatives = 0
    while tentatives < 3:
        answer = input(question + " ")
        answer_normalise = normaliser_texte(answer)

        if answer_normalise == reponse_attendue:
            print("✅ Correct !\n")
            return True  # La question a été réussie
        else:
            tentatives += 1
            essais_restants = 3 - tentatives
            if essais_restants > 0:
                print(f"❌ Incorrect... Il te reste {essais_restants} essai(s).")
            else:
                print("💀 Game Over !\n")
                return False  # Fin du jeu

def lancer_quiz():
    """Lance le quiz et gère la boucle de réessai"""
    print("🎮 Bienvenue à mon quiz !")

    while True:
        jeu = input("Veux-tu jouer ? [y/n] ").lower()
        if jeu == "y":
            print("Cool, c'est parti !\n")
            break
        elif jeu == "n":
            print("D'accord, une prochaine fois !")
            quit()
        else:
            print("❗ Y ou N, c'est pas compliqué !")

    # Liste des questions et réponses attendues
    questions = [
        ("Comment s'appelle ton personnage dans Elden Ring ?", "un sans eclat"),
    ("Comment s'appelle le jeu où un samouraï affronte Khotun Khan ?", "ghost of tsushima"),
    ("Comment s'appelle la première map zombie de Call of Duty : Black Ops ?", "kino der toten"),
    ("Dans quel jeu incarne-t-on Link pour sauver la princesse Zelda ?", "the legend of zelda"),
    ("Quel studio a développé The Witcher 3 ?", "cd projekt red"),
    ("Quel est le nom du tueur masqué dans Resident Evil 3 ?", "nemesis"),
    ("Comment s'appelle l'île où se déroule Far Cry 3 ?", "rook island"),
    ("Quel est le prénom du personnage principal de Red Dead Redemption 2 ?", "arthur morgan"),
    ("Dans quel jeu de survie devez-vous affronter des mutants cannibales sur une île après un crash d’avion ?", "the forest"),
    ("Quel est le nom du protagoniste de la série God of War ?", "kratos"),
    ("Comment s'appelle l'héroïne de Horizon Zero Dawn ?", "aloy"),
    ("Dans quel jeu incarne-t-on un chasseur de monstres dans un monde peuplé de créatures géantes ?", "monster hunter"),
    ("Comment s'appelle l'entreprise maléfique dans la saga Resident Evil ?", "umbrella corporation"),
    ("Dans quel jeu de Nintendo peut-on attraper des créatures et les faire combattre ?", "pokemon"),
    ("Quel est le nom du plombier emblématique de Nintendo ?", "mario")
    ("Dans quel jeu incarne-t-on un soldat nommé Master Chief ?", "halo"),
    ("Quel est le nom du scientifique fou dans Half-Life ?", "g-man"),
    ("Comment s'appelle le tueur en série masqué dans Dead by Daylight inspiré de Halloween ?", "michael myers"),
    ("Dans quel jeu de Rockstar Games incarne-t-on un gangster nommé Tommy Vercetti ?", "gta vice city"),
    ("Quel est le nom du mode de jeu ultra difficile dans Dark Souls ?", "new game plus"),
    ("Comment s'appelle le célèbre plombier rival de Mario, vêtu de vert ?", "luigi"),
    ("Dans quel jeu affronte-t-on des animatroniques effrayants dans une pizzeria ?", "five nights at freddy's"),
    ("Quel est le nom du personnage principal dans Metal Gear Solid ?", "solid snake"),
    ("Dans quel jeu doit-on construire des tours de défense pour empêcher des zombies d'attaquer un jardin ?", "plants vs zombies"),
    ("Quel est le nom du jeu où l’on incarne un chevalier en 2D avec une pelle ?", "shovel knight")
    ("Quel est le nom du héros dans la série de jeux Uncharted ?", "nathan drake"),
    ("Dans quel jeu doit-on résoudre des énigmes en manipulant des cubes colorés ?", "portal"),
    ("Comment s'appelle le jeu de survie où l'on doit collecter des ressources pour construire et survivre sur une île ?", "ark survival evolved"),
    ("Dans quel jeu de course automobile peut-on conduire des véhicules dans des courses de type arcade ?", "burnout"),
    ("Quel est le nom du premier jeu de la saga The Elder Scrolls ?", "arena"),
    ("Dans quel jeu incarne-t-on un rat qui rêve de devenir un grand chef ?", "ratatouille"),
    ("Quel est le nom de la ville fictive où se déroule l’action de la série de jeux vidéo Assassin's Creed ?", "jerusalem"),
    ("Dans quel jeu de stratégie temps réel incarne-t-on des marines spatiaux contre des extraterrestres ?", "starcraft"),
    ("Quel est le nom du jeu où un petit robot doit nettoyer un monde en détruisant des objets ?", "wall-e"),
    ("Dans quel jeu incarne-t-on un personnage appelé 'Geralt de Riv' ?", "the witcher")
    ]

    score = 0  # Score de bonnes réponses

    # Boucle sur les questions
    for question, reponse in questions:
        if poser_question(question, reponse):
            score += 1  # Augmente le score si la question est réussie
        else:
            print(f"💀 Fin du jeu. Tu as réussi {score}/{len(questions)} questions.")
            return  # Retourne au menu principal

    # Si toutes les questions sont passées avec succès
    print(f"🎉 Félicitations ! Tu as fini le quiz avec {score}/{len(questions)} bonnes réponses ! 🎉")

while True:  # Boucle principale pour réessayer
    lancer_quiz()
    
    # Demande si l'utilisateur veut rejouer
    while True:
        retry = input("🔄 Veux-tu réessayer ? [y/n] ").lower()
        if retry == "y":
            print("\n🔁 Redémarrage du quiz...\n")
            break  # Relance `lancer_quiz()`
        elif retry == "n":
            print("\n👋 Merci d'avoir joué ! À bientôt !")
            quit()
        else:
            print("❗ Y ou N, c'est pas compliqué !")
