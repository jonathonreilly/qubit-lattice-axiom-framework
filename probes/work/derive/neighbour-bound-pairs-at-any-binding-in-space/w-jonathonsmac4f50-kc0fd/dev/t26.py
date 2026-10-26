from t8 import *
rng=np.random.default_rng(7)
cs=[]
for it in range(600):
    c=rng.normal(size=5); c/=np.linalg.norm(c); cs.append(c)
up=np.array([1,0],complex); dn=np.array([0,1],complex)
UU=np.kron(up,up); DD=np.kron(dn,dn); UD=np.kron(up,dn); DU=np.kron(dn,up)
S=(UD-DU)/np.sqrt(2); T0=(UD+DU)/np.sqrt(2)
for it in (161,312):
    Mz=Mof(cs[it])
    B=np.array([UU,DD,S,T0]).T  # columns
    Mb=B.conj().T@Mz@B
    np.set_printoptions(precision=4,suppress=True)
    print(it); print(Mb)
