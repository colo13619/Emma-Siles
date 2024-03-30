from datetime import date, datetime

#menú
def Menu():
    print("\n\tMENÚ PRINCIPAL\n")
    print("1. Agregar nueva tarea.")
    print("2. Ver tareas / Marcar completadas.")
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
    deadline_date= date(fecha.year, fecha.month, fecha.day)             #Fecha límite tarea (datetime.date)
    task.append(deadline_date)
    cost= float(input("Digite el costo en colones de la tarea: ¢"))     #Costo tarea
    task.append(cost)
    print("\n\t  RESUMEN\n")
    print(f"Título:\t\t{task[0]}\nDescripción:\t{task[1]}")
    print("Fecha límite:\t{}/{}/{}".format(fecha.day,fecha.month,fecha.year))
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
    change = int(input("\nDigite el número de tarea pendiente que desea cambiar a completa: "))
    if (0 < change) and (change <= len(pending_tasks)):
        complete_tasks.append(pending_tasks[change-1])
        pending_tasks.pop(change-1)
        print("\nTarea eliminada de tareas pendientes y agregada a tareas completadas.")
    else:
        print("\nLa tarea no existe, por favor intente de nuevo.")

        
#Ver tareas pendientes y completas
def Check_Tasks (pending_tasks , complete_tasks):
    if (len(pending_tasks) == 0) and (len(complete_tasks) == 0):
        print("***NO HAY TAREAS PENDIENTES***\n")
        print("***NO HAY TAREAS COMPLETADAS***\n")
    
    elif (len(pending_tasks) > 0) and (len(complete_tasks) == 0):        #Si no hay tareas completas
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

    elif (len(pending_tasks) == 0) and (len(complete_tasks) > 0):
        print("***NO HAY TAREAS PENDIENTES***\n")
        print("\nTAREAS COMPLETADAS")
        for x in range (len(complete_tasks)):
            fecha= complete_tasks[x][2]
            print(f"\nTarea #{x+1}:")
            print(f"TÍTULO: {complete_tasks[x][0]}")        #Título
            print(f"DESCRIPCIÓN: {complete_tasks[x][1]}")   #Descripción
            print("FECHA LÍMITE: {}/{}/{}".format(fecha.day,fecha.month,fecha.year)) #Fecha límite
            print(f"COSTO: ¢{complete_tasks[x][3]}\n")      #Costo
                
    else:
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
                print("\nOpción inválida, por favor intente de nuevo.") #Repite bucle


# Editar o borrar tareas
def Edit_or_Delete_Task(pending_tasks):
    task_number = int(input("\nDigite el número de la tarea que desea editar o borrar: ")) - 1
    if 0 <= task_number < len(pending_tasks):
        print("\n1. Editar tarea.")
        print("2. Borrar tarea.")
        choice  = input("Seleccione la opción deseada: ")
        if choice == "1":  # Editar tarea
            print("\nEDITAR TAREA\n")
            print("1. Editar título")
            print("2. Editar descripción")
            print("3. Editar fecha límite")
            print("4. Editar costo")
            edit_choice = input("Seleccione el campo que desea editar: ")
            if edit_choice == "1":
                new_title = input("Ingrese el nuevo título: ")
                pending_tasks[task_number][0] = new_title.upper()
                print("Título editado correctamente.")
            elif edit_choice == "2":
                new_description = input("Ingrese la nueva descripción: ")
                pending_tasks[task_number][1] = new_description
                print("Descripción editada correctamente.")
            elif edit_choice == "3":
                new_date = input("Ingrese la nueva fecha límite (dd/mm/aaaa): ")
                new_date = datetime.strptime(new_date, "%d/%m/%Y")
                new_deadline = date(new_date.year, new_date.month, new_date.day)
                pending_tasks[task_number][2] = new_deadline
                print("Fecha límite editada correctamente.")
            elif edit_choice == "4":
                new_cost = float(input("Ingrese el nuevo costo en colones de la tarea: ¢"))
                pending_tasks[task_number][3] = new_cost
                print("Costo editado correctamente.")
            else:
                print("\nOpción inválida.")
        elif choice == "2":  # Borrar tarea
            del pending_tasks[task_number]
            print("\nTarea eliminada correctamente.")
        else:
            print("\nOpción inválida.")
    else:
        print("\nEl número de tarea ingresado no es válido.")
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
        Check_Tasks(pending_tasks , complete_tasks) #Llama función de ver tareas y marcar completadas
        input("\nPresione la tecla enter para salir al menú principal...")

    elif opt == "3":
        print("\nEDITAR O BORRAR TAREAS")
        Edit_or_Delete_Task(pending_tasks)  #Llama función de editar o eliminar 
        input("\nPresione la tecla enter para salir al menú principal...")

    elif opt == "4":
        print("\nGUARDAR Y CARGAR CAMBIOS AL ARCHIVO")
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
