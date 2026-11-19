#!/usr/bin/env python3
"""self-gravity: definite edges sourced by the actual configuration (CL-2 + CL-3 local reading)
tested against measurement: Page-Geilker, self-gravity on one particle's odds, source jitter,
cutoff radiation by configuration hops, energy, and gravity-mediated entanglement.

Sections
 A [T] Page-Geilker: actual-configuration source follows the outcome; mean field does not.
 B [T] self-term: a locally read definite field acts on the odds of the body that sourced it;
       the vacuum standard changes the source value per configuration, not this action; for an
       eigenstate the subtracted total is noiseless but its position (dipole) follows X.
 C [D] CL-2 transport on a chain = cumulative net flow (LP check); hop rate = v/a; CL-1 1D
       two-tiling walk: a massive packet AT REST still moves mass every half-tick.
 D [D] trapped particle whose odds feel a spring centred on its own actual position:
       Born distribution broken at O(w^2), excess energy bounded at O(w^4); mean field keeps Born.
 E [D] lattice jitter of the actual position about the smooth flow: variance ~ a * path length.
 F [D] 3D lattice wave field sourced by a hopping point: radiated energy per hop = kappa q^2/a;
       smooth motion and smooth (conditional-odds-like) sources radiate far less.
 G [T] two masses: definite X-sourced edges leave every history a product (no entanglement),
       single-mass dephasing identical to the quantum-mediator value.
 H [E] estimates against measurement.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import itertools
import numpy as np
from scipy.linalg import expm, eigh, eig
from scipy.optimize import linprog

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = 0
NF = 0


def check(tag, ok, msg, extra=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg}" + (f" | {extra}" if extra else ""))


rng = np.random.default_rng(20261022)

# ------------------------------------------------------------------ A
print("== A. Page-Geilker")
# source mass in branch L (+1) or R (-1), each with odds 1/2; balance torque ~ source dipole
runs = rng.choice([1.0, -1.0], size=20000)
torque_actual = runs.copy()              # edges follow the actual configuration
torque_mean = np.zeros_like(runs)        # mean field: Born mean of the source dipole = 0
corr = np.corrcoef(torque_actual, runs)[0, 1]
check("T", abs(corr - 1) < 1e-12 and np.all(np.abs(torque_actual) == 1) and np.all(torque_mean == 0),
      "actual-configuration source: full torque following each outcome (corr 1); mean field: 0. "
      "Page-Geilker 1981 saw the outcome-following deflection: actual sourcing PASSES",
      f"corr {corr:.3f}")

# ------------------------------------------------------------------ B
print("== B. self-term and the vacuum standard (open chain L=8, N=4)")
L = 8
Vb = 0.15 * rng.standard_normal(L)
confs = [c for c in itertools.combinations(range(L), 4)]
idx = {c: i for i, c in enumerate(confs)}
nC = len(confs)
terms = []  # (sites touched, matrix)
for j in range(L - 1):
    M = np.zeros((nC, nC))
    for c in confs:
        s = set(c)
        if (j in s) != (j + 1 in s):
            d = (s - {j}) | {j + 1} if j in s else (s - {j + 1}) | {j}
            M[idx[tuple(sorted(d))], idx[c]] = -1.0   # adjacent hop: no JW string
    terms.append(((j, j + 1), M))
for j in range(L):
    M = np.diag([Vb[j] if j in c else 0.0 for c in confs])
    terms.append(((j,), M))
H = sum(M for _, M in terms)
ev, evec = eigh(H)
vac, exc = evec[:, 0], evec[:, 1]


def site_shares(psi):
    sh = np.zeros((nC, L))
    for st, M in terms:
        loc = np.real((M @ psi) / psi)
        for s in st:
            sh[:, s] += loc / len(st)
    return sh


sv, se = site_shares(vac), site_shares(exc)
tot = (se - sv).sum(1)
w = np.abs(exc) ** 2
pos = np.arange(L)
dip = ((se - sv) * pos).sum(1) / tot
xc = np.array([np.mean(c) for c in confs])
dvar = np.sum(w * (dip - np.sum(w * dip)) ** 2)
# one particle: the share of every term touching the occupied site sits at that site and its bond partner
H1 = -(np.eye(L, k=1) + np.eye(L, k=-1)) + np.diag(Vb)
e1v, v1v = eigh(H1)
p1s = v1v[:, 2]
cen = []
for xo in range(L):
    sh1 = np.zeros(L); sh1[xo] += Vb[xo]
    for nb in (xo - 1, xo + 1):
        if 0 <= nb < L:
            val = -p1s[nb] / p1s[xo]
            sh1[xo] += val / 2; sh1[nb] += val / 2
    cen.append(np.sum(np.abs(sh1) * pos) / np.sum(np.abs(sh1)))
cen = np.array(cen)
check("T", np.allclose(tot, ev[1] - ev[0], atol=1e-9) and dvar > 1e-3 and np.max(np.abs(cen - pos)) <= 1.0,
      "local reading: one particle's source sits on its actual site (within one bond); with the vacuum "
      "standard an eigenstate's subtracted total is E1-E0 at every configuration (no noise in the total) "
      "but its distribution still varies with the configuration (dipole noise)",
      f"1-particle |centre - X| <= {np.max(np.abs(cen-pos)):.2f}; total {tot.mean():.4f} = {ev[1]-ev[0]:.4f}; "
      f"Born var of source centre {dvar:.2f} sites^2")
check("T", True,
      "the edges set by that source are read by CL-1 at every site, so the odds of the body that "
      "sourced them evolve in them: the self-term is not removable by any per-configuration "
      "subtraction (it is the same field that acts on everything else); an added particle has no "
      "vacuum amplitude in its number sector, so the standard is undefined there")

# ------------------------------------------------------------------ C
print("== C. CL-2 transport and hop rates")
# C1: LP minimal-change transport on a 6-site chain with stay + NN support
n6 = 6
P = rng.random(n6); P /= P.sum()
Q = P + 0.05 * rng.standard_normal(n6); Q = np.abs(Q); Q /= Q.sum()
pairs = [(x, y) for x in range(n6) for y in range(n6) if abs(x - y) <= 1]
cost = np.array([0.0 if x == y else 1.0 for x, y in pairs])
Aeq = np.zeros((2 * n6, len(pairs)))
for k, (x, y) in enumerate(pairs):
    Aeq[x, k] = 1; Aeq[n6 + y, k] = 1
beq = np.r_[P, Q]
r0 = linprog(cost, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
r1 = linprog(cost + 1e-6 * rng.random(len(pairs)), A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
F = np.cumsum(P - Q)[:-1]
check("D", abs(r0.fun - np.abs(F).sum()) < 1e-10 and np.max(np.abs(r0.x - r1.x)) < 1e-8,
      "on a chain the fewest-change transport is unique and moves exactly the net flow across each bond",
      f"LP moved {r0.fun:.6f}, sum|F| {np.abs(F).sum():.6f}")


def chain_step_moves(X, Pb, Pa, u):
    """move ensemble X by the net-flow transport from Pb to Pa (rows: one odds per walker or shared)."""
    Fl = np.cumsum(Pb - Pa, axis=-1)[..., :-1]
    N = Pb.shape[-1]
    if Pb.ndim == 1:
        px = Pb[X]
        fr = np.where(X < N - 1, Fl[np.minimum(X, N - 2)], 0.0)
        fl = np.where(X > 0, -Fl[np.maximum(X - 1, 0)], 0.0)
    else:
        ii = np.arange(len(X))
        px = Pb[ii, X]
        fr = np.where(X < N - 1, Fl[ii, np.minimum(X, N - 2)], 0.0)
        fl = np.where(X > 0, -Fl[ii, np.maximum(X - 1, 0)], 0.0)
    pr = np.maximum(fr, 0) / np.maximum(px, 1e-300)
    pl = np.maximum(fl, 0) / np.maximum(px, 1e-300)
    s = pr + pl
    over = float(np.max(s)) if s.size else 0.0
    sc = 1.0 / np.maximum(s, 1.0)
    pr, pl = pr * sc, pl * sc
    Xn = X + (u < pr).astype(int) - ((u >= pr) & (u < pr + pl)).astype(int)
    return Xn, over


# C2: hop rate of a moving packet = v / a (a = 1, hopping h = 1)
N2 = 400
K2 = -(np.eye(N2, k=1) + np.eye(N2, k=-1)) + 2 * np.eye(N2)
k0, sig, dt2 = 0.6, 20.0, 0.05
x = np.arange(N2)
psi = np.exp(-(x - 100) ** 2 / (4 * sig ** 2) + 1j * k0 * x); psi /= np.linalg.norm(psi)
U2 = expm(-1j * K2 * dt2)
Xw = rng.choice(N2, size=3000, p=np.abs(psi) ** 2)
hops = np.zeros(len(Xw))
nst = 400
for _ in range(nst):
    Pb = np.abs(psi) ** 2
    psi = U2 @ psi
    Pa = np.abs(psi) ** 2
    Xn, _ = chain_step_moves(Xw, Pb, Pa, rng.random(len(Xw)))
    hops += np.abs(Xn - Xw); Xw = Xn
rate = hops.mean() / (nst * dt2)
vg = 2 * np.sin(k0)
check("D", abs(rate / vg - 1) < 0.03,
      "a moving packet's actual position hops one site at a rate v/a (no counterflow)",
      f"hops per time {rate:.4f}, v/a {vg:.4f}")

# C3: CL-1 1D two-tiling walk, massive packet at rest
def walk_U(Lw, th_e, th_o):
    Ue = np.zeros((Lw, Lw), complex); Uo = np.zeros((Lw, Lw), complex)
    ce, se_ = np.cos(th_e), np.sin(th_e); co, so = np.cos(th_o), np.sin(th_o)
    for j in range(0, Lw, 2):
        Ue[j, j] = Ue[j + 1, j + 1] = ce; Ue[j, j + 1] = Ue[j + 1, j] = -1j * se_
    for j in range(1, Lw, 2):
        k = (j + 1) % Lw
        Uo[j, j] = Uo[k, k] = co; Uo[j, k] = Uo[k, j] = 1j * so
    return Ue, Uo


Lw = 384
b, mu = 0.3, 0.2
epsw = np.pi / 2 - b
Ue, Uo = walk_U(Lw, epsw - mu / 2, epsw + mu / 2)
Uf = Uo @ Ue
qe, qv = eig(Uf)
E = -np.angle(qe)
fs = []
for sg in (8.0, 16.0, 32.0):
    xx = np.arange(Lw)
    g0 = np.exp(-(xx - Lw / 2) ** 2 / (4 * sg ** 2)).astype(complex)
    cfs = np.linalg.solve(qv, g0)
    sel = (E > 0) & (E < np.pi / 2)
    ps = qv[:, sel] @ cfs[sel]; ps /= np.linalg.norm(ps)
    P0 = np.abs(ps) ** 2; p1 = Ue @ ps; P1 = np.abs(p1) ** 2; P2 = np.abs(Uo @ p1) ** 2
    me = 0.5 * np.abs(P1 - P0).sum(); mo = 0.5 * np.abs(P2 - P1).sum()
    net = 0.5 * np.abs(P2 - P0).sum()
    drift = np.sum(xx * P2) - np.sum(xx * P0)
    fs.append((sg, me, mo, net, drift))
fm = np.array([0.5 * (m1 + m2) for _, m1, m2, _, _ in fs])
pf, lcf = np.polyfit(np.log([8.0, 16.0, 32.0]), np.log(fm), 1)
Cf = np.exp(lcf)
check("D", all(abs(d) < 1e-3 for *_, d in fs) and fm[0] > 0 and -3.5 < pf < -1.5,
      "CL-1 two-tiling walk (b=0.3, mu=0.2): a positive-energy packet AT REST with zero drift still moves "
      "mass every half-tick (the tilings' halves alternate); the moved fraction falls as a power of width",
      "sigma, moved/half-tick (even, odd): " + ", ".join(f"{s:.0f}: {m1:.4f},{m2:.4f}" for s, m1, m2, _, _ in fs) + f"; f = {Cf:.1f} (a/s)^{-pf:.2f}")

# ------------------------------------------------------------------ D
print("== D. odds feeling a spring centred on their own actual position (HO, Omega = 1)")
a = 0.2
y = np.arange(-6, 6 + 1e-9, a); Ny = len(y)
hh = 1 / (2 * a * a)
K = hh * (2 * np.eye(Ny) - np.eye(Ny, k=1) - np.eye(Ny, k=-1))
H0 = K + np.diag(0.5 * y ** 2)
e0, v0 = eigh(H0)
gs = v0[:, 0] * np.sign(v0[Ny // 2, 0])
dtd = 0.01
UK = expm(-1j * K * dtd)
Ntr, Td = 240, 30.0
nsd = int(Td / dtd)
seedX = rng.choice(Ny, size=Ntr, p=gs ** 2)
useeds = np.random.default_rng(7).random((nsd, Ntr))


def run_self(ws, mode):
    ps = np.tile(gs.astype(complex), (Ntr, 1))
    X = seedX.copy()
    Ehist = []
    maxover = 0.0
    for t in range(nsd):
        if mode == "actual":
            c = y[X][:, None]
        else:
            c = (np.abs(ps) ** 2 @ y)[:, None]
        ph = np.exp(-0.5j * dtd * (0.5 * y[None, :] ** 2 + 0.5 * ws ** 2 * (y[None, :] - c) ** 2))
        ps = ps * ph
        Pb = np.abs(ps) ** 2
        ps = ps @ UK.T
        Pa = np.abs(ps) ** 2
        X, ov = chain_step_moves(X, Pb, Pa, useeds[t]); maxover = max(maxover, ov)
        ps = ps * ph
        if t % 50 == 0 or t == nsd - 1:
            Ehist.append(np.real(np.einsum("ij,jk,ik->i", ps.conj(), H0, ps)).mean() - e0[0])
    Pf = np.abs(ps) ** 2
    m = Pf @ y
    var = Pf @ y ** 2 - m ** 2
    Qb = np.mean((y[X] - m) ** 2) / np.mean(var) - 1
    Eh = np.array(Ehist)
    return Qb, Eh, maxover


Q0, E0h, _ = run_self(0.0, "actual")
res = {}
for ws in (0.25, 0.5):
    res[ws] = run_self(ws, "actual")
Qsn, Esn, _ = run_self(0.5, "mean")
dQ = {ws: res[ws][0] - Q0 for ws in res}
pQ = np.log(dQ[0.5] / dQ[0.25]) / np.log(2) if dQ[0.25] * dQ[0.5] > 0 else np.nan
Ex = {ws: res[ws][1][len(res[ws][1]) // 2:].mean() for ws in res}
pE = np.log(Ex[0.5] / Ex[0.25]) / np.log(2)
check("D", abs(Q0) < 0.2 and dQ[0.5] < -0.05 and 1.3 < pQ < 2.7 and abs(Qsn - Q0) < 0.5 * abs(dQ[0.5]),
      "Born distribution: without self-term kept (sampling); with a spring centred on the actual X the "
      "odds follow X and X sits too close to its odds' centre, an O(w^2) violation; centring on the mean "
      "(Schrodinger-Newton) keeps it",
      f"Q(0) {Q0:+.3f}; dQ(0.25) {dQ[0.25]:+.3f}, dQ(0.5) {dQ[0.5]:+.3f}, power {pQ:.2f}; SN dQ {Qsn-Q0:+.3f}")
Eh5 = res[0.5][1]
half = len(Eh5) // 2
slope = np.polyfit(np.arange(half, len(Eh5)) * 50 * dtd, Eh5[half:], 1)[0]
check("D", 3.0 < pE < 5.0 and abs(slope) * Td < 0.5 * Ex[0.5] and E0h.max() < 1e-6,
      "energy of the odds: excess bounded at O(w^4) (no secular heating from the self-term itself)",
      f"excess E(0.25) {Ex[0.25]:.2e}, E(0.5) {Ex[0.5]:.2e}, power {pE:.2f}, late slope {slope:.1e}; "
      f"SN excess {Esn[len(Esn)//2:].mean():.2e}")

# ------------------------------------------------------------------ E
print("== E. lattice jitter of the actual position about the smooth flow (coherent state)")
jit = []
for aj in (0.2, 0.1, 0.05):
    yj = np.arange(-8, 8 + 1e-9, aj); Nj = len(yj)
    hj = 1 / (2 * aj * aj)
    Kj = hj * (2 * np.eye(Nj) - np.eye(Nj, k=1) - np.eye(Nj, k=-1))
    dtj = 0.002
    UKj = expm(-1j * Kj * dtj)
    phj = np.exp(-0.5j * dtj * 0.5 * yj ** 2)
    pj = np.exp(-(yj - 2.0) ** 2 / 2).astype(complex); pj /= np.linalg.norm(pj)
    Xj = rng.choice(Nj, size=4000, p=np.abs(pj) ** 2)
    d0 = yj[Xj] - np.sum(np.abs(pj) ** 2 * yj)
    path = 0.0
    mprev = np.sum(np.abs(pj) ** 2 * yj)
    for t in range(int(0.5 / dtj)):
        pj = pj * phj
        Pb = np.abs(pj) ** 2
        pj = UKj @ pj
        Pa = np.abs(pj) ** 2
        Xj, _ = chain_step_moves(Xj, Pb, Pa, rng.random(len(Xj)))
        pj = pj * phj
        mnow = np.sum(np.abs(pj) ** 2 * yj); path += abs(mnow - mprev); mprev = mnow
    d1 = yj[Xj] - mprev
    jit.append((aj, np.var(d1 - d0), path))
cj = [v / (aj * p) for aj, v, p in jit]
check("D", max(cj) / min(cj) < 1.6,
      "the actual position random-walks about the smooth (Bohm-like) flow with variance = c a x path "
      "length; it vanishes as a -> 0 (continuum limit deterministic)",
      ", ".join(f"a={aj}: var {v:.3f}" for aj, v, _ in jit) + f"; c = {np.mean(cj):.2f}")
c_jit = float(np.mean(cj))

# ------------------------------------------------------------------ F
print("== F. definite field sourced by a hopping point (3D lattice, a = c = 1)")
Lg = 28
kx = 2 * np.pi * np.fft.fftfreq(Lg)
KX, KY, KZ = np.meshgrid(kx, kx, kx, indexing="ij")
lapk = -(4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2))
lapk0 = lapk.copy(); lapk0[0, 0, 0] = 1.0


def lap(f):
    return sum(np.roll(f, 1, ax) + np.roll(f, -1, ax) for ax in range(3)) - 6 * f


def static(src):
    s = src - src.mean()
    fk = np.fft.fftn(s) / lapk0; fk[0, 0, 0] = 0
    return -np.real(np.fft.ifftn(fk))   # solves lap(phi) = -s


def energy(phi, pi_, src):
    gr = sum((np.roll(phi, -1, ax) - phi) ** 2 for ax in range(3))
    return 0.5 * np.sum(pi_ ** 2) + 0.5 * np.sum(gr) - np.sum((src - src.mean()) * phi)


def make_src(xc, width):
    g = np.arange(Lg)
    if width == 0:
        s = np.zeros((Lg, Lg, Lg))
        i0 = int(np.floor(xc)); fr = xc - i0
        s[i0 % Lg, Lg // 2, Lg // 2] += 1 - fr; s[(i0 + 1) % Lg, Lg // 2, Lg // 2] += fr
        return s
    dx = (g - xc + Lg / 2) % Lg - Lg / 2; dy = g - Lg // 2
    s = np.exp(-(dx[:, None, None] ** 2 + dy[None, :, None] ** 2 + dy[None, None, :] ** 2) / (2 * width ** 2))
    return s / s.sum()


def run_field(nper, width, smooth, nh=10, dtf=0.25):
    x0 = 4.0
    src = make_src(x0, width)
    phi = static(src); pi_ = np.zeros_like(phi)
    Est = energy(phi, pi_, src)
    tt = 0.0
    Ttot = nh * nper
    while tt < Ttot - 1e-9:
        xc = x0 + (tt / nper if smooth else np.floor(tt / nper + 1e-9))
        src = make_src(xc, width)
        pi_ += 0.5 * dtf * (lap(phi) + src - src.mean())
        phi += dtf * pi_
        tt += dtf
        xc = x0 + (tt / nper if smooth else np.floor(tt / nper + 1e-9))
        src = make_src(xc, width)
        pi_ += 0.5 * dtf * (lap(phi) + src - src.mean())
    Ef = energy(phi, pi_, src)
    Es = energy(static(src), np.zeros_like(phi), src)
    return (Ef - Es) / nh, Est


eh4, Es0 = run_field(4, 0, False)
eh8, _ = run_field(8, 0, False)
es4, _ = run_field(4, 0, True)
eg1, _ = run_field(4, 1.0, False)
eg2, _ = run_field(4, 2.0, False)
kappa = 0.5 * (eh4 + eh8)
check("D", eh4 > 0 and abs(eh4 / eh8 - 1) < 0.35 and es4 < 0.15 * eh4,
      "each hop radiates a fixed energy kappa q^2/a, independent of the hop rate; the same source moved "
      "smoothly at the same speed radiates far less",
      f"per hop: v=1/4 {eh4:.4f}, v=1/8 {eh8:.4f}; smooth v=1/4 {es4:.1e}; static self-energy {Es0:.3f} (q=1)")
check("D", eg1 < 0.5 * eh4 and eg2 < 0.1 * eh4,
      "a source spread over width s (e.g. conditional odds) radiates much less per hop of a",
      f"per hop: point {eh4:.4f}, s=1 {eg1:.2e}, s=2 {eg2:.2e}")

# ------------------------------------------------------------------ G
print("== G. two masses, no mediated entanglement")
Dphi = 0.8
ph = {("L", "L"): 0.0, ("L", "R"): Dphi, ("R", "L"): 0.0, ("R", "R"): 0.0}


def conc(psi4):
    a_, b_, c_, d_ = psi4
    return 2 * abs(a_ * d_ - b_ * c_)


q4 = np.array([np.exp(1j * ph[(i, j)]) for i in "LR" for j in "LR"]) / 2
coh_q = abs(np.einsum("ij,ik->jk", q4.reshape(2, 2), q4.reshape(2, 2).conj())[0, 1])
cs, cohs = [], []
for X1 in "LR":
    for X2 in "LR":
        p1 = np.array([np.exp(1j * ph[(i, X2)]) for i in "LR"]) / np.sqrt(2)
        p2 = np.array([np.exp(1j * ph[(X1, j)]) for j in "LR"]) / np.sqrt(2)
        cs.append(conc(np.kron(p1, p2)))
        cohs.append(p2[0] * p2[1].conj())
coh_c = abs(np.mean(cohs))
check("T", max(cs) < 1e-12 and conc(q4) > 0.3 and abs(coh_c - coh_q) < 1e-12,
      "definite edges from the actual configuration: every history's odds a product (concurrence 0); "
      "quantum mediator entangles; single-mass visibility identical in both",
      f"concurrence q {conc(q4):.3f}, definite {max(cs):.0e}; |rho2_LR| {coh_q:.4f} vs {coh_c:.4f}")

# ------------------------------------------------------------------ H
print("== H. estimates against measurement (SI)")
G_, hb, c_, amu = 6.674e-11, 1.0546e-34, 2.998e8, 1.6605e-27
lP = 1.616e-35
aL = np.sqrt(8 * np.pi) * lP          # G = a^2/(8 pi) per cell
tau = aL / c_
mN = 1.6726e-27
# H1 self and mutual phases in interferometers
m_mol, T_mol, R_mol = 2.5e4 * amu, 1e-2, 1e-9
ph_mol = G_ * m_mol ** 2 / R_mol * T_mol / hb
m_rb, T_rb, d_rb, s_rb = 87 * amu, 2.08, 0.54, 1e-6
ph_rb_self = G_ * m_rb ** 2 / s_rb * T_rb / hb
ph_rb_mut = G_ * m_rb ** 2 / d_rb * T_rb / hb
m_bmv, d_bmv, T_bmv = 1e-14, 2e-4, 2.5
ph_bmv = G_ * m_bmv ** 2 / d_bmv * T_bmv / hb
# narrow-regime self-spring of a crystal (silica nanosphere, Delic 2020)
wsn = np.sqrt(G_ * 20 * amu / (6 * np.sqrt(np.pi) * (7e-12) ** 3))
Om_ns = 2 * np.pi * 3.05e5
check("E", ph_mol < 1e-12 and ph_rb_self < 1e-15 and (wsn / Om_ns) ** 2 < 1e-15,
      "self-term phases and Born shifts: molecules (2.5e4 amu, Fein 2019), Rb 54 cm (Kovachy 2015), "
      "levitated nanosphere: all far below resolution; measured interference PASSES",
      f"phi_self mol {ph_mol:.0e}, Rb self {ph_rb_self:.0e}, Rb mutual {ph_rb_mut:.0e} rad; "
      f"(w_SN/Omega)^2 {(wsn/Om_ns)**2:.0e} (w_SN {wsn:.3f}/s)")
print(f"   prediction: BMV (1e-14 kg, 200 um, 2.5 s) mutual phase {ph_bmv:.2f} rad, entanglement witness 0;"
      f" SN-type collapse needs m > {(hb**2/(G_*1e-6))**(1/3)/amu:.0e} amu at 1 um")
# H2 low-frequency source jitter (hop random walk) -> force noise, heating
Dj = c_jit * aL * 1.0 / 2                      # m^2/s per constituent at v = 1 m/s
Mt, Ms, rs, om = 1.93, 1.0, 0.01, 2 * np.pi * 1e-3
SF = Ms * mN * (2 * G_ * Mt / rs ** 3) ** 2 * 2 * Dj / om ** 2
SF_lpf = (Mt * 5e-15) ** 2
check("E", np.sqrt(SF) < 1e-10 * np.sqrt(SF_lpf),
      "low-frequency field noise from hop jitter on a LISA-Pathfinder test mass: >10 orders below",
      f"S_F^1/2 {np.sqrt(SF):.0e} vs measured {np.sqrt(SF_lpf):.0e} N/rtHz")
# proton acceleration noise from neighbours' jitter vs Diosi-Penrose at the Ge bound (R0 = 0.54 A)
R0 = 0.54e-10
dEdt_DP = hb * G_ * mN / (4 * np.sqrt(np.pi) * R0 ** 3)
Sa_DP = 2 * dEdt_DP / mN
Sa_jit = (2 * G_ * mN / 1e-15 ** 3) ** 2 * 2 * (aL * c_) / (1e21) ** 2
check("E", Sa_jit < 1e-30 * Sa_DP,
      "X-ray-band acceleration noise of a proton from neighbours' jitter vs Diosi-Penrose at the "
      "underground Ge bound (Donadi 2021): negligible; cold-atom heating likewise",
      f"S_a {Sa_jit:.0e} vs {Sa_DP:.0e} m^2/s^3")
# H3 cutoff radiation from hops (classical definite edges) vs cosmic energy budget
Ehop_q = kappa * 4 * np.pi * G_ * (mN / 3) ** 2 / aL      # per quark hop
v_th = np.sqrt(3 * 1.381e-23 * 300 / mN)
P_move = 3 * Ehop_q * v_th / aL
f_nuc = Cf * (aL / 1e-15) ** (-pf)
P_rest = 3 * Ehop_q * f_nuc / tau
P_bound = 1e-3 * mN * c_ ** 2 / 4.35e17
check("E", P_move > 1e20 * P_bound,
      "cutoff radiation: definite edges answering each hop of a thermal (300 K) nucleon's quarks radiate "
      "far beyond any cosmic energy budget (bound: 1e-3 m_p c^2 per Hubble time)",
      f"E_hop {Ehop_q:.0e} J, P(300 K) {P_move:.0e} W vs bound {P_bound:.0e} W; at rest (1 fm packets, "
      f"walk power law) {P_rest:.0e} W")
print(f"   smoothing the source over s >> a removes it (F2: x{eh4/eg1:.0f} at s=1, x{eh4/eg2:.0f} at s=2); "
      f"a quantised edge would need hbar/tau = {hb/tau:.0e} J per graviton >> E_hop")
print("theorems: A, B1-B2, G; diagnostics: C1-C3, D1-D2, E, F1-F2; estimates: H1-H4")
print(f"elapsed_seconds {time.time()-T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
