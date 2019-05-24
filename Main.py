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
 #   try:
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
                       # try:
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
                                    db.matchPersonsOnCity(department)
                                elif(option == "2"):
                                    print("Mi Match Ideal")
                                    preferences = input("Que genero esta buscando?")
                                    db.matchMiMatchIdeal(age, food, musicGenre, department, preferences)
                                elif(option == "3"):
                                    print("Cerrando sesión...")
                                    logged = False      
                       # except:
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
                ages = ["18-25","26-40","41-60","60+"]
                print(">> De las siguientes opciones, ¿Cuál es tu rango de edad?")
                counter = 1
                for i in ages:
                    print("     " + str(counter) + ". " + i)
                    counter += 1
                chose = False    
                while(chose == False):
                    age = ""
                    while(age == ""):
                        age = input(">> Escoge tu rango de edad: ") 
                    if(age in ages):
                        chose = True
                #num = ""
                #while(num == ""):
                #    num = input(">> Escribe el número de teléfono al que te pueden contactar: ")
                foods = ["Italiana","Mexicana","China","Comida Rapida","Guatemalteca"]
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
                musicGenres = ["Rock","Reggaeton","Clasica","Electronica","Salsa","Jazz","Banda"]
                print(">> De las siguientes opciones, ¿Qué musica prefieres?")
                counter = 1
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
                #movieGenres = ["Accion","Miedo","Tragedia","Comedia","Drama","Romantica","Infantil"]
                #print(">> De las siguientes opciones, ¿Qué tipo de películas prefieres?")
                #counter = 1
                #for i in movieGenres:
                #   print("     " + str(counter) + ". " + i)
                #   counter += 1
                #chose = False
                #while(chose == False):
                #    movieGenre = ""
                #    while(movieGenre == ""):
                #        movieGenre = input(">> Escoge un género de pelicula: ")
                #    if(movieGenre in movieGenres):
                #        chose = True
                departments = ["Alta Verapaz","Baja Verapaz","Chimaltenango","Chiquimula","Peten","El Progreso","Quiche","Escuintla","Guatemala","Huehuetenango","Izabal","Jalapa","Jutiapa","Quetzaltenango","Retalhuleu","Sacatepequez","San Marcos","Santa Rosa","Solola","Suchitepequez","Totonicapan","Zacapa"]
                print(">> ¿En qué departamento vives?")
                counter = 1
                for i in departments:
                    print("     " + str(counter) + ". " + i)
                    counter += 1
                chose = False
                while(chose == False):
                    department = ""
                    while(department == ""):
                        department = input(">> Escoge tu departamento: ")
                    if(department in departments):
                        chose = True
                preferences = ["Hombre","Mujer"]
                print(">> ¿Cuales son tus preferencias?")
                counter = 1
                for i in preferences:
                    print("     " + str(counter) + ". " + i)
                    counter += 1
                chose = False
                while(chose == False):
                    preference = ""
                    while(preference == ""):
                        preference = input(">> Escoge tu preferencia: ")
                    if(preference in preferences):
                        chose = True
                
                db.add_user(name,user,password)
                print("Ya lo agregue broco!")
                #Verificar que los tipos de comida, pelicula, musica y ciudad existan, si no existen crea el nodo, de lo contrario los une             
                if(len(db.verifyExistence("Age",age)) > 0):
                    db.match_age(name, age)
                    print("relacion creada")
                else:
                    db.make_a_match("userToAge",name, age)
                    print("edad creada")

                if(len(db.verifyExistence("Food",food)) > 0):
                    db.match_food(name, food)
                    print("relacion creada")
                else:
                    db.make_a_match("userToFood",name, food)
                    print("comida creada")
                
                if(len(db.verifyExistence("Music",musicGenre)) > 0):
                    db.match_music(name, musicGenre)
                    print("relacion creada")
                else:
                    db.make_a_match("userToMusic",name, musicGenre)
                    print("musica creada")

                #if(len(db.verifyExistence("Movie",movieGenre)) > 0):
                #    db.match_movie("userToMovie",user, movieGenre)
                #    print("relacion creada")
                #else:
                #    db.add_movie(movieGenre)
                #    db.make_a_match("userToMovie",user, movieGenre)
                #    print("pelicula creada")
                
                if(len(db.verifyExistence("Department",department)) > 0):
                    db.match_department(name, department)
                    print("relacion creada")
                else:
                    db.make_a_match("userToDepartment",name, department)
                    print("departamento creado")

                if(len(db.verifyExistence("Preference",preference)) > 0):
                    db.match_preference(name, preference)
                    print("relacion creada")
                else:
                    db.make_a_match("userToPreference",name, preference)
                    print("departamento creado")
            elif(option == "3"):
                login = False
    #except:
     #   print("Entrada invalida...")    

