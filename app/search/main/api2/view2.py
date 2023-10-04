from bs4 import BeautifulSoup
import requests

def find_pages_with_text(text):
  """
  Encuentra todas las páginas web que incluyen un texto determinado.

  Args:
    text: El texto que se buscará.

  Returns:
    Una lista de URLs de las páginas que incluyen el texto.
  """

  # Realiza una búsqueda de Google con el texto especificado.
  response = requests.get("https://www.google.com/search?q=" + text)
  soup = BeautifulSoup(response.text, "html.parser")

  # Encuentra todos los elementos `a` (enlaces) en la página.
  a_elements = soup.find_all("a")

  # Crea una lista de URLs de las páginas que incluyen el texto.
  result_links = []
  for a_element in a_elements:
    # Si el texto se encuentra en el texto o el atributo `href` del enlace,
    # lo agregamos a la lista de resultados.
    if text in a_element.text or text in a_element["href"]:
      result_links.append(a_element["href"])

  return result_links


print(find_pages_with_text("vitales no disponibles"))
