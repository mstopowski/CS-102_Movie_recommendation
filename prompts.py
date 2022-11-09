from movieMethods import *

def introduction():
    print(("********************************************************************"))
    print("Welcome to the movie selector - MOVEX 9000.")
    print("We'll help you select a movie to watch.")
    show_main_menu()
    selection = input("Type number corresponding to selected action: ")
    return selection

def show_main_menu():
    print("---------------------------------------------------------------------")
    print("Please select next action by typing appropriate number.")
    print("1) View all movies from database (1 at a time)")
    print("2) View all movies from database - sorted")
    print("3) Narrow search by using one of available filters")
    print("4) Select random movie")
    print("5) Use our smart search")

def smart_search_menu():
    print("---------------------------------------------------------------------")
    print("You are now using our smart search.")    

def smart_search_input():
    answer = input("Please type at least 3 characters to initiate search: ")
    return answer

def sort_menu():
    print("---------------------------------------------------------------------")
    print("You can sort movies by:")
    print("1) Title")
    print("2) Year")
    print("3) Genre")
    print("4) Country")
    print("5) Director")
    print("6) Main actor")
    print("7) Length")
    print("8) Rotten audience score")
    answer = input("Select how you want to sort movies (type number from 1 to 8): ")
    return answer

def filter_menu():
    print("---------------------------------------------------------------------")
    print("You can filter movies by:")
    print("1) Genre")
    print("2) Country")
    answer = input("Select how you want to filter movies (type number from 1 to 2): ")
    return answer

def filter_selection(filter_list):
    print("---------------------------------------------------------------------")
    print("Available filters:")
    for item in filter_list:
        print(f"{filter_list.index(item)+1}) {item}")
    answer = input(f"Select filter (type number from 1 to {len(filter_list)}): ")
    return answer

def asc_desc_list():
    print("---------------------------------------------------------------------")
    print("Select how you want to view sorted list")
    print("1) Ascending order")
    print("2) Descending order")
    answer = input("Type 1 or 2: ")
    return answer

def table_of_movies(list):
    print("---------------------------------------------------------------------")
    print("| TITLE | YEAR | GENRE | ORIGIN | DIRECTOR | ACTOR | LENGTH | SCORE |")
    for movie in list:
        print(f"| {get_movie_title(movie)[:5]} | {get_movie_year(movie)} | {get_movie_genre(movie)[0:5]} | {get_movie_origin(movie)[0:6]} | {get_movie_director(movie[0:8])} | {get_movie_actor(movie)[0:5]} | {get_movie_length(movie)} | {get_movie_score(movie)} |")

def movie_decorator(movie):
    print("---------------------------------------------------------------------")
    print(f"TITLE: {get_movie_title(movie)}")
    print(f"YEAR OF PRODUCTION: {get_movie_year(movie)}")
    print(f"GENRE: {get_movie_genre(movie)}")
    print(f"ORIGIN: {get_movie_origin(movie)}")
    print(f"DIRECTOR: {get_movie_director(movie)}")
    print(f"MAIN ACTOR: {get_movie_actor(movie)}")
    print(f"LENGTH: {get_movie_length(movie)}min")
    print(f"AUDIANCE SCORE: {get_movie_score(movie)}/100")

def continue_prompt(index, length_of_list):
    print("---------------------------------------------------------------------")
    print(f"We've shown you {index} out of {length_of_list} movies.")
    result = input("Do you want to continue browsing Y/N? ")
    return result