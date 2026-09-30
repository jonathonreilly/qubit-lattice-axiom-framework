#!/usr/bin/env python3
"""Literal S* S / original B* reconstruction with a distinct Gram-path check.

Coordinates are unfolded Z^3. The Gram implementation shares no hop functions.
No external scientific data are read. Imported package-local Gram source and
source-note bytes are declared cache inputs; output coefficients are computed.
All matter factors commute at distinct sites, as required by the supplied law.
"""
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "scripts/original_first_birth_energy_gram_2026_09_29.py",
    "docs/ORIGINAL_FIRST_BIRTH_SYSTEM_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-29.md",
    "docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib, json, os, time

ROOT = (0, 0, 0)
EDGE_B = (1, 0, 0)
DIRS = tuple(tuple(s if i == j else 0 for i in range(3))
             for j in range(3) for s in (-1, 1))
OUT = Path(__file__).resolve().parents[1] / "outputs" / "original-first-birth-energy-2026-09-29"
import original_first_birth_energy_gram_2026_09_29 as gram

def add(x, y): return tuple(a+b for a,b in zip(x,y))
def adjacent(x): return tuple(add(x,d) for d in DIRS)
def parity(x): return sum(x) % 2
def neighbors2(x):
    return {z for y in adjacent(x) for z in adjacent(y)} - {x}

# Matter deviations from q_A=+1,q_B=0; all entries are literal charges.
VAC = ()
def charge(m, x): return dict(m).get(x, 0 if parity(x) else 1)
def change(m, updates):
    q = dict(m)
    for x,v in updates:
        if v == (0 if parity(x) else 1): q.pop(x, None)
        else: q[x] = v
    return tuple(sorted(q.items()))

# Edge coordinate is always (A,B); electric word shifts E by its coefficient.
def shift(w, a, b, v):
    f = dict(w); e = (a,b); f[e] = f.get(e,0)+v
    if not f[e]: del f[e]
    return tuple(sorted(f.items()))

def outward(m, w, a):
    q = charge(m,a)
    if not q: return
    for b in adjacent(a):
        if charge(m,b) == 0:
            yield change(m, ((a,0),(b,q))), shift(w,a,b,-q)

def inward(m, w, a):
    if charge(m,a): return
    for b in adjacent(a):
        q = charge(m,b)
        if q:
            yield change(m, ((a,q),(b,0))), shift(w,a,b,q)

def pair_operator(m, w, a, c):
    # F_a then F_c then F_c* then F_a*: S_ac* S_ac, not a norm Gram.
    for m1,w1 in outward(m,w,a):
        for m2,w2 in outward(m1,w1,c):
            for m3,w3 in inward(m2,w2,c):
                yield from inward(m3,w3,a)

FOOT = tuple(d for d in adjacent(ROOT) if d != EDGE_B)
FIRST = []
for sigma in (-1,1):
    for d in FOOT:
        m = change(VAC, ((ROOT,sigma),(EDGE_B,-sigma),(d,1)))
        w = shift(shift((),ROOT,d,-1),ROOT,EDGE_B,sigma)
        FIRST.append((sigma,d,m,w))

def inverse_original_mark(m,w):
    # j_sigma* first removes the actual created pair; F_0* then restores
    # its old + particle. Keep the returned foot label for interference.
    sigma = charge(m,ROOT)
    if sigma not in (-1,1) or charge(m,EDGE_B) != -sigma: return
    m1 = change(m, ((ROOT,0),(EDGE_B,0)))
    w1 = shift(w,ROOT,EDGE_B,-sigma)
    for d in FOOT:
        if charge(m1,d) != 1: continue
        m2 = change(m1, ((ROOT,1),(d,0)))
        if m2 == VAC:
            yield ((0 if sigma == -1 else 5)+FOOT.index(d),
                   shift(w1,ROOT,d,1))

def gauss(m,w):
    div = Counter()
    for (a,b),v in w: div[a]+=v; div[b]-=v
    desired = {x:q-(0 if parity(x) else 1) for x,q in m}
    return {x:v for x,v in div.items() if v} == desired

def canonical(poly):
    return [[[[list(a),list(b),v] for (a,b),v in w], str(c)]
            for w,c in sorted(poly.items()) if c]

def compute_pairs(pairs):
    pre=Counter(); blocks={ij:Counter() for ij in product((-1,1),repeat=2)}
    constant_matrix=[[0]*10 for _ in range(10)]
    per_pair_nonzero=0
    full_paths=0
    for a,c in sorted(pairs):
        pre_pair=Counter()
        for m,w in pair_operator(VAC,(),a,c):
            assert m==VAC
            pre_pair[w]+=1
        pre.update(pre_pair)
        pb={ij:Counter() for ij in blocks}
        for j,(sj,d,m,w) in enumerate(FIRST):
            for mm,ww in pair_operator(m,w,a,c):
                full_paths+=1
                for i,z in inverse_original_mark(mm,ww):
                    si=FIRST[i][0]
                    pb[si,sj][z]+=1
                    if not z: constant_matrix[i][j] += -2
        for i in range(10): constant_matrix[i][i] += 2*pre_pair[()]
        for ij in blocks: blocks[ij].update(pb[ij])
        residual=False
        for s in (-1,1):
            keys=set(pb[s,s]) | set(pre_pair)
            residual |= any(pb[s,s][k] != 5*pre_pair[k] for k in keys)
        residual |= bool(pb[-1,1] or pb[1,-1])
        per_pair_nonzero+=int(residual)
    polynomials={}
    for s in (-1,1):
        polynomials[str(s)]={w:Fraction(-2,5)*(blocks[s,s][w]-5*pre[w])
                            for w in set(blocks[s,s])|set(pre)}
    polynomials['coherent']={w:Fraction(-1,5)*(
        sum(blocks[ij][w] for ij in blocks)-10*pre[w])
        for w in set(pre).union(*(set(b) for b in blocks.values()))}
    polynomials={k:{w:v for w,v in p.items() if v} for k,p in polynomials.items()}
    for ij in ((-1,1),(1,-1)):
        assert not blocks[ij], ('cross-sign nonzero',ij)
    return polynomials,constant_matrix,{'pairs':len(pairs),
        'pairs_with_nonzero_increment':per_pair_nonzero,'full_return_paths':full_paths,
        'cross_sign_words':0}

def electric(m, w):
    # q_B=0 is the exact occupied-B mask; missing E entries vanish.
    return sum(v*(v-charge(m,a)) for (a,b),v in w if charge(m,b)==0)

def electric_checks():
    # Deterministic integer combinations of elementary plaquette cycles,
    # with nonzero fields at every relevant edge. Exact finite stencil test.
    plaquettes=[]
    for x in product(range(-2,3),repeat=3):
        for i in range(3):
            for j in range(i+1,3):
                di=tuple(int(k==i) for k in range(3));dj=tuple(int(k==j) for k in range(3))
                vs=(x,add(x,di),add(add(x,di),dj),add(x,dj),x)
                w=()
                for u,v in zip(vs,vs[1:]):
                    a,b,sg=(u,v,1) if parity(u)==0 else (v,u,-1)
                    w=shift(w,a,b,sg)
                plaquettes.append(w)
    for trial in range(31):
        fields=Counter()
        for k,p in enumerate(plaquettes):
            n=((k*17+trial*23+trial*k*k)%7)-3
            for e,v in p: fields[e]+=n*v
        E=tuple(sorted((e,v) for e,v in fields.items() if v))
        assert gauss(VAC,E)
        for sigma,d,m,w in FIRST:
            post=E
            for (a,b),v in w: post=shift(post,a,b,v)
            assert gauss(m,post)
            direct=electric(m,post)-electric(VAC,E)
            predicted=-sum(fields[c,x]**2 for x in (EDGE_B,d) for c in adjacent(x))
            if sigma==-1: predicted-=2*(fields[ROOT,EDGE_B]+fields[ROOT,d])
            assert direct==predicted,(trial,sigma,d,direct,predicted)
    return {'integer_circulation_inputs':31,'resolved_branches_per_input':10,
            'independent_plaquettes_in_each_input':len(plaquettes)}


def prebirth_geometry():
    counts=Counter(); diagonal=0; directed_loops=0
    for c in neighbors2(ROOT):
        shared=len(set(adjacent(ROOT))&set(adjacent(c))); poly=Counter()
        for m,w in pair_operator(VAC,(),ROOT,c):
            assert m==VAC and gauss(m,w)
            poly[w]+=1
        assert poly[()]==36-shared
        nonzero={w:n for w,n in poly.items() if w}
        assert len(nonzero)==shared*(shared-1)
        assert all(n==1 and len(w)==4 and all(abs(v)==1 for e,v in w) for w,n in nonzero.items())
        assert all(nonzero[tuple((e,-v) for e,v in w)]==n for w,n in nonzero.items())
        counts[shared]+=1;diagonal+=poly[()];directed_loops+=len(nonzero)
    assert dict(counts)=={1:6,2:12} and diagonal==618
    # Root-pair incidence counts each unordered pair twice; each geometric
    # plaquette contributes its two orientations once after that division.
    plaquettes=directed_loops//4
    assert plaquettes==6
    return {'partners_by_shared_B':dict(counts),'scalar_magnitude_per_A':diagonal,
            'plaquettes_per_A':plaquettes,'norm_V_bound_per_A':4*plaquettes}


def main():
    for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
        os.environ[name]='1'
    OUT.mkdir(parents=True,exist_ok=True)
    assert len(FIRST)==10 and all(gauss(m,w) for s,d,m,w in FIRST)
    electric=electric_checks();geometry=prebirth_geometry()
    active={ROOT}|neighbors2(ROOT)
    pairs={tuple(sorted((a,c))) for a in active for c in neighbors2(a)}
    assert len(active)==19 and len(pairs)==264
    polynomials,matrix,stats=compute_pairs(pairs)
    shell_centers={a for x in active for a in neighbors2(x)}-active
    shell_pairs={tuple(sorted((a,c))) for a in shell_centers for c in neighbors2(a)}-pairs
    shell,sm,ss=compute_pairs(shell_pairs)
    assert all(not p for p in shell.values()) and all(not v for row in sm for v in row)
    assert ss['pairs_with_nonzero_increment']==0
    # The two formulations compute every word independently, not just a norm.
    compared=0;normalizations={}
    for key,sigmas in [('-1',(-1,)),('1',(1,)),('coherent',(-1,1))]:
        vec=gram.birth(gram.ORIGIN,(1,0,0),sigmas)
        alternative=gram.work_laurent(vec)
        assert alternative==polynomials[key], ('literal/Gram mismatch',key)
        normalizations[key]=gram.norm2(vec);compared+=len(alternative)
    assert normalizations=={'-1':5,'1':5,'coherent':10}
    electric_cost=2*geometry['norm_V_bound_per_A']
    summary={}
    for name,p in polynomials.items():
        for w,c in p.items():
            assert p.get(tuple((e,-v) for e,v in w))==c and gauss(VAC,w)
        constant=p.get((),0);off=sum(abs(v) for w,v in p.items() if w)
        vertices=[x for w in p for (a,b),v in w for x in (a,b)]
        assert min(min(x) for x in vertices)>=-2 and max(max(x) for x in vertices)<=2
        assert constant-off-electric_cost>0
        summary[name]={'constant':str(constant),'off_constant_l1':str(off),
          'magnetic_lower':str(constant-off),'full_energy_lower_over_delta':str(constant-off-electric_cost),
          'nonconstant_words':len(p)-1}
    for w in set().union(*(set(p) for p in polynomials.values())):
        assert polynomials['coherent'].get(w,0)==(polynomials['-1'].get(w,0)+polynomials['1'].get(w,0))/2
    rate_per_A=len(DIRS)*normalizations['coherent']
    assert rate_per_A==len(DIRS)*(normalizations['-1']+normalizations['1'])
    power_lower=rate_per_A*Fraction(summary['coherent']['full_energy_lower_over_delta'])
    power_initial=rate_per_A*Fraction(summary['coherent']['constant'])
    # These published constants are checked against two independent algorithms.
    assert summary['-1']['constant']=='12172/5' and summary['1']['constant']=='8452/5'
    assert summary['coherent']['constant']=='10312/5'
    assert power_lower==75648 and power_initial==123744
    result={'claim':'finite-torus original first-wait system-energy bounds',
        'parameters':'even L>=24; K,delta,kappa>0; supplied full rotor law and Omega',
        'normalizations':normalizations,'geometry':geometry,'electric_branch_checks':electric,
        'pair_paths':stats,'remote_cancellation':ss,'independently_compared_coefficients':compared,
        'summary':summary,'rate_per_A_over_kappa':rate_per_A,
        'power_lower_over_kappa_delta_N':str(power_lower),
        'initial_power_over_kappa_delta_N':str(power_initial),
        'scope':'first-wait common-law system energy; no microscopic-energy or reservoir identification'}
    (OUT/'coefficients.json').write_text(json.dumps({k:canonical(v) for k,v in polynomials.items()},separators=(',',':'))+'\n')
    (OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    (OUT/'first_matrix.json').write_text(json.dumps(matrix,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('TOTAL: PASS=8 FAIL=0; exact marked normalization, magnetic words, coherent cross terms, electric compression, prebirth geometry, remote cancellation, independent reconstruction, and bound arithmetic.')

if __name__=='__main__':main()
