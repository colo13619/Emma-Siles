from datetime import date, datetime
import os

#menú
def Menu():
    print("\n\tMENÚ PRINCIPAL\n")
    print("1. Agregar nueva tarea.")
    print("2. Ver tareas / Marcar completadas.") #Unificación punto 2 y 3, después de mostrar las tareas pregunta si quiere pasar alguna tarea de pendiente a completada
    print("3. Editar o borrar tareas.")
    print("4. Guardar y cargar cambios al archivo.")
    print("5. Estadísiticas generales.")
    print("6. Salir.\n")

#almacenamiento tareas
pending_tasks = []
complete_tasks = []


#Agregar nueva tarea
def Add_Task (pending_tasks):
    task =[]
    tittle= input("\nAsigne un título para la nueva tarea: ").upper()   #Título tarea
    task.append(tittle)
    description= input("Escriba la descripción de la tarea:\n")         #Descripción tarea
    task.append(description)
    fecha= input("Escriba la fecha límite de la tarea (dd/mm/aaaa): ")  #Fecha límite tarea (texto)
    fecha= datetime.strptime(fecha,"%d/%m/%Y")
    fecha_t= date(fecha.year, fecha.month, fecha.day)             #Fecha límite tarea (datetime.date)
    task.append(fecha_t)
    cost= float(input("Digite el costo en colones de la tarea: ¢"))     #Costo tarea
    task.append(cost)

    #Resumen de la tarea
    print("\n\t  RESUMEN\n")
    print(f"Título:\t\t{task[0]}\nDescripción:\t{task[1]}")
    print("Fecha límite:\t{}/{}/{}".format(fecha_t.day,fecha_t.month,fecha_t.year))
    print(f"Costo:\t\t¢{task[3]}")

    while True:
        add= input("\n¿Desea agregar la tarea a pendientes? (s/n): ").lower() #Desea guardar la tarea en pendientes?
        if add == "s":
            pending_tasks.append(task)                              #Guardado correctamente
            print("\nLa tarea ha sido agregada correctamente.") 
            break
        elif add == "n":
            break       #No guarda la tarea
        else:
            print("\nOpción inválida, por favor intente de nuevo.") #Repite bucle


#Cambiar estado pendiente - completado:
            
def Change_to_Complete(pending_tasks , complete_tasks):
    change = int(input("\nDigite el número de tarea pendiente que desea cambiar a completada: ")) #número de tarea pendiente a cambiar a completada
    if (0 < change) and (change <= len(pending_tasks)): #verifica que esté en rango
        complete_tasks.append(pending_tasks[change-1])  #agrega tarea a completadas
        pending_tasks.pop(change-1) #elimina tarea de pendientes
        print("\nTarea eliminada de tareas pendientes y agregada a tareas completadas.")
    else:
        print("\nLa tarea no existe, por favor intente de nuevo.")

        
#Ver tareas pendientes y completas
def Check_Tasks (pending_tasks,complete_tasks):
    print()
    print("1. Datos del archivo.\n2. Datos de esta ejecución.")
    opt = input("\nSelecciona qué datos quieres visualizar: ")   #escoger si desea ver los datos dentro del archivo o dentro de las variables del programa

    if opt == "1": #datos del archivo
        print("\n________________________________________________________________\n")

        if os.path.isfile("tareas_pendientes.txt") == True:  #si "tareas_pendientes.txt" existe dentro del directorio...
            
            with open ("tareas_pendientes.txt", "r") as Tpendientes:  #abre el documento en modo lectura representado por la variable Tpendientes
                tareas_pendientes= Tpendientes.read().split("\n")     #divide el texto completo en líneas dejando un arreglo con las tareas
            tareas_pendientes.pop()                                   #elimina el último salto de página del archivo

            if len(tareas_pendientes)> 0:                       #Si existen tareas pendientes, mostrar
                print("\nTAREAS PENDIENTES")
                for i in range(len(tareas_pendientes)): 
                    print(f"\nTarea #{i+1}:")
                    task= tareas_pendientes[i].split(",")
                    fecha= task[2]
                    fecha_p= datetime.strptime(fecha,"%Y-%m-%d")
                    fecha= date(fecha_p.year, fecha_p.month, fecha_p.day)
                    print(f"Título:\t\t{task[0]}\nDescripción:\t{task[1]}")
                    print("Fecha límite:\t{}/{}/{}".format(fecha.day,fecha.month,fecha.year))
                    print(f"Costo:\t\t¢{task[3]}")

            else:
                print("\nEl archivo de tareas pendientes no existe, por favor guarde alguna tarea en el archivo. (Opción 4)") 

        else:
            print("\nEl archivo de tareas pendientes no existe, por favor guarde alguna tarea en el archivo. (Opción 4)")

        if os.path.isfile("tareas_completadas.txt") == True:            #si "tareas_completadas.txt" existe dentro del directorio...
            
            with open ("tareas_completadas.txt", "r") as Tcompletadas:  #abre el documento en modo lectura representado por la variable Tcompletadas
                tareas_completadas= Tcompletadas.read().split("\n")     #divide el texto completo en líneas dejando un arreglo con las tareas
            tareas_completadas.pop()                                    #elimina el último salto de página del archivo
            
            if len(tareas_completadas) > 0:                         #Si existen tareas completadas, mostrar
                print("\nTAREAS COMPLETADAS")
                for i in range(len(tareas_completadas)): 
                    print(f"\nTarea #{i+1}:")
                    task= tareas_completadas[i].split(",")
                    fecha= task[2]
                    fecha_c= datetime.strptime(fecha,"%Y-%m-%d")
                    fecha= date(fecha_c.year, fecha_c.month, fecha_c.day)
                    print(f"Título:\t\t{task[0]}\nDescripción:\t{task[1]}")
                    print("Fecha límite:\t{}/{}/{}".format(fecha.day,fecha.month,fecha.year))
                    print(f"Costo:\t\t¢{task[3]}")
            else:
                print("\nEl archivo de tareas completadas no existe, por favor guarde alguna tarea en el archivo. (Opción 4)")
                
        else:
            print("\nEl archivo de tareas completadas no existe, por favor guarde alguna tarea en el archivo. (Opción 4)")

            
        if os.path.isfile("tareas_pendientes.txt") == True:                 #abre una vez más el archivo en modo lectura
            with open ("tareas_pendientes.txt", "r") as Tpendientes:
                tareas_pendientes= Tpendientes.read().split("\n")
            tareas_pendientes.pop()

            if len(tareas_pendientes)> 0:                                   #si existen tareas pendientes, preguntar si desea marcar alguna como completa    
                while True:
                    complete= input("\n¿Desea marcar alguna tarea como completada? (s/n): ").lower()
                    if complete == "n":
                        break
                    elif complete == "s":                                   #en caso de colocar la opción "s", se pedirá el número de tarea a cambiar de archivo
                        change = int(input("\nDigite el número de tarea pendiente que desea cambiar a completa: "))
                        if (0 < change) and (change <= len( tareas_pendientes)):        #si el número está denro del rango...
                            aux= tareas_pendientes[change-1]                            #asignamos a una variable el valor de la tarea a cambiar
                            tareas_pendientes.pop(change-1)                             #se elimina la tarea de pendientes
                            file=open("tareas_pendientes.txt","w")
                            for i in range (len(tareas_pendientes)):
                                file.write(f"{tareas_pendientes[i]}\n")                 #se sobreescribe todo el archivo de pendientes sin el valor indicado
                            file.close()
                            print("\nLa tarea fue eliminada con éxito de tareas pendientes.")

                            if aux not in tareas_completadas:                           #si dicho valor no se encuentra dentro del archivo de tareas completadas, escribirlo
                                with open("tareas_completadas.txt","a")as TC:
                                    TC.write(f"{aux}\n")
                                print("La tarea fue agregada con éxito a tareas completadas")
                                break

                            else:
                                print("\nLa tarea ya existe en completadas.(Duplicada)")    #si se encuentra el valor, no repetirlo
                            
                        else:
                            print("\nOpción inválida, por favor intente de nuevo.")
                    else:
                        print("\nOpción inválida, por favor intente de nuevo.")
                
    elif opt == "2":  #datos de las variables del programa
        print("\n________________________________________________________________\n")
        if (len(pending_tasks) == 0) and (len(complete_tasks) == 0): #si no hay ninguna tarea en las variables
            print("***NO HAY TAREAS PENDIENTES***\n")
            print("***NO HAY TAREAS COMPLETADAS***\n")
        
        elif (len(pending_tasks) > 0) and (len(complete_tasks) == 0):     #Si no hay tareas completadas pero sí pendientes
            print("\nTAREAS PENDIENTES")
            for x in range (len(pending_tasks)):
                fecha= pending_tasks[x][2]      #posición de la fecha en el arreglo
                print(f"\nTAREA #{x+1}:")
                print(f"TÍTULO: {pending_tasks[x][0]}")    #Título
                print(f"DESCRIPCIÓN: {pending_tasks[x][1]}")  #Descripción
                print("FECHA LÍMITE: {}/{}/{}".format(fecha.day,fecha.month,fecha.year)) #Fecha límite
                print(f"COSTO: ¢{pending_tasks[x][3]}\n")
            print("***NO HAY TAREAS COMPLETADAS***\n")
            while True:
                complete= input("\n¿Desea marcar alguna tarea como completada? (s/n): ").lower()
                if complete == "n":
                    break               #No se realiza ninguna acción
                elif complete == "s":
                    Change_to_Complete(pending_tasks , complete_tasks) #Cambia de estado pendiente a completado
                    break
                else:
                    print("\nOpción inválida, por favor intente de nuevo.") #Repite bucle

        elif (len(pending_tasks) == 0) and (len(complete_tasks) > 0):   #si no hay tareas pendientes pero sí completadas
            print("***NO HAY TAREAS PENDIENTES***\n")
            print("\nTAREAS COMPLETADAS")
            for x in range (len(complete_tasks)):
                fecha= complete_tasks[x][2]
                print(f"\nTarea #{x+1}:")
                print(f"TÍTULO: {complete_tasks[x][0]}")        #Título
                print(f"DESCRIPCIÓN: {complete_tasks[x][1]}")   #Descripción
                print("FECHA LÍMITE: {}/{}/{}".format(fecha.day,fecha.month,fecha.year)) #Fecha límite
                print(f"COSTO: ¢{complete_tasks[x][3]}\n")      #Costo
                    
        else:  #en caso de haber tareas en ambas variables
            print("\nTAREAS PENDIENTES")
            for x in range (len(pending_tasks)):
                fecha= pending_tasks[x][2]      #posición de la fecha en el arreglo
                print(f"\nTAREA #{x+1}:")
                print(f"TÍTULO: {pending_tasks[x][0]}")         #Título
                print(f"DESCRIPCIÓN: {pending_tasks[x][1]}")    #Descripción
                print("FECHA LÍMITE: {}/{}/{}".format(fecha.day,fecha.month,fecha.year)) #Fecha límite
                print(f"COSTO: ¢{pending_tasks[x][3]}\n")       #Costo
            print("\nTAREAS COMPLETADAS")
            for x in range (len(complete_tasks)):
                fecha= complete_tasks[x][2]
                print(f"\nTarea #{x+1}:")
                print(f"TÍTULO: {complete_tasks[x][0]}")        #Título
                print(f"DESCRIPCIÓN: {complete_tasks[x][1]}")   #Descripción
                print("FECHA LÍMITE: {}/{}/{}".format(fecha.day,fecha.month,fecha.year)) #Fecha límite
                print(f"COSTO: ¢{complete_tasks[x][3]}\n")      #Costo
            while True:
                complete= input("\n¿Desea marcar alguna tarea como completada? (s/n): ").lower()
                if complete == "n":
                    break               #No se realiza ninguna acción
                elif complete == "s":
                    Change_to_Complete(pending_tasks , complete_tasks) #Cambia de estado pendiente a completado
                    break
                else:
                    print("\nOpción inválida, por favor intente de nuevo.") #Repite bucle"""
    else:
        print("\nOpción incorrecta, por favor intente de nuevo")


# Editar o borrar tareas
def Edit_or_Delete_Task(pending_tasks):
    while True:
        print()
        print("1. Datos del archivo.\n2. Datos de esta ejecución.")
        opt = input("\nSelecciona qué datos quieres editar o borrar: ")   #escoger si desea editar o eliminar los datos dentro del archivo o dentro de las variables del programa

        if opt == "1":  #datos del archivo de pendientes
            if os.path.isfile("tareas_pendientes.txt") == True:                 #abre una vez más el archivo en modo lectura
                with open ("tareas_pendientes.txt", "r") as Tpendientes:
                    tareas_pendientes= Tpendientes.read().split("\n")
                tareas_pendientes.pop()

                if len(tareas_pendientes)> 0:                                   #si existen tareas pendientes, mostrar
                    print("\nTAREAS PENDIENTES")
                    for i in range(len(tareas_pendientes)):
                        print(f"\nTarea #{i+1}:")
                        task= tareas_pendientes[i].split(",")
                        fecha= task[2]
                        fecha_p= datetime.strptime(fecha,"%Y-%m-%d")
                        fecha= date(fecha_p.year, fecha_p.month, fecha_p.day)
                        print(f"Título:\t\t{task[0]}\nDescripción:\t{task[1]}")
                        print("Fecha límite:\t{}/{}/{}".format(fecha.day,fecha.month,fecha.year))
                        print(f"Costo:\t\t¢{task[3]}")

                    task_number = int(input("\nDigite el número de la tarea que desea editar o borrar: ")) - 1 #número de tarea a editar o eliminar
                    if 0 <= task_number < len(tareas_pendientes):  #si el número de tarea está dentro del rango...
                        print("\n1. Editar tarea.")
                        print("2. Borrar tarea.")
                        choice  = input("Seleccione la opción deseada: ")  #elegir si quiere editar o borrar dicha tarea
                        task = tareas_pendientes[task_number].split(",")
                        
                        if choice == "1":  # Editar tarea
                            print("\nEDITAR TAREA\n")
                            print("1. Editar título")
                            print("2. Editar descripción")
                            print("3. Editar fecha límite")
                            print("4. Editar costo")

                            edit_choice = input("\nSeleccione el campo que desea editar: ") #escoger el campo a editar
                            if edit_choice == "1":      #Título
                                new_title = input("\nIngrese el nuevo título: ")
                                task[0] = new_title.upper()
                                tareas_pendientes[task_number] = f"{task[0]},{task[1]},{task[2]},{task[3]}"
                                print("\nTítulo editado correctamente.")

                            elif edit_choice == "2":    #Descripción
                                new_description = input("\nIngrese la nueva descripción: ")
                                task[1] = new_description
                                tareas_pendientes[task_number] = f"{task[0]},{task[1]},{task[2]},{task[3]}"
                                print("\nDescripción editada correctamente.")

                            elif edit_choice == "3":    #Fecha
                                new_date = input("\nIngrese la nueva fecha límite (dd/mm/aaaa): ")
                                new_date = datetime.strptime(new_date, "%d/%m/%Y")
                                new_deadline = date(new_date.year, new_date.month, new_date.day)
                                task[2] = new_deadline
                                tareas_pendientes[task_number] = f"{task[0]},{task[1]},{task[2]},{task[3]}"
                                print("\nFecha límite editada correctamente.")

                            elif edit_choice == "4":    #costo
                                new_cost = float(input("\nIngrese el nuevo costo en colones de la tarea: ¢"))
                                task[3] = new_cost
                                tareas_pendientes[task_number] = f"{task[0]},{task[1]},{task[2]},{task[3]}"
                                print("\nCosto editado correctamente.")

                            else:
                                print("\nOpción inválida.")

                            with open("tareas_pendientes.txt", "w") as Tpendientes:
                                for x in range (len(tareas_pendientes)):
                                    Tpendientes.write(f"{tareas_pendientes[x]}\n")

                        elif choice == "2": #borrar tarea
                            tareas_pendientes.pop(task_number)
                            with open("tareas_pendientes.txt", "w") as Tpendientes:
                                for x in range (len(tareas_pendientes)):
                                    Tpendientes.write(f"{tareas_pendientes[x]}\n")
                            print("\nLa tarea ha sido eliminada satisfactoriamente.")
                        
                    break

                else:
                    print("\nNo hay tareas pendientes dentro del archivo, primero agregue alguna.")
                    break

            else:
                print("\nEl archivo de tareas pendientes no existe, por favor guarde alguna tarea en el archivo. (Opción 4)")
                break




        elif opt == "2": #datos de las variables en ejecución
            if len(pending_tasks) > 0:
                print("\nTAREAS PENDIENTES")
                for x in range (len(pending_tasks)):
                    fecha= pending_tasks[x][2]      #posición de la fecha en el arreglo
                    print(f"\nTAREA #{x+1}:")
                    print(f"TÍTULO: {pending_tasks[x][0]}")    #Título
                    print(f"DESCRIPCIÓN: {pending_tasks[x][1]}")  #Descripción
                    print("FECHA LÍMITE: {}/{}/{}".format(fecha.day,fecha.month,fecha.year)) #Fecha límite
                    print(f"COSTO: ¢{pending_tasks[x][3]}\n")
                    
                task_number = int(input("\nDigite el número de la tarea que desea editar o borrar: ")) - 1 #número de tarea a editar o eliminar
                if 0 <= task_number < len(pending_tasks):  #si el número de tarea está dentro del rango...
                    print("\n1. Editar tarea.")
                    print("2. Borrar tarea.")
                    choice  = input("Seleccione la opción deseada: ")  #elegir si quiere editar o borrar dicha tarea
                    if choice == "1":  # Editar tarea
                        print("\nEDITAR TAREA\n")
                        print("1. Editar título")
                        print("2. Editar descripción")
                        print("3. Editar fecha límite")
                        print("4. Editar costo")
                        
                        edit_choice = input("\nSeleccione el campo que desea editar: ") #escoger el campo a editar
                        if edit_choice == "1":      #Título
                            new_title = input("\nIngrese el nuevo título: ")
                            pending_tasks[task_number][0] = new_title.upper()
                            print("\nTítulo editado correctamente.")
                            break
                            
                        elif edit_choice == "2":    #Descripción
                            new_description = input("\nIngrese la nueva descripción: ")
                            pending_tasks[task_number][1] = new_description
                            print("\nDescripción editada correctamente.")
                            break
                            
                        elif edit_choice == "3":    #Fecha
                            new_date = input("\nIngrese la nueva fecha límite (dd/mm/aaaa): ")
                            new_date = datetime.strptime(new_date, "%d/%m/%Y")
                            new_deadline = date(new_date.year, new_date.month, new_date.day)
                            pending_tasks[task_number][2] = new_deadline
                            print("\nFecha límite editada correctamente.")
                            break
                            
                        elif edit_choice == "4":    #costo
                            new_cost = float(input("\nIngrese el nuevo costo en colones de la tarea: ¢"))
                            pending_tasks[task_number][3] = new_cost
                            print("\nCosto editado correctamente.")
                            break
                            
                        else:
                            print("\nOpción inválida.")
                            
                    elif choice == "2":  # Borrar tarea
                        pending_tasks.pop(task_number)
                        print("\nTarea eliminada correctamente.")
                        break
                    
                    else:
                        print("\nOpción inválida.")
                else:
                    print("\nEl número de tarea ingresado no es válido.")


            else:
                print("\nNo hay datos en la variable de tareas pendientes en ejecución.")

        else:
            print("\nOpción incorrecta, por favor intente de nuevo")
        

#GUARDAR Y CARGAR CAMBIOS AL ARCHIVO
def Save_files (pending_tasks, complete_tasks):
    if len(pending_tasks) > 0:  #si hay tareas pendientes en la variable
        if os.path.isfile("tareas_pendientes.txt") == True: #si existe el archivo de tareas pendientes
            Tpendientes= open("tareas_pendientes.txt", "r+")    #abrir en modo lectura
            tareas_pendientes= Tpendientes.read().split("\n")   #separar por líneas
            tareas_pendientes.pop()                             #eliminar último salto de página
            tpendientes_lista=[]                                #crear una lista para cada tarea
            for i in range (len(tareas_pendientes)):            #recorre las líneas del archivo
                task = tareas_pendientes[i].split(",")          #divide cada tarea en valores 
                tpendientes_lista.append(task)                  #agrega la lista "task" a la lista bidimensional
            for x in range (len(pending_tasks)):
                pending_tasks[x][2] = str(pending_tasks[x][2])  #cambia el valor de la fecha en la variable a string
                pending_tasks[x][3] = str(pending_tasks[x][3])  #cambia el valor de la fecha en la variable a string
                
                if pending_tasks[x] not in tpendientes_lista:   #compara tareas dentro de la variable y el archivo
                    Tpendientes.write(f"{pending_tasks[x][0]},{pending_tasks[x][1]},{pending_tasks[x][2]},{pending_tasks[x][3]}\n") #en caso de no existir, agrega
                    print(f"\nTarea #{x+1} fue agregada al archivo de tareas pendientes.")
                else:
                    print(f"\nTarea #{x+1} ya existe en el archivo de tareas pendientes.")

                pending_date = datetime.strptime(pending_tasks[x][2],"%Y-%m-%d")                    #se devuelven los 2 valores a su tipo original, para no crear conflicto
                pending_tasks[x][2] = date(pending_date.year,pending_date.month,pending_date.day)
                pending_tasks[x][3] = float(pending_tasks[x][3])
                
            Tpendientes.close()

        else:   #si el archivo no exíste lo crea
            with open("tareas_pendientes.txt","w") as Tpendientes:
                for x in range (len(pending_tasks)):
                    Tpendientes.write(f"{pending_tasks[x][0]},{pending_tasks[x][1]},{pending_tasks[x][2]},{pending_tasks[x][3]}\n") #agrega todas las líneas de la variable pending_tasks
    else:
        print("\nNo hay tareas pendientes que actualizar al archivo.")

    if len(complete_tasks) > 0: #si hay tareas completadas en la variable
        if os.path.isfile("tareas_completadas.txt") == True:        #si existe el archivo de tareas completadas
            Tcompletadas= open("tareas_completadas.txt", "r+")      #abrir en modo lectura
            tareas_completadas= Tcompletadas.read().split("\n")     #separar por líneas
            tareas_completadas.pop()                                #eliminar último salto de página
            tcompletadas_lista=[]                                   #crear una lista para cada tarea
            for i in range (len(tareas_completadas)):               #recorre las líneas del archivo
                task = tareas_completadas[i].split(",")             #divide cada tarea en valores 
                tcompletadas_lista.append(task)                     #agrega la lista "task" a la lista bidimensional
            for x in range (len(complete_tasks)):
                complete_tasks[x][2] = str(complete_tasks[x][2])    #cambia el valor de la fecha en la variable a string
                complete_tasks[x][3] = str(complete_tasks[x][3])    #cambia el valor de la fecha en la variable a string
                
                if complete_tasks[x] not in tcompletadas_lista:     #compara tareas dentro de la variable y el archivo
                    Tcompletadas.write(f"{complete_tasks[x][0]},{complete_tasks[x][1]},{complete_tasks[x][2]},{complete_tasks[x][3]}\n") #en caso de no existir, agrega
                    print(f"\nTarea #{x+1} fue agregada al archivo de tareas completadas.")
                else:
                    print(f"\nTarea #{x+1} ya existe en el archivo de tareas completadas.")

                complete_date = datetime.strptime(complete_tasks[x][2],"%Y-%m-%d")                  #se devuelven los 2 valores a su tipo original, para no crear conflicto
                complete_tasks[x][2] = date(complete_date.year,complete_date.month,complete_date.day)
                complete_tasks[x][3] = float(complete_tasks[x][3])
                
            Tcompletadas.close()

        else:   #si el archivo no exíste lo crea
            with open("tareas_completadas.txt", "w") as Tcompletadas:
                for i in range(len(complete_tasks)):
                    Tcompletadas.write(f"{complete_tasks[i][0]},{complete_tasks[i][1]},{complete_tasks[i][2]},{complete_tasks[i][3]}\n")
                print(f"Tarea #{i+1} fue agregada al archivo de tareas completadas.")

    else:
        print("\nNo hay tareas completadas que actualizar al archivo.")
        
#Bucle de ejecución
while True:
    Menu()
    opt = input("Digite la opción que desea realizar: ") #solicita opción del menú a ejecutar

    #condicionales del menú
    if opt == "1":
        print("\n________________________________________________________________\n")
        print("\nAGREGAR NUEVA TAREA")
        Add_Task(pending_tasks)  #Llama función para agregar una nueva tarea
        input("\nPresione la tecla enter para salir al menú principal...")

    elif opt == "2":
        print("\n________________________________________________________________\n")
        print("\nVER TAREAS / MARCAR COMPLETADAS\n")
        Check_Tasks(pending_tasks,complete_tasks) #Llama función de ver tareas y marcar completadas
        input("\nPresione la tecla enter para salir al menú principal...")

    elif opt == "3":
        print("\nEDITAR O BORRAR TAREAS")
        Edit_or_Delete_Task(pending_tasks)  #Llama función de editar o eliminar 
        input("\nPresione la tecla enter para salir al menú principal...")

    elif opt == "4":
        print("\nGUARDAR Y CARGAR CAMBIOS AL ARCHIVO")
        Save_files(pending_tasks, complete_tasks)   #Llama función de guardar y cargar cambios al archivo
        input("\nPresione la tecla enter para salir al menú principal...")

    elif opt == "5":
        print("\nESTADÍSTICAS GENERALES")
        input("\nPresione la tecla enter para salir al menú principal...")

    elif opt == "6":
        break

    else:
        print("\nOpción inválida, por favor intente de nuevo.")
        input("\nPresione la tecla enter para salir al menú principal...")

print("\n¡¡Muchas gracias por utilizar nuestro programa!!")
