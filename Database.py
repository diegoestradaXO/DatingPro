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

    #Crea un nodo segun el tipo indicado
    def add_user(self, name, user, password, age, num):
        with self._driver.session() as session:
            return session.write_transaction(self.create_user_node, name, user, password, age, num)
    @staticmethod
    def create_user_node(tx, name, user, password, age, num):
        return tx.run("CREATE (u:User {name: $name, user: $user, password: $password, age: $age, num: $num}) RETURN id(u)",
         name=name, user=user, password=password, age=age, num=num).single().value()
    def verifyAccount(self, user, password):
        results=[]
        matchQuery = "MATCH (u:User {user: '" + user + "', password: '" + password + "'}) RETURN u"
            # Execute the CQL query
        with self._driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(matchQuery)
            for node in nodes:
                results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
            return results

    def verifyExistence(self, nodeType, param):
        if(nodeType == "Music"):
            results=[]
            matchQuery = "MATCH (m:Music {type: '" + param + "'}) RETURN m"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Movie"):
            results=[]
            matchQuery = "MATCH (p:Movie {type: '" + param + "'}) RETURN p"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "Food"):
            results=[]
            matchQuery = "MATCH (f:Food {type: '" + param + "'}) RETURN f"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results
        if(nodeType == "City"):
            results=[]
            matchQuery = "MATCH (c:City {name: '" + param + "'}) RETURN c"
                # Execute the CQL query
            with self._driver.session() as graphDB_Session:
                nodes = graphDB_Session.run(matchQuery)
                for node in nodes:
                    results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
                return results


            
    @staticmethod
    def _Default(tx,result):
        return tx.run(result)

    @staticmethod
    def _getNodes(tx,result,value):
        return tx.run(result,value=value)

    @staticmethod
    def _getNode(tx,result,value):
        return tx.run(result,value=value)

    @staticmethod
    def _upgrade(tx,result,value,newValue):
        result = tx.run(result,value=value,newValue=newValue)

    @staticmethod
    def _deleteLink(tx,result,variable1,variable2):
        result = tx.run(result,variable1=variable1,variable2=variable2) 

    @staticmethod
    def _delete(tx,result,value):
        result = tx.run(result,value=value)            

    @staticmethod
    def _connect(tx,result,variable1,variable2):
        result = tx.run(result,variable1=variable1,variable2=variable2) 

    """This method is used by write"""
    @staticmethod
    def _create(tx,arguments,result):
        result = tx.run(result,arguments=arguments)        

