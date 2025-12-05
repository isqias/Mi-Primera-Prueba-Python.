
# Pedimos nombre y lo capitalizamos
nombre = input("Cual es tu nombre? ").capitalize()

# Guardamos la edad como entero
edad = int(input("Cual es tu edad? "))

# Preguntas sobre Python y color favorito
pregunta1 = input("Te gusta aprender Python?? ").lower()
pregunta2 = input("Cual es tu color favorito?? ").lower().capitalize()

# Mensaje según la edad
if edad >= 18:
    print(nombre + " Jaja vaya que eres un adulto curioso 😂🤣")
else:
    print(nombre + ", Eres un mocoso curioseando en Python eh?? jaja 👌")

# Mensaje según si le gusta Python
if pregunta1 == "si":
    print("Me alegra que te guste aprender Python, " + nombre + "!")
else:
    print("Que mal que no te guste aprender Python, " + nombre + " 😢")

# Mensaje sobre el color favorito
print("WOW, en serio tu color favorito es: " + pregunta2 + " ?? que increíble de verdad 🎨")
