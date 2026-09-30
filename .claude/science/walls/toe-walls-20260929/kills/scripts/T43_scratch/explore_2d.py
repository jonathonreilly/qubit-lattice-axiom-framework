import numpy as np, itertools
from stag import *
L=8; lat=Lat(L,2); Q=1; m=0.5; m5=0.1
U=u1_flux_links_2d(lat,Q); U0=np.ones((lat.V,2,1,1),complex)
D=stag_D(lat,U).toarray(); D0=stag_D(lat,U0).toarray()
Nc=1
C=[]
for mu in range(2):
    T=fwd_shift(lat,U,mu); C.append(0.5*(T+T.conj().T))
S=(0.5*(C[0]@C[1]+C[1]@C[0])).toarray()
print("pattern  herm  |{G,D}|free  arg det (Q=1)")
for a in itertools.product((0,1),repeat=2):
    for ph in (1,1j):
        z=ph*(-1.0)**(lat.coords@np.array(a)); G=np.diag(z)@S
        h=np.abs(G-G.conj().T).max()
        if h>1e-12: continue
        T0=[]; 
        C0=[]
        for mu in range(2):
            T=fwd_shift(lat,U0,mu); C0.append(0.5*(T+T.conj().T))
        S0=(0.5*(C0[0]@C0[1]+C0[1]@C0[0])).toarray()
        G0=np.diag(z)@S0
        anti=np.abs(G0@D0+D0@G0).max()
        aa,_=argdet(D+m*np.eye(lat.V)+1j*m5*G)
        print(a,ph,f"{h:.1e} {anti:.2e} {aa:+.5f}")
Os=singlet_op(lat,U,True).toarray()
# what is Os in terms of S-type ops?
for a in itertools.product((0,1),repeat=2):
    for ph in (1,1j):
        z=ph*(-1.0)**(lat.coords@np.array(a)); G=np.diag(z)@S
        for sgn in (1,-1):
            if np.abs(Os-sgn*G).max()<1e-9: print("Os == ",sgn,a,ph)
# zero-mode structure of D
w,v=np.linalg.eig(D)
idx=np.argsort(np.abs(w))[:6]
Gf=gamma_f_2d(lat,U).toarray()
for i in idx:
    vv=v[:,i]/np.linalg.norm(v[:,i])
    print("lam",w[i], " <Gf>",(vv.conj()@Gf@vv).real, " <eps>",(vv.conj()@np.diag(lat.eps)@vv).real)
