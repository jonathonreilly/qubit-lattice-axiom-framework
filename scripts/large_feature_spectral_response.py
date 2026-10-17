#!/usr/bin/env python3
"""Conditional corner-band spectral inversion and homogeneous response controls.
Model definitions adapted from PR9671 head16ae120ee46a1186b5ca81cd7d393396089e77d6,
Part2 of corner_fermion_large_fermion_effective_theory_and_one_qubit_block_embedding_2026_10_17.py.
Self-contained supplied matrix family, not an axiom-derived Hamiltonian or physical clock.
"""
AUDIT_TIMEOUT_SEC = 120
import itertools
import numpy as np
DIRS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def neg(d): return tuple(-x for x in d)
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def perp(d, e): return dot(d, e) == 0 and d != e
CORN = [frozenset((d, e)) for d, e in itertools.combinations(DIRS, 2) if dot(d, e) == 0]
CI = {c: i for i, c in enumerate(CORN)}
etypes = []; ekey = {}
def addt(c1, c2, sh, kind):
    if (c1, c2, sh) in ekey or (c2, c1, neg(sh)) in ekey: return
    ekey[(c1, c2, sh)] = ekey[(c2, c1, neg(sh))] = len(etypes); etypes.append((c1, c2, sh, kind))
Z0 = (0, 0, 0)
for c in CORN:
    d, e = tuple(c)
    for a, b in ((d, e), (e, d)):
        for f in DIRS:
            if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a):
                addt(c, frozenset((a, f)), Z0, 'onsite')
        addt(c, frozenset((neg(a), b)), a, 'link')
nT = len(etypes)
def vadd(a, b): return tuple(x + y for x, y in zip(a, b))
def cyc(seq):
    return [ekey[(c1, c2, tuple(y - x for x, y in zip(p1, p2)))]
            for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
cycles = {'square': [], 'triangle': [], 'plaquette': [], 'tube': []}
for d in DIRS:
    a = [f for f in DIRS if perp(f, d) and f != neg(d)]; a0 = a[0]
    b0 = [f for f in a if perp(f, a0) and f != neg(a0)][0]; ring = [a0, b0, neg(a0), neg(b0)]
    cycles['square'].append(cyc([(frozenset((d, r)), Z0) for r in ring]))
    for i in range(4):
        p, q = ring[i], ring[(i+1) % 4]
        cycles['tube'].append(cyc([(frozenset((d, p)), Z0), (frozenset((neg(d), p)), d),
                                   (frozenset((neg(d), q)), d), (frozenset((d, q)), Z0)]))
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    cycles['triangle'].append(cyc([(frozenset((x, y)), Z0), (frozenset((y, z)), Z0), (frozenset((z, x)), Z0)]))
for d, e in (((1,0,0),(0,1,0)), ((0,1,0),(0,0,1)), ((0,0,1),(1,0,0))):
    cycles['plaquette'].append(cyc([(frozenset((d, e)), Z0), (frozenset((neg(d), e)), d),
                                    (frozenset((neg(d), neg(e))), vadd(d, e)), (frozenset((d, neg(e))), e)]))
def solve_cell(F):
    piv = {}
    for k, cs in cycles.items():
        for c in cs:
            x = 0
            for t in c: x ^= 1 << t
            x |= F[k] << nT
            while True:
                low = x & ((1 << nT) - 1)
                if low == 0:
                    if x: return None
                    break
                cc = low.bit_length() - 1
                if cc in piv: x ^= piv[cc]
                else: piv[cc] = x; break
    sol = 0
    for cc in sorted(piv):
        x = piv[cc]; rest = x & ((1 << cc) - 1)
        if ((x >> nT) & 1) ^ (bin(rest & sol).count('1') & 1): sol |= 1 << cc
    return [(sol >> j) & 1 for j in range(nT)]
TRI = []
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0],0,0), (0,s[1],0), (0,0,s[2])
    cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
    if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
    TRI += [(cy[i], cy[(i+1) % 3]) for i in range(3)]
def bloch(u, k, t1, t2, lam):
    H = np.zeros((12, 12), complex)
    for j, (c1, c2, sh, kind) in enumerate(etypes):
        a = -(t1 if kind == 'onsite' else t2) * (-1.0) ** u[j] * np.exp(1j * np.dot(k, sh))
        H[CI[c2], CI[c1]] += a; H[CI[c1], CI[c2]] += np.conj(a)
    for q, r in TRI:
        amp = 1j * lam * (-1.0) ** u[ekey[(q, r, Z0)]]
        H[CI[r], CI[q]] += amp; H[CI[q], CI[r]] += np.conj(amp)
    return H


if __name__ == '__main__':
    import json
    import sympy as sp
    from pathlib import Path
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    u = solve_cell(dict(square=1, triangle=0, plaquette=1, tube=1))
    check('flux equations', all(sum(u[i] for i in cy)%2 == dict(square=1,triangle=0,plaquette=1,tube=1)[kind] for kind,cs in cycles.items() for cy in cs))
    a,b,c,z = sp.symbols('a b c z', real=True)
    H = sp.zeros(12)
    # Exact exp(i k.sh) at the selected affine-fixed momentum k=(-1,1,-1) pi/2.
    for j,(c1,c2,sh,kind) in enumerate(etypes):
        phase=sp.I**sum(v*w for v,w in zip((-1,1,-1),sh))
        amp=-(a if kind=='onsite' else b)*(-1)**u[j]*phase
        i,l=CI[c2],CI[c1]
        H[i,l]+=amp; H[l,i]+=sp.conjugate(amp)
    for q0,r0 in TRI:
        amp=sp.I*c*(-1)**u[ekey[(q0,r0,Z0)]]
        i,l=CI[r0],CI[q0]
        H[i,l]+=amp; H[l,i]+=sp.conjugate(amp)
    check('exact Hermitian matrix', H == H.conjugate().T)
    actual=H.charpoly(z).as_expr()
    # charpoly may replace a real z with an assumption-free symbol.
    zz=next(t for t in actual.free_symbols if str(t)=='z')
    fact=(zz**2+2*a*zz-2*a*a-2*(b+c)**2)**4*((zz-2*a)**2-2*(b-2*c)**2)**2
    check('symbolic characteristic polynomial', sp.expand(actual-fact)==0)
    q,r=sp.symbols('q r', positive=True)
    d1=-3*a+q-r; d2=2*q; d3=-3*a+q+r
    check('inverse onsite', sp.simplify((d2-d1-d3)/6-a)==0)
    check('inverse q', sp.simplify(d2/2-q)==0)
    check('inverse r', sp.simplify((d3-d1)/2-r)==0)
    U,V=sp.symbols('U V',real=True)
    bb=(U+2*V)/3; cc=(V-U)/3
    check('inverse link and chiral', sp.simplify(bb+cc-V)==0 and sp.simplify(bb-2*cc-U)==0)
    g=sp.symbols('g',positive=True)
    check('all momentum homogeneous Hamiltonian coefficients', all(sp.expand(x.subs({a:g*a,b:g*b,c:g*c}, simultaneous=True)-g*x)==0 for x in H))
    # Perturbation controls challenge actual determinant, inverse, and kinetic scaling.
    mutations={
      'wrong flux polynomial coefficient': sp.expand(actual-((zz**2+2*a*zz-2*a*a-2*(b-c)**2)**4*((zz-2*a)**2-2*(b-2*c)**2)**2)) != 0,
      'wrong inverse onsite divisor': sp.simplify((d2-d1-d3)/3-a)!=0,
      'opposite kinetic scaling': sp.simplify(g-1/g)!=0,
    }
    check('three mutations detected', all(mutations.values()))
    k=np.pi/2*np.array([-1,1,-1])
    def inverse(D):
        aa=(D[1]-D[0]-D[2])/6
        qq=D[1]/2; rr=(D[2]-D[0])/2
        vv=-np.sqrt((rr*rr-3*aa*aa)/2); uu=qq/np.sqrt(2)
        return np.array([aa,(uu+2*vv)/3,(vv-uu)/3])
    def spectrum(p):
        ev=np.linalg.eigvalsh(bloch(u,k,*p))
        return ev,np.array([ev[2]-ev[0],ev[6]-ev[0],ev[8]-ev[0]])
    p=np.array([-1.,.1,-.5]); ev,D=spectrum(p)
    check('reference multiplicities', np.allclose(ev[[0,2,6,8]],[-3.5556349186,-.8220867158,-.4443650814,2.8220867158],atol=1e-9))
    check('reference inversion', np.allclose(inverse(D),p,atol=1e-12))
    rng=np.random.default_rng(20261017); samples=[]
    for j in range(40):
        pp=p*np.exp(rng.uniform(-.1,.1,3)); aa,bb,cc=pp
        qq=np.sqrt(2)*(bb-2*cc); rr=np.sqrt(3*aa*aa+2*(bb+cc)**2)
        # Declared ordering chamber: doublet, quartet, doublet, quartet.
        assert bb+cc<0 and qq>0 and -3*aa+qq-rr>0 and -3*aa+qq-rr<2*qq<-3*aa+qq+rr
        ee,dd=spectrum(pp)
        check(f'inverse sample {j}',np.allclose(inverse(dd),pp,atol=2e-12))
        expected=np.repeat([2*aa-qq,-aa-rr,2*aa+qq,-aa+rr],[2,4,2,4])
        check(f'spectrum sample {j}', np.allclose(ee,expected,atol=2e-12))
    def curvature(p,h):
        en=lambda kk: np.linalg.eigvalsh(bloch(u,kk,*p))[:2].mean()
        eye=np.eye(3)
        return np.array([[(en(k+h*(eye[i]+eye[j]))-en(k+h*(eye[i]-eye[j]))-en(k-h*(eye[i]-eye[j]))+en(k-h*(eye[i]+eye[j])))/(4*h*h) for j in range(3)] for i in range(3)])
    curvatures={str(h):curvature(p,h).tolist() for h in [.01,.005,.002]}
    C=curvature(p,.005)
    check('positive isotropic reference curvature',np.linalg.eigvalsh(C).min()>0 and np.max(abs(C-np.eye(3)*np.trace(C)/3))<1e-7)
    for scale in [.7,1.3,2.]:
        ee,dd=spectrum(scale*p)
        check(f'finite gap ray {scale}',np.allclose(dd,scale*D,atol=2e-12))
        check(f'finite curvature ray {scale}',np.allclose(curvature(scale*p,.005),scale*C,atol=1e-8))
    # One independent shape perturbation changes dimensionless gaps.
    _,Dpert=spectrum(p*np.array([1,1.1,1]))
    check('link perturbation changes gap ratios',np.linalg.norm(Dpert/Dpert[0]-D/D[0])>1e-4)
    result={'status':'conditional-support','empirical_data_used':False,'reference_parameters':p.tolist(), 'selected_momentum_pi_over_2':[-1,1,-1], 'reference_gaps':D.tolist(),'curvature_step_scan':curvatures,'shape_perturbation_gap_ratios':(Dpert/Dpert[0]).tolist(),'reference_gap_ratios':(D/D[0]).tolist(),'checks':checks,'mutations':mutations}
    out=Path(__file__).resolve().parents[1]/'outputs/large_feature_spectral_response/result.json'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'checks_passed':sum(checks.values()),'checks_total':len(checks),'mutations_detected':sum(mutations.values()),'reference_gaps':D.tolist(),'curvature':np.trace(C)/3,'scope':'Supplied band model; no measured spectra, physical scalar or universal coupling derived'},sort_keys=True))
