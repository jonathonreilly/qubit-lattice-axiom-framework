#!/usr/bin/env python3
"""J:derive:ray-limit-of-the-clocked-walk:a4 - checks for ATTEMPT.md (same directory).

Block 54's clocked walk (open PR #8570): H = sum_j sigma_j D_j, D_j = (i/2)(T_j - T_j^dag), (T_j psi)(x) = psi(x - e_j),
H_w = sqrt(w) H sqrt(w), u = log w. EXACT parts: sympy / exact small-matrix identities to machine precision; FLOAT parts:
the walk on boxes (the packet construction and measurement of block 54's control specs/supervisor_control_block54_orientation.py,
re-implemented), clouds of rays with and without the anomalous velocity, quadratures.
"""
import sys
import time

import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


# ------------------------------------------------------------------ A: the curvature of the positive branch (EXACT + FLOAT)
def omega_plus(k):
    k = np.atleast_2d(k)
    s, c = np.sin(k), np.cos(k)
    e = np.sqrt((s * s).sum(axis=1))
    prod = np.stack([s[:, 0] * c[:, 1] * c[:, 2], c[:, 0] * s[:, 1] * c[:, 2], c[:, 0] * c[:, 1] * s[:, 2]], 1)
    return -prod / (2 * e[:, None] ** 3)


k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
dvec = sp.Matrix([sp.sin(k1), sp.sin(k2), sp.sin(k3)])
dn = sp.sqrt(dvec.dot(dvec))
Pm = (sp.eye(2) + sum(((dvec[j] / dn) * sp.Matrix(SIG[j].tolist()) for j in range(3)), sp.zeros(2, 2))) / 2
ks = (k1, k2, k3)
# gauge-invariant curvature F_jl = i Tr(P [d_j P, d_l P]); Omega_i = F_jl for (i, j, l) cyclic; evaluate at rational points
pts = [(sp.Rational(3, 10), sp.Rational(-7, 10), sp.Rational(11, 10)), (sp.Rational(1, 2), sp.Rational(1, 5), sp.Rational(-2, 5)),
       (sp.Rational(29, 10), sp.Rational(3, 10), sp.Rational(-1, 10))]
dP = [sp.diff(Pm, kk) for kk in ks]
a_ok = True
for pnt in pts:
    sub = dict(zip(ks, pnt))
    Pn = np.array(Pm.subs(sub).evalf(30).tolist(), dtype=complex)
    dPn = [np.array(dPk.subs(sub).evalf(30).tolist(), dtype=complex) for dPk in dP]
    Om = []
    for i, j, l in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        Om.append(np.real(1j * np.trace(Pn @ (dPn[j] @ dPn[l] - dPn[l] @ dPn[j]))))
    a_ok &= np.allclose(Om, omega_plus(np.array([float(v) for v in pnt]))[0], atol=1e-12)


def plaquette_flux(k0, i, h=1e-4):
    """Berry phase of the positive eigenvector around a small square in the (j, l) plane, (i, j, l) cyclic."""
    j, l = (i + 1) % 3, (i + 2) % 3
    corners = []
    for dj, dl in ((0, 0), (1, 0), (1, 1), (0, 1)):
        kk = np.array(k0, float); kk[j] += dj * h; kk[l] += dl * h
        _, v = np.linalg.eigh(sum(np.sin(kk[m]) * SIG[m] for m in range(3)))
        corners.append(v[:, 1])
    prod = 1.0 + 0j
    for m in range(4):
        prod *= np.vdot(corners[m], corners[(m + 1) % 4])
    return -np.angle(prod) / h ** 2


kt = np.array([0.4, -0.9, 1.3])
pl = [plaquette_flux(kt, i) for i in range(3)]
ok("A1", a_ok and np.allclose(pl, omega_plus(kt)[0], rtol=1e-3),
   "positive branch of h(k) = sin k . sigma: Omega_i = -sin k_i cos k_j cos k_l / (2 |d|^3), (i, j, l) cyclic, |d|^2 = "
   "sum sin^2 k (i Tr P[dP, dP] at three points to 1e-12; small-plaquette Berry phases agree, fixing the sign); at small "
   "k it is -k/(2|k|^3), and Omega_- = -Omega_+")

weyl = [np.array(K, float) for K in np.array(np.meshgrid(*[[0, np.pi]] * 3, indexing="ij")).reshape(3, -1).T]
fluxes = []
th, wt = np.polynomial.legendre.leggauss(40)
for K in weyl:
    rad = 0.05
    tot = 0.0
    for ct, wc in zip(th, wt):
        for ph in np.linspace(0, 2 * np.pi, 80, endpoint=False):
            st = np.sqrt(1 - ct * ct)
            nrm = np.array([st * np.cos(ph), st * np.sin(ph), ct])
            tot += wc * (2 * np.pi / 80) * rad ** 2 * (omega_plus(K + rad * nrm)[0] @ nrm)
    fluxes.append(tot)
chis = [int(round(np.prod(np.cos(K)))) for K in weyl]
ok("A2", all(abs(f + 2 * np.pi * c) < 2e-2 for f, c in zip(fluxes, chis)) and sum(chis) == 0,
   f"the eight zero-energy points K_j in {{0, pi}}: flux of Omega_+ through a sphere of radius 0.05 around K is "
   f"{', '.join(f'{f:+.3f}' for f in fluxes)} = -2 pi chi_K for chi = {chis} (chi_K = prod cos K_j, Omega_+ ~ -chi_K q/"
   "(2|q|^3)): four of each handedness, total zero")

# ------------------------------------------------------------------ B: exact operator identities behind the theorem
Lb = 4
rng = np.random.default_rng(3)
nb = Lb ** 3


def shift_mat(j, L):
    M = np.zeros((L ** 3, L ** 3))
    for x in np.ndindex(L, L, L):
        y = list(x); y[j] = (y[j] + 1) % L
        M[np.ravel_multi_index(y, (L, L, L)), np.ravel_multi_index(x, (L, L, L))] = 1  # (T psi)(x + e_j) = psi(x)
    return M


Ts = [np.kron(shift_mat(j, Lb), np.eye(2)) for j in range(3)]
Hf = sum(np.kron(0.5j * (shift_mat(j, Lb) - shift_mat(j, Lb).T), SIG[j]) for j in range(3))
u = rng.normal(0, 0.3, nb)
sw = np.kron(np.diag(np.exp(u / 2)), np.eye(2))
Hw = sw @ Hf @ sw
Xs = [np.kron(np.diag([x[j] for x in np.ndindex(Lb, Lb, Lb)]).astype(float), np.eye(2)) for j in range(3)]
b_ok = np.allclose(Hw, Hw.conj().T)
for a in range(3):
    Ta = Ts[a]
    ua = np.array([u[np.ravel_multi_index(tuple((np.array(x) + np.eye(3, dtype=int)[a]) % Lb), (Lb,) * 3)]
                   for x in np.ndindex(Lb, Lb, Lb)])
    swa = np.kron(np.diag(np.exp(ua / 2)), np.eye(2))
    b_ok &= np.allclose(Hw @ Ta - Ta @ Hw, Ta @ (swa @ Hf @ swa - Hw))  # [H_w, T_a] = T_a (H_{w(.+a)} - H_w)
# velocity: on the interior (away from the periodic seam) i[H_w, X_j] = sqrt(w) sigma_j C_j sqrt(w)
Cj = [np.kron(0.5 * (shift_mat(j, Lb) + shift_mat(j, Lb).T), SIG[j]) for j in range(3)]
vel_ok = True
for j in range(3):
    lhs = 1j * (Hw @ Xs[j] - Xs[j] @ Hw)
    rhs = sw @ Cj[j] @ sw
    mask = np.ones_like(lhs, bool)
    for x in np.ndindex(Lb, Lb, Lb):
        if x[j] in (0, Lb - 1):
            i0 = 2 * np.ravel_multi_index(x, (Lb,) * 3)
            mask[i0:i0 + 2, :] = False; mask[:, i0:i0 + 2] = False
    vel_ok &= np.allclose(lhs[mask], rhs[mask])
ok("B1", b_ok and vel_ok,
   "exact identities (4^3 torus, random u, to machine precision): H_w hermitian; [H_w, T_a] = T_a (H_{w(.+a)} - H_w), "
   "H_{w(.+a)} = sqrt(w) e^{delta/2} H e^{delta/2} sqrt(w), delta = u(. + a) - u; velocity i[H_w, X_j] = sqrt(w) sigma_j "
   "C_j sqrt(w), C_j = (T_j + T_j^dag)/2 (off the seam); with E = <H_w>, dE = |(H_w - E)psi| both conserved, these give "
   "Theorem A's bound |d<T_a>/dt - i(e^c - 1) E <T_a>| <= |e^c - 1| dE + (curvature remainder)")


# ------------------------------------------------------------------ C: the walk against clouds of rays (FLOAT)
def build(side, gsig, gdir):
    idx = np.arange(side ** 3).reshape(side, side, side)
    pos = np.stack(np.meshgrid(*[np.arange(side, dtype=float)] * 3, indexing="ij"))
    centre = np.array([side / 2.0] * 3)
    rel = pos - centre[:, None, None, None]
    uu = gsig * (rel[0] * gdir[0] + rel[1] * gdir[1] + rel[2] * gdir[2])
    swf = np.exp(0.5 * uu)
    rows, cols, vals = [], [], []
    for j in range(3):
        lo = [slice(None)] * 3; hi = [slice(None)] * 3
        lo[j] = slice(0, side - 1); hi[j] = slice(1, side)
        xa, xb = idx[tuple(lo)].ravel(), idx[tuple(hi)].ravel()
        amp = (swf[tuple(lo)] * swf[tuple(hi)]).ravel()
        for s1 in range(2):
            for s2 in range(2):
                c = SIG[j][s1, s2]
                if c == 0:
                    continue
                rows += [2 * xb + s1, 2 * xa + s1]; cols += [2 * xa + s2, 2 * xb + s2]
                vals += [0.5j * amp * c, -0.5j * amp * c]
    n = 2 * idx.size
    return coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr(), pos, centre


def packet(side, pos, kvec, start, sig, branch):
    d = pos - start[:, None, None, None]
    env = np.exp(-(d ** 2).sum(axis=0) / (4 * sig ** 2)) * np.exp(1j * (d[0] * kvec[0] + d[1] * kvec[1] + d[2] * kvec[2]))
    s0 = np.sin(kvec)
    _, vecs = np.linalg.eigh(sum(s0[j] * SIG[j] for j in range(3)))
    spinor = vecs[:, 1] if branch == 1 else vecs[:, 0]
    comp = [np.fft.fftn(env * spinor[0]), np.fft.fftn(env * spinor[1])]
    kk = 2 * np.pi * np.fft.fftfreq(side)
    kx, ky, kz = np.meshgrid(kk, kk, kk, indexing="ij")
    sx, sy, sz = np.sin(kx), np.sin(ky), np.sin(kz)
    e = np.sqrt(sx * sx + sy * sy + sz * sz); e[e == 0] = 1.0
    nx, ny, nz = branch * sx / e, branch * sy / e, branch * sz / e
    upc = 0.5 * ((1 + nz) * comp[0] + (nx - 1j * ny) * comp[1]); dnc = 0.5 * ((nx + 1j * ny) * comp[0] + (1 - nz) * comp[1])
    psi = np.zeros(2 * side ** 3, complex)
    psi[0::2] = np.fft.ifftn(upc).ravel(); psi[1::2] = np.fft.ifftn(dnc).ravel()
    return psi / np.linalg.norm(psi)


def mean_pos(psi, pos, side):
    p = (np.abs(psi[0::2]) ** 2 + np.abs(psi[1::2]) ** 2).reshape(side, side, side)
    return np.array([(p * pos[j]).sum() for j in range(3)]) / p.sum()


def neg_weight(psi, side):
    """weight on the negative branch of the free h(k) (w varies by < 10 per cent over the packet)."""
    a = [np.fft.fftn(psi[0::2].reshape(side, side, side)), np.fft.fftn(psi[1::2].reshape(side, side, side))]
    kk = 2 * np.pi * np.fft.fftfreq(side)
    kx, ky, kz = np.meshgrid(kk, kk, kk, indexing="ij")
    sx, sy, sz = np.sin(kx), np.sin(ky), np.sin(kz)
    e = np.sqrt(sx * sx + sy * sy + sz * sz); e[e == 0] = 1.0
    nx, ny, nz = sx / e, sy / e, sz / e
    upc = 0.5 * ((1 - nz) * a[0] - (nx - 1j * ny) * a[1]); dnc = 0.5 * (-(nx + 1j * ny) * a[0] + (1 + nz) * a[1])
    tot = (np.abs(a[0]) ** 2 + np.abs(a[1]) ** 2).sum()
    return float((np.abs(upc) ** 2 + np.abs(dnc) ** 2).sum() / tot)


def cloud(g, gdir, centre, start, sig, kvec, t_end, branch, berry, n=10000, steps=300, seed=54):
    rg = np.random.default_rng(seed)
    dx = sig * rg.standard_normal((n, 3)); dk = rg.standard_normal((n, 3)) / (2 * sig)
    x = start[None, :] + np.concatenate([dx, -dx, dx, -dx]); k = kvec[None, :] + np.concatenate([dk, dk, -dk, -dk])
    x0 = x.mean(axis=0)

    def f(x, k):
        s, c = np.sin(k), np.cos(k)
        e = np.sqrt((s * s).sum(axis=1))
        w = np.exp(g * ((x - centre[None, :]) @ gdir))
        kdot = -(branch * e * w * g)[:, None] * gdir[None, :]
        xdot = branch * (w / e)[:, None] * s * c
        if berry:
            xdot = xdot - np.cross(kdot, branch * omega_plus(k))
        return xdot, kdot

    h = t_end / steps
    for _ in range(steps):
        a1, b1 = f(x, k); a2, b2 = f(x + 0.5 * h * a1, k + 0.5 * h * b1)
        a3, b3 = f(x + 0.5 * h * a2, k + 0.5 * h * b2); a4, b4 = f(x + h * a3, k + h * b3)
        x = x + h * (a1 + 2 * a2 + 2 * a3 + a4) / 6; k = k + h * (b1 + 2 * b2 + 2 * b3 + b4) / 6
    return x.mean(axis=0) - x0


G, TT = 0.004, 30.0
GD = np.array([0.0, 0.0, 1.0])


def case(side, kvec, sig, branch=1, extra=None):
    kvec = np.array(kvec, float)
    s0, c0 = np.sin(kvec), np.cos(kvec); e0 = np.sqrt((s0 * s0).sum())
    v0 = branch * s0 * c0 / e0
    disp, cl = {}, {}
    for sg in (+1, -1):
        ham, pos, centre = build(side, sg * G, GD)
        start = centre - v0 * (0.5 * TT)
        psi = packet(side, pos, kvec, start, sig, branch)
        if extra is not None:
            psi = psi + packet(side, pos, np.array(extra, float), start, sig, branch)
            psi /= np.linalg.norm(psi)
        m0 = mean_pos(psi, pos, side)
        psit = expm_multiply(-1j * ham * TT, psi)
        disp[sg] = mean_pos(psit, pos, side) - m0
        if sg == 1:
            beta = neg_weight(psit, side)
            Hpsi = ham @ psi
            E = np.vdot(psi, Hpsi).real
            dE = np.linalg.norm(Hpsi - E * psi)
            cl["start"] = (centre, m0)
    odd = 0.5 * (disp[1] - disp[-1])
    mdir = v0 / np.linalg.norm(v0)
    sd = np.cross(GD, mdir); sd /= np.linalg.norm(sd)
    out = {"walk_side": odd @ sd, "walk_fall": odd @ GD, "beta": beta, "E": E, "dE": dE, "sd": sd}
    if extra is None:
        centre, m0 = cl["start"]
        for berry in (False, True):
            r = 0.5 * (cloud(G, GD, centre, m0, sig, kvec, TT, branch, berry) - cloud(-G, GD, centre, m0, sig, kvec, TT, branch, berry))
            out["cloud_side" if berry else "plain_side"] = r @ sd
            out["cloud_fall" if berry else "plain_fall"] = r @ GD
    return out


t0 = time.time()
rows = []
good = True
res_k = {}
for side, k0, sig in ((80, 0.25, 7.0), (68, 0.5, 5.0), (64, 1.0, 4.0)):
    r = case(side, (k0, 0, 0), sig)
    rows.append(f"k = {k0}: walk {r['walk_side']:+.4f}, rays + anomalous velocity {r['cloud_side']:+.4f}, plain rays "
                f"{r['plain_side']:+.4f}, -gT/(2k) {-G * TT / (2 * k0):+.4f}, lattice -gT/(2 sin k) {-G * TT / (2 * np.sin(k0)):+.4f}")
    good &= abs(r["walk_side"] - r["cloud_side"]) < 0.05 * abs(r["walk_side"]) and abs(r["plain_side"]) < 0.03 * abs(r["walk_side"])
    good &= abs(r["walk_fall"] - r["cloud_fall"]) < 0.015 * abs(r["walk_fall"])
    res_k[k0] = r
    if k0 == 1.0:
        good &= abs(r["walk_side"] + G * TT / (2 * np.sin(k0))) < abs(r["walk_side"] + G * TT / (2 * k0))
    if k0 == 0.5:
        beta05, dE05, E05 = r["beta"], r["dE"], r["E"]
ok("C1", good, "FLOAT, block 54's packets (g = 0.004, T = 30, motion along x, gradient along z; part odd in g; sideways = "
   "along gradient x motion): " + "; ".join(rows) + f". Branch admixture after T at k = 0.5: {beta05:.1e}; dE/E = "
   f"{dE05 / E05:.2f} ({time.time() - t0:.0f} s)")

t0 = time.time()
rn = case(68, (0.5, 0, 0), 5.0, branch=-1)
rw = case(68, (np.pi + 0.5, 0, 0), 5.0, branch=1)
rp = case(68, (0.5, 0, 0), 5.0, branch=1)
mix = case(68, (0.5, 0, 0), 5.0, branch=1, extra=(np.pi + 0.5, 0, 0))
ok("C2", rn["walk_side"] > 0.1 and abs(rn["walk_side"] + rp["walk_side"]) < 0.003 and rw["walk_side"] > 0.1
   and abs(rw["walk_side"] + rp["walk_side"]) < 0.003 and max(abs(rn["walk_fall"] - rp["walk_fall"]),
                                                               abs(rw["walk_fall"] - rp["walk_fall"])) < 0.003
   and abs(mix["walk_side"]) < 0.01 and abs(rn["walk_side"] - rn["cloud_side"]) < 0.004 and abs(rw["walk_side"] - rw["cloud_side"]) < 0.004,
   f"FLOAT, sideways relative to the motion at |q| = 0.5: positive branch at the chi = +1 point {rp['walk_side']:+.4f}; "
   f"negative branch {rn['walk_side']:+.4f} (rays {rn['cloud_side']:+.4f}); positive branch at K = (pi,0,0), chi = -1, "
   f"moving +x {rw['walk_side']:+.4f} (rays {rw['cloud_side']:+.4f}); the fall is the same, {rp['walk_fall']:+.4f}, "
   f"{rn['walk_fall']:+.4f}, {rw['walk_fall']:+.4f}; an equal superposition of the chi = +1 and chi = -1 packets moving "
   f"the same way: centroid sideways {mix['walk_side']:+.4f} ({time.time() - t0:.0f} s)")

status = "PARTIAL" if not FAILS else "PARTIAL (failed checks: " + ", ".join(FAILS) + ")"
print(f"SUMMARY: {status} the positive branch's exact lattice curvature is Omega_i = -sin k_i prod_(j!=i) cos k_j/(2|d|^3); "
      "rays of E = w eps plus the anomalous velocity -kdot x Omega = E grad u x Omega reproduce the clocked walk's sideways "
      "drift at k = 0.25, 0.5, 1 (where the continuum -gT/(2k) is 12 per cent off); the drift flips with the branch "
      "relative to the motion and with the handedness prod cos K_j, the fall does not; the wave-vector law and the "
      "velocity identity are proved with explicit remainders, the branch-purity step is assumed")
if not FAILS:
    rr = {k0: (res_k[k0]["cloud_side"], res_k[k0]["walk_side"]) for k0 in res_k}
    print("HIT: for block 54's clocked walk the first correction to the rays of E = w(x) eps(k) is the anomalous velocity "
          "E grad u x Omega(k) with the exact lattice curvature Omega_i = -sin k_i cos k_j cos k_l/(2 |d|^3) of the "
          "positive branch; rays carrying it give the sideways drift (rays/walk) "
          + ", ".join(f"{a:+.4f}/{b:+.4f}" for a, b in (rr[1.0], rr[0.5], rr[0.25])) + " at k = 1, 0.5, 0.25, where the "
          f"continuum -gT/(2k) gives {-G * TT / 2:+.4f} at k = 1; relative to the motion the drift is -chi_K g T/(2|q|) "
          "near the zero-energy point K (chi_K = prod cos K_j), changes sign with the branch, and the fall does not; an "
          "equal superposition of opposite-handedness packets moving together has no centroid drift")
