#!/usr/bin/env python3
"""Independent finite-chain certificates and scope countercontrols.

Writes only alongside this file. Does not import author code or read results.
Exact assertions use SymPy rational matrices; semigroup evaluations use SciPy.
"""
from pathlib import Path
from itertools import combinations, product
import hashlib,json
import numpy as np
import sympy as s
from scipy.linalg import expm
from scipy.integrate import quad
HERE=Path(__file__).resolve().parent
checks=[]
def done(name,details): checks.append({'name':name,'details':details})
def is_psd_exact(A):
    assert A==A.T.conjugate()
    minors=[]
    for k in range(1,A.rows+1):
        for inds in combinations(range(A.rows),k):
            d=s.factor(A.extract(inds,inds).det())
            assert d.is_nonnegative is True,(A,inds,d)
            minors.append(str(d))
    return len(minors)
def flow_matrix(n,cycles):
    Q=s.zeros(n)
    for vertices,w in cycles:
        for x,y in zip(vertices,vertices[1:]+vertices[:1]):
            assert x!=y
            Q[x,y]+=w
    assert [sum(Q[i,j] for j in range(n)) for i in range(n)]==[sum(Q[j,i] for j in range(n)) for i in range(n)]
    return Q
def negative_form(Q):return s.diag(*[sum(Q[i,j] for j in range(Q.cols)) for i in range(Q.rows)])-Q
# Full and antisymmetric optimal cycle constants, exact Loewner certificates.
cycle_details=[]
for m,C2 in [(2,s.Rational(1)),(3,s.Rational(4,3)),(4,s.Rational(2)),(6,s.Rational(4))]:
    Q=flow_matrix(m,[(list(range(m)),s.Rational(1))]);B=negative_form(Q)
    S=(B+B.T)/2;R=(B-B.T)/2;idx=list(range(1,m))
    S0=S.extract(idx,idx);B0=B.extract(idx,idx);R0=R.extract(idx,idx)
    assert S0.det()>0
    full=s.simplify(C2*S0-B0.T*S0.inv()*B0)
    anti=s.simplify((C2-1)*S0-R0.T*S0.inv()*R0)
    nm=is_psd_exact(full)+is_psd_exact(anti)
    assert full.det()==0 and anti.det()==0 # sharp constants on a Fourier direction
    cycle_details.append({'length':m,'full_constant_squared':str(C2),'anti_constant_squared':str(C2-1),'principal_minors_certified':nm})
done('exact_optimal_cycle_form_certificates',cycle_details)
# Distinct overlapping cycles, rational nonuniform law, two closed components.
pi=s.Matrix([s.Rational(i,28) for i in range(1,8)])
cycles=[([0,1],s.Rational(1,7)),([1,2,3],s.Rational(2,9)),([0,3,4,2],s.Rational(5,13)),([5,6],s.Rational(3,11))]
Q=flow_matrix(7,cycles);B=negative_form(Q);L=-s.diag(*[1/p for p in pi])*B
assert pi.T*L==s.zeros(1,7) and L*s.ones(7,1)==s.zeros(7,1)
S=(B+B.T)/2;R=(B-B.T)/2;idx=[1,2,3,4,6]
S0=S.extract(idx,idx);B0=B.extract(idx,idx);R0=R.extract(idx,idx)
assert S0.det()>0
nm=is_psd_exact(2*S0-B0.T*S0.inv()*B0)+is_psd_exact(S0-R0.T*S0.inv()*R0)
null=s.Matrix([13]*5+[-15]*2)
assert pi.dot(null)==0 and L*null==s.zeros(7,1) and (null.T*S*null)[0]==0
assert len(L.nullspace())==2
done('exact_nonuniform_reducible_overlap_sector_certificate',{'states':7,'closed_components':2,'max_cycle_length':4,'principal_minors_certified':nm,'centered_nonzero_null_function':[int(x) for x in null]})
# Complex semigroup identities, with direct joint-law differences and energy integration.
P=np.array(pi,float).ravel();G=np.array(L,float)
f=np.array([1+2j,-1+1j,2-1j,-3+4j,4-2j,-2-3j,5+1j]);f-=P@f
norm=lambda z:float(np.dot(P,np.abs(z)**2))
D=lambda z:float(-np.real(np.vdot(z,P*(G@z))))
var=norm(f);df=D(f);semigroup=[]
for t in [.0001,.02,.2,1.,5.]:
    T=expm(t*G);pt=T@f
    lhs=float(np.sum(P[:,None]*T*np.abs(f[None,:]-f[:,None])**2))
    correlation=float(2*np.real(np.vdot(f,P*(f-pt))))
    assert np.isclose(lhs,correlation,rtol=2e-11,atol=2e-11)
    integral,error=quad(lambda u:D(expm(u*G)@f),0,t,epsabs=2e-10,epsrel=2e-11)
    energy=(var-norm(pt))/2
    assert np.isclose(integral,energy,rtol=2e-10,atol=3e-10)
    bound=np.sqrt(2)*np.sqrt(2*t*df*var)
    assert lhs<=bound+1e-10
    semigroup.append({'time':t,'direct_stationary_difference':lhs,'sector_bound':float(bound),'energy_integral_error':float(abs(integral-energy))})
eigs=np.linalg.eigvals(G)
assert np.all(np.abs(eigs.imag)<=-eigs.real+1e-10)
done('complex_stationary_semigroup_and_energy_checks',semigroup)
# Explicit Gibbs plaquette orbits, including fixed and period-two configurations.
words=list(product((0,1),repeat=4));lookup={w:i for i,w in enumerate(words)}
rotate=lambda w:(w[-1],)+w[:-1]
def mass(w):
    spins=[2*x-1 for x in w]
    ans=s.Rational(2)**sum(spins[i]*spins[(i+1)%4] for i in range(4))
    for a,b in zip((2,3,5,7),w):ans*=s.Rational(a)**b
    return ans
weights=[mass(w) for w in words];Z=sum(weights);gpi=s.Matrix([w/Z for w in weights])
Lsq=s.zeros(16);Qdecomp=s.zeros(16);orbits=[];seen=set()
for i,w in enumerate(words):
    ap=2+s.Rational(sum(w),8);am=1+s.Rational(sum(w),16)
    for new,a in [(rotate(w),ap),(rotate(rotate(rotate(w))),am)]:
        j=lookup[new]
        if j!=i:Lsq[i,j]+=a/weights[i]
    for edge in range(4):
        new=list(w);j=(edge+1)%4;new[edge],new[j]=new[j],new[edge]
        dest=lookup[tuple(new)]
        if dest!=i:Lsq[i,dest]+=s.Rational(3,5)*min(1,weights[dest]/weights[i])
    Lsq[i,i]=-sum(Lsq[i,j] for j in range(16) if i!=j)
    if i not in seen:
        orbit=[i];v=rotate(w)
        while lookup[v]!=i:orbit.append(lookup[v]);v=rotate(v)
        seen.update(orbit);orbits.append(orbit)
        if len(orbit)>1:
            Qdecomp+=flow_matrix(16,[(orbit,ap/Z),(list(reversed(orbit)),am/Z)])
# Add each physical-bond reversible two-cycle once, retaining repeated channel multiplicity.
for edge in range(4):
    for i,w in enumerate(words):
        new=list(w);j=(edge+1)%4;new[edge],new[j]=new[j],new[edge];dest=lookup[tuple(new)]
        if i<dest:Qdecomp+=flow_matrix(16,[([i,dest],s.Rational(3,5)*min(gpi[i],gpi[dest]))])
Qactual=s.diag(*gpi)*Lsq
for i in range(16):Qactual[i,i]=0
assert Qactual==Qdecomp and gpi.T*Lsq==s.zeros(1,16)
done('exact_Gibbs_plaquette_cycle_decomposition',{'states':16,'permutation_orbit_lengths':sorted(map(len,orbits)),'metropolis_two_cycles_included':True,'nonuniform_rational_Gibbs_weights':[str(x) for x in weights]})
# Immutable two-species loop reversals: four states, all charges zero, nonuniform cycle law.
N=7
loop=lambda c:[tuple((np.array(c)+d)%N) for d in [(0,-1,0),(1,0,0),(0,1,0),(-1,0,0)]]
posA=loop((2,2,1));posB=loop((2,2,4));vectors=[(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]
initial={('A',i):posA[i] for i in range(4)}|{('B',i):posB[i] for i in range(4)}
def reversal(state,species):
    out=state.copy();positions=posA if species=='A' else posB
    for key,p in state.items():
        if key[0]==species:out[key]=positions[(positions.index(p)+2)%4]
    return out
def divergence(state,species):
    field=np.zeros((N,N,N,3),dtype=int)
    for (kind,i),p in state.items():
        if kind==species:field[p]=vectors[i]
    return sum(np.roll(field[...,j],-1,axis=j)-np.roll(field[...,j],1,axis=j) for j in range(3))
states=[initial]
for species in ['A','B','A','B']:states.append(reversal(states[-1],species))
assert states[-1]==states[0] and len({tuple(sorted(x.items())) for x in states[:-1]})==4
for st in states:
    assert len(set(st.values()))==8 and set(st)==set(initial)
    assert not divergence(st,'A').any() and not divergence(st,'B').any()
lpi=s.Matrix([s.Rational(x,11) for x in [1,2,3,5]])
lQ=flow_matrix(4,[([0,1,2,3],s.Rational(1,11))]);lL=-s.diag(*[1/p for p in lpi])*negative_form(lQ)
assert lpi.T*lL==s.zeros(1,4)
done('Gauss_preserving_four_configuration_cycle',{'side':N,'identities':8,'states':4,'stationary_weights':[str(p) for p in lpi],'uniform_flow':'1/11','reversal_order':['A','B','A','B']})
# Long configuration cycle: local jumps alone cannot provide uniform M.
long=[]
for size in [8,16,32,64,128,256]:
    lam=np.exp(2j*np.pi/size)-1;t=.25*size;corr=np.exp(t*lam)
    actual=2*(1-corr.real);false_bound=2*np.sqrt(t*(1-np.cos(2*np.pi/size)))
    long.append({'N':size,'correlation_real':float(corr.real),'correlation_imag':float(corr.imag),'difference':float(actual),'incorrect_M4_bound':float(false_bound),'true_anti_sector_constant':float(1/np.tan(np.pi/size))})
assert long[-1]['difference']>long[-1]['incorrect_M4_bound']
done('long_cycle_local_motion_countercontrol',long)
# Vanishing structure factor: independent nearest-neighbor dimers, M=2.
# Every dimer has exactly one occupied site and flips orientation at rate one.
small=[]
for size in [8,16,32,64,128]:
    k=2*np.pi/size;structure=.5*np.sin(k/2)**2;t=size*.1
    relative=2*(1-np.exp(-2*t))
    small.append({'N':size,'structure_factor':float(structure),'D':float(2*structure),'relative_difference':float(relative),'absolute_difference':float(structure*relative)})
assert small[-1]['relative_difference']>1.99 and small[-1]['absolute_difference']<small[0]['absolute_difference']
# Four-state two-dimer matrix directly confirms the covariance/eigenvalue formula.
size=4;states2=list(product((0,1),repeat=2));G2=np.zeros((4,4));f2=[]
for i,state in enumerate(states2):
    f2.append(sum(np.exp(-2j*np.pi*(2*r+o)/size) for r,o in enumerate(state))/np.sqrt(size))
    for r in range(2):new=list(state);new[r]^=1;G2[i,states2.index(tuple(new))]+=1
    G2[i,i]=-2
f2=np.array(f2);f2-=f2.mean();sf=np.mean(abs(f2)**2)
assert np.allclose(G2@f2,-2*f2) and np.isclose(sf,.5*np.sin(np.pi/size)**2)
done('small_structure_factor_renormalization_countercontrol',small)
# Nonstationary full-support initial product, symmetric exchanges on a cubic torus.
# E F_N(0)=delta sqrt(V)/2 for p_x=1/2+delta cos(2pi x1/N); L F=-4sin²(pi/N)F.
nonstat=[];delta=.2;T=.2
for size in [8,16,32,64,128,256]:
    rate=4*np.sin(np.pi/size)**2;mean0=delta*size**1.5/2
    shift=mean0*np.expm1(-rate*size*T)
    stationary_S=.25;stationary_D=rate*stationary_S
    bound=np.sqrt(2*size*T*stationary_D*stationary_S)
    nonstat.append({'N':size,'nonstationary_mean_shift_squared':float(shift*shift),'stationary_bound_inapplicable':float(bound)})
assert nonstat[-1]['nonstationary_mean_shift_squared']>10*nonstat[-1]['stationary_bound_inapplicable']
done('nonstationary_initial_product_countercontrol',nonstat)
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'status':'all assertions passed',
 'scope':'Exact cycle/flow/form controls; numerical complex semigroup evaluations; exact formulas for scope counterexamples. No author code/results read, no mixing or new hydrodynamic theorem.'}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result,indent=2,allow_nan=False))
