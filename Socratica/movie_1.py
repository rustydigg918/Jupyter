import json
# print(dir(json))

"""
>>> Key Methods:
json.load(f): Load JSON data from file (or file like object)
json.loads(s): Load JSON data from a string.
json.dump(j, f): write JSON objet to file (or file like object)
json.dumps(j): Output JSON object as string.

"""
json_file = open("C:/Users/P RAJ/Jupyter/Socratica/movie_1.txt", "r",encoding = 'utf-8' )
movie = json.load(json_file)
json_file.close()

print (movie)
print(type(movie))
