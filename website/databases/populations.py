import jaydebeapi
import os
 
def connect(db_driver_path: str, db_url: str, db_user: str, db_password: str) -> jaydebeapi.Connection:
    """
    connects to the h2 database
    :return:
    """
    conn = jaydebeapi.connect('org.h2.Driver', db_url, [db_user, db_password], db_driver_path)
    return conn
    # TODO read those configuration entries from a configuration file
path_to_java = r"C:\\Program Files\\Eclipse Adoptium\\jdk-11.0.18.10-hotspot\\bin"
path_to_h2_jar: str = r"C:\\H2\\bin\\h2-2.1.214.jar"
url: str = 'jdbc:h2:tcp://localhost/~/EPITADB'
user: str = 'gega'
password: str = 'gega'
os.environ["JAVA_HOME"] = path_to_java

connection: jaydebeapi.Connection = connect(path_to_h2_jar, url, user, password)
curs: jaydebeapi.Cursor = connection.cursor()
    # Interrogation marks will be replaced by query parameters given as
    # second argument of execute() function



def populations(course,year,intake):
    curs.execute(
    f"""SELECT COUNT(STUDENT_EPITA_EMAIL)  FROM STUDENTS s WHERE STUDENT_POPULATION_YEAR_REF = '{year}' AND STUDENT_POPULATION_CODE_REF LIKE '{course}' AND s.STUDENT_POPULATION_PERIOD_REF LIKE '{intake}'"""
    )
    data = curs.fetchall()
    return data[0][0]
    curs.close()
    connection.close()
