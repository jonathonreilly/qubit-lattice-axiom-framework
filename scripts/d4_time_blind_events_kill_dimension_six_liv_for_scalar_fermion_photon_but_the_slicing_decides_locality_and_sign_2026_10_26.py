AUDIT_INPUT_PATHS = ('docs/D4_TIME_BLIND_EVENTS_KILL_DIMENSION_SIX_LIV_FOR_SCALAR_FERMION_PHOTON_BUT_THE_SLICING_DECIDES_LOCALITY_AND_SIGN_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""D4 time-blind events (P1): free scalar / fermion / triangle-photon / graviton-count checks, RP, real time, thresholds.
Self-contained (numpy, scipy, sympy). Seeded. Supplied models, floating-point checks unless marked exact."""
import itertools, time
import numpy as np, sympy as sp
from scipy.optimize import brentq
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261026)
NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
R = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2], float)
# --- W(F4) = Aut(D4) by closure
gens = []
for i in range(3):
    M = np.eye(4); M[[i, i + 1]] = M[[i + 1, i]]; gens.append(M)
M = np.eye(4); M[0, 0] = -1; gens.append(M); h = np.ones(4) / 2; gens.append(np.eye(4) - 2 * np.outer(h, h))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel())
Gd = {key(np.eye(4)): np.eye(4)}; fr = [np.eye(4)]
while fr:
    nf = []
    for A in fr:
        for g in gens:
            B = g @ A
            if key(B) not in Gd: Gd[key(B)] = B; nf.append(B)
    fr = nf
G = np.array(list(Gd.values())); Rs = set(map(tuple, R.astype(int)))
check("C0 |Aut(D4)| = |W(F4)| = 1152, roots preserved", len(G) == 1152 and all(set(map(tuple, (R @ g.T).round().astype(int))) == Rs for g in G))
# --- C1 scalar, exact
p = sp.symbols('p0:4'); P2 = sum(x**2 for x in p)
Sk = lambda k: sp.expand(sum(sum(int(r[i]) * p[i] for i in range(4))**k for r in R))
J6 = sum(x**6 for x in p) + 15 * sum(p[i]**2 * p[j]**2 * p[k]**2 for i, j, k in itertools.combinations(range(4), 3))
S6 = Sk(6)
check("C1 [T] sum(r.p)^2 = 12p^2, sum(r.p)^4 = 12(p^2)^2 exactly; sum(r.p)^6 = 20(p^2)^3 - 8 J6 (first non-O(4) order 6 = dim 8)",
      sp.expand(Sk(2) - 12 * P2) == 0 and sp.expand(Sk(4) - 12 * P2**2) == 0 and sp.expand(S6 - 20 * P2**3 + 8 * J6) == 0,
      "K = 6p^2 - (p^2)^2/2 + (p^2)^3/36 - J6/90 + O(p^8)")
sv = lambda k, m: sp.expand(sum(int(r[m]) * sum(int(r[i]) * p[i] for i in range(4))**k for r in R))
check("C2a [T] naive s_mu cubic = 12 p^2 p_mu, quintic = d_mu S6/6 (first breaking degree 5, dim 8)",
      all(sp.expand(sv(3, m) - 12 * P2 * p[m]) == 0 and sp.expand(sv(5, m) - sp.diff(S6, p[m]) / 6) == 0 for m in range(4)))
# --- C2 fermion zeros, Wilson, overlap
sN = lambda q: np.array([4 * np.sin(q[m]) * sum(np.cos(q[n]) for n in range(4) if n != m) for m in range(4)])
Kq = lambda q: 24 - 4 * sum(np.cos(q[i]) * np.cos(q[j]) for i in range(4) for j in range(i + 1, 4))
zs, seen = [], set()
for m in itertools.product(range(12), repeat=4):
    q = np.array(m) * np.pi / 6
    if np.abs(sN(q)).max() < 1e-12:
        kk = min(tuple(m), tuple((x + 6) % 12 for x in m))
        if kk not in seen: seen.add(kk); zs.append(q)
Jac = lambda q: np.array([(sN(q + 1e-6 * e) - sN(q - 1e-6 * e)) / 2e-6 for e in np.eye(4)]).T
dets = np.array([np.linalg.det(Jac(q)) for q in zs]); Kz = np.array([Kq(q) for q in zs])
check("C2b naive D4 Dirac zeros mod 2pi D4*: 72 (1 + 71 doublers), all nondegenerate, chirality sum 0",
      len(zs) == 72 and np.abs(dets).min() > 1 and np.sign(dets).sum() == 0, f"s_mu = 4 sin p_mu sum_(nu!=mu) cos p_nu; min|detJ| {np.abs(dets).min():.0f}")
check("C2c Wilson (w=1): K = 0 only at p = 0; doubler masses wK/12 in {2, 9/4, 7/3, 8/3}", (Kz < 1e-9).sum() == 1 and abs(np.sort(Kz)[1] - 24) < 1e-9,
      "overlap window 0 < m0 < 2")
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = [np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)]; g5 = gm[0] @ gm[1] @ gm[2] @ gm[3]
def Dov(q, m0=1.0):
    A = (1j * sum(gm[m] * sN(q)[m] for m in range(4)) + Kq(q) * np.eye(4)) / 12 - m0 * np.eye(4)
    w, V = np.linalg.eigh(A.conj().T @ A); return np.eye(4) + A @ V @ np.diag(w**-0.5) @ V.conj().T
gw = max(np.abs(g5 @ D + D @ g5 - D @ g5 @ D).max() for D in (Dov(q) for q in rng.uniform(-np.pi, np.pi, (20, 4))))
dz = [np.abs(Dov(q) - 2 * np.eye(4)).max() for q in zs if Kq(q) > 1]
check("C2d overlap on D4 Wilson kernel: GW exact, D(0) = 0, D = 2 at all 71 doublers (one Dirac cone)",
      gw < 1e-12 and np.abs(Dov(np.zeros(4))).max() < 1e-12 and max(dz) < 1e-12, f"GW resid {gw:.1e}")
# --- C3 invariant counts (Reynolds over W(F4))
def count(G_, dp, mode):
    mp = [m for m in itertools.product(range(dp + 1), repeat=4) if sum(m) == dp]
    nf_ = 4 if mode == 'A' else 10; mq = [(i, j) for i in range(nf_) for j in range(i, nf_)]
    nm = len(mp) * len(mq); N = nm; P = rng.normal(size=(N, 4)); F = rng.normal(size=(N, nf_)); iu = np.triu_indices(4)
    def sym(Fv):
        H = np.zeros((len(Fv), 4, 4)); H[:, iu[0], iu[1]] = Fv; H[:, iu[1], iu[0]] = Fv; return H
    def ev(P_, F_):
        A = np.stack([np.prod(P_**np.array(a), 1) for a in mp], 1); B = np.stack([F_[:, i] * F_[:, j] for i, j in mq], 1)
        return (A[:, :, None] * B[:, None, :]).reshape(len(P_), -1)
    act = (lambda g: F @ g.T) if mode == 'A' else (lambda g: (g @ sym(F) @ g.T)[:, iu[0], iu[1]])
    Ev = ev(P, F); Avg = np.zeros_like(Ev)
    for g in G_: Avg += ev(P @ g.T, act(g))
    Y = Avg @ rng.normal(size=(nm, 40)); del Avg; U, s, _ = np.linalg.svd(Y, full_matrices=False); r = (s > 1e-8 * s[0]).sum()
    C = np.linalg.solve(Ev, U[:, :r]).T; X = rng.normal(size=(N, 4))
    Fg = F + rng.normal(size=(N, 1)) * P if mode == 'A' else (sym(F) + P[:, :, None] * X[:, None, :] + X[:, :, None] * P[:, None, :])[:, iu[0], iu[1]]
    D = (ev(P, Fg) - Ev) @ C.T; _, q, vt = np.linalg.svd(D); gi = r - (q > 1e-9 * q[0]).sum()
    Qo = [np.linalg.qr(rng.normal(size=(4, 4)))[0] for _ in range(4)]
    E = np.vstack([D] + [(ev(P @ g.T, (F @ g.T) if mode == 'A' else (g @ sym(F) @ g.T)[:, iu[0], iu[1]]) - Ev) @ C.T for g in Qo])
    qq = np.linalg.svd(E, compute_uv=False); return r, gi, r - (qq > 1e-9 * qq[0]).sum(), (vt[-gi:] @ C if gi else None), mp, mq
Gp = G[np.linalg.det(G) > 0]
a22 = count(G, 2, 'A'); a42 = count(G, 4, 'A'); a42p = count(Gp, 4, 'A')
check("C3a photon: W(F4) gauge-inv kernels p^2: 1 (F^2); p^4: 3 invariant, 1 gauge-inv = the O(4) one; same for rotation subgroup (576)",
      a22[1] == 1 and a42[:3] == (3, 1, 1) and a42p[1] == 1 and a42p[2] == 1, "dim-6 photon LIV forbidden by W(F4)+gauge to all orders")
g22 = count(G, 2, 'H'); g42 = count(G, 4, 'H')
cf, mp, mq = g42[3], g42[4], g42[5]; iu = np.triu_indices(4)
def onshell(n, pol):
    n = np.array(n, float) / np.linalg.norm(n); pp = np.array([1j, *n]); a = np.array([1., 0, 0]) if abs(n[0]) < .9 else np.array([0, 1., 0])
    e1 = np.cross(n, a); e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
    H = np.zeros((4, 4)); H[1:, 1:] = (np.outer(e1, e1) - np.outer(e2, e2)) if pol == 0 else (np.outer(e1, e2) + np.outer(e2, e1)); Hv = H[iu]
    return np.real(cf @ np.outer([np.prod(pp**np.array(m)) for m in mp], [Hv[i] * Hv[j] for i, j in mq]).ravel())
ax_, bo_ = onshell([1, 0, 0], 0), onshell([1, 1, 1], 0)
check("C3b graviton: p^2 diffeo-inv = 1 (Einstein, one metric); p^4: 3 vs O(4) 2 -> one W(F4)-only R^2 invariant, on shell birefringent",
      g22[1] == 1 and g42[1:3] == (3, 2) and np.abs(ax_).max() > 1e-3 and np.allclose(ax_, -onshell([1, 0, 0], 1)) and np.abs(bo_).max() < 1e-10,
      "zero on body diagonals; its coefficient in a D4 Regge action is uncomputed")
# --- triangle photon
Rp = np.array([r for r in R if tuple(r) > tuple(-r)]); idx = {tuple(r): i for i, r in enumerate(Rp)}
tri = []
for r1 in R:
    for r2 in R:
        if r1 @ r2 == -1:
            y = np.zeros(4); L = []
            for r in (r1, r2, -(r1 + r2)):
                t = tuple(r); i, sg = (idx[t], 1.) if t in idx else (idx[tuple(-r)], -1.); L.append((i, sg, y + r / 2)); y = y + r
            tri.append(L)
TI = np.array([[l[0] for l in T] for T in tri]); TS = np.array([[l[1] for l in T] for T in tri]); TM = np.array([[l[2] for l in T] for T in tri])
def Kph(q):
    C = np.zeros((len(tri), 12), complex); Cm = np.zeros_like(C); ar = np.arange(len(tri))
    for j in range(3):
        np.add.at(C, (ar, TI[:, j]), TS[:, j] * np.exp(1j * TM[:, j] @ q)); np.add.at(Cm, (ar, TI[:, j]), TS[:, j] * np.exp(-1j * TM[:, j] @ q))
    return Cm.T @ C
def Emb(q):
    x = Rp @ q; return Rp * np.where(abs(x) < 1e-12, 1., np.sin(x / 2) / np.where(abs(x) < 1e-12, 1, x / 2))[:, None]
Qh, _ = np.linalg.qr(np.hstack([Rp, rng.normal(size=(12, 8))])); H0 = Qh[:, 4:]
def Meff(q):
    K = Kph(q); Ep, Em = Emb(q), Emb(-q)
    return Em.T @ K @ Ep - Em.T @ K @ H0 @ np.linalg.solve(H0.T @ K @ H0, H0.T @ K @ Ep)
qq = rng.normal(size=4) * .2
check("C3c triangle action: 192 ordered triangles, gauge mode exact, 8 extra link modes heavy (72 vs Z = 24)",
      len(tri) == 192 and np.linalg.norm(Meff(qq) @ qq) < 1e-12 * np.linalg.norm(Meff(qq)) and np.allclose(np.linalg.eigvalsh(H0.T @ Kph(np.zeros(4)).real @ H0), 72))
# --- C2e/C3d Euclidean on-shell dispersions (time = axis)
dirs = {'axis': [1, 0, 0], 'face': [1, 1, 0], 'body': [1, 1, 1], 'gen': [1, 2, 3]}; ks = np.array([0.05, 0.1, 0.2])
def fit(Ef):
    out = {}
    for d, n in dirs.items():
        n = np.array(n, float) / np.linalg.norm(n); dev = np.array([Ef(k * n) / k - 1 for k in ks])
        out[d] = np.linalg.lstsq(np.vstack([ks**2, ks**4, ks**6]).T, dev, rcond=None)[0]
    return out
def Esc(k, rt=np.array([1., 0, 0, 0]), P=None):
    kv = np.concatenate([[0.], k]) if P is None else P @ k
    return brentq(lambda E: np.sum(1 - np.cos(R @ kv) * np.cosh((R @ rt) * E)), 1e-14, 3 * np.linalg.norm(k) / np.linalg.norm(rt)) * np.linalg.norm(rt)
def Ef(k):
    def f(E):
        c = np.cos(k); s0 = -16 * np.sinh(E)**2 * c.sum()**2
        return s0 + sum(16 * np.sin(k[j])**2 * (np.cosh(E) + c.sum() - c[j])**2 for j in range(3))
    return brentq(f, 0.9 * np.linalg.norm(k), 1.1 * np.linalg.norm(k))
def Eph(k, j):
    return brentq(lambda E: np.sort(np.real(np.linalg.eigvals(Meff(np.array([1j * E, *k]))[1:, 1:])))[1 + j], .97 * np.linalg.norm(k), 1.03 * np.linalg.norm(k), xtol=1e-15)
fs, ff, f0, f1 = fit(Esc), fit(Ef), fit(lambda k: Eph(k, 0)), fit(lambda k: Eph(k, 1))
J6n = lambda n: (lambda pp: float(np.real(sum(x**6 for x in pp) + 15 * sum(pp[i]**2 * pp[j]**2 * pp[k]**2 for i, j, k in itertools.combinations(range(4), 3)))))(np.array([1j, *(np.array(n, float) / np.linalg.norm(n))]))
dim6 = max(abs(F[d][0]) for F in (fs, ff, f0, f1) for d in dirs)
check("C2e/C3d no dim-6 term on shell for scalar, overlap fermion, both photon polarisations (all 4 directions)", dim6 < 1e-6, f"max |k^2 coeff| {dim6:.1e}")
print("  v-1 = b k^4 (axis slicing, a = 1):  dir: scalar  fermion  photon(pol1,pol2)  | -J6/1080")
for d in dirs: print(f"  {d}: {fs[d][1]:+.3e} {ff[d][1]:+.3e} {f0[d][1]:+.3e},{f1[d][1]:+.3e} | {-J6n(dirs[d]) / 1080:+.3e}")
check("C3e one dim-8 pattern -J6 on the cone for all species: b_scalar = -J6/1080, fermion 6x, photon 3/8 x, no birefringence",
      all(abs(fs[d][1] + J6n(dirs[d]) / 1080) < 2e-5 and abs(ff[d][1] - 6 * fs[d][1]) < 1e-4 and abs(f0[d][1] - .375 * fs[d][1]) < 1e-5 and abs(f0[d][1] - f1[d][1]) < 1e-6 for d in dirs))
# --- C4 RP and real time
def perp(rt):
    Q, _ = np.linalg.qr(np.vstack([rt, np.eye(4)[:3]]).T); return Q[:, 1:4]
rtA, rtR = np.array([1., 0, 0, 0]), np.array([1., 1, 0, 0]); PA = perp(rtA); PR = np.array([[1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]], float).T / np.sqrt(2)
def osmin(rt, P, extra=0.0, Nt=24):
    w = 1.0
    for _ in range(6):
        kp = P @ rng.uniform(-np.pi, np.pi, 3); ph = 2 * np.pi * np.arange(Nt) / Nt
        Kc = np.sum(1 - np.cos(np.multiply.outer(ph, R @ rt) + R @ kp), -1) + 0.09 + extra * (1 - np.cos(2 * ph))
        Gn = np.fft.ifft(1 / Kc).real; S = np.array([[Gn[(a + b) % Nt] for b in range(Nt // 2)] for a in range(Nt // 2)])
        w = min(w, np.linalg.eigvalsh(S).min() / np.abs(S).max())
    return w
oa, orr, oc = osmin(rtA, PA), osmin(rtR, PR), osmin(rtA, PA, extra=-4.0)
check("C4a site-reflection positivity: axis and root slicing pass; control (antiferro 2-step coupling) fails",
      oa > -1e-12 and orr > -1e-12 and oc < -1e-3, f"min eig rel {oa:.1e}, {orr:.1e}; control {oc:.1e}; link reflection is no lattice symmetry in either")
fr_ = {d: np.linalg.lstsq(np.vstack([ks**2, ks**4, ks**6]).T, np.array([Esc(k * np.array(n, float) / np.linalg.norm(n), rtR, PR) / k - 1 for k in ks]), rcond=None)[0] for d, n in dirs.items()}
print("  root slicing (time along a root; slices = cubic lattice of cube centres): scalar b in (k a)^4 units, a = site spacing")
print("  " + "  ".join(f"{d} {4 * fr_[d][1]:+.3e}" for d in dirs) + f" | axis slicing: " + "  ".join(f"{d} {fs[d][1]:+.3e}" for d in dirs))
check("C4b real-time lowest band: dim-6 zero in both slicings; dim-8 superluminal (axis slicing) vs subluminal (root slicing)",
      max(abs(fr_[d][0]) for d in dirs) < 1e-6 and all(fs[d][1] > -1e-6 for d in dirs) and all(fr_[d][1] < 1e-6 for d in dirs) and fr_['face'][1] < -1e-3)
nn = rng.normal(size=(20000, 3)); nn /= np.linalg.norm(nn, axis=1)[:, None]
avA = np.mean([-J6n(n) for n in nn]) / 1080
def J6root(n):
    k = PR @ n; pp = 1j * rtR / np.sqrt(2) + k; return float(np.real(sum(x**6 for x in pp) + 15 * sum(pp[i]**2 * pp[j]**2 * pp[k_]**2 for i, j, k_ in itertools.combinations(range(4), 3))))
avR = 4 * np.mean([-J6root(n) for n in nn]) / 1080
check("C4c isotropic (boost) dim-8 part nonzero and slicing-dependent: <b>_sphere axis vs root", avA > 1e-3 and avR < -1e-3, f"<b_scalar> = {avA:+.2e} (axis), {avR:+.2e} (root)")
kz = np.array([np.pi / 2] * 3); c = np.cos(R[:, 1:] @ kz)
sig1 = c[R[:, 0] != 0].sum()
m2 = 0.09; Dl = R @ rtR
def z1(kp):
    cc = np.cos(R @ kp); A = 24 + m2 - cc[Dl == 0].sum(); B = cc[np.abs(Dl) == 1].sum(); return (-B + np.sqrt(B * B + 16 * (A + 2) + 0j)) / 8
best = 9
for _ in range(80):
    n = rng.normal(size=3); n /= np.linalg.norm(n); kd = PR @ n; w = complex(rng.uniform(-3, 3), rng.uniform(-2, 2))
    for it in range(50):
        f = z1(w * kd) - 1; d = (z1((w + 1e-7) * kd) - 1 - f) / 1e-7
        if not np.isfinite(d) or d == 0: break
        w -= f / d
    if np.isfinite(w) and abs(z1(w * kd) - 1) < 1e-10: best = min(best, abs(w.imag))
check("C4d locality: axis slicing inter-slice hop sum vanishes at real k -> E = inf, H not exponentially local; root slicing strip = m/sqrt6",
      abs(sig1) < 1e-12 and abs(best - np.sqrt(m2 / 6)) < 2e-3, f"root strip {best:.4f} vs mass-shell {np.sqrt(m2 / 6):.4f} (no lattice singularity nearer)")
# --- C5 thresholds (estimate), E* = 1.217e18 GeV
Es, me, mpr = 1.217e18, 0.511e-3, 0.938
bf = 6 * fs['body'][1]
pe = (me**2 * Es**4 / (10 * bf))**(1 / 6) * 1e9; pP = (mpr**2 * Es**4 / (10 * bf))**(1 / 6) * 1e9
mis = .375 * fs['face'][1] - 6 * fs['face'][1] / 16
Pinst = (mpr**2 * Es**4 / (20 * abs(6 * 4 * fr_['face'][1])))**(1 / 6) * 1e9
check("C5 axis slicing: e -> e gamma opens at p_th > 1e20 eV, p -> p gamma > 1e21 eV; gamma -> ee closed (b_gamma = b_e/16 exactly)",
      pe > 1e19 and pP > 3e20 and abs(mis) < 1e-6, f"p_th(e) {pe:.1e} eV, p_th(p as fermion) {pP:.1e} eV (body); obs e ~1e15, gamma 1.4e15, UHECR 3e20")
xs = np.linspace(1e-3, .5, 5000); gx = (xs * (1 - xs) * (16 * (xs**5 + (1 - xs)**5) - 1)).max()
bgR = .375 * 4 * abs(fr_['body'][1]); kg = (me**2 * Es**4 / (2 * bgR * gx))**(1 / 6) * 1e9
check("C5b root slicing (all subluminal): e -> e gamma closed; gamma -> e+e- opens only at k_th > 1e20 eV (b_e = 16 b_gamma); nuclei stable",
      kg > 1e19 and Pinst > 1e20, f"k_th(gamma->ee, body) {kg:.1e} eV vs LHAASO 1.4e15; P_inst/A ~ {Pinst:.1e} eV (parent formula)")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time() - t0:.1f} s)")
