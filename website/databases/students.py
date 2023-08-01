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


def students(course,year,intake):
    curs.execute(
    f"""WITH avg_grades AS (
  SELECT s.STUDENT_EPITA_EMAIL, e.EXAM_COURSE_CODE, 
         (CASE WHEN SUM(g.GRADE_SCORE * e.EXAM_WEIGHT) / SUM(e.EXAM_WEIGHT) >= 10 THEN 1 ELSE 0 END) AS fgrades
  FROM STUDENTS s
  JOIN GRADES g ON s.STUDENT_EPITA_EMAIL = g.GRADE_STUDENT_EPITA_EMAIL_REF
  JOIN EXAMS e ON g.GRADE_COURSE_CODE_REF = e.EXAM_COURSE_CODE 
    GROUP BY s.STUDENT_EPITA_EMAIL, e.EXAM_COURSE_CODE
)
SELECT s.STUDENT_EPITA_EMAIL, c.CONTACT_FIRST_NAME, c.CONTACT_LAST_NAME,
       SUM(fgrades)  || '/' || COUNT(fgrades) 
FROM STUDENTS s
JOIN CONTACTS c ON s.STUDENT_CONTACT_REF = c.CONTACT_EMAIL
JOIN avg_grades ag ON s.STUDENT_EPITA_EMAIL = ag.STUDENT_EPITA_EMAIL
JOIN EXAMS e ON ag.EXAM_COURSE_CODE = e.EXAM_COURSE_CODE 
WHERE s.STUDENT_POPULATION_CODE_REF = '{course}' AND 
      s.STUDENT_POPULATION_YEAR_REF = {year} AND 
      s.STUDENT_POPULATION_PERIOD_REF LIKE '{intake}'
GROUP BY s.STUDENT_EPITA_EMAIL, c.CONTACT_FIRST_NAME, c.CONTACT_LAST_NAME
ORDER BY s.STUDENT_EPITA_EMAIL;"""
    )
    data = curs.fetchall()
    return data
    curs.close()
    connection.close()



