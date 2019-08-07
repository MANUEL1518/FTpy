import ftplib
import getpass
import time
import sys
import os

def command():
	print("=================================================")
	print("          Comandos que puedes usar: ")
	print("")
	print(" cd:     coloca en un directorio")
	print(" ls:     enlista contenido de directorio")
	print(" put:    sube archivos a servidor")
	print(" get:    baja archivo de servidor")
	print(" mget:   baja archivos en masa")
	print(" mkdir:  crea nueva carpeta")
	print(" delete: borra ficheros de directorio")
	print(" rm:     borra carpetas")
	print(" bye:    cierra conexion")
	print("")
	print("=================================================")

def comandos():
	try:
		intro_text = input("ftp>")
		intro = intro_text.split(" ")
		opc = intro[0]
		if opc=="cd":
			try:
				direc = intro[1]
			except:
				direc = input("(nombre de carpeta) ")
			try:
				ftp.cwd(direc)
			except:
				print("No hay un directorio llamado asi")
			comandos()
		else:
			if opc=="ls":
				ftp.dir()
				comandos()
			else:
				if opc=="put":
					try:
						filename = intro[1]
					except:
						filename = input("(file name) ")
					f = open(filename, 'rb')
					try:
						print("uploading...")
						ftp.storbinary('STOR ' + filename, f)
						f.close()
					except:
						print("No se encontro un archivo con este nombre")
					comandos()
				else:
					if opc=="get":
						try:
							filename = intro[1]
						except:
							filename = input("(file name) ")
						try:
							print("downloading...")
							ftp.retrbinary('RETR '+filename, open(filename, 'wb').write)
						except:
							print("No se encontro un archivo con este nombre")
						comandos()
					else:
						if opc=="mget":
							filenames = ftp.nlst()
							print("downloading...")
							for filename in filenames:
								local_filename = './' + "'" + filename + "'"
								file = open(local_filename, 'wb')
								ftp.retrbinary('RETR '+ filename, file.write)
							archivos = os.listdir(".")
							for archivo in archivos:
								new = archivo.replace("'", "")
								nombre = new.replace(" ", "_")
								os.rename(archivo, nombre)
							comandos()
						else:
							if opc=="delete":
								try:
									file = intro[1]
								except:
									file = input("(file name) ")
								ftp.delete(file)
								comandos()
							else:
								if opc=="rm":
									try:
										directorio = intro[1]
									except:
										directorio = input("(directorio) ")
									try:
										ftp.rmd(directorio)
									except:
										print("No se encontro un folder con este nombre")
									comandos()
								else:
									if opc=="mkdir":
										try:
											directorio = intro[1]
										except:
											directorio = input("(nombre de nuevo directorio) ")
										try:
											ftp.mkd(directorio)
										except:
											print("No se pudo crear folder")
										comandos()
									else:
										if opc=="bye" or opc=="exit":
											file.close()
											print("Good Bye")
										else:
											if opc=="help":
												command()
												comandos()
											else:
												if opc=="cls" or opc=="clear":
													try:
														try:
															os.system("cls")
														except:
															os.system("clear")
													except:
														print("Este comando no es compatible")
													comandos()
												else:
													print(opc," No es un comando elegible")
													comandos()
	except:
		print("no hay conexion")
		try:
			ftp.login(user, pasd)
			comandos()
		except:
			print("Conexion cerrada")
try:
	host = sys.argv[1]
except:
	host = input("direccion del servidor: ")
try:
    ftp = ftplib.FTP(host)
    try:
    	user = sys.argv[2]
    except:
    	user = input("Nombre de usuario: ")
    pasd = getpass.getpass("Contraseña: ")
    try:
        ftp.login(user, pasd)
        print("[OK]")
        command()
        comandos()
    except:
        print("### Usuario o contraseña incorrecta ###")
except:
    print("### [ERROR] Sintaxis FT.py [HOST] [USER] ###")