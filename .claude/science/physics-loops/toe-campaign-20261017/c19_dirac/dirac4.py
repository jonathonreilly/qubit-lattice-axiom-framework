from diraclib import *
rng=np.random.default_rng(11)
X=np.tensordot(rng.normal(size=len(Xb)),Xb,1); X/=np.abs(X).max()
Hbase=H0(-1.0,0.2)+0.05*X
bl=blocks_from(Hbase); EN=np.linalg.eigvalsh(Hk(bl,kst))[0]
ev0,V0=np.linalg.eigh(Hbase); idx=np.where(np.abs(ev0-EN)<1e-6)[0]; print('node energy',round(EN,5),'states there on L=4:',len(idx))
P4=V0[:,idx]
tsign=[(-1.0)**sum(t) for t in TV]
def symQ(Xm, use_inv=False):
    Y=np.zeros_like(Xm)
    for (P,s),sg in zip(trans,tsign): Y+=sg*conj(Xm,P,s)
    Z=np.zeros_like(Xm)
    for P,s in rots: Z+=conj(Y,P,s)
    return Z
for kind in ('real','imag'):
    for trial in range(5):
        A=np.zeros((nV,nV))
        for i in loc0:
            for j in loc0:
                A[i,j]=rng.normal()
        A=(A+A.T) if kind=='real' else (A-A.T)
        S=np.diag(par)@((1 if kind=='real' else 1j)*A)
        M=symQ(S); M=(M+M.conj().T)/2
        if np.abs(M).max()<1e-10: print('  ',kind,trial,'vanishes'); continue
        M/=np.abs(M).max()
        w=np.linalg.eigvalsh(P4.conj().T@M@P4)
        print('  staggered O-invariant on-site seed',kind,trial,': projected 4x4 mass eigenvalues',np.round(w,4))
