import movieData
import movieMethods as mm
import prompts as pr
import heapq

#Import movie database and store it under a variable
movieList = movieData.movie_data

if __name__ == "__main__":
    selection = int(pr.introduction())
    while selection not in range(1,6,1):
        selection = int(pr.introduction())
    if selection == 1:
        interested = True
        index = 1
        pr.table_of_movies(movieList)
    elif selection == 2:
        sort = int(pr.sort_menu())
        while sort not in range(1,9,1):
            sort = int(pr.sort_menu())
        order = int(pr.asc_desc_list())
        while order not in range(1,3,1):
            order = int(pr.asc_desc_list())
        _movieList = movieList.copy()
        if sort == 1:
            _movieList.sort(key=mm.get_movie_title)
        elif sort == 2:
            _movieList.sort(key=mm.get_movie_year)
        elif sort == 3:
            _movieList.sort(key=mm.get_movie_genre)
        elif sort == 4:
            _movieList.sort(key=mm.get_movie_origin)
        elif sort == 5:
            _movieList.sort(key=mm.get_movie_director)
        elif sort == 6:
            _movieList.sort(key=mm.get_movie_actor)
        elif sort == 7:
            _movieList.sort(key=mm.get_movie_length)
        elif sort == 8:
            _movieList.sort(key=mm.get_movie_score)
        if order == 2:
            _movieList.reverse()
        pr.table_of_movies(_movieList)
    elif selection == 3:
        filter_method = int(pr.filter_menu())
        while filter_method not in range(1, 3, 1):
            filter_method = int(pr.filter_menu())
        _movieList = movieList.copy()
        filter_list = []
        if filter_method == 1:
            for movie in _movieList:
                filter_list.append(mm.get_movie_genre(movie))
        elif filter_method == 2:
            for movie in _movieList:
                filter_list.append(mm.get_movie_origin(movie))
        filter_list = list(dict.fromkeys(filter_list))
        filter_index = int(pr.filter_selection(filter_list)) - 1
        filter = filter_list[filter_index]
        list_to_print = []
        for movie in _movieList:
            if filter in movie:
                list_to_print.append(movie)
        pr.table_of_movies(list_to_print)
    elif selection == 4:
        selected_movie = mm.get_random_movie(movieList)
        pr.movie_decorator(selected_movie)
    elif selection == 5:
        pr.smart_search_menu()
        seq = pr.smart_search_input()
        while len(seq) < 3:
            seq = pr.smart_search_input()
        _temp = mm.temp_name(seq, movieList)
        if _temp != []:
            pr.table_of_movies(_temp)
        else:
            print("Uups. Nothing was found in our database.")