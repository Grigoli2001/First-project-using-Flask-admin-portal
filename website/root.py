from flask import Blueprint, render_template,url_for
from .databases.attendance import att
from .databases.populations import populations as pop
from .databases.courses import courses
from .databases.grades import student_grades
from .databases.students import students
root = Blueprint('root',__name__)

course_list = [["AIs",2020,"FALL"],["AIs",2021,"SPRING"],["CS",2020,"FALL"],["CS",2021,"SPRING"],["DSA",2020,"FALL"],["DSA",2021,"SPRING"],["ISM",2020,"FALL"],["ISM",2021,"SPRING"],["SE",2020,"FALL"],["SE",2021,"SPRING"]]
@root.route('/')
def home():
    count_list = []
    att_list=[]
    for el in course_list:
        count_list.append(pop(el[0],el[1],el[2]))
    for i in course_list:
        att_list.append(att(i[0],i[1],i[2]))
    return render_template("home.html", att = att,pop = pop, count_list= count_list, att_list=att_list)

@root.route('/populations/<course>/<year>/<intake>')
def population(course,year,intake):
    return render_template('populations.html',pops = students(course,year,intake),stud = courses(course,year,intake), course=course,year=year,intake=intake)

@root.route('/grades/<course>/<year>/<intake>/<course_name>')
def grades(course,year,intake,course_name):
    return render_template("grades.html", data = student_grades(course,year,intake,course_name), course=course,year=year,intake=intake,course_name=course_name)


