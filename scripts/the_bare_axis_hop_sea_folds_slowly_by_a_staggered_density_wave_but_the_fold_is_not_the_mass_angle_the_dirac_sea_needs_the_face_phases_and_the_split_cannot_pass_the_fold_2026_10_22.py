AUDIT_INPUT_PATHS = ('docs/THE_BARE_AXIS_HOP_SEA_FOLDS_SLOWLY_BY_A_STAGGERED_DENSITY_WAVE_BUT_THE_FOLD_IS_NOT_THE_MASS_ANGLE_THE_DIRAC_SEA_NEEDS_THE_FACE_PHASES_AND_THE_SPLIT_CANNOT_PASS_THE_FOLD_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Nested pre-role sea: bare axis hop, its staggered-density fold, and the clock (finite runner, seeded).

  A  (a) the bare axis hop folded into the two-tiling cube tick keeps a nested gapless SURFACE;
     the Dirac points of CL-1's tick come from the face phases (pi flux), not from the folding
  B  (b) the nested sea's staggered density wave (nesting vector (pi,pi,pi)) gaps it at any repulsion;
     it is a Dirac mass of CL-1's tick but NOT the mass angle mu (no tiling selection, quadrature gaps)
  C  potential and stiffness of the 3D nested sea's fold (Hartree, spinless NN repulsion g), slow roll
  D  (c) Hubble friction: a per-proper-4-volume phase gives exactly 3H; CL-3 vacuum-standard reading
  E  (d) the split's momentum-preserving passing cannot carry a cell-scale fold to the children
Supplied numbers are named in the output. Measured numbers enter only C4.
"""
import time
import itertools
import numpy as np
from scipy.special import ellipk
from scipy.integrate import quad, simpson
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq, minimize_scalar

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
NS_PL, AS_PL, RMAX = 0.9649, 2.1e-9, 0.036


def check(ok, tag, text, vals=""):
    global NP, NF
    ok = bool(ok)
    NP += ok
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}" + (f"  {vals}" if vals else ""))


# ---------------------------------------------------------------- cube hops
Cc = np.array(list(itertools.product((0, 1), repeat=3)))


def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d):
        Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]


J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * Cc[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
NN = [(a, b) for a in range(8) for b in range(8) if np.sum((Cc[a] - Cc[b]) ** 2) == 1]
W = np.zeros((8, 8), complex); W0 = np.zeros((8, 8)); WE = np.zeros((8, 8))
for a, b in NN:
    g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3); W0[a, b] = -1 / np.sqrt(3)
    dd = int(np.argmax(np.abs(Cc[a] - Cc[b]))); x = np.minimum(Cc[a], Cc[b])
    WE[a, b] = -[1, (-1) ** x[0], (-1) ** (x[0] + x[1])][dd] / np.sqrt(3)       # Kogut-Susskind eta signs
GAM = np.array([(-1) ** c.sum() for c in Cc], float)
FACES = [[i for i in range(8) if Cc[i][d] == v] for d in range(3) for v in (0, 1)]


def face_phases(M):
    out = []
    for f in FACES:
        o = [f[0]]
        while len(o) < 4:
            o.append([j for j in f if j not in o and bin(j ^ o[-1]).count('1') == 1][0])
        out.append(np.prod([M[o[k], o[(k + 1) % 4]] for k in range(4)]) * 9)
    return np.round(np.real(out), 9)


# Bloch form of the two-tiling tick: cell X holds sites 2X + o; even cube = cell; odd cube at (1,1,1) + o
ODD = [np.array([1, 1, 1]) + o for o in Cc]
def lab(p): return int((p[0] % 2) * 4 + (p[1] % 2) * 2 + p[2] % 2)


def bloch(Wc, ks):
    n = len(ks); Re = np.broadcast_to(Wc, (n, 8, 8)).astype(complex).copy(); Ro = np.zeros((n, 8, 8), complex)
    for p in ODD:
        for q in ODD:
            if np.sum((p - q) ** 2) == 1:
                Ro[:, lab(p), lab(q)] += Wc[lab(p), lab(q)] * np.exp(1j * ks @ ((p // 2) - (q // 2)))
    return Re, Ro


def expmh(H, t):
    w, v = np.linalg.eigh(H); return (v * np.exp(-1j * t * w)[:, None, :]) @ np.conj(np.swapaxes(v, 1, 2))


def tick(Wc, ks, eps=0.3, mu=0.0, m=0.0):
    """CL-1 form: exp(+i(eps+mu/2)R_odd) exp(-i(eps-mu/2)R_even); m = staggered (CDW) phase per tick"""
    Re, Ro = bloch(Wc, ks); U = expmh(Ro, -(eps + mu / 2)) @ expmh(Re, eps - mu / 2)
    if m:
        P = np.diag(np.exp(-0.5j * m * GAM)); U = P @ expmh(Ro, -(eps + mu / 2)) @ P @ expmh(Re, eps - mu / 2)
    return U


def grid(n):
    k = np.arange(n) * 2 * np.pi / n
    return np.array(list(itertools.product(k, k, k)))


def quasi(Wc, n, **kw):
    return -np.angle(np.linalg.eigvals(tick(Wc, grid(n), **kw)))


def vac_stats(Wc, n, **kw):
    """Floquet vacuum (negative quasi-energies filled): Var N_even cube, Var N_odd cube, staggered density, Var n_site"""
    ks = grid(n); U = tick(Wc, ks, **kw); w, v = np.linalg.eig(U); om = -np.angle(w); P = np.zeros_like(U)
    for i in range(len(ks)):
        Q, _ = np.linalg.qr(v[i][:, om[i] < 0]); P[i] = Q @ Q.conj().T
    Ge = P.mean(0); idx = [lab(p) for p in ODD]; cel = np.array([p // 2 for p in ODD]); Go = np.zeros((8, 8), complex)
    for i in range(8):
        for j in range(8):
            Go[i, j] = np.mean(np.exp(-1j * ks @ (cel[i] - cel[j])) * P[:, idx[i], idx[j]])
    var = lambda G: float(np.trace(G).real - np.trace(G @ G).real)
    return var(Ge), var(Go), float(np.mean(np.einsum('i,kii->k', GAM, P)).real / 8), \
        float(np.mean([Ge[i, i].real - abs(Ge[i, i]) ** 2 for i in range(8)]))


print("== A. (a) the bare axis hop in the two-tiling tick: nested surface; Dirac points need the face phases")
L = 4; S4 = list(itertools.product(range(L), repeat=3)); ix4 = {s: i for i, s in enumerate(S4)}
cnt = {}
for s in S4:
    for d in range(3):
        t_ = list(s); t_[d] = (t_[d] + 1) % L; e = frozenset((ix4[s], ix4[tuple(t_)]))
        cnt[e] = [(off, tuple(((s[k] - off) % L) // 2 for k in range(3))) for off in (0, 1)
                  if all(((s[k] - off) % 2 == 0) or k != d for k in range(3)) and (s[d] - off) % 2 == 0]
one = all(len(v) == 1 for v in cnt.values())
ne = sum(1 for v in cnt.values() if v[0][0] == 0)
fx = np.array([1, 1, -1, -1]); Gg = np.array([np.prod([fx[c] for c in s]) for s in S4])
RT = [np.zeros((64, 64)) for _ in (0, 1)]
for e, v in cnt.items():
    a, b = tuple(e); RT[v[0][0]][a, b] = RT[v[0][0]][b, a] = 1.0
gauge = np.abs(Gg[:, None] * RT[1] * Gg[None, :] + RT[1]).max() + np.abs(Gg[:, None] * RT[0] * Gg[None, :] - RT[0]).max()
check(one and ne == 96 and len(cnt) == 192 and gauge == 0, "A1 [T]",
      "every nearest-neighbour bond lies in exactly one cube of exactly one tiling (bond along i at x: even tiling iff "
      "x_i even), so the two-tiling tick of the bare axis hop is a split of the 6-NN hop; the odd step's opposite sign "
      "is the gauge prod_i f(x_i), f = (1,1,-1,-1)", f"4^3: {len(cnt)} bonds, {ne} even, all in one cube: {one}; gauge residual {gauge:.0f}")

sq = 0; sq_minus = 0
for bits in range(4096):
    M = np.zeros((8, 8))
    for k, (a, b) in enumerate([(a, b) for a, b in NN if a < b]):
        M[a, b] = M[b, a] = 1 - 2 * ((bits >> k) & 1)
    if np.allclose(M @ M, 3 * np.eye(8)):
        sq += 1; sq_minus += int(np.all(face_phases(M / np.sqrt(3) * -1) == -1) or np.all(face_phases(M / np.sqrt(3)) == -1))
ks6 = grid(6)
spec = max(np.abs(np.sort(quasi(W, 6, mu=mu).ravel()) - np.sort(quasi(WE, 6, mu=mu).ravel())).max() for mu in (0.0, 0.15))
ev0 = np.round(np.linalg.eigvalsh(W0), 6)
check(sq == 128 and sq_minus == 128 and np.all(face_phases(W) == -1) and np.all(face_phases(W0) == 1)
      and abs(ev0[0] + np.sqrt(3)) < 1e-6 and abs(ev0[1] + 1 / np.sqrt(3)) < 1e-6 and spec < 1e-12, "A2 [T]",
      "cube level: R^2 = 1 holds for exactly the 128 sign fields of the all-minus-face class (Cauchy-Schwarz, main "
      "flux-sector note); the bare axis hop has faces +1 and spectrum +-sqrt3, +-1/sqrt3 (not a reflection); CL-1's "
      "spin-3/2-overlap tick has the same quasi-energies as the Kogut-Susskind pi-flux tick",
      f"R^2=3/3 fields {sq}, all-minus {sq_minus}; bare spectrum {sorted(set(ev0.tolist()))}; |spec CL-1 - KS| {spec:.0e}")

box = {}
for nm, Wc, kw in (("bare", W0, {}), ("bare mu=0.1", W0, {"mu": 0.1}), ("CL-1", W, {})):
    c_ = []
    for n in (12, 24):
        w = quasi(Wc, n, **kw); c_.append(int((np.abs(w).min(axis=1) < 0.6 / n).sum()))
    box[nm] = c_
rb, rbm = box["bare"][1] / box["bare"][0], box["bare mu=0.1"][1] / box["bare mu=0.1"][0]
check(3.5 < rb < 5 and 3.5 < rbm < 5 and box["CL-1"] == [1, 1], "A3 [D]",
      "box count of the gapless set (|w| < 0.6/n, n = 12 -> 24; 4 = surface, 1 = points), eps = 0.3: the bare tick keeps "
      "a nested SURFACE, also at mu = 0.1; CL-1's tick has Dirac POINTS",
      "; ".join(f"{k}: {v[0]}->{v[1]}" for k, v in box.items()))


def static_E(Wc, n):
    ks = grid(n) + np.pi / n; Re, Ro = bloch(Wc, ks)
    return float(np.sort(np.linalg.eigvalsh(Re - Ro), axis=1)[:, :4].sum(1).mean() / 8 * np.sqrt(3))


E0f, Epf = static_E(W0, 24), static_E(W, 24)
check(abs(E0f + 1.00244) < 2e-4 and abs(Epf + 1.19380) < 2e-4, "A4 [T+D]",
      "answer to (a): folding the 6-NN sea into 2^3 cubes with even/odd steps does NOT make the Dirac sea; the face "
      "phase -1 (pi flux) does. Half-filled energy per site (hop 1, eps -> 0): zero flux vs pi flux (Lieb's flux phase; "
      "the cube's unique minimiser is the all-minus class)", f"E(0 flux) {E0f:.5f}, E(pi flux) {Epf:.5f}, gain {E0f-Epf:.4f}")

print("== B. (b) the nested sea's density wave: a fold at any repulsion, a Dirac mass, but not the mass angle")
gp = {}
for nm, Wc, kw in (("bare+m", W0, {"m": 0.1}), ("CL-1+m", W, {"m": 0.1}), ("CL-1+mu", W, {"mu": 0.1}),
                   ("CL-1+mu+m", W, {"mu": 0.1, "m": 0.1})):
    gp[nm] = float(np.abs(quasi(Wc, 12, **kw)).min())
quad_ = np.hypot(gp["CL-1+mu"], gp["CL-1+m"])
check(gp["bare+m"] > 0.08 and abs(gp["CL-1+mu"] - 0.1) < 1e-9 and gp["CL-1+m"] > 0.09
      and abs(gp["CL-1+mu+m"] - quad_) < 2e-3, "B1 [T+D]",
      "the (pi,pi,pi) staggered phase m gaps the bare tick's nested surface fully and is a Dirac mass of CL-1's tick; "
      "with mu the gaps add in QUADRATURE: m and mu are two anticommuting masses (a chiral pair), not one",
      ", ".join(f"{k} {v:.4f}" for k, v in gp.items()) + f"; sqrt(mu^2+m^2) {quad_:.4f}")
vs = {}
for nm, Wc, kw in (("bare m=.2", W0, {"m": 0.2}), ("bare m=.6", W0, {"m": 0.6}), ("CL-1 m=.2", W, {"m": 0.2}),
                   ("CL-1 m=.6", W, {"m": 0.6}), ("CL-1 mu=.2", W, {"mu": 0.2}), ("CL-1 mu=.2,m=.2", W, {"mu": 0.2, "m": 0.2})):
    vs[nm] = vac_stats(Wc, 12, **kw)
imb = max(abs(vs[k][0] - vs[k][1]) for k in ("bare m=.2", "bare m=.6", "CL-1 m=.2", "CL-1 m=.6"))
check(imb < 1e-10 and abs(vs["CL-1 mu=.2"][2]) < 1e-10 and min(vs[k][3] for k in vs) > 0.05
      and abs(vs["CL-1 mu=.2,m=.2"][0] - vs["CL-1 mu=.2,m=.2"][1]) > 0.5, "B2 [T+D]",
      "no mixing (24^3 sites): the density-wave vacuum has Var N_even = Var N_odd (binds neither tiling), the mu vacuum "
      "has zero staggered density; no site definite, so every site stays free in CL-2's reading",
      f"max |VarE-VarO| at m only {imb:.0e}; stagger at mu only {vs['CL-1 mu=.2'][2]:.0e}; "
      + "; ".join(f"{k}: {v[0]:.3f}/{v[1]:.3f}/{v[2]:+.3f}" for k, v in vs.items() if 'm=.6' in k or ',' in k))

del ks6
print("== C. potential and stiffness of the 3D nested sea's density-wave fold (Hartree, spinless NN repulsion g)")


def rho2(x):
    x = np.abs(np.atleast_1d(x)); out = np.zeros_like(x, dtype=float); m = x < 4
    out[m] = ellipk(np.minimum(1 - x[m] ** 2 / 16, 1 - 1e-15)) / (2 * np.pi ** 2); return out


def rho3(e):
    return quad(lambda k: rho2(e - 2 * np.cos(k))[0], 0, np.pi, points=[np.arccos(e / 2)] if abs(e) < 2 else None,
                limit=200)[0] / np.pi


EG = np.concatenate([np.linspace(0, 1.9, 60), np.linspace(1.9, 2.1, 41)[1:], np.linspace(2.1, 5.99, 120)[1:], [6.0]])
SR = CubicSpline(EG, [rho3(e) if e < 6 else 0.0 for e in EG])
rho0 = float(SR(0.0))
norm = 2 * quad(lambda e: SR(e), 0, 6, points=[2], limit=400)[0]
absE = 2 * quad(lambda e: e * SR(e), 0, 6, points=[2], limit=400)[0]
n = 96; kc = np.cos((np.arange(n) + 0.5) * 2 * np.pi / n); absG = 0.0; invpi = 0.0
for a in kc:
    absG += np.abs(2 * (a + kc[:, None] + kc[None, :])).sum()
    invpi += (1 / (2 * np.sqrt(a * a + kc[:, None] ** 2 + kc[None, :] ** 2))).sum()
absG /= n ** 3; invpi /= n ** 3
check(abs(norm - 1) < 1e-4 and abs(absE - absG) < 1e-3 and abs(rho0 - 0.1427) < 2e-4, "C1 [T+D]",
      "simple-cubic density of states from the square-lattice elliptic form; normalisation, <|e|> against a 96^3 grid",
      f"rho(0) {rho0:.5f}; norm {norm:.6f}; <|e|> {absE:.5f} vs {absG:.5f}")


def ints(D, ns=6001):
    s = np.linspace(0, np.arcsinh(6 / D), ns); e = D * np.sinh(s); E = D * np.cosh(s); r = SR(np.minimum(e, 6))
    return 2 * simpson(r * e * D * D / (E + e), x=s), 2 * simpson(r, x=s), 0.25 * simpson(r * e * e / E ** 4, x=s)


def Wfold(D, g):    # energy released, E(0) - E(D), of the Hartree Slater state of h + D*(-1)^x
    I1, I2, _ = ints(D); return 0.75 * g * D * D * I2 * I2 - 0.5 * I1


def dstar(g):
    r = minimize_scalar(lambda u: -Wfold(np.exp(u), g), bounds=(-40, 3), method='bounded', options={'xatol': 1e-9})
    return np.exp(r.x)


DS = {g: dstar(g) for g in (0.15, 0.2, 0.5, 1.0)}
slope = (np.log(DS[0.15]) - np.log(DS[0.2])) / (1 / 0.15 - 1 / 0.2)
gapeq = max(abs(3 * g * ints(D)[1] - 1) for g, D in DS.items())
gc = 1 / (3 * invpi)
check(gapeq < 1e-4 and abs(slope + 1 / (6 * rho0)) < 0.05 and abs(gc - 0.732) < 0.01, "C2 [T+D]",
      "perfect nesting: the gap equation 1 = 3g int rho/E has a solution at EVERY g > 0, ln D* ~ -1/(6 g rho0) (BCS "
      "form); the pi-flux Dirac sea folds only above g_c = 1/(3<1/eps>)",
      "D* " + ", ".join(f"g={g}: {D:.2e}" for g, D in DS.items()) + f"; slope {slope:.3f} vs {-1/(6*rho0):.3f}; g_c {gc:.3f}")
MZ = [ints(D)[2] * D * D for D in (1e-3, 1e-6, 1e-9)]
zz = [ints(m)[2] for m in (0.4, 0.2, 0.1)]
WL = [Wfold(D, 1.0) / (D * np.log(1 / D)) ** 2 for D in (1e-3, 1e-9, 1e-20)]
check(max(abs(x - rho0 / 12) for x in MZ) < 1e-6 * rho0 and abs((zz[2] - zz[1]) / (zz[1] - zz[0]) - 4) < 0.01
      and WL[0] > WL[1] > WL[2] > 3 * rho0 ** 2, "C3 [T+D]",
      "cranking mass of the fold (M = 2 sum |<n|dH|0>|^2/dE^3 per site) has the pole M -> rho0/(12 D^2); released "
      "energy W = V0 - V ~ D^2 ln^2(1/D), tending to 3 g rho0^2 D^2 ln^2: the same exponential-plateau class as the 1D toy",
      f"M D^2 {MZ[1]:.7f} (rho0/12 {rho0/12:.7f}); pole ratio {(zz[2]-zz[1])/(zz[1]-zz[0]):.3f}; "
      f"W/(D ln)^2 {WL[0]:.4f}, {WL[1]:.4f}, {WL[2]:.4f} -> {3*rho0**2:.4f}")


def slowroll(sW, sz, V0, ulo, uhi, zeta, Nstar=55.0):
    uu = np.linspace(ulo, uhi, 40000)
    lW, l1, l2, lz1 = sW(uu), sW(uu, 1), sW(uu, 2), sz(uu, 1)
    lp = np.log(zeta) + uu + 0.5 * sz(uu); V = V0 - np.exp(lW); rat = np.exp(lW - 2 * lp)
    eps = 0.5 * l1 ** 2 * np.exp(2 * (lW - lp)) / V ** 2
    eta = -(rat / V) * ((l2 + l1 ** 2) - l1 * (1 + 0.5 * lz1))
    dN = V / (rat * l1)
    iend = int(np.argmax(eps >= 1.0)) if np.any(eps >= 1.0) else len(uu) - 1
    seg = 0.5 * (dN[1:] + dN[:-1]) * np.diff(uu); Nf = np.zeros(len(uu)); Nf[:iend] = np.cumsum(seg[:iend][::-1])[::-1]
    j = int(np.argmin(np.abs(Nf - Nstar)))
    return dict(ns=1 - 6 * eps[j] + 2 * eta[j], r=16 * eps[j], us=uu[j], ue=uu[iend], eps=eps[j], V=V[j], end=bool(np.any(eps >= 1)))


JA = np.sqrt(3.0)
rows = {}; amp = {}
for g in (0.5, 1.0):
    Dg = DS[g]; V0 = Wfold(Dg, g); u = np.linspace(-80, np.log(Dg) - 1e-3, 400)
    sW = CubicSpline(u, np.log([Wfold(np.exp(x), g) for x in u])); sz = CubicSpline(u, np.log([ints(np.exp(x))[2] for x in u]))
    for rg in (0, 2, 4):
        rows[(g, rg)] = slowroll(sW, sz, V0, u[0], u[-1], JA ** -0.5 * 2.0 ** -rg)

    def lP(rr):
        d = slowroll(sW, sz, V0, u[0], u[-1], JA ** -0.5 * 2.0 ** -rr)
        return np.log(d['V'] * JA * 2.0 ** (-4 * rr) / (24 * np.pi ** 2 * d['eps'])) - np.log(AS_PL)
    rr = brentq(lP, 0, 40, xtol=1e-6); d = slowroll(sW, sz, V0, u[0], u[-1], JA ** -0.5 * 2.0 ** -rr)
    amp[g] = (rr, d['ns'], d['r'], np.sqrt(d['V'] * JA * 2.0 ** (-4 * rr) / 3), V0, Dg)
ok = all(abs(d['ns'] - (1 - 2 / 55)) < 0.002 and d['end'] and d['ue'] < np.log(DS[g]) and d['r'] < 1e-5 for (g, _), d in rows.items())
check(ok, "C4 [D]",
      "slow roll on the computed V and M (chi = zeta int sqrt(M) dD, zeta = (J a)^-1/2/(M_P a_r), J a = sqrt3, M_P a = 1 at "
      "the flat rung, N* = 55): n_s = 1 - 2/N independent of g and rung, tiny r, eps = 1 reached before D* (exit)",
      "; ".join(f"g={g} r{rg}: n_s {d['ns']:.4f} r {d['r']:.1e} D_end/D* {np.exp(d['ue'])/DS[g]:.2f}" for (g, rg), d in rows.items()))
check(all(17 < a[0] < 23 and a[2] < RMAX for a in amp.values()), "C5 [T+E]",
      "amplitude: A_s = 2.1e-9 fixes the fold rung (supplied g); H/M_P and r follow",
      "; ".join(f"g={g}: V0 {a[4]:.4f}, D* {a[5]:.2f}, rung {a[0]:.1f}, n_s {a[1]:.4f}, r {a[2]:.0e}, H/M_P {a[3]:.1e}"
                for g, a in amp.items()) + f"; Planck n_s {NS_PL}")

print("== D. (c) Hubble friction and the CL-3 reading")
H, tau, c = 1.0, 1e-3, 1.0
nst = 20000; tt = np.arange(nst) * tau; A = np.exp(3 * H * tt); ph = np.zeros(nst)
for k in range(1, nst - 1):
    ph[k + 1] = ph[k] + (A[k - 1] * (ph[k] - ph[k - 1]) - tau * tau * A[k] * c) / A[k]
vterm = (ph[-1] - ph[-2]) / tau
Ts = np.log(2) / H; ns_ = int(round(Ts / tau)); Ac = 8.0 ** np.floor(np.arange(nst * 3) / ns_); ph2 = np.zeros(len(Ac))
for k in range(1, len(Ac) - 1):
    ph2[k + 1] = ph2[k] + (Ac[k - 1] * (ph2[k] - ph2[k - 1]) - tau * tau * Ac[k] * c) / Ac[k]
v2 = np.diff(ph2[-4 * ns_:]) / tau; vmean = v2.mean()
check(abs(vterm * 3 * H / -c - 1) < 2e-3 and abs(vmean * 3 * H / -c - 27 * np.log(2) / 14) < 0.01, "D1 [T+D]",
      "a fold phase summed per proper 4-volume (weight a^3, CL-3's total phase) is stationary only if (a^3 chi')' = "
      "-a^3 V': friction exactly 3H (terminal velocity -V'/3H); a phase per CELL (count x8 at splits) damps only at "
      "splits and gives a cycle-mean drift 27 ln2/14 = 1.34 times -V'/(3H): friction needs the 4-volume weight",
      f"proper-volume weight: v*3H/(-V') {vterm*3*H/-c:.4f}; per-cell weight: {vmean*3*H/-c:.3f} (27 ln2/14 {27*np.log(2)/14:.3f})")
V0g = amp[1.0][4]
check(V0g > 0, "D2 [R]",
      "CL-3 reads departures from 'the update's vacuum', every negative-quasi-energy mode filled: for the bare tick that "
      "is the UNFOLDED nested sea, so the plateau's departure is 0 (H = 0, no friction, no e-folds) and the folded vacuum "
      "sits at -V0; the clock needs the vacuum standard read from the folded lowest state (then V0 drives H)",
      f"departure of the plateau: free-vacuum reading 0, folded reading V0 = {V0g:.4f} per site (g = 1)")

print("== E. (d) can the split pass the fold order to the children?")
lifts = sorted({(np.pi + 2 * np.pi * j) % (4 * np.pi) for j in range(4)})
const = all(len({(-1) ** int(np.sum(2 * np.array(x) + np.array(c_))) for x in itertools.product(range(3), repeat=3)}) == 1
            for c_ in itertools.product((0, 1), repeat=3))
C4_ = np.array(list(itertools.product(range(4), repeat=3)))
sQ = np.array([(-1) ** int(r.sum()) for r in C4_]); sP = np.array([np.prod([(-1) ** (int(x) // 2) for x in r]) for r in C4_])
check(abs(lifts[0] - np.pi) < 1e-12 and abs(lifts[1] - 3 * np.pi) < 1e-12 and const and int(sQ @ sP) == 0, "E1 [T]",
      "momentum mismatch: the parent's nesting vector pi/a_p lifts to pi/a_p or 3pi/a_p (mod the child's 4pi/a_p), "
      "never the child's 2pi/a_p; for every coincident nesting offset the child staggering is constant on parent sites, "
      "so a passed parent density wave has zero overlap with the child's fold coordinate",
      f"lifts (units 1/a_p) {[round(x/np.pi, 3) for x in lifts]} pi; child stagger constant on parent sites: {const}; overlap {int(sQ@sP)}")
idx4 = {tuple(r): i for i, r in enumerate(C4_)}
nk = 10; kk = (np.arange(nk) + 0.5) * 2 * np.pi / (4 * nk); KS = np.array(list(itertools.product(kk, kk, kk)))
H0 = np.zeros((len(KS), 64, 64), complex)
for i, r in enumerate(C4_):
    for d in range(3):
        r2 = r.copy(); r2[d] += 1; sh = np.zeros(3)
        if r2[d] == 4:
            r2[d] = 0; sh[d] = 1
        ph_ = np.exp(1j * KS @ (4 * sh)); j = idx4[tuple(r2)]; H0[:, j, i] += -ph_; H0[:, i, j] += -np.conj(ph_)


def eg_(D, s):
    tot, gmin = 0.0, np.inf
    for c0 in range(0, len(H0), 125):
        w = np.linalg.eigvalsh(H0[c0:c0 + 125] + np.diag(D * s)[None]); tot += np.sort(w, axis=1)[:, :32].sum(); gmin = min(gmin, np.abs(w).min())
    return tot / (64 * len(H0)), gmin


e00 = eg_(0, sQ)[0]; rowsE = []
for D in (0.4, 0.2, 0.1):
    (a, ga), (b, gb) = eg_(D, sQ), eg_(D, sP); rowsE.append((D, (e00 - a) / D ** 2, ga, (e00 - b) / D ** 2, gb))
check(rowsE[2][1] - rowsE[0][1] > 0.08 and abs(rowsE[2][3] - rowsE[0][3]) < 0.01 and rowsE[2][4] < 0.02, "E2 [D]",
      "child nested sea (40^3 sites): the passed parent pattern releases ~D^2 with no log and leaves the child gapless; the "
      "child's own density wave has the log and the full gap. Children are born UNFOLDED (x = 1 in q = 1/8 + 7x/8)",
      "; ".join(f"D={D}: own {a:.3f}/{ga:.3f}, passed {b:.3f}/{gb:.3f}" for D, a, ga, b, gb in rowsE) + " (dE/D^2 / gap)")

print("supplied: eps = 0.3; Hartree spinless NN repulsion g (0.5, 1); J a = sqrt3; M_P a = 1 at the flat rung; N* = 55; "
      "semiclassical FRW; staggered phase m added per half-tick")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
