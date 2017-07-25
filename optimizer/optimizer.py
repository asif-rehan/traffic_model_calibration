'''
Created on Jun 30, 2017

@author: Asif Rehan
'''
import numpy
import pandas
import scipy.optimize as optimize
import math
from matplotlib import pyplot

global count
error = []
count = 1
def main():
    print process_m(func1, range)
    
def get_data(fp):
    data = pandas.read_csv(fp)
    return data
    
def process_m(model, ranges):
    global error
    x0 = [0.01, 85, (5.6327*(10**-6) +4.167*(10**-5))/2]
    x_opt = optimize.minimize(get_rmse_m1, x0,  bounds=((0.0001, 0.015),                  #s0
                                                     (80, 90),                                            #vf
                                                     (5.6327*(10**-6), 4.167*(10**-5)),                   #d
                                                     ))
    pyplot.plot(error)      
    pyplot.show()                                       #lp
    return x_opt

def func1(v, s0, vf, d, lp=0.005, T=0.0001389):
    x = s0 + v * T
    y = (1 - (v / vf)) ** d
    q = v * ( x * y ** -0.5+ lp) ** -1 
    return q

def get_rmse_m1(params):
    global count
    q_hat = data['Speed'].apply(lambda x: func1(x,
                                      s0=params[0], 
                                      vf=params[1], 
                                      d=params[2]))
    diff = q_hat - data['Flow']
    rmse = math.sqrt((diff ** 2).sum()/diff.shape[0])
    error.append(rmse)
    print count, '; rmse= ', rmse, len(error)
    count += 1
    
    return rmse

if __name__=='__main__':
    fp = r'D:\ar_doclib\temo\rafi\field_data.csv'
    data = get_data(fp)
    main()
    