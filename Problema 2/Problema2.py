import sys
from collections import defaultdict

def res_banco():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
        
    n = int(entrada[0])
    m = int(entrada[1])
    s = int(entrada[2])
    
    idx = 3
    
    # Diccionario para mapear terminales a socios
    terminal_a_socio = {}
    for _ in range(m):
        p = int(entrada[idx])
        t = int(entrada[idx+1])
        terminal_a_socio[t] = p
        idx += 2
        
    # Diccionario para contar compras por socio y cliente
    compras_por_socio = defaultdict(lambda: defaultdict(int))
    for _ in range(s):
        c = int(entrada[idx])
        t = int(entrada[idx+1])
        
        # Si el terminal corresponde a un socio se suma la compra al cliente correspondiente
        if t in terminal_a_socio:
            p = terminal_a_socio[t]
            compras_por_socio[p][c] += 1
            
        idx += 2
        
    # Evaluar los resultados de cada socio (1 hasta N)
    for p in range(1, n + 1):
        mejor_cliente = -1
        max_compras = -1
        
        if p in compras_por_socio:
            for cliente, cantidad in compras_por_socio[p].items():
                if cantidad > max_compras:
                    max_compras = cantidad
                    mejor_cliente = cliente
                elif cantidad == max_compras:
                    # Si hay empate, se elige el cliente con menor número
                    if mejor_cliente == -1 or cliente < mejor_cliente:
                        mejor_cliente = cliente
                        
        print(f"{p} {mejor_cliente}")

# Comando para ejecutar 
# Get-Content entradaP2.txt | python Problema2.py

if __name__ == '__main__':
    res_banco()