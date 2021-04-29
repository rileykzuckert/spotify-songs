'''
Author: Riley Zuckert
Date: April 25, 2021
Class: ISTA 350
Section Leader: Abby Collier
Assignment: Final Project
Description:
This file scrapes the 'spotify_songs.csv' data from Github's web page and creates visualizations of the of the top music genres of the 1970s.
'''
import pandas as pd, matplotlib.pyplot as plt, numpy as np, statsmodels.api as sm
from datetime import datetime

def get_data(url):
    '''
    This function cleans the spotify_songs.csv data to get the track album release date and playlist genre variables.
    It also adds in columns for the release date's decade, and finds the frequency of the tracks per playlist genre in the decade.
    '''
    df = pd.read_csv(url, usecols=['track_album_release_date', 'playlist_genre'])
    df['decade'] = df['track_album_release_date'].apply(lambda x: str(x) [:3]+'0s')
    seventies_decade = df[df['decade'] == '1970s']
    counts = seventies_decade.groupby('playlist_genre').count().decade
    return counts

def make_plot(counts, title, ylabel, xlabel):
    '''
    This function plots a bar graph of the genres with the greatest frequencies of tracks.
    '''
    counts.plot.barh(zorder=3, color=['teal', 'teal', 'teal', 'teal', 'teal', 'firebrick'])
    plt.title(title, weight='bold', fontsize=18, labelpad=10)
    plt.ylabel(ylabel, weight='bold', fontsize=15, labelpad=5)
    plt.xlabel(xlabel, weight='bold', fontsize=15, labelpad=5)
    ax = plt.gca()
    ax.set_facecolor('ghostwhite')
    plt.grid(zorder=0, axis='x')
    
def make_plot2(counts, title, ylabel, xlabel):
    '''
    This function removes the rock genre from the previous plot.
    '''
    no_rock = counts.drop('rock')
    no_rock.plot.barh(zorder=3, color=['teal', 'teal', 'teal', 'firebrick', 'teal'])
    plt.title(title, weight='bold', fontsize=18, labelpad=10)
    plt.ylabel(ylabel, weight='bold', fontsize=15, labelpad=5)
    plt.xlabel(xlabel, weight='bold', fontsize=15, labelpad=5)
    ax = plt.gca()
    ax.set_facecolor('ghostwhite')
    plt.grid(zorder=0, axis='x')

def make_plot3():
    '''
    This function plots a pie chart of the frequency distribution of the genres.
    '''
    labels = ['rock (90.06%)', 'r&b (6.31%)', 'rap (0.93%)', 'pop (1.86%)', 'latin (0.41%)', 'edm (0.41%)']
    pie_labels = ['rock', 'r&b', 'rap', 'pop', 'latin', 'edm']
    colors = ['maroon', 'darkmagenta', 'mediumslateblue', 'aqua', 'orange', 'hotpink']
    sizes = [90.06, 6.31, 0.93, 1.86, 0.41, 0.41]
    fig1, ax1 = plt.subplots()
    explode = (0.1, 0, 0, 0, 0, 0)
    ax1.axis('equal')
    plt.title('Track Distribution Across Genres in the 70s', weight='bold', fontsize=18)
    ax1.pie(sizes,labels=None, shadow=False, startangle=90, explode=explode, colors=colors)
    plt.legend(labels=labels, loc="best", title='Genres')
    plt.tight_layout()
    plt.show()

#==========================================================
def main():
    '''
    This file scrapes the spotify_songs.csv and creates three visualizations of the music genres of the 1970s.
    '''
    make_plot(get_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'), 'Top Music Genre of the 1970s', 'Genre', 'Number of Tracks')
    plt.show()
    make_plot2(get_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'), 'Music Genres of the 1970s,\n excluding the rock genre', 'Genre', 'Number of Tracks')
    plt.show()
    plt.show(make_plot3())

if __name__ == '__main__':
    main()
