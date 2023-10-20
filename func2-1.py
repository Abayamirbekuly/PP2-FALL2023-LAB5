def above_5_5(movie):
    return movie["imdb"] > 5.5


movie = {
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
}

result = above_5_5(movie)
print(result)  