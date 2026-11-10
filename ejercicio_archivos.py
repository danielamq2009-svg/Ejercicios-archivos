
ruta_file = "/Users/danimeza/Documents/Daniela Software/Archivos/mbox.txt"
ruta_from = "/Users/danimeza/Documents/Daniela Software/Archivos/envios.txt"

with open(ruta_file, "r", encoding="utf-8") as file, open(ruta_from, "w", encoding="utf-8") as enviados:

    correos = set()

    for linea in file:
        if linea.startswith("From:"):
            correos.add(linea.split()[1])

    correos = list(correos)

    for correo in reversed(correos):
        mensaje = correo + " enviado [ok]\n"
        print(mensaje, end="")
        enviados.write(mensaje)