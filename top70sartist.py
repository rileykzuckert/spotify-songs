'''
Author: Riley Zuckert
Date: April 25, 2021
Class: ISTA 350
Section Leader: Abby Collier
Assignment: Final Project
Description:
This file scrapes the 'spotify_songs.csv' data from Github's web page and creates a visualization of the top rock artists of the 1970s.
'''
import pandas as pd, matplotlib.pyplot as plt, numpy as np, statsmodels.api as sm
from datetime import datetime

def get_data(url):
    '''
    Thus function cleans the spotify_songs.csv data to get the track album release date, playlist genre, and track popularity variables.
    It also adds in columns for the release date's decade, and finds the top five producing rock artists of the 1970s.
    '''
    df = pd.read_csv(url, usecols=['track_album_release_date', 'playlist_genre', 'track_artist', 'track_popularity'])
    df['decade'] = df['track_album_release_date'].apply(lambda x: str(x) [:3]+'0s')
    seventies_decade = df[df['decade'] == '1970s']
    seventies_rock = seventies_decade[seventies_decade['playlist_genre'] == 'rock']
    artists = seventies_rock.groupby('track_artist').count().decade.nlargest(5)
    return artists

def make_plot(artists, title, ylabel, xlabel):
    '''
    This function plots a bar graph of the top five rock artists with the greatest number of tracks.
    '''
    artists.plot.barh(zorder=3, color=['firebrick', 'darkcyan', 'darkcyan', 'darkcyan', 'darkcyan', 'darkcyan', 'darkcyan', 'darkcyan', 'darkcyan', 'darkcyan'])
    plt.title(title, weight='bold', fontsize=18)
    plt.ylabel(ylabel, weight='bold', fontsize=15)
    plt.xlabel(xlabel, weight='bold', fontsize=15)
    ax = plt.gca()
    ax.set_facecolor('aliceblue')
    plt.grid(zorder=0, axis='x')

#==========================================================
def main():
    '''
    This file scrapes the spotify_songs.csv and creates a visualization of the top producing rock artists.
    '''
    #get_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')
    make_plot(get_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'), 'Top Producing Rock Artists of the 1970s', 'Artist', 'Number of Tracks')
    plt.show()



if __name__ == '__main__':
    main()
