import random

liste = []
  # 1. Saisie des noms
noms = [input(f"Étudiant {i+1} : ").strip().capitalize() 
        for i in range(int(input("Nombre d'étudiants : ")))]


# La repartition
print("")
print("1.Repartition aleatoire")
print("2.Repartition par niveau")
print("3.Repartition par besoin")
repartition = int(input("Veuillez choisir le type de repartition : "))

match repartition:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("Choix invalide")


# Le nombre de membre par gorupe
print("")
nbr_etudiant = max(2, int(input("Nombre d'etudiant par groupes (min 2) : ")))


nbr_groupe = (len(liste) / nbr_etudiant)
print(nbr_groupe)



# Repartition aleatoire
print("")
random.shuffle(noms)

groupes = [noms[i:i+2] for i in range(0, len(noms), nbr_etudiant)]

for i, groupe in enumerate(groupes, 1):
    print(f"Groupe {i}: {', '.join(groupe)}")

print("")



# Repartition par niveau
def former_groupes():    
    
    # 2. Création des groupes
    groupes = []
    restants = sorted(noms, key=lambda x: x[0])
    
    while restants:
        groupe = []
        for nom in restants[:]:
            if not any(nom[0] == g[0] for g in groupe):
                groupe.append(nom)
                restants.remove(nom)
                if len(groupe) == nbr_etudiant:
                    break
        groupes.append(groupe)
    
    # 3. Fusion des petits groupes
    for g in groupes[:]:
        if len(g) < 2:
            for autre in groupes:
                if autre != g and all(g[0][0] != m[0] for m in autre):
                    autre.extend(g)
                    groupes.remove(g)
                    break
    
    # 4. Affichage
    print("\nGroupes :")
    for i, g in enumerate(groupes, 1):
        print(f"Groupe {i}: {', '.join(g)}")

# Lancement
#former_groupes()



#print(liste)