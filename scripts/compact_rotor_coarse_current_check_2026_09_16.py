#!/usr/bin/env python3
"""Exact integer cochain and independent orientation-count challenges.

Arbitrary compact fields challenge dF/(2pi) integrality and dJ=0; they
are not samples from the quantum ground law. Parameter bounds are
evaluated with 80-digit arithmetic. No simulated phase is inferred.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_MEMORY_MB = 512
AUDIT_INPUT_PATHS = ['docs/COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/COMPACT_ROTOR_TEMPORAL_OSCILLATION_COARSE_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-16.md']
EXPECTED_INPUT_SHA256 = {'docs/COMPACT_ROTOR_SAMPLED_MAGNETIC_EVENT_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'aa61782c652fb722b65832dceed9b309e63a8bdae67cb6045830a2a974eb8ccc', 'docs/COMPACT_ROTOR_MAGNETIC_EXCURSION_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'c68e64839af884757499eb5223a479f7ad32aba3f339198fc2e2b5845816db7e', 'docs/COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md': '679709b4e68b94805eaa3b9fbdc6d16a3a033e15c8e9c22d798f7d796c2255c0', 'docs/COMPACT_ROTOR_TEMPORAL_OSCILLATION_COARSE_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-16.md': '0bec7eaaf856d6e48314e15c13468e98b6d5af3d90f52626c853cd5327d52416'}

# Numerical fixtures remain defined below. Declared proof inputs and this
# source are hash-bound; JSON diagnostics alone are not audit verdicts.

from collections import Counter
from itertools import combinations,product
from pathlib import Path
import hashlib
import json
import random
import time

import mpmath as mp


def shift(x,i,L):
    y=list(x);y[i]=(y[i]+1)%L
    return tuple(y)


def coboundary(form,degree,L,dimension=4):
    ans={}
    for x in product(range(L),repeat=dimension):
        for axes in combinations(range(dimension),degree+1):
            ans[x,axes]=sum((-1)**r*(form[shift(x,i,L),axes[:r]+axes[r+1:]]
                                     -form[x,axes[:r]+axes[r+1:]])
                             for r,i in enumerate(axes))
    return ans


def integer_currents():
    L,Q=4,12
    rng=random.Random(20260916)
    vertices=list(product(range(L),repeat=4))
    rows=[]
    last_J=None
    for trial in range(5):
        # Direction3 is time in this checker; time links have value0.
        # Note's labels0,1,2,3 differ by a coordinate permutation only.
        a={(x,(i,)):rng.randrange(-Q//2,Q//2) if i<3 else 0
           for x in vertices for i in range(4)}
        raw=coboundary(a,1,L)
        F={p:(v+Q//2)%Q-Q//2 for p,v in raw.items()}
        m={p:(raw[p]-F[p])//Q for p in F}
        assert all(raw[p]-F[p]==Q*m[p] for p in F)
        dF=coboundary(F,2,L)
        dm=coboundary(m,2,L)
        assert all(v%Q==0 for v in dF.values())
        J={c:v//Q for c,v in dF.items()}
        assert all(J[c]==-dm[c] for c in J)
        assert set(coboundary(J,3,L).values())=={0}
        # Independent dual vertex divergence via shifted primal3-cells.
        dual={(x,i):(-1)**i*J[shift(x,i,L),tuple(j for j in range(4) if j!=i)]
              for x in vertices for i in range(4)}
        divergence=[]
        for x in vertices:
            z=0
            for i in range(4):
                previous=list(x);previous[i]=(previous[i]-1)%L
                z+=dual[x,i]-dual[tuple(previous),i]
            divergence.append(z)
        assert set(divergence)=={0}
        witness_count=[]
        for (x,axes),j in J.items():
            if not j:continue
            faces=[]
            for r,i in enumerate(axes):
                rest=axes[:r]+axes[r+1:]
                faces += [(x,rest),(shift(x,i,L),rest)]
            witnesses=sum(abs(F[p])>=Q/6 for p in faces)
            assert witnesses>=1
            witness_count.append(witnesses)
        rows.append(dict(trial=trial,nonzero_primal_currents=sum(v!=0 for v in J.values()),
                         maximum_magnitude=max(abs(v) for v in J.values()),
                         witness_counts=dict(Counter(witness_count)),
                         max_dual_divergence=max(abs(v) for v in divergence)))
        last_J=J
    # Exact face incidence count, reconstructed by boundaries of every3-cell.
    occurrences=Counter()
    for x in vertices:
        for axes in combinations(range(4),3):
            for r,i in enumerate(axes):
                rest=axes[:r]+axes[r+1:]
                occurrences[x,rest]+=1
                occurrences[shift(x,i,L),rest]+=1
    assert set(occurrences.values())=={4}
    # Dual-edge adjacency sharing either endpoint.
    edges=[(x,i) for x in vertices for i in range(4)]
    at_vertex={x:[] for x in vertices}
    for e in edges:
        x,i=e;at_vertex[x].append(e);at_vertex[shift(x,i,L)].append(e)
    degrees=[]
    for e in edges:
        x,i=e
        degrees.append(len((set(at_vertex[x])|set(at_vertex[shift(x,i,L)]))-{e}))
    assert set(degrees)=={14}
    # Wrong Hodge signs must fail the separately assembled divergence.
    wrong={(x,i):last_J[shift(x,i,L),tuple(j for j in range(4) if j!=i)]
           for x in vertices for i in range(4)}
    wrong_div=[]
    for x in vertices:
        z=0
        for i in range(4):
            previous=list(x);previous[i]=(previous[i]-1)%L
            z+=wrong[x,i]-wrong[tuple(previous),i]
        wrong_div.append(z)
    assert max(abs(v) for v in wrong_div)>0
    return dict(size=L,angle_units_per_turn=Q,random_seed=20260916,rows=rows,
                face_threecell_incidence=4,dual_edge_adjacency_degree=14,
                wrong_Hodge_sign_max_divergence=max(abs(v) for v in wrong_div))


def edge_dissemination():
    rows=[]
    for L in (4,6,8):
        for orientation in range(3):
            normals=[j for j in range(3) if j!=orientation]
            for offsets in product((0,1),repeat=2):
                p=[0,0,0];q=[0,0,0];q[orientation]=1
                for j,b in zip(normals,offsets):p[j]=q[j]=b
                seen=Counter();signs=Counter()
                for x in product(range(L),repeat=3):
                    rp=tuple((x[j]+(p[j] if x[j]%2==0 else 1-p[j]))%L for j in range(3))
                    rq=tuple((x[j]+(q[j] if x[j]%2==0 else 1-q[j]))%L for j in range(3))
                    if (rq[orientation]-rp[orientation])%L==1:anchor,sign=rp,1
                    else:anchor,sign=rq,-1
                    assert all(anchor[j]%2==b for j,b in zip(normals,offsets))
                    seen[anchor]+=1;signs[sign]+=1
                assert len(seen)==L**3//4 and set(seen.values())=={4}
                rows.append(dict(L=L,orientation=orientation,offsets=offsets,
                                 distinct_links=len(seen),multiplicity=4,signs=dict(signs)))
    return rows


def constants():
    mp.mp.dps=80
    alpha=mp.pi/3;c=1-mp.cos(alpha/2)
    T=alpha/(16*mp.sqrt(2*c))
    C0=3*mp.pi**2/16+4-24/mp.pi**2
    rows=[]
    for gs in ('.01','.005','.004','.003'):
        g=mp.mpf(gs)
        logB=min(0,mp.log(17)/4+C0*T-T*c/(4*g*g))
        logE=min(0,mp.log(4)/4+C0*T-alpha*alpha/(32*g*g*T))
        logstar=max(logB,logE)
        p=min(1,6*mp.exp(logstar/24))
        rows.append(dict(g=gs,log_magnetic=str(logB),log_temporal=str(logE),
                         support_parameter=str(p),degree_squared_times_p=str(196*p)))
    assert mp.mpf(next(r for r in rows if r['g']=='.004')['degree_squared_times_p'])<mp.mpf('.021')
    # Explicit positivity of the sufficient range from the magnetic bound;
    # verify the temporal bound is smaller throughout this range below.
    threshold=mp.sqrt((T*c/96)/(mp.log(1176)+mp.log(17)/96+C0*T/24))
    assert mp.mpf('.004')<threshold<mp.mpf('.0051')
    assert alpha*alpha/(32*T)>T*c/4 and mp.log(4)/4<mp.log(17)/4
    return dict(alpha=str(alpha),T=str(T),C0=str(C0),
                sufficient_g_strictly_below=str(threshold),rows=rows)


def main():
    start=time.monotonic()
    ans=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             cochains=integer_currents(),edge_geometry=edge_dissemination(),constants=constants())
    # Check the witness loss using independently enumerated incidence and
    # orientation classes, rather than accepting the literal denominator.
    witness_loss=ans['cochains']['face_threecell_incidence']*len(list(combinations(range(4),2)))
    for row in ans['constants']['rows']:
        p=mp.mpf(row['support_parameter'])
        if p<1:
            observed=mp.log(p/6)/max(mp.mpf(row['log_magnetic']),mp.mpf(row['log_temporal']))
            assert abs(observed-1/mp.mpf(witness_loss))<mp.mpf('1e-65')
    ans['independently_enumerated_witness_loss']=witness_loss
    ans['elapsed_seconds']=time.monotonic()-start
    ans['status']='PERSONAL_CHECKS_COMPLETED'
    _emit(ans)




def _check_inputs():
    root = Path(__file__).resolve().parents[1]
    for name in AUDIT_INPUT_PATHS:
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != EXPECTED_INPUT_SHA256[name]:
            raise RuntimeError("input identity mismatch: " + name)

def _emit(report):
    report["input_sha256"] = dict(EXPECTED_INPUT_SHA256)
    report["completed_diagnostic_families"] = 3
    report["total_unit"] = "completed diagnostic families, not dynamic assertions"
    report["static_source_assert_statements"] = 15
    output = Path(__file__).resolve().parents[1] / "logs" / "runner-cache" / (Path(__file__).stem + ".json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("TOTAL: PASS=3 FAIL=0")
    print('per_element: exact oriented coboundary, integrality, conservation, dual divergence and witnesses.')
    print('per_site: five seeded integer fields on a four-dimensional L4 torus; not ground-law samples.')
    print('per_mode: checked and not executed — no physical spectrum is computed by this cochain program.')
    print('per_block: link dissemination at L4/6/8 and original80-digit fixed-coupling parameter checks.')
    print('lattice_wide: finite periodic cochain support and degree counts completed; infinite-Z4 current law uses the full spatial-path-limit proof.')

if __name__ == '__main__':
    _check_inputs()
    main()
