from t8 import *
# basis states for M(e_z): spin along bond z
up=np.array([1,0],complex); dn=np.array([0,1],complex)
UU=np.kron(up,up); DD=np.kron(dn,dn); UD=np.kron(up,dn); DU=np.kron(dn,up)
S=(UD-DU)/np.sqrt(2); T0=(UD+DU)/np.sqrt(2)
def proj(v): return np.outer(v,v.conj())
Ppm=proj(UU)+proj(DD)
def ray(c,ph=0.0):
    s=np.sqrt(1-c*c); v=c*S+np.exp(1j*ph)*s*T0; return proj(v)
fams={'coin-blind':np.eye(4,dtype=complex),'Ppm':Ppm,'zero-spin plane proj':proj(S)+proj(T0),
      'singlet S':proj(S),'t0':proj(T0),'ray c2=1/4':ray(0.5),'ray c2=1/2':ray(np.sqrt(.5),0.3),'ray c2=3/4':ray(np.sqrt(.75),0.7),'ray c2=0.9':ray(np.sqrt(.9))}
# check covariance: these must lie in commutant
Uq=U_rot((0,0,1),np.pi/2); G1=kr(Uq,Uq); Ux=U_rot((1,0,0),np.pi); G2=SWAP@kr(Ux,Ux)
for k,M in fams.items():
    print(k,'comm1',np.abs(M@G1-G1@M).max(),'comm2',np.abs(M@G2-G2@M).max())
res={}
for k,M in fams.items():
    rows=scanM(M,tabs)
    res[k]=rows
    EC_=2*np.sqrt(3)
    if not rows: print(k,'none'); continue
    mx=max(rows,key=lambda r:r[3])
    # restricted to gap>0.05
    r2=[r for r in rows if r[6]>0.0]
    print('%-22s nrows=%d max Wsum=%.3f at E=%.3f g=%.3f null=%d gap=%.3f ; min=%.3f'%(k,len(rows),mx[3],mx[0],mx[1],mx[2],mx[6],min(r[4] for r in rows)))
    # top 3 by E bins
    byE={}
    for r in rows: byE.setdefault(round(r[0],3),[]).append(r[3])
    Es=sorted(byE)
    print('     max Wsum at E~', {round(E,2):round(max(byE[E]),2) for E in Es[::9]})
