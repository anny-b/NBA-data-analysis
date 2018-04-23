import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def hw_plot(df, pl, year, n):
    df1=df[['Player','Age', 'Tm', 'G']]
    df2=df[df['Year']==year][['Player', 'PTS', 'Tm', 'Pos', 'G','3P','3P%','Year']]
    top_scorers_year = df2.sort_values(by='PTS', ascending=False)[0:n]
    df2['Avpoints']=df['PTS']/df['G']
    top_avg_scorers_year=df2.sort_values(by='Avpoints', ascending=False)[0:n]

    top_players_heights=pd.merge(pl[['Player', 'height', 'weight']], top_avg_scorers_year, on='Player')
    plt.figure(figsize=(15,10))

    ax=plt.axes()
    ax.set_xlabel('Height[cm]',fontsize=20)
    ax.set_ylabel('Weight[Kgs]',fontsize=20)
    ax.set_title('Heights and weights of top players in terms of position',fontsize=25)
    pts1 = plt.scatter(top_players_heights['height'],top_players_heights['weight'])
    labels1=top_players_heights['Player'].ravel()
    xs=top_players_heights['height'].ravel()
    ys=top_players_heights['weight'].ravel()

    pos=top_players_heights['Pos'].ravel()
    colors = {'PG': 'r', 'SG': 'b', 'SF':'g', 'C':'m', 'PF':'y'}
    cols=[colors[p] for p in pos]

    for label,p,x,y  in zip(labels1,pos,xs,ys):
        plt.annotate(
            label, xy=(x,y), xytext=(-10,10),
            textcoords='offset points', ha='right', va='bottom',rotation=0,
            bbox=dict(boxstyle='round,pad=0.5', fc=colors[p], alpha=0.5),
                    arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0')
    )

    red_dot = mpatches.Patch(color='red', label='PG')
    blue_dot = mpatches.Patch(color='blue', label='SG')
    green_dot = mpatches.Patch(color='green', label='SF')
    magenta_dot = mpatches.Patch(color='magenta', label='C')
    yellow_dot = mpatches.Patch(color='yellow', label='PF')
    plt.legend(handles=[red_dot,blue_dot,green_dot,magenta_dot,yellow_dot], loc=2)
    plt.show()

def hw_bin_plot(df, met):
    fig, axes = plt.subplots(2, 2, subplot_kw=dict(), figsize=(8,6))
    fig.set_figheight(5.5)
    axs = [axes[0,0], axes[0,1], axes[1,0], axes[1,1]]
    #plt.suptitle('Histogram of %s for different positions'%met)
    for pos in zip(['PG','SG','SF','C'],axs):
        pos[1].hist(df[met][df.Pos==pos[0]],25)
        mean = round(df[met][df.Pos==pos[0]].mean(),1)
        sd = round(df[met][df.Pos==pos[0]].std(),1)
        pos[1].set_title('Position=%s, mean=%s, sd=%s'%(pos[0],mean,sd))
    plt.tight_layout()
    plt.subplots_adjust(left=0.2, bottom=0.2)
    fig.text(
        0.5, 0.05,
        "Histogram of %s for different positions"%met,
        ha='center',size=15)
    plt.show()

def top_3p_players(df,pl,year,n):
    df1=df[['Player','Age', 'Tm', 'G']]
    df2=df[df['Year']==year][['Player', 'PTS', 'Tm', 'Pos', 'G','3P','3P%','Year']]
    df2['Avpoints']=df['PTS']/df['G']
    top_avg_scorers_year=df2.sort_values(by='Avpoints', ascending=False)[0:n]
    tasy=top_avg_scorers_year.copy()
    df_3p = tasy[['Player','3P','3P%','Year']]
    df_3p_topn = df_3p[(df_3p['3P']>50) & (df_3p['Year']==year)].sort_values(by="3P%", ascending=False)[0:n]

    plt.figure(figsize=(10,5))
    plt.axes([0.2,0,1,1])
    df_3p_topn.groupby('Player')['3P%'].mean().sort_values().plot(kind='barh',sort_columns=True,color='g')
    plt.show()

