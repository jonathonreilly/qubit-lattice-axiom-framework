#!/usr/bin/env python3
"""Supplied Wilson-form arithmetic and finite, PDG-informed candidate search.

No physical Higgs prediction, computed loop coefficient, or exhaustive
construction no-go is established. Original diagnostics recoverable at
f24d17d97d372df977476e4a69674577f31af575:scripts/cl3_higgs_mass_wilson_chain_2026_05_10_higgsH1.py.
"""
import itertools
import math

AUDIT_TIMEOUT_SEC = 300


def main():
    checks = []
    def check(name, value):
        checks.append(bool(value))
        print(('PASS' if value else 'FAIL') + ': ' + name)
    plaquette, planck, target = .5934, 1.221e19, 125.25
    u = plaquette ** .25
    bare = 1 / (4 * math.pi)
    alm, strong = bare / u, bare / u**2
    v = planck * (7/8)**.25 * alm**16
    curvature = v / (2*u)
    candidate = curvature * math.sqrt(1-2*strong)
    print('Scope: supplied arithmetic; coefficient2 and formula selected with PDG exposure.')
    print(f'v={v:.12f}; curvature={curvature:.12f}; fitted candidate={candidate:.12f} GeV')
    check('geometric-mean coupling identity', abs(alm**2-bare*strong)<1e-15)
    check('equivalent supplied curvature expressions', abs(curvature-planck*(7/8)**.25*alm**17/(2*bare))<1e-9)
    print(f'Historical comparison: tree relative error={abs(curvature-target)/target:.12g}; fitted relative error={abs(candidate-target)/target:.12g}')
    # Preserve the original finite box and comparison thresholds; no all-integer assertion.
    rows=[]
    for a,b,d,c,n in itertools.product(range(-4,9),range(-4,5),range(-3,4),range(-4,5),range(13,21)):
        value=planck*(7/8)**(a/4)*2**(-b)*3**(-d)*u**c*alm**n
        rows.append((abs(value-target)/target,(a,b,c,d,n),value))
    best=min(rows)
    for threshold in [.003,.001,.0005]:
        print(f'Finite box matches below {threshold*100:g}%: {sum(r[0]<threshold for r in rows)}')
    print(f'Best finite-box result (relative error, a b c d N, value): {best}')
    good=[r for r in rows if r[0]<.001]
    simple=min(good,key=lambda r:sum(abs(z) for z in r[1][:4])+abs(r[1][4]-16))
    print(f'Least chosen complexity among sub0.1% matches: {simple}')
    check('58968 tuples evaluated',len(rows)==58968)
    check('explicit counterexample to old no-sub0.1%-match claim',best[0]<.001)
    check('seven matches in this supplied finite box',len(good)==7)
    # Independently expressed witness, with original acceptance threshold unchanged.
    witness=planck*(7/8)**1.5*8*u**3*alm**16/9
    check('explicit witness appears at the finite minimum',abs(witness-best[2])<1e-9)
    print('Historical sister-form comparisons (not independent predictions):')
    for label,value,comparison in [('v',v,246.22),('tau',v*bare*alm,1.7768)]:
        print(label,value,comparison,abs(value-comparison)/comparison)
    print('No uncertainty budget, matching calculation, pole interpretation, or physical action selection is proved.')
    print(f'TOTAL: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}')
    return 0 if all(checks) else 1

if __name__=='__main__':
    raise SystemExit(main())
