#!/usr/bin/env python3
"""Cycle 712 - the fixed-source / far-field repair named as the successor by
PR #5662, applied to self_consistency_forces_poisson_note.

Parent row: docs/audit/data/ledger/se/self_consistency_forces_poisson_note.json
  criticality: critical, deps: [] (root), transitive_descendants: 727,
  load_bearing_score: 18.092.

PR #5656 showed the parent note's two operator discriminators are empty.
PR #5662 showed its finite-size caveat cannot defend the exponent, because the
self-consistent source is scale-locked to the box and the fit window lies inside
it. The successor named there was:

  "a localized source of fixed extent and fixed total mass, with the exponent
   fitted at radii OUTSIDE it."

This runner performs it, and reaches the opposite conclusion from the two prior
cycles about the PHYSICS while sharpening the conclusion about the EVIDENCE:

  * under a far-field protocol, unscreened Poisson uniquely gives the Newtonian
    exponent, so the parent note's operator-preference CONCLUSION is correct;
  * the parent note's own diagnostic is not merely noisy, it is INVERTED - under
    its window the biharmonic rival scores the Newtonian exponent and Poisson
    does not.

IMPORTANT SCOPE NOTE ON WHAT IS AND IS NOT NEW HERE.
Poisson's own far field is already landed repo content. Both
  docs/LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md
  docs/GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md
establish G(r) = 1/(4 pi r) + [5/(32 pi)] K4(nhat)/r^3 + O(1/r^5) on Z^3. U1
below is therefore a CONTROL that validates this runner's protocol against
already-landed content, not a new derivation. What is new is U2/U4 (the window
protocol inverts the ranking) and U5-U8 (the same measurement for the rival
operators, which the repo does not have).

Protocol. Every operator in the parent note's family is diagonal in Fourier
space on a periodic lattice, so the Green's function is exact and cheap at large
N and the Dirichlet boundary artifact is removed rather than modelled. Periodic
boundaries are NOT the parent note's Dirichlet boundaries; U4 runs the parent
note's own Dirichlet operators so the inversion is demonstrated on its actual
construction.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import splu

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import frontier_self_consistent_field_equation as F  # noqa: E402

FIX_LO, FIX_HI = 4, 10          # the fixed far-field window
PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")
    return condition


def laplacian_symbol(N: int) -> np.ndarray:
    k = 2 * np.pi * np.fft.fftfreq(N)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    return 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz)) - 6.0


def greens_periodic(N: int, power: int = 1, mu2: float = 0.0) -> np.ndarray:
    """Exact Green's function of (Delta - mu2)^power on the torus, zero mode
    removed. Uses the same nearest-neighbour stencil as the parent runner's
    build_laplacian_sparse, verified in U0."""
    d = np.zeros((N, N, N))
    d[0, 0, 0] = 1.0
    sym = (laplacian_symbol(N) - mu2) ** power
    dh = np.fft.fftn(d)
    out = np.zeros_like(dh)
    nz = np.abs(sym) > 1e-13
    out[nz] = dh[nz] / sym[nz]
    return np.real(np.fft.ifftn(out))


def axis_fit(phi: np.ndarray, lo: int, hi: int, origin=(0, 0, 0)):
    """log-log slope of |phi| along +y over integer radii [lo, hi]."""
    rs, vs = [], []
    for r in range(lo, hi + 1):
        idx = (origin[0], origin[1] + r, origin[2])
        if idx[1] >= phi.shape[1]:
            break
        v = abs(float(phi[idx]))
        if v > 1e-300:
            rs.append(float(r))
            vs.append(v)
    if len(rs) < 3:
        return float("nan"), float("nan")
    lnr, lnv = np.log(rs), np.log(vs)
    c = np.polyfit(lnr, lnv, 1)
    fit = c[0] * lnr + c[1]
    ssr = float(np.sum((lnv - fit) ** 2))
    sst = float(np.sum((lnv - np.mean(lnv)) ** 2))
    return float(-c[0]), float(1.0 - ssr / sst if sst > 0 else 0.0)


def dirichlet_greens(N: int, which: str) -> np.ndarray:
    """Green's function of the parent runner's OWN Dirichlet operator."""
    A, M = F.build_laplacian_sparse(N)
    Op = A if which == "poisson" else (A @ A)
    lu = splu(Op.tocsc())
    d = np.zeros((N, N, N))
    d[(N // 2, N // 2, N // 2)] = 1.0
    out = np.zeros((N, N, N))
    out[1:N - 1, 1:N - 1, 1:N - 1] = lu.solve(
        d[1:N - 1, 1:N - 1, 1:N - 1].ravel()).reshape((M, M, M))
    return out


print(__doc__)
print("=" * 78)
print("PART A - the protocol, validated against landed repo content")
print("=" * 78)

# --- U0 ---------------------------------------------------------------------
# The Fourier symbol must be the symbol of the parent runner's own stencil,
# otherwise every later row tests a different operator.
Nc = 8
A, M = F.build_laplacian_sparse(Nc)
dense = A.toarray()
diag_ok = bool(np.all(np.diag(dense) == -6.0))
offdiag_vals = sorted(set(dense[dense != 0].tolist()))
nn_count = int((dense[0] != 0).sum())
check(
    "U0  the Fourier symbol used here is the symbol of the parent runner's own "
    "nearest-neighbour stencil",
    diag_ok and offdiag_vals == [-6.0, 1.0],
    f"parent stencil diagonal is -6 everywhere: {diag_ok}\n"
    f"distinct nonzero entries of the parent Laplacian: {offdiag_vals}\n"
    f"symbol used here: 2*(cos kx + cos ky + cos kz) - 6, which is the exact\n"
    "Fourier transform of a -6 diagonal with unit nearest-neighbour couplings\n"
    "falsifier: a different diagonal or off-diagonal value, which would mean the\n"
    "periodic rows test a different operator from the parent note's.",
)

# --- U1 (CONTROL) -----------------------------------------------------------
NS_FIX = (32, 48, 64, 96, 128, 192)
u1 = []
for N in NS_FIX:
    G = -greens_periodic(N, 1)
    b, r2 = axis_fit(G, FIX_LO, FIX_HI)
    u1.append((N, b, r2, 4 * np.pi * FIX_HI * float(G[0, FIX_HI, 0])))
betas1 = [b for _, b, _, _ in u1]
norms1 = [v for _, _, _, v in u1]
check(
    "U1  CONTROL: with the window held FIXED and the box grown, Poisson "
    "reproduces the repo's landed asymptotic",
    all(betas1[i] > betas1[i + 1] for i in range(len(betas1) - 1))
    and betas1[-1] < 1.15
    and all(norms1[i] < norms1[i + 1] for i in range(len(norms1) - 1))
    and norms1[-1] > 0.85,
    "\n".join(f"    N={N:4d}  beta={b:8.5f}  R^2={r2:.5f}  "
              f"4*pi*r*G at r={FIX_HI} = {v:.5f}" for N, b, r2, v in u1) + "\n"
    f"beta decreases monotonically to {betas1[-1]:.5f} and 4*pi*r*G rises "
    f"monotonically to {norms1[-1]:.5f}\n"
    "the landed repo result is G(r) = 1/(4 pi r) + O(1/r^3), i.e. beta -> 1 and\n"
    "4*pi*r*G -> 1. This row is NOT a new derivation: it validates this runner's\n"
    "protocol against content the repo already has, so that the rival rows below\n"
    "can be trusted.\n"
    "falsifier: beta failing to approach 1 or 4*pi*r*G failing to approach 1,\n"
    "which would mean the protocol itself is wrong.",
)

# --- U2 ---------------------------------------------------------------------
u2 = []
for N in NS_FIX:
    G = -greens_periodic(N, 1)
    lo, hi = max(3, N // 16), N // 4
    b, r2 = axis_fit(G, lo, hi)
    u2.append((N, lo, hi, b, r2, 4 * np.pi * hi * float(G[0, hi, 0])))
late = [b for _, _, _, b, _, _ in u2][-3:]
check(
    "U2  a SCALING window converges to the WRONG value on the same operator and "
    "the same boundary-free lattice",
    max(late) - min(late) < 0.02 and abs(late[-1] - 1.0) > 0.5,
    "\n".join(f"    N={N:4d}  window {lo}..{hi:<3d}  beta={b:8.5f}  R^2={r2:.5f}  "
              f"4*pi*r*G at the outer edge = {v:.5f}"
              for N, lo, hi, b, r2, v in u2) + "\n"
    f"the last three sizes agree to {max(late) - min(late):.5f}, so this looks "
    f"converged,\nand it is converged to {late[-1]:.4f} rather than to 1.0. "
    "The normalisation\n4*pi*r*G sits near 0.65 rather than 1.\n"
    "a window whose radii scale with the box never leaves the region where the\n"
    "periodic images matter, so it measures a box property and reports it as a\n"
    "stable exponent. That is worse than failing to converge: it is a diagnostic\n"
    "that looks trustworthy and is wrong.\n"
    "falsifier: the scaling window also converging to 1.0, which would mean the\n"
    "window choice is immaterial.",
)

print()
print("=" * 78)
print("PART B - the parent note's window is a scaling window, and it inverts")
print("=" * 78)

# --- U3 ---------------------------------------------------------------------
src = (REPO_ROOT / "scripts" / "frontier_self_consistent_field_equation.py").read_text()
win_line = "for dy in range(1, mid - 2):"
mask_line = "mask = (np.abs(phi_arr) > 1e-30) & (r_arr > 1)"
check(
    "U3  the parent note's own decay diagnostic uses a window whose radii scale "
    "with the lattice",
    win_line in src and mask_line in src,
    f"check_field_physics contains {win_line!r}: {win_line in src}\n"
    f"check_field_physics contains {mask_line!r}: {mask_line in src}\n"
    "with mid = N//2 those two lines make the fit window radii 2..N//2-3, whose\n"
    "outer edge is a fixed fraction of the lattice. So the parent diagnostic is a\n"
    "scaling window in the exact sense U2 measures.\n"
    "falsifier: a window with N-independent endpoints in the parent source.",
)

# --- U4 ---------------------------------------------------------------------
NS_DIR = (16, 20, 24, 32, 40)
u4 = {}
for which in ("poisson", "biharmonic"):
    rows = []
    for N in NS_DIR:
        G = dirichlet_greens(N, which)
        b, r2 = axis_fit(G, 2, N // 2 - 3, origin=(N // 2, N // 2, N // 2))
        rows.append((N, b, r2))
    u4[which] = rows
p_dir = [b for _, b, _ in u4["poisson"]]
b_dir = [b for _, b, _ in u4["biharmonic"]]
inverted = all(abs(b_dir[i] - 1.0) < abs(p_dir[i] - 1.0) for i in range(len(b_dir)))
check(
    "U4  under the parent note's own window on its own Dirichlet operators the "
    "ranking is INVERTED: the biharmonic rival scores the Newtonian exponent",
    inverted and min(abs(b - 1.0) for b in b_dir) < 0.1
    and min(abs(b - 1.0) for b in p_dir) > 0.5,
    "\n".join(f"    N={N:3d}  window 2..{N//2-3:<3d}  poisson beta={pb:7.4f}  "
              f"biharmonic beta={bb:7.4f}"
              for (N, pb, _), (_, bb, _) in zip(u4["poisson"], u4["biharmonic"]))
    + f"\nbiharmonic reaches abs(beta-1) = "
      f"{min(abs(b - 1.0) for b in b_dir):.4f}; Poisson never gets closer than "
      f"{min(abs(b - 1.0) for b in p_dir):.4f}\n"
    "so on the parent note's actual construction, with the parent note's actual\n"
    "diagnostic, the operator whose far field is asymptotically FLAT (U5) is\n"
    "scored as the Newtonian one and the operator whose far field is exactly 1/r\n"
    "(U1) is scored as badly non-Newtonian. The diagnostic is inverted rather\n"
    "than merely noisy, which is why PR #5656 measured the biharmonic rival as\n"
    "closer to the target on the self-consistent field.\n"
    "falsifier: Poisson scoring closer to 1 than biharmonic at any tested size.",
)

print()
print("=" * 78)
print("PART C - the rivals' true far fields, which the repo does not have")
print("=" * 78)

# --- U5 ---------------------------------------------------------------------
u5 = []
for N in NS_FIX:
    b, r2 = axis_fit(greens_periodic(N, 2), FIX_LO, FIX_HI)
    u5.append((N, b, r2, b * N))
betas5 = [b for _, b, _, _ in u5]
prods = [p for _, _, _, p in u5][1:]
check(
    "U5  the biharmonic rival's far field is asymptotically FLAT: its exponent "
    "goes to zero like 1/N",
    all(betas5[i] > betas5[i + 1] for i in range(len(betas5) - 1))
    and betas5[-1] < 0.2
    and (max(prods) - min(prods)) / np.mean(prods) < 0.25,
    "\n".join(f"    N={N:4d}  beta={b:8.5f}  R^2={r2:.5f}  beta*N={p:7.2f}"
              for N, b, r2, p in u5) + "\n"
    f"beta falls monotonically to {betas5[-1]:.5f}, and beta*N is roughly "
    f"constant near {np.mean(prods):.1f},\nso beta ~ const/N -> 0. A vanishing "
    "exponent means no decay at all: the\nbiharmonic potential is asymptotically "
    "constant, which is maximally\nun-Newtonian rather than nearly Newtonian.\n"
    "falsifier: beta converging to a nonzero constant, especially 1.",
)

# --- U6 ---------------------------------------------------------------------
u6 = []
for N in (64, 96):
    g = np.mgrid[0:N, 0:N, 0:N].astype(float)
    for a in range(3):
        g[a] = np.minimum(g[a], N - g[a])
    ker = 1.0 / np.maximum(g[0] ** 2 + g[1] ** 2 + g[2] ** 2, 1.0)
    b, r2 = axis_fit(ker, FIX_LO, FIX_HI)
    u6.append((N, b, r2))
d32 = np.zeros((32, 32, 32))
d32[(16, 16, 16)] = 1.0
loc = F.solve_local(32, d32, 0.5)
loc_nonzero = int(np.sum(np.abs(loc) > 0))
check(
    "U6  the 1/r^2 kernel gives exactly 2 and the local operator has no extended "
    "field at all",
    all(abs(b - 2.0) < 1e-9 for _, b, _ in u6) and loc_nonzero == 1,
    "\n".join(f"    N={N:4d}  inv_r^2 kernel beta={b:.9f}  R^2={r2:.6f}"
              for N, b, r2 in u6) + "\n"
    f"local operator phi = G*rho from a point source: nonzero sites = "
    f"{loc_nonzero}\n"
    "the 1/r^2 kernel returns its own defining exponent, as it must, and it is 2\n"
    "rather than 1. The local operator produces a field only at the source site,\n"
    "so it has no decay exponent to compare.\n"
    "falsifier: either giving 1.",
)

# --- U7 ---------------------------------------------------------------------
NS_SCR = 192
u7 = []
for mu2 in (0.0, 0.01, 0.1, 0.5, 1.0, 2.0):
    b, r2 = axis_fit(-greens_periodic(NS_SCR, 1, mu2), FIX_LO, FIX_HI)
    u7.append((mu2, b, r2))
unscreened = u7[0][1]
check(
    "U7  within the screened family the exponent rises monotonically with the "
    "mass, so the unscreened case is uniquely the near-Newtonian one",
    all(u7[i][1] < u7[i + 1][1] for i in range(len(u7) - 1))
    and abs(unscreened - 1.0) < 0.15
    and all(abs(b - 1.0) > 0.5 for _, b, _ in u7[1:]),
    f"fixed window {FIX_LO}..{FIX_HI}, N={NS_SCR}, boundary-free:\n"
    + "\n".join(f"    mu^2={mu2:<5} beta={b:8.4f}  R^2={r2:.5f}" for mu2, b, r2 in u7)
    + "\nonly mu^2 = 0 lands near 1. This is the parent note's Test 4 conclusion,\n"
      "confirmed on a far-field diagnostic; it is consistent with PR #5656 R13,\n"
      "which showed the source-sign defect never reached Test 4.\n"
      "falsifier: a screened member landing closer to 1 than the unscreened case.",
)

# --- U8 ---------------------------------------------------------------------
summary = {
    "poisson (unscreened)": betas1[-1],
    "biharmonic": betas5[-1],
    "inv_r^2 kernel": u6[-1][1],
    "screened mu^2=0.1": [b for m, b, _ in u7 if m == 0.1][0],
}
others = [v for k, v in summary.items() if not k.startswith("poisson")]
check(
    "U8  so unscreened Poisson uniquely gives the Newtonian exponent, and the "
    "separation from every rival is of order 1",
    abs(summary["poisson (unscreened)"] - 1.0) < 0.15
    and all(abs(v - 1.0) > 0.5 for v in others),
    "\n".join(f"    {k:22s} beta = {v:8.4f}   abs(beta-1) = {abs(v-1.0):7.4f}"
              for k, v in summary.items()) + "\n"
    "local is excluded separately by U6 for having no extended field.\n"
    "the parent note's Bounded Claim 1 asserted exactly this preference. On a\n"
    "far-field diagnostic it holds, and the margin is of order 1 rather than the\n"
    "0.156 that PR #5656 measured inside a finite-size budget. The conclusion is\n"
    "recovered; the parent note's evidence for it never tested a far field.\n"
    "falsifier: any rival within 0.5 of 1, or Poisson further than 0.15 from it.",
)

print()
print("=" * 78)
print("PART D - but this cannot be done inside the self-consistent construction")
print("=" * 78)


def propagate(N, renormalize):
    """The parent propagator at phi = 0 with the per-layer and global
    normalization switchable. Identical to cycle 710 R1's verified
    reimplementation."""
    sx = sy = sz = N // 2
    yy, zz = np.mgrid[0:N, 0:N]
    psi0 = np.exp(-((yy - sy) ** 2 + (zz - sz) ** 2) / (2 * 2.0 ** 2)).astype(complex)
    psi0 /= np.sqrt(np.sum(np.abs(psi0) ** 2))
    dens = np.zeros((N, N, N))
    dens[sx, :, :] = np.abs(psi0) ** 2
    offs = [(a, b, math.sqrt(1 + a * a + b * b))
            for a in (-1, 0, 1) for b in (-1, 0, 1)]
    for direction in (+1, -1):
        pl = psi0.copy()
        rng = range(sx + 1, N) if direction == +1 else range(sx - 1, -1, -1)
        for xn in rng:
            pn = np.zeros((N, N), dtype=complex)
            for a, b, L in offs:
                s1, d1 = ((slice(0, N - a), slice(a, N)) if a > 0 else
                          ((slice(0, N), slice(0, N)) if a == 0
                           else (slice(-a, N), slice(0, N + a))))
                s2, d2 = ((slice(0, N - b), slice(b, N)) if b > 0 else
                          ((slice(0, N), slice(0, N)) if b == 0
                           else (slice(-b, N), slice(0, N + b))))
                pn[d1, d2] += np.exp(1j * 5.0 * L) / L * pl[s1, s2]
            if renormalize:
                nr = np.sqrt(np.sum(np.abs(pn) ** 2))
                if nr > 1e-30:
                    pn /= nr
            pl = pn
            dens[xn, :, :] += np.abs(pl) ** 2
    if renormalize:
        t = dens.sum()
        if t > 1e-30:
            dens /= t
    return dens


u9 = []
for N in (16, 24, 32, 40, 48):
    s = N // 2
    g = np.mgrid[0:N, 0:N, 0:N].astype(float)
    rad = np.sqrt((g[0] - s) ** 2 + (g[1] - s) ** 2 + (g[2] - s) ** 2)
    row = [N]
    for rn in (True, False):
        d = propagate(N, rn)
        m = float(d.sum())
        row.append((math.sqrt(float((d * rad ** 2).sum() / m)) / N, m))
    u9.append(row)
ratios_off = [r[2][0] for r in u9]
masses_off = [r[2][1] for r in u9]
ratios_on = [r[1][0] for r in u9]
check(
    "U9  removing the per-layer normalization does NOT localize the source: it "
    "spreads further and the total mass diverges",
    (max(ratios_off) - min(ratios_off)) < 0.05
    and min(ratios_off) > max(ratios_on)
    and masses_off[-1] / masses_off[0] > 1e10,
    "\n".join(f"    N={N:3d}  normalized: RMS/N={a:.4f}   "
              f"un-normalized: RMS/N={b:.4f}  total mass={m:.4e}"
              for N, (a, _), (b, m) in u9) + "\n"
    f"un-normalized RMS/N stays within "
    f"[{min(ratios_off):.4f}, {max(ratios_off):.4f}], i.e. still a fixed\n"
    f"fraction of the box, and larger than the normalized "
    f"{max(ratios_on):.4f}. Total mass grows\nby a factor "
    f"{masses_off[-1]/masses_off[0]:.2e} over this range.\n"
    "so neither branch supplies a fixed localized source. With the normalization\n"
    "the source is scale-locked (PR #5662 S5); without it the source is more\n"
    "spread AND the amplitude diverges. The far-field repair therefore requires\n"
    "an externally prescribed source and cannot be obtained from the parent\n"
    "note's self-consistent loop at all.\n"
    "falsifier: the un-normalized RMS saturating at a fixed absolute value with\n"
    "bounded total mass, which would have made the repair self-consistent.",
)

print()
print("=" * 78)
print(f"TOTAL: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
print("=" * 78)
sys.exit(0 if FAIL_COUNT == 0 else 1)
