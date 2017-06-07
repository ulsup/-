import tmdbsimple as data
data.API_KEY = '6fe3abae4ea97076bce8490e936ac183'

def example_1():
    search_1 = data.Search()
    response_1 = search_1.movie(query='Star Wars')
    for s in search_1.results:
        print(s['title'], s['id'], s['release_date'], s['popularity'])

example_1()

def example_2():
    search_2 = data.Search()
    response_2 = search_2.person(query='Emma Roberts')
    for i in search_2.results:
        print(i['popularity'], i['id'], i['name'], i['known_for'])

example_2()