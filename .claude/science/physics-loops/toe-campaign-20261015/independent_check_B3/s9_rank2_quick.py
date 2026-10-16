# quick evaluation of rank<=2 candidates using Groebner elements (b1!=0 branch and b1=0 branch)
import numpy as np, pickle, sympy as sp, mpmath as mp
mp.mp.dps=30
B=[sp.Symbol(n,real=True) for n in ('b0','b1','b2')]
Qf=sp.lambdify(B,pickle.load(open('Q.pkl','rb')),'mpmath')
for x in [r for r in np.roots([27,-153432,32])]+[r for r in np.roots([27,-72,-16]) if r>0]:
  x=mp.findroot(lambda t: 27*t**2-153432*t+32 if x<1e3 and x>1e-2 and False else (27*t**2-153432*t+32 if abs(27*x**2-153432*x+32)<1e-3*max(1,x**2) else 27*t**2-72*t-16), mp.mpf(x))
  for b2 in (mp.sqrt(x),-mp.sqrt(x)):
    b0=b2*(1587357*x**2-9020420424*x+472448)/236224
    for b1sq in mp.polyroots([236224,0,2037123*x**4-11576290482*x**3-561032*x**2]):
      if abs(mp.im(b1sq))>1e-20 or mp.re(b1sq)<=0: continue
      b1=mp.sqrt(mp.re(b1sq))
      M=mp.matrix(Qf(b0,b1,b2)); E=mp.eigsy(M)[0]
      print("b2^2=%s b=(%s,%s,%s) eig="%(mp.nstr(x,6),mp.nstr(b0,6),mp.nstr(b1,6),mp.nstr(b2,6)),[mp.nstr(e,6) for e in E])
