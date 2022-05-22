from flask import Flask, render_template, request
import usuario as usr
import csv

app = Flask(__name__)

usuarios = [usr.usuario('Gerardo'), usr.usuario('Luis'), usr.usuario('Yeni')]

usuarios[0].agregar_tarjeta('credito','Uno', 5, 2000)
usuarios[0].agregar_tarjeta('credito','Dos', 2, 8000)
usuarios[0].agregar_tarjeta('servicio', 'Tres', 15, 4000)

usuarios[1].agregar_tarjeta('credito','Uno', 5, 3000)
usuarios[1].agregar_tarjeta('credito','Dos', 2, 7000)
usuarios[1].agregar_tarjeta('servicio', 'Tres', 3, 6000)

usuarios[2].agregar_tarjeta('credito','Uno', 5, 10000)
usuarios[2].agregar_tarjeta('credito','Dos', 2, 5000)
usuarios[2].agregar_tarjeta('servicio', 'Tres', 3, 1000)

#Busca a un Usuario y obtiene su posicion en la lista
def get_index_lista_usuarios(nombre):
  for obj in usuarios:
    if nombre == obj.usuario:
      return usuarios.index(obj)
  return -1

#Se pueden usar diccionarios como argumentos para writerow
with open("usuarios.csv", 'w') as fcsv: 
    fields = ("Usuario", "Nombre Tarjeta", "Tasa Interes", "Deuda Inicial", "Por abonar") 
    writer = csv.DictWriter(fcsv, fieldnames=fields)
    #writer.writeheader()
    for user in usuarios:
        usuario_actual = user.usuario
        for tarj in user.lista_tarjetas:
            writer.writerow({'Usuario': usuario_actual, 'Nombre Tarjeta': tarj.nombre_tarjeta, 'Tasa Interes': str(tarj.tasa_interes), 'Deuda Inicial': str(tarj.deuda), 'Por abonar': str(tarj.abono_a_realizar)})

# Permite que la ruta funcione para peticiones GET y POST
@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    #print(request.form["usuario"])
    #print(request.form["tarjeta"])
    #print(request.form["tasa"])
    #print(request.form["deuda"])

    queryUser = get_index_lista_usuarios(request.form["usuario"])
    #queryTarjeta = usuarios[queryUser].get_index_lista_tarjetas(request.form["tarjeta"])
    usuarios[queryUser].multiples_reportes()

  with open("usuarios.csv") as file:
    return render_template("index.html", csv=file)