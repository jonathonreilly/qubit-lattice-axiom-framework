"""Numerical challenges of a derived free three-torus twist asymptotic.

The truncated reciprocal sum has no certified tail in this exploration.
"""
from pathlib import Path
import numpy as np,json

sb,cb,zeta,mu=.8,.6,.6,.2
R=np.sqrt(1-mu*mu);xn=np.arccos(R*cb);zn=np.arccos(1+zeta-R)
G=np.array([R*R,1,R*R*sb*sb*np.sin(zn)**2/np.sin(xn)**2])


def energy(L,phi):
    k=np.indices((L,L,L)).reshape(3,-1).T*2*np.pi/L+np.array(phi)/L
    sx=np.sin(k[:,0]);cx=np.cos(k[:,0]);sy=np.sin(k[:,1]);cy=np.cos(k[:,1]);cz=np.cos(k[:,2])
    a=-sb*cx;b=cb*sx;c=2+zeta-cb*cx-cy-cz;d=-sb*sx;m1=mu*sb;m3=mu*cb
    S=sy*sy+a*a+b*b+c*c+d*d+mu*mu
    U=(a*b+c*d)**2+(a*m1+c*m3)**2+(b*m3-d*m1)**2
    low=S-2*np.sqrt(U);assert low.min()>-1e-11
    return -np.sum(np.sqrt(S+2*np.sqrt(U))+np.sqrt(np.maximum(low,0)))


def leading(L,phi,M):
    m=np.indices((2*M+1,)*3).reshape(3,-1).T-M
    m=m[np.any(m,axis=1)]
    denom=np.sum(m*m/G,axis=1)**2
    phase=4*np.cos(L*m[:,0]*xn)*np.cos(L*m[:,2]*zn)
    return float(np.sum((np.cos(m@np.array(phi))-1)*phase/denom)/(np.pi**2*np.sqrt(np.prod(G))*L))


rows=[]
for phi in [[0,np.pi,0],[np.pi,np.pi,np.pi],[.4,1.2,2.1]]:
    for L in [4,8,12,16,24,32,48]:
        exact=float(energy(L,phi)-energy(L,[0,0,0]))
        p12=leading(L,phi,12);p24=leading(L,phi,24)
        rows.append(dict(L=L,phi=phi,full_lattice=exact,leading_M12=p12,leading_M24=p24,
                         difference=exact-p24,L2_difference=L*L*(exact-p24),reciprocal_cutoff_change=p24-p12))
# Direct Abel radial formula: integral q^2 exp(-eps q)sin(rq)dq=Im[2/(eps-ir)^3].
abel=[]
for radius in [.7,1.,2.3]:
    target=-1/(np.pi**2*radius**4)
    values=[float((2/(eps-1j*radius)**3).imag/(2*np.pi**2*radius)) for eps in [.1,.01,.001]]
    assert abs(values[-1]-target)<2e-5
    abel.append(dict(radius=radius,target=target,values=values))
out=dict(metric=G.tolist(),nodes=dict(x=xn,z=zn),rows=rows,abel=abel,
         limitation='Finite reciprocal cutoff and floating full-lattice sums; no certified tail or asymptotic rate. Derivation is provisional and concerns free matter only.')
p=Path(__file__).resolve().parent;(p/'BLOCK16_CASIMIR_EXPLORATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
