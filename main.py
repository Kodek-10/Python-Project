import random
from fpdf import FPDF

def saisir_etudiants():
    """Saisie des noms des étudiants"""
    nbr = int(input("Nombre d'étudiants : "))
    return [input(f"Étudiant {i+1} : ").strip().capitalize() 
            for i in range(nbr)]

def choisir_repartition():
    """Menu de choix de répartition"""
    print("\nTypes de répartition :")
    print("1. Aléatoire")
    print("2. Par niveau (ordre alphabétique)")
    print("3. Par besoin")
    return int(input("Votre choix (1-3) : "))

def repartition_aleatoire(noms, taille_groupe):
    """Répartition aléatoire des étudiants"""
    random.shuffle(noms)
    return [noms[i:i+taille_groupe] 
            for i in range(0, len(noms), taille_groupe)]

def repartition_par_niveau(noms, taille_groupe):
    """Répartition avec initiales différentes"""
    noms_tries = sorted(noms, key=lambda x: x[0])
    groupes = []
    
    while noms_tries:
        groupe = []
        for nom in noms_tries[:]:
            if not any(nom[0] == g[0] for g in groupe):
                groupe.append(nom)
                noms_tries.remove(nom)
                if len(groupe) == taille_groupe:
                    break
        groupes.append(groupe)
    
    return groupes

def generer_pdf(groupes):
    """Génération du PDF"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Groupes d'étudiants", 0, 1, 'C')
    
    for i, groupe in enumerate(groupes, 1):
        pdf.cell(0, 10, f"Groupe {i}: {', '.join(groupe)}", 0, 1)
    
    pdf.output("groupes.pdf")
    print("\nRésultats exportés dans groupes.pdf")

def main():
    # 1. Saisie des données
    noms = saisir_etudiants()
    taille_groupe = max(2, int(input("Nombre d'étudiants par groupe (min 2) : ")))
    
    # 2. Choix de la répartition
    choix = choisir_repartition()
    
    # 3. Application de la répartition
    if choix == 1:
        groupes = repartition_aleatoire(noms, taille_groupe)
    elif choix == 2:
        groupes = repartition_par_niveau(noms, taille_groupe)
    elif choix == 3:
        print("Option non implémentée - Utilisation de la répartition aléatoire")
        groupes = repartition_aleatoire(noms, taille_groupe)
    else:
        print("Choix invalide - Utilisation de la répartition aléatoire")
        groupes = repartition_aleatoire(noms, taille_groupe)
    
    # 4. Affichage et export
    print("\nGroupes formés :")
    for i, groupe in enumerate(groupes, 1):
        print(f"Groupe {i}: {', '.join(groupe)}")
    
    generer_pdf(groupes)

if __name__ == "__main__":
    main()