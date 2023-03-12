import polinomio
import sys
import helpers
import os

def menu():
    while True:
        helpers.limpiar_pantalla()

        print("=============================")
        print("      Menú de polinomios     ")
        print("=============================")
        print("      1. Sumar polinomios    ")
        print("      2. Restar polinomios   ")
        print("   3. Multiplicar polinomios ")
        print("      4. Dividir polinomios  ")
        print("      5. Evaluar polinomios  ")
        print("      6. Crear polinomio     ")
        print("       7. Salir              ")
        print("=============================")

        opcion = input("Seleccione una opción: ")

        if opcion==1:
            helpers.limpiar_pantalla()
            print("Has elegido sumar polinomios")
            print("¿Qué polinomios quieres sumar?")
            

            