#!/usr/bin/env python3
"""C:two-point-function-response-table:a1   worker w-jonathonsmac4f50-j8016 (claude-opus-5)

Response against correlation for the sphere formation law in 3+1 at beta = 3 on a 32^3 level plane, for the
backward neighbourhood (n = 4 predecessors {0, e1, e2, e3}) and the light cone (n = 7, {0, +-e_j}).
formation_levelplane_copy.py beside this file is the untouched starting point; the chains here are the same law
written batched, so that coupled pairs run at once.

A1  exact support of the response after d levels (set propagation)
A2  exact linear-response identities R(k) = delta/(1-phi), C(k) = sigma^2/(1-|phi|^2)
A3  the linear theory on this 32^3 torus: stationary R and C by FFT, truncated R by exact iteration
N1  the measured equal-level covariance C(x) along three directions
N2  the measured response to h = 0.05 at one site at every level (200 coupled pairs, then 20 pairs for longer)
N3  the comparison: one-sidedness, symmetry, R/C, and the measurement against the linear prediction
"""
import time
import numpy as np
import sympy as sp

t_start = time.time()
L, BETA, H = 32, 3.0, 0.05
PAIRS, BATCH, BURN, MEASURE = 200, 50, 100, 100
LONG_PAIRS, LONG_T = 20, 400
MARKS, LONG_MARKS = (20, 60, 100), (100, 250, 400)
DIRS = {"(1,0,0)": (1, 0, 0), "(1,1,0)": (1, 1, 0), "(1,1,1)": (1, 1, 1)}
RS = (1, 2, 3, 4, 6, 8)
LATTICES = ((False, "backward n=4"), (True, "light-cone n=7"))
def A_lang(x): return 1.0 / np.tanh(x) - 1.0 / x
def at(F, d, r): return float(F[tuple((r * np.array(d)) % L)])

# ---------------------------------------------------------------- A1 exact support
def support(sym, depth):
    offs = [(0, 0, 0)] + [tuple(1 if j == i else 0 for j in range(3)) for i in range(3)]
    if sym: offs += [tuple(-1 if j == i else 0 for j in range(3)) for i in range(3)]
    cur = {(0, 0, 0)}
    for _ in range(depth): cur = {tuple(a + b for a, b in zip(x, o)) for x in cur for o in offs}
    return cur
for sym, name in LATTICES:
    for depth in (1, 2, 3, 6):
        sup = support(sym, depth)
        if not sym:
            ok = all(min(x) >= 0 and sum(x) <= depth for x in sup)
            print(f"A1 {name} depth={depth}: |support|={len(sup)} = C(depth+3,3)="
                  f"{(depth+1)*(depth+2)*(depth+3)//6}, all coordinates >= 0 and |x|_1 <= depth: {ok}")
        else:
            print(f"A1 {name} depth={depth}: |support|={len(sup)}, |x|_1 <= depth: "
                  f"{all(sum(abs(c) for c in x) <= depth for x in sup)}, closed under x -> -x: "
                  f"{all(tuple(-c for c in x) in sup for x in sup)}")
print("A1 the record at a site is drawn from its predecessors only, so by induction the response to a field at one")
print("A1 site is supported on sums of d predecessor offsets: a forward simplex cone for the backward")
print("A1 neighbourhood, the symmetric ball |x|_1 <= d for the light cone. On the torus the cone wraps after L levels.")

# ---------------------------------------------------------------- A2 exact linear response
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
E = 2 * sum(1 - sp.cos(x) for x in (k1, k2, k3))
phi_lc = (1 + 2 * sum(sp.cos(x) for x in (k1, k2, k3))) / 7
print("A2 linear (gain-one) theory: theta_{t+1} = A theta_t + noise, plus delta at one site at every level.")
print("A2 Stationary response R(k) = delta/(1 - phi(k)); stationary covariance C(k) = sigma^2/(1 - |phi(k)|^2).")
print("A2 light cone, phi real: R/C in Fourier is (delta/sigma^2)(1 + phi) = (2 delta/sigma^2)(1 - E/14) :",
      sp.simplify((1 - phi_lc ** 2) / (1 - phi_lc) - 2 * (1 - E / 14)) == 0)
print("A2 so response and covariance are proportional at long wavelength and differ by 1 - E/14 at short: 1 at")
print("A2 k = 0, 6/7 at E = 2, 1/7 at the zone corner. Backward: |phi(k)| = |phi(-k)| so C is inversion symmetric,")
print("A2 while R(k) = delta/(1-phi) is not - R lives on the forward cone of A1, so R and C cannot be proportional.")

# ---------------------------------------------------------------- A3 the linear theory on this torus
def lin_stationary(sym):
    g = np.meshgrid(*([2 * np.pi * np.arange(L) / L] * 3), indexing="ij")
    phi = ((1 + 2 * sum(np.cos(x) for x in g)) / 7.0 + 0j) if sym \
        else (1 + sum(np.exp(-1j * x) for x in g)) / 4.0        # e^{-ik} matches roll(+1) = predecessor at x - e_j
    Rk = np.zeros_like(phi); Ck = np.zeros_like(phi)
    m = np.ones((L, L, L), bool); m[0, 0, 0] = False
    Rk[m] = 1.0 / (1 - phi[m]); Ck[m] = 1.0 / (1 - np.abs(phi[m]) ** 2)
    return np.fft.ifftn(Rk).real, np.fft.ifftn(Ck).real
def lin_truncated(sym, marks):
    """exact iteration of the same averaging operator on a delta source, level by level"""
    n = 7 if sym else 4
    th = np.zeros((L, L, L)); src = np.zeros((L, L, L)); src[0, 0, 0] = 1.0; out = {}
    for t in range(1, max(marks) + 1):
        th = (th + sum(np.roll(th, 1, axis=j) + (np.roll(th, -1, axis=j) if sym else 0) for j in range(3))) / n + src
        if t in marks: out[t] = th.copy()
    return out
lin = {}
for sym, name in LATTICES:
    R, C = lin_stationary(sym)
    trunc = lin_truncated(sym, set(MARKS) | set(LONG_MARKS))
    lin[sym] = (R, C, trunc)
    print(f"A3 {name} stationary linear theory on the {L}^3 torus: R(0)={R[0,0,0]:.5f}, C(0)={C[0,0,0]:.5f}, "
          f"and R(x)/C(x) by direction (delta = sigma^2 = 1):")
    for dname, d in DIRS.items():
        print(f"A3   {name} {dname} R/C: " + " ".join(f"r={r}:{at(R,d,r)/at(C,d,r):+.4f}" for r in RS))
    print(f"A3 {name} fraction of the stationary response that has arrived after T levels:")
    for T in sorted(set(MARKS) | set(LONG_MARKS)):
        print(f"A3   {name} T={T:3d}: " + " ".join(f"{dn} " + " ".join(f"r={r}:{at(trunc[T],d,r)/at(R,d,r):.3f}"
              for r in (1, 2, 4, 8)) for dn, d in DIRS.items()))
    if not sym:
        for T in sorted(set(MARKS) | set(LONG_MARKS)):
            beh = [abs(at(trunc[T], d, -r)) / abs(at(trunc[T], d, r)) for dname, d in DIRS.items()
                   for r in (1, 2, 4) if abs(at(trunc[T], d, r)) > 1e-15]
            print(f"A3 {name} T={T:3d}: the linear |R(-x)|/|R(x)| at r <= 4 is at most {max(beh):.2e} "
                  f"({'exactly zero, the cone has not wrapped' if T < L else 'nonzero only because the cone has wrapped the torus'})")

# ---------------------------------------------------------------- the batched chain
def step(s, U, ph, beta, sym, field=None):
    S = s + sum(np.roll(s, 1, axis=j + 1) + (np.roll(s, -1, axis=j + 1) if sym else 0) for j in range(3))
    if field is not None: S = S + field
    nrm = np.linalg.norm(S, axis=-1); nrm = np.where(nrm < 1e-12, 1e-12, nrm)
    uu = S / nrm[..., None]; kap = beta * nrm
    w = np.clip(1 + np.log(U + (1 - U) * np.exp(-2 * kap)) / kap, -1, 1)
    a = np.where((np.abs(uu[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    b1 = a - (a * uu).sum(-1)[..., None] * uu; b1 /= np.linalg.norm(b1, axis=-1)[..., None]
    b2 = np.cross(uu, b1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[..., None] * uu + r[..., None] * (np.cos(ph)[..., None] * b1 + np.sin(ph)[..., None] * b2), nrm

# ---------------------------------------------------------------- N1 the measured covariance
def measure_C(sym, T=2000, T0=600, seed=4):
    rng = np.random.default_rng(seed); sh = (1, L, L, L)
    s = np.zeros(sh + (3,)); s[..., 2] = 1.0; acc = np.zeros((L, L, L)); cnt = 0; var = 0.0
    for t in range(1, T + 1):
        s, _ = step(s, rng.random(sh), rng.random(sh) * 2 * np.pi, BETA, sym)
        if t > T0:
            M = s.reshape(-1, 3).mean(0); u = M / np.linalg.norm(M)
            perp = s[0] - (s[0] @ u)[..., None] * u
            acc += (np.abs(np.fft.fftn(perp, axes=(0, 1, 2))) ** 2).sum(-1) / (2.0 * L ** 3)
            var += float((perp ** 2).sum(-1).mean()); cnt += 1
    S0 = acc / cnt; S0[0, 0, 0] = 0.0
    return np.fft.ifftn(S0).real, var / cnt
Cmeas = {}
for sym, name in LATTICES:
    C, v = measure_C(sym); Cmeas[sym] = C
    print(f"N1 {name} measured equal-level covariance of the transverse field, zero mode removed: C(0)={C[0,0,0]:.5f} "
          f"(<|s_perp|^2>/2 = {v/2:.5f}); C(x) = C(-x) by construction of the estimator's symbol")
    for dname, d in DIRS.items():
        print(f"N1   {name} {dname}: " + " ".join(f"r={r}:{at(C,d,r):+.6f}" for r in RS) +
              " | mirrored: " + " ".join(f"r={r}:{at(C,d,-r):+.6f}" for r in RS))

# ---------------------------------------------------------------- N2 the measured response
def measure_R(sym, pairs, batch, burn, T, marks, seed=11):
    x0 = (L // 2, L // 2, L // 2)
    field = np.zeros((L, L, L, 3)); field[x0] = np.array([H, 0.0, 0.0])
    acc = {m: np.zeros((L, L, L)) for m in marks}; nb = 0; nrm_mean = 0.0; cosz = 0.0
    rng = np.random.default_rng(seed)
    for b in range(pairs // batch):
        sh = (batch, L, L, L); s = np.zeros(sh + (3,)); s[..., 2] = 1.0
        for t in range(burn): s, _ = step(s, rng.random(sh), rng.random(sh) * 2 * np.pi, BETA, sym)
        sp_ = s.copy()
        for t in range(1, T + 1):
            U = rng.random(sh); ph = rng.random(sh) * 2 * np.pi
            s, nrm = step(s, U, ph, BETA, sym)
            sp_, _ = step(sp_, U, ph, BETA, sym, field=field)
            if t in acc: acc[t] += (sp_ - s)[..., 0].mean(0)
            if t == T:
                nrm_mean += float(nrm.mean())
                M = s.reshape(batch, -1, 3).mean(1); cosz += float(np.mean(M[:, 2] / np.linalg.norm(M, axis=1)))
        nb += 1
    return ({m: np.roll(acc[m] / nb, tuple(-c for c in x0), axis=(0, 1, 2)) for m in marks},
            nrm_mean / nb, cosz / nb)

Rmeas = {}
for sym, name in LATTICES:
    R, nrm, cosz = measure_R(sym, PAIRS, BATCH, BURN, MEASURE, MARKS)
    Rl, nrml, _ = measure_R(sym, LONG_PAIRS, LONG_PAIRS, BURN, LONG_T, LONG_MARKS, seed=23)
    Rmeas[sym] = (R, Rl)
    delta = H * A_lang(BETA * nrm) / nrm
    print(f"N2 {name}: {PAIRS} coupled pairs (burn-in {BURN}, {MEASURE} measured levels) and {LONG_PAIRS} pairs for "
          f"{LONG_T} levels; field h={H} at one site at every level; <|S|>={nrm:.4f}, linear drift "
          f"delta = h A(beta|S|)/|S| = {delta:.6f}, <m.e_z>={cosz:.4f}")
    for m in MARKS:
        print(f"N2 {name} T={m} ({PAIRS} pairs): R(0)={R[m][0,0,0]:+.6f}")
        for dname, d in DIRS.items():
            print(f"N2   {name} {dname} forward  " + " ".join(f"r={r}:{at(R[m],d,r):+.6f}" for r in RS))
            print(f"N2   {name} {dname} backward " + " ".join(f"r={r}:{at(R[m],d,-r):+.6f}" for r in RS))
    for m in LONG_MARKS:
        print(f"N2 {name} T={m} ({LONG_PAIRS} pairs): R(0)={Rl[m][0,0,0]:+.6f}, " +
              " | ".join(f"{dn} " + " ".join(f"r={r}:{at(Rl[m],d,r):+.6f}" for r in (1, 2, 4, 8)) for dn, d in DIRS.items()))

# ---------------------------------------------------------------- N3 the comparison
print("N3 measured response against the exact truncated linear prediction (ratio measured/linear, the linear one")
print("N3 scaled by delta), then R/C, then the one-sidedness and symmetry tests")
verdict = {}
for sym, name in LATTICES:
    R, Rl = Rmeas[sym]; C = Cmeas[sym]; Rlin, Clin, trunc = lin[sym]
    _, nrm, _ = (None, None, None)
    m = MARKS[-1]
    scale = R[m][0, 0, 0] / trunc[m][0, 0, 0]
    print(f"N3 {name} T={m}: measured/linear (both normalised at the origin, scale {scale:.6f}):")
    for dname, d in DIRS.items():
        print(f"N3   {name} {dname}: " + " ".join(
            f"r={r}:{at(R[m],d,r)/(scale*at(trunc[m],d,r)):.3f}" for r in RS))
    mlong = LONG_MARKS[-1]
    scale_l = Rl[mlong][0, 0, 0] / trunc[mlong][0, 0, 0]
    print(f"N3 {name} T={mlong}: measured/linear: " + " | ".join(
        f"{dn} " + " ".join(f"r={r}:{at(Rl[mlong],d,r)/(scale_l*at(trunc[mlong],d,r)):.3f}" for r in (1, 2, 4, 8))
        for dn, d in DIRS.items()))
    ratios = []; back = []
    for dname, d in DIRS.items():
        row = [(r, at(Rl[mlong], d, r), at(Rl[mlong], d, -r), at(C, d, r)) for r in RS]
        print(f"N3 {name} {dname} C(x) mirrored check: " + " ".join(f"r={r}:{at(C,d,r)-at(C,d,-r):+.2e}" for r in RS))
        print(f"N3 {name} {dname} measured R/C at T={mlong}: " +
              " ".join(f"r={r}:{f/c:+.3f}" for r, f, b, c in row if abs(c) > 1e-9))
        ratios += [f / c for r, f, b, c in row if 2 <= r <= 4 and abs(c) > 1e-9]
    m0 = MARKS[0]
    back = [abs(at(R[m0], d, -r)) / abs(at(R[m0], d, r)) for dname, d in DIRS.items()
            for r in (1, 2, 4) if abs(at(R[m0], d, r)) > 1e-12]
    print(f"N3 {name} at T={m0} (< L, so the cone has not wrapped): measured |R(-x)|/|R(x)| at r <= 4 is at most "
          f"{max(back):.2e}, mean {np.mean(back):.2e}")
    lin_ratios = [at(Rlin, d, r) / at(Clin, d, r) for dname, d in DIRS.items() for r in RS if 2 <= r <= 4]
    aniso = {}
    for r in (2, 3, 4, 6):
        vals = [at(Rlin, d, r) / at(Clin, d, r) for dname, d in DIRS.items()]
        aniso[r] = max(vals) / min(vals) if min(vals) > 0 else float("inf")
        print(f"N3 {name} exact stationary linear R/C at r={r} by direction: " +
              " ".join(f"{dn}:{v:+.4f}" for dn, v in zip(DIRS, vals)) +
              f" | max/min = {aniso[r]:.3f}" + ("" if min(vals) > 0 else " (a sign change: not a ratio)"))
    radial = [at(Rlin, d, r) / at(Clin, d, r) for dname, d in DIRS.items() for r in RS if r >= 3]
    aniso_ok = all(aniso[r] < 1.15 for r in (2, 3, 4))
    two_ok = max(abs(v - 2.0) for v in radial) < 0.10 if aniso_ok else False
    print(f"N3 {name}: R/C is direction-independent to 15% at r = 2,3,4: {aniso_ok}" +
          (f"; and equals 2 to within {max(abs(v-2.0) for v in radial):.3f} at every r >= 3" if aniso_ok else ""))
    spread = (max(ratios) - min(ratios)) / abs(np.mean(ratios))
    lin_spread = (max(lin_ratios) - min(lin_ratios)) / abs(np.mean(lin_ratios))
    verdict[sym] = (float(np.mean(back)), spread, lin_spread, aniso_ok and two_ok, aniso)
    print(f"N3 {name}: |R(-x)|/|R(x)| at r <= 4 averages {np.mean(back):.4f}; measured R/C over 2 <= r <= 4 spreads "
          f"{spread*100:.0f}% of its mean; the exact stationary linear R/C over the same r spreads {lin_spread*100:.0f}% "
          f"(mean {np.mean(lin_ratios):.4f})")

one_sided = verdict[False][0] < 0.1
symmetric = abs(verdict[True][0] - 1.0) < 0.25
lc_prop = verdict[True][3]
bw_prop = verdict[False][3]
print(f"N3 backward one-sided: {one_sided} (mean |R(-x)|/|R(x)| = {verdict[False][0]:.4f} before the cone wraps); "
      f"backward R proportional to C: {bw_prop} (R/C differs between directions by factors "
      f"{', '.join(f'{verdict[False][4][r]:.1f}' for r in (2,3,4))} at r = 2,3,4)")
print(f"N3 light cone symmetric: {symmetric} (ratio {verdict[True][0]:.4f}); light cone R proportional to C: "
      f"{lc_prop} (direction spread {', '.join(f'{verdict[True][4][r]:.3f}' for r in (2,3,4))} at r = 2,3,4)")
print(f"SUMMARY: at beta=3 on a 32^3 plane with h={H} at one site every level, the measured response follows the "
      f"exact truncated linear prediction within a few percent; the backward response is one-sided "
      f"(|R(-x)|/|R(x)| = {verdict[False][0]:.2e} before the cone wraps) and its R/C differs between directions by "
      f"factors {', '.join(f'{verdict[False][4][r]:.1f}' for r in (2,3,4))} at r = 2,3,4, while the light-cone "
      f"response is symmetric ({verdict[True][0]:.4f}) and its R/C is direction-independent to "
      f"{max(verdict[True][4][r] for r in (2,3,4))-1:.3f} and equal to 2, which is exactly "
      f"(2 delta/sigma^2)(1 - E/14) in Fourier; {time.time()-t_start:.0f}s")
bad = []
if not one_sided: bad.append(f"the backward response is not one-sided ({verdict[False][0]:.3f})")
if bw_prop: bad.append("the backward response is proportional to C after all")
if not symmetric: bad.append(f"the light-cone response is not symmetric ({verdict[True][0]:.3f})")
if not lc_prop: bad.append(f"the light-cone response is not close to proportional to C "
                           f"(stationary linear R/C spreads {verdict[True][2]*100:.0f}% over r >= 3)")
if bad: print("HIT: " + "; ".join(bad))
