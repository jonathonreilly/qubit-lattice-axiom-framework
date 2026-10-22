#!/usr/bin/env python3
"""induced-response: can CL-5 shrink to 'edge lengths and links take the values at which the matter phase is stationary'?

Supplied model: the CL-2 tick (spin-3/2 edge hop W indexed by site type, even then odd 2^3 cubes, half-ticks
exp(-i(eps - mu/2)W) and exp(+i(eps + mu/2)W)), the filled negative-quasi-energy sea, CL-5 site-phase links
(centre-bond holonomies from straight segments), and a lattice-vielbein metric coupling (each bond's hop scaled by
1/length, each generator by proper time).  Static backgrounds, free sea, classical links, second order.
Finite diagnostics; no physical identification.
 A  engine: bands; U + U^+ = 2 cos w so the sea projector is algebraic; Bloch second-order Floquet sums equal exact
    diagonalisation of a (8 site)^3 torus; exact gauge invariance; exchange antisymmetry F(eps,mu) = -F(pi/2-mu/2, pi-2eps)
 B  induced Maxwell 1/e^2 (Coulomb E and magnetic B) on commensurate tori, q -> 0 then m -> 0
 C  induced gravity: static TT strain, lapse, spatial dilation
 D  vacuum phase of the sea and its stress versus eps
 E  estimates with measured numbers (supplied SM content, CL-5 spacing a = sqrt(8 pi) l_P)
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/THE_CUBE_TICK_SEA_INDUCES_NEITHER_A_LORENTZ_INVARIANT_MAXWELL_TERM_NOR_A_NEWTONIAN_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import itertools, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ------------------------------------------------------------------ CL-2 tick (type-labelled cubes)
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / r3; _, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
EDGES = [(a, b) for a in range(8) for b in range(8) if a < b and np.sum(abs(C8[a] - C8[b])) == 1]
AXIS = {e: int(np.argmax(abs(C8[e[0]] - C8[e[1]]))) for e in EDGES}
W = np.zeros((8, 8), complex)
for a, b in EDGES:
    g_ = XI[a].conj() @ XI[b]; W[a, b] = -g_ / abs(g_) / r3; W[b, a] = np.conj(W[a, b])
BOND = {}
for e in EDGES:
    X = np.zeros((8, 8), complex); X[e] = W[e]; X[e[::-1]] = W[e[::-1]]; BOND[e] = X
PP, PMI = (I8 + W) / 2, (I8 - W) / 2
def expmW(t): return np.cos(t) * I8 - 1j * np.sin(t) * W
def Dm(K): return np.exp(1j * (np.atleast_2d(K) @ C8.T))
def Uo(Ko, Ki, M):
    Do, Di = Dm(Ko), Dm(Ki); return Do[:, :, None] * M[None] * Di.conj()[:, None, :]
def tick(K, eps, mu):
    Ue = expmW(eps - mu / 2); Mo = expmW(-(eps + mu / 2)); return Uo(K, K, Mo) @ Ue, Ue, Mo
def Sof(K): return np.cos(np.atleast_2d(K)).sum(1) / 3
def w_an(K, eps, mu):
    A = (np.cos(mu) - np.cos(2 * eps)) / 2
    return np.arccos(np.clip(A * Sof(K) + (np.cos(2 * eps) + np.cos(mu)) / 2, -1, 1))
def speed2(eps, mu):
    A = (np.cos(mu) - np.cos(2 * eps)) / 2; return A / 3 * (mu / np.sin(mu) if mu else 1.0)
def mu_of_m(eps, m):                       # mass angle with inverse Compton length m (blocks^-1)
    mu = np.sin(eps) / r3 * m
    for _ in range(60): mu = np.sqrt(speed2(eps, mu)) * m
    return mu
def dag(A): return np.conj(np.swapaxes(A, -1, -2))
def tr(A): return np.trace(A, axis1=-2, axis2=-1)
def proj(U):
    cw = np.real(tr(U)) / 8; w = np.arccos(np.clip(cw, -1, 1)); X = (U - dag(U)) / (2j * np.sin(w)[:, None, None])
    return (I8 + X) / 2, (I8 - X) / 2, w
def second_order(U0, U0p, U0m, d1p, d1m, d2):
    """coefficient of lambda^2 in the filled quasi-energy sum (batch total): Floquet second order."""
    PF, _, w = proj(U0); _, PEp, wp = proj(U0p); _, PEm, wm = proj(U0m)
    M1p, M1m = dag(U0p) @ d1p, dag(U0m) @ d1m
    A2 = 1j * (dag(U0) @ d2 + 0.5 * (dag(M1p) @ M1p + dag(M1m) @ M1m))
    t1 = tr(PF @ A2); A1p, A1m = 1j * M1p, 1j * M1m
    t2 = -0.5 * (np.real(tr(PEp @ A1p @ PF @ dag(A1p))) / np.tan((w + wp) / 2)
                 + np.real(tr(PEm @ A1m @ PF @ dag(A1m))) / np.tan((w + wm) / 2))
    return np.sum(np.real(t1) + t2)
def gauge_blocks(K, eps, mu, q, h1, h2):
    U0, Ue, Mo = tick(K, eps, mu); Kp, Km = K + q, K - q
    Op, Om, O0 = Uo(Kp, Kp, Mo), Uo(Km, Km, Mo), Uo(K, K, Mo)
    ph = np.exp(1j * (C8 @ q) / 2)
    T1p, T1m, T2p, T2m = (np.diag(h * p) / 2 for h, p in ((h1, ph), (h1, ph.conj()), (h2, ph), (h2, ph.conj())))
    d1p = 1j * T2p @ O0 @ Ue + Op @ (1j * T1p) @ Ue; d1m = 1j * T2m @ O0 @ Ue + Om @ (1j * T1m) @ Ue
    d2 = (-0.25 * np.diag(h2 ** 2) @ O0 @ Ue - 0.25 * O0 @ np.diag(h1 ** 2) @ Ue - T2m @ Op @ T1p @ Ue - T2p @ Om @ T1m @ Ue)
    return U0, Op @ Ue, Om @ Ue, d1p, d1m, d2
def dd1(x, y): return -1j * np.exp(-1j * x) if abs(x - y) < 1e-12 else (np.exp(-1j * x) - np.exp(-1j * y)) / (x - y)
def dd2(x, y, z):
    if abs(x - y) < 1e-12 and abs(y - z) < 1e-12: return -np.exp(-1j * x) / 2
    if abs(x - z) < 1e-12: x, y = y, x
    return (dd1(x, y) - dd1(y, z)) / (x - z)
def fr1(G, A):
    return sum(dd1(ga, gb) * (Pa @ A @ Pb) for ga, Pa in G for gb, Pb in G)
def fr2(G, A, B):
    return sum(dd2(ga, gc, gb) * (Pa @ A @ Pc @ B @ Pb + Pa @ B @ Pc @ A @ Pb) for ga, Pa in G for gc, Pc in G for gb, Pb in G)
def gen_blocks(K, eps, mu, q, Yep, Yop):
    """cube-generator perturbation dG(n) = (1/2) sum_+- e^{+-iq.n} Y+-, Y- = Y+^dag (Bloch-effective phases)."""
    U0, Ue, Mo = tick(K, eps, mu); Kp, Km = K + q, K - q
    Ee = [(eps - mu / 2, PP), (-(eps - mu / 2), PMI)]; Eo = [(-(eps + mu / 2), PP), (eps + mu / 2, PMI)]
    fep, fem = fr1(Ee, Yep) / 2, fr1(Ee, Yep.conj().T) / 2; fop, fom = fr1(Eo, Yop) / 2, fr1(Eo, Yop.conj().T) / 2
    fe2, fo2 = fr2(Ee, Yep, Yep.conj().T) / 4, fr2(Eo, Yop, Yop.conj().T) / 4
    Op, Om = Uo(Kp, Kp, Mo), Uo(Km, Km, Mo)
    d1p = Uo(Kp, K, fop) @ Ue + Op @ fep; d1m = Uo(Km, K, fom) @ Ue + Om @ fem
    d2 = Uo(K, K, fo2) @ Ue + Uo(K, Kp, fom) @ fep + Uo(K, Km, fop) @ fem + Uo(K, K, Mo) @ fe2
    return U0, Op @ Ue, Om @ Ue, d1p, d1m, d2
def total(fn, Ks, *args, batch=2000):
    return sum(second_order(*fn(Ks[s:s + batch], *args)) for s in range(0, len(Ks), batch))
def kgrid(ns, shift=0.5):
    gs = [2 * np.pi * (np.arange(n) + shift) / n - np.pi for n in ns]
    return np.array(np.meshgrid(*gs, indexing='ij')).reshape(3, -1).T
def bpos(e, odd):                              # absolute bond midpoint in cube 0 (odd cube sites at 1 - t/2)
    t1, t2 = C8[e[0]], C8[e[1]]; return (1 - (t1 + t2) / 4) if odd else (t1 + t2) / 4
def hopY(q, wax, eps, odd, cube=False):        # kinetic hop-modulus perturbation (bond or cube-centre sampling)
    Y = np.zeros((8, 8), complex); cc = np.full(3, -0.25 if odd else 0.25)
    for e in EDGES:
        x = cc if cube else bpos(e, odd) - (1.0 if odd else 0.0); Y += wax[AXIS[e]] * np.exp(1j * q @ x) * BOND[e]
    return (-eps if odd else eps) * Y
def lapseY(q, eps, mu, odd, cube=True):        # generator times proper time (cube centre or bond sampling)
    g = -(eps + mu / 2) if odd else (eps - mu / 2)
    if cube: return g * W * np.exp(1j * q @ np.full(3, -0.25 if odd else 0.25))
    return g * sum(np.exp(1j * q @ (bpos(e, odd) - (1.0 if odd else 0.0))) * BOND[e] for e in EDGES)
D_R = C8 - 0.5                                  # even-centre -> odd-centre link through each site type (blocks)
def link_h(kind, q, adir=(0, 0, 1)):
    s = np.sinc((D_R @ q) / 2 / np.pi)
    if kind == 'E': return -0.5 * s, -0.5 * s
    a = (q / np.linalg.norm(q)) if kind == 'L' else np.array(adir, float); h = (D_R @ a) * s; return h, -h
kap = 2 / (6 * np.pi ** 2)                      # continuum log coefficient for two Dirac copies
def maxwell(eps, m, f=0.8, kinds=('E', 'B')):
    """1/e^2 from Coulomb (c delta_E) and magnetic (delta_B / c) responses, q -> 0 fit on a commensurate torus."""
    mu = mu_of_m(eps, m); c = np.sqrt(speed2(eps, mu)); Nx, Nt = int(round(f * 32 / m)), int(round(f * 16 / m))
    Ks = kgrid((Nx, Nt, Nt)); out = {}
    for kind in kinds:
        rows = []
        for j in (1, 2, 3):
            q = np.array([2 * np.pi * j / Nx, 0, 0]); r = total(gauge_blocks, Ks, eps, mu, q, *link_h(kind, q))
            rows.append((q[0] ** 2, (-4 if kind == 'E' else 4) * r / (q[0] ** 2 * len(Ks))))
        rows = np.array(rows); d0 = np.linalg.solve(np.stack([np.ones(3), rows[:, 0], rows[:, 0] ** 2], 1), rows[:, 1])[0]
        out[kind] = c * d0 if kind == 'E' else d0 / c
    return out, mu
def grav(kind, eps, m, f=0.8):
    """static response R(q) = R0 + R2 q^2 (+ q^4) per block per h^2, q along z."""
    mu = mu_of_m(eps, m); Nz, Nt = int(round(f * 32 / m)), int(round(f * 16 / m)); Ks = kgrid((Nt, Nt, Nz)); rows = []
    for j in (1, 2, 3):
        q = np.array([0, 0, 2 * np.pi * j / Nz])
        if kind in ('TT', 'TTc'): Y = [hopY(q, (-0.5, 0.5, 0), eps, o, kind == 'TTc') for o in (False, True)]
        elif kind == 'PSI': Y = [hopY(q, (1, 1, 1), eps, o) for o in (False, True)]
        else: Y = [lapseY(q, eps, mu, o, kind == 'PHI') for o in (False, True)]
        rows.append((q[2] ** 2, total(gen_blocks, Ks, eps, mu, q, *Y) / len(Ks)))
    rows = np.array(rows); return np.linalg.solve(np.stack([np.ones(3), rows[:, 0], rows[:, 0] ** 2], 1), rows[:, 1])

# ------------------------------------------------------------------ A. engine
print('== A. engine (exact checks)')
rng = np.random.default_rng(20261021); KR = rng.uniform(-np.pi, np.pi, (400, 3)); dv = cw = pf = 0
for eps, mu in ((0.04, 0.01), (0.7, 0.3), (1.5, 0.1)):
    U, _, _ = tick(KR, eps, mu); w = w_an(KR, eps, mu)
    dv = max(dv, np.abs(np.sort(np.abs(np.angle(np.linalg.eigvals(U))), 1) - w[:, None]).max())
    cw = max(cw, np.abs(U + dag(U) - 2 * np.cos(w)[:, None, None] * I8).max()); PF = proj(U)[0]
    pf = max(pf, np.abs(PF @ PF - PF).max(), np.abs(np.real(tr(PF)) - 4).max())
check('A1 all 8 bands obey cos w = A S + (cos2eps + cos mu)/2; U + U^+ = 2 cos w; P_F algebraic, rank 4', max(dv, cw, pf) < 1e-10,
      f'{max(dv, cw, pf):.1e}')
Lb = 4; L = 2 * Lb; NS = L ** 3; S = np.array(list(itertools.product(range(L), repeat=3)))
ridx = (S % 2) @ [4, 2, 1]; XS = S / 2.0
def idx(v): v = np.asarray(v) % L; return (v[0] * L + v[1]) * L + v[2]
def torus(Ge, Go, th1=None, th2=None):
    Ue = np.zeros((NS, NS), complex); Uo_ = np.zeros((NS, NS), complex)
    for n in itertools.product(range(Lb), repeat=3):
        n = np.array(n); ie = [idx(2 * n + t) for t in C8]; io = [idx(2 * n + 1 + (1 - t)) for t in C8]
        Ue[np.ix_(ie, ie)] = expm(-1j * Ge(n)); Uo_[np.ix_(io, io)] = expm(-1j * Go(n))
    V1 = np.ones(NS) if th1 is None else np.exp(1j * th1); V2 = np.ones(NS) if th2 is None else np.exp(1j * th2)
    e = -np.angle(np.linalg.eigvals((V2[:, None] * Uo_ * V1[None, :]) @ Ue)); return np.array([e[e < 0].sum(), e[e > 0].sum()])
KG = kgrid((Lb,) * 3, 0.0); worst = 0; flip = 0
for eps, mu in ((0.7, 0.3), (1.3, 0.4)):
    Ge0 = lambda n: (eps - mu / 2) * W; Go0 = lambda n: -(eps + mu / 2) * W; base = torus(Ge0, Go0)
    q = np.array([2 * np.pi / Lb, 2 * np.pi / Lb, 0]); amp = 1e-3
    h1, h2 = rng.normal(size=8), rng.normal(size=8)
    ed = sum(torus(Ge0, Go0, s * amp * h1[ridx] * np.cos(XS @ q), s * amp * h2[ridx] * np.cos(XS @ q)) for s in (1, -1)) - 2 * base
    worst = max(worst, abs(ed[0] / 2 / amp ** 2 / total(gauge_blocks, KG, eps, mu, q, h1, h2) - 1)); flip = max(flip, abs(ed[0] + ed[1]) / abs(ed[0]))
    wax = rng.normal(size=3)
    dG = lambda n, o: sum(wax[AXIS[e]] * np.cos(q @ (n + bpos(e, o))) * BOND[e] for e in EDGES) * (-eps if o else eps)
    ed = sum(torus(lambda n: Ge0(n) + s * amp * dG(n, False), lambda n: Go0(n) + s * amp * dG(n, True)) for s in (1, -1)) - 2 * base
    worst = max(worst, abs(ed[0] / 2 / amp ** 2 / total(gen_blocks, KG, eps, mu, q, hopY(q, wax, eps, False), hopY(q, wax, eps, True)) - 1))
    flip = max(flip, abs(ed[0] + ed[1]) / abs(ed[0]))
check('A2 Bloch second-order sums (link phases, bond hop moduli) = exact diagonalisation of the (8 site)^3 torus', worst < 2e-5,
      f'max rel dev {worst:.1e} (finite-difference amplitude 1e-3)')
check('A2b theorem: det U is unchanged at second order, so filling the other half (pi-reading) flips the sign of every induced '
      'coefficient; positive-energy photons select the 0-reading', flip < 1e-6, f'(dF + dE)/dF = {flip:.1e}')
Ks = kgrid((32, 16, 16)); q = np.array([2 * np.pi / 32, 0, 0])
pg = abs(total(gauge_blocks, Ks, 0.5, 0.1, q, *link_h('L', q))); ref = abs(total(gauge_blocks, Ks, 0.5, 0.1, q, *link_h('B', q)))
check('A3 pure-gauge link field gives zero response on the commensurate torus (exact gauge invariance)', pg < 1e-11 * ref, f'{pg:.1e} vs {ref:.1e}')
Ks = kgrid((12, 12, 12)); q = rng.normal(size=3) * 0.4; h1, h2 = rng.normal(size=8), rng.normal(size=8); asy = 0
for eps, mu in ((0.05, 0.01), (0.3, 0.2), (1.1, 0.5)):
    r1 = total(gauge_blocks, Ks, eps, mu, q, h1, h2); r2 = total(gauge_blocks, Ks, np.pi / 2 - mu / 2, np.pi - 2 * eps, q, h1, h2)
    asy = max(asy, abs(r1 + r2) / abs(r1))
z0 = abs(total(gauge_blocks, Ks, 0.8, np.pi - 1.6, q, h1, h2))
check('A4 theorem: every link response is odd under (eps,mu) -> (pi/2-mu/2, pi-2eps), i.e. 0-cone mass mu <-> pi-cone mass '
      'pi-2eps; it vanishes at mu = pi-2eps', asy < 1e-12 and z0 < 1e-9, f'rel {asy:.1e}; at exchange point {z0:.1e}')

# ------------------------------------------------------------------ B. induced Maxwell
print('== B. induced Maxwell term of the CL-2 sea (one species = two Dirac copies)')
ms = (0.5, 0.35, 0.25); res = {m: maxwell(0.05, m)[0] for m in ms}
CE = np.array([res[m]['E'] / kap - np.log(1 / m) for m in ms]); CB = np.array([res[m]['B'] / kap - np.log(1 / m) for m in ms])
slE = (res[0.25]['E'] - res[0.35]['E']) / np.log(0.35 / 0.25); slB = (res[0.25]['B'] - res[0.35]['B']) / np.log(0.35 / 0.25)
check('B1 log coefficient d(1/e^2)/d ln(1/m) = 2/(6 pi^2) (two Dirac copies) for both E and B (eps = 0.05)',
      abs(slE / kap - 1) < 0.03 and abs(slB / kap - 1) < 0.03, f'E {slE / kap:.3f}, B {slB / kap:.3f} x kappa')
mm = np.array(ms); Mf = np.stack([np.ones(3), mm ** 2, mm ** 2 * np.log(mm)], 1)
CE0, CB0 = np.linalg.solve(Mf, CE)[0], np.linalg.solve(Mf, CB)[0]; dC0 = CE0 - CB0
print(f'   C_E(m) = {np.round(CE, 4)}, C_B(m) = {np.round(CB, 4)} at m = {ms}; m -> 0: C_E = {CE0:.4f}, C_B = {CB0:.4f}')
check('B2 1/e^2_E = kappa[ln(1/m) + C_E], 1/e^2_B = kappa[ln(1/m) + C_B]: the finite parts differ (Lorentz-violating split)',
      dC0 > 0.1, f'dC = C_E - C_B = {dC0:.4f}: induced photon speed^2 = c^2 (L + C_B)/(L + C_E)')
dCs = {0.05: CE[1] - CB[1]}; Ce = {0.05: CE[1]}
for eps in (0.6, 1.2, 1.4):
    r, mu = maxwell(eps, 0.35); dCs[eps] = (r['E'] - r['B']) / kap; Ce[eps] = r['E'] / kap - np.log(1 / 0.35)
print('   at m = 0.35: ' + ', '.join(f'eps={e}: C_E={Ce[e]:+.3f} dC={dCs[e]:+.4f}' for e in dCs))
v = list(dCs.values())
check('B3 the split stays positive and falls only as eps -> pi/2 (the pi-cone, mass pi - 2eps, becomes a Pauli-Villars image)',
      all(x > 0 for x in v) and v[0] > v[2] > v[3], 'no eps < pi/2 makes the induced Maxwell term Lorentz invariant')
b14 = np.pi / 2 - 1.4; mpi = 2 * b14 / np.sqrt(speed2(np.pi / 2 - mu_of_m(1.4, 0.35) / 2, 2 * b14)); dPV = Ce[1.4] - np.log(mpi)
check('B4 near pi/2 the coupling is Pauli-Villars: C_E -> ln(m_pi) with m_pi the pi-cone inverse Compton length', abs(dPV) < 0.06,
      f'eps = 1.4: C_E - ln(m_pi) = {dPV:+.3f}')
rg, _ = maxwell(1.4, 0.9)
check('B5 signs: 1/e^2 > 0 (positive-energy photons) for mu < pi - 2eps; < 0 (ghost) beyond the exchange point',
      all(res[m][k] > 0 for m in ms for k in 'EB') and rg['E'] < 0 and rg['B'] < 0, f'eps=1.4, m=0.9: {rg["E"]:+.4f}, {rg["B"]:+.4f}')

# ------------------------------------------------------------------ C. induced gravity
print('== C. induced gravity (static; R per block per h^2, units of c0 = sin(eps)/sqrt3)')
c0 = np.sin(0.05) / r3; tt = {m: grav('TT', 0.05, m) / c0 for m in (0.35, 0.25)}; ttc = grav('TTc', 0.05, 0.35) / c0
R2tt = tt[0.25][1] + (tt[0.25][1] - tt[0.35][1]) * 0.25 ** 2 / (0.35 ** 2 - 0.25 ** 2)
check('C1 TT strain: gradient term R2 > 0 (positive-energy TT waves), robust to bond vs cube sampling; uniform term R0 < 0',
      R2tt > 0 and abs(ttc[1] / tt[0.35][1] - 1) < 0.08 and tt[0.35][0] < 0,
      f'R2 = {tt[0.35][1]:.5f}/{tt[0.25][1]:.5f} (m = .35/.25) -> {R2tt:.5f}; cube {ttc[1]:.5f}; R0 = {tt[0.25][0]:+.4f}')
phb, psi, phc = (grav(k, 0.05, 0.35) / c0 for k in ('PHIb', 'PSI', 'PHI'))
check('C2 static scalar sector: lapse and spatial dilation enter a massless tick only via bond hop / proper time, so their '
      'induced forms coincide; numerically ~0 (bond) or < 0 (cube lapse); Einstein needs (0, -4, +4) x R2_TT',
      abs(phb[1]) < 0.02 * R2tt and abs(psi[1]) < 0.12 * R2tt and phc[1] < -3 * R2tt,
      f'R2: lapse(bond) {phb[1]:+.5f}, dilation {psi[1]:+.5f}, lapse(cube) {phc[1]:+.5f}')
t145 = grav('TT', 1.45, 0.35) / (np.sin(1.45) / r3)
check('C3 the TT uniform-strain term falls toward 0 as eps -> pi/2 (exact zero there for the massless sea, D2)',
      abs(t145[0]) < 0.4 * abs(tt[0.35][0]), f'R0(1.45) = {t145[0]:+.4f}, R2(1.45) = {t145[1]:+.5f}')

# ------------------------------------------------------------------ D. vacuum phase
print('== D. vacuum phase Phi = sum of filled quasi-energies per block per tick')
KU = kgrid((48, 48, 48))
def Phi(eps, mu=0.0, m2=None):
    if m2 is None: return -4 * np.mean(w_an(KU, eps, mu))
    return -4 * np.mean(np.arccos(np.clip(np.cos(eps) ** 2 + np.sin(eps) ** 2 * (np.cos(KU) @ m2), -1, 1)))
es = np.array([0.02, 0.3, 0.6, 0.9, 1.2, 1.4, 1.5, np.pi / 2]); h = 1e-5
dP = np.array([(Phi(e + h) - Phi(e - h)) / (2 * h) for e in es])
print('   eps dPhi/deps: ' + ', '.join(f'{e:.2f}:{e * d:+.3f}' for e, d in zip(es, dP)))
dw = lambda e: np.abs(w_an(KR, e + 1e-6, 0) - w_an(KR, e - 1e-6, 0)).max() / 2e-6
check('D1 massless sea: Phi(eps) strictly decreasing, stationary only at eps = pi/2 where Phi = -2pi (0 mod 2pi); there EVERY '
      'mode has dw/deps = 0, so the zero is a decoupling of light from the lapse, not a cancellation',
      np.all(dP[:-1] < 0) and abs(dP[-1]) < 1e-6 and abs(Phi(np.pi / 2) + 2 * np.pi) < 1e-12 and dw(np.pi / 2) < 1e-5 < dw(0.04),
      f'Phi(pi/2) + 2pi = {Phi(np.pi / 2) + 2 * np.pi:.1e}; max dw/deps {dw(np.pi / 2):.1e} (pi/2) vs {dw(0.04):.2f} (0.04)')
an = max(abs(Phi(np.pi / 2, m2=rng.dirichlet(np.ones(3))) + 2 * np.pi) for _ in range(5))
check('D2 theorem: at eps = pi/2 the massless sea phase is -2pi for EVERY uniform hop anisotropy (K -> K + R pairing), so its '
      'stress and uniform-shear response vanish only there', an < 1e-12, f'{an:.1e}')
I0 = -(Phi(np.pi / 2, 0.02) + 2 * np.pi) / 0.02 ** 2; Ev = Phi(0.002) / (np.sin(0.002) / r3)
check('D3 mass residual at eps = pi/2: Phi + 2pi = -I0 mu^2 (I0 = 1.157); Hamiltonian-limit sea energy -9.55 c0 per block',
      abs(I0 - 1.157) < 0.01 and abs(Ev + 9.55) < 0.01, f'I0 = {I0:.4f}, E_vac/c0 = {Ev:.4f}')

# ------------------------------------------------------------------ E. estimates
print('== E. ESTIMATES with measured numbers (supplied SM charges and masses; not theorems)')
MP, blk = 1.220890e19, 2 * np.sqrt(8 * np.pi); ainv = 137.035999; tgt = ainv / (4 * np.pi); k1 = kap / 2
Meff = np.exp(CE0) * MP / blk; lep = [0.51099895e-3, 0.1056584, 1.77686]
one = (k1 * sum(np.log(Meff / x) for x in lep) + k1 * 11 / 3 * (np.log(Meff / 91.1876) + 5 / 6) + 0.02766 * ainv / (4 * np.pi)
       + k1 * 4 / 3 * np.log(Meff / 172.69))
wC = 16 * k1; Cstar = CE0 - (2 * one - tgt) / wC; bstar = np.exp(Cstar) / (2 * r3)
M2 = Meff / np.exp((tgt - one) / (8 * k1))
print(f'   1/e^2 needed {tgt:.3f}. eps->0: one copy {one:.3f} (1/alpha = {4 * np.pi * one:.1f}); two copies {2 * one:.3f} (1/alpha = {8 * np.pi * one:.1f})')
print(f'   two copies match alpha only at eps* = pi/2 - {bstar:.4f} (pi-cone at {2 * bstar * r3 * MP / blk / np.sin(np.pi / 2 - bstar):.1e} GeV), '
      f'beyond the eps < 0.04 stability bound; one light + one heavy copy: M_2 = {M2:.0f} GeV')
dcf = -0.5 * wC * dC0 / tgt; dcb = -2 * np.pi / ainv * 8 * k1 * dC0
print(f'   photon speed: fully induced dc/c = {dcf:.1e}; bare + one loop (one copy) {dcb:.1e} unless the clause fixes the dressed photon;'
      f' LEP 104.5 GeV electrons need |dc/c| < {0.5 * (0.511e-3 / 104.5) ** 2:.0e}')
Rcl5 = 0.5; per = R2tt / 2; ratio = 24 * per / Rcl5
print(f'   gravity: induced TT R2 = {per:.5f} c0 per Dirac copy vs Regge {Rcl5} c0 (site rung): SM (24 Dirac) adds {100 * ratio:.0f}% to the TT'
      f' term and 0 to the Newtonian one -> G_TT/G_N = {1 / (1 + ratio):.2f} vs Hulse-Taylor 0.998(2)')
rho0 = Ev * (MP / blk) ** 4; rhom = -3 * I0 * 172.69 ** 2 * (MP / blk) ** 2 / r3
print(f'   vacuum: eps->0 rho = {rho0:.1e} GeV^4 (radiation-like, p = rho/3); at eps = pi/2 the top residual (3 colours) {rhom:.1e} vs measured 2.5e-47')
check('E1 arithmetic: 1/alpha(induced, one copy) < 137 < 1/alpha(two copies); fully induced photon misses LEP by > 1e6',
      4 * np.pi * one < ainv < 8 * np.pi * one and abs(dcf) > 1e6 * 0.5 * (0.511e-3 / 104.5) ** 2)
print('supplied: tick, sea branch, site-phase coupling, straight links, vielbein reading (bond 1/length, proper-time generator,')
print('  bond or cube sampling), static fields, free sea, SM content and masses, measured hadronic running, a = sqrt(8 pi) l_P.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
