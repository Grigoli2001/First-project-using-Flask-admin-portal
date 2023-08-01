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


def courses(course,year,intake):
    curs.execute(
    f"""SELECT c.COURSE_CODE AS ID,c.COURSE_NAME , COUNT(s.SESSION_COURSE_REF)  FROM COURSES c JOIN PROGRAMS p ON c.COURSE_CODE = p.PROGRAM_COURSE_CODE_REF JOIN SESSIONS s ON s.SESSION_COURSE_REF = c.COURSE_CODE WHERE p.PROGRAM_ASSIGNMENT LIKE '{course}' AND s.SESSION_POPULATION_YEAR  ={year} AND s.SESSION_POPULATION_PERIOD LIKE '{intake}'GROUP BY ID"""
    )
    data = curs.fetchall()
    return data
    curs.close()
    connection.close()





