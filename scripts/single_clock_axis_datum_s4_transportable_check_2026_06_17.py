"""Single-clock axis selection: the per-axis antiperiodic-BC Z_2 datum is itself
S_4-transportable (companion runner of
SINGLE_CLOCK_ANTIPERIODIC_AXIS_DATUM_S4_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-06-17.md).

Context. The 2026-06-11 re-scope of
AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md
demoted evolution-axis selection to a declared evolution-axis premise because the
staggered surface is exactly invariant under the conjugated exchange
W = P_{tau<->1} . diag((-1)^{x_tau x_1}). The follow-up route-pruning no-go
SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md
computed the "sharpened pin": a single per-axis Z_2 boundary-condition datum
(antiperiodic-tau / periodic-space) breaks W exactly, and named it the minimal
axis-selecting input.

This runner SHARPENS that pin on its L=(4,4,4,4), time-first, m=0.3 surface.
For each adjacent pair it constructs
W_{a,a+1} = P_{a<->a+1} . diag((-1)^{x_a x_{a+1}}) and checks that the map
(i) preserves the periodic staggered hop exactly and (ii) maps the
antiperiodic-axis-a configuration exactly onto the
antiperiodic-axis-(a+1) configuration. The underlying coordinate swaps
generate S_4 acting transitively on the four axis labels. Hence the per-axis
Z_2 datum selects the evolution axis ONLY relative to an already-privileged
axis on that finite surface -- it is not itself a non-transportable axis
supplier there. The sublattice-parity grading is likewise W-inert (block [R]),
confirming that this tested grading carries no axis label.

Block tags: [S] baseline exchange certificate; [T] S_4 transitivity of the
antiperiodic-axis datum (the new load-bearing result); [REST] restoration /
falsification legs; [R] realness and sublattice-parity W-inertness.

All legs are class-A finite-dimensional exact linear algebra. Deterministic,
no RNG, runtime well under one minute. Convention note: the absolute
break-magnitude of a single-axis antiperiodic flip is hop-normalization
dependent; every load-bearing assertion below is classified by an exact-zero
(transport / restoration / preservation) or a strict nonzero
(non-triviality / break) result. No alternate staggered-phase convention is
tested.
"""
from __future__ import annotations

import itertools
import numpy as np

MASS = 0.3
TOL = 1e-9          # exact-zero tolerance (residuals are ~1e-15 in practice)
NONTRIV = 1.0       # a "genuinely nonzero" residual must exceed this

PASS = 0
FAIL = 0


def check(tag: str, name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {status}: {name}" + (f"  ({detail})" if detail else ""))


def build_staggered(L, bc, include_mass=True):
    """Kogut-Susskind staggered Dirac operator on a 4-torus block of shape L.

    bc[mu] in {+1,-1}: +1 periodic, -1 antiperiodic across the boundary in mu.
    Time-first phases eta_mu(x) = (-1)^{sum_{nu<mu} x_nu}, eta_0 = 1.
    The hop part is real antisymmetric (real anti-Hermitian); the mass term is
    a real diagonal (added iff include_mass).
    """
    d = len(L)
    sites = list(itertools.product(*[range(n) for n in L]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N))
    for s in sites:
        i = idx[s]
        if include_mass:
            M[i, i] += MASS
        for mu in range(d):
            eta = (-1) ** (sum(s[nu] for nu in range(mu)))
            fs = list(s)
            fs[mu] = (s[mu] + 1) % L[mu]
            fs = tuple(fs)
            sign = bc[mu] if s[mu] == L[mu] - 1 else 1
            j = idx[fs]
            M[i, j] += 0.5 * eta * sign
            M[j, i] += -0.5 * eta * sign
    return M, sites, idx


def signed_exchange(sites, idx, a, b):
    """W_{a,b} = P_{a<->b} composed with diag((-1)^{x_a x_b}). Orthogonal."""
    N = len(sites)
    W = np.zeros((N, N))
    for s in sites:
        sw = list(s)
        sw[a], sw[b] = s[b], s[a]
        W[idx[tuple(sw)], idx[s]] = (-1) ** (s[a] * s[b])
    return W


def plain_perm(sites, idx, a, b):
    N = len(sites)
    W = np.zeros((N, N))
    for s in sites:
        sw = list(s)
        sw[a], sw[b] = s[b], s[a]
        W[idx[tuple(sw)], idx[s]] = 1.0
    return W


def r(A):
    return float(np.linalg.norm(A))


# --------------------------------------------------------------------------
# [S] baseline exchange certificate (recomputed, with the no-sign falsifier)
#     On the tested equal-extent block, each checked coordinate swap maps the
#     site set to itself.
# --------------------------------------------------------------------------
L4 = (4, 4, 4, 4)                       # tested block, N = 256
Mper, sites, idx = build_staggered(L4, [1, 1, 1, 1])
W01 = signed_exchange(sites, idx, 0, 1)
N = len(sites)

check("S", "W01 orthogonal (W W^T = I)", r(W01 @ W01.T - np.eye(N)) < TOL,
      f"||WW^T-I||={r(W01 @ W01.T - np.eye(N)):.2e}")
res_pre = r(W01 @ Mper @ W01.T - Mper)
check("S", "signed exchange W01 preserves the periodic staggered hop exactly",
      res_pre < TOL, f"||W M W^T - M||={res_pre:.2e}")
P01 = plain_perm(sites, idx, 0, 1)
res_plain = r(P01 @ Mper @ P01.T - Mper)
check("S", "plain swap (no sign field) is NOT a symmetry -> certificate non-trivial",
      res_plain > NONTRIV, f"||P M P^T - M||={res_plain:.3f} (>1 required)")

# --------------------------------------------------------------------------
# [T] S_4 transitivity of the antiperiodic-axis datum (the new result)
#     adjacent transpositions (0,1),(1,2),(2,3): each preserves the periodic
#     operator AND maps antiperiodic-axis-a -> antiperiodic-axis-(a+1).
# --------------------------------------------------------------------------
def bc_anti(axis):
    bc = [1, 1, 1, 1]
    bc[axis] = -1
    return bc

for (a, b) in [(0, 1), (1, 2), (2, 3)]:
    Wab = signed_exchange(sites, idx, a, b)
    check("T", f"W_{a}{b} orthogonal", r(Wab @ Wab.T - np.eye(N)) < TOL)
    pres = r(Wab @ Mper @ Wab.T - Mper)
    check("T", f"W_{a}{b} preserves periodic staggered hop",
          pres < TOL, f"res={pres:.2e}")
    MapA, _, _ = build_staggered(L4, bc_anti(a))
    MapB, _, _ = build_staggered(L4, bc_anti(b))
    relabel = r(Wab @ MapA @ Wab.T - MapB)
    check("T", f"W_{a}{b} maps antiperiodic-axis-{a} EXACTLY onto antiperiodic-axis-{b}",
          relabel < TOL, f"||W M_ap{a} W^T - M_ap{b}||={relabel:.2e}")
    selfres = r(Wab @ MapA @ Wab.T - MapA)
    check("T", f"W_{a}{b} genuinely MOVES the antiperiodic axis (not a fixed point)",
          selfres > NONTRIV, f"||W M_ap{a} W^T - M_ap{a}||={selfres:.3f} (>1 required)")

print("[T] NOTE: the underlying swaps (0,1),(1,2),(2,3) generate S_4, which acts "
      "TRANSITIVELY on the 4 axis labels; compositions of the checked transports "
      "therefore give a single 4-element orbit on the tested surface.")

# --------------------------------------------------------------------------
# [SCOPE] tested odd-block falsifier.
#     The positive claim above is restricted to L=(4,4,4,4). At the tested
#     odd cubic block W is still well-defined but does NOT preserve the
#     periodic hop. This refutes extension to all finite cubic blocks; it is
#     not a proof for the untested family of even cubic blocks.
# --------------------------------------------------------------------------
Lodd = (3, 3, 3, 3)
Modd, sodd, iodd = build_staggered(Lodd, [1, 1, 1, 1])
Wodd = signed_exchange(sodd, iodd, 0, 1)
odd_break = r(Wodd @ Modd @ Wodd.T - Modd)
check("SCOPE", "at tested ODD cubic L=(3,3,3,3), W01 does NOT preserve the periodic "
      "hop (falsifier of an all-finite-cubic extension)",
      odd_break > NONTRIV, f"||W M_per W^T - M_per||_odd={odd_break:.3f} (>1 required)")
check("SCOPE", "at the claimed L=(4,4,4,4) surface it is exact (recap of [S])",
      r(W01 @ Mper @ W01.T - Mper) < TOL)

# --------------------------------------------------------------------------
# [REST] restoration + single-axis break (the pin, recomputed)
# --------------------------------------------------------------------------
Map0, _, _ = build_staggered(L4, [-1, 1, 1, 1])
Map01, _, _ = build_staggered(L4, [-1, -1, 1, 1])
break0 = r(W01 @ Map0 @ W01.T - Map0)
check("REST", "antiperiodic-axis-0 ALONE breaks the fixed W01 (the pin)",
      break0 > NONTRIV, f"||W M_ap0 W^T - M_ap0||={break0:.3f} (>1 required)")
restore = r(W01 @ Map01 @ W01.T - Map01)
check("REST", "antiperiodic in BOTH 0,1 restores W01 exactly (symmetric -> symmetry returns)",
      restore < TOL, f"||W M_ap01 W^T - M_ap01||={restore:.2e}")

# --------------------------------------------------------------------------
# [R] realness / discrete grading structure is W-inert (cannot be an axis
#     selector). The staggered sublattice-parity grading eps(x) =
#     (-1)^{x0+x1+x2+x3} anticommutes with the massless hop (eps D eps = -D)
#     on the tested surface. It is EXACTLY W-invariant: W permutes
#     coordinates (sum-invariant) and its
#     diagonal sign field commutes with the diagonal eps. So no axis label
#     is carried by the grading -- it is W-inert, not a selector. This is only
#     an invariance fact about the displayed grading operator, not a chirality
#     or CPT identification.
# --------------------------------------------------------------------------
Dhop, _, _ = build_staggered(L4, [1, 1, 1, 1], include_mass=False)   # real antisymmetric
eps = np.diag([(-1.0) ** (s[0] + s[1] + s[2] + s[3]) for s in sites])
check("R", "W01 is a REAL operator (commutes with K = complex conjugation)",
      r(W01 - W01.real) < TOL)
check("R", "sublattice-parity grading anticommutes with the hop: eps D eps = -D",
      r(eps @ Dhop @ eps + Dhop) < TOL, f"||eps D eps + D||={r(eps @ Dhop @ eps + Dhop):.2e}")
check("R", "the grading eps is EXACTLY W-invariant (W eps W^T = eps) -> W-inert, no axis label",
      r(W01 @ eps @ W01.T - eps) < TOL, f"||W eps W^T - eps||={r(W01 @ eps @ W01.T - eps):.2e}")

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
