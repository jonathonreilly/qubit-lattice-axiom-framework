#!/usr/bin/env python3
"""B26 part 1b/2: structure of the only enlargement the exhaustive class allows (the A2 half-letters A_a = A0 S^a),
in the B20_check model (second build; cross-check of classify_letters.py which used B7_check/chk_core).
(i) A0 is A2-pseudoscalar, not symmetric; A0^2 = -1; A_a := A0 S^a reproduces the chk_core list.
(ii) Algebra: A0 S A0^-1 = S^-1;  A0 normalises the on-site palette (H_on -> H_on, Lambda -> -Lambda, PLm permuted);
     A0 swaps D+ <-> D- at k*.  So even-A words = words in {S^n, R_L, Rt := A0 R_L A0^-1, palette'}.
(iii) Is Rt a word in the old palette?  Test Rt(k) vs U1 S^m R_L S^n U2 for symmetric on-site U1,U2.
(iv) Velocity at k* (B20 L1 mechanism): each letter's D+/D- compression and derivative; L1 for random words incl. Rt."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
t0 = time.time()
from b26lib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(11)
KS = rng.uniform(-np.pi, np.pi, size=(8, 3))

# (i)
check("untwisted average of c0 -> -c0 vanishes (no symmetric antipodal letter)", np.abs(A0_sym_try).max() < 1e-12 if np.isfinite(A0_sym_try).all() else True)
comm, a2, tr = covariance(A0)
check("A0 is a signed permutation c -> -c, translation invariant, A2-covariant, NOT rotation-symmetric", 
      np.allclose(np.abs(A0), np.abs(A0).round()) and (np.abs(A0) > .5).sum() == 12 and all((np.abs(A0[CI[frozenset(neg(x) for x in c)], CI[c]]) > .5) for c in CORN) and a2 and tr and not comm)
check("A0^2 = -1 (eigenvalues +-i, 6 each)", np.allclose(A0 @ A0, -np.eye(12)))
for a in (1, 2, -1, -2):
    pass
check("A0 S(k)^a A0^-1 = S(k)^-a  (a = 1, 2; 8 random k)", all(np.allclose(A0 @ Sk(k, a) @ A0i, Sk(k, -a)) for k in KS for a in (1, 2)))

# (ii) on-site palette normalisation
def match(Pset, X):
    for j, Q in enumerate(Pset):
        if np.allclose(Q, X): return j
    return None
permH = [match(PH, A0 @ P @ A0i) for P in PH]; permL = [match(PLm, A0 @ P @ A0i) for P in PLm]
print("  H_on eigen-projectors (eigvals", sorted(set(np.round(np.linalg.eigvalsh(Hon0), 4))), ") under A0 conj ->", permH)
print("  Lambda eigen-projectors (eigvals", sorted(set(np.round(np.linalg.eigvalsh(Lam), 4))), ") under A0 conj ->", permL)
check("A0 H_on A0^-1 = H_on and A0 Lambda A0^-1 = -Lambda", np.allclose(A0 @ Hon0 @ A0i, Hon0) and np.allclose(A0 @ Lam @ A0i, -Lam))
check("A0 permutes the PH/PLm projectors, so A0 (Clifford / pi6 palette) A0^-1 = palette (no new on-site letters)",
      None not in permH and None not in permL)
# full on-site symmetric algebra closure
B = np.array([b.reshape(-1) for b in ONSITE_BASIS]).T
def in_onsite(X): c, *_ = np.linalg.lstsq(B, X.reshape(-1), rcond=None); return np.allclose(B @ c, X.reshape(-1), atol=1e-9)
check("A0 conjugation maps the 6-dim symmetric on-site algebra into itself", all(in_onsite(A0 @ b @ A0i) for b in ONSITE_BASIS), f"dim {len(ONSITE_BASIS)}")
check("A0 is not in the symmetric on-site algebra", not in_onsite(A0))
Wk = Wword(['R'], kst)
check("A0 swaps D+ and D- (P_D+ A0 P_D+ = 0, ||P_D- A0 P_D+|| = ||P_D+||)", np.allclose(Dp.conj().T @ A0 @ Dp, 0) and np.isclose(np.linalg.norm(Dm.conj().T @ A0 @ Dp) ** 2, 2))

# (iii) Rt = A0 R_L A0^-1
check("Rt(k) is unitary, Hermitian, Rt^2 = 1 (constant spectrum +-1, like R_L)", all(np.allclose(RLt(k) @ RLt(k), np.eye(12)) and np.allclose(RLt(k), RLt(k).conj().T) for k in KS))
check("Rt(k) = R_L(-k)^? : Rt(k) != R_L(k) and Rt has the hop pattern of R_L(-k) (same |entries|)",
      not np.allclose(RLt(KS[0]), RLk(KS[0])) and all(np.allclose(np.abs(RLt(k)), np.abs(RLk(-k))) for k in KS))
# exact product identity (found after the first run, whose diagonal-gauge factorisation test was buggy; log kept)
check("Rt(k) = A0 R_L(k) A0^-1 = -S(k) R_L(k) S(k)^-1 exactly (8 random k): Rt is an OLD-palette word", all(np.allclose(RLt(k), -Sk(k, 1) @ RLk(k) @ Sk(k, -1)) for k in KS))
# direct, gauge-free test: is Rt in the algebra generated (over constant on-site symmetric coefficients) by S^m R S^n, m,n in -2..2?
basisY = []
for m in range(-2, 3):
    for n in range(-2, 3):
        for b1 in ONSITE_BASIS:
            for b2 in ONSITE_BASIS:
                basisY.append(np.concatenate([(b1 @ Sk(k, m) @ RLk(k) @ Sk(k, n) @ b2).reshape(-1) for k in KS]))
BY = np.array(basisY).T; tgt = np.concatenate([RLt(k).reshape(-1) for k in KS])
cf, *_ = np.linalg.lstsq(BY, tgt, rcond=None); res = np.linalg.norm(BY @ cf - tgt) / np.linalg.norm(tgt)
print(f"   least-squares residual of Rt in span{{U1 S^m R_L S^n U2 : U symmetric on-site, |m|,|n|<=2}} over 8 k: {res:.3e}")
check("consistency: Rt lies in span{U1 S^m R_L S^n U2} (symmetric on-site U, |m|,|n|<=2) -- no genuinely new symmetric letter", res < 1e-10, f"residual {res:.2e}")

# (iv) velocity at k* : D+/D- compressions
def comp(Xf, Dsp, k):
    X = Xf(k); h = 1e-6; dX = [(Xf(k + h * e) - Xf(k - h * e)) / (2 * h) for e in np.eye(3)]
    return Dsp.conj().T @ X @ Dsp, [Dsp.conj().T @ d @ Dsp for d in dX]
for name, Xf in [('S', lambda k: Sk(k, 1)), ('R_L', RLk), ('Rt', RLt)]:
    for sgn in (1, -1):
        for lab, Dsp in (('D+', Dp), ('D-', Dm)):
            X0, dX = comp(Xf, Dsp, sgn * kst)
            sc = np.allclose(X0, X0[0, 0] * np.eye(2), atol=1e-8)
            leak = np.linalg.norm((np.eye(12) - Dsp @ Dsp.conj().T) @ Xf(sgn * kst) @ Dsp)
            print(f"   {name:4s} at {'+' if sgn > 0 else '-'}k* on {lab}: scalar={sc} value={np.round(X0[0,0], 6)} leak={leak:.1e} "
                  f"||P dX P|| = {[round(float(np.linalg.norm(d)), 6) for d in dX]}")
X0p, dXp = comp(RLt, Dp, kst); X0m, dXm = comp(RLt, Dm, kst)
check("Rt acts on D+/D- at +k* as a scalar with ZERO compressed derivative (no velocity source, like R_L)",
      np.allclose(X0p, X0p[0, 0] * np.eye(2)) and np.allclose(X0m, X0m[0, 0] * np.eye(2)) and max(np.linalg.norm(d) for d in dXp + dXm) < 1e-6)
rp = [comp(RLk, D_, s * kst)[0][0, 0] for s in (1, -1) for D_ in (Dp, Dm)]; tp = [comp(RLt, D_, s * kst)[0][0, 0] for s in (1, -1) for D_ in (Dp, Dm)]
print("   R_L scalars (+k*:D+,D-; -k*:D+,D-) =", np.round(rp, 6), "  Rt scalars =", np.round(tp, 6))
check("Rt scalars on (D+, D-) at +-k* are those of R_L with D+ <-> D- swapped", np.allclose(tp, [rp[1], rp[0], rp[3], rp[2]]))

# L1 for random words including Rt and the full on-site algebra: every 2-fold k* level speed = |n_S| sqrt2/3
def rand_on(): return rand_onsite_unitary(rng)
bad = 0; tested = 0; maxdev = 0
for t in range(300):
    n = rng.integers(2, 6); w = []
    for _ in range(n):
        r_ = rng.random()
        w.append(rng.choice(['S', 'Si', 'S2', 'R', 'Rt']) if r_ < 0.6 else rand_on())
    w = [str(x) if isinstance(x, np.str_) else x for x in w]
    ns = nS(w); W0 = Wb(w, kst[None])[0]
    for E, m in levels(W0, 1e-6):
        if m != 2: continue
        r = dpt(w, kst, E)
        if r is None or r[0] != 2: continue
        sp = [np.abs(np.linalg.eigvalsh(sum(d[j] * r[1][j] for j in range(3)))) for d in DIRS43]
        dev = max(abs(x - abs(ns) * np.sqrt(2) / 3) for s_ in sp for x in s_)
        tested += 1; maxdev = max(maxdev, dev); bad += dev > 1e-5
check("L1 extended: every 2-fold k* level of random words in {S^+-1, S^2, R_L, Rt, full symmetric on-site algebra} has isotropic speed |n_S| sqrt2/3",
      tested > 100 and bad == 0, f"{tested} doublets, max dev {maxdev:.1e}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
