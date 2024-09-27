# Extracción de Palabras Clave en Páginas Web

## Descripción

Este proyecto tiene como objetivo extraer palabras clave específicas de varias páginas web de manera automatizada. El script hace uso de la librería `requests` para obtener el contenido HTML de cada página y de `BeautifulSoup` para analizar y extraer el texto visible de dicho contenido. En particular, el código busca una palabra clave en un conjunto de URLs y verifica si está presente en cada una de ellas. Si la palabra es encontrada, se imprime un mensaje indicando que se ha localizado en la URL correspondiente.

## Funcionamiento

El código itera a través de un rango de URLs que siguen una estructura similar, modificando el número de la página en cada iteración. Por ejemplo, accede a URLs como `http://www.soria-goig.org/fuentesymanantialesdesoria/ftes0015.htm`, `http://www.soria-goig.org/fuentesymanantialesdesoria/ftes0016.htm`, y así sucesivamente. Para cada página, el script:

1. Envía una solicitud HTTP para obtener el contenido HTML de la página.
2. Si la respuesta es exitosa (código de estado 200), analiza el HTML usando `BeautifulSoup` y extrae todo el texto visible de la página.
3. Busca si la palabra clave (en este caso, "habilitado") está presente en el texto extraído.
4. Imprime un mensaje indicando si la palabra ha sido encontrada en la URL correspondiente.
5. En caso de error o si la página no está accesible, muestra un mensaje informando el problema.

## Ejemplo de uso

Imagina que necesitas buscar la palabra **"habilitado"** en un conjunto de páginas web que siguen un formato numérico en su URL. Este script recorrerá esas páginas y te dirá en cuáles de ellas se encuentra la palabra. Podrías modificar el script para buscar diferentes palabras clave o cambiar el rango de páginas según sea necesario.

### Ejecución del script

Para ejecutar el script, solo necesitas tener Python y las librerías `requests` y `BeautifulSoup` instaladas. Puedes instalar las dependencias ejecutando:

```bash
pip install requests beautifulsoup4
```

Luego, puedes ejecutar el código en tu entorno local:

```bash
python nombre_del_script.py
```

## **Aplicación en Ingeniería de Datos**

**Este tipo de scripts puede ser de gran utilidad en el campo de la Ingeniería de Datos. La capacidad de automatizar la extracción de texto de páginas web es especialmente relevante cuando se trabaja con datos no estructurados (como el contenido HTML). En este caso, el script podría servir para recolectar datos de texto clave, hacer análisis de contenido o incluso para alimentar procesos de ETL (Extract, Transform, Load). Automatizar la ingesta de datos desde diferentes fuentes web es una tarea crítica en proyectos que requieren el procesamiento de información a gran escala, como en el scraping de noticias, revisiones de productos, monitoreo de sitios web y análisis de tendencias. Además, al permitir búsquedas de palabras clave, se puede utilizar este código para clasificar o filtrar contenido en función de criterios específicos, mejorando la eficiencia de las operaciones de datos.**

## Consideraciones

1. **Manejo de Errores:** El script incluye un manejo básico de errores. Si la página no se puede acceder, se imprime un mensaje de error. Sin embargo, sería recomendable extender el manejo de errores para situaciones como tiempos de espera excesivos o errores de conexión.
   
2. **Modificabilidad:** El script es fácilmente modificable para adaptarse a otros rangos de páginas web o palabras clave, lo que lo hace muy flexible para diferentes casos de uso.

3. **Requisitos del Entorno:** Es necesario contar con conexión a Internet para que el script pueda acceder a las URLs. Asegúrate de tener instaladas las dependencias mencionadas.

