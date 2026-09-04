def res_enrutamiento():
    # Número de rutas
    n = int(input().strip())
    rutas = []

    
    for _ in range(n):
        linea = input().strip().split()
        rutas.append((linea[0], linea[1]))  # linea[0] es el path ("/user/:id")
                                            # linea[1] es el contenido base ("UserPage")
        
    # Número de transiciones
    m = int(input().strip())
    
    for _ in range(m):
        transicion = input().strip()
        trans_partes = transicion.split('/')
        
        encontrado = False
        
        for ruta, contenido in rutas:
            ruta_partes = ruta.split('/')
            
            if len(ruta_partes) == len(trans_partes):
                coincide = True
                parametros = []
                
                # Comparando segmentos
                for r, t in zip(ruta_partes, trans_partes):
                    if r.startswith(':'):
                        # Es un parámetro si el segmento de la ruta empieza con :
                        parametros.append(t)
                    elif r != t:
                        # Se descarta esta ruta
                        coincide = False
                        break

                if coincide:
                    encontrado = True
                    if parametros:
                        # Añade los parámetros después del contenido
                        print(f"{contenido} {' '.join(parametros)}")
                    else:
                        print(contenido)
                    break
                    
        # Luego revisar las rutas y ninguna coincide
        if not encontrado:
            print("404 Not Found")

# Comando para ejecutar "powershell"
# Get-Content entradaP1.txt | python Problema1.py

if __name__ == '__main__':
    res_enrutamiento()