def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat et retourner celle-ci avec le mot-clé return.

    if n % 3 == 0 and n % 5 == 0:
        resultat = "fizzbuzz"
    elif n % 3 == 0:
        resultat = "fizz"
    elif n % 5 == 0:
        resultat = "buzz"
    else:
        resultat = n
    print(resultat)
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    fizzBuzz(n)
