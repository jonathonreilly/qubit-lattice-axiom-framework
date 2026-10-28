"""x6 POST-HOC (not pre-registered; written after x6_out.txt showed C1 unresolved at 2.4 SE).
Independent (psi-free) Monte Carlo of the cross-plane covariance c = Cov(D(theta P), D(P)) of the one-step straight
block flux, noise-free (sigma = 0), g0 = 1, same lattice as x6 C; compared with x6's closed-form value 2.84142096e-04."""
import os
for v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"): os.environ.setdefault(v,"1")
import numpy as np, time
N0, ns = 54, 9; shape=(N0,ns,ns,ns)
kh=[4*np.sin(np.pi*2*np.fft.fftfreq(m)/2)**2 for m in shape]
K=np.meshgrid(*kh,indexing="ij"); den=sum(K)
amp=np.where(den>0,1/np.sqrt(np.where(den>0,den,1)),0.0)
rng=np.random.default_rng(777); T=N0//3; p=np.arange(T)
t0=time.time(); n=40000; c=np.empty(n); vv=np.empty(n)
for i in range(n):
    B=[]
    for mu in range(4):
        A=np.real(np.fft.ifftn(np.fft.fftn(rng.standard_normal(shape))*amp))
        s=A+np.roll(A,-1,axis=mu)+np.roll(A,-2,axis=mu)
        B.append(s.reshape(T,3,3,3,3,3,3,3).sum(axis=(1,3,5,7))/81.0)
    Y=B[1]+np.roll(B[2],-1,axis=1)-np.roll(B[1],-1,axis=2)-B[2]
    c[i]=np.mean(Y[(p+1)%T]*Y[(p-2)%T]); vv[i]=np.mean(Y*Y)
se=c.std(ddof=1)/np.sqrt(n); ref=2.84142096e-04
print(f"MC c={c.mean():.6e} +- {se:.2e}; closed form {ref:.6e}; z={(c.mean()-ref)/se:+.2f}; c/SE={c.mean()/se:.1f}")
print(f"MC v={vv.mean():.6f} vs closed form 0.180592; wall {time.time()-t0:.0f}s")
