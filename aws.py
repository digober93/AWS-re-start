#a='hitch'
#y=2000
#v=True
#print('la pelicula es '+str(a)+' '+str(y)+' '+str(v))



peliculas=[
    "The Shawshank Redemption",
    "The Dark Knight",
    "Inception",
    "Pulp Fiction",
    "The Matrix",
    "Interstellar",
    "Parasite",
    "Gladiator",
    "Titanic",
    "The Lord of the Rings: The Fellowship of the Ring"
]

year=[
    1994,
    2008,
    2010,
    1994,
    1999,
    2014,
    2019,
    2000,
    1997,
    2001
]

watched=[
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False
]

for i in range (len(peliculas)):
                print("la peliculas es: ", peliculas[i], "estrenada en el año: ", year[i], "y la has visto?: ", watched[i])