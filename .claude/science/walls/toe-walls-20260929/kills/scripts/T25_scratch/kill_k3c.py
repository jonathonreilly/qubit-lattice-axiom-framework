import numpy as np, itertools
from scipy.optimize import minimize
# U(k)=alpha(k) I + i beta*sum_a sin k_a sigma_a with alpha=c0+2a*sum cos k_a (complex c0,a), beta complex.
# U^dag U = |alpha|^2+|beta|^2|s|^2 + [ i(conj(alpha) beta - alpha conj(beta)) ] s.sigma  (s x s = 0)
rng = np.random.default_rng(0)
k = np.array(list(itertools.product(np.linspace(0,2*np.pi,7,endpoint=False),repeat=3)))
C = np.cos(k).sum(1); S2 = (np.sin(k)**2).sum(1)
def resid(p, bmod):
    c0=p[0]+1j*p[1]; a=p[2]+1j*p[3]; be=bmod*np.exp(1j*p[4]); al=c0+2*a*C
    scal = np.abs(al)**2 + np.abs(be)**2*S2*4 - 1   # factor 2 from 2i beta sin
    vec = np.imag(np.conj(al)*be*2)                  # coefficient multiplying s.sigma
    return np.mean(scal**2)+np.mean(vec**2*S2)
for b in (0.02,0.1,0.25,0.5,1.0):
    r=min(minimize(resid, rng.normal(size=5), args=(b,), method='BFGS').fun for _ in range(40))
    print("K3 |beta| =",b," min residual of U^dag U=1:",f"{r:.3e}")
