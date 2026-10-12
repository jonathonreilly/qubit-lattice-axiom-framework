#!/usr/bin/env python3
"""Exact author controls for the supplied particle-to-nonlinear-fluid theorem.

Uses Q(omega), omega^2+omega+1=0, for a genuine 3^3 periodic Fourier grid.
No repository imports, numerical FFT, stochastic simulation, or external data.
Source note: SPATIAL_PARTICLE_TO_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md.
These controls support finite CTMC, alias, preparation and scale identities;
the source's analytic argument proves stopping and the smooth-lifetime limit.
The full fluid runner is not reproduced. No quantum histories are modeled.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
from hashlib import sha256
from time import perf_counter
import json
import sys

AUDIT_TIMEOUT_SEC = 180
# Cache/provenance dependencies; no contents are loaded to manufacture the
# finite checks. All model data are reconstructed below from the contract.
AUDIT_INPUT_PATHS = [
    'docs/SPATIAL_PARTICLE_TO_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'docs/D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'docs/SPATIAL_PARTICLE_TO_LINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-09.md',
    'docs/D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md',
    'docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md',
]


class EW:
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        if isinstance(a, EW):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)
    def __add__(self, x):
        x = EW(x)
        return EW(self.a + x.a, self.b + x.b)
    __radd__ = __add__
    def __neg__(self):
        return EW(-self.a, -self.b)
    def __sub__(self, x):
        return self + -EW(x)
    def __mul__(self, x):
        x = EW(x)
        return EW(self.a * x.a - self.b * x.b,
                  self.a * x.b + self.b * x.a - self.b * x.b)
    __rmul__ = __mul__
    def __truediv__(self, x):
        return EW(self.a / x, self.b / x)
    def conj(self):
        return EW(self.a - self.b, -self.b)
    def norm2(self):
        return self.a * self.a - self.a * self.b + self.b * self.b
    def __eq__(self, x):
        x = EW(x)
        return (self.a, self.b) == (x.a, x.b)


def root(n):
    return (EW(1), EW(0, 1), EW(-1, -1))[n % 3]


started = perf_counter()
source = Path(__file__).read_bytes()
print('Supplied nonlinear particle/fluid finite controls; standard library only')
print('AUDIT_TIMEOUT_SEC='+str(AUDIT_TIMEOUT_SEC))
V = list(product((-1, 0, 1), repeat=3))
Z = list(product(range(3), repeat=3))
K = V
M = [F(2, 3) ** (3 - sum(a*a for a in v)) * F(1, 6) ** sum(a*a for a in v) for v in V]
energy = [sum(a*a for a in v) for v in V]
A = [F(5 - 3*e, 2) for e in energy]
CC = [F(3*(e-1), 2) for e in energy]
w, delta, N = F(1, 27), F(1, 20), 101
phase = {(k,z): root(-sum(a*b for a,b in zip(k,z))) for k in K for z in Z}


def invariant(i,j):
    return tuple(V[i][a]+V[j][a] for a in range(3))+(energy[i]+energy[j],)


reactions=[]
for a,b,c,d in combinations(range(27),4):
    for i,j,k,l in ((a,b,c,d),(a,c,b,d),(a,d,b,c)):
        if invariant(i,j)==invariant(k,l):
            reactions.append((i,j,k,l))
assert len(reactions)==288
axial=[]
for r,(i,j,k,l) in enumerate(reactions):
    d1=[V[i][a]-V[j][a] for a in range(3)]
    d2=[V[k][a]-V[l][a] for a in range(3)]
    nz1=[a for a in range(3) if d1[a]]
    nz2=[a for a in range(3) if d2[a]]
    if len(nz1)==len(nz2)==1 and nz1!=nz2 and abs(d1[nz1[0]])==abs(d2[nz2[0]])==2:
        axial.append(r)
assert len(axial)==9
CRparts=[F(0),F(0)]
Sparts=[F(0),F(0)]
for r,(i,j,k,l) in enumerate(reactions):
    cl=int(r in axial)
    Sparts[cl]+=M[i]*M[j]
    CRparts[cl]+=M[i]*M[j]*sum(1/M[v] for v in (i,j,k,l))

# Direct total rates times jump energies at a realizable equilibrium count
# state. Its total N is 216 per cell; every species count is integral.
# Hop rates below omit only the positive factor 1/ell, kept symbolically.
Nc=216*27
counts={(z,v):Nc*w*M[v] for z in Z for v in range(27)}
assert all(n.denominator==1 for n in counts.values())
assert sum(counts.values())==Nc
hop_bracket=F(0)
collision_bracket=F(0)
for z in Z:
    for v,velocity in enumerate(V):
        for d in range(3):
            if velocity[d]:
                rate=abs(velocity[d])*counts[z,v]/delta
                jump_energy=2/(Nc*Nc*w*delta*delta*M[v])
                hop_bracket+=rate*jump_energy
    for i,j,k,l in reactions:
        Jr=sum(1/M[v] for v in (i,j,k,l))
        jump_energy=Jr/(Nc*Nc*w*delta*delta)
        rates=(counts[z,i]*counts[z,j]+counts[z,k]*counts[z,l])/(delta*delta*Nc*w)
        collision_bracket+=rates*jump_energy
assert hop_bracket*Nc*w*delta**3==108
assert collision_bracket*Nc*w*delta**4==2*sum(CRparts)
assert CRparts==[F(124,3),F(4,3)] and Sparts==[F(97,432),F(1,54)]
print('checked: exact count rates at a realizable equilibrium state; both collision directions; volume, clock and quadratic-variation factors')

# A genuinely nonuniform admissible count configuration checks the complete
# conditional drift without a factorization of random variables.
nstate={(z,i):(zi+3*i)%4 for zi,z in enumerate(Z) for i in range(27)}
Nstate=sum(nstate.values())
hstate={(z,i):(F(nstate[z,i],Nstate*w*M[i])-1)/delta for z in Z for i in range(27)}
actual_hop={(z,i):F(0) for z in Z for i in range(27)}
for z in Z:
    actual_coll=[F(0)]*27
    Bh=[F(0)]*27
    ghh=[F(0)]*27
    for i,j,k,l in reactions:
        net_rate=(nstate[z,i]*nstate[z,j]-nstate[z,k]*nstate[z,l])/(delta*delta*Nstate*w)
        linear=M[i]*M[j]*(hstate[z,k]+hstate[z,l]-hstate[z,i]-hstate[z,j])
        quadratic=M[i]*M[j]*(hstate[z,i]*hstate[z,j]-hstate[z,k]*hstate[z,l])
        for q,sign in ((i,-1),(j,-1),(k,1),(l,1)):
            actual_coll[q]+=net_rate*sign/(Nstate*w*delta*M[q])
            Bh[q]+=sign*linear/M[q]
            ghh[q]+=sign*quadratic/M[q]
    assert actual_coll==[-Bh[i]/(delta*delta)+ghh[i]/delta for i in range(27)]
    for i,v in enumerate(V):
        for d in range(3):
            if not v[d]:
                continue
            nxt=list(z)
            nxt[d]=(nxt[d]+v[d])%3
            nxt=tuple(nxt)
            # The same positive factor 1/ell multiplies both sides below.
            hop_rate=abs(v[d])*nstate[z,i]/delta
            dh=1/(Nstate*w*delta*M[i])
            actual_hop[z,i]-=hop_rate*dh
            actual_hop[nxt,i]+=hop_rate*dh
for z in Z:
    for i,v in enumerate(V):
        expected=F(0)
        for d in range(3):
            if v[d]:
                prev=list(z)
                prev[d]=(prev[d]-v[d])%3
                expected+=abs(v[d])*(hstate[tuple(prev),i]-hstate[z,i])/delta
        assert actual_hop[z,i]==expected
print('checked: exact nonlinear conditional drift at every species/cell of a nonuniform integer count state; no expectation closure')


def norm_jump(changes,s):
    out=F(0)
    for k in K:
        by_v={}
        for z,v,value in changes:
            by_v[v]=by_v.get(v,EW())+w*value*phase[k,z]
        out+=(1+sum(a*a for a in k))**s * sum(M[v]*a.norm2() for v,a in by_v.items())
    return out


jump_results={}
cell=(2,1,0)
for s in (0,3,4):
    Ks=sum((1+sum(a*a for a in k))**s for k in K)
    Hd=[sum((1+sum(a*a for a in k))**s*(root(k[d])-1).norm2() for k in K) for d in range(3)]
    assert all(h<=4*Ks for h in Hd)
    if s==0:
        assert Hd==[2*Ks]*3
    for i,j,k,l in reactions:
        Jr=sum(1/M[v] for v in (i,j,k,l))
        changes=[(cell,v,F(sign)/(N*w*delta*M[v])) for v,sign in ((i,-1),(j,-1),(k,1),(l,1))]
        exact=norm_jump(changes,s)
        assert exact==Ks*Jr/(N*N*delta*delta)
        # n/N instead of n/(Nw) loses exactly w^-2 in this norm.
        assert exact != w*w*exact
    for v,velocity in enumerate(V):
        for d in range(3):
            if not velocity[d]:
                continue
            nxt=list(cell)
            nxt[d]=(nxt[d]+velocity[d])%3
            jump=1/(N*w*delta*M[v])
            exact=norm_jump([(cell,v,-jump),(tuple(nxt),v,jump)],s)
            assert exact==Hd[d]/(N*N*delta*delta*M[v])
    jump_results[s]={'K_s_m':Ks,'H_s_m_d':list(map(str,Hd)),
                     'collision_events_checked':288,'directed_velocity_hops_checked':54}
print('checked: actual DFT jump energies for 288 collisions and 54 directed hops in H0,H3,H4')

# At an integer equilibrium state the first collision can overshoot the
# component-control stopping radius. N and delta here are finite controls,
# not the eventual simultaneous schedule. Comparator g=0 is exact.
i,j,k,l=reactions[0]
stop_delta=F(1,Nc)
radius_squared=w*min(M)
exit_energy=sum(F(1,Nc*Nc*w*stop_delta*stop_delta*M[q]) for q in (i,j,k,l))
assert exit_energy>radius_squared
assert all(counts[cell,q]>=1 for q in (i,j))
# The zero pre-jump error makes the generator norm-square increment exactly
# the entire jump energy; clipping it to the radius would change Dynkin's
# formula. This is a finite overshoot witness, not the stopping theorem.
assert min(exit_energy,radius_squared)!=exit_energy

# Exact complete-square identity behind the delta-uniform stopped drift.
# Its tight point uses q=||Qe||=||e||/4, so the projection norm constraint
# q<=||e|| is respected. Dropping a constant changes a tested equality.
lam=1/F(6224911145567,509693499350)
R0=F(3,2)
Ap=sum(CRparts)*(2*R0+1)/2
Lp=Ap*Ap/lam
energy_norm=F(1,7)
test_delta=lam/(4*Ap)
micro_norm=energy_norm/4
drift=-2*lam*micro_norm**2/test_delta**2+2*Ap*micro_norm*energy_norm/test_delta
bound=-lam*micro_norm**2/test_delta**2+Lp*energy_norm**2
assert drift==bound
for ratio in (F(0),F(1,5),F(1,2),F(1)):
    q=ratio*energy_norm
    lhs=-2*lam*q*q/test_delta**2+2*Ap*q*energy_norm/test_delta
    rhs=-lam*q*q/test_delta**2+Lp*energy_norm**2
    assert lam*(rhs-lhs)==(lam*q/test_delta-Ap*energy_norm)**2
print('checked: an admissible stopping overshoot and the exact dissipative complete square, including its sharp coefficient')

# Exactly normalized nonuniform initial probabilities with mean-zero rho.
def cos3(a):
    return F(1) if a%3==0 else F(-1,2)


p={}
for z in Z:
    rho=F(1,29)*cos3(z[2])
    j=(F(2,19)+F(1,23)*cos3(z[1]),F(1,13),F(-1,17))
    for i,v in enumerate(V):
        u=rho*A[i]+3*sum(j[a]*v[a] for a in range(3))
        p[z,i]=w*M[i]*(1+delta*u)
        assert 0<p[z,i]<2*w*M[i]
assert sum(p.values())==1
pv=[sum(p[z,i] for z in Z) for i in range(27)]
assert sum(pv[i]/M[i] for i in range(27))==27
phat={(k,i):sum((p[z,i]*phase[k,z] for z in Z),EW()) for k in K for i in range(27)}
initial_results={}
for s in (0,3,4):
    weights={k:(1+sum(a*a for a in k))**s for k in K}
    Ks=sum(weights.values())
    spectral=sum(weights[k]*(pv[i]-phat[k,i].norm2())/M[i] for k in K for i in range(27))/(N*delta*delta)
    # Independent trace of the full spatial multinomial covariance kernel.
    covariance_kernel={}
    for diff in Z:
        q=sum((weights[k]*root(sum(a*b for a,b in zip(k,diff))) for k in K),EW())
        assert q.b==0
        covariance_kernel[diff]=q.a
    direct=F(0)
    for i in range(27):
        val=F(0)
        for z in Z:
            for zz in Z:
                cov=p[z,i]*(int(z==zz)-p[zz,i])
                diff=tuple((a-b)%3 for a,b in zip(z,zz))
                val+=cov*covariance_kernel[diff]
        direct+=val/M[i]
    direct/=N*delta*delta
    assert direct==spectral
    assert 0<spectral<=27*Ks/(N*delta*delta)
    initial_results[s]={'exact_expectation':str(spectral),
                        'upper_bound':str(27*Ks/(N*delta*delta))}
print('checked: positive mass-normalized preparation and full multinomial covariance versus independent Fourier trace')

# A product outside the principal frequency set actually aliases here.
# g=a cos(y), h=b cos(y) has continuum frequencies 0,+/-2, which fold to
# 0,-/+1 on m=3. All collision output still lies in K-perp exactly.
av=[F(i-13,19) for i in range(27)]
bv=[F((i*i)%11-5,17) for i in range(27)]
out=[F(0)]*27
for i,j,k,l in reactions:
    flux=M[i]*M[j]*(av[i]*bv[j]+av[j]*bv[i]-av[k]*bv[l]-av[l]*bv[k])/2
    for v,sign in ((i,-1),(j,-1),(k,1),(l,1)):
        out[v]+=sign*flux/M[v]
invariants=[[F(1)]*27,*[[F(v[d]) for v in V] for d in range(3)],list(map(F,energy))]
assert any(out)
assert all(sum(M[i]*inv[i]*out[i] for i in range(27))==0 for inv in invariants)
for k in K:
    coeff=sum((w*cos3(z[1])**2*phase[k,z] for z in Z),EW())
    expected=F(1,2) if k==(0,0,0) else F(1,4) if k in ((0,1,0),(0,-1,0)) else 0
    assert coeff==expected
    assert all(sum((M[i]*inv[i]*out[i]*coeff for i in range(27)),EW())==0 for inv in invariants)

def principal(q,m):
    half=(m-1)//2
    return tuple((a+half)%m-half for a in q)


def alias_coefficients(full,m):
    folded={}
    for q,a in full.items():
        p=principal(q,m)
        folded[p]=folded.get(p,F(0))+a
    return folded


full_product={(0,0,0):F(1,2),(0,2,0):F(1,4),(0,-2,0):F(1,4)}
folded=alias_coefficients(full_product,3)
for k in K:
    direct=sum((w*cos3(z[1])**2*phase[k,z] for z in Z),EW())
    assert direct==folded.get(k,F(0))
# A Fourier cutoff drops the +/-2 terms; it is different from sampling.
cutoff={k:a for k,a in full_product.items() if k in K}
assert cutoff!=folded and cutoff[(0,0,0)]==folded[(0,0,0)]
for mesh in (3,5,7,9):
    half=(mesh-1)//2
    multiplicities={}
    for q in product(range(-2*half,2*half+1),repeat=3):
        p=principal(q,mesh)
        assert all(-half<=a<=half for a in p)
        assert sum(a*a for a in p)<=sum(a*a for a in q)
        multiplicities[p]=multiplicities.get(p,0)+1
        if q!=p:
            assert max(abs(a) for a in q)>half
    assert max(multiplicities.values())<=8
    assert max(multiplicities.values())-1<=7<26
print('checked: actual quadratic alias against a direct cyclotomic DFT, cutoff distinction, complete principal-map geometry, and P Gamma=0 after aliasing')

# Exact nearest-neighbor symbol is dissipative before any continuum limit.
for k in K:
    for v in V:
        symbol=sum((abs(v[d])*(root(-v[d]*k[d])-1) for d in range(3)),EW())
        assert symbol.a-symbol.b/2<=0  # real part; the positive 1/ell is omitted

scales={}
mesh_power=2
# The mesh must make the upwind consistency error ell/delta no larger
# than O(delta). Check this before stochastic powers: a coarser mesh can
# improve particle noise while still failing the deterministic comparison.
assert mesh_power-1>=1
for s in (3,4):
    q=4*s+15
    mode_power=mesh_power*(2*s+3)
    exponents={'initial_stopped_failure':q-mode_power-4,
               'hop_stopped_failure':q-mode_power-mesh_power-5,
               'collision_stopped_failure':q-mode_power-6}
    assert exponents=={'initial_stopped_failure':5,'hop_stopped_failure':2,'collision_stopped_failure':3}
    scales[f'H{s}_delta_stop']={'N_power':q,**exponents}
q=19
scales['L2_cell_stop']={'N_power':q,'initial_stopped_failure':q-6*mesh_power-2,
                       'hop_stopped_failure':q-7*mesh_power-3,'collision_stopped_failure':q-6*mesh_power-4,
                       'noise_threshold':F(3*mesh_power,2),'streaming_error':mesh_power-1,'alias_error':2*mesh_power-1,
                       'cutoff_error':2*mesh_power,'interpolation_error':mesh_power,'fluid_error':1}
assert scales['L2_cell_stop']['hop_stopped_failure']==2
assert min(scales['L2_cell_stop'][k] for k in ('streaming_error','alias_error','cutoff_error','interpolation_error','fluid_error'))>=1
assert 18-7*mesh_power-3<2  # a smaller N does not deliver the stated failure order
scales['L2_cell_stop']['noise_threshold']=str(scales['L2_cell_stop']['noise_threshold'])
print('checked: simultaneous error and failure exponents with distinct hop, collision, initial and mesh contributions')

print(json.dumps({'grid':{'m':3,'cell_weight':str(w),'N':N,'delta':str(delta)},
                  'finite_constants':{'C_R_rest_and_alpha_coefficients':list(map(str,CRparts)),
                                      'S_rest_and_alpha_coefficients':list(map(str,Sparts))},
                  'equilibrium_rate_sum_checks':{'N':Nc,'hop_coefficient':108,
                                                 'collision_coefficient_in_units_C_R':2,
                                                 'F_le_2M_upper_hop_coefficient':216,
                                                 'F_le_2M_upper_collision_coefficient_in_units_C_R':8},
                  'jump_checks':jump_results,'multinomial_covariance_checks':initial_results,
                  'aliased_collision_output_is_microscopic':True,
                  'all_upwind_symbols_dissipative':True,
                  'stopped_energy_checks':{'overshoot_energy':str(exit_energy),'radius_squared':str(radius_squared),
                                           'complete_square_checked':True},
                  'scale_checks':scales,
                  'limits':'Finite exact normalizations and exponents; analytic proof supplies stopping, alias estimates and PDE comparison.'},indent=2))
assert source==Path(__file__).read_bytes()
print('All exact particle/grid checks verified; wrong cell normalization and undersized N schedule rejected.')
print('runtime_seconds=%.6f'%(perf_counter()-started))
print('python='+sys.version.split()[0]+'; dependencies=Python standard library only; runtime inputs=none except source bytes for provenance hash')
print('script_sha256='+sha256(source).hexdigest())
