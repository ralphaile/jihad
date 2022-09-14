# Initialisation des variables 
capital_initial=2600
taux_annuel1=0.045
taux_annuel2=0.1
frais2=60

# Calcul du montant du capital avec le premier placement au 100ème jour de l'année 
C1=capital_initial+capital_initial*(taux_annuel1/365)*100
# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année 
C2=capital_initial-60+(capital_initial-60)*(taux_annuel2/365)*300
# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le premier
c1=0
c2=0
nb_jours=0
while(c1>=c2):
    c1=capital_initial+capital_initial*(taux_annuel1/365)*nb_jours
    c2=capital_initial-60+(capital_initial-60)*(taux_annuel2/365)*nb_jours
    nb_jours+=1
# Affichage des valeurs calculées
print(f"Montant du capital avec le premier placement au 100ème jour :\n{C1}")
print(f"Montant du capital avec le deuxième placement au 300ème jour :\n{C2}")
print(f"Jour à partir duquel le deuxième placement rapport plus que le premier:\n{nb_jours-1}")