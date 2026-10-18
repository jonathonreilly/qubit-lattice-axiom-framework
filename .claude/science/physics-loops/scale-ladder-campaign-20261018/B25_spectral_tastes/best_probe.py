#!/usr/bin/env python3
"""B25 part 2c: the closest ALIGN2 case, S4.P1.S4.L130.S4.P11.S4.L130 at E = 0 (D+ (+) D-), probed fully.
(a) full B24 stage C (Nelder-Mead node search, 40 starts) -- the screen stopped at the first defect;
(b) the defect classes (four C3-axis-type classes mod Lambda_sp): multiplicity, finite-difference cone (independent of DPT), its fixers;
(c) all (pi/16)Z^3 nodes at E classified.  Prints PASS/FAIL, TOTAL."""
import sys, os, time, collections
os.environ['B24_NM'] = '40'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
ALL.update(PLANE6)
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
sk, names = ('S4', 'p', 'S4', 'o', 'S4', 'q', 'S4', 'o'), ('P1', 'L130', 'P11', 'L130')
w = build24(sk, names); E = 0.0; vs = abs(nS(w)) * np.sqrt(2) / 3; print("n_S", nS(w), "v_D", vs)
A = analyse_word(w); print("lattices:", A['Lu'], A['Lsp'], "k-dependent cosets:", A['kdep'])
SPEC16 = np.array(list(itertools.product(np.arange(-16, 16) * np.pi / 16, repeat=3)))
ds = np.concatenate([dist_E(w, SPEC16[i:i + 8192], E) for i in range(0, len(SPEC16), 8192)])
cand = SPEC16[ds < 1e-7]; Ls = LATS[A['Lsp']]
typ = collections.Counter(point_type(k, Ls) for k in cand); print(f"(pi/16)Z^3 nodes at E: {len(cand)}, types mod Lambda_sp: {dict(typ)}")
# classify one representative per class mod Lambda_sp
Lv = np.array(sorted(Ls)); seen = set(); reps = []
for k in cand:
    v = tuple(int(round(x)) % 32 for x in k / (np.pi / 16))
    if v in seen: continue
    reps.append(k); seen |= {tuple((np.array(v) + t) % 32) for t in Lv}
cls = [(tuple(np.round(k / np.pi, 4)), point_type(k, Ls), classify(w, k, E, vs)) for k in reps]
for c in cls: print("   class rep", c[0], c[1], c[2][0], c[2][1], {a: round(b, 4) for a, b in c[2][2].items()})
bad = [c for c in cls if c[2][1] != 'ok']
check("grid nodes fall into classes mod Lambda_sp; the T-fixed classes are all isotropic untilted cones at v_D", all(c[2][1] == 'ok' for c in cls if c[1] == 'T'))
# FD cone at the defect
DIRS_ = np.vstack([np.eye(3), np.random.default_rng(5).normal(size=(300, 3))]); DIRS_ /= np.linalg.norm(DIRS_, axis=1)[:, None]
for c in bad:
    k0 = np.array(c[0]) * np.pi; m = c[2][0]; h = 1e-5; sl = []
    for d in DIRS_:
        e = np.angle(np.linalg.eigvals(Wb(w, (k0 + h * d)[None])[0])); dd = wrap(e - E); idx = np.argsort(np.abs(dd))[:m]; sl.append(np.sort(dd[idx]) / h)
    sl = np.array(sl); sp = np.abs(sl - sl.mean(1, keepdims=True))
    print(f"   defect {c[0]} type {c[1]}: FD speeds min {sp.min():.4f} max {sp.max():.4f}, tilt {np.abs(sl.mean(1)).max():.1e}")
    check("defect class confirmed anisotropic by finite differences (independent of DPT)", sp.max() - sp.min() > 1e-2)
# full stage C with Nelder-Mead
rec = dict(sk=sk, names=names, E=E, m=4, kind='D+D-', nS=16, nR=0, fermi=False, rimag=0.0)
r = stageC(rec)
gen = [x for x in r['bad'] if x[1] == 'gen']
print(f"   full stage C: {len(r['nodes'])} nodes, {len(r['bad'])} defective, of which generic {len(gen)}; gridmin {r['gridmin']:.2e}")
for x in r['bad'][:6]: print("     ", x[0], x[1], x[2], x[3], x[4].get('smin'), x[4].get('smax'))
check("full stage C ran (Nelder-Mead from 40 starts)", len(r['nodes']) > 0)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
