#!/usr/bin/env python3
"""C7_check C: O-fixed momenta and the gap of the selected sector 1c+11, independently.

Method (different from C7's L = 4 GF(2) sign propagation): in a period-1 gauge (12 bands) a proper rotation M of
the site maps the Hamiltonian to a gauge copy iff there are eta in {+-1}^12 (one sign per corner type) and
s in {0,1}^3 with  amp_M(e) = eta_{c1} eta_{c2} (-1)^{s.R} amp(e)  on all 36 edge types; the symmetry then maps
k -> M k + pi s.  I solve this exactly over GF(2) for every M and every s (s should be unique), confirm
E(Mk + pi s) = E(k) spectrally, and list the k in (pi/2){0..3}^3 with M k + pi s_M = k mod 2 pi for all 24 M
(complete: the three axis C2's force 2k in pi Z^3).  Controls: the real-hopping corner pattern 1011 (C6 A4:
a fixed pair) and the other chiral patterns that admit a period-1 gauge.
Gap: min positive eigenvalue of the 12-band one-body matrix on a 24^3 grid + Nelder-Mead, t2 in [0.05, 3].
"""
import itertools, os, sys, time
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k7_geom import Lat, TYPES, TKEY, CORNERS, CI, kgrid, solve_gauge, maj_targets, maj_amp, gf2, neg

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


L1 = Lat(1)
rng = np.random.default_rng(5)
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)
assert len(ROTS) == 24
rv = lambda M, a: tuple(int(x) for x in M @ np.array(a))
rc = lambda M, c: frozenset(rv(M, a) for a in c)


def sym_solutions(amp, M):
    """all s in {0,1}^3 for which a corner-sign gauge eta makes the M-rotated amplitudes equal to amp."""
    ampM = np.zeros(36, complex); okmap = True
    for t, (c1, c2, R, k) in enumerate(TYPES):
        t2, s = TKEY[(rc(M, c1), rc(M, c2), rv(M, R))]
        ampM[t2] = amp[t] if s == 1 else np.conj(amp[t])
    out = []
    for svec in itertools.product((0, 1), repeat=3):
        rows, rhs = [], []; ok = True
        for t, (c1, c2, R, k) in enumerate(TYPES):
            r = ampM[t] / amp[t]
            if abs(r - 1) < 1e-9: b = 0
            elif abs(r + 1) < 1e-9: b = 1
            else: ok = False; break
            rows.append([CI[c1], CI[c2]]); rhs.append((b + int(np.dot(svec, R))) % 2)
        if not ok:
            continue
        eta = gf2(rows, rhs, 12)
        if eta is not None:
            out.append((np.array(svec), eta))
    return out


def bands(amp, Ks):
    return np.linalg.eigvalsh(L1.bloch(amp, Ks))


def analyse(name, amp):
    sols = [sym_solutions(amp, M) for M in ROTS]
    if any(len(s) == 0 for s in sols):
        return dict(name=name, invariant=False)
    uniq = all(len(s) == 1 for s in sols)
    S = [s[0][0] for s in sols]
    ks = rng.uniform(0, 2 * np.pi, (40, 3)); e0 = bands(amp, ks)
    dev = max(np.max(np.abs(bands(amp, ks @ M.T + np.pi * s) - e0)) for M, s in zip(ROTS, S))
    # wrong shifts must fail spectrally (the test discriminates)
    wrong = min(np.max(np.abs(bands(amp, ks @ M.T + np.pi * ((s + d) % 2)) - e0))
                for M, s in zip(ROTS, S) for d in itertools.product((0, 1), repeat=3) if any(d))
    fixed = [k for k in itertools.product(range(4), repeat=3)
             if all(((M @ np.array(k) + 2 * s - np.array(k)) % 4 == 0).all() for M, s in zip(ROTS, S))]
    # C4^4 sign: product of eta over the 4-cycle of a corner under a C4 (uniform over corners)
    c4 = []
    for M, s in zip(ROTS, sols):
        if int(np.trace(M)) == 1:
            eta = s[0][1]
            vals = set()
            for c in CORNERS:
                p = 1; cc = c
                for _ in range(4):
                    cc = rc(M, cc); p *= (-1) ** int(eta[CI[cc]])
                vals.add(p)
            c4.append(tuple(sorted(vals)))
    return dict(name=name, invariant=True, unique=uniq, dev=dev, wrong=wrong, fixed=fixed, c4=sorted(set(c4)))


base = maj_amp(L1, np.zeros(36, np.uint8), 1, 1)
P0 = (1, 'c+', 1, 1)
x0 = solve_gauge(L1, base, maj_targets(L1, *P0))
check("1c+11 admits a period-1 (translation-invariant) gauge", x0 is not None)
res = {}
print(f"\nC1: spectral/exact symmetry test, period-1 gauges; t = {time.time()-T0:.1f}s")
for P in [(sq, 'c+', pl, tu) for sq in (0, 1) for pl in (0, 1) for tu in (0, 1)] + [(1, 's+', 1, 1)]:
    x = solve_gauge(L1, base, maj_targets(L1, *P))
    nm = f"{P[0]}{P[1]}{P[2]}{P[3]}"
    if x is None:
        print(f"   {nm}: no period-1 gauge"); continue
    r = analyse(nm, maj_amp(L1, x, 1, 0.37))
    res[nm] = r
    if not r['invariant']:
        print(f"   {nm}: not invariant under all 24 proper rotations (in this gauge class)")
    else:
        print(f"   {nm}: unique s per rotation {r['unique']}, spectral dev {r['dev']:.1e}, wrong-shift min dev "
              f"{r['wrong']:.2e}, C4^4 {r['c4']}, O-fixed momenta (pi/2 units) {r['fixed']}")
# control: real corner pattern 1011 (standard flux, t > 0), amplitudes -t u
baseR = -np.where(L1.onsite, 1.0, 1.0).astype(complex)
tgR = np.array([np.pi * {'square': 1, 'triangle': 0, 'plaquette': 1, 'tube': 1}[k] for k, _, _ in L1.faces])
xR = solve_gauge(L1, baseR, tgR)
ampR = -np.where(L1.onsite, -1.0, 0.37) * (-1.0) ** xR     # t1 = -1 (sign irrelevant for the symmetry test)
rR = analyse('1011 real', ampR.astype(complex))
print(f"   control corner 1011 (real): unique {rR['unique']}, spectral dev {rR['dev']:.1e}, wrong-shift min dev "
      f"{rR['wrong']:.2e}, C4^4 {rR['c4']}, fixed {rR['fixed']}")
r0 = res['1c+11']
check("1c+11: invariant under all 24 rotations with a unique momentum shift each; E(Mk + pi s) = E(k) to 1e-9 "
      "and every wrong shift fails (> 1e-3)", r0['invariant'] and r0['unique'] and r0['dev'] < 1e-9 and r0['wrong'] > 1e-3,
      f"dev {r0['dev']:.1e}, wrong {r0['wrong']:.2e}")
check("1c+11 has NO O-fixed momentum", r0['fixed'] == [], str(r0['fixed']))
check("control: corner pattern 1011 (real hopping) has exactly two O-fixed momenta, k and k + (pi,pi,pi)",
      rR['invariant'] and len(rR['fixed']) == 2 and
      all(((np.array(rR['fixed'][0]) + 2) % 4 == np.array(rR['fixed'][1])) | ((np.array(rR['fixed'][1]) + 2) % 4 == np.array(rR['fixed'][0]))),
      str(rR['fixed']))
check("C4^4 = -1 for 1c+11 and for the 1011 control", r0['c4'] == [(-1,)] and rR['c4'] == [(-1,)], f"{r0['c4']} / {rR['c4']}")
withfixed = sorted(n for n, r in res.items() if r.get('invariant') and r['fixed'])
print(f"   chiral/period-1 patterns with an O-fixed momentum: {withfixed}")

# ---------------------------------------------------------------- C2: gap scan
print(f"\nC2: Majorana gap of 1c+11 (min positive eigenvalue of the 12-band one-body matrix; the many-body fermion gap of"
      f" H_M = sum J u (i c c) is twice this); t = {time.time()-T0:.1f}s")
K24 = kgrid(24)
gaps = {}
for t2 in (0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9, 1.0, 1.3, 1.6, 2.0, 2.5, 3.0):
    a = maj_amp(L1, x0, 1, t2)
    ev = bands(a, K24)
    m = np.abs(ev).min(axis=1)
    f = lambda k: np.abs(np.linalg.eigvalsh(L1.bloch(a, k[None])[0])).min()
    best = m.min(); kb = K24[np.argmin(m)]
    for j in np.argsort(m)[:8]:
        r = minimize(f, K24[j], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-12, maxiter=4000))
        if r.fun < best: best, kb = r.fun, r.x
    nmin = int(np.sum(m < m.min() + 1e-9))
    gaps[t2] = best
    pts = sorted({tuple(int(round(x / np.pi)) % 2 for x in K24[j]) for j in np.where(m < m.min() + 1e-9)[0]})
    print(f"   t2 = {t2:4.2f}: Delta = {best:.5f} at k/pi = {np.round(np.mod(kb, 2*np.pi)/np.pi, 4)}; grid minima {nmin}: {pts}")
check("1c+11 fully gapped for t2 in [0.05, 3]: min Delta > 0.9", min(gaps.values()) > 0.9, f"min {min(gaps.values()):.5f}")
c7 = {0.05: 1.37380, 0.2: 1.25862, 0.5: 1.07226, 0.7: 1.00147, 1.0: 1.01065, 2.0: 1.84104, 3.0: 3.09218}
dv = max(abs(gaps[t] - v) for t, v in c7.items())
check("gap values agree with C7 c7_C.log at the 7 common t2", dv < 1e-4, f"max |diff| {dv:.1e}")
print(f"\nelapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")


# ---------------------------------------------------------------- C3: discrimination of the spectral test
print(f"\nC3: is the spectral shift test discriminating?  (extra spectral symmetry k -> k + pi(1,1,1)); t = {time.time()-T0:.1f}s")
a0 = maj_amp(L1, x0, 1, 0.37)
ks = rng.uniform(0, 2 * np.pi, (40, 3)); e0 = bands(a0, ks)
pas = {}
for d in itertools.product((0, 1), repeat=3):
    pas[d] = np.max(np.abs(bands(a0, ks + np.pi * np.array(d)) - e0)) < 1e-9
print("   shifts d with E(k + pi d) = E(k) for 1c+11:", [d for d, v in pas.items() if v])
eR0 = bands(ampR.astype(complex), ks)
print("   ... for the real 1011 control:", [d for d in itertools.product((0, 1), repeat=3)
                                          if np.max(np.abs(bands(ampR.astype(complex), ks + np.pi * np.array(d)) - eR0)) < 1e-9])
sols = [sym_solutions(a0, M)[0][0] for M in ROTS]

chi = []
for M in ROTS:
    tr = int(np.trace(M))
    # O -> S4 sign: C4 (tr 1) and edge C2 (tr -1, off-diagonal) are odd; C3 (tr 0), axis C2, e are even
    chi.append(1 if (tr == 1 or (tr == -1 and not np.allclose(np.abs(np.diag(M)), 1))) else 0)
alt = [(s + c * np.ones(3, int)) % 2 for s, c in zip(sols, chi)]
spec_alt = max(np.max(np.abs(bands(a0, ks @ M.T + np.pi * s) - e0)) for M, s in zip(ROTS, alt))
fixed_alt = [k for k in itertools.product(range(4), repeat=3)
             if all(((M @ np.array(k) + 2 * s - np.array(k)) % 4 == 0).all() for M, s in zip(ROTS, alt))]
print(f"   alternative shift assignment s'_M = s_M + chi(M)(1,1,1) (chi = sign rep): spectral dev {spec_alt:.1e}, "
      f"its 'fixed momenta' {fixed_alt}")
# is the alternative realised by a unitary Z2 gauge? (exact)
real_alt = all(any((s == sa).all() for s, _ in sym_solutions(a0, M)) for M, sa in zip(ROTS, alt))
print(f"   alternative realised by unitary corner-sign gauges: {real_alt}")
# antiunitary: improper rotation P' = -M combined with complex conjugation K (one-body: amp -> conj(amp) rotated)
def sym_src(src, tgt, M):
    ampM = np.zeros(36, complex)
    for t, (c1, c2, R, k) in enumerate(TYPES):
        t2_, s_ = TKEY[(rc(M, c1), rc(M, c2), rv(M, R))]
        ampM[t2_] = src[t] if s_ == 1 else np.conj(src[t])
    out = []
    for svec in itertools.product((0, 1), repeat=3):
        rows, rhs = [], []; ok = True
        for t, (c1, c2, R, k) in enumerate(TYPES):
            r = ampM[t] / tgt[t]
            if abs(r - 1) < 1e-9: b_ = 0
            elif abs(r + 1) < 1e-9: b_ = 1
            else: ok = False; break
            rows.append([CI[c1], CI[c2]]); rhs.append((b_ + int(np.dot(svec, R))) % 2)
        if ok and gf2(rows, rhs, 12) is not None:
            out.append(tuple(svec))
    return out


for nm, A in (('1c+11', a0), ('1011 real', ampR.astype(complex))):
    imp = [-M for M in ROTS]
    uni_imp = [sym_src(A, A, M) for M in imp]
    anti_imp = [sym_src(np.conj(A), A, M) for M in imp]
    anti_prop = [sym_src(np.conj(A), A, M) for M in ROTS]
    print(f"   {nm}: improper rotations unitary: {sum(bool(x) for x in uni_imp)}/24; improper x K: "
          f"{sum(bool(x) for x in anti_imp)}/24, inversion x K shift {anti_imp[0]}; proper x K: {sum(bool(x) for x in anti_prop)}/24")
