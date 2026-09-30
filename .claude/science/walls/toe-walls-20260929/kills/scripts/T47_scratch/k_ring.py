"""Spline response to the one-site spike (phi_E0 - phi_S = delta_origin/6): value and 2nd derivative of the spline interpolant vs distance along the axis."""
import sys, math
sys.dont_write_bytecode=True
import numpy as np
import ladder_infvol as L
from scipy.ndimage import spline_filter, map_coordinates
N=81; c=40
g=np.zeros((N,N,N)); g[c,c,c]=1/6
pad=np.pad(g,12,mode='edge'); coef=spline_filter(pad,3,mode='nearest')
def f(x,y=0,z=0):
    cc=(N-1)/2+12
    return float(map_coordinates(coef,np.array([[cc+x],[cc+y],[cc+z]]),order=3,mode='nearest',prefilter=False)[0])
h=0.04
print("R    spike-spline value   d2/dx2        ratio to previous knot (0.268 expected in magnitude)")
prev=None
for R in (2.0,3.0,4.0,5.0,6.0,8.0):
    v=f(R+0.25); d2=(f(R+0.25+h)-2*f(R+0.25)+f(R+0.25-h))/h**2
    print(f"{R+0.25:5.2f} {v:+.3e} {d2:+.3e}")
print("for scale: exact phi'' at r=4.25 is 2.07e-3 (x-dir); spike-ring d2 at 4.25 is:",(f(4.25+h)-2*f(4.25)+f(4.25-h))/h**2)
