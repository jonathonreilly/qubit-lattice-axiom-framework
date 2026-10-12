"""Executable M1/M5/D1 formulas. Compared against disjoint reference routes."""
import numpy as np
from scipy.sparse import coo_matrix

ORIGIN_SHIFT = -0.5
BOOST_SIGN = -1.0
CELL_POWER = -0.5
MASS_SIGN = 1.0
SPACE_SIGN = 1.0
HALF_DENSITY = 0.0
WEIGHTED_FIRST = 1.0
WEIGHTED_SECOND = 1.0
ENDPOINT_CORRECTIONS = True

def couplings(a,m,v):
    sigma=np.sqrt(m*m/4+v*v/(a*a))
    return sigma/2+m/4,sigma/2-m/4

def boost_matrix(indices,a,g,J,finite_open=False):
    """M5 on a consecutive finite box; optional literal spin endpoints."""
    indices=np.asarray(indices,dtype=int)
    assert np.all(np.diff(indices)==1)
    m=2*(g-J); c=2*a*J
    rows=[]; cols=[]; vals=[]
    def put(r,k,z): rows.append(r);cols.append(k);vals.append(z)
    for j,n in enumerate(indices):
        x=a*n
        left=x+(ORIGIN_SHIFT-.5)*a
        right=x+(ORIGIN_SHIFT+.5)*a
        mass=MASS_SIGN*m*(x+ORIGIN_SHIFT*a)
        put(2*j,2*j+1,1j*(mass+SPACE_SIGN*c*(left/a+HALF_DENSITY)))
        put(2*j+1,2*j,1j*(-mass+SPACE_SIGN*c*(-right/a+HALF_DENSITY)))
        if j>0: put(2*j,2*(j-1)+1,-1j*SPACE_SIGN*c*left/a)
        if j+1<len(indices): put(2*j+1,2*(j+1),1j*SPACE_SIGN*c*right/a)
    if finite_open and ENDPOINT_CORRECTIONS:
        for j,z in [(0,1j*a*g*(1-indices[0])),(len(indices)-1,-1j*a*g*indices[-1])]:
            put(2*j,2*j+1,z);put(2*j+1,2*j,np.conjugate(z))
    return coo_matrix((vals,(rows,cols)),shape=(2*len(indices),)*2).tocsr()

def cell_average(fixture,indices,a):
    return a**CELL_POWER*fixture.integral(a*np.asarray(indices),a*(np.asarray(indices)+1))

def bound_R(norms,a,m,v):
    return (WEIGHTED_FIRST*m/2*norms['xf1']
            +WEIGHTED_SECOND*v/2*norms['xf2']+2*v*norms['f1']
            +7*m/4*norms['f0']+v*a/6*norms['f2'])
