import fibonacci
import time

inicio = time.time() 
fibonacci.caso1
tiempo_caso1 = inicio-time.time()

inicio = time.time() 
fibonacci.caso2
tiempo_caso2 = inicio-time.time()

if tiempo_caso1>tiempo_caso2:
    print("Es mejor el caso 2")
else: 
    print("Es mejor el caso 1")