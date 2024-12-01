def main():
    while input('Do you want to enter a movie title? ').lower() == 'y':
        movie_title = input('Enter a one word movie title: ')
        code = ''
        if len(movie_title) <= 4:
            code += movie_title
        elif len(movie_title) == 5:
            code += movie_title[0]
            code += movie_title[2]
            code += movie_title[4]
        else:
            code += movie_title[0]
            code += movie_title[2]
            code += movie_title[4]
            code += movie_title[len(movie_title) - 1]

        code += input('What year was this movie released? ')
        print(f'The code for the movie \'{movie_title}\' is {code}')

main()