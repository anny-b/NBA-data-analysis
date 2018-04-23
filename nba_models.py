import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy
from sklearn.linear_model import Perceptron

def plot_pos_metric(df, pos, met): 
    sl = df[df.Pos==pos].groupby('Year').mean().reset_index()
    plt.plot(sl.Year,sl[met])
    plt.xlabel('Year')
    plt.ylabel(met)
    plt.suptitle('Trends in %s of position %s through years'%(met,pos))
    plt.show()

def plot_allpos_metric(df,met,metname): 
    sl = df.groupby(['Year','Pos']).mean().reset_index()
    slPG = sl[sl.Pos=='PG']
    plt.plot(slPG.Year,slPG[met])
    slSG = sl[sl.Pos=='SG']
    plt.plot(slSG.Year,slSG[met],color='r')
    slC = sl[sl.Pos=='C']
    plt.plot(slC.Year,slC[met],color='g')
    slSF = sl[sl.Pos=='SF']
    plt.plot(slSF.Year,slSF[met],color='m')
    plt.legend(['PG','SG','C','SF'])
    plt.xlabel('Year')
    plt.ylabel(met)
    plt.suptitle('Trends in %s through years'%(metname))
    plt.show()

def plot_metric(df, met, win, metname):
    dfm=df[met].rolling(window=win).mean()
    plt.plot(df[['Year']],df[[met]],color='c')
    plt.plot(df[['Year']],dfm,color='r')
    plt.xlabel('Year')
    plt.ylabel(met)
    plt.legend([met,"%s-year Rolling Average"%win], loc='lower right')
    plt.title('Trend in player average %ss through years'%metname)
    file = "%s.png"%met
    plt.savefig(file)

def linear_reg(df, xmet, ymet):
    lm = linear_model.LinearRegression()
    x = df[xmet].values.reshape(-1,1)
    y = df[ymet].values
    lm.fit(x, y)
    xp = numpy.arange(1980,2030).reshape(-1,1)
    yp = lm.predict(xp)
    mean_sq_err = numpy.mean((y-yp[:38])**2)
    plt.plot(x,y,color='b')
    plt.scatter(xp,yp,color='r')
    plt.xlabel(xmet)
    plt.ylabel(ymet)
    minx=xp.min()
    maxy=yp.max()
    miny=yp.min()
    plt.text(minx, maxy, "Mean Sq. Error = %s"%mean_sq_err, color='g',fontsize='15')
    plt.show()

def polynomial_fit(df, xmet, ymet, degree):
    lm = linear_model.LinearRegression()
    poly = PolynomialFeatures(degree)
    x = df[xmet].values.reshape(-1,1)
    y = df[ymet].values.reshape(-1,1)
    x_= poly.fit_transform(x)
    lm.fit(x_,y)
    xp = numpy.arange(1980,2030).reshape(-1,1)
    xp_= poly.fit_transform(xp)
    yp = lm.predict(xp_)
    mean_sq_err = numpy.mean((y-yp[:38])**2)
    plt.plot(x,y,color='b')
    plt.scatter(xp,yp,color='r')
    plt.xlabel(xmet)
    plt.ylabel(ymet)
    minx=xp.min()
    maxy=yp.max()
    miny=yp.min()
    plt.text(minx, maxy, "Mean Sq. Error = %s"%mean_sq_err, color='g',fontsize='15')
    plt.show()

