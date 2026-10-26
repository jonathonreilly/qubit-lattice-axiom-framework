import sympy as sp, time
d=sp.symbols('delta',positive=True); m=sp.symbols('m',positive=True); s=sp.symbols('s',positive=True)
t0=time.time()
def S(x,n): return sp.series(x,d,0,n).removeO()
z=-1+d
E=S(sp.sqrt(4*m**2+d**2/(-1+d)),6)
q=S((1+d)/E,5)
t=S((q+sp.sqrt(q**2+16*m**2))/2,5)
c=S(-(d)/E,6); w1=S(-1/E,5)
# N = Nn/d form: multiply by d
Nfull=w1**2+(1+c**2)/(1-z**2)+4*m**2*(1/t**2+z**2/(E**2*(1-z**2)))
dN=S(sp.simplify(d*Nfull),4)       # d*N
S1=S(-1/E+c/(1-z),3)
Q=S((2*m/t)**2+(2*m)**2*(z/E-1/t)**2+(2*m/E)**2*z**2*(1-z)/(1+z),3)
W=S((E*S1+Q)/(2*dN/d),3)           # N=dN/d  => W=(..)*d/(2 dN)  -> careful
