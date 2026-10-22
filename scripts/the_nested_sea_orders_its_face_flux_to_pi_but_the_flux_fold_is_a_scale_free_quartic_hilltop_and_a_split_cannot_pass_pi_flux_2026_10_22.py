AUDIT_INPUT_PATHS = ('docs/THE_NESTED_SEA_ORDERS_ITS_FACE_FLUX_TO_PI_BUT_THE_FLUX_FOLD_IS_A_SCALE_FREE_QUARTIC_HILLTOP_AND_A_SPLIT_CANNOT_PASS_PI_FLUX_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Face-flux fold: the half-filled sea's energy and stiffness against the face flux Phi (0 -> pi), slow roll,
passing through a split, exit and the flux sign (finite runner, seeded, self-contained).

  A  energy landscape E(Phi) of the half-filled nearest-neighbour cubic sea at uniform face-flux magnitude Phi
     along three paths (uniform field, scaled Kogut-Susskind stripes S, nesting pattern N), plus random flux
  B  the stiffness (Inglis cranking mass) along S and N; the nested surface, nodal lines, Dirac points
  C  slow roll on path S from the computed potential and stiffness (no free kinetic constant)
  D  passing: a split that keeps parent loop holonomies cannot pass pi flux per face
  E  exit and reheating; F  the flux sign
Supplied numbers are named in the output. Measured numbers enter only C.
"""
import time
import itertools
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
PI = np.pi
NS_PL, NS_SIG, AS_PL, RMAX = 0.9649, 0.0042, 2.1e-9, 0.036
E3 = np.eye(3, dtype=int)


def check(ok, tag, text, vals=""):
    global NP, NF
    ok = bool(ok)
    NP += ok
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}" + (f"  {vals}" if vals else ""))


# ------------------------------------------------ Bloch form on the 2^3 cell (8 sublattices), hop -exp(iA)
SUB = np.array(list(itertools.product((0, 1), repeat=3)))
def lab(p): return int((p[0] % 2) * 4 + (p[1] % 2) * 2 + p[2] % 2)


def H8(Af, ks):
    H = np.zeros((len(ks), 8, 8), complex)
    for i, s in enumerate(SUB):
        for mu in range(3):
            t = s + E3[mu]; j = lab(t); R = (t - (t % 2)) // 2
            ph = -np.exp(1j * Af(mu, s)) * np.exp(2j * ks @ R)
            H[:, j, i] += ph; H[:, i, j] += ph.conj()
    return H


def kgrid(L):
    k = (np.arange(L) + 0.5) / L * PI
    return np.stack(np.meshgrid(k, k, k, indexing='ij'), -1).reshape(-1, 3)


def E8(Af, L, ch=16000):
    ks = kgrid(L); s = 0.0
    for i in range(0, len(ks), ch):
        ev = np.linalg.eigvalsh(H8(Af, ks[i:i + ch])); s += np.sum(np.where(ev < 0, ev, 0))
    return s / len(ks) / 8


def Zc(Afam, Phi, L, ch=8000, h=1e-6):
    """Inglis cranking mass per site, M = 2 sum |<b|dH/dPhi|a>|^2/(E_b - E_a)^3 over particle-hole pairs."""
    ks = kgrid(L); Z = 0.0
    for i in range(0, len(ks), ch):
        k = ks[i:i + ch]; H = H8(Afam(Phi), k); D = (H8(Afam(Phi + h), k) - H8(Afam(Phi - h), k)) / (2 * h)
        ev, U = np.linalg.eigh(H)
        M = np.abs(np.einsum('kia,kij,kjb->kab', U.conj(), D, U)) ** 2
        occ = ev < 0; dE = np.abs(ev[:, None, :] - ev[:, :, None]) + 1e-300
        with np.errstate(divide='ignore', invalid='ignore'):
            Z += 2 * np.sum(np.where(occ[:, :, None] & (~occ[:, None, :]), M / dE ** 3, 0))
    return Z / len(ks) / 8


def gapless(Afp, n):
    ev = np.linalg.eigvalsh(H8(Afp, kgrid(n)))
    return int(np.sum(np.min(np.abs(ev), 1) < 1.5 * PI / n))


# path S: scaled Kogut-Susskind field in the zero-mean gauge, A_y = (Phi/2)(-1)^x, A_z = (Phi/2)(-1)^(x+y)
AS = lambda Phi: (lambda mu, s: [0.0, 0.5 * Phi * (-1) ** s[0], 0.5 * Phi * (-1) ** (s[0] + s[1])][mu])

# separable divergence-free face-sign patterns sigma_p(r) = s_p (-1)^(v_p.r) on the 2^3 cell; A solves dA = Phi sigma
VS = [np.array(v) for v in itertools.product((0, 1), repeat=3) if any(v)]
PL = [(0, 1), (1, 2), (2, 0)]


def solveA(pat):
    A = {}
    for vt in {tuple(v) for _, v in pat}:
        v = np.array(vt); M = np.zeros((3, 3)); F = np.zeros(3)
        for p, (mu, nu) in enumerate(PL):
            M[p, nu] += -2 * v[mu]; M[p, mu] += 2 * v[nu]
            if tuple(pat[p][1]) == vt: F[p] = PI * pat[p][0]
        a = np.linalg.lstsq(M, F, rcond=None)[0]
        if np.max(np.abs(M @ a - F)) > 1e-9: return None
        A[vt] = a
    return A


def Afam_of(A):
    return lambda Phi: (lambda mu, s: (Phi / PI) * sum(a[mu] * (-1) ** int(np.dot(v, s)) for v, a in A.items()))


def face_mags(Af):
    out = []
    for r in SUB:
        for mu, nu in PL:
            g = lambda m, x: Af(m, np.array(x) % 2)
            out.append(abs(g(mu, r) + g(nu, r + E3[mu]) - g(mu, r + E3[nu]) - g(nu, r)))
    return np.array(out)


# path U: uniform field B = (Phi,Phi,Phi), A_x = Phi (x - y), A_z = -Phi (x - y), Phi = 2 pi p/q (q-site cell)
def EU(p, q, N=24):
    Phi = 2 * PI * p / q
    def dec(s):
        d = s[0] - s[1]; w = d % q; return w, np.array([s[1], s[2], (d - w) // q])
    th = (np.arange(N) + 0.5) / N * 2 * PI; N3 = max(2, int(np.ceil(N / q))); th3 = (np.arange(N3) + 0.5) / N3 * 2 * PI
    TH = np.stack([g.ravel() for g in np.meshgrid(th, th, th3, indexing='ij')], 1)
    H = np.zeros((len(TH), q, q), complex)
    for w in range(q):
        s = np.array([w, 0, 0]); _, n0 = dec(s)
        for mu in range(3):
            w2, n2 = dec(s + E3[mu]); ph = -np.exp(1j * [Phi * w, 0.0, -Phi * w][mu]) * np.exp(1j * TH @ (n2 - n0))
            H[:, w2, w] += ph; H[:, w, w2] += ph.conj()
    ev = np.linalg.eigvalsh(H)
    return np.sum(np.where(ev < 0, ev, 0)) / len(TH) / q


def torus_E(L, sign_fn):
    """half-filled energy per site of -sum s_l (c^dag c + h.c.) on an L^3 torus with link factors sign_fn(r, mu)"""
    V = L ** 3; idx = lambda r: (r[0] % L) * L * L + (r[1] % L) * L + r[2] % L
    M = np.zeros((V, V), complex)
    for r in itertools.product(range(L), repeat=3):
        for mu in range(3):
            t = list(r); t[mu] += 1; a, b = idx(r), idx(t); f = sign_fn(r, mu)
            M[b, a] += -f; M[a, b] += -np.conj(f)
    ev = np.linalg.eigvalsh(M)
    return float(np.sum(ev[:V // 2]) / V)


print(f"AUDIT_TIMEOUT_SEC = {AUDIT_TIMEOUT_SEC}; seed 20261022; hop 1, half filling, energies per site; supplied in C: "
      "J a = sqrt3, M_P a = 1 at the flat rung (reduced Planck), N* = 55; Planck n_s = 0.9649 +- 0.0042, A_s = 2.1e-9")
print("== A. energy landscape E(Phi) at uniform face-flux magnitude Phi")
eS0, eSpi = E8(AS(0.0), 40), E8(AS(PI), 40)
check(abs(eS0 + 1.002420) < 2e-5 and abs(eSpi + 1.193801) < 2e-5, "A1 [D]",
      "end points reproduce the main flux-sector note (Theorem 6 Bloch integrals): zero flux and pi flux",
      f"E(0) = {eS0:.5f}, E(pi) = {eSpi:.5f}, Lieb gain {eS0 - eSpi:.5f}")
pats = []
for c in itertools.product(range(7), (1, -1), range(7), (1, -1), range(7), (1, -1)):
    pat = [(c[1], VS[c[0]]), (c[3], VS[c[2]]), (c[5], VS[c[4]])]
    A = solveA(pat)
    if A is not None: pats.append((pat, A))
e1 = [E8(Afam_of(A)(PI), 6) for _, A in pats]
e02 = np.array([E8(Afam_of(A)(0.2 * PI), 10) for _, A in pats])
hasQ = [any(v == (1, 1, 1) and np.ptp(a) > 1e-9 for v, a in A.items()) for _, A in pats]
best = np.flatnonzero(e02 < e02.min() + 1e-9)
AN = Afam_of(pats[best[0]][1])
magsN, magsS = face_mags(AN(0.3 * PI)), face_mags(AS(0.3 * PI))
check(np.ptp(e1) < 1e-10 and all(hasQ[i] for i in best) and np.ptp(magsN) < 1e-12 and np.ptp(magsS) < 1e-12, "A2 [T+D]",
      "divergence-free separable face-sign patterns on the 2^3 cell (|flux| = Phi on every face, zero mean, local A): all "
      "reach the same pi-flux class at Phi = pi; the lowest at Phi = 0.2 pi is the pattern family carrying the nesting "
      "vector (pi,pi,pi) (path N; cubic images degenerate)",
      f"{len(pats)} patterns, E(pi) spread {np.ptp(e1):.1e}; lowest {len(best)} at {e02.min():.5f}, all with (pi,pi,pi): "
      f"{all(hasQ[i] for i in best)}; |face flux| = 0.3 pi exactly on N and S")
fr = [0.25, 0.5, 0.75]
rowS = [E8(AS(f * PI), 24) for f in fr]; rowN = [E8(AN(f * PI), 24) for f in fr]
rowU = [EU(1, 8), EU(1, 4), EU(3, 8)]
check(all(n < s < u for n, s, u in zip(rowN, rowS, rowU)) and all(np.diff([eS0] + rowN + [eSpi]) < 0)
      and all(np.diff([eS0] + rowS + [eSpi]) < 0), "A3 [D]",
      "E(Phi) falls monotonically from 0 to pi on N and S; N lies lowest, the uniform field (Hofstadter) highest",
      "Phi/pi 0.25,0.5,0.75: N " + ", ".join(f"{x:.4f}" for x in rowN) + "; S " + ", ".join(f"{x:.4f}" for x in rowS)
      + "; U " + ", ".join(f"{x:.4f}" for x in rowU))
curS = [(E8(AS(p), 48) - E8(AS(0.0), 48)) / p ** 2 for p in (0.1, 0.2, 0.4)]
curN = [(E8(AN(p), 40) - E8(AN(0.0), 40)) / p ** 2 for p in (0.1, 0.2, 0.4)]
slN = (curN[0] - curN[2]) / np.log(4)
check(np.ptp(curS) < 0.002 and curN[0] < curN[1] < curN[2] and slN < -0.02, "A4 [D]",
      "top of the landscape: Phi = 0 is a maximum on both paths; on S quadratic, V = V0 - (k/2) Phi^2; on N the nesting "
      "log, E - E0 ~ -alpha Phi^2 ln(1/Phi): the zero-flux nested sea is unstable to flux at any strength",
      f"S (E-E0)/Phi^2 = {', '.join(f'{x:.4f}' for x in curS)} (k = {-2*np.mean(curS):.4f}); "
      f"N = {', '.join(f'{x:.4f}' for x in curN)} (alpha = {-slN:.4f} per ln)")
eZ2 = torus_E(12, lambda r, mu: RNG.choice((-1.0, 1.0)))
eU1 = torus_E(12, lambda r, mu: np.exp(2j * PI * RNG.random()))
check(eSpi < eZ2 < eS0 and eSpi < eU1 < eS0, "A5 [D]",
      "random face flux (12^3 torus, seeded) sits part-way down, not at the top: 'random' and 'zero' pre-role flux are "
      "not the same start", f"Z2 random {eZ2:.5f}, U(1) random {eU1:.5f}; fraction of the Lieb drop already released "
      f"{(eS0-eZ2)/(eS0-eSpi):.2f}, {(eS0-eU1)/(eS0-eSpi):.2f}")

print("== B. stiffness: nested surface, nodal lines, Dirac points")
bx = {f: (gapless(AS(f * PI), 12), gapless(AS(f * PI), 24), gapless(AN(f * PI), 12), gapless(AN(f * PI), 24))
      for f in (0.25, 0.5)}
bpi = gapless(AS(PI), 24)
okb = all(3.3 < b[1] / b[0] < 4.7 and 1.6 < b[3] / b[2] < 2.5 for b in bx.values()) and bpi == 0
check(okb, "B1 [D]", "gapless set (box count n = 12 -> 24; x4 surface, x2 lines): S keeps a surface, N leaves lines, "
      "Dirac points appear only at Phi = pi exactly", "; ".join(f"Phi={f}pi S {b[0]}->{b[1]} N {b[2]}->{b[3]}"
                                                              for f, b in bx.items()) + f"; pi: {bpi}")
# Theorem: on the nested surface any flux coupling at Q = (pi,pi,pi) is m(k) = 2i Phi sum a_mu cos k_mu, odd under k -> k+Q
th = RNG.uniform(-PI, PI, (4000, 2)); kz = np.arccos(np.clip(-np.cos(th[:, 0]) - np.cos(th[:, 1]), -1, 1))
fs = np.c_[th, kz][np.abs(np.cos(th[:, 0]) + np.cos(th[:, 1])) <= 1]
aa = RNG.normal(size=(50, 3)); sg = [(np.min(np.cos(fs) @ a) < 0 < np.max(np.cos(fs) @ a)) for a in aa - aa.mean(1)[:, None]]
check(all(sg), "B2 [T]", "no flux pattern gaps the whole nested surface: m(k + Q) = -m(k) maps the surface to itself, so "
      "m changes sign on it and vanishes on a curve (the density wave's scalar coupling does not)",
      f"sign change on the surface for {sum(sg)}/50 random non-gauge couplings")
c1 = 1 / (32 * PI); g2d = lambda d: ellipk(1 - d ** 2 / 16) / (2 * PI ** 2)
Zas = lambda P: (c1 + (np.log(16 / P) - 1) / (32 * PI ** 2)) / P


def ZQ2(P):   # two-level integral for the (pi,pi,0) crossing (separable: delta from kx,ky with the exact 2D density of
    # states; kz carries the mean -2cos kz and |m| = |sin kz| = 1 + O(P^2) in the window |cos kz| < R/2 at kz = +-pi/2)
    f = lambda d: g2d(abs(d)) * d * d * 2 * np.arcsin(min(1.0, np.sqrt(d * d + P * P) / 2)) / (4 * (d * d + P * P) ** 2.5)
    return 2 * sum(quad(f, a, b, limit=400)[0] for a, b in ((0, P), (P, 30 * P), (30 * P, 1e-1), (1e-1, 4))) / (2 * PI)


q2 = ZQ2(1e-3) * 1e-3; q2a = (np.log(16e3) - 1) / (32 * PI ** 2)
Jint = quad(lambda u: u * u * np.log(u) / (1 + u * u) ** 2, 0, np.inf)[0]
check(abs(q2 / q2a - 1) < 0.01 and abs(Jint - PI / 4) < 1e-8, "B3 [T+D]",
      "S stiffness pole: Z_S = [1/(32 pi) + (ln(16/Phi) - 1)/(32 pi^2)]/Phi + O(1): the (pi,0,0) crossing lines give 1/(32 pi),"
      " the (pi,pi,0) lines ride the square-lattice van Hove log (exact two-level quadrature at Phi = 1e-3)",
      f"Phi Z_Q2 at 1e-3: {q2:.5f} vs {q2a:.5f}; int u^2 ln u/(1+u^2)^2 = {Jint:.6f} (pi/4)")
zs = {f: Zc(AS, f * PI, 40) for f in (0.05, 0.1, 0.2)}
check(all(abs(zs[f] / Zas(f * PI) - 1) < 0.05 for f in (0.05, 0.1)), "B4 [D]",
      "lattice cranking mass on S (40^3 cells) matches the asymptotic pole; a 1/Phi pole gives a FINITE field distance "
      "(int sqrt(Z) dPhi converges), not the plateau's 1/Phi^2",
      "; ".join(f"Phi={f}pi Z {zs[f]:.4f} (asym {Zas(f*PI):.4f})" for f in zs))
zN = [Zc(AN, 0.4 * PI, L) for L in (16, 32, 48)]; zpi = [Zc(AS, PI, L) for L in (16, 32, 48)]
check(zN[2] / zN[0] > 2.5 and zN[0] < zN[1] < zN[2] and zpi[0] < zpi[1] < zpi[2] and zpi[2] - zpi[1] < zpi[1] - zpi[0], "B5 [D]",
      "on N the zero-energy nodal lines make the adiabatic stiffness grow ~ L (Ohmic: the roll is damped into the sea, "
      "not inertial); at pi the Dirac points give only a log", f"N at 0.4pi, L=16,32,48: {', '.join(f'{x:.3f}' for x in zN)}; "
      f"S at pi: {', '.join(f'{x:.4f}' for x in zpi)}")

print("== C. slow roll on S from the computed V and Z (zeta = (J a)^-1/2/(M_P a_r))")
kS = -2 * np.mean(curS); V0 = eS0 - eSpi
pg = np.linspace(0.15, 1.0, 12) * PI
Vg = np.array([E8(AS(p), 24) for p in pg]) - eSpi; Zg = np.array([Zc(AS, p, 20) for p in pg[:-1]])
uu0 = np.log(np.r_[np.logspace(-300, -1.3, 300), pg[:-1]])
lWv = np.r_[np.log(0.5 * kS) + 2 * uu0[:300], np.log(V0 - Vg[:-1])]
lZv = np.r_[np.log(Zas(np.exp(uu0[:300]))), np.log(Zg)]
sW, sZ = CubicSpline(uu0, lWv), CubicSpline(uu0, lZv)


def slowroll(lz, Nstar=55.0):
    """log-form slow roll; lz = ln zeta, chi = zeta int sqrt(Z) dPhi in reduced Planck units"""
    u = np.linspace(uu0[0], uu0[-1], 80000)
    lW, w1, w2, lZ, z1 = sW(u), sW(u, 1), sW(u, 2), sZ(u), sZ(u, 1); V = V0 - np.exp(lW)
    lq = lW - 2 * u - 2 * lz - lZ                      # ln[W / (Phi chi')^2]
    leps = np.log(0.5) + 2 * (lW - u - lz - 0.5 * lZ) + 2 * np.log(w1) - 2 * np.log(V)   # eps = (1/2)(V_chi/V)^2
    eta = -np.exp(lq) * (w1 * (w1 - 1 - 0.5 * z1) + w2) / V                              # V_chi chi / V
    ldN = np.log(V) - lq - np.log(w1)                   # dN/du
    end = leps >= 0
    iend = int(np.argmax(end)) if np.any(end) else len(u) - 1
    dN = np.exp(ldN); seg = 0.5 * (dN[1:] + dN[:-1]) * np.diff(u)
    Nf = np.zeros(len(u)); Nf[:iend] = np.cumsum(seg[:iend][::-1])[::-1]
    j = int(np.argmin(np.abs(Nf - Nstar))); eps = np.exp(leps[j])
    return dict(ns=1 - 6 * eps + 2 * eta[j], r=16 * eps, leps=leps[j], P=np.exp(u[j]), Pe=np.exp(u[iend]), V=V[j],
                end=bool(np.any(end)), eta=eta[j], Nmax=Nf[0])


JA = np.sqrt(3.0); LZ = lambda rg: -0.25 * np.log(JA) - rg * np.log(2)
rows = {rg: slowroll(LZ(rg)) for rg in (0, 2, 4)}
check(all(d['end'] and d['Nmax'] > 55 and abs(d['ns'] - (1 - 3 / 55)) < 0.008 and d['r'] < 1e-4 for d in rows.values()),
      "C1 [D]", "the computed S potential with its own stiffness is a quartic-hilltop (log-corrected) roll: "
      "n_s ~ 1 - 3/N*, tiny r, eps = 1 before pi (exit)",
      "; ".join(f"rung {rg}: n_s {d['ns']:.4f} r {d['r']:.1e} Phi*/pi {d['P']/PI:.1e} Phi_end/pi {d['Pe']/PI:.2f}"
                for rg, d in rows.items()) + f"; 1 - 3/55 = {1-3/55:.4f}")


def lP(rr):
    d = slowroll(LZ(rr))
    return np.log(d['V'] * JA) - 4 * rr * np.log(2) - np.log(24 * PI ** 2) - d['leps'] - np.log(AS_PL)


scan = {x: float(lP(x)) for x in (0, 20, 60, 120, 200)}
sig = (NS_PL - rows[0]['ns']) / NS_SIG
check(sig > 3 and min(scan.values()) > 20, "C2 [T+E]",
      "against measurement: n_s is low by more than 3 sigma, and A_s cannot be met at ANY rung: V ~ 2^-4r while the "
      "canonical field ~ 2^-r sqrt(Phi), so the quartic coupling V0 lambda is rung-free (a scale-free quartic hilltop) "
      "and P ~ lambda N^3 stays ~1e14 times A_s (only the stiffness log drifts); P > 1 also means the roll near the top "
      "is diffusion-dominated", f"n_s(rung 0) {rows[0]['ns']:.4f} ({sig:.1f} sigma low); ln(P/A_s) at rungs "
      + ", ".join(f"{x}: {v:.1f}" for x, v in scan.items()) + f"; P(rung 0) = {np.exp(scan[0])*AS_PL:.1e}")

print("== D. passing: a split that keeps parent loop holonomies")
# the parent link is two child links; the parent face loop bounds a 2x2 block of child faces (exact Stokes)
L = 8; ang = RNG.uniform(-PI, PI, (L, L, L, 3))
def lk(r, mu): return np.exp(1j * ang[tuple(np.array(r) % L)][mu])
def plaq(r, mu, nu, s=1):
    r = np.array(r); a = lk(r, mu) if s == 1 else lk(r, mu) * lk(r + E3[mu], mu)
    o = s * E3[mu]
    b = lk(r + o, nu) if s == 1 else lk(r + o, nu) * lk(r + o + E3[nu], nu)
    c = lk(r + E3[nu] * s, mu) if s == 1 else lk(r + 2 * E3[nu], mu) * lk(r + 2 * E3[nu] + E3[mu], mu)
    d = lk(r, nu) if s == 1 else lk(r, nu) * lk(r + E3[nu], nu)
    return a * b * np.conj(c) * np.conj(d)
errs = []
for _ in range(20):
    r = RNG.integers(0, L, 3); mu, nu = PL[RNG.integers(3)]
    kids = np.prod([plaq(r + i * E3[mu] + j * E3[nu], mu, nu) for i in (0, 1) for j in (0, 1)])
    errs.append(abs(kids - plaq(r, mu, nu, 2)))
fix = [p for p in np.linspace(0, 2 * PI, 2401)[:-1] if abs(np.angle(np.exp(1j * 3 * p))) < 1e-9]
check(max(errs) < 1e-12 and abs(np.exp(4j * PI) - 1) < 1e-12 and np.allclose(fix, [0, 2 * PI / 3, 4 * PI / 3]), "D1 [T]",
      "parent face holonomy = product of its four child faces: children at pi each read 0 at the parent; a parent pi "
      "face forces an odd number of pi children (Z2) or mean pi/4 (U(1)); per-face flux is kept only at 0, 2pi/3, 4pi/3",
      f"Stokes error {max(errs):.0e} (20 random U(1) fields); 4 pi -> 0; fixed points of Phi -> 4 Phi: "
      f"{[round(x/PI,4) for x in fix]} pi")
# born child states compatible with a parent pi face
eUq = EU(1, 8); xU = (eUq - eSpi) / (eS0 - eSpi)
ks_c = lambda r, mu: [1.0, (-1.0) ** r[0], (-1.0) ** (r[0] + r[1])][mu]
def born(r, mu):
    P = [x // 2 for x in r]; first = r[mu] % 2 == 0
    return ks_c(r, mu) * (ks_c(P, mu) if first else 1.0)
eB = torus_E(8, born); eK8 = torus_E(8, ks_c); e08 = torus_E(8, lambda r, mu: 1.0)
xZ = (eB - eK8) / (e08 - eK8)
check(0.5 < xU < 1 and 0 < xZ < 1, "D2 [D]",
      "born children: the self-similar field passes Phi -> Phi/4 (child pi/4); the Z2 lift (child KS x parent KS on half "
      "links) keeps every parent face at pi; both start far up the child landscape (x = share of the Lieb drop not "
      "yet released)", f"U(1) pi/4: E {eUq:.4f}, x = {xU:.3f}; Z2 lift on 8^3: E {eB:.4f} vs child pi {eK8:.4f}, "
      f"zero {e08:.4f}, x = {xZ:.3f}")
gr = 2 ** abs(rows[0]['eta'])
check(gr < 4, "D3 [T+D]", "clock arithmetic: during one split interval (ln 2 e-folds) a slow roll grows Phi by 2^|eta| "
      "while faithful passing divides it by 4, so the order is reset each split (a fixed born share x: power law or de Sitter, no clock); keeping pi per face "
      "needs a passing that inserts a pi flux line through every parent face, which writes the clock into the rule",
      f"2^|eta| at N* = 55, rung 0: {gr:.4f} < 4")

print("== E. exit and reheating;  F. the flux sign")
cpi = [(E8(AS(PI - d), 32) - eSpi) / d ** 2 for d in (0.1, 0.2)]
cpN = [(E8(AN(PI - d), 32) - eSpi) / d ** 2 for d in (0.1, 0.2)]
check(min(cpi + cpN) > 0, "E1 [D]", "pi flux is a stable minimum on both paths (exit lands on the Dirac sea; released "
      "energy V0 per site; oscillations decay into Dirac particle-hole pairs, whose q = 0 density ~ omega^2 is nonzero "
      "at every omega > 0)", f"V''/2 at pi: S {cpi[0]:.4f}, N {cpN[0]:.4f}; V0 = {V0:.5f}")
sym = max(abs(E8(AN(p), 12) - E8(AN(-p), 12)) for p in (0.3, 1.1, 2.5))
check(sym < 1e-12 and np.ptp(e1) < 1e-10, "F1 [T+D]", "E(Phi) = E(-Phi) (complex conjugation); +pi and -pi are one holonomy, "
      "and every pattern ends in the same class, so the T-breaking domains of the roll merge at exit: no selector and no "
      "surviving walls", f"|E(Phi)-E(-Phi)| on N {sym:.0e}; "
      f"E(-pi) - E(pi) = {abs(E8(AS(-PI), 24) - E8(AS(PI), 24)):.0e}")
print(f"time {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
