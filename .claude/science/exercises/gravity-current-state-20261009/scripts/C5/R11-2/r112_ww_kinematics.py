# WW on a box domain: the boost to the brick-wall (P = p + p' at rest) frame for two massless legs.
# Claim: along the whole boost path 0..eta*, each leg's energy stays <= max(E1, E2); eta* = artanh(|P|/(E1+E2)) -> inf as theta -> 0.
import numpy as np
rng=np.random.default_rng(3); out=[]
def p(s): print(s); out.append(s)
worst=0.0; n=0
for trial in range(20000):
    E1,E2=rng.uniform(0.01,1.0,2); th=10**rng.uniform(-6,np.log10(np.pi))
    n1=np.array([0,0,1.0]); n2=np.array([np.sin(th),0,np.cos(th)])
    P3=E1*n1+E2*n2; v=np.linalg.norm(P3)/(E1+E2); u=P3/np.linalg.norm(P3); eta_s=np.arctanh(min(v,1-1e-16))
    for eta in np.linspace(0,eta_s,60):
        for E,nn in [(E1,n1),(E2,n2)]:
            Ep=E*(np.cosh(eta)-np.sinh(eta)*np.dot(nn,u))
            worst=max(worst,Ep/max(E1,E2)); n+=1
p(f"max over {n} path points of E_leg(eta)/max(E1,E2) = {worst:.12f}  (<= 1 => boost orbit never leaves the ball |k| <= max(|p|,|p'|))")
for th in [1e-1,1e-3,1e-6,1e-9]:
    v=np.cos(th/2); p(f"equal energies, theta={th:.0e}: eta* = artanh(cos(theta/2)) = {np.arctanh(v):.3f} ~ ln(4/theta) = {np.log(4/th):.3f}; brick-wall leg energy / E = sin(theta/2) = {np.sin(th/2):.2e}")
open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
