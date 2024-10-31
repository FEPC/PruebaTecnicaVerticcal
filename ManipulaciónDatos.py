leads = [
{"id": 1, "name": "Ana Salcedo", "location": "Medellín", "budget": 200000000},
{"id": 2, "name": "Santiago Gallo", "location": "Medellín", "budget": 500000000},
{"id": 3, "name": "Carlota Habib", "location": "Medellín", "budget": 650000000},
{"id": 4, "name": "Pablo Sánchez", "location": "Bogotá", "budget": 350000000},
{"id": 5, "name": "Manuel Franco", "location": "Bogotá", "budget": 150000000},
# ... más leads
]

#Filtrado de datos por lugar
def filtrado(location):
    #Variable donde se guardaran los elementos del filtro = filtro
    filtro = []
    #Busqueda de los elementos que cumplen la condición dentro de los Leads
    for i in range(0,len(leads)):
        if leads[i].get('location') == location:
            filtro.append(leads[i])
    #Impresión del filtro
    print("Elementos Filtrados:")
    print(filtro)
    #Retorno de la lista de filtrados
    return filtro

#Sumatoria de presupuestos 
def sumatoria(location):
    #Llamada de función de filtro para crear una lista solo con los elementos deseados
    leadsF = filtrado(location)
    #Variable donde se sumaran los presupuestos
    resultado = 0
    #Suma de cada uno de los elementos de la lista
    for i in range(0,len(leadsF)):
        resultado += leadsF[i].get('budget')
    #Impresión del resultado
    print("Sumatoria de elementos filtrados: " + str(resultado))

#Organización de los elementos de leads de mayor a menor
def ordenar():
    #Variable donde se tomaran los presupuestos
    presupuestos = []
    #Variable donde se quitaran los elementos repetidos
    presupuestosR = []
    #Lista donde se guardaran los elementos de forma ordenada
    leadsO = []
    #Obtención de los presupuestos
    for i in range(0,len(leads)):
        presupuestos.append(leads[i].get('budget'))
    #Organización de la lista de mayor a menor
    presupuestos.sort(reverse = True)
    #Adición de los elementos no repetidos
    for i in range(0,len(presupuestos)):
        if presupuestos[i] not in presupuestosR[:i]:
            presupuestosR.append(presupuestos[i])
    #Adición de los elementos de la lista de forma ordenada
    for i in range(0,len(presupuestos)):
        for j in range(0,len(leads)):
            if leads[j].get('budget') == presupuestos[i]:
                leadsO.append(leads[j])
    #Impresión de least ordenada
    print("Elementos Ordenados:")
    print(leadsO)
        
