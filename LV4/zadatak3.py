import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy
 
x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

#make polynomial features
poly_low = PolynomialFeatures(degree=2)
poly_med = PolynomialFeatures(degree=6)
poly_high = PolynomialFeatures(degree=15)
xlow = poly_low.fit_transform(x)
xmed = poly_med.fit_transform(x)
xhigh = poly_high.fit_transform(x)
    
np.random.seed(12)
indeksi_h = np.random.permutation(len(xhigh))
indeksi_h_train = indeksi_h[0:int(np.floor(0.7*len(xhigh)))]
indeksi_h_test = indeksi_h[int(np.floor(0.7*len(xhigh)))+1:len(xhigh)]
indeksi_m = np.random.permutation(len(xmed))
indeksi_m_train = indeksi_m[0:int(np.floor(0.7*len(xmed)))]
indeksi_m_test = indeksi_m[int(np.floor(0.7*len(xmed)))+1:len(xmed)]
indeksi_l = np.random.permutation(len(xlow))
indeksi_l_train = indeksi_l[0:int(np.floor(0.7*len(xlow)))]
indeksi_l_test = indeksi_l[int(np.floor(0.7*len(xlow)))+1:len(xlow)]

x_h_train = xhigh[indeksi_h_train,]
y_h_train = y_measured[indeksi_h_train]
x_m_train = xmed[indeksi_m_train,]
y_m_train = y_measured[indeksi_m_train]
x_l_train = xlow[indeksi_m_train,]
y_l_train = y_measured[indeksi_m_train]

xtesthigh = xhigh[indeksi_h_test,]
ytesthigh = y_measured[indeksi_h_test]
xtestmed = xmed[indeksi_m_test,]
ytestmed = y_measured[indeksi_m_test]
xtestlow = xlow[indeksi_l_test,]
ytestlow = y_measured[indeksi_l_test]

linearModelhigh = lm.LinearRegression()
linearModelhigh.fit(x_h_train,y_h_train)
linearModelmed = lm.LinearRegression()
linearModelmed.fit(x_m_train,y_m_train)
linearModellow = lm.LinearRegression()
linearModellow.fit(x_l_train,y_l_train)

yhigh = linearModelhigh.predict(xtesthigh)
MSE_test_high = mean_squared_error(ytesthigh, yhigh)
y_train_high = linearModelhigh.predict(x_h_train)
MSE_train_high = mean_squared_error(y_h_train, y_train_high)
ymed = linearModelmed.predict(xtestmed)
MSE_test_med = mean_squared_error(ytestmed, ymed)
y_train_med = linearModelmed.predict(x_m_train)
MSE_train_med = mean_squared_error(y_m_train, y_train_med)
ylow = linearModellow.predict(xtestlow)
MSE_test_low = mean_squared_error(ytestlow, ylow)
y_train_low = linearModellow.predict(x_l_train)
MSE_train_low = mean_squared_error(y_l_train, y_train_low)

plt.figure(0)
plt.plot(xtesthigh[:,1],yhigh,'ob',label='predicted high')
plt.plot(xtesthigh[:,1],ytesthigh,'oc',label='test high')
plt.legend(loc = 4)
plt.show()

plt.figure(1)
plt.plot(xtestmed[:,1],ymed,'or',label='predicted med')
plt.plot(xtestmed[:,1],ytestmed,'oy',label='test med')
plt.legend(loc = 4)
plt.show()

plt.figure(2)
plt.plot(xtestlow[:,1],ylow,'og',label='predicted low')
plt.plot(xtestlow[:,1],ytestlow,'om',label='test low')
plt.legend(loc = 4)
plt.show()

#pozadinska funkcija vs model
plt.figure(3)
plt.plot(x,y_true,'k',label='f')
plt.plot(x, linearModelhigh.predict(xhigh),'r-',label='model high')
plt.plot(x, linearModelmed.predict(xmed),'g:',label='model med')
plt.plot(x, linearModellow.predict(xlow),'b-.',label='model low')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 4)
plt.show()

plt.plot(x, linearModelmed.predict(xmed),'g:',label='model_med')

plt.plot(x, linearModellow.predict(xlow),'b-.',label='model_low')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = 4)
plt.show()