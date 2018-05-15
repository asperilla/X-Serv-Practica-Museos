from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from xml.dom import minidom
from django.contrib.auth.models import User

# Create your views here.

from .models import Museo

# Defino los botones -> "Todos" e "Inicio":
boton_inicio = """
	<form action="http://localhost:8000/" method="GET">
	<input type="submit" value="Inicio">
	</form>
	"""

boton_todos = """
	<form action="http://localhost:8000/museos" method="GET">
	<input type="submit" value="Todos">
	</form>
	"""

boton_accesibles = """
	<form action="http://localhost:8000/" method="POST">
	<input type="submit" value="Accesibles">
	</form>
	"""

boton_accesibles_get = """
	<form action="http://localhost:8000/" method="GET">
	<input type="submit" value="Accesibles">
	</form>
	"""

# Código visto en StackOverFlow



@csrf_exempt
def barra(request):

	if request.user.is_authenticated():
		logged = 'Logged in as ' + request.user.username + ' <a href=logout?next=/>logout</a>'
	else:
		logged = 'Not logged in.' + ' <a href=login?next=/>login</a>'

	if request.method == "POST":
		museos = Museo.objects.all()
		respuesta = "<ul>"
		for museo in museos:
			if museo.Accesibilidad == 0:
				url = museo.Enlace
				direccion = "Dirección: " + museo.Direccion
				mas_info = '<a href="/museos/' + str(museo.id) + '">' + "Más información" + '</a>'
				contenido = direccion + "<br>" + mas_info
				respuesta += '<li>''<a href=' + url + '>' + museo.Nombre + '</a>' + "<br>" + direccion + "<br>" + mas_info + "<br>" + "<br>"
		respuesta += "<ul>"
		template = get_template("Plantilla_1/index.html") #	
		c = Context({'logged': logged, 'content': respuesta, 'accesibles': boton_accesibles_get, 'todos': boton_todos})
		return HttpResponse(template.render(c))
			
	
	museos = Museo.objects.all() # dame  los museos; me los devuelve en una lista; museo.id, museo.nombre...
	if not museos:

		#Parseo el archivo xml
		xmldoc = minidom.parse('museos.xml')

		for i in range(66):
			dicc = {}
			atributos_list = xmldoc.getElementsByTagName('atributos')[i]
			atributo_list = atributos_list.getElementsByTagName('atributo')
			for item in atributo_list:
				llave = item.attributes['nombre'].value
				valor = item.childNodes[0].nodeValue
		#print(item.attributes['nombre'].value + "=" + item.childNodes[0].nodeValue)
				dicc[llave] = valor
		

			try:
				museo_nuevo = Museo(Nombre=dicc["NOMBRE"], Descripcion=dicc["DESCRIPCION-ENTIDAD"], Accesibilidad=dicc["ACCESIBILIDAD"],
									Barrio=dicc["BARRIO"], Distrito=dicc["DISTRITO"], Telefono=dicc["TELEFONO"], Fax=dicc["FAX"],
									Email=dicc["EMAIL"], Direccion=dicc["NOMBRE-VIA"], CodigoPostal=dicc["CODIGO-POSTAL"],
									Enlace=dicc["CONTENT-URL"])

			except KeyError:
				continue
			except ValueError:
				continue

			museo_nuevo.save()

	#respuesta = "<ul>"
	#for museo in museos:
	#	url = museo.Enlace
	#	direccion = "Dirección: " + museo.Direccion
	#	mas_info = '<a href="/museos/' + str(museo.id) + '">' + "Más información" + '</a>'
	#	contenido = direccion + "<br>" + mas_info
	#	respuesta += '<li>''<a href=' + url + '>' + museo.Nombre + '</a>' + "<br>" + direccion + "<br>" + mas_info + "<br>" + "<br>"
	#respuesta += "<ul>"

	museos_comentados = Museo.objects.order_by('-NumeroComentarios')
	respuesta = "<ul>"
	k = 0
	for museo in museos_comentados:
		if museo.NumeroComentarios >0:
			url = museo.Enlace
			direccion = "Dirección: " + museo.Direccion
			mas_info = '<a href="/museos/' + str(museo.id) + '">' + "Más información" + '</a>'
			contenido = direccion + "<br>" + mas_info
			respuesta += '<li>''<a href=' + url + '>' + museo.Nombre + '</a>' + "<br>" + direccion + "<br>" + mas_info + "<br>" + "<br>"
		k = k +1
		if k == 5:
			break
	respuesta += "<ul>"


	users_list = []
	users = User.objects.all()

	for user in users:
		users_list += [user]

	template = get_template("Plantilla_1/index.html") #	
	c = Context({'logged': logged, 'content': respuesta, 'lista_usuarios': users_list ,'accesibles': boton_accesibles, 'todos': boton_todos})
	return HttpResponse(template.render(c))



@csrf_exempt
def museos(request):

	if request.user.is_authenticated():
		logged = 'Logged in as ' + request.user.username + ' <a href=logout?next=/museos>logout</a>'
	else:
		logged = 'Not logged in.' + ' <a href=http://localhost:8000/login?next=/museos>login</a>'

	formulario_distrito = """
		<form action="" method="POST">
		<br>Introduce distrito:<br>
			Distrito <input type="text" name="distrito"><br>
			<input type="submit" value="Enviar">
		</form>
		"""

	if request.method == "POST":
		request_body = request.body.decode('utf-8')
		distrito = request_body.split('=')[1]
		museos = Museo.objects.all()
		respuesta = "<ul>"
		for museo in museos:
			if distrito == museo.Distrito:
				respuesta += '<li><a href="/museos/' + str(museo.id) + '">' + museo.Nombre + '</a>'
		respuesta += "<ul>"
		template = get_template("Plantilla_museos/index.html") #	
		c = Context({'logged': logged, 'formulario_distrito': formulario_distrito, 'content': respuesta, 'inicio': boton_inicio})
		return HttpResponse(template.render(c))

	museos = Museo.objects.all() # dame todos los museos; me los devuelve en una lista; museo.id, museo.nombre...
	respuesta = "<ul>"
	for museo in museos:
		respuesta += '<li>''<a href="/museos/' + str(museo.id) + '">' + museo.Nombre + '</a>'		
	respuesta += "<ul>"			

	#return HttpResponse("TODOS LOS MUSEOS" + "<br>" + logged + "<br>" + formulario + "<br>" + "Museos: " + "<br>" + respuesta+ "<br>" + boton_inicio)

	template = get_template("Plantilla_museos/index.html") #	
	c = Context({'logged': logged, 'formulario_distrito': formulario_distrito, 'content': respuesta, 'inicio': boton_inicio})
	return HttpResponse(template.render(c))


def museo(request, number):

	if request.method == "POST":
		m = Museos(nombre = request.POST['nombre'], direccion = request.POST['direccion'], 
					enlace = request.POST['enlace'])
		m.save()
		number = m.id

	try:
		museo =	Museos.objects.get(id=int(number))
		respuesta = "Su dirección es: " + museo.direccion
	except Museos.DoesNotExist:
		return HttpResponse("No existe" + "<br>")

	return HttpResponse(respuesta)

def usuario(request):
	return HttpResponse("Museos seleccionados por este usuario")





