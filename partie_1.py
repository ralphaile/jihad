# Initialisation des variables 

capital = 8000 # en dollars
nb_jours = 72 # en jours
taux_annuel = 0.065# pourcentage / 100 

# Calcul du taux périodique 
taux_periodique=taux_annuel/365

# Calcul des intérêts 
interets=capital*taux_periodique*nb_jours

# Calcul de la valeur acquise
valeur_acquise=capital+interets

# Affichage des interets et de la valeur acquise 
print(f"Les intérêts gagnés après {nb_jours} jours sont : \n{interets}\nLa valeur_acquise après {nb_jours} jours est: \n{valeur_acquise}")
