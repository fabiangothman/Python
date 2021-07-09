#Datatypes
print(type("Hello world"))              #str
print(type(100))                        #int
print(type(100.5))                      #float
print(type(False))                      #bool
print(type([1, 2, 3]))                  #list
print(type(["Hello", "Bye", "Again"]))  #list
print(type([10, "Hello", True, 11.5]))  #list
print(type(None))                       #NoneType

#Inmutables data types (doesn't change)
print(type((10, 30, 55)))               #tuple

#Sets list without index
print(type({"Pedro", "Paco", "Luis"}))  #str

#Dictionaries
print(type({                            #dict
    'name': 'Ryan',
    'age': 15,
    'alias': 'Ry',
    'family': {
        'mom': 'Grey',
        'dad': 'Joseph',
        'grandparents':[
            {
                'type': 'grandmom',
                'name':'Norah'
            },
            {
                'type': 'grandmom',
                'name':'Philliphs'
            }
        ]
    }
}))

#Operators
print("hola_"+"como_"+"estas.")