"""Challenge the exponential-weight generator bound with noncommuting blocks."""
from pathlib import Path
import json,math
import numpy as np
from scipy.linalg import expm,eigvalsh
rng=np.random.default_rng(821517)
out=[]
for S in [1,2,4,7]:
    d=3;E=np.repeat(np.arange(-S,S+1),d);V=np.zeros((len(E),len(E)),complex)
    for n in range(2*S):
        z=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));z/=np.linalg.norm(z,2)
        V[(n+1)*d:(n+2)*d,n*d:(n+1)*d]=z
    J=np.linalg.norm(V,2);H=V+V.conj().T+np.diag(rng.normal(size=len(E))*17)
    assert np.linalg.norm(np.diag(E)@V-V@np.diag(E)-V)<1e-12
    psi=np.zeros(len(E),complex);z=rng.normal(size=d)+1j*rng.normal(size=d);z/=np.linalg.norm(z);psi[S*d:(S+1)*d]=z
    for lam in [.13,.7,1.2]:
        w=np.exp(lam*abs(E));Hw=(w[:,None]*H)/w[None,:]
        skew=(Hw-Hw.conj().T)/(2j);actual=np.max(abs(eigvalsh(skew)));bound=2*J*np.sinh(lam)
        assert actual<=bound+1e-12
        t=.61;state=expm(-1j*t*H)@psi;weighted=np.linalg.norm(w*state);cb=np.exp(bound*t)
        assert weighted<=cb+1e-12
        tail=np.linalg.norm(state[abs(E)==S]);assert tail<=np.exp(-lam*S)*cb+1e-12
        moment=np.linalg.norm(E**4*state);mb=(4/(math.e*lam))**4*cb;assert moment<=mb+1e-12
        out.append({'S':S,'lambda':lam,'skew_norm':actual,'skew_bound':bound,'weighted_state_norm':weighted,'weighted_bound':cb,'endpoint_norm':tail,'endpoint_bound':np.exp(-lam*S)*cb,'eighth_moment_sqrt':moment,'moment_bound':mb})
for N in range(3,100,2):
    S=(N-1)//2
    for n in range(-S,S+1):
        x=math.pi*n/N;error=1-(math.sin(x)/x if x else 1)**2
        assert error>=-1e-15 and error<=x*x/3+1e-15
Path(__file__).with_name('BLOCK1_GENERATOR_BOUND_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print('noncommuting block weighted bounds checked:',len(out));print('largest ratio',max(x['skew_norm']/x['skew_bound'] for x in out))
