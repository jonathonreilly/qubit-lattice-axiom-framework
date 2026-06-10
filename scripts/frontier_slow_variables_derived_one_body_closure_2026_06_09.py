#!/usr/bin/env python3
"""The 'added slow variables' premise retires: the closing variable set is DERIVED.

Class-A exact verification for the source note

    docs/SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09.md

CONTEXT (retire-mode follow-on to the gauge-dynamics campaign).  The induced
composite-link trajectory note exhibited the induced composite link's NON-AUTONOMY
(two states, same U_eff, different dU_eff/dt) and the lever-space map listed
"added slow variables" as a promotion route REQUIRING a new premise.  This note
retires that premise: NO slow-variable
admission is needed, because the closing variable set is already DERIVED.

THESIS (exact; conditional on the named quadratic generator):
  (T1) OPERATOR-LEVEL CLOSURE.  For the named quadratic hopping generator (
       H = sum h_ij a_i^dag a_j, h Hermitian), the Heisenberg flow of the one-body
       bilinears CLOSES on itself: a_i^dag a_j (t) stays in the span of {a_k^dag a_l}
       exactly, for ALL states (state-independent), with G(t) = U_t G U_t^dag,
       U_t = exp(-i h^T t)... (convention fixed in the runner).  The "slow variables"
       are the rest of the one-body density G -- forced by the quadratic structure,
       not chosen.
  (T2) RECORD CHANNELS PRESERVE THE CLOSURE.  The campaign's two named instruments
       (I-A occupation dephasing, I-B site-pinching Lueders) act on G by EXACT linear
       one-body rules (re-verified here on NON-Gaussian Fock states) -- so the
       interleaved (Hamiltonian + record) flow is closed at the G level.
  (T3) THE LINK IS A COORDINATE.  U_eff = polar(G_xy) is a nonlinear coordinate of the
       closed object G; the induced-trajectory note's non-autonomy exhibit is
       COORDINATE non-autonomy: the same closed G-flow, read through a lossy
       coordinate.  The Sylvester increment law is re-derived FROM the G-flow.
  (T4) TEETH.  A quartic (non-quadratic) interaction term BREAKS the closure (dG/dt
       acquires two-body terms): the closure is a derived property of the RETAINED
       quadratic hopping, not generic.

WHAT THIS RETIRES / WHAT IT DOES NOT:
  - DISCHARGES the CHOSEN-ENLARGEMENT form of the route-(i) premise (as a source
    proposal; the audit lane grades): no slow-variable CHOICE is needed -- the closing set
    is DERIVED (the full one-body G; strictly larger than the registered (U,Q)~M, which
    does NOT close on its own).  The link acquires NO autonomous law.
  - Does NOT close the campaign's record-level reduction (the pointer-frame admission
    {P_r} stands -- the stratification theorem is untouched); does NOT cover
    interacting/non-quadratic matter (T4 shows exactly why); conditional on the named
    quadratic generator (the realization gate for "the physical dynamics IS this H" is
    a separate lane) and the supplied C^3 color carrier.

Run: python3 scripts/frontier_slow_variables_derived_one_body_closure_2026_06_09.py
"""

from __future__ import annotations

import itertools
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


rng = np.random.default_rng(20260609)

# ---------------------------------------------------------------------------
# Small exact Fock machinery (n modes, dim 2^n) -- memory-safe at n = 6.
# ---------------------------------------------------------------------------
N_MODES = 6   # 2 sites x 3 colors
DIM = 2 ** N_MODES


def annihilator(j, n=N_MODES):
    """Jordan-Wigner a_j on 2^n Fock space (exact)."""
    sz = np.array([[1, 0], [0, -1]], float)
    sm = np.array([[0, 1], [0, 0]], float)   # lowers occupation: |1> -> |0>
    ops = [sz] * j + [sm] + [np.eye(2)] * (n - j - 1)
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


A = [annihilator(j) for j in range(N_MODES)]
AD = [a.T.conj() for a in A]


def quadratic_H(h):
    return sum(h[i, j] * AD[i] @ A[j] for i in range(N_MODES) for j in range(N_MODES))


def one_body_G(psi):
    return np.array([[psi.conj() @ (AD[i] @ A[j]) @ psi for j in range(N_MODES)]
                     for i in range(N_MODES)])


h = rng.normal(size=(N_MODES, N_MODES)) + 1j * rng.normal(size=(N_MODES, N_MODES))
h = (h + h.conj().T) / 2
H = quadratic_H(h)

# ---------------------------------------------------------------------------
# Part 1.  (T1) Operator-level closure: a_i^dag a_j (t) stays in the bilinear span.
#   Heisenberg: a_j(t) = sum_k (e^{-i h t})_{jk}^* ... fix convention numerically:
#   verify e^{iHt} a_i^dag a_j e^{-iHt} == sum_{kl} W*_{ki} W_{lj} a_k^dag a_l ... derive W.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 1  (T1) operator-level closure of the one-body bilinears (state-independent)")
print("=" * 78)

t = 0.37
Ut_fock = expm(1j * H * t)          # Heisenberg conjugation operator
W = expm(-1j * h * t)               # single-particle propagator candidate

worst = 0.0
pairs = [(0, 0), (0, 3), (2, 5), (4, 1)]
for (i, j) in pairs:
    lhs = Ut_fock @ (AD[i] @ A[j]) @ Ut_fock.conj().T
    # da_j/dt = i[H,a_j] = -i sum_l h_jl a_l  =>  a_j(t) = sum_l W_jl a_l, W = e^{-iht}
    rhs = sum(W.conj()[i, k] * W[j, l] * (AD[k] @ A[l])
              for k in range(N_MODES) for l in range(N_MODES))
    worst = max(worst, float(np.max(np.abs(lhs - rhs))))
check("Heisenberg flow of a_i^dag a_j stays EXACTLY in the bilinear span "
      "(4 representative pairs, full 64-dim Fock space)",
      worst < 1e-10, f"max dev {worst:.1e} -- closure is operator-level, state-independent")

# state-level corollary: G(t) = W^dag... verify on a NON-Gaussian state
psi_ng = rng.normal(size=DIM) + 1j * rng.normal(size=DIM)
psi_ng /= np.linalg.norm(psi_ng)
psi_t = expm(-1j * H * t) @ psi_ng
G0 = one_body_G(psi_ng)
Gt = one_body_G(psi_t)
Gt_pred = W.conj() @ G0 @ W.T          # the DERIVED convention: G(t) = conj(W) G W^T
check("G(t) = conj(W) G(0) W^T on a NON-GAUSSIAN state (the derived convention; exact)",
      np.allclose(Gt_pred, Gt, atol=1e-9),
      f"max dev {np.max(np.abs(Gt_pred - Gt)):.1e}")

# ---------------------------------------------------------------------------
# Part 2.  (T2) The named record channels act on G by exact one-body rules
#   (re-verified on non-Gaussian states; the campaign's I-A and I-B).
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 2  (T2) record channels preserve the closure (exact one-body rules, non-Gaussian)")
print("=" * 78)

lam = 0.6
NUM = [AD[j] @ A[j] for j in range(N_MODES)]


def apply_IA(rho):
    """I-A: occupation-basis dephasing of strength lam on every mode (named frame)."""
    out = (1 - lam) * rho
    # full dephasing component: project onto occupation basis (diagonal in Fock basis)
    out += lam * np.diag(np.diag(rho))
    return out


rho_ng = np.outer(psi_ng, psi_ng.conj())
rho_IA = apply_IA(rho_ng)
G_IA = np.array([[np.trace(rho_IA @ (AD[i] @ A[j])) for j in range(N_MODES)]
                 for i in range(N_MODES)])
# exact one-body rule for full-mode occupation dephasing: off-diagonal G entries damp
# by (1-lam), diagonal preserved (i != j entries of a^dag_i a_j are off-diagonal in the
# occupation basis -> damped; i == j entries are diagonal -> preserved).
G_rule = (1 - lam) * G0 + lam * np.diag(np.diag(G0))
check("I-A (occupation dephasing): G -> (1-lam) G + lam diag(G) EXACTLY on a "
      "non-Gaussian state (the closure survives the record step)",
      np.allclose(G_IA, G_rule, atol=1e-10),
      f"max dev {np.max(np.abs(G_IA - G_rule)):.1e}")
print("   (I-B site-pinching Lueders: same structure; exact one-body rules established in")
print("    the record-instrument source note with Fock-anchored checks to 6e-17 -- cited,")
print("    not re-proven.)")

# ---------------------------------------------------------------------------
# Part 3.  (T3) The link is a COORDINATE of the closed flow; the induced-trajectory
#   note's Sylvester law is re-derived FROM the G-flow; the non-autonomy is coordinate
#   non-autonomy.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 3  (T3) U_eff = polar(G_xy): a nonlinear coordinate; Sylvester law re-derived")
print("=" * 78)


def polar_u(M):
    w, V = np.linalg.eigh(M.conj().T @ M)
    return M @ V @ np.diag(w ** -0.5) @ V.conj().T


# Slater state with K=3 occupied modes -> rank-3 G_xy generically
K = 3
PSI_orb = np.linalg.qr(rng.normal(size=(N_MODES, K)) + 1j * rng.normal(size=(N_MODES, K)))[0]
G_sl = PSI_orb @ PSI_orb.conj().T
Gxy = G_sl[:3, 3:]
check("K=3 Slater: the cross block G_xy is full-rank (the PR #3398 precondition)",
      np.linalg.matrix_rank(Gxy) == 3)

# The TRUE derived G-flow (from T1's operator law, h Hermitian):
#   G(t) = conj(W) G W^T = e^{+i h^T t} G e^{-i h^T t}   =>   dG/dt = i [h^T, G].
# (The state-level check in Part 1 uses exactly this derived convention.)
Gdot_true = 1j * (h.T @ G_sl - G_sl @ h.T)
Mdot = Gdot_true[:3, 3:]
U = polar_u(Gxy)
w, V = np.linalg.eigh(Gxy.conj().T @ Gxy)
Qm = V @ np.diag(np.sqrt(w)) @ V.conj().T          # Q = (M^dag M)^{1/2}
# Sylvester: Omega Q + Q Omega = U^dag Mdot - Mdot^dag U.
RHS = U.conj().T @ Mdot - Mdot.conj().T @ U
ww, VV = np.linalg.eigh(Qm)
Omega = VV @ ((VV.conj().T @ RHS @ VV) / (ww[:, None] + ww[None, :])) @ VV.conj().T
# REVIEWER-HARDENED: the finite difference uses the ACTUAL evolution (the exact
# one-parameter propagation of G), NOT a hand-written Gdot — so the check would FAIL
# for a wrong generator (the prior draft's check was generator-circular and is replaced).
ds = 1e-6
G_ds = expm(1j * h.T * ds) @ G_sl @ expm(-1j * h.T * ds)
dU_fd = (polar_u(G_ds[:3, 3:]) - U) / ds
dU_syl = U @ Omega
check("the induced-trajectory Sylvester law evaluated ON THE TRUE G-flow generator: dU_eff/dt = "
      "U*Omega matches the finite difference of the ACTUAL evolution",
      np.allclose(dU_fd, dU_syl, atol=1e-4),
      f"max dev {np.max(np.abs(dU_fd - dU_syl)):.1e}")
# control (teeth on the check itself): a WRONG generator must FAIL this test
G_ds_wrong = expm(-1j * h.T * ds) @ G_sl @ expm(1j * h.T * ds)    # reversed arrow
dU_fd_wrong = (polar_u(G_ds_wrong[:3, 3:]) - U) / ds
check("CONTROL: a wrong generator (reversed arrow) FAILS the same test (the check has "
      "discriminating power; not generator-circular)",
      not np.allclose(dU_fd_wrong, dU_syl, atol=1e-4),
      f"wrong-generator dev {np.max(np.abs(dU_fd_wrong - dU_syl)):.1e}")
# REVIEWER-ADDED positive content: the registered route premise was the CROSS-BLOCK pair
# (U, Q) ~ M = G_xy alone.  That set does NOT close: dG_xy depends on the DIAGONAL blocks.
# Exhibit: two G's with the SAME cross block but different diagonal blocks give different
# dG_xy under the same flow.
G_alt = G_sl.copy()
D_extra = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
D_extra = (D_extra + D_extra.conj().T) / 2
G_alt[:3, :3] = G_alt[:3, :3] + 0.3 * D_extra      # change a diagonal block only
dMxy_1 = (1j * (h.T @ G_sl - G_sl @ h.T))[:3, 3:]
dMxy_2 = (1j * (h.T @ G_alt - G_alt @ h.T))[:3, 3:]
check("the cross-block (U,Q)~M alone does NOT close: same G_xy, different diagonal "
      "blocks => different dG_xy (the registered route's chosen set is insufficient; "
      "only the FULL one-body G closes)",
      np.allclose(G_alt[:3, 3:], G_sl[:3, 3:]) and not np.allclose(dMxy_1, dMxy_2, atol=1e-6),
      f"dG_xy difference {np.max(np.abs(dMxy_1 - dMxy_2)):.3f}")
print("   => the induced-trajectory non-autonomy = COORDINATE non-autonomy:")
print("      U_eff (and even (U,Q))")
print("      discards G data that the closed derived flow carries; the link acquires NO")
print("      autonomous law (consistent with the campaign's vacuous-link-generator result).")

# ---------------------------------------------------------------------------
# Part 4.  (T4) Teeth: a quartic interaction BREAKS the closure.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 4  (T4) teeth: a non-quadratic (quartic) term breaks the one-body closure")
print("=" * 78)

H_int = H + 0.8 * (NUM[0] @ NUM[3])     # density-density interaction
Ut_int = expm(1j * H_int * t)
lhs = Ut_int @ (AD[0] @ A[3]) @ Ut_int.conj().T
# best bilinear approximation: project onto the bilinear span and measure the residual
basis = [AD[i] @ A[j] for i in range(N_MODES) for j in range(N_MODES)] + [np.eye(DIM)]
Bmat = np.array([b.flatten() for b in basis]).T
coef, *_ = np.linalg.lstsq(Bmat, lhs.flatten(), rcond=None)
resid = np.linalg.norm(Bmat @ coef - lhs.flatten())
check("with a quartic term, a_0^dag a_3 (t) LEAVES the bilinear span (closure broken: "
      "residual O(1)) -- the closure is a property of the named quadratic hopping",
      resid > 0.1, f"projection residual {resid:.3f}")

# ---------------------------------------------------------------------------
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE (retire-mode): the route-(i) 'added slow variables' promotion premise is")
print("  retired as a source proposal -- the closing variable set is DERIVED, not admitted:")
print("  the one-body bilinear algebra closes under the named quadratic hopping at the")
print("  OPERATOR level (state-independent), the campaign's record channels act by exact")
print("  one-body rules (closure survives), and the composite link is a nonlinear lossy")
print("  COORDINATE of this closed flow (the induced-trajectory Sylvester law is")
print("  re-derived from it; its non-autonomy = coordinate non-autonomy).  A quartic")
print("  term breaks the closure --")
print("  the result is conditional on the named quadratic generator (realization gate a")
print("  separate lane) + the supplied C^3 carrier.  Does NOT touch the pointer-frame")
print("  admission {P_r} or the stratification theorem; the audit lane grades status.")
if FAIL:
    raise SystemExit(1)
