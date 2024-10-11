 # Joaquin Molina Vargas 
import requests
import sys
import getopt
import time

# Función para buscar el fabricante de una dirección MAC
# Esta función toma como parámetro una dirección MAC, realiza una consulta a una API
# pública y luego imprime el fabricante asociado a la dirección MAC y el tiempo de respuesta.
def buscar_fabricante(mac):
    print(f"Consultando fabricante para MAC: {mac}")
    # URL de la API pública para obtener información de la MAC
    url = f'https://api.maclookup.app/v2/macs/{mac}'
    try:
        # Inicio del temporizador para calcular el tiempo de respuesta
        inicio = time.time()
        # Solicitud a la API
        respuesta = requests.get(url)
        # Calcula el tiempo de respuesta en milisegundos
        tiempo_respuesta = int((time.time() - inicio) * 1000)
        
        # Verifica si la respuesta fue exitosa (código 200)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Obtiene el fabricante de la respuesta JSON; si no está, muestra 'Not found'
            fabricante = datos.get('company', 'Not found')
            if not fabricante:  # Verifica si el valor es vacío o None
                fabricante = 'Not found'
            # Imprime la dirección MAC, el fabricante y el tiempo de respuesta
            print(f'MAC address : {mac}')
            print(f'Fabricante      : {fabricante}')
            print(f'Tiempo de respuesta {tiempo_respuesta}ms')
        else:
            # Muestra "Not found" si el estado de respuesta no es 200
            print(f'MAC address : {mac}')
            print('Fabricante     : Not found')
            print(f'Tiempo de respuesta {tiempo_respuesta}ms')
    except Exception as e:
        # Manejo de errores en caso de que ocurra una excepción durante la solicitud
        print(f"Error: {e}")

# Función para mostrar una tabla simulada de direcciones MAC y sus fabricantes
# Esta función imprime una tabla con algunas direcciones MAC de ejemplo y sus respectivos fabricantes.
def mostrar_tabla_arp():
    print("Mostrando tabla ARP simulada...")
    # Diccionario que simula una tabla ARP con direcciones MAC y sus fabricantes
    tabla_arp = {
        '00:01:97:bb:bb:bb': 'cisco',
        'b4:b5:fe:92:ff:c5': 'Hewlett Packard',
        '00:E0:64:aa:aa:aa': 'Samsung',
        'AC:F7:F3:aa:aa:aa': 'Xiaomi'
    }
    print("MAC/Vendor:")
    # Itera sobre cada elemento del diccionario e imprime la MAC y el fabricante
    for mac, fabricante in tabla_arp.items():
        print(f'{mac} / {fabricante}')

# Función principal que procesa los argumentos de línea de comandos y ejecuta las funciones correspondientes
# La función analiza los parámetros pasados por la línea de comandos, como --mac, --arp, y --help
# y llama a las funciones respectivas para procesar las solicitudes.
def main():
    print("Ejecutando script OUILookup...")
    # Obtiene los argumentos pasados en la línea de comandos, excluyendo el nombre del archivo
    argumentos = sys.argv[1:]
    # Define los parámetros que se aceptan
    opciones_largas = ["mac=", "arp", "help"]
    
    try:
        # Analiza los argumentos de línea de comandos usando getopt
        opts, args = getopt.getopt(argumentos, "", opciones_largas)
    except getopt.GetoptError:
        # Muestra un mensaje de ayuda si se produce un error en el análisis de argumentos
        print('Uso: python OUILookup.py --mac <direccion_mac> | --arp | --help')
        sys.exit(2)
    
    # Itera sobre los argumentos y ejecuta la acción correspondiente
    for opt, arg in opts:
        if opt == "--mac":
            # Llama a la función de búsqueda de fabricante con la dirección MAC proporcionada
            buscar_fabricante(arg)
        elif opt == "--arp":
            # Muestra la tabla ARP simulada
            mostrar_tabla_arp()
        elif opt == "--help":
            # Imprime un mensaje de ayuda
            print('Uso: python OUILookup.py --mac <direccion_mac> | --arp | --help')
            sys.exit()

# Verifica que el script se esté ejecutando directamente y llama a la función principal
if __name__ == "__main__":
    main()
