import numpy as np
from common import sets, dial
from estimators import fit_two, masses
np.set_printoptions(precision=8)
print('\n##### TEST 2 : joint point of the family A = a_s P_s + a_d P_d #####')
# --- (a) explicit matrices: typing 1 (AM-GM equipartition weights) and typing 2 (normalised-trace response)
C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); w=np.exp(2j*np.pi/3)
P=[sum(w**(-k*j)*np.linalg.matrix_power(C,j) for j in range(3))/3 for k in range(3)]
Ps=P[0]; Pd=P[1]+P[2]
def typing(a_s,a_d):
    A=a_s*Ps+a_d*Pd
    Phi=np.trace(np.linalg.inv(A)@Pd).real/3      # tau(A^-1 P_d), normalised trace
    delta=Phi/3                                   # Brannen: Phi = 3 delta (cycle holonomy)
    r=(a_s/a_d)/2                                 # Frobenius-note AM-GM equipartition with w_s/w_d = a_s/a_d
    return r,delta,Phi
r,d,Phi=typing(1.,1.)
print('A = I : r=%.6f  Phi=tau(A^-1 P_d)=%.6f (=2/3: %s)  delta=Phi/3=%.7f (=2/9: %s); det A=%.3f, Tr A=%.3f'%(r,Phi,abs(Phi-2/3)<1e-12,d,abs(d-2/9)<1e-12,np.linalg.det(Ps+Pd).real,np.trace(Ps+Pd).real))
# explicit circulant at (r,delta)=(1/2,2/9): spectrum -> masses, Q, and eigenvalue check
a=17.715; b=np.sqrt(r)*a*np.exp(1j*d)
H=a*np.eye(3)+b*C+np.conj(b)*C@C
ev=np.sort(np.linalg.eigvalsh(H)); m=ev**2
print('circulant spectrum masses ratio m/m_e:',m/m[0],' Q=%.9f'%(m.sum()/np.sqrt(m).sum()**2))
# --- (b) data-implied point in the (a_s/a_d , a_d) plane
print('\nData-implied natural-coordinates (a_s/a_d = 2r, a_d = 2/(9 delta)):')
for nm,ms in sets.items():
    mm=[ms['e'][0],ms['mu'][0],ms['tau'][0]]
    q,rf,df=dial(mm)
    print(' %-18s r-free 3-mass: (%.7f, %.7f)   | r=1/2 fixed,(e,mu): (1, %.7f)   (e,tau): (1, %.7f)'%(nm,2*rf,2/(9*df),
          2/(9*fit_two([mm[0],mm[1]],(0,1))[1]), 2/(9*fit_two([mm[0],mm[2]],(0,2))[1])))
# --- (c) sector extension to quarks: three normalisation rules
print('\nQuark sectors at M_Z (MSbar, n_f-universal running => dial is scale-free within a sector):')
qs={'up':[1.24e-3,0.624,171.7],'down':[2.69e-3,0.0535,2.86]}
import itertools
print('%-6s %-8s %-9s | pred delta: a_d=1 | det A=1 | Tr A=3 | observed | required (a_d, a_s, detA, TrA)'%('sector','r','delta_obs'))
for nm,mm in qs.items():
    q,rr,dd=dial(mm)
    p1=2/9; p2=(2/9)*(2*rr)**(1/3); p3=(4/27)*(1+rr)
    ad=2/(9*dd); as_=2*rr*ad
    print('%-6s %-8.4f %-9.4f |   %.4f     | %.4f  | %.4f | %.4f   | (%.2f, %.2f, %.1f, %.1f)'%(nm,rr,dd,p1,p2,p3,dd,ad,as_,as_*ad*ad,as_+2*ad))
# robustness of the observed quark delta to the inputs
rng=np.random.default_rng(3)
for nm,mm,err in [('up',qs['up'],[0.3e-3,0.02,0.5]),('down',qs['down'],[0.2e-3,0.005,0.03])]:
    ds=[];rs=[]
    for _ in range(4000):
        x=[abs(rng.normal(mm[i],err[i])) for i in range(3)]
        q,rr,dd=dial(x); ds.append(dd); rs.append(rr)
    print(nm,'MC: r=%.3f+-%.3f  delta=%.4f+-%.4f  [1st,99th pct delta: %.4f, %.4f]'%(np.mean(rs),np.std(rs),np.mean(ds),np.std(ds),*np.percentile(ds,[1,99])))
