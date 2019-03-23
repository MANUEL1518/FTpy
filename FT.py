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
            print("       mget: baja archivos en masa")
            print("       mkdir: crea nueva carpeta")
            print("       delete: borra ficheros de directorio")
            print("       rm: borra carpetas")
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
                            print("uploading...")
                            ftp.storbinary('STOR ' + filename, f)
                            f.close()
                        else:
                            if opc=="get":
                                filename=input("(file name)")
                                print("downloading...")
                                ftp.retrbinary('RETR '+filename, open(filename, 'wb').write)
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
                                else:
                                    if opc=="delete":
                                        file = input("(file name)")
                                        ftp.delete(file)
                                    else:
                                        if opc=="rm":
                                            directorio = input("(directorio)")
                                            ftp.rmd(directorio)
                                        else:
                                            if opc=="mkdir":
                                                directorio = input("(nombre de nuevo directorio)")
                                                ftp.mkd(directorio)
                                            else:
                                                if opc=="bye":
                                                    file.close()
                                                    break
                                                else:
                                                    print(opc,"No es un comando elegible")
        except:
            print("no hay conexion")
            ftp.login(nickwite,BEto123321)

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

