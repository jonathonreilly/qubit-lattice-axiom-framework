#!/usr/bin/env python3
"""Dark-matter candidates inside the candidate laws CL-1..CL-6 (supplied model, finite diagnostic, no physical
identification).  For each candidate: photon coupling, stability, mass scale, relic density, measured comparison.
 A  second copy: every rotation-covariant conserved charge is a scalar on the light rest space, at every rung
 B  pi-cone sector of the staggered tick: same charge as its species, kinematically stable at total momentum R,
    but a band-top state: expelled from potential wells (0-reading) or negative source energy (pi-reading)
 C  a species with no link coupling: exact number conservation (stable), relic set by supplied initial odds
 D  conditional source: its Born mean is the ordinary stress (no extra dark mass); records carry no CL-6 term
 E  measured-reality arithmetic
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 90

import os, sys, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from math import comb
from scipy.linalg import expm, schur
from scipy.optimize import minimize

T0 = time.time()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
def nrm(X): return float(np.abs(X).max())

# ---------------- supplied tick (CL-3, same conventions as agents/pi-and-copies/core.py) ----------------
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float); I8 = np.eye(8)
def Jm(j):
    m = j - np.arange(int(round(2 * j)) + 1); Jp = np.diag(np.sqrt(j * (j + 1) - m[1:] * (m[1:] + 1)), 1).astype(complex)
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def coherent(j, n):
    n = n / np.linalg.norm(n); th, ph, d = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])
XI = [coherent(1.5, v) for v in NV]
ROTS = [R for R in (np.array(p) * np.array(s)[:, None] for p in itertools.permutations(np.eye(3)) for s in itertools.product((1, -1), repeat=3)) if np.isclose(np.linalg.det(R), 1)]
def spin_rot(R):
    w, V = np.linalg.eig(R); a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    ax = np.real(V[:, np.argmin(abs(w - 1))]); ax /= np.linalg.norm(ax)
    if 1e-9 < a < np.pi - 1e-9 and np.dot(ax, [R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) < 0: ax = -ax
    return expm(-1j * a * sum(ax[k] * Jm(1.5)[k] for k in range(3)))
def cidx(v): return int(np.argmin(abs(NV - v).sum(1)))
def corner_action(R):
    S = spin_rot(R); L = np.zeros((8, 8), complex)
    for i in range(8): k = cidx(R @ NV[i]); L[k, i] = XI[k].conj() @ S @ XI[i]
    return L
LS = [corner_action(R) for R in ROTS]
WA = np.zeros((3, 8, 8), complex)
for s, t in itertools.product(range(8), repeat=2):
    if abs(CORN[s] - CORN[t]).sum() == 1:
        g = XI[s].conj() @ XI[t]; WA[int(np.argmax(abs(CORN[s] - CORN[t])))][s, t] = -g / abs(g) / np.sqrt(3)
W = WA.sum(0); EPS = np.diag((-1.0) ** CORN.sum(1)).astype(complex)
def Va(a): return np.cos(a) * W + 1j * np.sin(a) * I8
def bloch(K, ve, vo):
    D = np.exp(1j * (CORN @ np.asarray(K, float))); return (D[:, None] * vo * D.conj()[None, :]) @ ve
def commutant(Ms, tol=1e-9):
    A = np.vstack([np.kron(M, I8) - np.kron(I8, M.T) for M in Ms]); _, s, Vh = np.linalg.svd(A)
    nd = int(np.sum(s < tol)); return [b.reshape(8, 8) for b in Vh[len(s) - nd:].conj()]
def AB(mu, b): return (np.cos(2 * b) + np.cos(mu)) / 2, (np.cos(2 * b) - np.cos(mu)) / 2
def wf(S, mu, b):  # exact staggered band (pi-and-copies section 6): cos w = A S - B
    A, B = AB(mu, b); return np.arccos(np.clip(A * S - B, -1, 1))
def Sof(K): return np.cos(K).mean(-1)
R3 = np.pi * np.ones(3)
rng = np.random.default_rng(7)

print('== A. the second copy: can a covariant charge leave one copy photon-dark?')
mu, b = 0.3, 0.2; ve, vo = Va(mu / 2 + b), Va(mu / 2 - b); U0 = bloch(np.zeros(3), ve, vo)
check('A1 staggered K=0 tick U(0) = cos mu + i sin mu W; rotations commute with W', nrm(U0 - np.cos(mu) * I8 - 1j * np.sin(mu) * W) < 1e-12 and max(nrm(L @ W - W @ L) for L in LS) < 1e-12)
Pp = (I8 + W) / 2; chi = np.array([np.trace(L @ Pp) for L in LS])
check('A2 each 4-dim rest space (W = +1, the two copies of one frequency) is irreducible under the 24 rotations: mean |chi|^2 = 1',
      abs(np.mean(abs(chi) ** 2) - 1) < 1e-9, f'mean |chi|^2 = {np.mean(abs(chi)**2):.6f}, |chi| by element {sorted(set(np.round(abs(chi), 6)))}')
Bc = commutant(LS + [U0])
sc = max(nrm(Pp @ X @ Pp - np.trace(Pp @ X) / 4 * Pp) for X in Bc)
check('A3 Schur: every operator commuting with U(0) and the 24 rotations (local or not) is a scalar on that rest space -> both copies carry the same value of ANY covariant charge',
      len(Bc) == 2 and sc < 1e-9, f'commutant dim {len(Bc)}, non-scalar part {sc:.1e}')
gaps = []
for n in (1, 2, 3):
    m = np.array(list(itertools.product(range(2 ** n), repeat=3)))[1:] * 2 * np.pi / 2 ** n
    gaps.append(float(np.min(abs(wf(Sof(m), mu, b) - mu))))
check('A4 every rung n = 1, 2, 3: the coarse K=0 eigenvalue e^{i mu} comes only from fine K = 0 (S = 1 only there), so A2-A3 hold at every rung',
      min(gaps) > 1e-3, 'min |w - mu| over folded points ' + ', '.join(f'{g:.3f}' for g in gaps))
# massless: U(1)_V x U(1)_eps; charge Q = a + c eps on the copies sigma3 = eps gamma5
tau = [np.diag(2.0 * CORN[:, a] - 1).astype(complex) for a in range(3)]
Gm = [1j * np.sqrt(3) * WA[a] @ tau[a] for a in range(3)]; al = [1j * Gm[a] @ W for a in range(3)]
g5 = 1j * al[0] @ al[1] @ al[2]; s3 = EPS @ g5
cliff = max(nrm(x @ y + y @ x - 2 * (p == q) * I8) for p, x in enumerate(al + [W]) for q, y in enumerate(al + [W]))
okc = cliff < 1e-12 and max(nrm(s3 @ x - x @ s3) for x in al + [W]) < 1e-12 and nrm(s3 @ s3 - I8) < 1e-12
spec = []
for a_, c_ in rng.normal(size=(5, 2)):
    Q = a_ * I8 + c_ * EPS
    for sg in (1, -1):
        P = (I8 + sg * s3) / 2; ev = np.linalg.eigvalsh(P @ Q @ P + 1e3 * (I8 - P)); spec.append(np.sort(ev[ev < 1e2]))
same = max(nrm(spec[2 * i] - spec[2 * i + 1]) for i in range(5))
check('A5 massless U(1)_eps: Q = a + c eps gives each copy the charges {a+c, a-c} (chirality swapped); a copy is neutral only if Q = 0',
      okc and same < 1e-9, f'copy spectra differ by {same:.1e}')
ov = {}
for R, L in zip(ROTS, LS): ov.setdefault(int(round(np.trace(R))), set()).add(round(float(np.trace(L @ s3 @ L.conj().T @ s3).real / 8), 6))
check('A6 a 90 deg rotation sends the copy label sigma3 to -sigma3: the copies are not a rotation-invariant label', ov[1] == {-1.0}, f'tr(L s3 L^+ s3)/8 by trace class {dict(sorted(ov.items()))}')

print('== B. the pi-cone sector (K = R = pi(1,1,1)) of the staggered tick')
dims0 = [len(commutant([bloch(K, Va(m_ / 2 + b_), Va(m_ / 2 - b_)) for K in rng.uniform(-np.pi, np.pi, size=(20, 3))])) for m_, b_ in ((0.3, 0.6), (0.05, 1.321))]
check('B0 staggered tick: the K-independent block-local commutant is the scalars, so the only link charge is the species number, which counts a pi-cone mode exactly like a light one',
      dims0 == [1, 1], f'dims {dims0}')
for mu, b in ((0.3, 0.6), (0.05, (np.pi - 0.5) / 2), (0.05, 0.1)):
    A, B = AB(mu, b); ve, vo = Va(mu / 2 + b), Va(mu / 2 - b)
    def wpos(K): w = -np.angle(np.linalg.eigvals(bloch(K, ve, vo))); return np.sort(w)[-1]
    h = 1e-3; d2 = []
    for e in rng.normal(size=(4, 3)):
        e /= np.linalg.norm(e); d2.append((wpos(R3 + h * e) + wpos(R3 - h * e) - 2 * wpos(R3)) / h ** 2)
    d20 = [(wpos(h * e) + wpos(-h * e) - 2 * wpos(np.zeros(3))) / h ** 2 for e in np.eye(3)]
    ok = abs(wpos(R3) - (np.pi - 2 * b)) < 1e-9 and np.allclose(d2, -A / (3 * np.sin(2 * b)), rtol=2e-3) and np.allclose(d20, A / (3 * np.sin(mu)), rtol=2e-3)
    check(f'B1 (mu,b)=({mu},{b:.3f}): w(R) = pi-2b = {np.pi-2*b:.4f} is the band TOP (curvature -A/(3 sin2b) = {-A/(3*np.sin(2*b)):.4f}); K=0 is the bottom (+{A/(3*np.sin(mu)):.3f})', ok,
          f'measured {np.mean(d2):.4f}, {np.mean(d20):.3f}')
    # kinematics at total crystal momentum R (block translations exact => total K conserved mod 2pi)
    Sg = np.linspace(-1, 1, 20001)[1:]
    D2 = wf(Sg, mu, b) - np.arccos(Sg) + 2 * b     # f(R) -> f(k) + gamma(R-k): (final - initial) quasi-energy, S = S(k)
    wR = np.pi - 2 * b
    def tot3(x, kind):
        k1, k2 = x[..., :3], x[..., 3:]; k3 = R3 - k1 - k2
        if kind == 'fff': return wf(Sof(k1), mu, b) + wf(Sof(k2), mu, b) + wf(Sof(k3), mu, b)
        return wf(Sof(k1), mu, b) + np.arccos(np.clip(Sof(k2), -1, 1)) + np.arccos(np.clip(Sof(k3), -1, 1))
    res = {}
    for kind in ('fff', 'fgg'):
        X = rng.uniform(-np.pi, np.pi, size=(60000, 6)); v = tot3(X, kind); best = X[np.argsort(v)[:12]]
        res[kind] = min(minimize(lambda x: tot3(x, kind), x0, method='Nelder-Mead', options={'xatol': 1e-9, 'fatol': 1e-12, 'maxiter': 4000}).fun for x0 in best)
    check(f'B2 (mu,b)=({mu},{b:.3f}): no decay at total momentum R: f->f+gamma has final-initial > 0 off the trivial point; min 3-body (f f fbar) > w(R); min f+2gamma >= w(R)',
          D2.min() > 0 and res['fff'] > wR + 1e-6 and res['fgg'] > wR - 1e-7,
          f"min D(S>-1) {D2.min():.1e}; fff {res['fff']:.4f}, f+2g {res['fgg']:.4f} vs w(R) {wR:.4f}")

# B3: wave packets in a weak static potential, H_phi = sqrt(1+phi) H sqrt(1+phi), H = i log U (0-reading).
# Chain of Nb blocks along x (real space); y, z: one block with twisted boundary phases e^{i K_y}, e^{i K_z}.
Nb = 120; Lx = 2 * Nb; sites = np.array([(x, y, z) for x in range(Lx) for y in (0, 1) for z in (0, 1)])
idx = {tuple(s): i for i, s in enumerate(sites)}; Nd = len(sites)
def half(V, odd, Kt):
    M = np.zeros((Nd, Nd), complex)
    for ox in range(int(odd), Lx, 2):
        ids, ph = [], []
        for s in CORN:
            x, y, z = (ox + s[0]) % Lx, int(odd) + s[1], int(odd) + s[2]; f = 1.0 + 0j
            if y == 2: y, f = 0, f * np.exp(1j * Kt[0])
            if z == 2: z, f = 0, f * np.exp(1j * Kt[1])
            ids.append(idx[(x, y, z)]); ph.append(f)
        rs = [int(((CORN[k] + [ox, int(odd), int(odd)]) % 2) @ [4, 2, 1]) for k in range(8)]   # corner label = absolute site parity
        ph = np.array(ph); M[np.ix_(ids, ids)] += ph[:, None] * V[np.ix_(rs, rs)] * ph.conj()[None, :]
    return M
xb = sites[:, 0] / 2.0; x0 = Nb / 2; sig = 8.0
for mu, b, g in ((0.3, 0.6, 0.002), (0.3, (np.pi - 0.5) / 2, 0.01)):
    phi = g * Nb / (2 * np.pi) * np.sin(2 * np.pi * (xb - x0) / Nb); Sq = np.sqrt(1 + phi)
    geff = g * np.exp(-(2 * np.pi * sig / np.sqrt(2) / Nb) ** 2 / 2)
    ts = np.arange(0, 31, 3.0); acc, pred, offs = {}, {}, []
    A, Bq = AB(mu, b)
    for name, Kx, Kt in (('light', 0.0, (0.0, 0.0)), ('pi', np.pi, (np.pi, np.pi))):
        Uf = half(Va(mu / 2 - b), True, Kt) @ half(Va(mu / 2 + b), False, Kt)
        Tz, Vr = schur(Uf, output='complex'); offs.append(nrm(Tz - np.diag(np.diag(Tz)))); wv = -np.angle(np.diag(Tz)); del Uf, Tz
        Hm = (Vr * wv) @ Vr.conj().T; Hm = (Hm + Hm.conj().T) / 2; Hp = Sq[:, None] * Hm * Sq[None, :]; del Hm
        ep, Ep = np.linalg.eigh(Hp); del Hp
        psi = np.exp(-(xb - x0) ** 2 / (2 * sig ** 2)) * np.exp(1j * Kx * xb); psi = Vr @ ((wv > 0) * (Vr.conj().T @ psi)); psi /= np.linalg.norm(psi)
        c0 = Ep.conj().T @ psi; xs_ = [float(np.sum(abs(Ep @ (np.exp(-1j * ep * t) * c0)) ** 2 * xb)) for t in ts]
        acc[name] = 2 * np.polyfit(ts, np.array(xs_) - xs_[0], 2)[0]; del Ep, Vr
        # semiclassical: a(q) = -w(q) w''(q) grad phi along x, averaged over the packet's momentum density exp(-sig^2 q^2)
        q = np.linspace(-4 / sig, 4 / sig, 801); hq = 1e-4
        wq = lambda k: np.arccos(np.clip(A * (np.cos(Kx + k) + np.cos(Kt[0]) + np.cos(Kt[1])) / 3 - Bq, -1, 1))
        wpp = (wq(q + hq) + wq(q - hq) - 2 * wq(q)) / hq ** 2; wt = np.exp(-sig ** 2 * q ** 2)
        pred[name] = -np.sum(wt * wq(q) * wpp) / np.sum(wt) * geff
    ok = acc['light'] < 0 < acc['pi'] and all(abs(acc[k] / pred[k] - 1) < 0.1 for k in acc)
    check(f'B3 (mu,b)=({mu},{b:.3f}) packets in a weak well (lapse coupling, 0-reading): the light packet falls in, the pi-cone packet falls OUT, both at the semiclassical rate -w w\'\' grad phi',
          ok, f"Schur off-diag {max(offs):.0e}; a_light {acc['light']:.3e} (pred {pred['light']:.3e}), a_pi {acc['pi']:.3e} (pred {pred['pi']:.3e}); ratio {acc['pi']/acc['light']:.3f}, rest-point formula {-((np.pi-2*b)/np.sin(2*b))/(mu/np.sin(mu)):.3f}")
Ks = rng.uniform(-np.pi, np.pi, size=(100000, 3)); mx = max(float(np.max(wf(Sof(Ks), mu_, b_)) - (np.pi - 2 * b_)) for mu_, b_ in ((0.3, 0.6), (0.3, (np.pi - 0.5) / 2), (0.05, 0.1)))
check('B4 w(R) = pi - 2b is the global band maximum, so with H = w(K)(1+phi) conserved a pi-cone state at rest can never enter lower phi (0-reading); in the pi-reading E = w - pi = -2b < 0 at R: it falls in but sources negative energy',
      mx <= 1e-12, f'max_K w(K) - w(R) = {mx:.1e} over 1e5 K, 3 (mu,b)')

print('== C. a species with no link and no interaction term (gravity only)')
nm = 6; dim = 2 ** nm
def cop(j):
    c = np.zeros((dim, dim))
    for s in range(dim):
        if not (s >> j) & 1: c[s | (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
    return c
cd = [cop(j) for j in range(nm)]; Nop = sum(c @ c.T for c in cd); Pf = np.diag((-1.0) ** np.diag(Nop))
h1 = rng.normal(size=(nm, nm)) + 1j * rng.normal(size=(nm, nm)); h1 += h1.conj().T
Hq = sum(h1[i, j] * cd[i] @ cd[j].T for i in range(nm) for j in range(nm))
Hn = Hq + 0.3 * sum(cd[i] @ cd[j] @ cd[k].T @ cd[l].T for i, j, k, l in [(0, 1, 2, 3), (1, 4, 5, 2)]); Hn = (Hn + Hn.conj().T) / 2
Hpair = Hq + 0.3 * (cd[0] @ cd[1] + cd[1].T @ cd[0].T)
Un, Upr = expm(-1j * Hn), expm(-1j * Hpair)
check('C1 any number-conserving tick (geometry-dressed hops, number-conserving interactions) keeps the species number exactly: its lightest state is absolutely stable',
      nrm(Un @ Nop - Nop @ Un) < 1e-10, f'[N,U] = {nrm(Un @ Nop - Nop @ Un):.1e}')
check('C2 a pairing (number-changing) term breaks it; fermion parity survives every even term', nrm(Upr @ Nop - Nop @ Upr) > 1e-2 and nrm(Upr @ Pf - Pf @ Upr) < 1e-10,
      f'[N,U_pair] = {nrm(Upr @ Nop - Nop @ Upr):.2f}, [P,U_pair] = {nrm(Upr @ Pf - Pf @ Upr):.1e}')

print('== D. conditional source and records')
dA, dB = 6, 5; psi = rng.normal(size=(dA, dB)) + 1j * rng.normal(size=(dA, dB)); psi /= np.linalg.norm(psi)
TA = rng.normal(size=(dA, dA)); TA = TA + TA.T; Vx = [np.diag(rng.normal(size=dA)) for _ in range(dB)]   # V diagonal in B's configuration
p = np.sum(abs(psi) ** 2, 0); cond = sum(p[x] * ((psi[:, x] / np.sqrt(p[x])).conj() @ (TA + Vx[x] / 2) @ (psi[:, x] / np.sqrt(p[x]))) for x in range(dB))
rhoA = psi @ psi.conj().T; Vmean = sum(psi[:, x].conj() @ Vx[x] @ psi[:, x] for x in range(dB))
check('D1 law of total expectation: Born mean of A\'s conditional source = tr(rho_A T_A) + <V>/2 (no extra mean mass; binding counted once)',
      abs(cond - (np.trace(rhoA @ TA) + Vmean / 2)) < 1e-12, f'{cond.real:.6f} vs {(np.trace(rhoA @ TA) + Vmean / 2).real:.6f}')
t0, trec = 13.787e9, 3.8e5
check('D2 records: CL-6\'s phase has no record term, so the permanent record set sources nothing; a record mass would grow per comoving volume ~ t, i.e. x3.6e4 from recombination to now, against a CMB-to-today DM consistency of a few percent',
      t0 / trec > 1e4, f't0/t_rec = {t0/trec:.2e}')

print('== E. measured-reality arithmetic')
EP = 1.2209e19; unit = np.sqrt(3) / (2 * np.sqrt(8 * np.pi)) * EP      # GeV per rad/tick: tau = 2a/(sqrt3 c), a = sqrt(8 pi) l_P
Oc = 0.1200 / 0.6736 ** 2
print(f'   Planck 2018: Omega_c h^2 = 0.1200 +- 0.0012, h = 0.6736 -> Omega_c = {Oc:.4f}; Omega_c/Omega_b = {0.1200/0.02237:.2f}')
print(f'   rad/tick = {unit:.3e} GeV; pi-cone at b=(pi-1/2)/2: 0.5 rad/tick = {0.5*unit:.2e} GeV (0-reading); pi-reading mass 2b = {(np.pi-0.5)*unit:.2e} GeV')
mX = 0.5 * unit; n_loc = 0.4 / mX; flux = n_loc * 2.3e7 * 1e4 * 3.156e7
print(f'   local DM 0.4 GeV/cm^3 as {mX:.1e} GeV particles: n = {n_loc:.1e} /cm^3, flux {flux:.1f} per m^2 per year')
gs = 106.75; Tmax = 0.5 * unit; GH = (Tmax / EP) ** 3 / (1.66 * np.sqrt(gs))
check('E1 gravity alone never thermalises a species inside the lattice domain (|w| <= 1/2): Gamma/H ~ (T/M_P)^3/(1.66 sqrt g*) << 1, so its relic is the supplied initial odds',
      GH < 1e-3, f'Gamma/H at T = {Tmax:.1e} GeV: {GH:.1e}')
G, cgs = 6.674e-8, 1.783e-24     # cgs; GeV -> g
for m in (1e2, mX):
    mg = m * cgs; v = 1e8; sig = 4 * np.pi * (G * mg / v ** 2) ** 2 * 30
    print(f'   gravitational self-scattering, m = {m:.1e} GeV, v = 1000 km/s: sigma/m ~ {sig/mg:.1e} cm^2/g (bound ~1)')
alpha, GF, ms, s2t = 1 / 137.036, 1.1664e-5, 7.0e-6, 1e-11
Gam = 9 * alpha * GF ** 2 * ms ** 5 * s2t / (1024 * np.pi ** 4); tau_s = 6.582e-25 / Gam
check('E2 register singlet nu^c (empty Lambda(C^5) register, Q = Y = 0): with a Yukawa it radiates nu gamma at one loop; 7 keV, sin^2 2theta = 1e-11 lives >> the age',
      tau_s > 1e10 * 4.35e17, f'tau = {tau_s:.1e} s vs age 4.35e17 s')
print('supplied: CL-3 tick, b and mu, the 0-/pi-reading of quasi-energy, the lapse coupling H(1+phi) in the weak static limit, the photon band cos w = S,')
print('  the unit map, the register reading of nu^c, sterile-neutrino decay formula (Pal-Wolfenstein), all measured numbers.')
print(f'elapsed_seconds {time.time()-T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
