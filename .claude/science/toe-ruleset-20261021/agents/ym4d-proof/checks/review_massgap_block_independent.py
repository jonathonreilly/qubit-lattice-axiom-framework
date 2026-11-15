#!/usr/bin/env python3
"""Independent finite diagnostics, not a proof of an SU(N) limit theorem.

Uses the non-Abelian quaternion group on a three-edge theta graph; unlike
the author's Z2 graph and SU2 character-cycle diagnostics this constructs
the gauge projector explicitly in coordinate space. All Haar sums are
normalized. Tolerance is fixed before first execution at 5e-11 for identities
and 1e-10 for positive forms; decisive mutation residuals must exceed 1e-7.
"""
from __future__ import annotations
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import eigh
from scipy.special import roots_legendre

START = time.time()
ROWS = []
DIAG = {}
TOL = 5e-11


def check(name, ok, **details):
    ROWS.append(dict(name=name, passed=bool(ok), **details))


def close(name, actual, expected, tol=TOL):
    err = float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    check(name, err <= tol, residual=err, tolerance=tol)


def killed(name, residual, threshold=1e-7):
    check('mutation: '+name, float(residual)>threshold,
          mutation_killed=float(residual)>threshold,
          residual=float(residual), detection_threshold=threshold)


def quaternion_product(a, b):
    return np.r_[a[0]*b[0]-a[1:]@b[1:],
                 a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]


def geometry(d, side=4):
    sites=list(itertools.product(range(side),repeat=d))
    edges=[(x,mu) for x in sites for mu in range(d)]
    index={e:i for i,e in enumerate(edges)}
    def shift(x,mu):
        y=list(x); y[mu]=(y[mu]+1)%side; return tuple(y)
    plaquettes=[]
    for x in sites:
        for mu in range(d):
            for nu in range(mu+1,d):
                plaquettes.append({index[x,mu],index[shift(x,mu),nu],
                                   index[shift(x,nu),mu],index[x,nu]})
    incidence=[[] for _ in edges]
    for p,es in enumerate(plaquettes):
        for e in es: incidence[e].append(p)
    return edges,plaquettes,incidence


for dim in (3,4):
    edges,ps,inc=geometry(dim)
    check(f'actual {dim}D plaquettes per link',
          all(len(q)==2*(dim-1) for q in inc),value=2*(dim-1))
    row=[sum(len(ps[p]-{e}) for p in inc[e]) for e in range(len(edges))]
    check(f'actual {dim}D influence incidence row',
          min(row)==max(row)==6*(dim-1),value=max(row))
    if dim==3:
        block=ps[0]
        touched=set().union(*(set(inc[e]) for e in block))
        check('actual cubic plaquette has four links and thirteen touched plaquettes',
              len(block)==4 and len(touched)==13,b=len(block),p_B=len(touched))
        check('witness exponent from independently counted geometry',
              4*(len(block)+len(touched))==68,value=4*(len(block)+len(touched)))

b=Fraction(1,32)
qplus=14*b
qstep=12*b+b*b/(1-qplus)
rate=b/(1-qstep)
check('rational half-slab endpoint',qplus==Fraction(7,16),value=str(qplus))
check('rational output endpoint',qstep==Fraction(217,576),value=str(qstep))
check('rational physical contraction endpoint',rate==Fraction(18,359),value=str(rate))

# The fundamental of SU(2) is quaternionic but its character is real.
# Integrating w^2 over S3 has exact second moment 1/4 by symmetry; for SU(N)
# with distinct fundamental/conjugate characters Schur gives 2/(4N^2).
check('SU2 real-character normalization',Fraction(1,2**2)==Fraction(1,4))
for n in (3,4,7):
    check(f'SU{n} conjugate pair normalization',Fraction(2,4*n*n)==Fraction(1,2*n*n))

G=np.array([s*np.eye(4,dtype=int)[j] for j in range(4) for s in (1,-1)])
lookup={tuple(g):i for i,g in enumerate(G)}
mul=np.array([[lookup[tuple(quaternion_product(x,y))] for y in G] for x in G])
inv=np.array([lookup[tuple(x*np.array([1,-1,-1,-1]))] for x in G])
check('Q8 noncommutative group control',mul[2,4]!=mul[4,2])
check('Q8 exact inverses',np.all(mul[np.arange(8),inv]==0))
states=np.array(list(itertools.product(range(8),repeat=3)))
state_index={tuple(x):i for i,x in enumerate(states)}
size=len(states)
# All edges point from x to y. There are three two-edge magnetic loops.
pairs=[(0,1),(0,2),(1,2)]
loops=np.array([G[mul[states[:,i],inv[states[:,j]]],0] for i,j in pairs]).T
W=loops[:,0].astype(float)
variant=G[states[:,0],0].astype(float)
perms=[]
for hx,hy in itertools.product(range(8),repeat=2):
    changed=mul[mul[hx,states],inv[hy]]
    perms.append(np.array([state_index[tuple(x)] for x in changed]))
projector=np.zeros((size,size))
for perm in perms: projector[np.arange(size),perm]+=1/64
close('explicit full finite gauge projector is symmetric',projector,projector.T)
close('explicit full finite gauge projector is idempotent',projector@projector,projector)
close('loop is invariant under entire gauge group',projector@W,W)
close('single link trace is gauge variant',projector@variant,0)
DIAG['finite_model']='Q8, two vertices, three parallel oriented edges, three magnetic two-edge loops; labelled analogue only'


def model(beta):
    single=np.exp(beta*(G@G.T))
    raw=np.ones((size,size))
    for e in range(3): raw*=single[states[:,e,None],states[None,:,e]]
    A=np.exp(-beta/2*np.sum(1-loops,axis=1))
    That=(A[:,None]*raw)*A[None,:]/size
    eig,vec=eigh(That)
    psi=vec[:,-1]
    if psi.sum()<0: psi=-psi
    psi*=np.sqrt(size)
    lam=eig[-1]
    u=A*psi
    Q=raw*u[None,:]; Q/=Q.sum(axis=1,keepdims=True)
    projected=raw@projector
    P=projected*u[None,:]; P/=P.sum(axis=1,keepdims=True)
    pi=psi**2/size
    return dict(beta=beta,single=single,raw=raw,A=A,T=That,eig=eig,
                psi=psi,lam=lam,u=u,Q=Q,P=P,pi=pi,projected=projected)


models={beta:model(beta) for beta in (1/32,0.7,2.0)}
for beta,M in models.items():
    A,psi,u,raw,Q,P,pi=[M[k] for k in ('A','psi','u','raw','Q','P','pi')]
    prefix=f'beta={beta:g}: '
    close(prefix+'Perron equation',M['T']@psi,M['lam']*psi)
    close(prefix+'Perron vector invariant',projector@psi,psi)
    close(prefix+'Q stationary under psi squared',pi@Q,pi)
    close(prefix+'Q detailed balance',pi[:,None]*Q,pi[None,:]*Q.T)
    close(prefix+'P and Q agree on invariant loop',P@W,Q@W)
    close(prefix+'projected P kills gauge variant',P@variant,0)
    check(prefix+'Q retains gauge variant direction',np.max(np.abs(Q@variant))>1e-4)
    check(prefix+'positive unprojected finite transfer spectrum',M['eig'][0]>-1e-12)
    # Every local block ratio is tested at every fixed exterior value.
    ratio=psi/A
    worst=max(np.ptp(np.log(ratio[states[:,2]==z])) for z in range(8))
    check(prefix+'block Perron ratio for two links',worst<=4*beta+TOL,
          observed=worst,bound=4*beta)
    D=2*beta*(3+2)
    us=u.reshape(8,8,8)
    osc=max(np.ptp(np.log(us[:,:,z])) for z in range(8))
    check(prefix+'actual A psi block range',osc<=D+TOL,observed=osc,bound=D)
    cond=pi.reshape(8,8,8)
    cond=cond/cond.sum(axis=(0,1),keepdims=True)*64
    L=2*beta*3+4*beta*2
    check(prefix+'conditional finite energy bounds',
          cond.min()>=np.exp(-L)-TOL and cond.max()<=np.exp(L)+TOL,
          density_min=float(cond.min()),density_max=float(cond.max()))
    # Rank-one proof is independently checked as a matrix form in normalized Haar.
    c0=M['single'][0].mean(); single=M['single']/(8*c0)
    kb=np.kron(single,single)
    wb=G[mul[np.repeat(np.arange(8),8),inv[np.tile(np.arange(8),8)]],0]
    rf=np.sinh(beta)/(np.cosh(beta)+3)
    close(prefix+'one-link fundamental multiplier',single@G[:,0],rf*G[:,0])
    close(prefix+'loop tensor multiplier',kb@wb,rf**2*wb)
    close(prefix+'local Haar loop variance',np.mean(wb*wb),0.25)
    m=float(pi@W); fb=wb-m; F=W-m
    inverse_norm=float(fb@np.linalg.solve(kb,fb)/64)
    close(prefix+'rank-one inverse norm',inverse_norm,m*m+0.25/rf**2,tol=1e-6)
    c=1/(1+0.25/rf**2)
    residual=kb-c*np.outer(fb,fb)/64
    mineig=float(eigh(residual,eigvals_only=True)[0])
    check(prefix+'rank-one OPERATOR residual',mineig>=-1e-10,min_eigenvalue=mineig)
    bfun=np.mean(us*(fb[:,None].reshape(8,8,1)**2),axis=(0,1))
    umin=us.min(axis=(0,1))
    kb_all=raw/(size*c0**3)
    num=float((u*F)@kb_all@(u*F)/size)
    den=float(u@kb_all@u/size)
    exterior=float(umin@single@umin/8)
    lower_local=c*float(bfun@single@bfun/8)
    check(prefix+'tensor rank-one quadratic lower bound',num>=lower_local-1e-10)
    check(prefix+'pointwise-positive exterior comparison',
          float(bfun@single@bfun/8)>=0.25**2*exterior-1e-10)
    check(prefix+'magnetic denominator comparison',den<=np.exp(2*D)*exterior+1e-10)
    eta=0.25**2*np.exp(-2*D)/(1+0.25/rf**2)
    corr=float((pi*F)@(Q@F))
    close(prefix+'actual one-step covariance quotient',corr,num/den)
    check(prefix+'positive finite magnetic witness',corr>=eta-1e-10,
          correlation=corr,lower_bound=eta)
    if beta==2.0:
        check('operator positivity does not imply entrywise rank-one residual',
              residual.min() < -1e-4,minimum_entry=float(residual.min()))
    DIAG[prefix+'nonvacuum unprojected eigenvalue']=float(M['eig'][-2]/M['lam'])

M=models[0.7]
raw,A,psi,u,Q,P,pi=[M[k] for k in ('raw','A','psi','u','Q','P','pi')]
# Direct two-step temporal slab with full interior and a terminal half action.
R2=np.zeros(size)
for i in range(size):
    R2[i]=sum(raw[i,j]*A[j]**2*np.mean(raw[j]*A) for j in range(size))/size
close('open slab cap agrees with twice-applied actual transfer',
      R2,M['T']@(M['T']@np.ones(size))/A)
killed('drop magnetic action in implemented slab',
       np.max(np.abs(R2-np.mean(raw,axis=1)**2)))
wrongcap=raw@(A*A*(raw@(A*A)/size))/size
killed('terminal half action replaced by full action',np.max(np.abs(R2-wrongcap)))

# The first attempted fixture (1,i,j) -> (-1,i,j) was gauge equivalent,
# hence its true tilt normalizer was exactly one. Retained attempt02 records
# the surviving omission mutation. Use (1,1,i) -> (-1,1,i), which changes
# the first Wilson loop, to exercise a nontrivial normalizer.
U=state_index[0,0,2]; Ue=state_index[1,0,2]
Uf=state_index[0,1,2]; Uef=state_index[1,1,2]
He=np.log(raw[Ue]/raw[U]); Hf=np.log(raw[Uf]/raw[U])
close('single boundary source full oscillation',np.ptp(He),4*M['beta'])
killed('halve implemented boundary oscillation allowance',np.ptp(He)-2*M['beta'])
base=raw[U]*(A*A)*(raw@A/size)
nodes,weights=roots_legendre(16); nodes=(nodes+1)/2; weights=weights/2
integral=0.
for s,ws in zip(nodes,weights):
    for t,wt in zip(nodes,weights):
        p=base*np.exp(s*He+t*Hf);p/=p.sum()
        integral+=ws*wt*((p*He)@Hf-(p@He)*(p@Hf))
mixed=np.log(R2[Uef])-np.log(R2[Ue])-np.log(R2[Uf])+np.log(R2[U])
close('mixed log partition difference equals integrated actual covariance',mixed,integral)

# Finite tilt, including the exact normalizer. Projection is deliberately
# not used when altering all bottom-field coordinates.
tilted=Q[U]*np.exp(He); tilt_norm=tilted.sum(); tilted/=tilt_norm
close('all-boundary finite tilt including normalizer',tilted,Q[Ue])
killed('omit finite tilt normalizer',abs(tilt_norm-1))
projected_tilt=P[U]*np.exp(He);projected_tilt/=projected_tilt.sum()
killed('identify projected P with unprojected all-boundary Q',
       np.max(np.abs(projected_tilt-P[Ue])))
for label,outweight in [('omit A in output',psi),('omit psi in output',A)]:
    mutated=raw*outweight[None,:];mutated/=mutated.sum(axis=1,keepdims=True)
    killed(label+' conditional',np.max(np.abs(mutated-Q)))
    killed(label+' stationary law',np.max(np.abs(pi@mutated-pi)))
wrongpi=u/u.sum()
killed('center under A psi instead of psi squared',abs(wrongpi@W-pi@W))

# Fourier injectivity is a measure statement. Test a signed measure against
# the full convolution, and show the projected or beta=0 replacements fail.
signed=np.zeros(size);signed[0]=1;signed[1]=-1
observed=raw@signed
close('signed measure recovered through strictly positive Fourier operator',
      np.linalg.solve(raw,observed),signed,tol=5e-8)
check('nonzero signed measure survives full convolution',np.linalg.norm(observed)>1)
zero_mode=variant.copy()
close('projected kernel has variant null direction',M['projected']@zero_mode,0)
check('unprojected convolution retains that direction',np.linalg.norm(raw@zero_mode)>1)
close('beta zero annihilates zero-total signed measure',np.ones((size,size))@signed,0)

# Conditional comparison and physical (one-step) contraction in the analogue.
M=models[1/32]; Q=M['Q'];beta=M['beta'];psi=M['psi'];A=M['A'];u=M['u']
theta_Q=2*beta+beta*beta/(1-4*beta)
theta_r=beta/(1-theta_Q)
def oscillations(f):
    x=f.reshape(8,8,8)
    return np.array([np.ptp(x,axis=j).max() for j in range(3)])
for name,f in [('loop',W),('link trace',variant),('intersecting loop product',loops[:,0]*loops[:,1]),
               ('sum of loops',loops.sum(axis=1))]:
    lhs=oscillations(Q@f).sum();rhs=theta_r*oscillations(f).sum()
    check('physical step contraction: '+name,lhs<=rhs+TOL,observed=float(lhs),bound=float(rhs))
wrongrate=beta*beta/(1-theta_Q)
killed('replace input sensitivity beta by beta squared in contraction',
       oscillations(Q@variant).sum()-wrongrate*oscillations(variant).sum())
# Enumerate all conditional inputs for output edge0, at a fixed input U.
qrow=Q[0].reshape(8,8,8)
condition=qrow/qrow.sum(axis=0,keepdims=True)
sum_tv=0.
for varied in (1,2):
    worst=0.
    for other in range(8):
        for v,vp in itertools.product(range(8),repeat=2):
            p=condition[:,v,other] if varied==1 else condition[:,other,v]
            pp=condition[:,vp,other] if varied==1 else condition[:,other,vp]
            worst=max(worst,float(np.sum(abs(p-pp))/2))
    sum_tv+=worst
check('actual output conditional influence within ground-state majorant',
      sum_tv<=theta_Q+TOL,observed=sum_tv,bound=theta_Q)
# Exact factor-four likelihood source and quarter covariance negative controls.
f=np.r_[np.ones(4),np.zeros(4)]
var=float(np.mean(f*f)-np.mean(f)**2)
close('quarter oscillation covariance at product Haar',var,0.25)
killed('replace covariance quarter by sixteenth',var-np.ptp(f)**2/16)
positive_semidefinite=np.array([[1.,-.9],[-.9,1.]])
lower=np.array([1.,10.]);upper=np.array([2.,10.])
check('negative-entry exterior remains positive operator',
      np.linalg.eigvalsh(positive_semidefinite).min()>0)
killed('replace pointwise-positive exterior by only PSD exterior',
       lower@positive_semidefinite@lower-upper@positive_semidefinite@upper)

result=dict(schema='independent-review-finite-diagnostics-v1',
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            runtime_seconds=time.time()-START,numpy=np.__version__,
            passed=sum(r['passed'] for r in ROWS),total=len(ROWS),
            mutation_total=sum(r['name'].startswith('mutation:') for r in ROWS),
            diagnostics=DIAG,checks=ROWS,
            limitations=['Q8 theta graph is a labelled finite analogue, not SU(N) proof.',
                         'Cubic incidence enumeration is finite at side four.',
                         'No infinite-volume, Fubini, martingale or continuum proof is supplied by this runner.'])
print(json.dumps(result,indent=2))
sys.exit(0 if all(r['passed'] for r in ROWS) else 1)
