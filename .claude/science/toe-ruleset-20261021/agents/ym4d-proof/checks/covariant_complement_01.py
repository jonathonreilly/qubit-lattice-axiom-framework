#!/usr/bin/env python3
"""Finite actual-model diagnostics; criteria saved before implementation."""
import itertools as it
import json
import math
import os
from pathlib import Path
import time
import numpy as np
from scipy.linalg import expm, logm
from scipy.special import i1e
from numpy.polynomial.legendre import leggauss

start = time.monotonic()
records = []
rng = np.random.default_rng(291021)


def check(name, ok, data, mutation=False):
    entry = dict(name=name, passed=bool(ok), mutation=mutation, data=data)
    records.append(entry)
    print(json.dumps(entry, sort_keys=True), flush=True)


def shift(x, mu, step=1, period=None):
    y = list(x)
    y[mu] += step
    if period:
        y = [z % period for z in y]
    return tuple(y)


def hermitian(N):
    z = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
    a = (z+z.conj().T)/2
    a -= np.trace(a)/N*np.eye(N)
    return a/np.linalg.norm(a)


def haar(N):
    z = rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
    q,r = np.linalg.qr(z)
    q = q @ np.diag(np.diag(r)/abs(np.diag(r)))
    q[:,0] /= np.linalg.det(q)
    return q


def plaque(field, x, mu, nu, period=None):
    return (field[(x,mu)] @ field[(shift(x,mu,period=period),nu)] @
            field[(shift(x,nu,period=period),mu)].conj().T @ field[(x,nu)].conj().T)


def defect(a):
    return float(np.linalg.norm(np.eye(len(a))-a,2))


# Actual open four-dimensional block. Arbitrary vertex gauges are retained.
L=3
sites = list(it.product(range(-1,2),repeat=4))
edges = [(x,mu) for x in sites for mu in range(4) if x[mu]<1]
plaquettes = [(x,mu,nu) for x in sites for mu in range(4) for nu in range(mu+1,4)
              if x[mu]<1 and x[nu]<1]
tree = {e for e in edges if all(e[0][nu]==0 for nu in range(e[1]+1,4))}
check('actual_open_block_counts', len(edges)==216 and len(tree)==80 and len(plaquettes)==216,
      dict(links=len(edges),tree=len(tree),plaquettes=len(plaquettes)))
for N in (2,3):
    ident=np.eye(N,dtype=complex)
    directions={e: (np.zeros((N,N),complex) if e in tree else hermitian(N)) for e in edges}
    eps=min(.25,1/(32*3),1/(384*9),math.pi/(8*N*3))
    def field_at(s):
        return {e:expm(1j*s*a) for e,a in directions.items()}
    def maxp(field):
        return max(defect(plaque(field,*p)) for p in plaquettes)
    lo,hi=0.,.01
    for unused in range(38):
        mid=(lo+hi)/2
        if maxp(field_at(mid))<eps*(1-1e-8): lo=mid
        else: hi=mid
    base=field_at(lo)
    gauge={x:haar(N) for x in sites}
    gauge[(0,0,0,0)]=ident
    original={e:gauge[e[0]].conj().T@base[e]@gauge[shift(*e)] for e in edges}
    recovered={}
    for x in sites:
        y=(0,0,0,0); val=ident.copy()
        for mu in range(4):
            direction=1 if x[mu]>=0 else -1
            for unused in range(abs(x[mu])):
                if direction==1: val=val@original[(y,mu)]; y=shift(y,mu)
                else: y=shift(y,mu,-1); val=val@original[(y,mu)].conj().T
        recovered[x]=val
    fixed={e:recovered[e[0]]@original[e]@recovered[shift(*e)].conj().T for e in edges}
    error=max(np.linalg.norm(fixed[e]-base[e]) for e in edges)
    check(f'SU{N}_rooted_tree_and_gauge',error<2e-11 and abs(maxp(original)-maxp(base))<2e-11,
          dict(matrix_error=float(error),max_original=maxp(original),max_fixed=maxp(fixed),epsilon=eps))
    r=eps/1000; t=1-32*r/eps
    contracted={e:recovered[e[0]].conj().T@expm(t*logm(fixed[e]))@recovered[shift(*e)] for e in edges}
    max_contract=maxp(contracted)
    max_perturb=0.
    for unused in range(2):
        cap={e:expm(1j*.99*r*hermitian(N))@contracted[e] for e in edges}
        max_perturb=max(max_perturb,maxp(cap))
    check(f'SU{N}_simultaneous_cut_cap',max_contract<=eps-8*r+2e-11 and max_perturb<eps,
          dict(radius=r,t=t,predicted_margin=8*r,actual_margin=eps-max_contract,
               perturbed_margin=eps-max_perturb,all_plaquettes=len(plaquettes)))
    if N==2:
        wrong={e:expm(t*logm(v)) for e,v in original.items()}
        check('ungauged_log_contraction_mutation',maxp(wrong)>10*eps,
              dict(wrong_max_defect=maxp(wrong),cut=eps),True)


# The finite periodic S4-prime geometry, including all 64 coarse links.
period=6; crossing=((1,1,0,0),0); internal=((0,0,0,0),0)
perms=list(it.permutations(range(4)))
offsets=list(it.product(range(-1,2),repeat=4))
def leg(root,off,perm):
    x=tuple(v%period for v in root); out=[]
    for mu in perm:
        for unused in range(abs(off[mu])):
            if off[mu]>0: out.append(((x,mu),1)); x=shift(x,mu,period=period)
            else: x=shift(x,mu,-1,period); out.append(((x,mu),-1))
    return out,x
def word(root,mu,off,perm):
    left,x=leg(root,off,perm); straight=[]
    for unused in range(L):
        straight.append(((x,mu),1)); x=shift(x,mu,period=period)
    right,unused=leg(shift(root,mu,L,period),off,perm)
    return left+straight+[(e,-sign) for e,sign in reversed(right)],straight
cross_counts={}; internal_full=0; internal_straight=0; selected=[]; repeated=0
for X in it.product(range(2),repeat=4):
    root=tuple(3*x for x in X)
    for mu in range(4):
        count=0
        for off in offsets:
            for perm in perms:
                w,straight=word(root,mu,off,perm)
                hit=sum(e==crossing for e,sign in w)
                count+=hit; repeated=max(repeated,hit)
                internal_full+=sum(e==internal for e,sign in w)
                internal_straight+=sum(e==internal for e,sign in straight)
                if X==(0,0,0,0) and mu==0: selected.append(w)
        if count: cross_counts[str((X,mu))]=count
check('actual_S4_crossing_incidence',list(cross_counts.values())==[72] and repeated==1 and len(selected)==1944,
      dict(readers=cross_counts,max_multiplicity=repeated,words_per_kernel=len(selected),mean=72/1944))
check('paired_root_leg_incidence_mutation',internal_full>internal_straight,
      dict(interior_reader_occurrences_full=internal_full,without_root_legs=internal_straight),True)

sigma=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
I=np.eye(2,dtype=complex)
V=[expm(.55j*sigma[0]),expm(.37j*sigma[1]),I,I]
P=V[0]@V[1]@V[0].conj().T@V[1].conj().T
qP=float(np.trace(P).real/2)
vP=np.array([(np.trace(P@s)/(2j)).real for s in sigma]); vnorm=float(np.linalg.norm(vP))
all_sites=list(it.product(range(period),repeat=4))
lift={(x,mu):(V[mu] if (x[mu]+1)%L==L-1 else I) for x in all_sites for mu in range(4)}
def block(x): return tuple(((v+1)//L)%2 for v in x)
touched=[]
for x in all_sites:
    for mu in range(4):
        for nu in range(mu+1,4):
            pe=[(x,mu),(shift(x,mu,period=period),nu),(shift(x,nu,period=period),mu),(x,nu)]
            if crossing in pe: touched.append((x,mu,nu))
cut_flags=[]
for x,mu,nu in touched:
    verts=[x,shift(x,mu,period=period),shift(x,nu,period=period),shift(shift(x,mu,period=period),nu,period=period)]
    cut_flags.append(len({block(y) for y in verts})==1)
check('crossing_Wilson_and_cut_readers',len(touched)==6 and not any(cut_flags),
      dict(plaquettes=[str(p) for p in touched],interior_cut_flags=cut_flags))
f=1/27
for ix,a in enumerate((np.array([.11,.08,-.07]),np.array([-.12,.04,.17]))):
    Q=expm(1j*sum(a[i]*sigma[i] for i in range(3)))
    field=dict(lift); field[crossing]=Q@V[0]
    mean=np.zeros((2,2),complex)
    for w in selected:
        mat=I.copy()
        for e,sign in w: mat=mat@(field[e] if sign==1 else field[e].conj().T)
        mean+=mat/len(selected)
    expected=((1-f)*I+f*Q)@V[0]
    six=sum(1-np.trace(plaque(field,*p,period=period)).real/2 for p in touched)
    predicted=5*(1-np.trace(Q).real/2)+1-np.trace(Q@P).real/2
    check(f'actual_noncommuting_density_words_{ix}',np.linalg.norm(mean-expected)<2e-11 and abs(six-predicted)<2e-11,
          dict(mean_error=float(np.linalg.norm(mean-expected)),Wilson_error=float(abs(six-predicted)),Wilson=six))


# Full SU(2) Haar conditional integral; the sphere angle is integrated,
# not frozen to one colour. The second implementation does its z quadrature.
kappa=1.3
def logH(z):
    z=np.asarray(z)
    return np.where(z<1e-8,z*z/8,np.log(2*i1e(np.maximum(z,1e-8))/np.maximum(z,1e-8))+z)
def sinhc(z):
    z=np.asarray(z,dtype=complex)
    out=np.ones_like(z)
    take=abs(z)>1e-7
    out[take]=np.sinh(z[take])/z[take]
    out[~take]=1+z[~take]**2/6
    return out
def integrate(u,eps,low=0.,high=math.pi,angular=False,drop_normalizer=False,flat_angle=False,
              drop_curvature=False,subtract_vacuum=False,n=240):
    x,w=leggauss(n); theta=(high-low)*x/2+(high+low)/2; wt=w*(high-low)/2
    c=np.cos(theta); s=np.sin(theta); radius=np.sqrt(1-2*f*(1-f)*(1-c)); t=kappa*u
    qq=1. if drop_curvature else qP; vv=0. if drop_curvature else vnorm
    core=-u*(5*(1-c)+(1+eps)*(1-qq*c))+t*(1-f+f*c)
    if not drop_normalizer: core-=logH(t*radius)
    if subtract_vacuum: core+=u*eps*(1-qP)
    if angular:
        z,zw=leggauss(160)
        orient=np.exp(-u*(1+eps)*s[:,None]*vv*z[None,:])@(zw/2)
    else: orient=sinhc(u*(1+eps)*s*vv)
    density=np.ones_like(s)/math.pi if flat_angle else (2/math.pi)*s*s
    return complex(np.sum(wt*density*np.exp(core)*orient))
def shell_bounds(h):
    return (2*math.asin((.45-h)/2),2*math.asin((.45+h)/2))
def probability(u,eps,h=.015,**kw):
    low,high=shell_bounds(h)
    return integrate(u,eps,low,high,**kw)/integrate(u,eps,**kw)
for u in (1,8,40):
    z1=integrate(u,.1); z2=integrate(u,.1,angular=True,n=300)
    probs=[probability(u,.1,h).real for h in (.015,.0075,.00375)]
    ratios=[probs[i]/probs[i+1] for i in range(2)]
    check(f'full_Haar_angular_integral_u{u}',abs(z1-z2)/abs(z1)<2e-9,
          dict(Z_analytic=[z1.real,z1.imag],Z_angular=[z2.real,z2.imag],relative_error=abs(z1-z2)/abs(z1)))
    check(f'actual_boundary_shell_u{u}',all(1.85<x<2.15 for x in ratios),
          dict(probabilities=probs,successive_ratios=ratios))
baseline=probability(8,.1).real
for label,kw in [('normalizer',dict(drop_normalizer=True)),('full_Haar',dict(flat_angle=True)),
                 ('noncommuting_curvature',dict(drop_curvature=True))]:
    wrong=probability(8,.1,**kw).real
    check(label+'_mutation',abs(wrong-baseline)>1e-6,
          dict(correct=baseline,mutated=wrong,difference=wrong-baseline),True)
z0=integrate(8,0)
ratio=integrate(8,.1)/z0
vac=math.exp(-8*.1*(1-qP))
sub=integrate(8,.1,angular=True,subtract_vacuum=True,n=300)/z0
check('original_source_vacuum_identity',abs(ratio-vac*sub)<2e-10,
      dict(ratio=ratio.real,vacuum=vac,subtracted_expectation=sub.real,error=abs(ratio-vac*sub)))
check('source_vacuum_omission_mutation',abs(ratio-sub)>1e-5,
      dict(correct=ratio.real,omitted=sub.real,difference=abs(ratio-sub)),True)
low,high=shell_bounds(.015)
complex_shell=integrate(8,.1+.07j,low,high)
real_shell=integrate(8,.1,low,high).real
check('raw_complex_source_envelope',abs(complex_shell)<=real_shell*(1+2e-10),
      dict(complex_shell=[complex_shell.real,complex_shell.imag],positive_real_envelope=real_shell))
theta=2*math.asin(.45/2); tiny=1e-8
below=expm(1j*(theta-tiny)*sigma[2]); above=expm(1j*(theta+tiny)*sigma[2])
check('hard_root_selector_sup_jump',defect(below)<.45<defect(above),
      dict(left=defect(below),right=defect(above),displacement=float(np.linalg.norm(above-below,2)),indicator_jump=1))

summary=dict(records=records,passed=sum(x['passed'] for x in records),total=len(records),
             mutations=sum(x['mutation'] for x in records),elapsed_seconds=time.monotonic()-start,
             numerical_threads={k:os.environ.get(k) for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
             scope='Finite full-colour block geometry and full-SU2 conditional-Haar diagnostics only')
Path(__file__).with_name('covariant_complement_01_results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='records'},sort_keys=True),flush=True)
raise SystemExit(0 if summary['passed']==len(records) else 1)
