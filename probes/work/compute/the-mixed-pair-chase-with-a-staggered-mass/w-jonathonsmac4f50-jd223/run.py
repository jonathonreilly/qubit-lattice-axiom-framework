#!/usr/bin/env python3
"""Block 71's mixed-pair chase with block 77's staggered rest term, on a ring of 1500 (block 55/71's control machinery), run 1 of 2.

As landed.
Block 71 (#8603):
  T1: twins source oppositely.
  T2 (weak pair ansatz): the pulls are antisymmetric for any signs, and a ray from rest obeys d^2x/dt^2 = -w grad w whatever
      the sign of its energy.  It gives no exact coupled conservation theorem.
Block 77 (#8612):
  Supplied family H = a0 I + 2a sum C_j + sum sigma_j S_j plus a staggered m eps, eps = (-1)^x.
  T3: odd-displacement terms anticommute with eps, and phi (K + m eps) phi = phi K phi + m w eps.
  T4: paired energies a0 +- sqrt((2a c + lambda)^2 + m^2).

Reduced ring walk (one axis, block 55's control): H = a0 + 2a C + sigma_z S + m eps; clocked H_w = phi H phi, phi = e^{u/2}.
  The a0 term becomes a0 w on-site.
  The rest term becomes m w eps.
Field (block 55's static weak-field law): 2u_z - u_{z+1} - u_{z-1} = -Gamma (s_z - mean s).
  s = e^A + e^B, with e_z = Re chi_z^dagger (H_w chi)_z.
  Solved to self-consistency at every step.
  Walkers are advanced by expm_multiply with a midpoint field (predictor-corrector).
Bodies at rest:
  Coin up; a Gaussian of width 30 in position about k* on one branch.
  Built exactly per momentum pair {k, k + pi} from the 2x2 block [[a0 + b, m], [m, a0 - b]], b = 2a cos k + sin k.
  X shows that the rest momentum is k* = -arctan(2a) and the rest energies are a0 +- m.
Wave-vector change: phase of <chi|T^2|chi>/2 (T^2 commutes with eps and is conserved by the free walk).
  Each walker's change is taken against a free (Gamma = 0) control of the same packet.
Displacements: circular mean position, against the same free control.
Ledger: <H_w>_A + <H_w>_B + (1/(2 Gamma)) sum u (2u - u+ - u-).
  At the slaved field it is exactly stationary in u, so the continuous dynamics keeps it; its drift measures the integrator.
Floating point throughout, labelled.  The identities in X are exact (sympy).
"""
import time
import numpy as np
import sympy as sp
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply

def out(s): print(s, flush=True)

# ------------------------------------------------------------------ X: exact identities
n8 = 8
T8 = sp.zeros(n8, n8)
for i in range(n8): T8[i, (i + 1) % n8] = 1
S8 = (T8 - T8.T) / (2 * sp.I); C8 = (T8 + T8.T) / 2; E8 = sp.diag(*[(-1) ** i for i in range(n8)])
ok_anti = (E8 * S8 + S8 * E8).is_zero_matrix and (E8 * C8 + C8 * E8).is_zero_matrix and (E8 * T8 * T8 - T8 * T8 * E8).is_zero_matrix
k, a, m = sp.symbols('k a m', real=True)
b = sp.sin(k) + 2 * a * sp.cos(k)
ok_shift = sp.simplify(sp.expand_trig(b - sp.sqrt(1 + 4 * a ** 2) * sp.sin(k + sp.atan(2 * a)))) == 0
blk = sp.Matrix([[b, m], [m, -b]])
ok_pair = sp.expand(blk.charpoly().as_expr() - (sp.Symbol('lambda') ** 2 - b ** 2 - m ** 2)) == 0
out("X exact:")
out("  on a ring of 8, eps anticommutes with S and with C, and commutes with T^2: %s" % ("PASS" if ok_anti else "FAIL"))
out("  on the coin-up pair block [[b, m], [m, -b]] the energies are +-sqrt(b^2 + m^2): %s" % ("PASS" if ok_pair else "FAIL"))
out("  sin k + 2a cos k = sqrt(1 + 4a^2) sin(k + arctan 2a): %s" % ("PASS" if ok_shift else "FAIL"))
out("  so on one axis the scalar hop moves the coin-up rest momentum to k* = -arctan(2a), rescales the speed by sqrt(1 + 4a^2),")
out("  and leaves the rest energies at +-m.  On one axis it does NOT put the two walkers at different levels; the offset a0 does (a0 +- m).")

L = 1500
X = np.arange(L)
EPS = (-1.0) ** X
UP = (X + 1) % L
Tr = sps.csr_matrix((np.ones(L), (X, UP)), shape=(L, L))
T2op = sps.kron(Tr @ Tr, sps.identity(2)).tocsr()

def ring_ops(u, m, a, a0):
    rt = np.exp(0.5 * u); w = rt * rt
    amp = rt[UP] * rt
    rows, cols, vals = [], [], []
    for s_, c_ in ((0, 1.0), (1, -1.0)):          # sigma_z S
        rows += [2 * X + s_, 2 * UP + s_]; cols += [2 * UP + s_, 2 * X + s_]; vals += [c_ * amp / 2j, -c_ * amp / 2j]
    for s_ in (0, 1):
        rows.append(2 * X + s_); cols.append(2 * X + s_); vals.append((m * EPS * w + a0 * w).astype(complex))
        if a:
            rows += [2 * X + s_, 2 * UP + s_]; cols += [2 * UP + s_, 2 * X + s_]; vals += [(a * amp).astype(complex)] * 2
    return sps.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * L, 2 * L))

def energy_density(h, chi): return np.real((chi.conj() * (h @ chi)).reshape(L, 2).sum(1))
def dens(chi): return (np.abs(chi) ** 2).reshape(L, 2).sum(1)
def field(s, gam):
    kk = 2 * np.pi * np.fft.fftfreq(L)
    sym = 2 - 2 * np.cos(kk); sym[0] = 1.0
    sh = np.fft.fft(-(s - s.mean())) * gam / sym; sh[0] = 0
    return np.real(np.fft.ifft(sh))
def circ_mean(p):
    ang = 2 * np.pi * X / L
    return (np.angle((p * np.exp(1j * ang)).sum()) % (2 * np.pi)) * L / (2 * np.pi)
def wrapd(d): return (d + L / 2) % L - L / 2
def kbar(chi): return np.angle(np.vdot(chi, T2op @ chi)) / 2

def body(z0, branch, m, a, a0, width=30.0):
    """Coin-up packet at rest on one branch: Gaussian about k* in the half zone, spread exactly onto {k, k+pi} by the branch eigenvector."""
    kst = -np.arctan(2 * a)
    j = np.arange(L); kk = 2 * np.pi * j / L
    half = np.abs(np.angle(np.exp(1j * (kk - kst)))) < np.pi / 2      # one member of every pair {k, k+pi}
    psi_k = np.zeros(L, complex)
    for jj in j[half]:
        k_ = kk[jj]
        dk = np.angle(np.exp(1j * (k_ - kst)))
        g = np.exp(-dk ** 2 * width ** 2) * np.exp(-1j * k_ * z0)
        bb = 2 * a * np.cos(k_) + np.sin(k_)
        E = np.hypot(bb, m)
        v = np.array([bb + branch * E, m]); v /= np.linalg.norm(v)
        psi_k[jj] += g * v[0]; psi_k[(jj + L // 2) % L] += g * v[1]
    up = np.fft.ifft(psi_k)
    psi = np.zeros(2 * L, complex); psi[0::2] = up
    return psi / np.linalg.norm(psi)

TS = (100, 200, 300)
IT = 5
def run(m, a, a0, branches, gam=0.002, dt=1.0):
    chis = [body(500.0, branches[0], m, a, a0), body(1000.0, branches[1], m, a, a0)]
    h0 = ring_ops(np.zeros(L), m, a, a0)
    free = {t: [expm_multiply(-1j * h0 * t, c) for c in chis] for t in TS}
    def src(chis, u):
        h = ring_ops(u, m, a, a0)
        return sum(energy_density(h, c) for c in chis)
    def solve_u(chis, u, it=None):
        it = IT if it is None else max(it, IT)
        for _ in range(it): u = field(src(chis, u), gam)
        return u
    def ledger(chis, u):
        h = ring_ops(u, m, a, a0)
        return sum(np.real(np.vdot(c, h @ c)) for c in chis) + (u * (2 * u - np.roll(u, 1) - np.roll(u, -1))).sum() / (2 * gam)
    u = solve_u(chis, np.zeros(L), 10)
    h = ring_ops(u, m, a, a0)
    E0 = [np.real(np.vdot(c, h @ c)) for c in chis]
    # weak-ansatz prediction of the initial pulls: dk_A/dt = -E_A <du_B/dz>_A with u_B the field of B alone
    uA_only = solve_u([chis[0]], np.zeros(L), 10); uB_only = solve_u([chis[1]], np.zeros(L), 10)
    grad = lambda uu: (np.roll(uu, -1) - np.roll(uu, 1)) / 2
    pred = [-E0[0] * (dens(chis[0]) * grad(uB_only)).sum(), -E0[1] * (dens(chis[1]) * grad(uA_only)).sum()]
    led0 = ledger(chis, u)
    k0 = [kbar(c) for c in chis]
    traj = []
    nsteps = int(round(TS[-1] / dt))
    for step in range(1, nsteps + 1):
        h = ring_ops(u, m, a, a0)
        trial = [expm_multiply(-1j * h * dt, c) for c in chis]
        u_mid = 0.5 * (u + solve_u(trial, u))
        hm = ring_ops(u_mid, m, a, a0)
        chis = [expm_multiply(-1j * hm * dt, c) for c in chis]
        u = solve_u(chis, u_mid)
        t = step * dt
        if any(abs(t - tt) < 1e-9 for tt in TS):
            tt = int(round(t))
            disp = [wrapd(circ_mean(dens(c)) - circ_mean(dens(f))) for c, f in zip(chis, free[tt])]
            dk = [kbar(c) - kbar(f) for c, f in zip(chis, free[tt])]
            traj.append((tt, disp, dk))
    return dict(E0=E0, pred=pred, traj=traj, drift=ledger(chis, u) - led0, led0=led0,
                free_dk=[kbar(f) - k_ for f, k_ in zip(free[TS[-1]], k0)])

VARIANTS = (("no scalar term (a = 0, a0 = 0)", 0.0, 0.0), ("block 77's scalar hop a = 0.1", 0.1, 0.0),
            ("offset a0 = 0.1 (walkers at different levels)", 0.0, 0.1))
PAIRS = (("mixed (A +, B -)", (+1, -1)), ("both +", (+1, +1)), ("both -", (-1, -1)))
res = {}
t0 = time.time()
out("")
out("N ring of 1500, Gamma = 0.002, dt = 1, bodies at sites 500 (A) and 1000 (B), width 30; changes against the free (Gamma = 0) control")
for vlab, a_, a0_ in VARIANTS:
    for m_ in (0.3, 0.6):
        for plab, br in PAIRS:
            r = run(m_, a_, a0_, br)
            res[(vlab, m_, plab)] = r
            tT, dispT, dkT = r["traj"][-1]
            big = max(abs(dkT[0]), abs(dkT[1]))
            acc = [2 * d / tT ** 2 for d in dispT]
            out("N %s, m = %.1f, %s:" % (vlab, m_, plab))
            out("    energies A %+.4f, B %+.4f; free control's wave-vector drift A %+.1e, B %+.1e"
                % (r["E0"][0], r["E0"][1], r["free_dk"][0], r["free_dk"][1]))
            out("    wave-vector changes at t = 300: A %+.4e, B %+.4e, sum %+.2e = %.1e of the larger"
                % (dkT[0], dkT[1], dkT[0] + dkT[1], abs(dkT[0] + dkT[1]) / big))
            out("    weak-ansatz initial rates x 300: A %+.4e, B %+.4e" % (300 * r["pred"][0], 300 * r["pred"][1]))
            out("    displacements at t = 100, 200, 300: A %s; B %s"
                % (" ".join("%+.4f" % tr[1][0] for tr in r["traj"]), " ".join("%+.4f" % tr[1][1] for tr in r["traj"])))
            out("    mean accelerations A %+.2e, B %+.2e: %s"
                % (acc[0], acc[1], "same direction (chase)" if acc[0] * acc[1] > 0 else "opposite directions"))
            out("    ledger drift %+.1e of %.5f (%.0f s)" % (r["drift"], r["led0"], time.time() - t0))

# checks on the mixed pair's residual: step, field self-consistency, coupling, time profile
out("")
rr = run(0.6, 0.1, 0.0, (+1, -1), dt=0.5)
r1 = res[("block 77's scalar hop a = 0.1", 0.6, "mixed (A +, B -)")]
out("N dt check (a = 0.1, m = 0.6, mixed): dt = 0.5 gives wave-vector changes A %+.6e, B %+.6e (sum %+.3e) against dt = 1: A %+.6e, B %+.6e (sum %+.3e)"
    % (rr["traj"][-1][2][0], rr["traj"][-1][2][1], sum(rr["traj"][-1][2]), r1["traj"][-1][2][0], r1["traj"][-1][2][1], sum(r1["traj"][-1][2])))
r0 = res[("no scalar term (a = 0, a0 = 0)", 0.6, "mixed (A +, B -)")]
IT = 20
ri = run(0.6, 0.0, 0.0, (+1, -1))
IT = 5
out("N self-consistency check (a = 0, m = 0.6, mixed): 20 field iterations per solve give sum %+.4e against 5 iterations: %+.4e"
    % (sum(ri["traj"][-1][2]), sum(r0["traj"][-1][2])))
rg = run(0.6, 0.0, 0.0, (+1, -1), gam=0.001)
out("N coupling check (a = 0, m = 0.6, mixed): Gamma = 0.001 gives changes A %+.4e, B %+.4e, sum %+.3e = %.2e of the larger (Gamma = 0.002: %.2e)"
    % (rg["traj"][-1][2][0], rg["traj"][-1][2][1], sum(rg["traj"][-1][2]), abs(sum(rg["traj"][-1][2])) / max(map(abs, rg["traj"][-1][2])),
       abs(sum(r0["traj"][-1][2])) / max(map(abs, r0["traj"][-1][2]))))
out("N residual against time for the mixed pairs (sum of the two wave-vector changes / the larger, at t = 100, 200, 300):")
for (vlab, m_, plab), r in res.items():
    if plab.startswith("mixed"):
        out("    %s, m = %.1f: %s" % (vlab, m_, "  ".join("%+.2e / %.2e" % (sum(tr[2]), max(map(abs, tr[2]))) for tr in r["traj"])))

out("")
hits = []
for (vlab, m_, plab), r in res.items():
    if not plab.startswith("mixed"): continue
    tT, dispT, dkT = r["traj"][-1]
    big = max(abs(dkT[0]), abs(dkT[1]))
    if abs(dkT[0] + dkT[1]) > 1e-4 * big:
        hits.append("the mixed pair's pulls do not cancel to 1e-4 of the larger (%s, m = %.1f): A %+.4e, B %+.4e, sum = %.1e of the larger"
                    % (vlab, m_, dkT[0], dkT[1], abs(dkT[0] + dkT[1]) / big))
    if dispT[0] * dispT[1] <= 0:
        hits.append("the mixed pair no longer chases (%s, m = %.1f): displacements A %+.4f, B %+.4f" % (vlab, m_, dispT[0], dispT[1]))
for hh in hits: out("HIT: " + hh)
mx = [(kk_, v) for kk_, v in res.items() if kk_[2].startswith("mixed")]
out("SUMMARY: block 71's mixed pair with block 77's staggered rest term (ring of 1500, Gamma = 0.002, t = 300): "
    + "; ".join("%s m = %.1f: pulls cancel to %.1e of the larger, displacements A %+.3f B %+.3f (%s)"
                % (kk_[0].split(" (")[0], kk_[1], abs(sum(v["traj"][-1][2])) / max(abs(x) for x in v["traj"][-1][2]),
                   v["traj"][-1][1][0], v["traj"][-1][1][1], "chase" if v["traj"][-1][1][0] * v["traj"][-1][1][1] > 0 else "no chase")
                for kk_, v in mx))
