titre = "Le Pierre national"
message = "J'apporte la modification"
print(titre, message)
a = 2
b = 12
c = a + b
print(c)
print("Ca va ? ")
valeur = str(input())
if valeur == "y":
    print("ok cool")
elif valeur == "n":
    print("qu'est-ce qui va pas bro ?")
else:
    print("réponds bro")

print("Quel est ton chiffre pref ?")
chiffre = int(input())
if chiffre != 3:
    print("m'en fous")
else:
    print("MAIS NON COMME MOI")

print("Est-tu Eric Zemmour ?")
eric = bool(input())
if eric:
    print("ba t pas gentil")
else:
    print("bravo comme christine")