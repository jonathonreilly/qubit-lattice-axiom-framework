AUDIT_INPUT_PATHS = ('docs/D4_ROOT_SLICED_FERMIONS_HAVE_NO_POSITIVE_SLICE_TRANSFER_AND_THE_UNITARY_WALK_LOSES_DIMENSION_SIX_PROTECTION_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""D4 fermion positivity under root slicing: (A) twisted/any slice-local reflection, Theta-independent pole test,
(B) modified W(F4) and time-projector fermions, (C) unitary real-time walk on the root-sliced D4 events.
Self-contained (numpy/scipy). Seeded. Supplied free models; float diagnostics plus exact group counts."""
import itertools, time
import numpy as np, scipy.linalg as sl
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261026)
NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
R = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2], float)
S2 = np.array([v for v in itertools.product(range(-2, 3), repeat=4) if sum(np.square(v)) == 4 and sum(v) % 2 == 0], float)
rt = np.array([1., 1, 0, 0]); E4 = np.eye(4)
# ---- C0 groups and quartic invariant counts (exact: character average of Sym^4)
gens = []
for i in range(3):
    M = np.eye(4); M[[i, i + 1]] = M[[i + 1, i]]; gens.append(M)
M = np.eye(4); M[0, 0] = -1; gens.append(M); h = np.ones(4) / 2; gens.append(np.eye(4) - 2 * np.outer(h, h))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); D = {key(E4): E4}; fr = [E4]
while fr:
    nf = []
    for A in fr:
        for g in gens:
            B = g @ A
            if key(B) not in D: D[key(B)] = B; nf.append(B)
    fr = nf
G = np.array(list(D.values())); St = np.array([A for A in G if np.allclose(A @ rt, rt)])
St2 = np.array([A for A in G if np.allclose(np.abs(A @ rt - 0), np.abs(rt)) and (np.allclose(A @ rt, rt) or np.allclose(A @ rt, -rt))])
Qp = np.linalg.qr(np.vstack([rt, E4[:3]]).T)[0][:, 1:]          # orthonormal basis of the slice
def sym4(H):
    p = [np.trace(np.linalg.matrix_power(H, k), axis1=1, axis2=2) for k in (1, 2, 3, 4)]
    return int(round(np.mean((p[0]**4 + 6 * p[0]**2 * p[1] + 3 * p[1]**2 + 8 * p[0] * p[2] + 6 * p[3]) / 24)))
nW, nS3, nS4 = sym4(G), sym4(np.einsum('ai,gab,bj->gij', Qp, St, Qp)), sym4(St2)
check("C0 |W(F4)| = 1152, root stabiliser 48 (cube group of the slice); quartic invariants: W(F4) on R^4 = 1, stabiliser on the slice = 2",
      len(G) == 1152 and len(St) == 48 and nW == 1 and nS3 == 2, f"stabiliser of +-r_t on R^4: {nS4} (t^4, t^2 k^2, (k^2)^2, sum k^4)")
# ---- A1 isometries x -> A x + c (A^2 = 1, A r_t = -r_t) mapping slice n to K - n: site (K even) vs link (K odd)
box = [np.array(c, float) for c in itertools.product(range(-3, 4), repeat=4) if sum(c) % 2 == 0]
link, site, pure_link, LA = 0, 0, 0, []
s_ref = E4 - np.outer(rt, rt)
for A in G:
    if not (np.allclose(A @ A, E4) and np.allclose(A @ rt, -rt)): continue
    Ks = {int(c @ rt) % 2 for c in box if np.allclose(A @ c, -c)}
    site += (0 in Ks); link += (1 in Ks); pure_link += (1 in Ks and np.allclose(A, s_ref)); LA += [A] if 1 in Ks else []
ph = 4 * np.pi * np.arange(256) / 256; k0 = Qp @ np.array([.7, -.4, 1.1])
Gs1 = np.mean(np.exp(-1j * ph / 2) / np.array([np.sum(1 - np.cos(R @ (k0 + f * rt / 2))) + .09 for f in ph]))
mv = min(np.linalg.norm(A @ k0 - k0) for A in LA)
check("A1 [exact] every untwisted reflection perp to the root is site-type; link-type maps exist only twisted, and twisted maps pair k with A k != k",
      pure_link == 0 and link == 7 and mv > .1 and abs(Gs1) > 1e-3,
      f"{site} site-type, {link} link-type, {pure_link} pure link; min|Ak-k| {mv:.2f}; scalar Gram block [[0,X],[X*,0]], |X| = {abs(Gs1):.3f} -> eig +-|X|: twisted RP fails even for the scalar")
# ---- fermion kernels and the slice pole test
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
gt = (gm[0] + gm[1]) / np.sqrt(2); gv = lambda r: np.einsum('m,mab->ab', r, gm)
def cD4(k, w, m, w2=0., b2=0.):        # D(z) = sum_a C[a] z^(a-2), z per slice n = x.r_t
    C = np.zeros((5, 4, 4), complex); C[2] += (2 * w + m + 2 * w2) * E4
    for r in R: C[int(r @ rt) + 2] += np.exp(1j * r @ k) * (gv(r) - w * E4) / 12
    for r in S2: C[int(r @ rt) + 2] += np.exp(1j * r @ k) * (b2 * gv(r) - w2 * E4) / 12
    return C
def cZ4(k, w, m):
    C = np.zeros((5, 4, 4), complex); C[2] += (4 * w + m) * E4
    for mu in (1, 2, 3): C[2] += -w * np.cos(k[mu]) * E4 + 1j * np.sin(k[mu]) * gm[mu]
    C[3] += (gm[0] - w * E4) / 2; C[1] += (-gm[0] - w * E4) / 2; return C
Dz = lambda C, z: sum(C[a] * z**(a - 2) for a in range(5))
def poles(C):
    A = [C[a] for a in range(5)]
    while np.abs(A[-1]).max() < 1e-14: A = A[:-1]
    d = len(A) - 1; L = np.zeros((4 * d, 4 * d), complex); Mb = np.eye(4 * d, dtype=complex)
    L[:4 * (d - 1), 4:] = np.eye(4 * (d - 1)); Mb[4 * (d - 1):, 4 * (d - 1):] = A[d]
    for a in range(d): L[4 * (d - 1):, 4 * a:4 * (a + 1)] = -A[a]
    ev = sl.eigvals(L, Mb); return ev[np.isfinite(ev)]
def resids(C):          # G(n) = sum_j lam_j^n P_j (n >= 1), lam = 1/z over poles |z| > 1
    ev = poles(C); cl = []
    for z in ev[np.abs(ev) > 1 + 1e-9]:
        if not any(abs(z - c) < 1e-6 * abs(c) for c in cl): cl.append(z)
    out = []
    for z in cl:
        rad = min([abs(z - c) for c in ev if abs(z - c) > 1e-6 * abs(z)] + [1.0]) / 3
        th = 2 * np.pi * (np.arange(64) + .5) / 64
        Rj = sum(np.linalg.inv(Dz(C, z + rad * np.exp(1j * t))) * rad * np.exp(1j * t) for t in th) / 64
        out.append((1 / z, -Rj / z))
    return out
cplx = lambda C: max([abs(z.imag) / abs(z) for z in poles(C) if abs(z) > 1 + 1e-9] + [0])
def wrong(rs, Gm, lamw=False):  # 0 iff all (lam) P_j Gamma are Hermitian and of one sign
    ev = np.concatenate([np.linalg.eigvalsh(((l if lamw else 1) * P @ Gm + ((l if lamw else 1) * P @ Gm).conj().T) / 2) for l, P in rs])
    return min(-ev.min(), ev.max()) / np.abs(ev).max()
tk = lambda: Qp @ rng.uniform(-np.pi, np.pi, 3)
kz = [np.r_[0, rng.uniform(-np.pi, np.pi, 3)] for _ in range(4)]
zw = max(wrong(resids(cZ4(k, 1., .3)), gm[0]) for k in kz); zn_s = min(wrong(resids(cZ4(k, 0., .3)), gm[0]) for k in kz)
zn_l = max(wrong(resids(cZ4(k, 0., .3)), gm[0], True) for k in kz)
check("A2 calibration Z^4 (time axis): Wilson r=1 one real pole, definite (T >= 0); naive: real +-lam poles, lam*P definite (link RP) but P not (T indefinite)",
      max(cplx(cZ4(k, 1., .3)) for k in kz) < 1e-9 and zw < 1e-9 and zn_l < 1e-9 and zn_s > .5, f"Wilson {zw:.0e}, naive link {zn_l:.0e}, naive T {zn_s:.2f}")
kt = [tk() for _ in range(8)]
ws = [0., .5, 1., 1.40, 1.42, 1.5, 2., 3.]; cm = {w: max(cplx(cD4(k, w, .3)) for k in kt) for w in ws}
check("A3 D4 Wilson family, root time: slice energies COMPLEX for w < sqrt2 (no Hermitian transfer for ANY Theta), real for w >= sqrt2",
      all(cm[w] > 1e-2 for w in ws if w < 1.41) and all(cm[w] < 1e-9 for w in ws if w > 1.415), " ".join(f"w={w:.2f}:{cm[w]:.1e}" for w in ws))
basis = [np.eye(16)[i].reshape(4, 4) * (1 if j == 0 else 1j) for j in (0, 1) for i in range(16)]
def herm_space(rs):
    A = np.vstack([np.array([np.r_[(P @ B - (P @ B).conj().T).real.ravel(), (P @ B - (P @ B).conj().T).imag.ravel()] for B in basis]).T for l, P in rs])
    u, s, vt = np.linalg.svd(A); n = int(np.sum(s < 1e-9 * s[0])); return [sum(c * B for c, B in zip(v, basis)) for v in vt[len(s) - n:]]
res = {}
for w in (1.5, 2., 3.):
    dims, best = [], 0
    for k in kt[:5]:
        rs = resids(cD4(k, w, .3)); Hs = herm_space(rs); dims.append(len(Hs))
        best = max(best, min(wrong(rs, np.cos(t) * Hs[0] + np.sin(t) * Hs[-1]) for t in np.linspace(0, np.pi, 361)))
    res[w] = (max(dims), best)
check("A4 w >= sqrt2: per-k Hermitian pairings Gamma(k) span 2 dims (g_t and a spin generator); best wrong-sign fraction over all of them stays ~1",
      all(d <= 2 and b > .5 for d, b in res.values()), "; ".join(f"w={w}: dim {d}, best {b:.3f}" for w, (d, b) in res.items()))
kk = 0.02 * tk() / np.pi; gh = {}
for w in (np.sqrt(2), 1.5, 2., 3.):
    rs = resids(cD4(kk, w, .02)); sg = [(np.sqrt(2) * -np.log(abs(l.real)), np.linalg.eigvalsh((P @ gt + (P @ gt).conj().T) / 2)) for l, P in rs]
    light = min(sg, key=lambda x: x[0]); sgn = np.sign(light[1][np.argmax(np.abs(light[1]))])
    gh[w] = sorted(float(round(E, 2)) for E, e in sg if np.sign(e[np.argmax(np.abs(e))]) != sgn)
check("A5 ghosts: with the light branch positive, heavy time branches carry negative norm (1 at w = sqrt2, 2 for w > sqrt2)",
      len(gh[np.sqrt(2)]) == 1 and all(len(gh[w]) == 2 for w in (1.5, 2., 3.)), "ghost E (lattice units): " + "; ".join(f"w={w:.2f} {gh[w]}" for w in gh))
# ---- B: second shell (W(F4)-covariant) random search
found, nreal = 0, 0
for _ in range(50):
    w1, w2, b2 = rng.uniform(0, 4), rng.uniform(-2, 2), rng.uniform(-1, 1); ok = True
    for k in kt[:2]:
        C = cD4(k, w1, .3, w2, b2)
        if cplx(C) > 1e-6: ok = False; break
        rs = resids(C); Hs = herm_space(rs)
        if not Hs or min(wrong(rs, np.cos(t) * Hs[0] + np.sin(t) * Hs[-1]) for t in np.linspace(0, np.pi, 91)) > 1e-6: ok = False; nreal += 1; break
    found += ok
check("B1 W(F4) family with a second shell (w1, w2, b2): no sampled point has a positive slice transfer", found == 0, f"50 points, {nreal} real-pole-but-indefinite, 0 positive")
F = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, np.sqrt(2), 0], [0, 0, 0, np.sqrt(2)]]) / np.sqrt(2); gp = np.einsum('am,mij->aij', F, gm)
Pp, Pm = (E4 + gp[0]) / 2, (E4 - gp[0]) / 2
def cP(q, m, bs, wsp):  # time-projector variant: corners K(q) P-/+, in-slice Wilson-Dirac (spacing sqrt2)
    K = np.prod(np.cos(q / np.sqrt(2))); C = np.zeros((5, 4, 4), complex)
    C[2] = (1 + m) * E4 + sum(wsp * (1 - np.cos(np.sqrt(2) * q[j])) * E4 + 1j * bs * np.sin(np.sqrt(2) * q[j]) * gp[j + 1] for j in range(3))
    C[3], C[1] = -K * Pm, -K * Pp; return C
qs = [rng.uniform(-np.pi, np.pi, 3) for _ in range(6)]
rpP = max(wrong(resids(cP(q, .3, .5, .5)), gp[0]) for q in qs); npl = max(len(resids(cP(q, .3, .5, .5))) for q in qs)
dirs = {'axis': [1, 0, 0], 'face': [1, 1, 0], 'body': [1, 1, 1], 'gen': [.3, .5, .81]}
def disp(f):
    out = {}
    for nm, n in dirs.items():
        n = np.array(n, float) / np.linalg.norm(n); x = np.array([.01, .02, .03]); c = np.polyfit(x**2, [f(t * n) / t for t in x], 2); out[nm] = (c[2], c[1])
    return out
def Elight(C):
    ev = poles(C); z = ev[np.abs(ev) > 1 + 1e-12]; return np.sqrt(2) * np.log(np.abs(z).min())
dP = {wsp: disp(lambda q: Elight(cP(q, 0., .5, wsp))) for wsp in (.5, 1.)}
an = {wsp: d['body'][1] - d['axis'][1] for wsp, d in dP.items()}
Tk0 = resids(cP(np.array([np.pi / np.sqrt(2), .3, .2]), .3, .5, .5))
check("B2 time-projector variant (breaks W(F4) to the stabiliser): T >= 0 holds, but speed = 2 b_s is tuned, dim-6 returns, and T(k) = 0 on a real surface",
      rpP < 1e-9 and npl == 1 and abs(dP[.5]['axis'][0] - 1) < 1e-6 and all(abs(a - 2 / 9) < 1e-3 for a in an.values()) and len(Tk0) == 0,
      "v-1 = c k^2: " + "; ".join(f"ws={wsp}: axis {d['axis'][1]:+.4f} face {d['face'][1]:+.4f} body {d['body'][1]:+.4f}" for wsp, d in dP.items()) + "; body-axis = 2/9 for every ws")
# ---- C: unitary real-time walk on the root-sliced events (each half-tick: 8 corner hops = one D4 slice step)
al = [1j * (gp[0] @ gp[j]) for j in (1, 2, 3)]; ex = [lambda q, j=j: sl.expm(-1j * al[j] * q[j] / np.sqrt(2)) for j in range(3)]
def U(q):
    W1 = ex[0](q) @ ex[1](q) @ ex[2](q); W2 = ex[2](q) @ ex[1](q) @ ex[0](q); return W2 @ W1
un = max(np.abs(U(q).conj().T @ U(q) - E4).max() for q in qs)
def wph(q):
    ph = np.abs(np.angle(np.linalg.eigvals(U(q)))); return ph.min() / np.sqrt(2)
dC = disp(wph); fitC = {nm: d[1] + (1 - sum(np.array(n, float)**4) / np.linalg.norm(n)**4) / 6 for (nm, d), n in zip(dC.items(), dirs.values())}
dE = disp(lambda q: Elight(cD4(Qp @ q, 1., 0.)))
check("C1 unitary walk (palindromic, two half-ticks = the two tilings): unitary, speed 1, dim-6 NONZERO: v - 1 = -(1 - sum n^4)/6 k^2 (zero only on axes)",
      un < 1e-12 and all(abs(d[0] - 1) < 1e-6 for d in dC.values()) and max(abs(v) for v in fitC.values()) < 1e-4 and abs(dC['body'][1]) > 0.1,
      "c: " + " ".join(f"{nm} {d[1]:+.4f}" for nm, d in dC.items()) + f"; unitarity {un:.0e}")
check("C2 control: the Euclidean W(F4) kernel's light branch (w = 1, root slice) has no k^2 term in v - 1 in any direction",
      max(abs(d[1]) for d in dE.values()) < 1e-5 and all(abs(d[0] - 1) < 1e-6 for d in dE.values()), "c: " + " ".join(f"{nm} {d[1]:+.1e}" for nm, d in dE.items()))
print("VERDICT: A FAIL (no slice-local Theta, twisted or not: complex energies w<sqrt2, ghosts w>=sqrt2); B FAIL (W(F4) family: no positive point;")
print("  projector variant positive but dim-6 back + tuned speed + T=0 surface); C works as real-time definition but dim-6 != 0 -> NONE")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time() - t0:.1f} s)")
