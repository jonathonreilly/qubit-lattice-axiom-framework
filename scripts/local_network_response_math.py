"""Conditional finite real-network response identities; no physical law selection."""
import math
import sympy as sp
AUDIT_TIMEOUT_SEC = 120

def schur_response(z, a, coupling, hidden):
    return 1 / (z*z+a-(coupling.T*(z*z*sp.eye(hidden.rows)+hidden).inv()*coupling)[0])

def rank_one_difference(resolvent, source, readout, direction, theta):
    h=(readout.T*resolvent*direction)[0]*(direction.T*resolvent*source)[0]
    j=(direction.T*resolvent*direction)[0]
    return theta*h/(1+theta*j)

def three_setting_residual(settings, differences):
    t1,t2,t3=settings;d1,d2,d3=differences
    return t2*(t3-t1)*d1*d3-t3*(t2-t1)*d1*d2+t1*(t2-t3)*d2*d3

def error_certificate(settings, differences, errors):
    t1,t2,t3=settings
    def product_bound(i,j):
        return errors[i]*abs(differences[j])+errors[j]*abs(differences[i])+errors[i]*errors[j]
    return abs(t2*(t3-t1))*product_bound(0,2)+abs(t3*(t2-t1))*product_bound(0,1)+abs(t1*(t2-t3))*product_bound(1,2)

def first_access_moment(stiffness, source, direction):
    value=source
    for degree in range(stiffness.rows):
        moment=(direction.T*value)[0]
        if moment != 0:
            return degree,moment
        value=stiffness*value
    return None,None

def leading_impulse_difference(theta,moment,degree,t):
    return theta*moment**2*t**(4*degree+3)/math.factorial(4*degree+3)

def remainder_certificate(norm_bound,degree,t):
    return 2*norm_bound**(2*degree+2)*abs(t)**(4*degree+5)/math.factorial(4*degree+5)*math.cosh(math.sqrt(norm_bound)*abs(t))

def spring_stiffness(size,edges):
    stiffness=sp.eye(size)
    for i,j,weight in edges:
        direction=sp.zeros(size,1);direction[i]=1;direction[j]=-1
        stiffness+=weight*direction*direction.T
    return stiffness
