#!/usr/bin/env python3
"""Finite diagnostics for SOURCE_SEA_CONSTRUCTION_ASTRA.md; no continuum claim.

Run from any directory. JSON is printed to stdout; caller preserves each run.
The four-dimensional geometry uses actual links. The exact Z2 model and the
rational replacement fixture are explicitly different, smaller models.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json
import math
import platform
import sys
import traceback

import mpmath as mp
import numpy as np


def shift(x, a, n, d=1):
    y = list(x)
    y[a] = (y[a] + d) % n
    return tuple(y)


def cell_vertices(x, n):
    return {tuple((a+b) % n for a, b in zip(x, bit))
            for bit in product((0, 1), repeat=4)}


def cell_edges(x, n):
    return {(y, a) for a in range(4)
            for y in cell_vertices(x, n) if y[a] == x[a]}


def cell_plaquettes(x, n):
    return {(y, a, b) for a, b in combinations(range(4), 2)
            for y in cell_vertices(x, n) if y[a] == x[a] and y[b] == x[b]}


def touched_plaquettes(edges, n):
    out = set()
    for x, a in edges:
        for b in range(4):
            if a != b:
                lo, hi = sorted((a, b))
                out.add((x, lo, hi))
                out.add((shift(x, b, n, -1), lo, hi))
    return out


def geometry():
    n = 6
    sites = list(product(range(n), repeat=4))
    incidence = Counter(p for x in sites for p in cell_plaquettes(x, n))
    assert len(incidence) == 6*n**4 and set(incidence.values()) == {4}
    witness_p = next(iter(incidence))
    witness_bad_cells = [x for x in sites if witness_p in cell_plaquettes(x,n)]
    # A single plaquette witness creates four cell events; counting it once
    # per cell would falsely demand four distinct plaquettes.
    wrong_distinct_bad_plaquette_lower_bound = len(witness_bad_cells)
    assert 1 < wrong_distinct_bad_plaquette_lower_bound
    assert all(len(cell_edges(x, n)) == 32 and len(cell_plaquettes(x, n)) == 24
               for x in sites)
    crossings = 0
    for x in sites:
        verts = cell_vertices(x, n)
        for a in range(4):
            for k in (0, 1):
                coords = {(y[a]-k) % n for y in verts}
                crossings += bool(coords.intersection(range(1, n//2)) and
                                  coords.intersection(range(n//2+1, n)))
    assert crossings == 0
    touched = touched_plaquettes(cell_edges((0,)*4, n), n)
    missing_if_cell_only = len(touched-cell_plaquettes((0,)*4, n))
    assert missing_if_cell_only > 0
    rows = []
    for L, T in ((3, 2), (3, 4), (5, 2)):
        n = L*T
        blocks = list(product(range(T), repeat=4))
        coarse = [(x, a) for x in blocks for a in range(4)]
        def block_vertices(q):
            return {tuple(L*a+b for a, b in zip(q, r))
                    for r in product(range(L), repeat=4)}
        c = ((0,)*4, 0)
        end = block_vertices(c[0]) | block_vertices(shift(c[0], 0, T))
        K = {tuple((y[i]-bit[i]) % n for i in range(4))
             for y in end for bit in product((0, 1), repeat=4)}
        E = {(x, a) for x in end for a in range(4) if shift(x, a, n) in end}
        P = touched_plaquettes(E, n)
        assert len(K) <= 2*(L+1)**4
        assert len(E) <= 8*L**4 and len(P) <= 48*L**4
        reflection_checks=0
        for axis in range(4):
            # Reflection through the centre of block zero preserves blocking.
            reflected_end={tuple((L-1-y[i]) % n if i==axis else y[i] for i in range(4))
                           for y in end}
            K_ref={tuple((y[i]-bit[i]) % n for i in range(4))
                   for y in reflected_end for bit in product((0,1),repeat=4)}
            reflected_cells={tuple((L-2-x[i]) % n if i==axis else x[i] for i in range(4))
                             for x in K}
            assert K_ref==reflected_cells
            reflection_checks+=1
        # All residue positions, plus translated/wrapping boundary samples.
        samples = set(product(range(L), repeat=4)) | set(product((0, L-1, n-1), repeat=4))
        maxdirty = 0
        for x in samples:
            incident = {tuple(z//L for z in y) for y in cell_vertices(x, n)}
            dirty = {(q, a) for q, a in coarse
                     if q in incident or shift(q, a, T) in incident}
            maxdirty = max(maxdirty, len(dirty))
            assert len(dirty) <= 128
        rows.append(dict(L=L, T=T, K_cells=len(K), endpoint_links=len(E),
                         source_plaquettes=len(P), max_single_cell_dirty=maxdirty,
                         K_geometric_reflection_checks=reflection_checks))
    return dict(torus_n=6, checked_cells=6**4, plaquettes=len(incidence),
                cells_per_plaquette=4, reflection_crossings=crossings,
                mutation_single_cell_multiplicity_witness=dict(actual_bad_plaquettes=1,
                    witnessed_bad_cells=len(witness_bad_cells),
                    wrong_lower_bound=wrong_distinct_bad_plaquette_lower_bound),
                mutation_cell_only_source_missing=missing_if_cell_only,
                coarse_geometry=rows)


def su2_reflection():
    n = 6
    sites = list(product(range(n), repeat=4))
    rng = np.random.default_rng(20261029)
    raw = rng.normal(size=(len(sites)*4, 4))
    raw /= np.linalg.norm(raw, axis=1)[:, None]
    def matrix(q):
        a,b,c,d = q
        return np.array([[a+1j*b, c+1j*d], [-c+1j*d, a-1j*b]])
    U = {(x,a):matrix(raw[4*i+a]) for i,x in enumerate(sites) for a in range(4)}
    def reflection(invert):
        out = {}
        for x in sites:
            rx = ((-x[0]) % n,)+x[1:]
            for a in range(4):
                if a == 0:
                    z = U[(shift(rx, 0, n, -1), 0)]
                    out[(x,a)] = z.conj().T if invert else z
                else:
                    out[(x,a)] = U[(rx,a)]
        return out
    def energies(V):
        return {(x,a,b):1-np.trace(V[(x,a)] @ V[(shift(x,a,n),b)] @
                                  V[(shift(x,b,n),a)].conj().T @ V[(x,b)].conj().T).real/2
                for x in sites for a,b in combinations(range(4), 2)}
    base = energies(U)
    reflected = energies(reflection(True))
    mutation = energies(reflection(False))
    delta = abs(sum(base.values())-sum(reflected.values()))
    broken = abs(sum(base.values())-sum(mutation.values()))
    cell_error = 0.
    for x in sites:
        rx = ((-x[0]-1) % n,)+x[1:]
        cell_error = max(cell_error, abs(max(base[p] for p in cell_plaquettes(rx,n))-
                                          max(reflected[p] for p in cell_plaquettes(x,n))))
    assert delta < 1e-9 and cell_error < 1e-12 and broken > 1e-3
    return dict(seed=20261029, fine_links=len(U), action_reflection_error=delta,
                cell_defect_reflection_error=cell_error,
                omitted_normal_inverse_action_change=broken,
                nature="actual noncommuting SU(2) links, numerical symmetry diagnostic")


def z2_penalty():
    nx, ny = 4, 2
    vertices = list(product(range(nx),range(ny)))
    edges = [(x,a) for x in vertices for a in (0,1)]
    idx = {e:i for i,e in enumerate(edges)}
    def step(x,a):
        return ((x[0]+1)%nx,x[1]) if a==0 else (x[0],(x[1]+1)%ny)
    configs = np.arange(1 << len(edges), dtype=np.uint32)
    patterns = np.zeros_like(configs)
    for i,x in enumerate(vertices):
        p_edges = [(x,0),(step(x,0),1),(step(x,1),0),(x,1)]
        parity = np.zeros_like(configs)
        for e in p_edges:
            parity ^= (configs >> idx[e]) & 1
        patterns |= parity << i
    counts = np.bincount(patterns, minlength=1 << len(vertices))
    assert set(int(z) for z in counts) == {0, 512}
    q = F(1,3)
    weights = [F(int(counts[m]), int(counts[0]))*q**m.bit_count() for m in range(256)]
    assert all(w <= q**m.bit_count() for m,w in enumerate(weights))
    holes_checked = 0
    for H in range(256):
        value = sum(w for m,w in enumerate(weights) if m & ~H == 0)
        assert value <= (1+q)**H.bit_count()
        holes_checked += 1
    rows = []
    for t in (F(1),F(1,2),F(1,8),F(1,100)):
        tilted = [w*t**m.bit_count() for m,w in enumerate(weights)]
        total = sum(tilted)
        max_ratio = F(0)
        for A in range(1,256):
            event = sum(w for m,w in enumerate(tilted) if m & A == A)/total
            budget = (q*t)**A.bit_count()
            assert event <= budget
            max_ratio = max(max_ratio,event/budget)
        rows.append(dict(exp_minus_h=str(t), maximal_event_budget_ratio=str(max_ratio)))
    one_mu0 = sum(w for m,w in enumerate(weights) if m&1)/sum(weights)
    assert one_mu0 > q/F(100)
    # SEA-CONTROL-01: explicitly realize the probability-only counterexample.
    # This law is a generic diagnostic, not a Wilson or reflection-positive law.
    single_defect_q = F(1,4)
    singleton_law = {1 << i: F(1,4) for i in range(4)}
    assert sum(singleton_law.values()) == 1
    singleton_moments = []
    for A in range(16):
        moment = sum((w for mask,w in singleton_law.items() if mask & A == A), F(0))
        budget = single_defect_q**A.bit_count()
        assert moment <= budget
        singleton_moments.append(dict(subset=A, moment=str(moment), budget=str(budget)))
    empty_reference = singleton_law.get(0, F(0))
    assert empty_reference == 0
    # Test Z_A <= q^|A| Z_empty directly; never divide by the zero reference.
    failed_reference_patterns = [mask for mask,w in singleton_law.items()
                                 if w > single_defect_q**mask.bit_count()*empty_reference]
    assert set(failed_reference_patterns) == set(singleton_law)
    probability_only_control = bool(failed_reference_patterns) and empty_reference == 0
    return dict(model="2D Z2 Wilson gauge theory on 4x2 torus, Haar link enumeration",
                configurations=len(configs), exact_patterns=256, realized_patterns=int(np.count_nonzero(counts)),
                good_reference_haar_mass=str(F(int(counts[0]),len(configs))), sharp_q=str(q),
                holes_checked=holes_checked, tilted_checks=rows,
                mutation_omitted_penalty_detected=True,
                mutation_probability_only_reference_detected=probability_only_control,
                probability_only_counterexample=dict(
                    scope="generic probability law, not the Wilson tilted family",
                    law={str(mask):str(w) for mask,w in singleton_law.items()},
                    all_subset_moments=singleton_moments,
                    empty_reference_mass=str(empty_reference),
                    failed_reference_inequality_patterns=failed_reference_patterns,
                    zero_reference_division_used=False),
                infinite_penalty_limit="exact coefficient: every pattern outside A removed; constant term is the same good reference")


class Q:
    """Tiny exact Gaussian-rational field for source identity diagnostics."""
    def __init__(self, r=0, i=0):
        if isinstance(r,Q): self.r,self.i=r.r,r.i
        else: self.r,self.i=F(r),F(i)
    def __add__(self,z):
        z=Q(z); return Q(self.r+z.r,self.i+z.i)
    __radd__=__add__
    def __neg__(self): return Q(-self.r,-self.i)
    def __sub__(self,z): return self+-Q(z)
    def __mul__(self,z):
        z=Q(z); return Q(self.r*z.r-self.i*z.i,self.r*z.i+self.i*z.r)
    __rmul__=__mul__
    def __truediv__(self,z):
        z=Q(z); d=z.r*z.r+z.i*z.i
        return self*Q(z.r/d,-z.i/d)
    def __eq__(self,z):
        z=Q(z); return self.r==z.r and self.i==z.i
    def norm(self): return math.hypot(float(self.r),float(self.i))
    def serial(self): return dict(real=str(self.r),imag=str(self.i))


def replacement_fixture():
    states = list(product((0,1),repeat=2))
    def K(i,x,e,v,normalized=True):
        def raw(z): return F(1+(i+1)*(x+1)+(e+1)*(z+1)+2*x*z)
        return 2*raw(v)/(raw(0)+raw(1)) if normalized else raw(v)
    def local(i,x,e,v,norm=True): return F(2+x+2*e+i)*K(i,x,e,v,norm)
    def S(i,x,e): return Q(1+F((i+1)*(x+1),11),F(1+x+2*e,13+i))
    def Sext(e): return Q(1+F(e,7),F(e+1,17))
    def fail(x,e,V):
        return sum((1<<i) for i in range(2) if x[i] and (e+V[i]+i)%2)
    def refine(x,e,V):
        A=sum(x[i]<<i for i in range(2))
        C=sum(1<<i for i in range(2) if not x[i] and V[i]!=e)
        return A,C
    def insertion(x,e,V): return F(1 if (x[0]^x[1])==e else 0)
    def matches(x,e,V,select):
        return select is None or (refine(x,e,V)+(fail(x,e,V),))==select
    zcutV = {V:sum(F(2+e)*local(0,0,e,V[0])*local(1,0,e,V[1])/8
                  for e in (0,1)) for V in states}
    zcut = sum(zcutV.values())/4
    def direct(select=None, normalized=True):
        out=Q()
        for e,V,x in product((0,1),states,states):
            if not matches(x,e,V,select): continue
            w=F(2+e)*local(0,x[0],e,V[0],normalized)*local(1,x[1],e,V[1],normalized)/32
            out+=w*Sext(e)*S(0,x[0],e)*S(1,x[1],e)*insertion(x,e,V)
        return out/zcut
    def replacement(select=None,mutation=None):
        total=Q()
        for V in states:
            val=Q()
            for e in (0,1):
                base=F(2+e)*local(0,0,e,V[0])*local(1,0,e,V[1])/8
                source=S(0,0,e)*S(1,0,e)*(1 if mutation=='outside_source' else Sext(e))
                ret=Q()
                for x in states:
                    if mutation=='drop_failures' and fail(x,e,V): continue
                    z=Q(1)
                    for i in range(2):
                        if x[i]:
                            den=Q(local(i,0,e,V[i]))
                            if mutation!='source_compensation': den*=S(i,0,e)
                            z*=Q(local(i,1,e,V[i]))*S(i,1,e)/den
                    eval_x=(0,0) if mutation=='unreplaced_insertion' else x
                    if matches(eval_x,e,V,select): ret+=z*insertion(eval_x,e,V)
                val+=base*source*ret
            weight=F(1,4)/zcutV[V] if mutation=='uniform_coarse_weight' else F(1,4)/zcut
            total+=weight*val
        return total
    for i,x,e in product(range(2),(0,1),(0,1)):
        assert sum(K(i,x,e,v) for v in (0,1))/2==1
    assert direct()==replacement()
    nonzero=0
    for A,C,H in product(range(4),repeat=3):
        sel=(A,C,H)
        left,right=direct(sel),replacement(sel)
        assert left==right
        nonzero+=left!=Q()
    mutations={}
    for name in ('uniform_coarse_weight','source_compensation','drop_failures',
                 'unreplaced_insertion','outside_source'):
        error=(replacement(mutation=name)-direct()).norm()
        assert error>1e-8, name
        mutations[name]=error
    error=(direct(normalized=False)-direct()).norm()
    assert error>1e-8
    mutations['omitted_kernel_normalizer']=error
    return dict(model="finite rational fixture; two returned interiors, shared exterior, two normalized soft coordinates",
                arithmetic="exact Gaussian rational", refined_identities_checked=64,
                nonzero_refined_identities=nonzero, integrated_reference=str(zcut),
                normalized_inserted_weight=direct().serial(), mutations_detected=mutations)


def su2_normalizer():
    mp.mp.dps=65
    eta=mp.mpf(1)
    theta0=2*mp.asin(eta/2)
    cH=mp.mpf('0.01')
    # sin(theta)>=2theta/pi on [0,pi/2], theta(r)>=r, r<=1.
    assert cH<8/(3*mp.pi**3)
    rows=[]
    for t in (20,80,400):
        for r in (mp.mpf(1),mp.cos(mp.mpf('.01')),mp.mpf(-1)):
            f=lambda theta: 2/mp.pi*mp.sin(theta)**2*mp.exp(-t*(1-r*mp.cos(theta)))
            intervals=[0,mp.mpf('.05'),mp.mpf('.2'),1,2,mp.pi-mp.mpf('.2'),mp.pi-mp.mpf('.05'),mp.pi]
            integral=mp.quad(f,intervals)
            exact=mp.exp(-t)*2*mp.besseli(1,t*r)/(t*r)
            mass=integral/exact
            assert abs(mass-1)<mp.mpf('1e-40')
            tail=mp.quad(f,[theta0,2,mp.pi-mp.mpf('.2'),mp.pi-mp.mpf('.05'),mp.pi])/exact
            clean_budget=mp.e/cH*t**3*mp.exp(-t/8)
            if r>0:
                assert tail<=min(1,clean_budget)*(1+mp.mpf('1e-40'))
            rows.append(dict(t=t,r=mp.nstr(r,18),normalized_mass_error=mp.nstr(abs(mass-1),8),
                             raw_kernel_mass=mp.nstr(exact,12),eta_one_tail=mp.nstr(tail,12),
                             clean_tail_budget=mp.nstr(clean_budget,12)))
            if t==400 and r==-1:
                assert tail>mp.mpf('.99') and clean_budget<mp.mpf('1e-10')
    return dict(group="SU(2)", haar_radial_density="2 sin(theta)^2 / pi", decimal_digits=65,
                eta=1, rows=rows, mutation_dropped_normalizer_detected=True,
                mutation_rough_mean_priced_as_clean_detected=True,
                rough_mean_scope="M=-I is a unitary mean; no global S4-contour realization inferred")


def scaling_and_sources():
    rows=[]
    for L,N in product((3,5),(2,3)):
        eps1,epsloc=1e-6,1e-5
        eta=min(1,epsloc/2)
        AL=3*L*(L-1)/2
        delta=min(eps1,epsloc/2,eta**2/(8*N*AL))
        a=delta**2/(8*N); b=.5*eta**2/(4*N)
        nA=192+6144*L**4; nC=48*L**4
        nP=6*4*L**3*(L-1)
        rho0=eps1**2/(32*N*nP)
        rho=min(rho0,a/(4*nA),b/(4*nC))
        assert rho>0 and rho<=rho0
        assert a-2*rho*nA>=a/2*(1-1e-14)
        assert b-2*rho*nC>=b/2*(1-1e-14)
        slope=11*N*N/(12*math.pi**2)
        max_product=11*N/(96*math.pi**2)
        assert max_product<4
        rows.append(dict(L=L,N=N,diagnostic_epsilon1=eps1,diagnostic_epsilonloc=epsloc,
                         delta=delta,eta=eta,nA=nA,nC=nC,rho0=rho0,rho_sea=rho,
                         a_delta=a,b_eta=b,remaining_fine_rate=a-2*rho*nA,
                         remaining_soft_rate=b-2*rho*nC,proposed_Wilson_u_slope=slope,
                         maximum_a_times_slope_for_delta_le_1=max_product,
                         minimum_volume_growth_exponent=4-max_product,
                         union_window_contains_fixed_physical_volume_limit=False))
    return dict(rows=rows, flow_status="conditional arithmetic, not a running-coupling theorem",
                thresholds_status="diagnostic values; general formulas cover smaller lane thresholds")


def main():
    report=dict(scope="author diagnostics only; independent review and continuum results not supplied",
                python=sys.version,platform=platform.platform(),numpy=np.__version__,mpmath=mp.__version__)
    for name,fn in [('geometry',geometry),('su2_reflection',su2_reflection),
                    ('z2_penalty',z2_penalty),('replacement_fixture',replacement_fixture),
                    ('su2_normalizer',su2_normalizer),('scaling_and_sources',scaling_and_sources)]:
        try:
            report[name]=dict(status='PASS',result=fn())
        except Exception as error:
            report[name]=dict(status='FAIL',error=repr(error),traceback=traceback.format_exc())
    report['status']='PASS' if all(v.get('status')!='FAIL' for v in report.values() if isinstance(v,dict)) else 'FAIL'
    print(json.dumps(report,indent=2,sort_keys=True))
    return 0 if report['status']=='PASS' else 1


if __name__=='__main__':
    raise SystemExit(main())
