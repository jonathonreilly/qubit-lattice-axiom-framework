#!/usr/bin/env python3
"""Finite full-space controls of the supplied static local-reference SWAP.
General-N estimates are proved in the bound note, not inferred from these fixtures.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import signal,sys,time,json,math,itertools
from decimal import Decimal as D,localcontext,ROUND_CEILING
from fractions import Fraction as F
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('archive/local_reference_static_swap_review_2026_10_18/MANIFEST.json', 'archive/local_reference_static_swap_review_2026_10_18/original-recovery.tar.gz', 'docs/LOCAL_REFERENCE_STATIC_SWAP_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'outputs/local_reference_static_swap_review_2026_10_18/INPUT_CLOSURE.json', 'outputs/local_reference_static_swap_review_2026_10_18/README.md', 'outputs/local_reference_static_swap_review_2026_10_18/proofs/local_reference_chain_weights.md', 'outputs/local_reference_static_swap_review_2026_10_18/proofs/local_reference_static_swap.md', 'outputs/local_reference_static_swap_review_2026_10_18/proofs/product_reference_static_swap.md') # filled by external packaging
if not __debug__:
    raise RuntimeError('Assertions must remain enabled')
def expired(signum,frame):
    raise TimeoutError('180-second declared cap reached')
signal.signal(signal.SIGALRM,expired)
signal.alarm(AUDIT_TIMEOUT_SEC)
import numpy as np
import sympy as sp
COUNT=0

def check(label,condition,**data):
    global COUNT
    if not bool(condition):
        print('[FAIL] '+label+' '+json.dumps(data),flush=True)
        raise AssertionError(label)
    COUNT+=1
    print('[PASS] '+label+' '+json.dumps(data,sort_keys=True),flush=True)

def norm(a):
    return float(np.linalg.norm(a,2))
def unitary(h,t):
    e,v=np.linalg.eigh(h)
    return (v*np.exp(-1j*t*e))@v.conj().T
I=np.eye(2);X=np.array([[0.,1.],[1.,0.]]);Y=np.array([[0.,-1j],[1j,0.]]);Z=np.diag([1.,-1.]);number=np.diag([0.,1.])
def tensor(items):
    out=np.array([[1.]])
    for a in items:out=np.kron(out,a)
    return out
def local(n,j,a):
    return tensor([a if i==j else I for i in range(n)])
def swap(n,a,b):
    dim=1<<n;mat=np.zeros((dim,dim))
    for i in range(dim):
        aa=(i>>(n-1-a))&1;bb=(i>>(n-1-b))&1
        j=i if aa==bb else i^(1<<(n-1-a))^(1<<(n-1-b))
        mat[j,i]=1
    return mat
def exchange(n,a,b):
    return (local(n,a,X)@local(n,b,X)+local(n,a,Y)@local(n,b,Y))/2

def gate():
    x=sp.symbols('x');xx=sp.Matrix(X.astype(int));zz=sp.Matrix(Z.astype(int));ii=sp.eye(2)
    h=(sp.kronecker_product(xx,ii)+sp.kronecker_product(ii,xx))/sp.sqrt(2)+sp.sqrt(5)*(sp.kronecker_product(zz,ii)+sp.kronecker_product(ii,zz))/4+sp.Rational(3,4)*sp.kronecker_product(zz,zz)
    poly=sp.expand(h.charpoly(x).as_expr());expected=sp.prod(x-r for r in [-sp.Rational(7,4),-sp.Rational(3,4),sp.Rational(1,4),sp.Rational(9,4)])
    check('full four-dimensional exact spectrum',sp.simplify(poly-expected)==0,polynomial=str(poly))
    hf=np.array(h.evalf(),complex);target=np.exp(-1j*np.pi/4)*swap(2,0,1);u=unitary(hf,np.pi)
    check('coherent singlet and triplet SWAP phases',norm(u-target)<2e-13,error=norm(u-target),missing_scalar_phase_error=norm(u-swap(2,0,1)))
    check('omitted scalar phase mutant differs',norm(u-swap(2,0,1))>.5)
    return hf

def reference(N,heff):
    # Symmetric projector constructed from normalized Hamming-weight states.
    dim=1<<N;columns=np.zeros((dim,N+1))
    for z in range(dim):columns[z,z.bit_count()]=1/math.sqrt(math.comb(N,z.bit_count()))
    pi=columns@columns.T;eye=np.eye(dim);q=eye-pi
    chain=sum((eye-swap(N,j,j+1) for j in range(N-1)),np.zeros((dim,dim)))
    complete=sum((eye-swap(N,j,k) for j in range(N) for k in range(j+1,N)),np.zeros((dim,dim)))
    ev=np.linalg.eigvalsh(chain);gap=float(min(ev[ev>1e-9]))
    check(f'N={N} complete-space symmetric kernel and gap',norm(chain@pi)<1e-13 and np.sum(abs(ev)<1e-9)==N+1 and np.linalg.eigvalsh(chain-q/N**2).min()>-1e-12,gap=gap,lower_bound=1/N**2,kernel=N+1)
    check(f'N={N} complete-graph versus path forms',np.linalg.eigvalsh(N**3*chain-complete).min()>-1e-10 and np.linalg.eigvalsh(complete-N*q).min()>-1e-11)
    weights=np.linspace(.3,.9,N-1);weighted=sum((w*(eye-swap(N,j,j+1)) for j,w in enumerate(weights)),np.zeros((dim,dim)))
    check(f'N={N} unequal positive chain kernel',norm(weighted@pi)<1e-13 and np.linalg.eigvalsh(weighted-weights.min()*q/N**2).min()>-1e-12,weights=weights.tolist())
    # Compress actual P-B1 exchange on all data/reference inputs, not a sector.
    n=N+2;P=np.kron(np.eye(4),pi);loc=exchange(n,1,2);star=sum((exchange(n,1,j+2) for j in range(N)),np.zeros((1<<n,1<<n),complex))/N
    check(f'N={N} exact projected local exchange',norm(P@(loc-star)@P)<2e-13 and norm((np.eye(1<<n)-P)@star@P)<2e-13)
    beta=np.ones(dim)/math.sqrt(dim);E=np.kron(np.eye(4),beta[:,None]);g=math.sqrt(2);residual=(g*star-local(n,1,X)/math.sqrt(2))@E;sing=np.linalg.svd(residual,compute_uv=False)
    check(f'N={N} all-input product-reference residual',max(abs(sing-g/(2*math.sqrt(N))))<2e-13,singular_values=sing.tolist())
    # Construct literal positive physical blocks and exact free-factor identity.
    lam=.125;omega=1.;kap=.4;a=lam/math.sqrt(2);b=math.sqrt(5)*lam/4;c=3*lam/4;gg=math.sqrt(2)*lam;ident=np.eye(1<<n)
    block_list=[((0,),a*(ident+local(n,0,X))),((0,),b*(ident+local(n,0,Z))),((1,),b*(ident+local(n,1,Z))),((0,1),c*(ident+local(n,0,Z)@local(n,1,Z))),((1,2),gg*(ident+loc))]
    block_list += [((j+2,j+3),kap*(ident-swap(n,j+2,j+3))) for j in range(N-1)]
    block_list += [((j,),omega*local(n,j,number)) for j in range(1,n)]
    HE=sum((omega*local(n,j,number) for j in range(1,n)),np.zeros((1<<n,1<<n)))
    H=sum((v for _,v in block_list),np.zeros_like(HE,dtype=complex));HF=np.kron(np.eye(4),kap*chain);HS=a*local(n,0,X)+b*(local(n,0,Z)+local(n,1,Z))+c*local(n,0,Z)@local(n,1,Z);W=HS+gg*loc;s=a+2*b+c+gg
    mine=min(np.linalg.eigvalsh(v).min() for _,v in block_list);comm=max(norm(HE@v-v@HE) for _,v in block_list)
    loads=[sum(norm(v) for support,v in block_list if j in support) for j in range(n)]
    expected=[2*a+2*b+2*c,omega+2*b+2*c+2*gg]+[omega+2*kap*((j>0)+(j<N-1))+(2*gg if j==0 else 0) for j in range(N)]
    check(f'N={N} full-support positivity commutation and loads',mine>-2e-13 and comm<2e-13 and len(block_list)==2*N+5 and np.max(abs(np.array(loads)-expected))<2e-13,min_eigenvalue=float(mine),loads=loads,blocks=len(block_list))
    revival_error=norm(unitary(HE,np.pi/lam)-ident)
    data_energy=omega*np.kron(I,number)
    check(f'N={N} full free-energy revival and noncommuting comparison',revival_error<1e-12 and norm(data_energy@heff-heff@data_energy)>.1,revival_error=revival_error)
    for t in [.17,.8]:
        error=norm(unitary(H,t)-np.exp(-1j*s*t)*unitary(HE,t)@unitary(HF+W,t))
        # Ordered star comparator retains actual free reference profile.
        beta_t=np.exp(-1j*omega*t*np.array([z.bit_count() for z in range(dim)]))*beta
        comparison=np.exp(-1j*s*t)*np.kron(unitary(omega*np.kron(I,number),t)@unitary(lam*heff,t),beta_t[:,None])
        Hstar=HE+s*ident+HS+gg*star
        starerror=norm(unitary(Hstar,t)@E-comparison)
        check(f'N={N} ordered free/scalar factors t={t}',error<3e-13 and starerror<=gg*t/(2*math.sqrt(N))+3e-13,factor_error=error,complete_star_error=starerror,bound=gg*t/(2*math.sqrt(N)))

def leakage():
    # A nondegenerate complement and two-dimensional zero sector; full outputs kept.
    A=np.diag([0.,0.,7.,11.,23.]);P=np.diag([1.,1.,0.,0.,0.]);Q=np.eye(5)-P
    W=np.array([[.2,.07,.1,-.05,.03],[.07,-.1,.02,.08,-.04],[.1,.02,.15,.06,0],[-.05,.08,.06,-.2,.09],[.03,-.04,0,.09,.1]])
    v=norm(W);c=norm(Q@W@P);d=7-v
    for t in [.1,1.,4.]:
        actual=unitary(A+W,t)@P;comparison=unitary(P@W@P,t)@P
        qb=c/d*(2+v*t);pb=c*c/d*(2*t+v*t*t/2)
        check(f'complete leakage integration bound t={t}',norm(Q@actual)<=qb and norm(P@actual-comparison)<=pb and norm(actual-comparison)<=qb+pb,leakage=norm(Q@actual),projected=norm(P@actual-comparison),complete=norm(actual-comparison),bound=qb+pb)
    constant=2*math.sqrt(2)*(2+8*math.pi)+16*math.pi+32*math.pi**2
    check('uniform elimination coefficient below512',constant<512,constant=constant)

def policy():
    with localcontext() as ctx:
        ctx.prec=90;pi=D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628');sqrt2=D(2).sqrt();cp=(D(5).sqrt()+3)/2+2*sqrt2
        for eps,omega,margin,eta in itertools.product(map(D,['1','.4','.1']),map(D,['.3','1.5']),map(D,['.25','2']),map(D,['1','.2'])):
            # All rational cap boundaries and integer ceilings are exact. In
            # these fixtures the third cap is the minimum: c_plus<6, so the
            # stronger rational 12*third<=margin certifies its irrational cap.
            ceilq=lambda q:-(-q.numerator//q.denominator)
            dec=lambda q:D(q.numerator)/D(q.denominator)
            ee,oo,mm,et=map(F,(eps,omega,margin,eta))
            pi_lo=F(pi);pi_hi=pi_lo+F(1,10**(-pi.as_tuple().exponent))
            N=ceilq(512*pi_lo*pi_lo/(ee*ee))
            assert N==ceilq(512*pi_hi*pi_hi/(ee*ee))
            kapq=mm/8;deltaq=et*kapq/(N*N);lmq=ee*deltaq/16384
            assert lmq<=oo/2 and 12*lmq<=mm
            ratioq=oo/(2*lmq);m=ceilq(ratioq);lamq=oo/(2*m)
            exact_caps=(ratioq<=m<ratioq+1 and lmq/2<=lamq<=lmq and lamq<=deltaq/8)
            kap,delta,lam=map(dec,(kapq,deltaq,lamq))
            tau=pi/lam;w=eps/(32*(omega+D(9)*lam/4));g=sqrt2*lam
            loads=[lam*(sqrt2+(D(5).sqrt()+3)/2),omega+cp*lam,omega+2*kap+2*g,omega+4*kap]
            leak=512*lam/delta;center=leak+pi/(D(2*N).sqrt());edge=leak+g*(tau+w)/(2*D(N).sqrt())+(omega+D(9)*lam/4)*w
            ok=(exact_caps and w<tau and center<=eps/16 and edge<eps/8 and max(loads)<omega+margin)
            check(f'simultaneous policy eps={eps} omega={omega} margin={margin} eta={eta}',ok,N=N,m=m,lambda_value=str(lam),center_bound=str(center),window_bound=str(edge),epsilon_over8=str(eps/8),max_load=str(max(loads)),qubits=N+2,blocks=2*N+5)

def main():
    heff=gate()
    for N in [2,3,4]:reference(N,heff)
    leakage();policy()
    print('per_element: All four coherent data amplitudes and scalar/singlet phases are checked, with full positive local block spectra.')
    print('per_site: Incident full-support norms and equal-gap commutators are checked for each finite-chain site; exact supplied coefficients are assumed.')
    print('per_mode: Full reference Hilbert spaces, symmetric kernel, complementary gap, compressed exchange and all residual singular values are retained.')
    print('per_block: Complete output leakage and ordered free evolution are checked; no postselection, discarded reference output or fitted phase is used.')
    print('lattice_wide: General finite-chain and accuracy estimates remain the written proof; small matrices do not simulate the enormous policy N or establish a native bulk realization, preparation, halt or reuse.')
    print(f'TOTAL: PASS={COUNT} FAIL=0',flush=True)
if __name__=='__main__':main()
