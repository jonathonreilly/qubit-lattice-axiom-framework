"""One-flux covariance integrals and exact curl/Bianchi symbol challenges."""
from pathlib import Path
from itertools import combinations
import json,math
import numpy as np
from scipy.integrate import quad

# Supplied scalar massive four-site determinant, separate from the Wilson
# realization: det(M I+t adjacency(phi))=c-b cos(phi).
M=4.;t=1.;e=.7;c=M**4-4*M*M*t*t+2*t**4;b=2*t**4
assert c>2*b
alpha=e*e*2*b/(c-b)
for phi in np.linspace(-4,4,29):
    K=np.zeros((4,4),complex)
    for i in range(4):
        j=(i+1)%4;z=np.exp(1j*phi) if i==3 else 1
        K[i,j]=t*z;K[j,i]=t*np.conjugate(z)
    assert abs(np.linalg.det(M*np.eye(4)+K)-(c-b*np.cos(phi)))<1e-10
cov=[]
for beta in [.03,.1,.3,1.]:
    assert beta>alpha
    den=c*c+b*b/2-2*c*b*np.exp(-e*e/(2*beta))+b*b/2*np.exp(-2*e*e/beta)
    analytic=1/beta+(2*c*b*e*e*np.exp(-e*e/(2*beta))-2*b*b*e*e*np.exp(-2*e*e/beta))/(beta*beta*den)
    def weight(x):return np.exp(-beta*x*x/2)*(c-b*np.cos(e*x))**2/(c*c)
    def score(x):return beta*x-2*b*e*np.sin(e*x)/(c-b*np.cos(e*x))
    def hessian(x):return beta-2*b*e*e*(c*np.cos(e*x)-b)/(c-b*np.cos(e*x))**2
    Z=quad(weight,-np.inf,np.inf,epsabs=1e-10)[0]
    var=quad(lambda x:x*x*weight(x),-np.inf,np.inf,epsabs=1e-10)[0]/Z
    cross=quad(lambda x:x*score(x)*weight(x),-np.inf,np.inf,epsabs=1e-10)[0]/Z
    eg2=quad(lambda x:score(x)**2*weight(x),-np.inf,np.inf,epsabs=1e-10)[0]/Z
    eh=quad(lambda x:hessian(x)*weight(x),-np.inf,np.inf,epsabs=1e-10)[0]/Z
    assert abs(var-analytic)<1e-8
    assert abs(cross-1)<1e-9 and abs(eg2-eh)<1e-9
    assert 1/(beta+alpha)<=var<=1/(beta-alpha)
    assert var>=1/eh-1e-10
    cov.append({'beta':beta,'alpha':alpha,'variance_quadrature':var,'variance_closed_form':analytic,'lower_comparison':1/(beta+alpha),'upper_comparison':1/(beta-alpha),'score_cross':cross,'score_second_moment':eg2,'expected_action_hessian':eh})
    print(cov[-1],flush=True)


def curl_symbol(q):
    d=len(q);pairs=list(combinations(range(d),2));C=np.zeros((len(pairs),d),complex)
    for r,(i,j) in enumerate(pairs):C[r,j]=q[i];C[r,i]=-q[j]
    return pairs,C


def bianchi_symbol(q):
    d=len(q);pairs=list(combinations(range(d),2));pos={p:i for i,p in enumerate(pairs)}
    B=np.zeros((math.comb(d,3) if d>=3 else 0,len(pairs)),complex)
    for r,(i,j,k) in enumerate(combinations(range(d),3)):
        B[r,pos[j,k]]=q[i];B[r,pos[i,k]]=-q[j];B[r,pos[i,j]]=q[k]
    return B

symbols=[]
for d in [2,3,4,5]:
    cases=[np.linspace(.21,.87,d)]+[np.eye(d)[i]*v for i in range(d) for v in [.3,.03,.003]]
    for k in cases:
        q=np.exp(1j*k)-1;pairs,C=curl_symbol(q);P=C@C.conj().T/np.vdot(q,q).real
        require_norm=max(np.linalg.norm(P@P-P),np.linalg.norm(P-P.conj().T),np.linalg.norm(bianchi_symbol(q)@C))
        assert require_norm<1e-12
        assert abs(np.trace(P).real-(d-1))<1e-12
        for j,(mu,nu) in enumerate(pairs):
            assert abs(P[j,j]-(abs(q[mu])**2+abs(q[nu])**2)/np.vdot(q,q).real)<1e-12
    stacked=np.concatenate([bianchi_symbol(np.eye(d)[i]) for i in range(d)],axis=0)
    nullity=len(pairs)-(np.linalg.matrix_rank(stacked) if len(stacked) else 0)
    assert nullity==(1 if d==2 else 0)
    symbols.append({'dimension':d,'momenta_checked':len(cases),'curl_range_rank':d-1,'common_Bianchi_kernel_dimension':int(nullity)})
    print(symbols[-1],flush=True)
# A compact Wilson cosine has negative action curvature at pi; a global
# Maxwell lower Hessian bound cannot be substituted for it.
assert math.cos(math.pi)<0
Path(__file__).with_name('BLOCK2_COVARIANCE_PROJECTION_CHECK.json').write_text(json.dumps({'one_flux_covariances':cov,'symbols':symbols},indent=2)+'\n')
