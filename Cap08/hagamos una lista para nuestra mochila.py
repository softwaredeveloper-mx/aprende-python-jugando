mochila = ["linterna", "manta", "botella de agua"]

def mostrar_mochila():
    print("Tu mochila contiene:")
    for item in mochila:
        print(f"- {item}")

def agregar_a_mochila(item):
    mochila.append(item)
    print(f"{item} ha sido agregado a tu mochila.")

mostrar_mochila()
agregar_a_mochila("mapa")
mostrar_mochila()
