import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon = response.json()
        nombre_pokemon = pokemon["name"].capitalize()
        id_pokemon = pokemon["id"]
        habilidades=",".join([habilidad["ability"]["name"]for habilidad in pokemon["abilities"]])
        tipos = ",".join([tipo["type"]["name"] for tipo in pokemon["types"]])
        url_imagen = pokemon["sprites"]["front_default"]
        response_imagen = requests.get(url_imagen)
        img = Image.open(BytesIO(response_imagen.content))
        mostrar_info_pokemon(nombre_pokemon, id_pokemon, tipos, img,habilidades)
    else:
        messagebox.showerror("Error", "Pokemon no encontrado o nombre inválido")
    
def mostrar_info_pokemon(nombre,id_pokemon,tipos,img,habilidades):
    for widget in ventana.winfo_children():
        widget.destroy()
    label_nombre = tk.Label(ventana, text=f"{nombre} (ID: {id_pokemon})",font=("Arial", 20))
    label_nombre.pack(pady=5)
    
    label_tipos =tk.Label(ventana,text=f"Tipos: {tipos}",font=("Arial",14))
    label_tipos.pack(pady=5)
    
    img = img.resize((200,200))#redimensionar la imagen
    img_tk = ImageTk.PhotoImage(img)
    label_imagen = tk.Label(ventana, image=img_tk)
    label_imagen.image = img_tk
    label_imagen.pack(pady=10)
    
    label_habilidades = tk.Label(ventana,text=f"Habilidades: {habilidades}",font=("Arial",14))
    label_habilidades.pack(pady=10)
    
def buscar_pokemon():
    nombre = entry_nombre.get()
    if nombre:
        obtener_pokemon(nombre)
    else:
        messagebox.showwarning("Advertencia, ingrese un nombre de Pokémon")

ventana = tk.Tk()
ventana.title("Buscador de pokemon")
ventana.geometry("400x500")

label_bienvenida = tk.Label(ventana, text="Introduce el nombre de un Pokémon: ",font=("Arial", 14))
label_bienvenida.pack(pady=10)

entry_nombre = tk.Entry(ventana,font=("Arial", 14))
entry_nombre.pack(pady=10)

boton_buscar = tk.Button(ventana,text="Buscar Pokémon",font=("Arial", 14), command=buscar_pokemon)
boton_buscar.pack(pady=10)

ventana.mainloop()
""""-------------------------por archivo json-------------------------
    with open("ditto_data.json","w") as file:
        json.dump(data, file, indent=4)
    print("La información se ha guardado en ditto_data.json")
    
    #-------------------------por consola-------------------------
    nombre = data["name"]
    tipo = [t["type"]["name"] for t in data["types"]]
    habilidades = [h["ability"]["name"] for h in data["abilities"]]

    print(f"Nombre: {nombre}")
    print(f"Tipo: {",".join(tipo)}")
    print(f"Habilidades: {",".join(habilidades)}")"""
