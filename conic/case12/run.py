from casadi import *

x = MX.sym("x",6)

alpha = 6.81
gamma = 0.0464
beta = 0.5*gamma

A = blockcat([[-alpha,0,alpha,0,beta,-beta],[0,-alpha,0,alpha,gamma,-gamma],[-5,5,0,0,0,0],[0,0,-5,5,0,0],[0,0,0,0,-1,1]])

solver = qpsol("solver","qrqp",{"x":x,"f":dot(vertcat(0,0,0,0,0.005,0.005),x),"g":mtimes(A,x)})
print solver(lbg=[-0.1,-0.1,-1,-1,0],ubg=[0.1,0.1,0,0,0],lam_g0=[0,0,0.09413,0.07892,-0.00001124])

