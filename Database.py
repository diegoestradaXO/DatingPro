#Proyceto 2 de Algoritmos y Estructura de Datos
#DatingPro: recomendaciones con graph database usando Neo4J
#Autores:
#Michael Chan 18562 
#Diego Estrada 18540
#Isabel Ortiz 18176

from neo4j import GraphDatabase

class Database(object):
    #Crea la base de datos
    def __init__(self, uri,user,password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    #Cierra la base de datos
    def close(self):
        self._driver.close()

    def user_to_age(cls, tx, param1, param2):
        tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                "MATCH (b:age) WHERE b.range = $param2 "
                "MERGE (a)-[:edad]->(b)",
            param1=param1, param2=param2)
    def match_age(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_age, param1, param2)

    def user_to_food(cls, tx, param1, param2):
        tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                "MATCH (b:food) WHERE b.type = $param2 "
                "MERGE (a)-[:comida]->(b)",
            param1=param1, param2=param2)
    def match_food(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_food, param1, param2)

    def user_to_movie(cls, tx, param1, param2):
        tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                "MATCH (b:movies) WHERE b.genre = $param2 "
                "MERGE (a)-[:pelicula]->(b)",
            param1=param1, param2=param2)
    def match_movie(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_movie, param1, param2)

    def user_to_department(cls, tx, param1, param2):
        tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                "MATCH (b:department) WHERE b.department = $param2 "
                "MERGE (a)-[:departamento]->(b)",
            param1=param1, param2=param2)
    def match_department(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_department, param1, param2)
    
    def user_to_music(cls, tx, param1, param2):
        tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                "MATCH (b:music) WHERE b.genre = $param2 "
                "MERGE (a)-[:musica]->(b)",
            param1=param1, param2=param2)
    def match_music(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_music, param1, param2)

    def user_to_preference(cls, tx, param1, param2):
        tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                "MATCH (b:preferences) WHERE b.type = $param2 "
                "MERGE (a)-[:preferencias]->(b)",
            param1=param1, param2=param2)
    def match_preference(self, param1,  param2):
         with self._driver.session() as session:
             return session.write_transaction(self.user_to_preference, param1, param2)

    def add_user(self, name, user, password):
        with self._driver.session() as session:
            return session.write_transaction(self.create_user_node, name, user, password)
    @staticmethod
    def create_user_node(tx, name, user, password):
        tx.run("CREATE (:Person {name: $name, user: $user, password: $password})",
         name=name, user=user, password=password)

    def verifyAccount(self, user, password):
        results=[]
        matchQuery = "MATCH (p:Person {user: '" + user + "', password: '" + password + "'}) RETURN p"
            # Execute the CQL query
        with self._driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(matchQuery)
            for node in nodes:
                results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
            return results

    def verifyExistence(self, nodeType, param):
        if(nodeType == "Age"):
            results=[]
            matchQuery = "MATCH (x:age {range: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Music"):
            results=[]
            matchQuery = "MATCH (x:music {genre: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Movie"):
            results=[]
            matchQuery = "MATCH (x:movies {genre: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Food"):
            results=[]
            matchQuery = "MATCH (x:food {type: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Department"):
            results=[]
            matchQuery = "MATCH (x:department {department: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Preference"):
            results=[]
            matchQuery = "MATCH (x:preferences {type: '" + param + "'}) RETURN x"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
    #def add_food(self, typeOfFood):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_food_node, typeOfFood)
    #@staticmethod
    #def create_food_node(tx, typeOfFood):
     #   tx.run("CREATE (:Food {typeOfFood: $typeOfFood})",
      #   typeOfFood=typeOfFood)


    #def add_movie(self, genre):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_movie_node, genre)
    #@staticmethod
    #def create_movie_node(tx, genre):
     #   tx.run("CREATE (:Movie {genre: $genre})",
      #   genre=genre)

    #def add_music(self, genre):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_music_node, genre)
    #@staticmethod
    #def create_music_node(tx, genre):
     #   tx.run("CREATE (:Music {genre: $genre})",
      #   genre=genre)     

    #def add_city(self, name):
     #   with self._driver.session() as session:
      #      return session.write_transaction(self.create_city_node, name)
    #@staticmethod
    #def create_city_node(tx, name):
     #   tx.run("CREATE (:City {name: $name})",
      #   name=name)

    def make_a_match(self, relation, param1, param2):
        with self._driver.session() as session:
            return session.write_transaction(self.create_a_match, relation, param1, param2)
                    

    def create_a_match(cls, tx, relation, param1, param2):
        if(relation == "userToFood"):
           tx.run("MATCH (a:User) WHERE a.name = $param1 "
           "MERGE (b:Food {typeOfFood: $param2})"
           "MERGE (a)-[:LIKES]->(b)",
           param1=param1, param2=param2)
        elif(relation == "userToMovie"):
            tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                    "MERGE (b:movies {genre: $param2})"
                    "MERGE (a)-[:pelicula]->(b)",
                    param1=param1,param2=param2)
        elif(relation == "userToMusic"):
            tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                    "MERGE (b:music {genre: $param2})"
                    "MERGE (a)-[:musica]->(b)",
                    param1=param1,param2=param2)
        elif(relation == "userToDepartment"):
            tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                    "MERGE (b:department {department: $param2})"
                    "MERGE (a)-[:departamento]->(b)",
                    param1=param1,param2=param2)
        elif(relation == "userToAge"):
            tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                    "MERGE (b:age {range: $param2})"
                    "MERGE (a)-[:edad]->(b)",
                    param1=param1,param2=param2)
        elif(relation == "userToPreference"):
            tx.run("MATCH (a:Person) WHERE a.name = $param1 "
                    "MERGE (b:preferences {type: $param2})"
                    "MERGE (a)-[:preferencias]->(b)",
                    param1=param1,param2=param2)
        
        
        		# Funcion que crea las relaciones segun las opciones elegidas
    def match(user):
        result = tx.run("match (:Person {name:$user})--(departamento:department)"
            "match (:Person {name:$user})--(comida:food)"
            "match (:Person {name:$user})--(musica:music)"
            "return departamento,comida,musica",
            user=user)

        comida = result[1]
        departamento = result[0]
        musica = result[2]

        # Devuelve las relaciones segun la departamento, comida y musica 
        tx.run("match (musica:music)--(persona:Person) where musica.genre = $var1 "
            "match (comida:Food)--(persona:Person) where comida.type = $var2"
            "optional match (deparatmento:department)--(persona:Person) where deparatmento.department = $var3"
            "return persona.name",
            var1=musica,var2=comida,var3=departamento)

    def personsOnYourCity(cls, tx, param1):
        cont = 0
        for person in tx.run("MATCH (a:Person) -[:departamento]->(f:department {department:$param1}) return a.name ",
            param1=param1):
            cont += 1
            print(str(cont) + ". " + person["a.name"])
    def matchPersonsOnCity(self, param1):
         with self._driver.session() as session:
             return session.write_transaction(self.personsOnYourCity, param1)

    def miMatchIdeal(cls,tx, age, food, music, department, preferences):
        cont = 0
        if(preferences == "Hombre"):
            preferences = "Mujer"
            for i in tx.run("MATCH (p:Person)" 
                    "WHERE (p)-[:edad]->(:age {range:$age}) and (p) -[:comida]->(:food {type:$food}) and (p) -[:musica]->(:music {genre:$music}) and (p) -[:departamento]->(:department {department:$department}) and (p) -[:preferencias]->(:preferences {type:$preferences} )"
                    "RETURN p.name ",
                age=age, food=food, music=music, department=department, preferences=preferences):
                cont += 1
                print(str(cont) + ". " + i["p.name"])
        elif(preferences == "Mujer"):
            preferences = "Hombre"
            for i in tx.run("MATCH (p:Person)" 
                    "WHERE (p)-[:edad]->(:age {range:$age}) and (p) -[:comida]->(:food {type:$food}) and (p) -[:musica]->(:music {genre:$music}) and (p) -[:departamento]->(:department {department:$department}) and (p) -[:preferencias]->(:preferences {type:$preferences} )"
                    "RETURN p.name ",
                age=age, food=food, music=music, department=department, preferences=preferences):
                cont += 1
                print(str(cont) + ". " + i["p.name"])

    def matchMiMatchIdeal(self, age, food, music, department, preferences):
        with self._driver.session() as session:
             return session.write_transaction(self.miMatchIdeal, age, food, music, department, preferences)