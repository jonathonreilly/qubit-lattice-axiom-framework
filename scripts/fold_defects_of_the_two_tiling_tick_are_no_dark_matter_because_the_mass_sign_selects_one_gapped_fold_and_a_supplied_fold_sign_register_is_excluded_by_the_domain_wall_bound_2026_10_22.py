AUDIT_INPUT_PATHS = ('docs/FOLD_DEFECTS_OF_THE_TWO_TILING_TICK_ARE_NO_DARK_MATTER_BECAUSE_THE_MASS_SIGN_SELECTS_ONE_GAPPED_FOLD_AND_A_SUPPLIED_FOLD_SIGN_REGISTER_IS_EXCLUDED_BY_THE_DOMAIN_WALL_BOUND_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Fold defects of CL-1's two-tiling tick as dark-matter candidates.

Finite exact diagnostics on single-particle two-tiling ticks (8-site cube hop with face phases -1, even step
eps - mu/2, odd step eps + mu/2, copy mass M, diagonal metric weights), Bloch 2^3 cells, Lx x 2 x 2 slabs with
transverse twists, and a 10^3 torus. Seeded, self-contained (numpy + scipy).
"""
import itertools
import signal
import sys
import time

import numpy as np
from scipy.linalg import expm, schur

AUDIT_TIMEOUT_SEC = 120
signal.signal(signal.SIGALRM, lambda *a: (print("TIMEOUT"), sys.exit(2)))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f"\n     [{vals}]" if vals else ""))


EPS = 0.3
Cc = np.array(list(itertools.product((0, 1), repeat=3)))


def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d):
        Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]


J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * Cc[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        dd = Cc[a] - Cc[b]
        if np.sum(dd ** 2) == 1:
            g = XI[a].conj() @ XI[b]; Wi[int(np.argmax(abs(dd)))][a, b] = -g / abs(g)
RI = Wi  # R_i = sqrt3 W_i: unit-modulus axis hops


def cube_ops(w):
    R = sum(w[i] * RI[i] for i in range(3)) / np.linalg.norm(w)
    return R, 1j * RI[0] @ RI[1] @ RI[2] @ R


def build(L, k, w=(1.0, 1.0, 1.0)):
    """two tilings of the L torus by 2^3 cubes, Bloch twist k per wrap; returns sites, (R, s, cubes) per tiling"""
    Rc, Sc = cube_ops(np.array(w, float))
    sites = list(itertools.product(*[range(n) for n in L])); ix = {s: i for i, s in enumerate(sites)}; N = len(sites)
    out = []
    for off in (0, 1):
        R = np.zeros((N, N), complex); Sm = np.zeros((N, N), complex); cubes = {}
        for c in itertools.product(*[range(off, off + n, 2) for n in L]):
            mem, ph, lab = [], [], []
            for o in Cc:
                p = [c[d] + o[d] for d in range(3)]
                mem.append(ix[tuple(p[d] % L[d] for d in range(3))])
                ph.append(np.exp(1j * sum(k[d] * (p[d] // L[d]) for d in range(3))))
                lab.append((p[0] % 2) * 4 + (p[1] % 2) * 2 + (p[2] % 2))
            ph = np.array(ph); P = np.ix_(mem, mem); Q = np.ix_(lab, lab); phm = np.outer(ph.conj(), ph)
            R[P] += phm * Rc[Q]; Sm[P] += phm * Sc[Q]; cubes[c] = mem
        out.append((R, Sm, cubes))
    return sites, N, out


def tick(RE, RO, SE, aE, bO, M=0.0, P=None):
    N = RE.shape[0]
    UE = np.diag(np.cos(aE)) - 1j * np.diag(np.sin(aE)) @ RE
    UO = np.diag(np.cos(bO)) + 1j * np.diag(np.sin(bO)) @ RO
    if P is not None:
        UE = np.diag(P) @ UE @ np.diag(P)
    if M:
        CM = expm(1j * (M / 4) * (np.eye(N) - SE) @ RE); return UO @ CM @ UE @ CM
    return UO @ UE


def qe(U): return -np.angle(np.linalg.eigvals(U))


def Evac(om): return float(om[om < 0].sum())


def bloch_U(mu, k, M=0.0, w=(1, 1, 1), D=0.0):
    sites, N, ((RE, SE, _), (RO, _, _)) = build((2, 2, 2), k, w)
    P = np.exp(-1j * D / 2 * np.array([(-1) ** sum(s) for s in sites])) if D else None
    return tick(RE, RO, SE, np.full(N, EPS - mu / 2), np.full(N, EPS + mu / 2), M, P)


def kgrid(n, d=3): return list(itertools.product(2 * np.pi * np.arange(n) / n, repeat=d))


print("== A. the fold's vacuum manifold under CL-1 (what a defect would have to wind)")
cl = max(np.abs(RI[i] @ RI[j] + RI[j] @ RI[i] - 2 * (i == j) * np.eye(8)).max() for i in range(3) for j in range(3))
lap = RNG.uniform(0.3, 3.0, (200, 3)); Nl = np.sin(EPS) / (np.sqrt(3) * np.sqrt(np.mean(lap, axis=1)))
K8 = kgrid(6); sp = 0.0; gp = 9.0
for k in K8:
    a1, a2 = qe(bloch_U(0.2, k)), qe(bloch_U(-0.2, k)); sp = max(sp, np.abs(np.sort(a1) - np.sort(a2)).max())
    gp = min(gp, np.abs(a1).min())
check(cl < 1e-13 and Nl.min() > 0 and sp < 1e-12 and abs(gp - 0.2) < 1e-9, "A1 [T]",
      "law text: mu = mN with m >= 0 and the lapse N = sin(eps0)/(sqrt3 rms sqrt(gamma^ii)) > 0 in every cube, so every "
      "species' mass angle has ONE sign everywhere; mu -> -mu is the (1,1,1) image (equal spectra), and the vacuum "
      "at fixed sign is unique with gap |mu|: the fold is explicitly selected, not spontaneously chosen",
      f"Clifford defect {cl:.0e}; min lapse over 200 metrics {Nl.min():.3f}; |spec(mu)-spec(-mu)| {sp:.0e}; gap {gp:.6f}")

rows = []; ok = True
for t in range(8):
    mu = RNG.uniform(0.02, 0.3); M = RNG.uniform(0.0, 0.25); w = RNG.uniform(0.5, 2.0, 3)
    g = min(np.abs(qe(bloch_U(mu, k, M, w))).min() for k in kgrid(6))
    rows.append(g / mu); ok &= g > 0.5 * mu
check(ok, "A2 [D+T]",
      "every CL-1 parameter (mu > 0, copy mass M, diagonal metric) keeps the tick gapped (sampled), and that "
      "parameter space (interval x interval x convex PD(3)) is contractible: any register texture deforms to the "
      "uniform vacuum without closing the gap, so pi_0 = pi_1 = pi_2 = 0 -- no topological fold wall, string or point",
      "gap/mu over 8 random (mu, M, metric): " + ", ".join(f"{r:.3f}" for r in rows))

wf = {}
for mu in (0.05, 0.1, 0.2):
    dE = 0.0
    for k in kgrid(8):
        Tm, V = schur(bloch_U(mu, k), output='complex'); om = -np.angle(np.diag(Tm)); H = V @ np.diag(om) @ V.conj().T
        Tm2, V2 = schur(bloch_U(-mu, k), output='complex'); om2 = -np.angle(np.diag(Tm2)); occ = V2[:, om2 < 0]
        dE += np.trace(occ.conj().T @ H @ occ).real - om[om < 0].sum()
    wf[mu] = dE / (8 * 8 ** 3)
check(all(v > 0 for v in wf.values()) and 1.0 < wf[0.05] / 0.05 ** 2 < 2.0, "A3 [D]",
      "the other fold (the -mu vacuum, i.e. the (1,1,1)-shifted fold) is not degenerate: under the +mu tick it costs "
      "~1.4 mu^2 per site, so a wrong-fold region is an excited state with a volume cost, not a second vacuum",
      "cost per site / mu^2: " + ", ".join(f"mu={m}: {v/m**2:.3f}" for m, v in wf.items()))

L6 = 6
off2 = RNG.integers(0, 2, (L6, L6, L6)); off8 = RNG.integers(0, 8, (L6, L6, L6))
def burg(f):
    tot = 0
    for ax in itertools.combinations(range(3), 2):
        e1 = np.eye(3, dtype=int)[ax[0]]; e2 = np.eye(3, dtype=int)[ax[1]]
        for p in itertools.product(range(L6), repeat=3):
            q = [tuple((np.array(p) + v) % L6) for v in (0 * e1, e1, e1 + e2, e2)]
            tot += np.bitwise_xor.reduce([f[q[i]] ^ f[q[(i + 1) % 4]] for i in range(4)]) != 0
    return tot
def junc(f):
    n = 0
    for p in itertools.product(range(L6), repeat=3):
        e = np.eye(3, dtype=int); q = [tuple((np.array(p) + v) % L6) for v in (0 * e[0], e[0], e[0] + e[1], e[1])]
        n += len({f[x] for x in q}) >= 3
    return n
b2, b8, j2, j8 = burg(off2), burg(off8), junc(off2), junc(off8)
check(b2 == 0 and b8 == 0 and j2 == 0 and j8 > 0, "A4 [T]",
      "a fold offset is a single-valued function on the fixed Z^3 sites, so its jumps sum to zero around every loop: "
      "no Burgers charge, no free dislocation of the fold (it would need a dislocated lattice, which the axioms "
      "forbid); with CL-1's two tilings no three-domain junction exists; even an 8-offset fold has junction lines "
      "only as wall junctions, never as free strings",
      f"plaquette Burgers sums != 0: 2-offset {b2}, 8-offset {b8}; 3-domain junction plaquettes: {j2}, {j8}")
print(f"   (t = {time.time()-T0:.1f} s)")

print("== B. if the mass sign were a register: mu-sign walls (supplied profiles)")
def slab(Lx, k, mufun, M=0.0, Dfun=None):
    sites, N, ((RE, SE, cE), (RO, _, cO)) = build((Lx, 2, 2), (0.0, k[0], k[1]))
    a = np.zeros(N); b = np.zeros(N)
    for c, mem in cE.items(): a[mem] = EPS - mufun(c[0] + 0.5) / 2
    for c, mem in cO.items(): b[mem] = EPS + mufun(c[0] + 0.5) / 2
    P = np.array([np.exp(-1j * Dfun(s[0]) / 2 * (-1) ** sum(s)) for s in sites]) if Dfun else None
    return qe(tick(RE, RO, SE, a, b, M, P))
LX = 32; m0 = 0.2
step = lambda x: m0 if (x % LX) < LX / 2 else -m0
om0 = slab(LX, (0, 0), step); z0 = int((np.abs(om0) < 1e-8).sum())
disp = [np.sort(np.abs(slab(LX, (q, 0), step)))[0] for q in (0.05, 0.1)]
check(z0 == 8 and abs(disp[1] / disp[0] - 2) < 0.1, "B1 [D]",
      "a sharp mu-sign wall (M = 0) binds Jackiw-Rebbi modes: 4 zero modes per wall at zero transverse momentum, "
      "dispersing linearly (2+1D Dirac cones of the two copies)",
      f"Lx = {LX}, two walls, mu = +-{m0}: zero modes {z0}; lowest |w| at q = 0.05, 0.1: {disp[0]:.4f}, {disp[1]:.4f}")

gq = min(np.abs(qe(bloch_U(0.1, k, D=0.1))).min() for k in kgrid(6))
def theta(x, wd):
    x = x % LX
    if LX / 4 < x < 3 * LX / 4: return np.pi * np.clip((x - LX / 2 + wd / 2) / wd, 0, 1)
    return np.pi * (1 - np.clip(((x - LX) if x >= 3 * LX / 4 else x) / wd + 0.5, 0, 1))
DSC = 1 / 0.955
rot = {}
for wd in (4, 8):
    mf = lambda x, wd=wd: m0 * np.cos(theta(x, wd)); Df = lambda x, wd=wd: m0 * DSC * np.sin(theta(x, wd))
    rot[wd] = min(np.abs(slab(LX, k, mf, 0.0, Df)).min() for k in [(0, 0), (0.2, 0), (0.2, 0.2)])
check(abs(gq - 0.13826) < 2e-4 and rot[4] > 0.4 * m0 and rot[8] > rot[4], "B2 [D]",
      "the index is not protected: a staggered on-site phase D (a second Dirac-mass direction, adding in quadrature) "
      "lets the wall rotate mu -> -mu through D without closing the gap; the bound modes leave",
      f"uniform gap at mu = D = 0.1: {gq:.5f} (= sqrt(0.1^2 + 0.0955^2)); rotating wall min gap w=4: {rot[4]:.4f}, "
      f"w=8: {rot[8]:.4f} (sharp flip: 0)")

sitesB, NB, ((REb, SEb, cEb), (ROb, _, cOb)) = build((10, 10, 10), (0.0, 0.0, 0.0))
bub = {}
for side in (0, 4):
    lo = (10 - side) / 2; hi = lo + side; inside = lambda c: side and all(lo < c[d] + 1 < hi for d in range(3))
    a = np.zeros(NB); b = np.zeros(NB)
    for c, mem in cEb.items(): a[mem] = EPS - (-0.3 if inside(c) else 0.3) / 2
    for c, mem in cOb.items(): b[mem] = EPS + (-0.3 if inside(c) else 0.3) / 2
    s_ = np.sort(np.abs(qe(tick(REb, ROb, SEb, a, b)))); bub[side] = (s_[0], int((s_ < 0.27).sum()))
del REb, ROb, SEb
check(abs(bub[0][0] - 0.3) < 1e-9 and bub[4][0] > 0.05 and bub[4][1] > 0, "B3 [D]",
      "a CLOSED mu-sign bubble has no zero mode (the 2+1D Dirac index on a closed wall without link flux is zero): "
      "its in-gap levels are ordinary species states, not a conserved defect number",
      f"10^3 torus, mu = +-0.3: lowest |w| uniform {bub[0][0]:.4f}; cubic bubble of side 4: {bub[4][0]:.4f} with "
      f"{bub[4][1]} in-gap states")

LT = 48; sig = {}
for m in (0.05, 0.1, 0.2, 0.4):
    st = lambda x, m=m: m if (x % LT) < LT / 2 else -m; un = lambda x, m=m: m
    sig[m] = np.mean([Evac(slab(LT, k, st)) - Evac(slab(LT, k, un)) for k in kgrid(8, 2)]) / 8
cs = {m: v / m ** 2 for m, v in sig.items()}
check(all(v > 0 for v in sig.values()) and 0.3 < min(cs.values()) and max(cs.values()) < 1.0
      and cs[0.05] > cs[0.1] > cs[0.2], "B4 [D]",
      "wall tension of a sharp mu-sign wall: sigma ~ c mu^2 per site^2 with c ~ 0.4-0.7 slowly rising as mu -> 0 "
      "(UV-sensitive thin wall: sigma ~ m^2/a, not m^3)",
      "sigma/mu^2: " + ", ".join(f"mu={m}: {v:.3f}" for m, v in cs.items()))

G = 2
fb = {m: (12 * np.pi * sig[m] / G) ** (1 / 3) / m for m in sig}
check(all(v > 1 for v in fb.values()), "B5 [T+D]",
      "Fermi-ball test: N wall fermions (g = 2 cones per wall) on a sphere minimise 4 pi sigma R^2 + (2/3) N^1.5 "
      "/(sqrt(g) R) at E/N = (12 pi sigma/g)^(1/3); bound only if E/N < |mu|. It fails at every mu (it would need "
      "mu > 12 pi c/g ~ 5, beyond the 2 eps = 0.6 limit): wall fermions escape and bubbles collapse",
      "(E/N)/mu: " + ", ".join(f"mu={m}: {v:.2f}" for m, v in fb.items()))
print(f"   (t = {time.time()-T0:.1f} s)")

print("== C. abundance and measurement (estimates; unit map and bounds supplied)")
E0 = 2.1e18; IA = 2.43e18; MPL = 1.22e19; H0 = 1.44e-42
c0 = cs[0.05]
def sig_phys(m): return c0 * m * m * IA ** 2 / E0
def om_wall(s): return 8 * np.pi * s / (3 * MPL ** 2 * H0)
zko = 1e-9
print(f"   sigma_phys^(1/3) = (c m^2 (1/a)^2 / E0)^(1/3), c = {c0:.2f}: electron {sig_phys(5.11e-4)**(1/3):.2e} GeV, "
      f"nu (0.05 eV) {sig_phys(5e-11)**(1/3):.2e}, top {sig_phys(173.)**(1/3):.2e}; ZKO/CMB: sigma < (1 MeV)^3")
print(f"   scaling-network Omega_w ~ 8 pi sigma/(3 M_P^2 H0): electron {om_wall(sig_phys(5.11e-4)):.1e}, "
      f"nu {om_wall(sig_phys(5e-11)):.1e}; walls have w = -2/3, never cold matter")
check(sig_phys(5e-11) > zko and om_wall(sig_phys(5e-11)) > 1, "C1 [E]",
      "if any species' mass sign were a register, even a 0.05 eV neutrino's walls would exceed the domain-wall "
      "bound (sigma < (1 MeV)^3) and overclose; a supplied fold-sign register is excluded by measurement",
      f"nu wall sigma/(1 MeV)^3 = {sig_phys(5e-11)/zko:.1e}; electron {sig_phys(5.11e-4)/zko:.1e}")
print("   law text (passing): a split carries the update's vacuum onto the children's vacuum and each excitation onto")
print("   the lowest of the same charges, so a split re-seeds the SAME fold: Kibble-Zurek defect density zero.")
print(f"   (t = {time.time()-T0:.1f} s)")
print(f"TOTAL: PASS={NP} FAIL={NF}")
