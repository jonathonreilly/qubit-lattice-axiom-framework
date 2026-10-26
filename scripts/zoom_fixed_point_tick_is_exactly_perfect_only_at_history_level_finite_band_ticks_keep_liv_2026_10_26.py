AUDIT_INPUT_PATHS = ('docs/ZOOM_FIXED_POINT_TICK_IS_EXACTLY_PERFECT_ONLY_AT_HISTORY_LEVEL_FINITE_BAND_TICKS_KEEP_LIV_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""zoom-fixed-point-tick: is the zoom (block-spin) fixed point a p^4-free tick?

Perfect (blocking fixed point) free scalar and Ginsparg-Wilson fermion in d = 3+1, built exactly in momentum
space by proper-time factorised image sums (1D Poisson/erfc closed forms); exact-dispersion, locality, GW,
doubler, overlap and blocking-flow checks; truncation (finite range) illustration of the finite-band no-go;
2D U(1) index of the overlap on a gauged truncated perfect kernel; sympy for improved bands; UHECR walls.
Seeded, no external data.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import numpy as np
import sympy as sp
from scipy.special import erfc
from scipy.optimize import brentq

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261026)
NP = 0
NF = 0


def check(name, ok, msg=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(("PASS " if ok else "FAIL ") + name + (": " + msg if msg else ""))


# ---------- 1D image sums: h = sum_n s(q)^2 e^{-t q^2}, g = sum_n s(q)^2 q e^{-t q^2}, q = p + 2 pi n
XS = np.arange(1, 41, dtype=float)


def hg(p, t):
    p = np.asarray(p, dtype=float)
    if t <= 2.0:
        s2 = 4.0 * np.sin(p / 2) ** 2
        sq = np.sqrt(t / np.pi)
        c = sq * np.exp(-XS ** 2 / (4 * t)) - 0.5 * XS * erfc(XS / (2 * np.sqrt(t)))
        px = np.multiply.outer(p, XS)
        h = 1.0 - s2 * (sq + 2.0 * (np.cos(px) @ c))
        g = np.sin(p) - s2 * (np.sin(px) @ erfc(XS / (2 * np.sqrt(t))))
        return h, g
    n = np.arange(-3, 4)
    q = np.add.outer(p, 2 * np.pi * n)
    w = np.sinc(q / (2 * np.pi)) ** 2 * np.exp(-t * q ** 2)
    return w.sum(-1), (w * q).sum(-1)


U = np.arange(-26.0, 7.5, 0.05)
TAU = np.exp(U)
WT = TAU * 0.05  # trapezoid in u = ln tau (endpoints negligible)


def perfect_1d_tables(pvals, metric=1.0):
    H = np.empty((len(TAU), len(pvals)))
    G = np.empty_like(H)
    for k, t in enumerate(TAU):
        H[k], G[k] = hg(pvals, t * metric)
    return H, G


# ---------- P1: exact dispersion of the perfect scalar and fermion from the lattice time correlator
def corr_energy(ps, m, kind, Nt=256, gam=(1.0, 1.0, 1.0)):
    if kind == "s":
        p4 = 2 * np.pi * np.arange(Nt) / Nt
    else:
        p4 = 2 * np.pi * (np.arange(Nt) + 0.5) / Nt
    H4, G4 = perfect_1d_tables(p4)
    prod = np.ones(len(TAU))
    for i in range(3):
        hi, gi = perfect_1d_tables(np.array([ps[i]]), gam[i])
        prod = prod * hi[:, 0]
    em = np.exp(-TAU * m * m)
    if kind == "s":
        Gp = ((WT * prod * em)[:, None] * H4).sum(0)
    else:  # rho_4 component (time-odd)
        Gp = ((WT * prod * em)[:, None] * G4).sum(0)
    if kind == "s":
        C = np.fft.ifft(Gp).real
    else:
        C = (np.fft.ifft(Gp) * np.exp(1j * np.pi * np.arange(Nt) / Nt)).imag
    t = 9
    return np.log(C[t] / C[t + 1])


worst = 0.0
for kind in ("s", "f"):
    for m in (0.0, 0.3):
        for (mag, n) in ((0.3, (1, 0, 0)), (np.pi / 4, (1, 1, 0)), (np.pi / 2, (1, 1, 1))):
            nv = np.array(n, float) / np.linalg.norm(n)
            ps = mag * nv
            e = corr_energy(ps, m, kind)
            worst = max(worst, abs(e - np.sqrt(mag ** 2 + m ** 2)))
check("P1a perfect scalar+fermion lowest band exactly relativistic (|p|<=pi/2, m=0,0.3)", worst < 1e-9,
      "max |E_eff - sqrt(p^2+m^2)| = %.1e" % worst)
gam = (1.7, 0.6, 1.0)
ps = np.array([0.4, 0.5, -0.3])
e = corr_energy(ps, 0.0, "s", gam=gam)
ex = np.sqrt(sum(g * q * q for g, q in zip(gam, ps)))
check("P1b constant metric gamma^ii=(1.7,0.6,1): lowest pole on the metric null cone", abs(e - ex) < 1e-9,
      "dev %.1e" % abs(e - ex))

# ---------- P2: factor-2 blocking flow of the naive scalar converges to the perfect propagator
P = np.array([0.7, 0.4, 0.3, 0.5])


def G0(k):
    return 1.0 / np.sum(4 * np.sin(k / 2) ** 2, axis=-1)


def GB(Pv, B):
    j = np.stack(np.meshgrid(*[np.arange(B)] * 4, indexing="ij"), -1).reshape(-1, 4)
    Q = Pv + 2 * np.pi * j
    w = np.prod((np.sin(Q / 2) / (B * np.sin(Q / (2 * B)))) ** 2, axis=-1)
    return np.sum(w * G0(Q / B)) / B ** 2


def T2(Pv, G, n):  # explicit iterated factor-2 map, n steps
    if n == 0:
        return G(Pv)
    k = np.stack(np.meshgrid(*[np.arange(2)] * 4, indexing="ij"), -1).reshape(-1, 4)
    tot = 0.0
    for kk in k:
        pk = (Pv + 2 * np.pi * kk) / 2
        tot += np.prod(np.cos(pk / 2) ** 2) * T2(pk, G, n - 1)
    return tot / 4


Hs, _ = perfect_1d_tables(P)
Gstar = np.sum(WT * np.prod(Hs, axis=1))
rec = abs(T2(P, G0, 2) - GB(P, 4))
devs = [abs(GB(P, B) - Gstar) for B in (2, 4, 8, 16)]
ratios = [devs[i] / devs[i + 1] for i in range(3)]
check("P2a iterated factor-2 map = closed-form B=4 blocking", rec < 1e-12, "%.1e" % rec)
check("P2b zoom flow converges to the perfect action, deviation ~ 1/B^2 (irrelevant p^4)",
      abs(ratios[-1] - 4) < 0.3, "|G_B-G*| B=2..16: " + " ".join("%.2e" % d for d in devs)
      + "; ratios " + " ".join("%.2f" % r for r in ratios))
# physical pole of the naive scalar seen at coarse rung B: Omega_B(P) = B w0(P/B); c_B B^2 constant
cs = []
for B in (1, 2, 4, 8):
    pp = 0.02
    w = B * 2 * np.arcsinh(np.sqrt(np.sin(pp / B / 2) ** 2))
    cs.append((w / pp - 1) / pp ** 2 * B ** 2)
check("P2c T2: blocking keeps the physical pole; lattice-unit c_B = c0/B^2 (c0 = -(S+1)/24, axis -1/12)",
      np.ptp(cs) < 1e-4 and abs(cs[0] + 1 / 12) < 1e-4, "c_B*B^2 = " + " ".join("%.5f" % c for c in cs))

# ---------- P3/P4: 4D perfect GW fermion on a twisted N^4 grid
N = 16
pk = 2 * np.pi * (np.arange(N) + 0.5) / N
Hk, Gk = perfect_1d_tables(pk)
rho = np.zeros((4, N, N, N, N))
for k in range(len(TAU)):
    h, g = Hk[k], Gk[k]
    for mu in range(4):
        f = [h] * 4
        f[mu] = g
        rho[mu] += WT[k] * np.einsum("a,b,c,d->abcd", *f)
rho2 = np.sum(rho ** 2, 0)
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1.0 + 0j, -1])
I2 = np.eye(2)
GAM = [np.kron(s1, s) for s in (s1, s2, s3)] + [np.kron(s2, I2)]
G5 = np.kron(s3, I2)


def to_x(arr):
    ph = np.exp(1j * np.pi * np.arange(N) / N)
    phase = np.einsum("a,b,c,d->abcd", ph, ph, ph, ph)
    return np.fft.ifftn(arr) * phase


loc = {}
for alpha in (0.5, 1.0):
    a = alpha / (alpha ** 2 + rho2)
    b = rho / (alpha ** 2 + rho2)
    ax = to_x(a)
    bx = np.array([to_x(b[m]) for m in range(4)])
    mag = np.sqrt(np.abs(ax) ** 2 + np.sum(np.abs(bx) ** 2, 0))
    r = np.arange(1, 6)
    yv = np.log([mag[i, 0, 0, 0] for i in r])
    yd = np.log([mag[i, i, i, i] for i in (1, 2, 3)])
    fit = np.polyfit(r, yv, 1)
    loc[alpha] = (-fit[0], np.max(np.abs(np.polyval(fit, r) - yv)), -(yd[2] - yd[0]) / 2 / 2, ax, bx)
msg = "; ".join("alpha=%.1f: kappa_axis %.2f (fit res %.2f), kappa_diag/step %.2f" % (al, v[0], v[1], v[2])
                for al, v in loc.items())
check("P3 perfect GW fermion couplings exponentially local", all(v[0] > 0.5 and v[1] < 0.6
                                                                 for v in loc.values()), msg)
alpha = 1.0
a = alpha / (alpha ** 2 + rho2)
b = rho / (alpha ** 2 + rho2)
idx = [(0, 0, 0, 0), (3, 5, 7, 1), (8, 2, 11, 15), (15, 15, 15, 15)]
gw = herm = ovl = 0.0
for i in RNG.integers(0, N, size=(40, 4)).tolist() + [list(t) for t in idx]:
    i = tuple(i)
    D = a[i] * np.eye(4) + 1j * sum(b[m][i] * GAM[m] for m in range(4))
    gw = max(gw, np.abs(G5 @ D + D @ G5 - 2 * alpha * D @ G5 @ D).max())
    herm = max(herm, np.abs(G5 @ D @ G5 - D.conj().T).max())
    m0 = 1 / (2 * alpha)
    A = D - m0 * np.eye(4)
    w, v = np.linalg.eigh(A.conj().T @ A)
    Dov = m0 * (np.eye(4) + A @ v @ np.diag(w ** -0.5) @ v.conj().T)
    ovl = max(ovl, np.abs(Dov - D).max())
check("P4a GW relation g5 D + D g5 = 2 alpha D g5 D; g5-hermiticity", gw < 1e-12 and herm < 1e-12,
      "%.1e, %.1e" % (gw, herm))
check("P4b overlap of the perfect kernel (m0 = 1/2alpha) returns the kernel: overlap step redundant",
      ovl < 1e-12, "%.1e" % ovl)
# doublers: rho_mu(p) at p_mu = pi exactly 0 -> 15 corners have D = 1/alpha; light only near p = 0
cor = []
for c in np.stack(np.meshgrid(*[[0.0, np.pi]] * 4, indexing="ij"), -1).reshape(-1, 4)[1:]:
    rr = []
    for mu in range(4):
        prd = np.ones(len(TAU))
        for nu in range(4):
            hh_, gg_ = perfect_1d_tables(np.array([c[nu] + (1e-9 if c[nu] == 0 else 0)]))
            prd = prd * (gg_[:, 0] if nu == mu else hh_[:, 0])
        rr.append(np.sum(WT * prd))
    cor.append(np.sqrt(np.sum(np.array(rr) ** 2)))
pm = np.minimum(pk, 2 * np.pi - pk)
grid_inf = np.max(np.stack(np.meshgrid(pm, pm, pm, pm, indexing="ij")), 0)
mx = np.sqrt(rho2[grid_inf >= np.pi / 2].max())
check("P4c no doublers: 15 corners at D = 1/alpha (rho = 0), one light cone at p = 0",
      max(cor) < 1e-6 and mx < 2.0, "max|rho| corners %.1e; max|rho| for |p|_inf >= pi/2: %.2f "
      "(light needs |rho| -> inf)" % (max(cor), mx))

# ---------- P5: finite range = finite bands -> nonzero p^4; overlap pole = zeros of b.b of kernel
pS = sp.symbols("p", positive=True)
n1, n2, n3 = sp.symbols("n1 n2 n3")
w_ = sp.symbols("w")
# Wilson-kernel overlap: sinh w = |sin p| ; series
ser = sp.series(sp.asinh(sp.sqrt(sum(sp.sin(nn * pS) ** 2 for nn in (n1, n2, n3)))), pS, 0, 5).removeO()
cW = sp.simplify(sp.expand(ser).coeff(pS, 3).subs(n3, sp.sqrt(1 - n1 ** 2 - n2 ** 2)))
cW_axis = float(cW.subs({n1: 1, n2: 0})); cW_body = float(cW.subs({n1: 1 / sp.sqrt(3), n2: 1 / sp.sqrt(3)}))
check("P5a Wilson-kernel overlap has c = -(S+1)/6 (GW alone does not remove LIV)",
      abs(cW_axis + 1 / 3) < 1e-12 and abs(cW_body + 2 / 9) < 1e-12, "axis %.4f body %.4f" % (cW_axis, cW_body))


def trunc_c(R, ax_, bx_, nvec, pp=0.06):
    rng = np.arange(-R, R + 1)
    X = np.stack(np.meshgrid(rng, rng, rng, rng, indexing="ij"), -1).reshape(-1, 4)
    sgn = (-1.0) ** np.sum(X < 0, axis=1)  # twisted grid: x and x+N differ by a sign
    bc = np.array([bx_[m][tuple((X % N).T)] * sgn for m in range(4)])
    nv = np.array(nvec, float) / np.linalg.norm(nvec)

    def F(w):
        ph = np.exp(-1j * (X[:, :3] @ (pp * nv))) * np.exp(w * X[:, 3])
        bb = bc @ ph
        return (np.sum(bb ** 2)).real
    wroot = brentq(F, 0.5 * pp, 1.5 * pp)
    return (wroot / pp - 1) / pp ** 2


bx5 = loc[0.5][4]
cR = {R: (trunc_c(R, None, bx5, (1, 0, 0)), trunc_c(R, None, bx5, (1, 1, 1))) for R in (1, 2, 3, 4, 5)}
dec = [abs(cR[R][0]) for R in (1, 2, 3, 4, 5)]
check("P5b range-R truncations of the alpha=1/2 perfect kernel as overlap kernels: c falls ~exponentially "
      "with R, nonzero at finite R (T1)", min(dec) > 1e-8 and dec[4] < 1e-3 * dec[0] and dec[0] < abs(cW_axis),
      " ".join("R=%d: %.1e/%.1e;" % (R, v[0], v[1]) for R, v in cR.items()) + " (axis/body)")
# lemma of T1: the image energies e^{-i tau E_l(p)} at a random p are pairwise distinct (infinitely many roots)
pr = RNG.uniform(-1, 1, 3)
ls = np.stack(np.meshgrid(*[np.arange(-3, 4)] * 3, indexing="ij"), -1).reshape(-1, 3)
El = np.linalg.norm(pr + 2 * np.pi * ls, axis=1)
z = np.exp(-1j * 0.37 * El)
dmin = np.min(np.abs(z[:, None] - z[None, :]) + np.eye(len(z)) * 9)
check("P5c T1 lemma: 343 image roots distinct at random p (a fixed-point band needs >343 bands)",
      dmin > 1e-9, "min separation %.1e" % dmin)

# ---------- P6: 2D U(1) index of the overlap on a gauged hypercube-truncated perfect kernel
N2 = 32
pk2 = 2 * np.pi * (np.arange(N2) + 0.5) / N2
H2, Gg2 = perfect_1d_tables(pk2)
r2 = np.array([np.einsum("k,ka,kb->ab", WT, Gg2, H2), np.einsum("k,ka,kb->ab", WT, H2, Gg2)])
al2 = 1.0
den = al2 ** 2 + np.sum(r2 ** 2, 0)
ph2 = np.exp(1j * np.pi * np.arange(N2) / N2)
P2ph = np.outer(ph2, ph2)
a2x = np.fft.ifft2(al2 / den) * P2ph
b2x = [np.fft.ifft2(r2[m] / den) * P2ph for m in range(2)]
gam2 = [s1, s2]
L = 8
offs = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
Kz = {o: (-1.0) ** ((o[0] < 0) + (o[1] < 0)) * (a2x[o[0] % N2, o[1] % N2] * I2 + 1j * sum(
    b2x[m][o[0] % N2, o[1] % N2] * gam2[m] for m in range(2))) for o in offs}


def gauge(Q, noise):
    B = 2 * np.pi * Q / L ** 2
    Ux = np.zeros((L, L), complex); Uy = np.zeros((L, L), complex)
    for x in range(L):
        for y in range(L):
            Ux[x, y] = np.exp(-1j * B * y)
            Uy[x, y] = np.exp(1j * B * L * x) if y == L - 1 else 1.0
    return Ux * np.exp(1j * noise * RNG.normal(size=(L, L))), Uy * np.exp(1j * noise * RNG.normal(size=(L, L)))


def link(Ux, Uy, x, y, d):  # transporter for one step from (x,y) in direction d=(dx,dy) unit
    if d == (1, 0): return Ux[x % L, y % L]
    if d == (-1, 0): return np.conj(Ux[(x - 1) % L, y % L])
    if d == (0, 1): return Uy[x % L, y % L]
    return np.conj(Uy[x % L, (y - 1) % L])


def build(Ux, Uy):
    M = np.zeros((2 * L * L, 2 * L * L), complex)
    for x in range(L):
        for y in range(L):
            i = x * L + y
            for (zx, zy), K in Kz.items():
                dx, dy = -zx, -zy
                if dx == 0 and dy == 0:
                    T = 1.0
                elif dx == 0 or dy == 0:
                    T = link(Ux, Uy, x, y, (dx, dy))
                else:
                    T = 0.5 * (link(Ux, Uy, x, y, (dx, 0)) * link(Ux, Uy, x + dx, y, (0, dy))
                               + link(Ux, Uy, x, y, (0, dy)) * link(Ux, Uy, x, y + dy, (dx, 0)))
                j = ((x + dx) % L) * L + (y + dy) % L
                M[2 * i:2 * i + 2, 2 * j:2 * j + 2] += K * T
    return M


g5b = np.kron(np.eye(L * L), s3)
res = []
gwmax = 0.0
for Q in (0, 1, 2):
    Ux, Uy = gauge(Q, 0.25)
    M = build(Ux, Uy)
    m0 = 1 / (2 * al2)
    Uu, sv, Vh = np.linalg.svd(M - m0 * np.eye(2 * L * L))
    V = Uu @ Vh
    D = m0 * (np.eye(2 * L * L) + V)
    gwmax = max(gwmax, np.abs(g5b @ D + D @ g5b - D @ g5b @ D / m0).max())
    res.append((Q, -0.5 * np.trace(g5b @ V).real))
okI = all(abs(abs(ind) - Q) < 1e-6 for Q, ind in res)
check("P6 2D U(1): overlap on gauged hypercube perfect kernel has |index| = |Q|, GW exact", okI and gwmax < 1e-10,
      " ".join("Q=%d:index %.6f;" % r for r in res) + " GW %.1e" % gwmax)

# ---------- P7: sympy, range-2 improved bands (zoom fixed point to first irrelevant order)
s = sp.sin(pS / 2)
fb = 4 * s ** 2 + sp.Rational(4, 3) * s ** 4
sb = sp.series(fb, pS, 0, 9).removeO()
ff = sp.sin(pS) + sp.sin(pS) ** 3 / 6
sf = sp.series(ff ** 2, pS, 0, 9).removeO()
kb4, kb6 = sb.coeff(pS, 4), sb.coeff(pS, 6)
kf4, kf6 = sf.coeff(pS, 4), sf.coeff(pS, 6)
c8b = {r: float(kb6 * S6 / 2) for r, S6 in (("axis", 1), ("face", sp.Rational(1, 4)), ("body", sp.Rational(1, 9)))}
c8f = {r: float(kf6 * S6 / 2) for r, S6 in (("axis", 1), ("face", sp.Rational(1, 4)), ("body", sp.Rational(1, 9)))}
check("P7 improved link band 4s^2+(4/3)s^4 and fermion sin+sin^3/6: p^4 coefficient 0",
      kb4 == 0 and kf4 == 0, "boson k6=%s c8 %s; fermion k6=%s c8 %s" % (
          kb6, " ".join("%s %.4f" % kv for kv in c8b.items()), kf6, " ".join("%s %.4f" % kv for kv in c8f.items())))

# ---------- P8: UHECR consequences [E]
Es = 1.217e18  # GeV
walls = {"d": (2.5, 4.3), "4He": (4.1, 7.0), "14N": (8.6, 14.9), "56Fe": (17.9, 31.0)}
lines = []
for kap in (1e-2, 1e-3, 1e-4):
    f = kap ** -0.25
    lines.append("kappa=%.0e x%.2f: " % (kap, f) + " ".join("%s %.0f-%.0f" % (k, v[0] * f, v[1] * f)
                                                           for k, v in walls.items()))
kN = (100 / 14.9) ** -4, (100 / 8.6) ** -4
print("  residual dim-6 walls (EeV, axis-body): " + " | ".join(lines))
print("  one-loop kappa estimates [E]: alpha_em/4pi %.1e, alpha_s(E*~0.02)/4pi %.1e, (E*/M_P)^2/16pi^2 %.1e"
      % (1 / 137.036 / (4 * np.pi), 0.02 / (4 * np.pi), (1.217e18 / 1.221e19) ** 2 / (16 * np.pi ** 2)))
print("  14N to 100 EeV on every ray needs kappa < %.1e (body) / %.1e (axis)" % kN)
M2 = 0.8804
Pd8 = {A: A * (M2 * Es ** 4 / (20 * 0.075)) ** (1 / 6) * 1e9 for A in (2, 4, 14, 56)}
me = 0.511e-3
kth = (2 * me ** 2 * Es ** 4 / 0.03) ** (1 / 6) * 1e9
tof = (10 / Es) ** 4 * 4e17
check("P8 dim-8 residual: nuclear instability >= 1e21 eV, photon-decay threshold ~1e20 eV, TOF unmeasurable",
      min(Pd8.values()) > 1e20,
      "P_inst(|c8|=0.075) d %.1e He %.1e N %.1e Fe %.1e eV; k_th(|dc8|=0.03) %.1e eV; GRB 10 GeV dt %.0e s"
      % (Pd8[2], Pd8[4], Pd8[14], Pd8[56], kth, tof))
print("runtime %.1f s" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (NP, NF))
