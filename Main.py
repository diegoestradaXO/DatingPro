#Proyceto 2 de Algoritmos y Estructura de Datos
#DatingPro: recomendaciones con graph database usando Neo4J
#Autores:
#Michael Chan 18562 
#Diego Estrada 18540
#Isabel Ortiz 18176

from Database import Database

#Se crea la base de datos
db = Database("bolt://localhost:7687", "neo4j","password")

#Controlador de menu de login
login = True
loginOptions = [1,2,3]
while login:
    try:
        print("""
=========================================================    
    ____        __  _                   ____           
   / __ \____ _/ /_(_)___  ____ _      / __ \_________ 
  / / / / __ `/ __/ / __ \/ __ `/_____/ /_/ / ___/ __ \ 
 / /_/ / /_/ / /_/ / / / / /_/ /_____/ ____/ /  / /_/ /
/_____/\__,_/\__/_/_/ /_/\__, /     /_/   /_/   \____/ 
                        /____/      
=========================================================
                        LOGIN:
                    1. Ingresar
                    2. Registrarse
                    3. Salir
=========================================================                
        """)
        option = input(">> ")
        if(int(option) in loginOptions):
            if(option == "1"):
                user = ""
                while(user == ""): #Programacion defensiva para que agregue el campo obligatorio
                    user = input(">> Nombre de usuario: ")
                password = ""
                while(password == ""): #Programacion defensiva para que agregue el campo obligatorio
                    password = input(">> Contraseña: ")   
                print("Ingresando...") 
                if(len(db.verifyAccount(user,password)) > 0):
                    print("Bienvenido!")
                    logged = True
                    loggedOptions = [1,2,3]
                    while logged:
                        try:
                            print("""
=========================================================
 _____                _____     _         _         _ 
|     |___ ___ _ _   |  _  |___|_|___ ___|_|___ ___| |
| | | | -_|   | | |  |   __|  _| |   |  _| | . | .'| |
|_|_|_|___|_|_|___|  |__|  |_| |_|_|_|___|_|  _|__,|_|
                                           |_|        
=========================================================
                        OPCIONES:
                1. Personas en mi ciudad
                2. Mi Match Ideal
                3. Cerrar Sesion
========================================================= 
                            """)
                            option = input(">> ")
                            if(int(option) in loggedOptions):
                                if(option == "1"):
                                    print("Personas en mi ciudad")
                                elif(option == "2"):
                                    print("Mi Match Ideal")
                                elif(option == "3"):
                                    print("Cerrando sesión...")
                                    logged = False      
                        except:
                            print("Entrada ivalida...")              
                else:
                    print("Nombre de usuario y/o contraseña incorrecta...")    


            elif(option == "2"):
                print("hola 2")
            elif(option == "3"):
                print("Hola 3")        
                login = False
    except:
        print("Entrada invalida...")    

