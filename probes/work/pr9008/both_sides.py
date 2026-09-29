"""PR 9008 attack-b: SAME TEST, BOTH SIDES.

The note separates two things with one estimator: 'uniform ice keeps the transverse form S_zz = P_zz/K at small wavevectors' (A) against
'the covariance has a direction-dependent implied stiffness' (B).  Every separating statement is applied here, unchanged, to both kinds of object and in every
representation the note uses (raw covariance S_zz, ratio r = K_cont sum S / sum P, the unit-arrow identity, the implied stiffness c of the 24 smallest wavevectors):
  A  ice under the note's hypothesis  S = P/K            (exact expectation, K = K_cont, no sampling)
  B  independent +-1 arrows                              (S = 1 for every k != 0 exactly; a field that is not divergence-free)
  C  ice with a z-axis distortion S = P (1 + eps s_z^2)/K, eps = 0.5% (what a failure of the form would look like)
Exact expectations in exact arithmetic where the note's quantities are exact (Fractions of algebraic numbers replaced by 50-digit mpmath).
"""
import itertools, sys
import mpmath as mp
import numpy as np
mp.mp.dps = 50
L = 16; N = L ** 3
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

s2 = [2 - 2 * mp.cos(2 * mp.pi * a / L) for a in range(L)]
KC = mp.mpf(2 * N + 1) / (3 * N)
def P(m, zc): return 1 - s2[zc] / sum(s2[a] for a in m)
def wavevectors(m, zc):
    out = []
    for a, b, c in itertools.product(range(L), repeat=3):
        f = tuple(min(t, L - t) for t in (a, b, c))
        if tuple(sorted(f)) == m and f[2] == zc:
            out.append((a, b, c))
    return out
NOTE5 = [(0, 1, 1), (0, 1, 2), (0, 2, 2), (1, 1, 2), (1, 2, 2)]

def S_A(k, K=KC): return P_k(k) / K
def P_k(k):
    a, b, c = k; return 1 - s2[c] / (s2[a] + s2[b] + s2[c])
def S_B(k): return mp.mpf(1)
def S_C(k, eps=mp.mpf("0.005")): return P_k(k) * (1 + eps * s2[k[2]]) / KC

def group_stats(m, zc, Sfun):
    ks = [k for k in wavevectors(m, zc) if P_k(k) > mp.mpf("0.05")]
    sumS = sum(Sfun(k) for k in ks); sumP = sum(P_k(k) for k in ks)
    return sumS / len(ks), KC * sumS / sumP           # mean raw S_zz, ratio r

rows = {}
print("multiset      (lo z-fold, hi z-fold)   raw S_zz(lo) - S_zz(hi)  [A | B | C]        ratio r(lo) - r(hi)  [A | B | C]")
for m in NOTE5:
    us = [zc for zc in sorted(set(m)) if P(m, zc) > mp.mpf("0.05")]
    lo = min(us, key=lambda z: P(m, z)); hi = max(us, key=lambda z: P(m, z))
    raw = []; rat = []
    for Sf in (S_A, S_B, S_C):
        a_lo, r_lo = group_stats(m, lo, Sf); a_hi, r_hi = group_stats(m, hi, Sf)
        raw.append(a_lo - a_hi); rat.append(r_lo - r_hi)
    rows[m] = (raw, rat)
    print(f"{str(m):12s}   ({lo},{hi})   " + " | ".join(f"{float(x):+.4f}" for x in raw) + "        " + " | ".join(f"{float(x):+.5f}" for x in rat))

# 1. the note's representation (ratio) separates A from B by orders of magnitude, and the raw representation separates them the WRONG way round
zeroA = max(abs(rows[m][1][0]) for m in NOTE5)
minB = min(abs(rows[m][1][1]) for m in NOTE5)
check("ratio representation: A gives exactly zero difference in every multiset, B gives at least 0.2 (the note's se is about 0.0008: several hundred standard errors)",
      zeroA < mp.mpf(10) ** -40 and minB > 0.2, f"max |diff| A = {mp.nstr(zeroA, 3)}, min |diff| B = {mp.nstr(minB, 4)}, in note-se units {float(minB)/0.0008:.0f}")
rawA = min(abs(rows[m][0][0]) for m in NOTE5); rawB = max(abs(rows[m][0][1]) for m in NOTE5)
check("raw-covariance representation separates them the other way: ice (A) differs between assignments by at least 0.2/K_cont, the iid arrows (B) by exactly zero — a raw angular difference is not evidence for or against the transverse form",
      rawA > 0.3 and rawB < mp.mpf(10) ** -40, f"min |raw diff| A = {mp.nstr(rawA, 4)}, max |raw diff| B = {mp.nstr(rawB, 3)}")
# 2. the distortion C is what the ratio test can see; size in note-se units
cd = [abs(rows[m][1][2]) for m in NOTE5]
print(f"   C (eps = 0.5% z-axis distortion): ratio differences " + " ".join(f"{float(x)*100:.3f}%" for x in cd) + " ; in units of the note's per-multiset se (0.06-0.09%): "
      + " ".join(f"{float(x)/0.0008:.1f}" for x in cd))
check("C is visible in the ratio representation at the few-sigma level per multiset (0.5% distortion -> 0.1-0.3% differences), consistent with 'holds within about 0.2%'", min(cd) > 0.0005 and max(cd) < 0.005, f"{[round(float(x)*100,3) for x in cd]} %")
# 3. the unit-arrow identity separates nothing: iid arrows obey it to rounding, exactly like ice
rng = np.random.default_rng(90082)
worst = 0.0
for _ in range(5):
    E = rng.choice([-1.0, 1.0], size=(L, L, L))
    F = np.fft.fftn(E); worst = max(worst, abs((np.abs(F) ** 2).sum() / N - N))
check("the unit-arrow identity (sum_k S_zz = N) holds for iid +-1 arrows exactly as for ice, so passing it distinguishes nothing between them (it is a normalisation check)", worst < 1e-8, f"iid arrows: max deviation {worst:.1e} (note: ice 1.8e-12)")
# 4. the implied stiffness of the 24 smallest wavevectors, both sides
sel = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)
       if 0 < sum(min(t, L - t) ** 2 for t in (a, b, c)) <= 3 and P_k((a, b, c)) > mp.mpf("0.05")]
sumP = sum(P_k(k) for k in sel)
cA = sumP / (2 * sum(S_A(k) for k in sel)) if True else None
cB = sumP / (2 * sum(S_B(k) for k in sel))
cL = KC / 2
print(f"   24 smallest wavevectors: {len(sel)}; implied c: A {float(cA):.5f} (= K_cont/2 {float(cL):.5f}), B (iid) {float(cB):.5f}, note (ice, sampled) 0.33450")
check("the offset test separates ice from iid arrows: iid c is about 8% above K_cont/2, the note's ice offset is 0.337%; and under the exact hypothesis A the offset is zero",
      len(sel) == 24 and abs(cA - cL) < mp.mpf(10) ** -40 and (cB / cL - 1) > 0.05, f"iid offset {float(cB/cL-1)*100:.2f}%")
# 5. the multisets with a THIRD assignment: the note quotes lowest-minus-highest only; the middle pairs are equally implied by the form
m = (0, 1, 2)
us = sorted([zc for zc in set(m) if P(m, zc) > mp.mpf("0.05")], key=lambda z: P(m, z))
print("   {0,1,2} has three usable assignments, P_zz =", [round(float(P(m, z)), 3) for z in us], "-> the note's row compares the extremes only; the two other pairs are implied by the form too")
check("under A every pair of assignments of {0,1,2} has ratio difference exactly zero (so the two unquoted pairs are equally testable)", all(
      abs(group_stats(m, a, S_A)[1] - group_stats(m, b, S_A)[1]) < mp.mpf(10) ** -40 for a, b in itertools.combinations(us, 2)))

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-b same test both sides on PR 9008: ratio-difference test gives 0 for the hypothesis S=P/K and >= {float(minB):.2f} (>= {float(minB)/0.0008:.0f} note-se) for iid arrows, raw angular differences separate the other way round, unit-arrow identity passed equally by iid arrows (normalisation only), 0.5% z-axis distortion reads as {min(float(x) for x in cd)*100:.2f}-{max(float(x) for x in cd)*100:.2f}%, offset test: iid {float(cB/cL-1)*100:.1f}% vs ice 0.34%; the note claims no separation that the identity or the raw representation carries; PASS={PASS} FAIL={FAIL}; no defect")
sys.exit(1 if FAIL else 0)
