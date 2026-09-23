"""Independent finite neutral-spin band control; no author code imports."""
from pathlib import Path
from itertools import combinations
from datetime import datetime, timezone
import hashlib, json
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent
OUT=HERE/'BAND_ALGEBRA_RESULTS.json'
assert not OUT.exists()
n=4
edges=[(0,1),(1,2),(2,3),(3,0),(0,2)]
phi=[1,-2,0,3,1]
chi=[2,1,-1,0,3]
states=[]
for plus in combinations(range(n),n//2):
    states.append(tuple(1 if i in plus else -1 for i in range(n)))
ix={q:i for i,q in enumerate(states)}
z=len(states)
u=s.ones(z,1)/s.sqrt(z)
inc=s.zeros(n,len(edges))
H0=s.zeros(z);H1=s.zeros(z);H2=s.zeros(z)
for e,(a,c) in enumerate(edges):
    inc[a,e]=1;inc[c,e]=-1
    for j,q in enumerate(states):
        if q[a]==q[c]:
            H0[j,j]-=2;H2[j,j]+=phi[e]**2
        else:
            qq=list(q);qq[a],qq[c]=qq[c],qq[a];i=ix[tuple(qq)]
            H0[i,j]-=2;H1[i,j]+=2*s.I*q[a]*chi[e];H2[i,j]+=chi[e]**2
assert H0==H0.T and H1==H1.conjugate().T and H2==H2.T
E0=-2*len(edges)
assert H0*u==E0*u
excited=H0-E0*s.eye(z)
assert excited.rank()==z-1
P=u*u.T
G=(excited+P).inv()-P
actual=s.simplify((u.T*H2*u-u.T*H1*G*H1*u)[0])
pe=s.Rational(n-2,2*(n-1));po=s.Rational(n,2*(n-1))
red=inc[:-1,:]
proj=s.eye(len(edges))-red.T*(red*red.T).inv()*red
expected=s.simplify(pe*(s.Matrix(phi).T*s.Matrix(phi))[0]+po*(s.Matrix(chi).T*proj*s.Matrix(chi))[0])
assert actual==expected
qmap=s.Matrix(states)
b=inc*s.Matrix(chi)
assert H1*u==-s.I*qmap*b/s.sqrt(z)
for f in [s.Matrix([1,-1,0,0]),s.Matrix([1,1,-1,-1])]:
    assert excited*(qmap*f)==2*qmap*(inc*inc.T*f)

def potential(t,ph=phi,ch=chi):
    out=np.zeros((z,z),complex)
    for e,(a,c) in enumerate(edges):
        for j,q in enumerate(states):
            if q[a]==q[c]:out[j,j]-=2*np.cos(t*ph[e])
            else:
                qq=list(q);qq[a],qq[c]=qq[c],qq[a]
                out[ix[tuple(qq)],j]-=2*np.exp(-1j*t*q[a]*ch[e])
    assert np.max(np.abs(out-out.conj().T))<1e-13
    return out
finite=[]
for t in [0.1,0.05,0.025,0.0125]:
    ev=np.linalg.eigvalsh(potential(t));evminus=np.linalg.eigvalsh(potential(-t))
    estimate=(ev[0]-E0)/t**2
    finite.append({'angle':t,'ground_energy':float(ev[0]),'quadratic_quotient':float(estimate),
                   'error_from_exact':float(estimate-float(expected)),
                   'odd_energy_difference':float(ev[0]-evminus[0]),'gap':float(ev[1]-ev[0])})
assert abs(finite[-1]['error_from_exact'])<0.0015
lam=s.Matrix([1,-2,3,-2])
chi_g=list(2*inc.T*lam)
Hg=potential(0.173,[0]*len(edges),chi_g)
D=np.diag(np.exp(1j*0.173*np.array(qmap*lam,dtype=float).reshape(-1)))
assert np.max(np.abs(Hg-D@np.array(H0,dtype=float)@D.conj().T))<1e-13
assert abs(np.linalg.eigvalsh(Hg)[0]-E0)<1e-13
out={'created_utc':datetime.now(timezone.utc).isoformat(),'neutral_sites':n,
     'basis':states,'edges':edges,'phi_direction':phi,'two_path_direction':chi,
     'potential_ground_energy_at_zero':E0,'ground_unique':True,
     'H0_minus_E0_eigenvalues':{str(k):v for k,v in excited.eigenvals().items()},
     'p_equal':str(pe),'p_opposite':str(po),'direct_fixed_matter_quadratic':str((u.T*H2*u)[0]),
     'relaxation_subtraction':str(s.simplify((u.T*H1*G*H1*u)[0])),
     'relaxed_quadratic_exact':str(actual),'projected_formula_exact':str(expected),
     'derivative_vector_and_laplacian_factor_two_exact':True,
     'finite_angle_controls':finite,'pure_gauge_covariance_error':float(np.max(np.abs(Hg-D@np.array(H0,dtype=float)@D.conj().T))),
     'scope':'Complete six-dimensional neutral matter potential on a connected five-exchange graph; local potential algebra control, not a separate full cubic lattice.',
     'source':{'path':str(Path(__file__).resolve()),'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
