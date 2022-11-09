import random
from movieData import movie_data

def get_movie_title(movie):
    return movie[0]

def get_movie_year(movie):
    return movie[1]

def get_movie_genre(movie):
    return movie[2]

def get_movie_origin(movie):
    return movie[3]

def get_movie_director(movie):
    return movie[4]

def get_movie_actor(movie):
    return movie[5]

def get_movie_length(movie):
    return movie[6]

def get_movie_score(movie):
    return movie[7]

def get_random_movie(list):
    return list[random.randint(0, len(list)+1)]

def temp_name(seq, movieList):
    result = []
    for movie in movieList:
        if sequence_in_movie(movie, seq) == True:
            result.append(movie)
    return result

def sequence_in_movie(movie, seq):
    result = False
    for item in movie:
        if sequence_in_item(item, seq) == True:
            result = True
            break
    return result

def sequence_in_item(item, seq):
    result = False
    _item = str(item).lower()
    _seq = str(seq).lower()
    for i in range(len(_item)):
        count = 0
        if _item[i] == _seq[0]:
            for j in range(len(_seq)):
                try:
                    if _item[i+j] == _seq[j]:
                        count += 1
                    else:
                        break
                except IndexError:
                    pass
        if count == len(_seq):
            result = True
            break
    return result