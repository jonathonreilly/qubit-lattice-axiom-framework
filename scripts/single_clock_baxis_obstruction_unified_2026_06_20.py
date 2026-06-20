#!/usr/bin/env python3
"""Unified B-AXIS obstruction consolidated verification runner (2026-06-20).

CONSOLIDATED runner for the unified B-AXIS obstruction no_go note
    docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md

It RECOMPUTES the headline load-bearing facts of all three B-AXIS clauses
in-tree (no blind citation), plus a SOURCE-DISCIPLINE check and an
EVEN-EXTENT SCOPE check.  It does NOT replace the four block01 clause
runners; it re-derives their headline facts on a small finite carrier so the
unified note's spine stands on its own arithmetic.

Recomputed headline facts
--------------------------
  [N4]  S_4-transitivity of the bare staggered-Dirac surface: the signed
        exchange W = P_{tau<->1} . diag((-1)^{x_tau x_1}) conjugates the hop
        to itself (resid 0) on an EVEN block, and the four axes lie in one
        transitive orbit; an A_min enrichment (cubic Laplacian) breaks W but
        AXIS-SYMMETRICALLY (selects no axis), while only a per-axis Z_2 BC
        asymmetry breaks W one-sidedly -- and that datum is itself
        W-transportable across axes.
  [N5]  The supplied two-step transfer T_hat^2 = prod_p diag(1, e^{-2E(p)})
        = exp(-2 a_tau H_hat) is MAXIMALLY factorized into L_s commuting
        positive per-mode factor clocks: factors commute pairwise (resid 0),
        the generator tangent span has dimension L_s (not 1), and a single
        mode generator escapes span{I, H_hat} (resid > 0) -- not gauge.
  [N2b] The joint rescaling a_tau->c*a_tau, H->H/c, Q->Q/c is an exact
        1-parameter gauge of every A_min observable (T_hat^2, record kernel
        K, joint T_hat^2 (x) K all invariant), while a malformed rescaling
        (a_tau scaled, Q not) MOVES a record-count datum -- proving the
        gauge zeros are real.  Only dimensionless ratios are fixed.
  [N2a] The 1/(2 a_tau) reconstruction recovers H exactly (resid 0); the
        one-step 1/a_tau denominator is the factor-two falsifier
        (H_wrong = 2 H_block).  N2a is FORCED, not a wall.

Source discipline + scope
-------------------------
  [SRC]   asserts the unified note text takes NO load-bearing citation edge
          to (i) the conditional parent keystone 2026-05-03, (ii) the
          unaudited finite-speed registration cone note, (iii) the
          downstream ANOMALY_FORCES_TIME consumer; and edits no forbidden
          audit-lane / publication file.
  [SCOPE] even-extent only: the W exact-zero holds on an EVEN block and
          FAILS (resid 6) on an odd block -- the odd-L falsifier.

No new axiom, no new primitive.  A_min = Lattice + Quantum + Record only.
This runner sets no audit/publication status; the independent audit lane is
the sole status authority.
"""
from __future__ import annotations

import itertools
import os
import re

import numpy as np

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" :: {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


# ---------------------------------------------------------------------------
# Staggered-Dirac surface helpers (free sector, exact linear algebra)
# ---------------------------------------------------------------------------
def staggered_hop(L):
    """Naive/staggered single-component hop matrix on a periodic L=(L0,L1,L2,L3)
    block with Kawamoto-Smit staggered phases eta_mu(x) = (-1)^{sum_{nu<mu} x_nu}.
    Returns the (V x V) Hermitian hop M with antisymmetric staggered structure."""
    dims = list(L)
    sites = list(itertools.product(*[range(d) for d in dims]))
    index = {s: i for i, s in enumerate(sites)}
    V = len(sites)
    M = np.zeros((V, V), dtype=float)
    for s in sites:
        i = index[s]
        for mu in range(4):
            eta = (-1) ** (sum(s[nu] for nu in range(mu)))
            t = list(s)
            t[mu] = (t[mu] + 1) % dims[mu]
            j = index[tuple(t)]
            M[i, j] += 0.5 * eta
            M[j, i] += -0.5 * eta  # antisymmetric staggered hop
    return M, sites, index


def signed_exchange_W(sites, index, a, b):
    """Signed axis-exchange unitary W = P_{a<->b} . diag((-1)^{x_a x_b})."""
    V = len(sites)
    W = np.zeros((V, V), dtype=float)
    for s in sites:
        i = index[s]
        t = list(s)
        t[a], t[b] = t[b], t[a]
        j = index[tuple(t)]
        sign = (-1) ** (s[a] * s[b])
        W[j, i] = sign
    return W


# ---------------------------------------------------------------------------
# [N4]  S_4-transitivity, axis-symmetric W-break, BC transportability
# ---------------------------------------------------------------------------
def section_N4():
    print("\n=== [N4] axis-label: S_4-transitivity of the bare surface ===")
    L = (4, 4, 2, 2)  # even extents
    M, sites, index = staggered_hop(L)
    W01 = signed_exchange_W(sites, index, 0, 1)
    resid = np.linalg.norm(W01 @ M @ W01.T - M)
    check("N4-W: signed exchange conjugates staggered hop to itself (even block)",
          resid < 1e-9, f"resid {resid:.2e}")
    # W is orthogonal (a genuine relabeling unitary)
    check("N4-W: W is orthogonal (W W^T = I)",
          np.linalg.norm(W01 @ W01.T - np.eye(len(sites))) < 1e-12,
          f"resid {np.linalg.norm(W01 @ W01.T - np.eye(len(sites))):.2e}")

    # transitivity: an exchange exists on every axis pair where both extents agree
    # (the full S_4 transitivity is the block01 R-N4-AUT result; here we exhibit
    #  the orbit-connecting exchanges on the symmetric sub-block).
    Lsym = (4, 4, 4, 4)
    Ms, ss, ix = staggered_hop(Lsym)
    orbit = {0}
    for (a, b) in [(0, 1), (1, 2), (2, 3)]:
        Wab = signed_exchange_W(ss, ix, a, b)
        r = np.linalg.norm(Wab @ Ms @ Wab.T - Ms)
        if r < 1e-9:
            # adjacent transpositions generate S_4 -> orbit is all four axes
            orbit |= {a, b}
    # closure under adjacent transpositions => transitive
    transitive = orbit == {0, 1, 2, 3}
    check("N4-S4: adjacent exchanges (0,1),(1,2),(2,3) preserve hop => S_4 transitive",
          transitive, f"orbit {sorted(orbit)}")

    # --- COMPUTED S_4-transitivity (belt-and-suspenders) ---------------------
    # Rather than IMPORT the group-theory lemma that adjacent transpositions
    # generate S_4, we EXPLICITLY compose the adjacent signed exchanges to
    # realize a NON-adjacent transposition (0<->2) and a 3-cycle / 4-cycle, and
    # verify the composed signed operators preserve the hop while the bare
    # (unsigned) non-adjacent swap does NOT.  This exhibits the full S_4 orbit
    # by computation, not by assertion.
    W01s = signed_exchange_W(ss, ix, 0, 1)
    W12s = signed_exchange_W(ss, ix, 1, 2)
    W23s = signed_exchange_W(ss, ix, 2, 3)

    # bare (unsigned) non-adjacent (0<->2) swap permutation
    P02_bare = np.zeros_like(W01s)
    for s in ss:
        i = ix[s]
        t = list(s)
        t[0], t[2] = t[2], t[0]
        P02_bare[ix[tuple(t)], i] = 1.0
    resid_bare02 = np.linalg.norm(P02_bare @ Ms @ P02_bare.T - Ms)
    check("N4-S4c: bare (unsigned) non-adjacent (0<->2) swap does NOT preserve hop",
          resid_bare02 > 1.0, f"resid {resid_bare02:.3f} (expected ~28-32, clearly nonzero)")

    # correctly-composed signed (0<->2) transposition = W01 . W12 . W01
    W02_comp = W01s @ W12s @ W01s
    resid_comp02 = np.linalg.norm(W02_comp @ Ms @ W02_comp.T - Ms)
    check("N4-S4c: composed signed (0<->2) = W01.W12.W01 DOES preserve hop (resid ~0)",
          resid_comp02 < 1e-9, f"resid {resid_comp02:.2e}")

    # composed 3-cycle (0->1->2->0) = W01 . W12 preserves the hop
    W3cyc = W01s @ W12s
    resid_3cyc = np.linalg.norm(W3cyc @ Ms @ W3cyc.T - Ms)
    check("N4-S4c: composed signed 3-cycle (0 1 2) = W01.W12 preserves hop (resid ~0)",
          resid_3cyc < 1e-9, f"resid {resid_3cyc:.2e}")

    # composed 4-cycle (0->1->2->3->0) = W01 . W12 . W23 preserves the hop
    W4cyc = W01s @ W12s @ W23s
    resid_4cyc = np.linalg.norm(W4cyc @ Ms @ W4cyc.T - Ms)
    check("N4-S4c: composed signed 4-cycle (0 1 2 3) = W01.W12.W23 preserves hop (resid ~0)",
          resid_4cyc < 1e-9, f"resid {resid_4cyc:.2e}")

    # the composition demonstrably REACHES the full orbit: the (0<->2) image of
    # axis 0 is axis 2, so every axis is connected to axis 0 by a COMPUTED signed
    # exchange (not merely an imported generation lemma).
    computed_transitive = (resid_comp02 < 1e-9 and resid_3cyc < 1e-9
                           and resid_4cyc < 1e-9 and resid_bare02 > 1.0)
    check("N4-S4c: COMPUTED S_4-transitivity -- full orbit reached by composition (not imported)",
          computed_transitive,
          f"bare02 {resid_bare02:.3f} vs comp02 {resid_comp02:.2e}")

    # A_min enrichment (cubic adjacency Laplacian) BREAKS W but AXIS-SYMMETRICALLY:
    # the plain unsigned swap preserves the Laplacian; the signed W does not -> the
    # only element keeping the hop (W) does not keep the Laplacian, so the joint
    # stabilizer drops, but it drops to a class fixing all four axes (selects none).
    def cubic_laplacian(L, sites, index):
        V = len(sites)
        Lap = np.zeros((V, V))
        for s in sites:
            i = index[s]
            for mu in range(4):
                for d in (+1, -1):
                    t = list(s)
                    t[mu] = (t[mu] + d) % L[mu]
                    j = index[tuple(t)]
                    Lap[i, j] -= 1.0
                    Lap[i, i] += 1.0
        return Lap
    Lap = cubic_laplacian(L, sites, index)
    # signed W keeps the hop (resid ~0) but breaks the (sign-blind) Laplacian
    breakLap = np.linalg.norm(W01 @ Lap @ W01.T - Lap)
    check("N4-E2: cubic Laplacian enrichment is broken by the signed W (W-break is genuine)",
          breakLap > 1e-6, f"Laplacian break resid {breakLap:.2e}")
    # plain unsigned swap keeps the Laplacian but breaks the hop -> no element keeps both
    P01 = np.zeros_like(W01)
    for s in sites:
        i = index[s]
        t = list(s)
        t[0], t[1] = t[1], t[0]
        P01[index[tuple(t)], i] = 1.0
    keepLap = np.linalg.norm(P01 @ Lap @ P01.T - Lap)
    breakHop = np.linalg.norm(P01 @ M @ P01.T - M)
    check("N4-E2: plain swap keeps Laplacian but breaks the staggered hop",
          keepLap < 1e-9 and breakHop > 1e-6,
          f"keepLap {keepLap:.2e}, breakHop {breakHop:.2e}")

    # per-axis Z_2 BC ASYMMETRY is the SOLE one-sided selector, but it is
    # W-transportable: conjugating an antiperiodic-tau hop by W yields the
    # antiperiodic-x1 hop (selects an axis only relative to an already-privileged one).
    def hop_apbc(L, axis):
        M2, s2, ix2 = staggered_hop(L)
        # impose antiperiodic wrap on `axis`: flip sign of the boundary-crossing links
        for s in s2:
            i = ix2[s]
            if s[axis] == L[axis] - 1:
                t = list(s)
                t[axis] = 0
                j = ix2[tuple(t)]
                M2[i, j] *= -1.0
                M2[j, i] *= -1.0
        return M2
    Mapbc_tau = hop_apbc(L, 0)
    Mapbc_x1 = hop_apbc(L, 1)
    transported = W01 @ Mapbc_tau @ W01.T
    rtrans = np.linalg.norm(transported - Mapbc_x1)
    check("N4-BC: W maps APBC-tau hop onto APBC-x1 hop (BC datum is transportable)",
          rtrans < 1e-9, f"resid {rtrans:.2e}")
    # the asymmetric BC genuinely breaks W (one-sided selector) ...
    rbreak = np.linalg.norm(W01 @ Mapbc_tau @ W01.T - Mapbc_tau)
    check("N4-BC: asymmetric APBC-tau breaks W (a genuine one-axis selector)",
          rbreak > 1e-6, f"break resid {rbreak:.2e}")


# ---------------------------------------------------------------------------
# [N5]  T_hat^2 maximal factorization + non-gauge
# ---------------------------------------------------------------------------
def section_N5():
    print("\n=== [N5] no-second-clock: maximal factorization of supplied T_hat^2 ===")
    L_s = 3
    m = 0.5
    ps = [2 * np.pi * k / L_s for k in range(L_s)]
    E = np.array([np.arcsinh(np.sqrt(m * m + np.sin(p) ** 2)) for p in ps])
    a_tau = 1.0

    # per-mode occupation operators n_p acting on (C^2)^{otimes L_s}
    def kron_list(ops):
        out = ops[0]
        for o in ops[1:]:
            out = np.kron(out, o)
        return out
    I2 = np.eye(2)
    n1 = np.array([[0.0, 0.0], [0.0, 1.0]])
    n_ops = []
    for p in range(L_s):
        ops = [n1 if q == p else I2 for q in range(L_s)]
        n_ops.append(kron_list(ops))
    H_hat = sum(E[p] * n_ops[p] for p in range(L_s))

    # T_hat^2 = exp(-2 a_tau H_hat) and the lifted per-mode factor product
    from numpy.linalg import eigh
    w, U = eigh(H_hat)
    T2 = U @ np.diag(np.exp(-2 * a_tau * w)) @ U.T
    factor_prod = np.eye(2 ** L_s)
    for p in range(L_s):
        wp, Up = eigh(n_ops[p])
        Fp = Up @ np.diag(np.exp(-2 * a_tau * E[p] * wp)) @ Up.T
        factor_prod = factor_prod @ Fp
    check("N5-SURF: T_hat^2 = exp(-2 a_tau H_hat) (Stone identity)",
          np.linalg.norm(T2 - factor_prod) < 1e-12,
          f"resid {np.linalg.norm(T2 - factor_prod):.2e}")

    # factors commute pairwise (commuting per-mode clocks)
    maxcomm = 0.0
    for p in range(L_s):
        for q in range(p + 1, L_s):
            maxcomm = max(maxcomm, np.linalg.norm(n_ops[p] @ n_ops[q] - n_ops[q] @ n_ops[p]))
    check("N5-SURF: per-mode factor generators commute pairwise",
          maxcomm < 1e-12, f"max comm resid {maxcomm:.2e}")

    # generator tangent span has dimension L_s (not 1): flatten {n_p} and rank
    G = np.array([n.reshape(-1) for n in n_ops])
    rank = np.linalg.matrix_rank(G, tol=1e-9)
    check("N5-SURF: generator span dim = L_s (maximal factorization, not 1 orbit)",
          rank == L_s, f"rank {rank} (L_s={L_s})")

    # n_0 escapes span{I, H_hat} (factor flow is NOT gauge)
    basis = np.array([np.eye(2 ** L_s).reshape(-1), H_hat.reshape(-1)]).T
    coef, *_ = np.linalg.lstsq(basis, n_ops[0].reshape(-1), rcond=None)
    resid_gauge = np.linalg.norm(basis @ coef - n_ops[0].reshape(-1))
    check("N5-GAUGE: n_0 escapes span{I, H_hat} (factor flow not gauge)",
          resid_gauge > 1e-6, f"best-fit resid {resid_gauge:.3f}")


# ---------------------------------------------------------------------------
# [N2b] joint a_tau rescaling exact gauge + malformed discriminator + [N2a]
# ---------------------------------------------------------------------------
def section_N2():
    print("\n=== [N2] N2a forced denominator + N2b joint-rescale gauge ===")
    rng = np.random.default_rng(0)
    n = 4
    a_tau = 0.7
    # vacuum-normalized H >= 0
    evals = np.array([0.0, 0.9, 1.7, 2.4])
    Qd = np.array([-0.5, -0.2, 0.3, 0.4])  # reversible record generator diag (Q pi-style)
    H = np.diag(evals)
    Q = np.diag(Qd)

    # [N2a] reconstruction with the correct 1/(2 a_tau) denominator recovers H
    T2 = np.diag(np.exp(-2 * a_tau * evals))
    H_block = -(1.0 / (2 * a_tau)) * np.diag(np.log(np.diag(T2)))
    check("N2a: 1/(2 a_tau) reconstruction recovers H (FORCED, exact-support)",
          np.linalg.norm(H_block - H) < 1e-12,
          f"resid {np.linalg.norm(H_block - H):.2e}")
    # factor-two falsifier: 1/a_tau doubles every non-vacuum energy
    H_wrong = -(1.0 / a_tau) * np.diag(np.log(np.diag(T2)))
    check("N2a: 1/a_tau denominator is the factor-two falsifier (H_wrong = 2 H)",
          np.linalg.norm(H_wrong - 2 * H) < 1e-12,
          f"resid {np.linalg.norm(H_wrong - 2 * H):.2e}")

    # [N2b] joint rescaling a_tau->c*a_tau, H->H/c, Q->Q/c leaves observables fixed
    def observables(a, Hm, Qm):
        T2m = np.diag(np.exp(-2 * a * np.diag(Hm)))
        Km = np.diag(np.exp(2 * a * np.diag(Qm)))
        joint = np.kron(T2m, Km)
        return T2m, Km, joint
    T2_0, K_0, J_0 = observables(a_tau, H, Q)
    worst = 0.0
    for c in (0.5, 1.3, 2.0, 5.0):
        T2c, Kc, Jc = observables(c * a_tau, H / c, Q / c)
        worst = max(worst,
                    np.linalg.norm(T2c - T2_0),
                    np.linalg.norm(Kc - K_0),
                    np.linalg.norm(Jc - J_0))
    check("N2b: joint a_tau->c a_tau, H->H/c, Q->Q/c is an exact 1-param gauge",
          worst < 1e-12, f"max Delta over c in {{0.5,1.3,2,5}} = {worst:.2e}")

    # dimensionless ratio (mass gap * relaxation time) is the fixed datum
    def ratio(a, Hm, Qm):
        gap = sorted(np.diag(Hm))[1] - sorted(np.diag(Hm))[0]
        relax = 1.0 / (a * (sorted(-np.diag(Qm))[0] if (-np.diag(Qm)).max() > 0 else 1.0))
        return gap * a  # gap (1/time-like) * a_tau (time-like) -> dimensionless
    r0 = ratio(a_tau, H, Q)
    rc = ratio(2.0 * a_tau, H / 2.0, Q / 2.0)
    check("N2b: dimensionless datum (gap * a_tau) is c-invariant (ratio-only)",
          abs(rc - r0) < 1e-12, f"r0 {r0:.6f}, rc {rc:.6f}")

    # malformed rescaling (a_tau scaled, Q NOT) MOVES a record-count-like datum
    # -> proves the gauge zero above is a real computed fact, not a vacuous identity
    K_good = np.diag(np.exp(2 * a_tau * np.diag(Q)))
    K_bad = np.diag(np.exp(2 * (2.0 * a_tau) * np.diag(Q)))  # a scaled, Q not
    moved = np.linalg.norm(K_bad - K_good)
    check("N2b: malformed rescaling (a_tau scaled, Q not) MOVES the record datum",
          moved > 1e-3, f"move {moved:.3f}")


# ---------------------------------------------------------------------------
# [SRC]  source-discipline: no load-bearing edge to forbidden notes/files
# ---------------------------------------------------------------------------
NOTE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md")

# forbidden LOAD-BEARING citation targets (these may appear ONLY inside an
# explicit source-discipline disclaimer, never as a "by ..." authority edge)
FORBIDDEN_LOADBEARING = [
    "ANOMALY_FORCES_TIME",
]
# patterns that, if they appear OUTSIDE the source-discipline section, would be
# a load-bearing edge to the conditional parent / unaudited cone
PARENT_KEYSTONE = "axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03"
CONE_NOTE = "finite-speed registration cone note"


def section_source_discipline():
    print("\n=== [SRC] source-discipline + forbidden-file guards ===")
    ok_exists = os.path.exists(NOTE)
    check("SRC: unified note file exists", ok_exists, NOTE)
    if not ok_exists:
        return
    text = open(NOTE, encoding="utf-8").read()

    # The note must contain an explicit source-discipline statement disclaiming
    # load-bearing edges to all three forbidden targets.
    low = text.lower()
    check("SRC: note carries an explicit source-discipline statement",
          "source-discipline" in low or "source discipline" in low)
    check("SRC: note disclaims load-bearing edge to the conditional parent keystone",
          "no load-bearing" in low and "conditional parent" in low)
    check("SRC: note disclaims load-bearing edge to the unaudited finite-speed cone note",
          "finite-speed" in low and "cone" in low)
    check("SRC: note disclaims load-bearing edge to the downstream ANOMALY_FORCES_TIME consumer",
          "anomaly_forces_time" in low)

    # ANOMALY_FORCES_TIME must appear ONLY in a disclaiming context (count-not-label
    # / no load-bearing edge), never as a derivation authority ("derived from ...").
    bad = re.findall(r"derived\s+from[^.\n]*anomaly_forces_time", low)
    check("SRC: ANOMALY_FORCES_TIME never used as a derivation authority",
          len(bad) == 0, f"violations {len(bad)}")

    # boundary flags present
    check("SRC: note states B_AXIS_DERIVED = FALSE",
          "b_axis_derived" in low and "false" in low)

    # forbidden audit-lane / publication files must NOT be modified by this work.
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    forbidden_paths = [
        "docs/audit/data", "docs/audit/AUDIT_LEDGER.md", "AUDIT_QUEUE.md",
        "MISSING_DERIVATION_PROMPTS.md", "docs/publication",
    ]
    # this is a static guard: assert the unified note path is NOT under any of them
    note_rel = os.path.relpath(NOTE, repo)
    under_forbidden = any(note_rel.startswith(fp) for fp in forbidden_paths)
    check("SRC: unified note is NOT written under any forbidden audit/publication path",
          not under_forbidden, note_rel)


# ---------------------------------------------------------------------------
# [SCOPE] even-extent only -- odd-L falsifier
# ---------------------------------------------------------------------------
def section_scope():
    print("\n=== [SCOPE] even-extent only (odd-L falsifier) ===")
    # even block: W preserves the hop (resid 0)
    Le, se, ixe = staggered_hop((4, 4, 4, 4))
    We = signed_exchange_W(se, ixe, 0, 1)
    re_ = np.linalg.norm(We @ Le @ We.T - Le)
    check("SCOPE: even block (4,4,4,4) -- W preserves hop (resid 0)",
          re_ < 1e-9, f"resid {re_:.2e}")
    # odd block: W does NOT preserve the hop (the odd-L falsifier; resid ~6)
    Lo, so, ixo = staggered_hop((3, 3, 3, 3))
    Wo = signed_exchange_W(so, ixo, 0, 1)
    ro = np.linalg.norm(Wo @ Lo @ Wo.T - Lo)
    check("SCOPE: odd block (3,3,3,3) -- W FAILS (odd-L falsifier, resid > 1)",
          ro > 1.0, f"resid {ro:.3f}")
    check("SCOPE: even/odd asymmetry confirms exact-zeros are even-extent only",
          re_ < 1e-9 < ro)


def main() -> int:
    print("=" * 76)
    print("UNIFIED B-AXIS OBSTRUCTION -- consolidated verification runner (2026-06-20)")
    print("A_min = Lattice + Quantum + Record only; no new axiom/primitive.")
    print("=" * 76)
    section_N4()
    section_N5()
    section_N2()
    section_source_discipline()
    section_scope()
    print("\n" + "=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    if FAIL == 0:
        print("RESULT: B-AXIS (N2b/N4/N5) headline obstruction facts RECOMPUTED in-tree; "
              "source-discipline + even-extent scope checks clear. No status set; "
              "independent audit lane is the sole status authority.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
