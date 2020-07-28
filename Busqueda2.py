import sys, os
import smtplib
import subprocess
import glob
from datetime import datetime,timedelta

def enviomail(destino,asunto):
	fromaddr = 'AvisoRamsomware@xxxxx.xx'
	toaddrs  = destino
	user = 'autoriza'
	passw = 'autoriza4732()'
	subj = asunto
	#mensaje = args.argmailhtm
	mensaje = """Aviso de posible Ramsomware mire el fichero de log EL ORDENADOR SERA APAGADO<br/> <br/> 
	Este es un <b>e-mail</b> enviando desde <b>Python</b> 
	"""
	msg =  "From: %s\n" % fromaddr
	msg += "To: %s\n" % toaddrs
	msg += "MIME-Version: 1.0\n"
	msg += "Content-type: text/html\n"
	msg += "Subject:%s\n" % subj
	msg += "\n"
	msg += "%s" % mensaje
	server = smtplib.SMTP('xxx.xxx.xxx.xxx')
	#server.starttls()
	server.login(user,passw)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()


buscar = "xxxxx"
directorio = os.getcwd()
total = 0
salir = False
hora = datetime.now()
enviado = 0

f = open(sys.argv[1] + "extensiones.txt","r")
d = open(sys.argv[1] + "directorios.txt","r")

extensiones = f.read().splitlines()
f.close()
directorios = d.read().splitlines()
d.close()
#print(extensiones)
l = open(sys.argv[1] + "extensiones.log","a")
while True:
	primero = 0
	l.close()
	l = open(sys.argv[1] + "extensiones.log","a")
	horaant = hora
	for directorio in directorios:
		#print(directorio)
		if primero == 0:
			hora = datetime.now()
			#print (str(hora - horaant))
			if (hora - horaant) > timedelta(seconds=300) and enviado == 0:
				enviomail("xxxxx@xxxxx.xx","Parece que estoy tardando")
				enviado = 1
			#if (hora - horaant) == 
			l.write(str(datetime.now()) + directorio + ' ' + '\n')
			primero = 1
		for extension in extensiones:
			#print(extension)
			for file in sorted(glob.glob(directorio + '**/'+ extension,recursive=True)):
				#print(file)
				l.write(str(datetime.now()) + extension + ' ' + file + '\n')
				total = 1
				break
			else:
				continue
			break
		else:
			continue
		break
	else:
		continue
	break
if total > 0:
	l.close()
	enviomail("xxxxxx@xxxxx.xx","He encontrado algo")
	#subprocess.call("shutdown -l ")
