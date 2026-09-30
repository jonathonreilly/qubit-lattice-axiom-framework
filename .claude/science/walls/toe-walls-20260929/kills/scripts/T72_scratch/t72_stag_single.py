import numpy as np, scipy.linalg as la
from t72_stag import *
N=240
print("# staggered single walker, open chain N=240; dressed double commutator; W_pred = E0*eps''(0)")
print("class             beta   m     e0   W_pred    W_meas    rel.err")
cases=[("W1 stag mass",1.0,1.0,0.0),("W1 stag mass",1.0,0.5,0.0),("W1 stag mass",1.0,0.25,0.0),
       ("c-mismatch",0.8,1.0,0.0),("c-mismatch",1.2,0.5,0.0),("c-mismatch",0.5,1.0,0.0),
       ("W2 scalar offset",1.0,1.0,0.5),("W2 scalar offset",1.0,0.5,1.0),("W2 scalar offset",0.9,1.0,0.3)]
xc=(N-1)/2; xs=np.arange(N)
X=Xone(N)
for name,b,m,e0 in cases:
    Hfun=lambda g: h1(N,np.exp(g*(xs-xc)),b,m,e0)
    ev,V=la.eigh(Hfun(0.0).toarray())
    idx=np.where(ev>e0+0.5*m)[0][0]
    Wm=W_direct(Hfun,X,ev,V,idx,e0+0.5*m)
    Wp=band_W(b,m,e0)[0]
    print(f"{name:17s} {b:4.2f} {m:5.2f} {e0:5.2f}  {Wp:8.4f}  {Wm:8.4f}  {abs(Wm-Wp)/max(abs(Wp),0.1):8.2e}")
