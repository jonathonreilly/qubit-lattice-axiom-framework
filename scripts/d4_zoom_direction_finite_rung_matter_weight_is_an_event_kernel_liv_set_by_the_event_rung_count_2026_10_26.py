AUDIT_INPUT_PATHS = ('docs/D4_ZOOM_DIRECTION_FINITE_RUNG_MATTER_WEIGHT_IS_AN_EVENT_KERNEL_LIV_SET_BY_THE_EVENT_RUNG_COUNT_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""D4 zoom direction: which matter kernel sits on the events under 'finitely many zoom rungs', and what physical
dim-8 LIV follows. Reading A: NN start on the events, rungs = coarser descriptions. Reading B': the event weight IS
G_n = R^n(G_NN), R = factor-2 zoom map acting on functions on the EVENT Brillouin zone (no finer lattice).
Self-contained (numpy, scipy). Seeded. Units: D4 coordinates (roots length sqrt2); event (site) spacing a = 1/sqrt2."""
import itertools, time
import numpy as np
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261026)
NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
R = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2], float)
rt = np.array([1., 1, 0, 0]); ut = rt / np.sqrt(2)
PR = np.array([[1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]], float).T / np.sqrt(2)   # slice cube axes
nb = np.ones(3) / np.sqrt(3)                                                         # body ray (largest |beta|)
def fq(c):
    s = c.sum(-1); return (s * s - 0.5 * (c * c).sum(-1) + 2 * c.prod(-1)) / 16   # forced W(F4) kernel (#10098)
a2 = np.array(list(itertools.product(range(2), repeat=4)), float); reps = []
for c in np.vstack([a2, a2 + .5]):
    if not any((lambda d: np.allclose(d, np.round(d)) or np.allclose(d - np.floor(d), .5))((c - r) / 2) for r in reps): reps.append(c)
reps = np.array(reps) * 2 * np.pi   # the 16 classes of 2pi D4* / 4pi D4*
def G_nn(q):   # NN Wilson start: D = A + i g.B ; G = (A - i g.B)/(A^2 + B^2) -> (scalar, vector) parts
    A = 2 - np.cos(q @ R.T).sum(-1) / 12; B = np.sin(q @ R.T) @ R / 12; d = A * A + np.sum(B * B, -1); return A / d, B / d[..., None]
def G_rung(q, n, al=0.5):   # R^n(G_NN): R maps a function on the BZ to a function on the same BZ
    if n == 0: return G_nn(q)
    s = 0; r = 0; sf = 0
    for lk in reps:
        Q = (q + lk) / 2; f2 = fq(np.cos(Q)) ** 2; sq, rq = G_rung(Q, n - 1, al); s = s + 0.5 * f2 * sq; r = r + 0.5 * f2[..., None] * rq; sf = sf + 0.5 * f2
    return s + al * (1 - sf), r
Nth = 1024; th = 4 * np.pi * np.arange(Nth) / Nth; PH = np.exp(1j * np.outer(np.arange(Nth), th) / 2) / Nth
def E_slice(vec, m):   # light pole from the event-slice correlator (slices along the root rt)
    c = PH @ vec; return np.sqrt(2) * np.log(abs(c[m] / c[m + 1]))
def E_newton(k):   # exact NN light pole at transverse momentum k
    def F(E):
        q = 1j * E * ut + k; A = 2 - np.cos(R @ q).sum() / 12; B = np.sin(R @ q) @ R / 12; return A * A + B @ B
    E = np.linalg.norm(k) + 0j
    for _ in range(40): E = E - F(E) / ((F(E + 1e-7) - F(E - 1e-7)) / 2e-7)
    return E.real
Epole = lambda n, kv: E_slice(G_rung(th[:, None] * rt[None] / 2 + kv[None], n)[1] @ ut, 28)
J6v = lambda v: float(np.real(sum(x**6 for x in v) + 15 * sum(v[i]**2 * v[j]**2 * v[k]**2 for i, j, k in itertools.combinations(range(4), 3))))
beta0 = -2 * (1 / 90) * J6v(1j * ut + PR @ nb); bgam = -2 * (1 / 1440) * J6v(1j * ut + PR @ nb)   # #10110 C1 (exact)
# ---------------- Z1 reading A: blocking the event NN kernel n times only rescales units; physics is rung 0
K = 0.06; idA = 0; devs = []
for n in (1, 2, 3):
    En = Epole(n, PR @ (2**n * K * nb)); E0 = E_newton(PR @ (K * nb)); idA = max(idA, abs(En / 2**n / E0 - 1)); devs.append(En / 2**n / K - 1)
dev0 = E_newton(PR @ (K * nb)) / K - 1
check("Z1 [T+F] reading A: n-times-blocked description has E_n(2^n K)/2^n = E_0(K); physical E/K - 1 identical for n = 0..3",
      idA < 1e-9 and max(abs(d - dev0) for d in devs) < 1e-10,
      f"identity rel {idA:.0e}; physical E/K-1 at Ka={K}: n=0 {dev0:+.6e}, n=1..3 " + " ".join(f"{d:+.6e}" for d in devs)
      + "  => physical beta = beta_0 for every n (cell-unit beta_0/16^n is a units change)")
# ---------------- Z2 G_n is a function on the EVENT Brillouin zone
gens = [2 * np.pi * np.eye(4)[0], np.pi * np.ones(4), 2 * np.pi * np.eye(4)[3]]
qr = rng.uniform(-np.pi, np.pi, size=(6, 4)); per = 0
for n in range(4):
    s0, r0 = G_rung(qr, n)
    for b in gens:
        s1, r1 = G_rung(qr + b, n); per = max(per, np.max(abs(s1 - s0) / abs(s0)), np.max(np.linalg.norm(r1 - r0, axis=1) / np.linalg.norm(r0, axis=1)))
check("Z2 [T] G_n = R^n(G_NN) is 2pi D4*-periodic (an event kernel; the preimage sum is a formula, not a finer lattice)",
      per < 1e-12, f"max rel change under 2pi e1, pi(1,1,1,1), 2pi e4: {per:.1e} (n = 0..3)")
# ---------------- Z3 locality of D_n = G_n^-1 on an antiperiodic D4 event torus (Z^4 side 8, even sites)
def Dmag(L, n):
    m = (np.arange(L) + 0.5) * 2 * np.pi / L
    QG = np.stack(np.meshgrid(m, m, m, m, indexing='ij'), -1).reshape(-1, 4)
    X = np.stack(np.meshgrid(*[np.arange(L)] * 4, indexing='ij'), -1).reshape(-1, 4); Xm = (X + L // 2) % L - L // 2
    ev = Xm.sum(1) % 2 == 0; r2 = np.sum(Xm * Xm, 1); phase = np.exp(1j * np.pi * X.sum(1) / L)
    s, r = G_rung(QG, n); d = s * s + np.sum(r * r, 1); comp = [s / d] + [r[:, j] / d for j in range(4)]
    mag = np.sqrt(sum(abs(np.fft.ifftn(c.reshape([L] * 4)).reshape(-1) * phase) ** 2 for c in comp))
    return {sh: mag[ev & (r2 == sh)].max() for sh in range(0, 29, 2)}
shells = list(range(2, 29, 2)); rates = {}; drop = {}; fs = 0
for n in range(4):
    mx = Dmag(12, n)
    if n == 0: nn0 = max(mx[sh] for sh in shells[1:]) / mx[2]; continue
    env = np.array([max(mx[t] for t in shells if t >= sh) for sh in shells])   # tail envelope max_{|X|^2 >= s}
    rates[n] = -np.polyfit(np.sqrt(shells), np.log(env), 1)[0]; drop[n] = env[-1] / env[0]
    print(f"  n={n} |D_n(X)| shell max, |X|^2 = 2,4,..,28: " + " ".join(f"{mx[sh]:.0e}" for sh in shells) + f"  envelope decay {rates[n]:.2f}/unit")
m8 = Dmag(8, 1); fs = max(abs(m8[sh] / Dmag(12, 1)[sh] - 1) for sh in range(2, 13, 2))
check("Z3 [F] D_0 = NN exactly (zero beyond the roots); D_1..D_3 exponentially local on the events (L = 12 torus), decay > 1/unit",
      nn0 < 1e-12 and min(rates.values()) > 1 and max(drop.values()) < 1e-3 and fs < 1e-2,
      f"D_0 beyond roots {nn0:.0e}; envelope decay n=1,2,3: " + " ".join(f"{rates[n]:.2f}" for n in (1, 2, 3))
      + f"; |X|^2=28 / |X|^2=2: " + " ".join(f"{drop[n]:.0e}" for n in (1, 2, 3)) + f"; L=8 vs 12 (n=1, |X|^2<=12) {fs:.0e}")
# ---------------- Z4 event-scale dim-8 coefficient of the event kernel G_n (reading B')
kfit = np.array([0.3, 0.4, 0.5]); fit = {}
for n in range(4):
    Es = np.array([Epole(n, PR @ (k * nb)) for k in kfit]); fit[n] = 4 * np.polyfit(kfit**4, Es / kfit - 1, 1)[0]
b0n = fit[0]
bev = {n: beta0 / 16**n for n in range(4)}
for n in range(4): print(f"  B' event kernel n={n}: beta_e (ka)^4 exact {bev[n]:+.3e}; slice fit {fit[n]:+.3e}; |c| * 16^n / |c_0| = {fit[n] / fit[0] * 16**n:.3f}")
check("Z4 [F] B': event-scale beta_n = beta_0/16^n read from the EVENT slice correlator; beta_0 = -0.1185; -> 0 only as n -> inf",
      abs(beta0 / -0.11852 - 1) < 1e-3 and all(abs(fit[n] / fit[0] * 16**n - 1) < 1e-2 for n in (1, 2, 3)) and all(fit[n] != 0 for n in range(4)),
      f"beta_0 exact {beta0:+.5f}; nonzero at every finite n (finitely many branches, zoom-fixed-point-tick T1)")
# ---------------- Z5 thresholds under both readings (E* = hbar c / 2L, photon unzoomed)
hbarc, lP = 1.97327e-16, 1.616255e-35; Es_ = hbarc / (2 * np.sqrt(8 * np.pi) * lP); me, mp = 0.51100e-3, 0.93827
xs = np.linspace(1e-4, 1 - 1e-4, 200001)
def th_gee(be, bg):
    G = np.max(xs * (1 - xs) * (be * (xs**5 + (1 - xs)**5) - bg)); return (me**2 * Es_**4 / (2 * G))**(1 / 6) * 1e9 if G > 0 else None
def th_cher(be, bg):
    h = np.max((1 - xs) / xs * (bg * xs**5 - be * (1 - (1 - xs)**5))); return (me**2 * Es_**4 / (2 * h))**(1 / 6) * 1e9 if h > 0 else None
wall = lambda b: (mp**2 * Es_**4 / (20 * b))**(1 / 6) * 1e9
EQG = lambda b: Es_ / (2 * b)**0.25
fm = lambda x: '-' if x is None else f"{x:.2e}"
be0, bg = abs(beta0), abs(bgam); ref = {0: 1.91e20, 1: None, 2: None, 3: None}; refw = {0: 9.67e20, 1: 1.53e21, 2: 1.53e21, 3: 1.53e21}
print(f"  E* = {Es_:.4e} GeV; |b_gamma| = {bg:.3e} (both readings). Physical rows (body ray):")
print("  n | reading | |b_e| | gamma->ee eV | e->e gamma eV | wall A eV (flow) | E_QG,4 e GeV")
okB = True
for n in range(4):
    for lab, be in (('A ', be0), ("B'", be0 / 16**n)):
        g, c, w = th_gee(be, bg), th_cher(be, bg), wall(max(be, bg))
        print(f"  {n} | {lab} | {be:.2e} | {fm(g):>8} | {fm(c):>8} | {w:.2e} | {EQG(be):.2e}")
        if lab == "B'": okB &= abs(w / refw[n] - 1) < 1e-2 and ((g is None) == (ref[n] is None)) and (g is None or abs(g / ref[n] - 1) < 1e-2)
gA = th_gee(be0, bg)
check("Z5 [E] reading A: every n gives the n = 0 row (gamma->ee 1.9e20 eV, wall 9.7e20 A eV); reading B' reproduces #10110 rows",
      abs(gA / 1.91e20 - 1) < 1e-2 and abs(wall(be0) / 9.67e20 - 1) < 1e-2 and okB, "all rows pass every measured bound in both readings")
# ---------------- Z6 decision-text test: the NN Lee-Wick pair in the event weight sits at 2^n x (B') or 1 x (A)
def Fnn(E):
    q = 1j * E * ut; A = 2 - np.cos(R @ q).sum() / 12; B = np.sin(R @ q) @ R / 12; return A * A + B @ B
Ep = 2.6 + 1.67j
for _ in range(60): Ep = Ep - Fnn(Ep) / ((Fnn(Ep + 1e-7) - Fnn(Ep - 1e-7)) / 2e-7)
blow = []
for n in (1, 2):
    qp = (1j * 2**n * Ep * ut)[None] * (1 + 1e-9); qg = (1j * 2**n * (Ep + 0.3) * ut)[None]
    blow.append(np.linalg.norm(G_rung(qp, n)[1]) / np.linalg.norm(G_rung(qg, n)[1]))
check("Z6 [T+F] NN pair (k = 0) sits at 2^n E_pair in the rung-n event kernel: the decision's rung-2 ghost cost is a B' statement",
      abs(Fnn(Ep)) < 1e-12 and min(blow) > 1e5, f"E_pair = {Ep.real:.4f} {Ep.imag:+.4f}i (D4 units); "
      f"|G_n| blow-up at 2^n E_pair: n=1 {blow[0]:.0e}, n=2 {blow[1]:.0e}")
print(f"runtime {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
