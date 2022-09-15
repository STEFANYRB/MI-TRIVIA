RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[39m'
import time
import random
puntaje = random.randint(0,10)
iniciar_trivia = True
intentos = 0
print("Hello World!")
print (YELLOW+"Bienvenido a mi trivia sobre licencias de construccion"+RESET)
print (YELLOW+"Pondremos a prueva tus conocimientos"+RESET)
print("Tienes", puntaje, "puntos")
nombre = input("Ingrese su nombre:")
while iniciar_trivia == True:
 intentos += 1
 puntaje = 0
 print("\nIntento número:", intentos)
 input("Presiona Enter para continuar") 
 print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n") 
#pregunta 1
 time.sleep(2)
 print (GREEN+"\n1) ¿Que procedimiento administrativo otorga la licencia de construccion para edificaciones de vivienda menores de 120m2?"+RESET)
 print ("a) Licencia modalidad A")
 print ("b) Licencia modalidad B")
 print ("c) Licencia modalidad C")
 print ("d) Ninguno")
#respuesta 1
 respuesta_1 = input("\nTu respuesta:")
 while respuesta_1 not in ("a","b","c","d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente:")
 if respuesta_1 == "b":
  print("Incorrecto!", nombre,"La licencia modalidad B es para edificaciones mayores de 120m2")
  puntaje = puntaje - 2
 elif respuesta_1 =="c":
  print("Incorrecto!", nombre, "La licencia modalidad C es para edificaciones de indole comercial")
  puntaje = puntaje - 4
 elif respuesta_1 =="d":
  print("Incorrecto!", nombre, "sigue intentandolo!")
  puntaje = puntaje - 4
 else:
  puntaje +=10
  print ("Muy bien!", nombre,"!")
 print("llevas", puntaje, "puntos")
#pregunta 2
 time.sleep(2)
 print (GREEN+"\n2) ¿Que procedimiento administrativo otorga la licencia de construccion para una edificacion de vivienda de 200m2?"+RESET)
 print ("a) Licencia modalidad A")
 print ("b) Licencia modalidad B")
 print ("c) Licencia modalidad C") 
#respuesta 2
 respuesta_2 = input("Tu respuesta:")
 while respuesta_2 not in ("a","b","c","x"):
  respuesta_2 = input("Debes responder a,b o c. Ingresa nuevamente:")
 if respuesta_2 == "x":
  print("Alto!", nombre, "este es un mensaje secreto")
 elif respuesta_2 == 'a':
  print("Incorrecto!", nombre, "La licencia modalidad A es para edificaciones menores de 120m2")
  puntaje = puntaje - 1
 elif respuesta_2 == "c":
  print("Incorrecto!", nombre, "La licencia modalidad C es para edificaciones de indole comercial")
  puntaje = puntaje - 1
 else:
  puntaje +=10
  print ("Muy bien!", nombre,"!")
 print("llevas", puntaje, "puntos")

  #pregunta 3
 time.sleep(2)
 print(GREEN+"\n3) ¿Que procedimiento administrativo otorga la licencia de construccion para un cerco perimetrico menor de 20ml?"+RESET)
 print ("a) Licencia modalidad A")
 print ("b) Licencia modalidad B")
 print ("c) Ninguno")
   #respuesta 3
 respuesta_3 = input("Tu respuesta:")
 while respuesta_3 not in ("a","b","c"):
  respuesta_3 = input("Debes responder a,b,c o d. Ingresa nuevamente:")
 if respuesta_3 == "a":
  print("Incorrecto, puedes hacerlo mejor...")
  puntaje = puntaje - 5
 elif respuesta_3 == "b":
  print("...!", nombre, "La licencia modalidad B es para edificaciones de vivienda")
  puntaje = puntaje - 3
 else:
  puntaje = puntaje * 3
  print ("Muy bien..!", nombre,"!")
 print("Excelente, llevas", puntaje, "puntos")
 print(RED+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
 repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
 if repetir_trivia != "si": 
  print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
  iniciar_trivia = False