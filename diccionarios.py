diccionario ={1:'Hola', 
              2:"Mundo", 
              3:"Desde",
              "cuatro":"diccionario"}

print(type(diccionario))

print(diccionario["cuatro"])

for keys in diccionario:
    print(f"""llave{keys}:valor-{diccionario[keys]}""")


for keys,value in diccionario.items():
    print(f"""llave{keys}:valor-{value}""")


persona = {}

persona["nombre"]="Luis"
persona["apellido"]="Ley"
persona["edad"]=21
persona["edad"]=22
persona["correo"]="luis008m@hotmail.com"

for datos,value in persona.items():
    print(f"""{datos}-{value}""")

if "correo" in persona:
    print(f"""El correo es {persona["correo"]}""")
else:
    print("No tiene correo")

if persona.get("altura")==None:
    persona["altura"]="1.80mts"


print(persona.get("altura"))