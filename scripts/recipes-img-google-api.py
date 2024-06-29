# Definir las variables
api_key = 'AIzaSyD4aPp9PC-lpHL87Eng90Ckjj8lA0xLD44'
search_engine_id = '822ed65bb7bb74597'
# https://www.googleapis.com/customsearch/v1?key=AIzaSyD4aPp9PC-lpHL87Eng90Ckjj8lA0xLD44&cx=822ed65bb7bb74597&q=manzana&searchType=image

import os
import requests
import urllib.parse
from slugify import slugify

# Listado de recetas
recetas = [
    "pan blanco recipe",
    "tarta de manzana recipe",
    "paella recipe",
    # Agrega más recetas según sea necesario
]

# Carpeta donde se guardarán las imágenes
output_folder = '../img-recetas/'

# Función para obtener la URL de la imagen desde Google
def get_img_url(query):
    # Formatear la consulta para la API de Google
    search_query = urllib.parse.quote(query)

    # URL de la API de búsqueda de Google (general search)
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={search_query}&searchType=image'

    # Realizar la solicitud a la API de Google
    response = requests.get(url)
    data = response.json()

    # Obtener la URL de la primera imagen encontrada
    if 'items' in data and len(data['items']) > 0:
        img_url = data['items'][0]['link']
        return img_url
    else:
        return None

# Función para descargar la imagen y guardarla en la carpeta de salida
def download_image(url, output_folder):
    try:
        # Obtener el nombre del archivo de la URL de la imagen
        img_name = url.split('/')[-1]
        img_path = os.path.join(output_folder, img_name)

        # Descargar la imagen y guardarla en el archivo
        response = requests.get(url)
        with open(img_path, 'wb') as f:
            f.write(response.content)

        return img_path  # Devolver la ruta donde se guardó la imagen
    except Exception as e:
        print(f"Error al descargar la imagen: {e}")
        return None

# Probar con cada receta y descargar la imagen si se encuentra
for receta in recetas:
    img_url = get_img_url(receta)
    print(f"Receta: {receta}, {img_url}")
    if img_url:
        print(f"URL de la imagen: {img_url}")
        # Descargar la imagen y mostrar la ruta donde se guardó
        saved_img_path = download_image(img_url, output_folder)
        if saved_img_path:
            print(f"Imagen guardada en: {saved_img_path}")
        else:
            print("Error al guardar la imagen.")
    else:
        print(f"No se encontró una URL de imagen válida para '{receta}'.")
        print(f"URL de la imagen {img_url}")
    print()

