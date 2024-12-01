def main():
    premier = ('Liverpool', 'Chelsea', 'Arsenal')
    mls = ('LAFC', 'LA Galaxy', 'St. Louis City SC')

    print('Premier Teams:')
    for team in premier:
        print(team)
    
    print('MLS Teams:')
    for i in range(len(mls)):
        print(mls[i])

    (mls1, mls2, mls3) = mls

    soccer_teams = []
    for team in premier:
        soccer_teams.append(team)
    
    for team in mls:
        soccer_teams.append(team)

    print('All Soccer Teams:')
    for team in soccer_teams:
        print(team)

    soccer_teams_tuple = tuple(soccer_teams)
    print('All Soccer Teams (Tuple):')
    for team in soccer_teams:
        print(team)


main()