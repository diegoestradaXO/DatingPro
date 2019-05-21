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
|    ____        __  _                   ____           |
|   / __ \____ _/ /_(_)___  ____ _      / __ \_________ |
|  / / / / __ `/ __/ / __ \/ __ `/_____/ /_/ / ___/ __ \|
| / /_/ / /_/ / /_/ / / / / /_/ /_____/ ____/ /  / /_/ /|
|/_____/\__,_/\__/_/_/ /_/\__, /     /_/   /_/   \____/ |
|                        /____/                         |
=========================================================
|                        LOGIN:                         |
|                    1. Ingresar                        |
|                    2. Registrarse                     |
|                    3. Salir                           |
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
| _____                _____     _         _         _  |
||     |___ ___ _ _   |  _  |___|_|___ ___|_|___ ___| | |
|| | | | -_|   | | |  |   __|  _| |   |  _| | . | .'| | |
||_|_|_|___|_|_|___|  |__|  |_| |_|_|_|___|_|  _|__,|_| |
|                                           |_|         |
=========================================================
|                        OPCIONES:                      |
|                1. Personas en mi ciudad               |
|                2. Mi Match Ideal                      |
|                3. Cerrar Sesion                       |
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
                print("Registro..")
                name = ""
                while(name == ""):
                    name = input(">> Escribe tu nombre real: ")
                user = ""
                while(user == ""):
                    user = input(">> Escoge un nombre de usuaio: ")
                password = ""
                while(password == ""):
                    password = input(">> Escoge una contraseña: ")
                age = ""  
                while(age == ""):
                    age = input(">> ¿Cuántos años tienes?: ")
                num = ""
                while(num == ""):
                    num = input(">> Escribe el número de teléfono al que te pueden contactar: ")
                foods = ["Italiana","Mexicana","China","FastFood","Chapina","Sushi"]
                print(">> De las siguientes opciones, ¿Cuál es tu comida favorita?")
                counter = 1
                for i in foods:
                    print("     " + str(counter) + ". " + i)
                    counter += 1
                chose = False    
                while(chose == False):
                    food = ""
                    while(food == ""):
                        food = input(">> Escoge un tipo de comida: ") 
                    if(food in foods):
                        chose = True  
                musicGenres = ["Rock","Reggaetón","RnB","Clásica","Electrónica","Cumbia","Hip Hop"]
                print(">> De las siguientes opciones, ¿Qué musica prefieres?")
                counter = 0
                for i in musicGenres:
                    print("     " + str(counter) + ". " + i)
                    counter += 1
                chose = False
                while(chose == False):
                    musicGenre = ""
                    while(musicGenre == ""):
                        musicGenre = input(">> Escoge un género de música: ")
                    if(musicGenre in musicGenres):
                        chose = True
                movieGenres = ["Acción","Terror","Tragedia","Comedia","Drama","Superhéroes"]
                print(">> De las siguientes opciones, ¿Qué tipo de películas prefieres?")
                counter = 0
                for i in movieGenres:
                    print("     " + str(counter) + ". " + i)
                    counter += 1
                chose = False
                while(chose == False):
                    movieGenre = ""
                    while(movieGenre == ""):
                        movieGenre = input(">> Escoge un género de música: ")
                    if(movieGenre in movieGenres):
                        chose = True
                city = ""
                while(city == ""):
                    city = input(">> ¿En qué ciudad vives?: ")
                

                # Despues de la recoleccion de datos, se procede a crear el usuario
                #db.add_user(name,user,password,age,num)
                #print("Ya lo agregue broco!")
                #Verificar que los tipos de comida, pelicula, musica y ciudad existan, si no existen crea el nodo, de lo contrario los une             
                    
            elif(option == "3"):
                print("Hola 3")        
                login = False
    except:
        print("Entrada invalida...")    

