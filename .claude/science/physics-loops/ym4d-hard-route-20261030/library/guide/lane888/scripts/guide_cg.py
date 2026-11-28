# GUIDE only: Monte Carlo check of Lemma 3.2(b): squared norm of the spin-J component (in g) of
# chi_{1/2}(gW) chi_j(gV), averaged over Haar W, V, equals d_J/(2 d_j).  Also Lemma 4.2(b): 3/16.
import numpy as np
rng = np.random.default_rng(12345)
def haar(n):
    q = rng.normal(size=(n,4)); q /= np.linalg.norm(q,axis=1)[:,None]; return q
def qmul(a,b):
    a0,a1,a2,a3 = a.T; b0,b1,b2,b3 = b.T
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],axis=1)
def qinv(a):
    b = a.copy(); b[:,1:] *= -1; return b
def chi(twoj, q):   # character of spin j = twoj/2 at unit quaternion q: sin((2j+1)t)/sin t, cos t = q0
    t = np.arccos(np.clip(q[:,0],-1,1)); s = np.sin(t)
    s = np.where(np.abs(s)<1e-9, 1e-9, s)
    return np.sin((twoj+1)*t)/s
N = 4_000_000
for twoj in (1, 5):
    W, V, g, h = haar(N), haar(N), haar(N), haar(N)
    f_g = chi(1, qmul(g,W))*chi(twoj, qmul(g,V))
    f_h = chi(1, qmul(h,W))*chi(twoj, qmul(h,V))
    hg = qmul(qinv(h), g)
    for twoJ in (twoj-1, twoj+1):
        est = (twoJ+1)*np.mean(f_g*f_h*chi(twoJ,hg))
        err = (twoJ+1)*np.std(f_g*f_h*chi(twoJ,hg))/np.sqrt(N)
        print(f"j={twoj}/2 J={twoJ}/2: MC {est:.4f} +- {err:.4f}   formula d_J/(2 d_j) = {(twoJ+1)/(2*(twoj+1)):.4f}")
# Lemma 4.2(b): spin-5/2 component of prod_{i=1..4} chi_{1/2}(g W_i) * chi_{1/2}(g V): expect 3/16 = 0.1875
Ws = [haar(N) for _ in range(5)]; g, h = haar(N), haar(N)
f_g = np.prod([chi(1,qmul(g,w)) for w in Ws],axis=0); f_h = np.prod([chi(1,qmul(h,w)) for w in Ws],axis=0)
v = 6*f_g*f_h*chi(5,qmul(qinv(h),g))
print(f"five fundamentals, spin-5/2 part: MC {v.mean():.4f} +- {v.std()/np.sqrt(N):.4f}   formula 3/16 = {3/16:.4f}")
