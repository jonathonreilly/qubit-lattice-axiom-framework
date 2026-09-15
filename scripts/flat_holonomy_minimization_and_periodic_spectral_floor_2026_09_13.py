"""Exact rational enclosures of the supplied 3^3 mixed-carrier twist energy.

Integer square-root brackets certify a strict comparison, not a global minimum.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path
import json

AUDIT_TIMEOUT_SEC = 90

checks=0


def check(ok,label):
    global checks
    assert ok,label
    checks+=1


def sqrt_interval(value,scale=10**35):
    check(value>=0,'nonnegative exact radicand')
    k=isqrt(value.numerator*scale*scale//value.denominator)
    lo,hi=Q(k,scale),Q(k+1,scale)
    check(lo*lo<=value<=hi*hi,'integer-certified square-root enclosure')
    return lo,hi


def energy_interval(twist_y):
    periodic=[(Q(1),Q(0)),(Q(-1,2),Q(1,2)),(Q(-1,2),Q(-1,2))]
    antiperiodic=[(Q(1,2),Q(1,2)),(Q(-1),Q(0)),(Q(1,2),Q(-1,2))]
    lower=Q(0);upper=Q(0);records=[]
    for (cx,sx),(cy,sy),(cz,sz) in product(periodic,antiperiodic if twist_y else periodic,periodic):
        # Sines are the second coordinate times sqrt(3), which squares exactly.
        a=-Q(4,5)*cx;b=Q(3,5)*sx
        c=Q(13,5)-Q(3,5)*cx-cy-cz;d=-Q(4,5)*sx
        m1,m3=Q(4,25),Q(3,25)
        S=3*sy*sy+a*a+3*b*b+c*c+3*d*d+Q(1,25)
        U=3*(a*b+c*d)**2+(a*m1+c*m3)**2+3*(b*m3-d*m1)**2
        ulo,uhi=sqrt_interval(U)
        pluslo,_=sqrt_interval(S+2*ulo);_,plushi=sqrt_interval(S+2*uhi)
        minuslo,_=sqrt_interval(S-2*uhi);_,minushi=sqrt_interval(S-2*ulo)
        lower-=plushi+minushi;upper-=pluslo+minuslo
        check(S*S-4*U>0,'two strictly negative occupied bands on this finite grid')
        records.append(dict(cosines=[str(cx),str(cy),str(cz)],S=str(S),U=str(U)))
    return lower,upper,records



"""A charged ring with a dynamical flat holonomy: exploratory evidence."""
from itertools import combinations
from pathlib import Path
import json
import numpy as np
from scipy import sparse as sp
from scipy.sparse.linalg import eigsh

states=[sum(1<<i for i in pair) for pair in combinations(range(4),2)]
fi={s:j for j,s in enumerate(states)}
eta=np.array([0,1,0,1])
offsets=[]
for s in states:
    rho=np.array([(s>>j)&1 for j in range(4)])-eta
    offsets.append(np.r_[np.cumsum(rho)[:3],0])


def move(s,x,y):
    if not s>>y&1 or s>>x&1:return None
    sign=(-1)**((s&((1<<y)-1)).bit_count())
    v=s^(1<<y)
    sign*=(-1)**((v&((1<<x)-1)).bit_count())
    return fi[v|(1<<x)],sign


def matrix(g,S):
    basis=[(f,n) for f in range(6)
           for n in range(-S-int(min(offsets[f])),S-int(max(offsets[f]))+1)]
    ix={v:j for j,v in enumerate(basis)}
    H=sp.lil_matrix((len(basis),len(basis)))
    W=sp.lil_matrix(H.shape)
    for col,(f,n) in enumerate(basis):
        H[col,col]=.5*g*g*np.dot(offsets[f]+n,offsets[f]+n)
        if (f,n+1) in ix:W[ix[f,n+1],col]=1
        for edge in range(4):
            result=move(states[f],edge,(edge+1)%4)
            if result is not None:
                ff,sign=result;label=(ff,n+(edge==3))
                if label in ix:
                    row=ix[label];H[row,col]+=sign;H[col,row]+=sign
    return H.tocsr(),W.tocsr()


def free(theta):
    h=np.zeros((4,4),complex)
    for j in range(4):
        h[j,(j+1)%4]=np.exp(1j*theta) if j==3 else 1
        h[(j+1)%4,j]=h[j,(j+1)%4].conjugate()
    e=np.linalg.eigvalsh(h)
    return e[:2].sum()



"""Explore supplied mixed-quartet torus energies; no global-minimum claim."""
from pathlib import Path
from itertools import product
import numpy as np,json
from scipy.optimize import minimize

s1=np.array([[0,1],[1,0]],complex);s2=np.array([[0,-1j],[1j,0]]);s3=np.diag([1.,-1.]);I=np.eye(2)
sig=[np.kron(I,s) for s in [s1,s2,s3]]
tx=np.kron(s1,I);tz=np.kron(s3,I)
sinb,cosb,zeta,mu=.8,.6,.6,.2
on=(2+zeta)*sig[2]+mu*tx@(sinb*sig[0]+cosb*sig[2])
Cs=[-sinb*sig[0]-cosb*sig[2],-sig[2],-sig[2]]
Ss=[tz@(cosb*sig[0]-sinb*sig[2]),sig[1],np.zeros((4,4))]
Ts=[(c-1j*s)/2 for c,s in zip(Cs,Ss)]


def bloch(k):
    return on+sum(c*np.cos(q)+s*np.sin(q) for q,c,s in zip(k,Cs,Ss))


def band_energy(phi,L):
    points=(2*np.pi*np.array(list(product(range(L),repeat=3)))+np.array(phi))/L
    h=np.array([bloch(k) for k in points])
    return float(np.sort(np.linalg.eigvalsh(h).ravel())[:2*L**3].sum())


def direct_energy(phi,L):
    vertices=list(product(range(L),repeat=3));vi={v:j for j,v in enumerate(vertices)}
    H=np.kron(np.eye(L**3),on)
    for v in vertices:
        for axis,T in enumerate(Ts):
            w=list(v);w[axis]=(w[axis]+1)%L;w=tuple(w)
            a,b=4*vi[v],4*vi[w]
            H[a:a+4,b:b+4]+=T*np.exp(1j*phi[axis]/L)
            H[b:b+4,a:a+4]+=T.conj().T*np.exp(-1j*phi[axis]/L)
    return float(np.linalg.eigvalsh(H)[:2*L**3].sum())





def square_and_metric_checks():
    import sympy as sy
    a,b,c,d,m,n,y=sy.symbols('a b c d m n y',real=True)
    one=sy.eye(2);x=sy.Matrix([[0,1],[1,0]]);yy=sy.Matrix([[0,-sy.I],[sy.I,0]]);z=sy.diag(1,-1)
    sx,syy,sz=[sy.kronecker_product(one,v) for v in [x,yy,z]]
    tx0,ty0,tz0=[sy.kronecker_product(v,one) for v in [x,yy,z]]
    h=(a*sy.eye(4)+b*tz0+m*tx0)*sx+y*syy+(c*sy.eye(4)+d*tz0+n*tx0)*sz
    scalar=y*y+a*a+b*b+c*c+d*d+m*m+n*n
    expected=scalar*sy.eye(4)+2*(a*b+c*d)*tz0+2*(a*m+c*n)*tx0+2*(b*n-d*m)*syy*ty0
    check((h*h-expected).applyfunc(sy.expand)==sy.zeros(4),'exact symbolic mixed-carrier square')
    check((syy*h.conjugate()*syy+h).applyfunc(sy.expand)==sy.zeros(4),'exact spectral anti-symmetry')
    gammas=[tz0,tx0,syy*ty0]
    for gamma in gammas:check(gamma*gamma==sy.eye(4),'Clifford square')
    for i in range(3):
        for j in range(i):check(gammas[i]*gammas[j]+gammas[j]*gammas[i]==sy.zeros(4),'Clifford anticommutator')
    K=sy.Matrix([[4,4],[4,8]]);A=sy.diag(1,0);L=sy.Matrix([[1,0],[-1,1]])
    check(L*K*L.T==4*sy.eye(2),'mixed normal/tangent metric diagonalization')
    check((K*A).eigenvals()=={sy.Integer(4):1,sy.Integer(0):1},'correct rank-one normal frequency')
    check(K[0,0]-K[0,1]**2/K[1,1]==2,'wrong Schur normal coefficient differs from 4')


def run_checks():
    square_and_metric_checks()
    zero=energy_interval(False);twist=energy_interval(True)
    difference=(twist[0]-zero[1],twist[1]-zero[0])
    check(difference[1]<Q(-14424,10000),'strict actual-carrier twist improvement')
    check(difference[0]>Q(-14425,10000),'strict actual-carrier difference lower bracket')
    for phi,interval in [([0,0,0],zero),([0,np.pi,0],twist)]:
        direct=direct_energy(phi,3);bloch_value=band_energy(phi,3)
        check(abs(direct-bloch_value)<1e-10,'independent full site versus Bloch spectrum')
        check(abs(direct-float(interval[0]))<1e-10,'site matrix versus exact radical certificate')
    for theta in np.linspace(0,2*np.pi,17):
        check(abs(free(theta)+2*(np.cos(theta/4)+np.sin(theta/4)))<2e-12,
              'direct ring one-particle matrix versus analytic filled-band energy')
    # Separate six-dimensional CAR construction checks the ring Fourier potential.
    for theta in [0,.71,np.pi,5.1]:
        annihilators=[]
        for j in range(4):
            op=np.zeros((16,16))
            for f in range(16):
                if f>>j&1:op[f^(1<<j),f]=(-1)**sum((f>>k)&1 for k in range(j))
            annihilators.append(op)
        many=np.zeros((16,16),complex)
        for j in range(4):
            term=annihilators[j].T@annihilators[(j+1)%4]*np.exp(1j*theta*(j==3))
            many+=term+term.conj().T
        check(abs(np.linalg.eigvalsh(many[np.ix_(states,states)])[0]-free(theta))<2e-12,
              'direct six-state CAR potential versus free filled spectrum')
    samples=[]
    for g in [.2,.05,.01]:
        S=int(np.ceil((3+np.log(1/g))/np.sqrt(g)))
        H,W=matrix(g,S);e,v=eigsh(H,k=4,which='SA',tol=2e-12)
        order=np.argsort(e);e=e[order];v=v[:,order]
        check(e[0]>=-2*np.sqrt(2)-1e-10,'positive electric lower bound on ring ground')
        samples.append(dict(g=g,S=S,levels=e.tolist(),loop_real=float(v[:,0]@(W@v[:,0])),
                            correction_over_g=float((e[0]+2*np.sqrt(2))/g),gap_over_g=float((e[1]-e[0])/g)))
    check(abs(samples[-1]['levels'][0]+2*np.sqrt(2))<.005,'sampled ring minimum limit')
    check(samples[-1]['levels'][3]-samples[-1]['levels'][0]<.026,'sampled low-level accumulation')
    check(samples[-1]['loop_real']<-.98,'sampled loop concentration at pi')
    check(abs(samples[-1]['correction_over_g']-2**(-5/4))<.004,'formal ground coefficient numerical challenge only')
    check(abs(samples[-1]['gap_over_g']-2**(-1/4))<.001,'formal slow-gap coefficient numerical challenge only')
    print('EXACT_TWIST',json.dumps(dict(identity_interval=list(map(str,zero[:2])),twist_interval=list(map(str,twist[:2])),difference_interval=list(map(str,difference)))))
    print('RING',json.dumps(samples))
    for label,message in [
        ('per_element','exact radical square-root brackets and flat-link phases checked; no chosen coupling derived'),
        ('per_site','direct site matrix and independent finite CAR actions checked'),
        ('per_mode','ring energy branches, normal metric coefficient and sampled slow levels checked'),
        ('per_block','strict 3-cubed actual-carrier flat-twist comparison certified with integer arithmetic'),
        ('lattice_wide','finite-graph localization proof proposed; no uniform growing-volume phase or payload rate established')]:print(label+': '+message)
    print(f'TOTAL: PASS={checks} FAIL=0')


if __name__=='__main__':run_checks()
