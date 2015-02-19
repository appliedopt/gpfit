from numpy import arange, meshgrid, hstack, log, exp, amax, maximum, linspace
from gpfit.compare_fits import compare_fits

[X, Y] = meshgrid(linspace(1,2,30),linspace(0.2,0.4,30))
Z = X**2 + 30*X*exp(-(Y-0.06*X)/0.039)

u1, u2 = X, Y

w = Z.reshape(Z.size,1)
X = X.reshape(X.size,1)
Y = Y.reshape(Y.size,1)
u = hstack((X,Y))

x = log(u)
y = log(w)

s = compare_fits(x,y, 2,1)


# Max Affine Fitting
PAR_MA = s['max_affine']['params'][0][0]
A = PAR_MA[[1,2,4,5]]
B = PAR_MA[[0,3]]
w_MA_1 = exp(B[0]) * u1**A[0] * u2**A[1]
w_MA_2 = exp(B[1]) * u1**A[2] * u2**A[3]
w_MA = maximum(w_MA_1, w_MA_2)
print amax(w_MA - Z)


# Softmax Affine Fitting
PAR_SMA = s['softmax_optMAinit']['params'][0][0]
A = PAR_SMA[[1,2,4,5]]
B = PAR_SMA[[0,3]]
alpha = 1/PAR_SMA[-1]
w_SMA = (exp(alpha*B[0]) * u1**(alpha*A[0]) * u2**(alpha*A[1]) +
        exp(alpha*B[1]) * u1**(alpha*A[2]) * u2**(alpha*A[3])
        )**(1/alpha)

print amax(w_SMA - Z)