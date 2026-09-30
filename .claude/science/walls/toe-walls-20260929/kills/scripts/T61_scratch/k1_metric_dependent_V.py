# Kill check K1: is the "no interaction cancels it" claim limited to e-independent interactions?
# Same ED model as attacker d3_ed.py, but V -> V*(1 + b*t^2) along the axis shear path e=expm(t eps/2).
import numpy as np
from scipy.linalg import expm
import d3_ed as D
axis = np.diag([1.0,-1.0])/np.sqrt(2)
def cvp(V,b,h=0.04):
    f=lambda t: D.ground(expm(t*axis/2), V*(1+b*t*t))
    c1=(f(h)+f(-h)-2*f(0.0))/h**2; c2=(f(h/2)+f(-h/2)-2*f(0.0))/(h/2)**2
    return (4*c2-c1)/3
for V in (0.5,1.0):
    print("V=",V)
    for b in (0,1,2,4,8):
        print("  b=%d  c_vp=%+.5f"%(b,cvp(V,b)))
