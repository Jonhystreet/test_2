from ctypes import addressof
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

#Creacion del esquema y las tablas posterior mente usaremos otro metodo para acceder a la informacion
#----------------------------------------------------------------------------------------------------*
app = Flask(__name__)
#Conexion con la base de datos el primer parametro es el tipo de base de datos
#segundo parametro despues del :// es tu usuario
#tercer parametro despues de : es tu contraseña
# @aquivatuhost/elnombredelabasededatos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/test'
db = SQLAlchemy(app)


#Creamos las tablas de usuario y de restaurantes
class User_0(db.Model):
    name = db.Column(db.String(80), primary_key=True ,unique=True, nullable=False)
    mail = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(30), nullable=False )

    def __init__(self, name, mail,password):
        self.name = name
        self.mail = mail
        self.password = password

class restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    adress = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(30), nullable=False )
    telephone = db.Column(db.String(12),nullable=False)

    def __init__(self,id ,name, adress,type,telephone):
        self.id = id
        self.name = name
        self.adress = adress
        self.type = type
        self.telephone = telephone

#---------------------------------------------------------------------------------------------------*
#Ralizamos la conexion
#CONEXION PARA VISUALIZAR DATOS
#----------------------------------------------------------------*
import psycopg2
try: 
    conn = psycopg2.connect(database="test", user="postgres",  
    password="1234", host="localhost")
    print("Conectado")
except:
    print ("No puedo conectarme a la base de datos")
mycursor = conn.cursor()
#*------------------------------------------------------------------*


#Se empiezan a crear los requisitos
#Iniciamos con nuestro indice
@app.route('/') 
def index():
    return render_template('index.html')

#*----------------------------------------------------------------#
#Visualizador de restaurantes
@app.route('/v_restaurant')
def v_restaurant():
    mycursor.execute("SELECT * FROM restaurant")
    data = mycursor.fetchall()
    return render_template('v_restaurant.html', data=data)
#*----------------------------------------------------------------#

#*----------------------------------------------------------------#
#Alta restaurante

#primero creo una route que me lleva al formulario html del restaurant


@app.route('/form_restaurant')
def form_restaurant():
    return render_template("form_restaurant.html")

#Aqui uso el metodo post y voy a almacenar los datos


@app.route('/alta_res', methods=['POST'])
def alta_res():
    name = request.form.get("name")
    adress = request.form.get("adress")
    type = request.form.get("type")
    telephone = request.form.get("telephone")
    
    #Ejectumas y obtenemos el maximo id del momento a eso
    #le sumaremos uno posterior mente el .fetchone() guarda solo un valor
    mycursor.execute("SELECT MAX(id) from restaurant")
    result= mycursor.fetchone()
    id = result[0] + 1
    
    #print(id)

    entry = restaurant(id,name,adress,type,telephone)  
    db.session.add(entry)
    db.session.commit() 
    return render_template("index.html")


#*----------------------------------------------------------------#
#Alta usuario

@app.route('/form_usu')
def form_usu():
    return render_template("form_usu.html")

#Aqui uso el metodo post y voy a almacenar los datos


@app.route('/alta_usu', methods=['POST'])
def alta_usu():
    
    name = request.form.get("name")
    mail = request.form.get("mail")
    password = request.form.get("password")
    
    entry = User_0(name,mail,password)  
    db.session.add(entry)
    db.session.commit() 
    return render_template("index.html")

#*----------------------------------------------------------------#

#Alta USUARIO
if __name__ == '__main__':
    db.create_all()
    app.run()