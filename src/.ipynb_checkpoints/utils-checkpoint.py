import scipy.stats as stats

def greater_comparison(df1, df2, lst):
    '''
    Compare a list of statistics between two players to see who performs "better"
    (who has less) in certain stats.

    Parameters
    ----------
    df1: pandas dataframe
        Df of all the games an individual player has played in, win or loss
    df2: pandas dataframe
        Df of all the games a second individual player has played in, win or loss
    lst:
        List of all the statistics that we want to compare between the two players.
        In this case, more of the certain statistic is considered to be better
        
    Returns
    -------
    List: Values from the mannwhitneyu; test statistic (wins for the player) and the 
          associated p-value. These values alternate (ie: Num of wins in even indexes 
          and p-values in odd indexes)
    '''
    score_lst = []
    for item in lst:
        wins, p_val = stats.mannwhitneyu(df1[item], df2[item], alternative='greater')
        score_lst.append(wins)
        score_lst.append(p_val)
    return score_lst

def less_comparison(df1, df2, lst):
    '''
    Compare a list of statistics between two players to see who performs "better"
    (who has less) in certain stats.

    Parameters
    ----------
    df1: pandas dataframe
        Df of all the games an individual player has played in, win or loss
    df2: pandas dataframe
        Df of all the games a second individual player has played in, win or loss
    lst:
        List of all the statistics that we want to compare between the two players.
        In this case, less of the certain statistic is considered to be better
        
    Returns
    -------
    List: Values from the mannwhitneyu; test statistic (wins for the player) and the 
          associated p-value. These values alternate (ie: Num of wins in even indexes 
          and p-values in odd indexes)
    '''
    score_lst = []
    for item in lst:
        wins, p_val = stats.mannwhitneyu(df1[item], df2[item], alternative='less')
        score_lst.append(wins)
        score_lst.append(p_val)                                 
    return score_lst

