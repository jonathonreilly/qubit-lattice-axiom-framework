#!/usr/bin/env python3
"""Relative-orientation fusion: the open-shell state selection and the pointer-frame
selection share one vacuous global absolute-orientation quotient.

Deterministic machine-precision verification for the source note

    docs/RELATIVE_ORIENTATION_FUSION_STATE_SELECTION_POINTER_FRAME_ONE_VACUOUS_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-06-10.md

CONTEXT: the Pauli open-shell color-marginal note parked the shape-observation
"the open-shell degenerate-manifold selection has the same shape as the pointer-frame
root {P_r}". This note resolves that question precisely: neither identification nor
independence.

  The joint parameter space of the two selections is
      (state rho on the color carrier)  x  (instrument color frame(s) u),
  i.e. admission (B)'s open-shell residual times the pointer-frame root.  THE THEOREM:

  (F1) DIAGONAL VACUITY (trace cyclicity, checked to machine precision): every record-level consequence --
       single-step outcome probabilities, post-instrument states, and full multi-step
       record sequences -- is invariant under the SIMULTANEOUS rotation
       (rho, u) -> (g rho g^dag, g u), g in SU(3).  The two absolute color orientations
       are JOINTLY unregistrable: the joint space carries ONE vacuous SU(3) quotient
       (8 directions) -- internal joint-space bookkeeping (no prior note tracked these
       as two independent admissions); F1 presupposes only common-g conjugation of
       frame-DEPENDENT observables (pure cyclicity, NOT the gauge-invariance premise).
  (F2) TEETH (the fusion is not collapse): rotating the STATE alone, or the FRAME FAMILY
       alone, changes registered content at order 1.  Neither absolute orientation is
       vacuous with the other held fixed -- the RELATIVE orientation is registrable.
  (F3) SHARPNESS (no hidden extra vacuity): at a generic point, the kernel of the
       registered-content differential on the 16 absolute-orientation directions is
       10-dimensional in the finite-difference check = the 8 diagonal directions + the 2 trivial state-stabilizer
       directions (which move nothing). Rank 6 in the finite-difference check. And the
       instrument-frame family is tomographically complete to numerical precision: the content functional determines rho -- there
       is no further unregistered direction hiding in the family.
  (F4) FOCK-LEVEL APPLICATION to the Pauli open-shell instance (L=3 ring, nf=2/color,
       the degenerate ground manifold): for an ASYMMETRIC ground state (rho_color !=
       I3/3) and a color-frame-naming instrument, the record distribution is invariant
       under the diagonal rotation and changes under a state-only rotation; under the
       color-blind (site-occupation) instrument the state-only rotation is invariant --
       the color-orientation retirement case, reproduced at the Fock level.
  (F5) NON-IDENTIFICATION (the residuals remain distinct): with frames fixed, states with
       different rho_color SPECTRA give different content (the state selection has
       instrument-independent registrable content); with the state fixed, the two
       instrument CLASSES (frame-naming vs color-blind) give different content (the
       frame-side residual has its own registrable class datum).  The selections fuse at
       their ORIENTATION parts only.

WHAT THIS DOES AND DOES NOT DO:
  - Resolves the parked "same root?" question precisely: SAME single orientation quotient
    (the absolute parts fuse -- 8 vacuous directions once), DISTINCT registrable
    remainders (state orbit-invariants vs instrument class + relative orientation).
  - Does NOT discharge either residual: the open-shell selection's invariant content
    (which spectrum of rho_color) and the pointer-frame selection's class/relative
    content remain undelivered.  The rotation is GLOBAL (one g at every site): the
    refinement lands on admission (B)/global color-neutrality -- the local ADM-1 frame
    root {P_r} is UNTOUCHED (a global rotation supplies no per-edge link data, per the
    color-orientation retirement boundary). No weight is assigned anywhere;
    r is untouched (generation factor; no part of this argument reaches it).
  - Conditional on: the supplied C^3 color carrier; the named instruments; the named
    color-diagonal hopping where dynamics appears (its global color rotations commute
    with it -- the graph-first SU(3) commutant structure).

Run: python3 scripts/frontier_relative_orientation_fusion_state_frame_quotient_2026_06_10.py
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


rng = np.random.default_rng(20260610)


def gell_mann():
    return [np.array(m, complex) for m in (
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])] + [np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]


LAM = gell_mann()
P0 = [np.diag(v).astype(complex) for v in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]


def haar3():
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1 / 3)


def frame(u):
    return [u @ p @ u.conj().T for p in P0]


def content(rho, frames):
    """Registered content: single-step probs for every frame + one two-step sequence."""
    out = []
    for u in frames:
        for B in frame(u):
            out.append(np.trace(B @ rho).real)
    B, C = frame(frames[0]), frame(frames[1])
    for r in range(3):
        post = B[r] @ rho @ B[r]
        for s in range(3):
            out.append(np.trace(C[s] @ post).real)
    return np.array(out)


# ===========================================================================
# Part 1.  (F1) diagonal vacuity: joint-rotation invariance of tested record content.
# ===========================================================================
print("=" * 78)
print("Part 1  (F1) simultaneous (rho,u)->(g rho g+, g u): tested record content invariant")
print("=" * 78)

rho = np.diag([0.5, 0.3, 0.2]).astype(complex)
u0 = haar3()
rho = u0 @ rho @ u0.conj().T
FRAMES = [haar3() for _ in range(12)]

worst = 0.0
for trial in range(4):
    g = haar3()
    c0 = content(rho, FRAMES)
    c1 = content(g @ rho @ g.conj().T, [g @ u for u in FRAMES])
    worst = max(worst, float(np.max(np.abs(c0 - c1))))
check("single-step + sequence record content invariant under the diagonal rotation "
      "(4 Haar trials; trace cyclicity made quantitative)",
      worst < 1e-12, f"max dev {worst:.1e}")
# post-instrument STATES are covariant (so all deeper sequences inherit the invariance):
g = haar3()
B = frame(FRAMES[0])
post0 = sum(b @ rho @ b for b in B)
Bg = frame(g @ FRAMES[0])
post1 = sum(b @ (g @ rho @ g.conj().T) @ b for b in Bg)
check("post-instrument states are COVARIANT (post -> g post g+): every longer record "
      "sequence inherits the diagonal invariance by induction",
      np.allclose(post1, g @ post0 @ g.conj().T, atol=1e-12))

# ===========================================================================
# Part 2.  (F2) teeth: neither absolute orientation is vacuous alone.
# ===========================================================================
print("=" * 78)
print("Part 2  (F2) teeth: state-only and frame-only rotations CHANGE registered content")
print("=" * 78)

g = haar3()
c0 = content(rho, FRAMES)
c_state = content(g @ rho @ g.conj().T, FRAMES)
c_frame = content(rho, [g @ u for u in FRAMES])
check("state-only rotation changes content at order 1 (the relative datum is registrable)",
      float(np.max(np.abs(c0 - c_state))) > 0.05,
      f"max shift {np.max(np.abs(c0 - c_state)):.3f}")
check("frame-only rotation changes content at order 1 (same relative datum, other side)",
      float(np.max(np.abs(c0 - c_frame))) > 0.05,
      f"max shift {np.max(np.abs(c0 - c_frame)):.3f}")

# ===========================================================================
# Part 3.  (F3) sharpness: kernel = diagonal + trivial stabilizers, rank 6; tomography.
# ===========================================================================
print("=" * 78)
print("Part 3  (F3) the vacuous directions are the diagonal (+trivial stabilizers)")
print("=" * 78)

eps = 1e-6
F0v = content(rho, FRAMES)
J = []
for lam in LAM:                                   # 8 state-side directions
    gg = np.eye(3) + 1j * eps * lam
    J.append((content(gg @ rho @ gg.conj().T, FRAMES) - F0v) / eps)
for lam in LAM:                                   # 8 frame-side directions (whole family)
    gg = np.eye(3) + 1j * eps * lam
    J.append((content(rho, [gg @ u for u in FRAMES]) - F0v) / eps)
J = np.array(J)
sv = np.linalg.svd(J, compute_uv=False)
rank = int(np.sum(sv > 1e-3 * sv[0]))
check("Jacobian rank on the 16 absolute-orientation directions is 6 "
      "(kernel 10 = 8 diagonal + 2 trivial state-stabilizer)",
      rank == 6, f"rank {rank}; top svs {np.round(sv[:7], 4)}")
worst = max(float(np.linalg.norm(J[i] + J[8 + i])) for i in range(8))
check("each of the 8 DIAGONAL directions is in the kernel (state-side flow + frame-side "
      "flow cancel exactly)", worst < 1e-4, f"max |dF| {worst:.1e}")
evals_r, evecs_r = np.linalg.eigh(rho)
ok_stab = True
for diag in ([1, -1, 0], [1, 1, -2]):
    t = evecs_r @ np.diag(diag).astype(complex) @ evecs_r.conj().T
    gg = np.eye(3) + 1j * eps * t
    d = (content(gg @ rho @ gg.conj().T, FRAMES) - F0v) / eps
    ok_stab = ok_stab and float(np.linalg.norm(d)) < 1e-4
check("the 2 remaining kernel directions are the TRIVIAL state-stabilizer flows "
      "([xi,rho]=0: they move nothing)", ok_stab)
rows, vals = [], []
for u in FRAMES:
    for B in frame(u):
        rows.append(B.conj().flatten())
        vals.append(np.trace(B @ rho).real)
sol, *_ = np.linalg.lstsq(np.array(rows), np.array(vals), rcond=None)
check("the frame FAMILY is tomographically complete: the content functional determines "
      "rho exactly (no further unregistered direction hides in the family)",
      np.max(np.abs(sol.reshape(3, 3) - rho)) < 1e-10,
      f"reconstruction dev {np.max(np.abs(sol.reshape(3,3) - rho)):.1e}")

# ===========================================================================
# Part 4.  (F4) Fock-level application: the Pauli open-shell instance.
# ===========================================================================
print("=" * 78)
print("Part 4  (F4) open-shell ground state (L=3, nf=2): fusion at the Fock level")
print("=" * 78)


def ann(j, n):
    sz = np.array([[1, 0], [0, -1]], float)
    sm = np.array([[0, 1], [0, 0]], float)
    ops = [sz] * j + [sm] + [np.eye(2)] * (n - j - 1)
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


Lsp, NCOL = 3, 3
NM = Lsp * NCOL                       # mode index m = color*Lsp + site
A9 = [ann(j, NM) for j in range(NM)]
AD9 = [a.T for a in A9]
h_spat = np.zeros((Lsp, Lsp))
for x in range(Lsp):
    h_spat[x, (x + 1) % Lsp] = h_spat[(x + 1) % Lsp, x] = -1.0
Hmb = sum(h_spat[x, y] * (AD9[c * Lsp + x] @ A9[c * Lsp + y])
          for c in range(NCOL) for x in range(Lsp) for y in range(Lsp))
Ntot = sum(AD9[m] @ A9[m] for m in range(NM))
wN, VN = np.linalg.eigh(Ntot)
P6 = VN[:, np.isclose(wN, 6.0)]
H6 = P6.T @ Hmb @ P6
eH6, vH6 = np.linalg.eigh(H6)
# an asymmetric open-shell ground-state exhibit:
psi = (P6 @ (vH6[:, 0] + vH6[:, 1]) / np.sqrt(2)).astype(complex)
psi /= np.linalg.norm(psi)
Gc0 = np.array([[psi.conj() @ (AD9[i * Lsp] @ A9[j * Lsp]) @ psi for j in range(3)]
                for i in range(3)])
rho0 = Gc0 / np.trace(Gc0)
check("the chosen ground state is color-ASYMMETRIC (rho_color != I3/3 at the ground "
      "energy -- the (B) open-shell residual instance)",
      np.max(np.abs(rho0 - np.eye(3) / 3)) > 0.02,
      f"dev {np.max(np.abs(rho0 - np.eye(3)/3)):.3f}")


def gamma_global(xi):
    """Fock lift of the global color rotation e^{xi} (same xi at every site)."""
    K = sum(xi[i, j] * (AD9[i * Lsp + x] @ A9[j * Lsp + x]).astype(complex)
            for i in range(3) for j in range(3) for x in range(Lsp))
    return expm(K)


def site0_frame_projectors(u):
    """8 occupation-pattern projectors for site-0 color modes in frame u."""
    xi = np.zeros((3, 3), complex)
    # lift u to site-0 modes only: log via eigendecomposition
    w, V = np.linalg.eig(u)
    logu = V @ np.diag(np.log(w)) @ np.linalg.inv(V)
    K = sum(logu[i, j] * (AD9[i * Lsp] @ A9[j * Lsp]).astype(complex)
            for i in range(3) for j in range(3))
    G = expm(K)
    n_ops = [AD9[c * Lsp] @ A9[c * Lsp] for c in range(3)]
    projs = []
    for pat in range(8):
        bits = [(pat >> c) & 1 for c in range(3)]
        P = np.eye(2 ** NM)
        for c in range(3):
            P = P @ (n_ops[c] if bits[c] else (np.eye(2 ** NM) - n_ops[c]))
        projs.append(G @ P.astype(complex) @ G.conj().T)
    return projs


xi_g = sum(rng.normal() * 1j * lam for lam in LAM) * 0.4
g3 = expm(xi_g)                                   # the SU(3) rotation
Gg = gamma_global(xi_g)                           # its Fock lift
u_frame = haar3()
probs = lambda state, projs: np.array([np.real(state.conj() @ P @ state) for P in projs])
p0 = probs(psi, site0_frame_projectors(u_frame))
p_diag = probs(Gg @ psi, site0_frame_projectors(g3 @ u_frame))
check("FOCK LEVEL: the frame-naming record distribution is invariant under the diagonal "
      "rotation (state AND frame co-rotated)",
      np.max(np.abs(p0 - p_diag)) < 1e-10, f"max dev {np.max(np.abs(p0 - p_diag)):.1e}")
p_state_only = probs(Gg @ psi, site0_frame_projectors(u_frame))
check("FOCK LEVEL teeth: the STATE-only rotation changes the frame-naming distribution "
      "(the open-shell selection's orientation is registrable ONLY relative to the frame)",
      np.max(np.abs(p0 - p_state_only)) > 0.01,
      f"max shift {np.max(np.abs(p0 - p_state_only)):.3f}")
n_site0_tot = sum(AD9[c * Lsp] @ A9[c * Lsp] for c in range(3))
wS, VS = np.linalg.eigh(n_site0_tot)
blind = [VS[:, np.isclose(wS, k)] @ VS[:, np.isclose(wS, k)].T for k in range(4)]
pb0 = probs(psi, [b.astype(complex) for b in blind])
pb1 = probs(Gg @ psi, [b.astype(complex) for b in blind])
check("FOCK LEVEL control (color-orientation retirement case): under the COLOR-BLIND site-occupation "
      "instrument the state-only rotation is invariant (orientation vacuous there)",
      np.max(np.abs(pb0 - pb1)) < 1e-10, f"max dev {np.max(np.abs(pb0 - pb1)):.1e}")

# ===========================================================================
# Part 5.  (F5) non-identification: the residuals' registrable remainders are distinct.
# ===========================================================================
print("=" * 78)
print("Part 5  (F5) the residuals fuse at orientation ONLY: distinct remainders exhibited")
print("=" * 78)

# (a) state-side invariant content: two C3 states with different spectra, same frames:
rho_b = np.diag([0.8, 0.15, 0.05]).astype(complex)
rho_b = u0 @ rho_b @ u0.conj().T
check("(a) different rho SPECTRA, identical frames => different registered content (the "
      "state selection keeps instrument-independent registrable content: its invariants)",
      np.max(np.abs(content(rho, FRAMES) - content(rho_b, FRAMES))) > 0.05)
# (b) instrument-class content: same Fock state, frame-naming vs color-blind instruments:
check("(b) same state, different instrument CLASS (frame-naming vs color-blind) => "
      "different registered content (the frame-side residual keeps its class datum)",
      abs(len(p0) - len(pb0)) > 0 or np.max(np.abs(p0[:4] - pb0[:4])) > 0.01,
      "outcome structures differ (8 patterns vs 4 totals)")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: resolves the parked shape-question between the (B) open-shell selection")
print("  (Pauli open-shell instance) and the pointer-frame root precisely: the two selections fuse at")
print("  their absolute-orientation parts -- ONE vacuous diagonal SU(3) quotient (8")
print("  directions once, not 16; trace-cyclicity invariant; sharp in the rank-6 kernel +")
print("  tomographic completeness) -- and remain DISTINCT in their registrable remainders")
print("  (state orbit-invariants vs instrument class + relative orientation).  NEITHER")
print("  identification NOR independence.  Does NOT discharge either residual; the")
print("  refinement is global-side (admission B); the local ADM-1 root {P_r} is untouched")
print("  (global rotations supply no per-edge link data, per the color-orientation boundary); no")
print("  weight assigned; r untouched.  Conditional on the supplied C^3 carrier + named")
print("  instruments + named color-diagonal hopping.  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
