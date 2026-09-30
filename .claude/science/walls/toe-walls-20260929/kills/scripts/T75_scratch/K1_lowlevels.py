import numpy as np
from A3_diamond import vacuum_C, tri
def levels(N):
    C=vacuum_C(N); j=np.arange(1,N+1,dtype=float)
    w=(j-.5)*(N+.5-j)/N; H=tri(np.sqrt(w[:-1]*w[1:]))
    nu,U=np.linalg.eigh(C)
    ok=(nu>1e-13)&(nu<1-1e-13)
    eps=np.log((1-nu[ok])/nu[ok]); Uo=U[:,ok]
    E=np.einsum("il,ij,jl->l",Uo,H,Uo)
    pos=eps>0; e=eps[pos];E2=E[pos]; o=np.argsort(e)
    return e[o],E2[o]
for N in (100,200,400,800,1600,3200):
    e,E=levels(N)
    r=e/(np.pi*E)
    # also unweighted mean ratio over levels eps<8 and the spread
    m=e<8
    print(N,"lowest 4 ratios",np.round(r[:4],4),"mean(eps<8)",round(r[m].mean(),4),"min/max",round(r[m].min(),4),round(r[m].max(),4),"lowest eps",round(e[0],4))
