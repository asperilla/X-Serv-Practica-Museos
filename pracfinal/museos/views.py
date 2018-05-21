from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
from xml.dom import minidom
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

from .models import Museo
from .models import Comentario
from .models import User
from .models import PagPersonal

# Defino los botones -> "Accesibles":

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
			if museo.Accesibilidad == "0":
				url = museo.Enlace
				direccion = "Dirección: " + museo.Direccion
				mas_info = '<a href="/museos/' + str(museo.id) + '">' + "Más información" + '</a>'
				contenido = direccion + "<br>" + mas_info
				respuesta += '<li>''<a href=' + url + '>' + museo.Nombre + '</a>' + "<br>" + direccion + "<br>" + mas_info + "<br>" + "<br>"
		respuesta += "<ul>"
		template = get_template("Plantilla_1/index.html") #	
		c = Context({'logged': logged, 'content': respuesta, 'accesibles': boton_accesibles_get})
		return HttpResponse(template.render(c))
			
	
	museos = Museo.objects.all() # dame  los museos; me los devuelve en una lista; museo.id, museo.nombre...
	if not museos:

	## Código visto en StackOverFlow ##

			#Parseo el archivo xml
		xmldoc = minidom.parse('museos.xml')

		for i in range(67):
			dicc = {}
			atributos_list = xmldoc.getElementsByTagName('atributos')[i]
			atributo_list = atributos_list.getElementsByTagName('atributo')

			for item in atributo_list:
				llave = item.attributes['nombre'].value
				if llave != "NOMBRE" and llave != "DESCRIPCION-ENTIDAD" and llave != "ACCESIBILIDAD" and llave != "BARRIO" and llave != "DISTRITO" and llave != "TELEFONO" and llave != "EMAIL" and llave != "NOMBRE-VIA" and llave != "CODIGO-POSTAL" and llave != "CONTENT-URL":
					continue
				else:
					valor = item.childNodes[0].nodeValue
					dicc[llave] = valor
			
			lista_caracteristicas = ["NOMBRE","DESCRIPCION-ENTIDAD","ACCESIBILIDAD","BARRIO,DISTRITO","TELEFONO","EMAIL","NOMBRE-VIA","CODIGO-POSTAL","CONTENT-URL"]
			lista_keys = []
			for key,value in dicc.items():
				lista_keys += [key]
			print(lista_keys)
			
			for i in lista_caracteristicas:
				if i not in lista_keys:
					dicc[i] = ""

			try:
				museo_nuevo = Museo(Nombre=dicc["NOMBRE"], Descripcion=dicc["DESCRIPCION-ENTIDAD"], Accesibilidad=dicc["ACCESIBILIDAD"],
									Barrio=dicc["BARRIO"], Distrito=dicc["DISTRITO"], Telefono=dicc["TELEFONO"], Email=dicc["EMAIL"], 									Direccion=dicc["NOMBRE-VIA"], CodigoPostal=dicc["CODIGO-POSTAL"], Enlace=dicc["CONTENT-URL"])

			except KeyError:
				continue
			except ValueError:
				continue

			museo_nuevo.save()


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
		k = k + 1
		if k == 5:
			break
	respuesta += "<ul>"

	l_nombres = []
	users = User.objects.all()
	for user in users:
		nombre = user.username
		l_nombres += [nombre]
		
	template = get_template("Plantilla_1/index.html")
	c = Context({'logged': logged, 'content': respuesta, 'accesibles': boton_accesibles, 'lista_usuarios': l_nombres})
	return HttpResponse(template.render(c))



@csrf_exempt
def museos(request):

	formulario_distrito = """
		<form action="" method="POST">
		<br>Introduce distrito:<br>
			Distrito <input type="text" name="distrito"><br>
			<input type="submit" value="Enviar">
		</form>
		"""
	if request.user.is_authenticated():
		logged = 'Logged in as ' + request.user.username + ' <a href=/logout?next=/museos>logout</a>'
	else:
		logged = 'Not logged in.' + ' <a href=http://localhost:8000/login?next=/museos>login</a>'

	if request.method == "POST":
		request_body = request.body.decode('utf-8')
		distrito = request_body.split('=')[1]
		museos = Museo.objects.all()
		respuesta = "<ul>"
		for museo in museos:
			if distrito == museo.Distrito:
				respuesta += '<li><a href="/museos/' + str(museo.id) + '">' + museo.Nombre + '</a>'
		respuesta += "<ul>"
		respuesta = "Museos en distrito: " + distrito + "<br>" + respuesta
		template = get_template("Plantilla_museos/index.html") #	
		c = Context({'logged': logged, 'formulario_distrito': formulario_distrito, 'content': respuesta})
		return HttpResponse(template.render(c))

	museos = Museo.objects.all() # dame todos los museos; me los devuelve en una lista; museo.id, museo.nombre...
	respuesta = "<ul>"
	for museo in museos:
		respuesta += '<li>''<a href="/museos/' + str(museo.id) + '">' + museo.Nombre + '</a>'		
	respuesta += "<ul>"			

	l_nombres = []
	users = User.objects.all()
	for user in users:
		nombre = user.username
		l_nombres += [nombre]

	template = get_template("Plantilla_museos/index.html") #	
	c = Context({'logged': logged, 'content': respuesta, 'formulario_distrito': formulario_distrito, 'lista_usuarios': l_nombres})
	return HttpResponse(template.render(c))

@csrf_exempt
def museo(request, number):

	recurso = request.path
	number = recurso.split('/')[2]
	n_int = int(number)


	formulario_comentario = """
		<form action="" method="POST">
		<br>Introduce comentario:<br>
			<input type="text" name="comentario"><br>
			<input type="submit" value="Enviar">
		</form>
		"""

	boton_añadir = """
		<form action="" method="POST">
		<input type="submit" name= "añadir" value="Añadir">
		</form>
		"""

	museo =	Museo.objects.get(id=int(number))
	print("nummmm: " + str(museo.NumeroComentarios))
	nombre = museo.Nombre

	comentarios = Comentario.objects.all()
	
	comentarios_museo = "<ul>"
	for comentario in comentarios:
		if comentario.MuseoComentado.Nombre == museo.Nombre:
			comentarios_museo += comentario.Comment + "<br>"
	comentarios_museo += "<ul>"

	respuesta = '<li>'"Dirección: " + museo.Direccion + "<br>" + '<li>'"Descripción: " + museo.Descripcion + "<br>" + '<li>'"Accesibilidad: "+ str(museo.Accesibilidad) + "<br>" + '<li>'"Barrio: " + museo.Barrio + "<br>" + '<li>'"Distrito: " + museo.Distrito + "<br>" + '<li>'"Teléfono: " + museo.Telefono + "<br>" + "<br>" + "<br>" + "<h2>Comentarios:</h2>" + "<br>" + comentarios_museo 


	if request.user.is_authenticated():
		logged = 'Logged in as ' + request.user.username + '<a href=' + "/logout?next=/museos/" + number + '> logout</a>'
		respuesta = boton_añadir + "<br>" + respuesta + "<br>" + formulario_comentario
	else:
		logged = 'Not logged in.' + '<a href=' + "http://localhost:8000/login?next=/museos/" + number + '> login</a>'
		respuesta = respuesta

	if request.method == "POST":	
		coment = request.POST.get("comentario")
		añadido = request.POST.get("añadir")
		if coment:
			comentario_nuevo = Comentario(MuseoComentado = museo, Comment = coment)
			comentario_nuevo.save()
			museo.NumeroComentarios = museo.NumeroComentarios + 1
			museo.save()

			comentarios = Comentario.objects.all()
	
			comentarios_museo = "<ul>"
			for comentario in comentarios:
				if comentario.MuseoComentado.Nombre == museo.Nombre:
					comentarios_museo += comentario.Comment + "<br>"
			comentarios_museo += "<ul>"

			respuesta = '<li>'"Dirección: " + museo.Direccion + "<br>" + '<li>'"Descripción: " + museo.Descripcion + "<br>" + '<li>'"Accesibilidad: "+ str(museo.Accesibilidad) + "<br>" + '<li>'"Barrio: " + museo.Barrio + "<br>" + '<li>'"Distrito: " + museo.Distrito + "<br>" + '<li>'"Teléfono: " + museo.Telefono + "<br>" + "<br>" + "<br>" + "<h2>Comentarios:</h2>" + "<br>" + comentarios_museo 
			if request.user.is_authenticated():
				logged = 'Logged in as ' + request.user.username + '<a href=' + "/logout?next=/museos/" + number + '> logout</a>'
				respuesta = boton_añadir + "<br>" + respuesta + "<br>" + formulario_comentario
			else:
				logged = 'Not logged in.' + '<a href=' + "http://localhost:8000/login?next=/museos/" + number + '> login</a>'
				respuesta = respuesta

		if añadido:
			usuario = User.objects.get(username=request.user.username)
			nuevo_museo_seleccionado = PagPersonal(Usuario = usuario, MuseoSeleccionado = museo)
			nuevo_museo_seleccionado.save()
			respuesta = "Museo añadido a tu página personal" + "<br>" + respuesta + "<br>" + formulario_comentario 
		
		template = get_template("Plantilla_museo/index.html") #	
		c = Context({'logged': logged, 'nombre': nombre, 'content': respuesta})
		return HttpResponse(template.render(c))
	

	l_nombres = []
	users = User.objects.all()
	for user in users:
		nombre_m = user.username
		l_nombres += [nombre_m]

	template = get_template("Plantilla_museo/index.html") #	
	c = Context({'logged': logged, 'nombre': nombre, 'content': respuesta, 'lista_usuarios': l_nombres})
	return HttpResponse(template.render(c))

@csrf_exempt
def usuario(request, name):

	boton_cargar = """
		<form action="" method="POST">
		<input type="submit" name= "cargar" value="Cargar más">
		</form>
		"""

	formulario_titulo = """
		<form action="" method="POST">
		<br>Introduce un título para tu página personal:<br>
			<input type="text" name="nuevo_titulo"><br>
			<input type="submit" value="Enviar">
		</form>
		"""

	formulario_color = """
		<form action="" method="POST">
		<br>Introduce un color para tu página personal:<br>
			<input type="text" name="nuevo_color"><br>
			<input type="submit" value="Enviar">
		</form>
		"""

	formulario_letra = """
		<form action="" method="POST">
		<br>Introduce un tamaño de letra para tu página personal:<br>
			<input type="text" name="nueva_letra"><br>
			<input type="submit" value="Enviar">
		</form>
		"""

	pulsado = request.POST.get("añadir")
	cambio_titulo = request.POST.get("nuevo_titulo")
	cambio_color = request.POST.get("nuevo_color")
	cambio_letra = request.POST.get("nueva_letra")

	paginas = PagPersonal.objects.all()

	try:
		usuario = User.objects.get(username=name)
	except ObjectDoesNotExist:
		nombre = "Este usuario no está registrado"
		template = get_template("Plantilla_personal/index.html") 
		c = Context({'logged': logged, 'nombre': nombre, 'content': ""})
		return HttpResponse(template.render(c))

	respuesta = "<ul>"
	primera_respuesta = "<ul>"
	segunda_respuesta = "<ul>"

	k = 0
	for pag in paginas:
		if usuario.username == pag.Usuario.username:
			nombre = pag.MuseoSeleccionado.Nombre
			direccion = pag.MuseoSeleccionado.Direccion
			url = pag.MuseoSeleccionado.Enlace
			mas_info = '<a href="/museos/' + str(pag.MuseoSeleccionado.id) + '">' + "Más información" + '</a>'
			fecha = str(pag.FechaSeleccion)
			respuesta += '<li>''<a href=' + url + '>' + nombre + '</a>' + "<br>" + direccion + "<br>" + fecha + "<br>" + mas_info + "<br>" + "<br>"
			
			k = k + 1
			if k == 5:
				primera_respuesta = respuesta
				
	respuesta += "<ul>"

	if k < 5:
		contenido = respuesta + boton_cargar

	if k >= 5:
		contenido = primera_respuesta + boton_cargar


	usuario = User.objects.get(username=name)


	if request.method == "POST":
		if pulsado:
			if k > 5:
				contenido = respuesta

			if k <= 5:
				contenido = "No hay más museos"
		
		if cambio_titulo:
			for pag in paginas:
				if usuario.username == pag.Usuario.username:			
					titulo = cambio_titulo
					pag.Titulo = titulo
					pag.save()

		if cambio_color:
			for pag in paginas:
				if usuario.username == pag.Usuario.username:
					color = cambio_color
					pag.Color = color
					pag.save()

		if cambio_letra:
			for pag in paginas:
				if usuario.username == pag.Usuario.username:
					letra = cambio_letra
					pag.TamañoLetra = letra
					pag.save()

	paginapers = PagPersonal.objects.all()
	
	k = 0
	for pag in paginapers:
		if usuario.username == pag.Usuario.username:
			paginaP = pag
			k = k + 1
			if k == 1:
				break
			
	l_nombres = []
	users = User.objects.all()
	for user in users:
		nombre = user.username
		l_nombres += [nombre]

		
	contenido = "<h4>Museos seleccionados por el usuario:</h4>" + "<br>" + "<br>" + contenido
	if request.user.is_authenticated():
		logged = 'Logged in as ' + request.user.username + '<a href=' + "/logout?next=/" + name + '> logout</a>'
		if request.user.username == name:
			contenido = formulario_titulo + "  " + formulario_color + "  " + formulario_letra + "<br>" + contenido
	else:
		logged = 'Not logged in.' + '<a href=' + "http://localhost:8000/login?next=/" + name + '> login</a>'

	template = get_template("Plantilla_personal/index.html") 
	c = Context({'logged': logged, 'nombre': paginaP.Titulo, 'color': paginaP.Color, 'letra': paginaP.TamañoLetra, 'content': contenido, 'lista_usuarios': l_nombres})
	return HttpResponse(template.render(c))

		
def about(request):
	return HttpResponse("Esta es la práctica final de la asignatura Servicios y Aplicaciones en Redes de Ordenadores" + "<br>" + 
						"Realizada por: Sergio Asperilla Díaz")
		#	Nombre = pag.MuseoSeleccionado.Nombre
		#	Descripcion = pag.MuseoSeleccionado.Descripcion
			#Accesibilidad = pag.MuseoSeleccionado.Accesibilidad
		#	Barrio = pag.MuseoSeleccionado.Barrio
			#Distrito = pag.MuseoSeleccionado.Distrito
			#Telefono = pag.MuseoSeleccionado.Telefono
			#Email = pag.MuseoSeleccionado.Email
			#Direccion = pag.MuseoSeleccionado.Direccion
			#CodigoPostal = pag.MuseoSeleccionado.CodigoPostal
			#Enlace = pag.MuseoSeleccionado.Enlace

def xml(request, usuarioxml):
	usuario = User.objects.get(username = usuarioxml)
	paginas = PagPersonal.objects.all()

	nombreuser = usuario.username

	
	template = get_template("Plantilla_xml/index.html") 
	c = Context({'usuario': usuarioxml, 'paginas': paginas, 'nombreuser': nombreuser})#, 'nombre': Nombre, 'descripcion':Descripcion ,'accesibilidad':Accesibilidad, 'barrio':Barrio, 'distrito':Distrito, 'telefono':Telefono,'email':Email,'direccion':Direccion,'codigopostal':CodigoPostal,'enlace':Enlace})
	
	return HttpResponse(template.render(c), content_type = "text/xml")


