'''
Author: Riley Zuckert
Date: April 25, 2021
Class: ISTA 350
Section Leader: Abby Collier
Assignment: Final Project
Description:
This file scrapes the 'spotify_songs.csv' data from Github's web page and creates a visualization of Queen's tracks by popularity and tempo.
'''
import pandas as pd, matplotlib.pyplot as plt, numpy as np, statsmodels.api as sm
from datetime import datetime

def get_data(url):
    '''
    This function cleans the spotify_songs.csv data to get the track album release date, playlist genre, track popularity, track name, and tempo variables.
    It also adds in columns for the release date's decade, and finds data surrounding Queen's 1970's rock tracks.
    '''
    df = pd.read_csv(url, usecols=['track_album_release_date', 'playlist_genre', 'track_artist', 'track_popularity', 'track_name', 'tempo'])
    df['decade'] = df['track_album_release_date'].apply(lambda x: str(x) [:3]+'0s')
    seventies_decade = df[df['decade'] == '1970s']
    seventies_rock = seventies_decade[seventies_decade['playlist_genre'] == 'rock']
    queen_df = seventies_rock[seventies_rock['track_artist'] == 'Queen']
    s = pd.DataFrame(index=queen_df['tempo'].values, data=queen_df['track_popularity'].values)
    # get top 10 most popular tracks
    #top_tracks = queen_df.groupby('track_name').max().track_popularity.nlargest(10)
    # get top 10 fastest tracks
    #top_tempo = queen_df.groupby('track_name').max().tempo.nlargest(10)
    #return top_tracks, top_tempo
    return s
                        
def make_plot(s, title, ylabel, xlabel):
    '''
    This function plots a scatter plot with a regression line of Queen's tracks based upon track popularity and tempo.
    '''
    x = s.index.values
    y = s.values
    s.plot(marker='o', linestyle='', color='mediumslateblue')
    plt.title(title, weight='bold', fontsize=18)
    plt.xlabel(xlabel, weight='bold', fontsize=15)
    plt.ylabel(ylabel, weight='bold', fontsize=15)
    x = s.index.values
    X = sm.add_constant(x)
    model = sm.OLS(s, X)
    line = model.fit()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, color='maroon', linewidth=2)
    plt.legend()
    ax = plt.gca()
    ax.set_facecolor('ghostwhite')
    ax.get_legend().remove()
    plt.grid()
    #print(line.summary())

#==========================================================
def main():
    '''
    This file scrapes the spotify_songs.csv and creates a visualization of Queen's tracks mapping popularity versus tempo.
    '''
    make_plot(get_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'), 'Popularity of 1970s Queen Album Tracks by Tempo', 'Track Popularity', 'Tempo')
    plt.show()



if __name__ == '__main__':
    main()
