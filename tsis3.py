movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def function_1(movie):
    for part in movies:
        if movie in part.values():
            if part["imdb"] >= 5.5:
                return True
    return False
print(function_1("We Two"))
def function_2(movie):
    for part in movies:
        if movie in part.values():
            if part["imdb"] >= 5.5:
                return (part)
    return (False)
print(function_2("We Two"))
def function_3(category):
    films = []
    for part in movies:
        if category in part.values():
            films.append(part["name"])
    return films
print (function_3("Romance"))
def function_4(films):
    allimdb = 0
    n = 0
    for part in movies:
        for film in films:
            if film in part.values():
                allimdb += int(part["imdb"])
                n = 1 + n
    return allimdb/n
print (function_4(['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']))

def function_5(category):
    all = 0
    n = 0
    for part in movies:
        if category in part.values():
            all += int(part["imdb"])
            n =1+n
    return all/n
print(function_5("Romance"))

