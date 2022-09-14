# Initilisation des variables 
C=300000

# Calcul du capital au bout de 20 années 
for i in range(20):
    C=C+C*0.08

# Affichage du capital au bout de 20 années
print(f"Capital au bout de 20 années : {C}")