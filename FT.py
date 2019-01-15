import ftplib
import time
import os
#definir comandos
def comandos():
    while True:
        try:
            print("=================================================")
            print("          Comandos que puedes usar:")
            print("")
            print("       cd: coloca en un directorio")
            print("       ls: enlista contenido de directorio")
            print("       put: sube archivos a servidor")
            print("       get: baja archivo de servidor")
            print("       bye: cierra conexion")
            print("")
            print("=================================================")
            while True:
                opc = input("ftp>")
                if opc=="cd":
                    direc=input("(directorio)")
                    ftp.cwd(direc)
                else:
                    if opc=="ls":
                        ftp.dir()
                    else:
                        if opc=="put":
                            filename=input("(file name)")
                            f = open(filename, 'rb')
                            
                            f.close()
                        else:
                            if opc=="get":
                                filename=input("(file name)")
                                ftp.retrbinary('RETR '+filename, open(filename, 'wb').write)
                            else:
                                if opc=="bye":
                                    ftp.close()
                                    break
                                else:
                                    print(opc,"No es un comando elegible")
        except:
            print("no hay conexion")
            ftp.login(user,pasd)

#Menu de inicio
print("==================Conectar_FTP===================")
print("")
host = input("Escribe el nombre del servidor: ")
try:
    ftp = ftplib.FTP(host)
    #Si se pudo conectar al servidor
    print("Se ha podido conectar excitosamente el host")
    print("=================================================")
    user = input("Ingresa tu Usuario: ")
    pasd = input("Ingresa tu Contrasena: ")
    try:
        ftp.login(user, pasd)
        #Si se pudo acceder con excito
        print("Se ha podido conectar excitosamente tu espacio")
        print("=================================================")
        comandos()
    except:
        #Usuario o contraseña incorrectos
        print("=================================================")
        print("Usuario o contrasena incorrecta :c")
except:
    #Problema al acceder a servidor
    print("=================================================")
    print("Hubo un error. Asegurate que ayas escrito bien el servidor")
