#!/usr/bin/env python3
"""The sideways drift of the clocked walk's packets, as a grid.  Worked computation, run 2 of 2.

As landed on main, block 54 (#8570): its exact packet force is withdrawn (T3 a finite-power identity, T4 a conditional ray model); the
sideways drift was executed there, never claimed.  Here: H_w = sqrt(w) H sqrt(w), H = sum_j sigma_j D_j, w = exp(u), u = +-g (r.ghat).
Exact part (sympy): the Berry curvature of the branches of h(k) = sin(k).sigma; at k = (q,0,0), |Omega_x| = 1/(2 sin^2 q), so the
anomalous velocity -kdot x Omega with kdot = -E grad u gives a sideways speed g/(2 sin q): drift g T/(2 sin q) (-> g T/(2 q) as q -> 0).
Reduction (exact): for a gradient along a primitive integer vector m, u depends on n = m.r only, and states exp(i k.r) f(m.r) are closed
under H_w; a packet that is a plane wave across ghat and Gaussian along it evolves on the 1D chain n, and its displacement along a direction d
perpendicular to m is int <dH_w/dk_d> dt.  Floating point for all evolutions.  Prediction compared: the central ray of E = w eps with the
anomalous velocity -kdot x Omega (a semiclassical model, ASSUMED, averaged over the packet's momentum spread).  One 3D packet (block 54's
propagation, box 68) ties the reduction to block 54's executed numbers.
"""
import sys, time
import numpy as np
import sympy as sp
from scipy.sparse import diags, kron, csr_matrix, coo_matrix
from scipy.sparse.linalg import expm_multiply

def out(s): print(s, flush=True)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]

# ------------------------------------------------------------------ exact: Berry curvature of h = sin(k).sigma
kx, ky, kz, q = sp.symbols('k_x k_y k_z q', real=True)
d = sp.Matrix([sp.sin(kx), sp.sin(ky), sp.sin(kz)])
eps = sp.sqrt(d.dot(d))
dh = d / eps
trip = dh.dot(sp.diff(dh, ky).cross(sp.diff(dh, kz)))
closed = sp.sin(kx) * sp.cos(ky) * sp.cos(kz) / eps ** 3
pts = [(sp.Rational(1, 3), sp.Rational(2, 7), -sp.Rational(5, 11)), (sp.Rational(9, 10), -sp.Rational(1, 4), sp.Rational(3, 5)), (2, 1, -3)]
ok = all(abs(sp.N((trip - closed).subs({kx: a, ky: b, kz: c}), 40)) < sp.Float(10) ** -30 for a, b, c in pts)
ok_simpl = sp.simplify(sp.expand_trig(trip - closed)) == 0
out("X exact: dhat.(d_ky dhat x d_kz dhat) = sin k_x cos k_y cos k_z / eps^3 (eps = |sin k|), and cyclically: %s (40-digit check at three points: %s)"
    % ("PASS (sympy simplify)" if ok_simpl else "simplify inconclusive", "PASS" if ok else "FAIL"))
out("X exact: at k = (q,0,0) this is 1/(sin q |sin q|): the branch curvature |Omega_x| = 1/(2 sin^2 q); with a force of size g eps = g |sin q| "
    "the anomalous speed is g/(2 |sin q|): drift g T/(2 sin q) = g T/(2q) (1 + q^2/6 + ...)")
# the eight zero-energy points: k = pi n + delta gives h = D (sin delta), D = diag((-1)^n_j), and the triple product picks up det D
chis = []
for nvec in [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]:
    sub = {kx: sp.pi * nvec[0] + sp.Rational(1, 3), ky: sp.pi * nvec[1] + sp.Rational(2, 7), kz: sp.pi * nvec[2] - sp.Rational(5, 11)}
    r = sp.nsimplify(sp.N(closed.subs(sub) / closed.subs({kx: sp.Rational(1, 3), ky: sp.Rational(2, 7), kz: -sp.Rational(5, 11)}), 30))
    chis.append(int(r))
out("X exact: the curvature at pi n + delta is det D = (-1)^(n_x+n_y+n_z) times the curvature at delta: signs %s over the eight points "
    "(sum %d); the staggering (-1)^(n.r) maps the walk at pi n + delta to the walk at delta with sigma_j -> (-1)^n_j sigma_j, a qubit rotation "
    "when det D = +1 and minus a qubit rotation when det D = -1" % (chis, sum(chis)))

# ------------------------------------------------------------------ reduced chain (exact reduction; floating-point evolution)
def chain_run(k, m, branch, g, T, sigma, dvec, steps=160):
    """Gradient along the primitive integer vector m: u = g (m.r - nc)/|m|.  States psi(r) = exp(i k.r) f(m.r) are closed under H_w; f lives
    on the chain n = m.r.  Packet: f Gaussian (|f|^2 ~ exp(-s^2/(2 sigma^2)), s = n/|m| the distance along ghat), projected on the branch
    momentum by momentum (full momentum k + p m).  Returns the displacement along dvec (a vector perpendicular to m) as int <V_d> dt
    (Simpson), the fall along ghat, and the weight within two sites of the chain ends."""
    m = np.array(m); mm = np.linalg.norm(m)
    s_ = np.sin(k); c_ = np.cos(k); eps_ = np.linalg.norm(s_)
    vm = branch * (s_ * c_ / eps_) @ m                         # d<n>/dt
    sig_n = sigma * mm
    Nn = int(8 * sig_n + abs(vm) * T + 80)
    n = np.arange(Nn); nc = Nn / 2; n0 = nc - vm * T / 2
    phi = np.exp(0.5 * g * (n - nc) / mm)
    H = csr_matrix((2 * Nn, 2 * Nn), dtype=complex); V = csr_matrix((2 * Nn, 2 * Nn), dtype=complex)
    for j in range(3):
        a = int(m[j])
        if a == 0:
            H = H + kron(diags(phi ** 2 * np.sin(k[j])), csr_matrix(SIG[j]))
            V = V + dvec[j] * kron(diags(phi ** 2 * np.cos(k[j])), csr_matrix(SIG[j]))
            continue
        rows = n[(n + a >= 0) & (n + a < Nn)]; cols = rows + a
        A = coo_matrix((phi[rows] * phi[cols] * np.exp(1j * k[j]) / 2j, (rows, cols)), shape=(Nn, Nn)).tocsr()
        H = H + kron(A + A.conj().T, csr_matrix(SIG[j]))
        V = V + dvec[j] * kron(1j * (A - A.conj().T), csr_matrix(SIG[j]))
    H = H.tocsr(); V = V.tocsr()
    env = np.exp(-(n - n0) ** 2 / (4 * sig_n ** 2))
    F = np.fft.fft(env); pp = 2 * np.pi * np.fft.fftfreq(Nn)
    _, v_ = np.linalg.eigh(sum((s_[a] / eps_) * SIG[a] for a in range(3)))
    sp0 = v_[:, 1] if branch > 0 else v_[:, 0]
    psi_k = np.zeros((Nn, 2), complex)
    for i, p in enumerate(pp):
        hv = np.sin(k + p * m); nv = hv / max(np.linalg.norm(hv), 1e-12)
        psi_k[i] = F[i] * ((0.5 * (np.eye(2) + branch * sum(nv[a] * SIG[a] for a in range(3)))) @ sp0)
    psi = np.stack([np.fft.ifft(psi_k[:, 0]), np.fft.ifft(psi_k[:, 1])], axis=1).ravel()
    psi /= np.linalg.norm(psi)
    rho0 = (np.abs(psi.reshape(Nn, 2)) ** 2).sum(1); m0 = (rho0 * n).sum()
    dt = T / steps; vals = [np.real(np.vdot(psi, V @ psi))]
    for _ in range(steps):
        psi = expm_multiply(-1j * H * dt, psi); vals.append(np.real(np.vdot(psi, V @ psi)))
    vals = np.array(vals)
    disp = dt / 3 * (vals[0] + vals[-1] + 4 * vals[1:-1:2].sum() + 2 * vals[2:-1:2].sum())
    rho = (np.abs(psi.reshape(Nn, 2)) ** 2).sum(1)
    return disp, ((rho * n).sum() - m0) / mm, rho[:2].sum() + rho[-2:].sum(), (n0, nc, mm)

def omega(k, branch):
    """branch curvature (vector) in the convention of the anomalous velocity rdot = dE/dk - kdot x Omega; the overall sign is fixed once, against
    orientation A, and then used unchanged for every other orientation, species and branch."""
    s_, c_ = np.sin(k), np.cos(k); e3 = np.linalg.norm(s_) ** 3
    T3 = np.array([s_[0] * c_[1] * c_[2], s_[1] * c_[2] * c_[0], s_[2] * c_[0] * c_[1]]) / e3
    return -0.5 * branch * T3

def ray(k0, ghat, s0, sc, branch, g, T, anomalous, steps=600):
    """central ray of E = branch w(s) eps(k), w = exp(g (s - sc)), s = r.ghat; with or without the anomalous velocity (a SEMICLASSICAL MODEL,
    ASSUMED here, not a result of block 54: its landed T3 is polynomial algebra and its force reading is withdrawn)."""
    def f(y):
        r, k = y[:3], y[3:]
        s_ = np.sin(k); c_ = np.cos(k); e = np.linalg.norm(s_)
        w = np.exp(g * (r @ ghat - sc))
        kdot = -branch * g * w * e * ghat
        rdot = branch * w * s_ * c_ / e
        if anomalous:
            rdot = rdot - np.cross(kdot, omega(k, branch))
        return np.concatenate([rdot, kdot])
    y = np.concatenate([s0 * ghat, k0]); y0 = y.copy(); h = T / steps
    for _ in range(steps):
        a1 = f(y); a2 = f(y + 0.5 * h * a1); a3 = f(y + 0.5 * h * a2); a4 = f(y + h * a3)
        y = y + h * (a1 + 2 * a2 + 2 * a3 + a4) / 6
    return (y - y0)[:3]

GH_X, GH_W = np.polynomial.hermite_e.hermegauss(11); GH_W = GH_W / GH_W.sum()

def drift(nvec, mhat, m, q0, branch, g=0.004, T=30.0):
    """species n: k = pi n + q0 mhat (motion along +mhat on the positive branch, -mhat on the negative, at every zero-energy point)."""
    k = np.pi * np.array(nvec, float) + q0 * mhat
    ghat = np.array(m, float) / np.linalg.norm(m)
    s_ = np.sin(k); c_ = np.cos(k); eps_ = np.linalg.norm(s_)
    v0 = branch * s_ * c_ / eps_
    dv = np.cross(ghat, v0); dv = dv / np.linalg.norm(dv)
    sigma = max(6.0, 5.0 / q0)
    res = {}
    for sg in (+1, -1):
        res[sg] = chain_run(k, m, branch, sg * g, T, sigma, dv)
    odd = 0.5 * (res[1][0] - res[-1][0])
    n0, nc, mm = res[1][3]
    pred = {}
    for anomalous in (False, True):
        tot = 0.0
        for x, wgt in zip(GH_X, GH_W):                       # the packet's momentum spread along ghat: std 1/(2 sigma)
            kk = k + x * ghat / (2 * sigma)
            tot += wgt * 0.5 * (ray(kk, ghat, n0 / mm, nc / mm, branch, g, T, anomalous) - ray(kk, ghat, n0 / mm, nc / mm, branch, -g, T, anomalous)) @ dv
        pred[anomalous] = tot
    return odd, max(res[1][2], res[-1][2]), g * T / (2 * q0), pred[False], pred[True], dv

ORIENT = [("A: motion x, gradient y", np.array([1.0, 0, 0]), (0, 1, 0)),
          ("B: motion (x+z)/sqrt2, gradient y", np.array([1.0, 0, 1.0]) / np.sqrt(2), (0, 1, 0)),
          ("C: motion (x+y+z)/sqrt3, gradient y", np.array([1.0, 1.0, 1.0]) / np.sqrt(3), (0, 1, 0)),
          ("D: motion (x-y)/sqrt2, gradient (x+y+z)/sqrt3", np.array([1.0, -1.0, 0]) / np.sqrt(2), (1, 1, 1))]
KS = (0.15, 0.25, 0.35, 0.5, 0.8, 1.2)
SPECIES = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]
t0 = time.time()
table = {}
worst_edge = 0.0
worst_berry = 0.0
for oname, mhat, m in ORIENT:
    for nvec in SPECIES:
        for branch in (+1, -1):
            row = []
            for q0 in KS:
                odd, edge, pq, pray, pberry, dv = drift(nvec, mhat, m, q0, branch)
                worst_edge = max(worst_edge, edge)
                worst_berry = max(worst_berry, abs(odd / pberry - 1))
                table[(oname, nvec, branch, q0)] = (odd, pq, pray, pberry)
                row.append((q0, odd, pq, pray, pberry))
            chi = (-1) ** sum(nvec)
            out("N %-45s point %s (det D %+d) %s branch: drift along ghat x v [/(gT/2k); rays alone; rays + curvature; measured/(rays+curvature)]: %s"
                % (oname, nvec, chi, "+" if branch > 0 else "-",
                   " | ".join("%.2f: %+.4f [%+.3f; %+.4f; %+.4f; %.4f]" % (qq, o, o / pq, pr, pb, o / pb) for qq, o, pq, pr, pb in row)))
out("N largest weight within two sites of the chain ends: %.1e (< 1e-3 required)" % worst_edge)
out("N largest |measured/(central ray + curvature) - 1| over the grid (4 orientations x 4 points x 2 branches x 6 wave vectors): %.4f" % worst_berry)
# eight points, symmetric superposition (same delta at each point)
eight = {}
for oname, mhat, m in (ORIENT[0], ORIENT[3]):
    tot = 0.0; tot_an = 0.0; parts = []
    for nvec in [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]:
        odd, _, pq, pray, _, dv = drift(nvec, mhat, m, 0.5, +1)
        parts.append((nvec, odd, odd - pray)); tot += odd; tot_an += odd - pray
    eight[oname[0]] = (tot, tot_an, abs(parts[0][2]))
    out("N eight zero-energy points, %s, q = 0.5, + branch (same delta): drift [walk minus its central ray without curvature] %s; "
        "sum of the drifts %+.2e, sum of walk minus ray %+.2e (single anomalous drift %.4f)"
        % (oname, " ".join("%s:%+.4f[%+.4f]" % pt for pt in parts), tot, tot_an, abs(parts[0][2])))
out("N reduced grid elapsed %.0f s" % (time.time() - t0))

# ------------------------------------------------------------------ one 3D packet with block 54's propagation (box 68, q = 0.5, motion x, gradient z)
def three_d(side=68, k0=0.5, g=0.004, T=30.0, sig=5.0):
    idx = np.arange(side ** 3).reshape(side, side, side)
    pos = np.stack(np.meshgrid(*[np.arange(side, dtype=float)] * 3, indexing="ij"))
    centre = np.array([side / 2.0] * 3); kvec = np.array([k0, 0, 0])
    s0, c0 = np.sin(kvec), np.cos(kvec); e0 = np.linalg.norm(s0); v0 = s0 * c0 / e0
    start = centre - v0 * (0.5 * T); rel = pos - centre[:, None, None, None]
    res = {}
    for sign in (+1, -1):
        sw = np.exp(0.5 * sign * g * rel[2])
        rows, cols, vals = [], [], []
        for j in range(3):
            lo = [slice(None)] * 3; hi = [slice(None)] * 3; lo[j] = slice(0, side - 1); hi[j] = slice(1, side)
            xa, xb = idx[tuple(lo)].ravel(), idx[tuple(hi)].ravel(); amp = (sw[tuple(lo)] * sw[tuple(hi)]).ravel()
            for s1 in range(2):
                for s2 in range(2):
                    cc = SIG[j][s1, s2]
                    if cc == 0: continue
                    rows += [2 * xb + s1, 2 * xa + s1]; cols += [2 * xa + s2, 2 * xb + s2]; vals += [0.5j * amp * cc, -0.5j * amp * cc]
        n = 2 * idx.size
        ham = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
        _, vecs = np.linalg.eigh(sum(s0[j] * SIG[j] for j in range(3))); spinor = vecs[:, 1]
        dd = pos - start[:, None, None, None]
        env = np.exp(-(dd ** 2).sum(axis=0) / (4 * sig ** 2)) * np.exp(1j * (dd[0] * kvec[0]))
        comp = [np.fft.fftn(env * spinor[0]), np.fft.fftn(env * spinor[1])]
        kk = 2 * np.pi * np.fft.fftfreq(side); kx, kyy, kzz = np.meshgrid(kk, kk, kk, indexing="ij")
        sx, sy, sz = np.sin(kx), np.sin(kyy), np.sin(kzz); e = np.sqrt(sx * sx + sy * sy + sz * sz); e[e == 0] = 1.0
        nx, ny, nz = sx / e, sy / e, sz / e
        upc = 0.5 * ((1 + nz) * comp[0] + (nx - 1j * ny) * comp[1]); dnc = 0.5 * ((nx + 1j * ny) * comp[0] + (1 - nz) * comp[1])
        psi = np.zeros(n, complex); psi[0::2] = np.fft.ifftn(upc).ravel(); psi[1::2] = np.fft.ifftn(dnc).ravel(); psi /= np.linalg.norm(psi)
        p0 = (np.abs(psi[0::2]) ** 2 + np.abs(psi[1::2]) ** 2).reshape(side, side, side); m0 = np.array([(p0 * pos[j]).sum() for j in range(3)])
        pt = expm_multiply(-1j * ham * T, psi)
        p = (np.abs(pt[0::2]) ** 2 + np.abs(pt[1::2]) ** 2).reshape(side, side, side); m1 = np.array([(p * pos[j]).sum() for j in range(3)]) / p.sum()
        res[sign] = (m1 - m0, p[:2].sum() + p[-2:].sum() + p[:, :2].sum() + p[:, -2:].sum() + p[:, :, :2].sum() + p[:, :, -2:].sum(), m0)
    odd = 0.5 * (res[1][0] - res[-1][0])
    return odd[1], max(res[1][1], res[-1][1]), res[1][2]      # sideways = along gradient(z) x motion(x) = y

def cloud3d(k0=0.5, g=0.004, T=30.0, sig=5.0, side=68):
    """rays with the curvature term, 3D momentum spread 1/(2 sig) in every direction (7-point Gauss-Hermite product), odd part along y."""
    x7, w7 = np.polynomial.hermite_e.hermegauss(7); w7 = w7 / w7.sum()
    ghat = np.array([0, 0, 1.0]); tot = np.zeros(2)
    s0 = side / 2.0 - 0.0
    for a, wa in zip(x7, w7):
        for b, wb in zip(x7, w7):
            for c, wc in zip(x7, w7):
                kk = np.array([k0, 0, 0]) + np.array([a, b, c]) / (2 * sig)
                for i, an in enumerate((False, True)):
                    tot[i] += wa * wb * wc * 0.5 * (ray(kk, ghat, 0.0, 0.0, 1, g, T, an) - ray(kk, ghat, 0.0, 0.0, 1, -g, T, an))[1]
    return tot

three = None
if len(sys.argv) < 2 or sys.argv[1] != "no3d":
    t1 = time.time()
    s3, edge3, _ = three_d()
    cr, cb = cloud3d()
    red = drift((0, 0, 0), np.array([1.0, 0, 0]), (0, 0, 1), 0.5, +1)
    three = (s3, cb)
    out("N 3D packet (box 68, width 5, q = 0.5, motion x, gradient z; block 54's propagation): sideways odd in g %+.4f (weight within two sites of the walls %.1e); "
        "3D cloud of rays: without curvature %+.4f, with curvature %+.4f (3D over cloud %.3f); reduced chain (plane wave in x, y) %+.4f; block 54 executed "
        "walk minus cloud -0.119; g T/(2k) = %.3f  (%.0f s)" % (s3, edge3, cr, cb, s3 / cb, red[0], red[2], time.time() - t1))
print()
A = [table[("A: motion x, gradient y", (0, 0, 0), 1, q0)] for q0 in KS]
out("SUMMARY: the sideways drift of the walk's packets is the anomalous velocity of the branch curvature of h = sin(k).sigma (curvature sin k_x cos k_y "
    "cos k_z/(2 eps^3) cyclically, exact): over 4 orientations (one oblique gradient) x 4 zero-energy points x 2 branches x 6 wave vectors the measured "
    "drift equals the central ray with that term to within %.1f%%; along an axis it is g T/(2 sin q) (measured/that = %s at q = %s), g T/(2k) only as "
    "k -> 0; the drift vector flips with det D = (-1)^(n_x+n_y+n_z) and is the same vector on both branches (so it is minus the sense times "
    "ghat x v on the + branch, plus on the -); in a symmetric superposition of the eight points the anomalous parts cancel (sums %+.0e, %+.0e) but the "
    "ordinary lattice ray part, which is the same at all eight points, survives for the oblique gradient (sum %+.3f; zero for axis gradients, %+.0e)%s"
    % (100 * worst_berry, eight["A"][1], eight["D"][1], eight["D"][0], eight["A"][0], ", ".join("%.3f" % (v[0] / (0.004 * 30 / (2 * np.sin(q0)))) for v, q0 in zip(A, KS)), ", ".join("%.2f" % q0 for q0 in KS),
       "" if three is None else "; the 3D box-68 packet drifts %+.4f against %+.4f for its 3D cloud" % three))
