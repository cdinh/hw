def main():
    with open ('misl.txt', 'r') as file:
        (champs, howmany) = get_champs(file)

    for i in range(howmany):
        team = champs[2 * i]
        year = champs[(2 * i) + 1]
        print(f'{team} were the {year} MISL champions.')

def get_champs(file):
    num = 0
    the_list = []
    team = file.readline().rstrip('\n')

    while team:
        year = file.readline().rstrip('\n')
        the_list.append(team)
        the_list.append(year)
        num += 1
        team = file.readline().rstrip('\n')

    return (the_list, num)

main()