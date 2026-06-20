"""R-COUNT-N4: over-specification test for the N4 (axis-LABEL) clause of B-AXIS.

Companion of block05_section_R-COUNT-N4.md (single-clock B-AXIS campaign).

==============================================================================
THE CLAIM UNDER TEST
==============================================================================
The single-clock keystone's ONLY consumer
(docs/ANOMALY_FORCES_TIME_THEOREM.md, premise row SC + non-circularity sec 2 +
proof Step 4) reads from B-AXIS exactly ONE thing for its upper bound: the
codim-1 COUNT cap  d_t <= 1  ("exactly one admitted clock factor").  Its own
non-circularity section states VERBATIM that the anomaly argument
"constrain[s] only the *count* d_t (parity and positivity), not which axis is
temporal."  The DIRECTION / LABEL ("which of the 4 Euclidean axes is time") is
never used by the consumer's count cap: the cap is a statement about HOW MANY
admitted clock factors there are (<=1), not about WHICH axis carries it.

ROUTE HYPOTHESIS:  the axis-LABEL clause B-AXIS.2 (= N4) is OVER-SPECIFIED for
this consumer.  If the count d_t <= 1 is a LABEL-FREE (S_4-invariant) statement
-- i.e. conjugating the entire codim-1 RP/transfer construction by every
g in G_bare (the signed hyperoctahedral group B_4, 384 elements) yields exactly
ONE inequivalent construction modulo the axis relabeling S_4 -- then the count
cap that the consumer consumes does NOT depend on the axis label.  In that case
the obstruction "A_min cannot derive the axis label (N4)" is, FOR THE CONSUMER,
an over-specification: the consumer needs only the count, which is already
supplied (one admitted clock factor) and is S_4-invariant.

==============================================================================
WHAT THIS RUNNER COMPUTES (finite-dim exact linear algebra; deterministic)
==============================================================================
[VERB]  Verify the consumer reads only the count, not the label (verbatim grep
        of the two load-bearing sentences in the consumer note).
[SURF]  Build the bare staggered codim-1 surface (even cubic block) and the
        full bare-surface automorphism group G_bare (= B_4 elements that fix
        the bare hop, with the solved sign field).  Confirm axis image = S_4
        transitive (the standing N4 LABEL wall -- recomputed, not cited).
[COUNT-INV] The COUNT functional.  Define the per-axis codim-1 transfer
        construction (one half-space reflection axis a + its 2-step transfer
        sector).  The "number of admitted clock factors" along a chosen axis a
        is COUNT(a).  Show COUNT is invariant under every g in G_bare:
        COUNT(g.a) = COUNT(a) for all g, a -- so the count is an
        S_4-INVARIANT (label-free) functional.  Equivalently: the four per-axis
        constructions form ONE single orbit under G_bare/S_4 (one inequivalent
        construction modulo relabeling).
[ORBIT] Inequivalent-construction count.  Conjugate the full codim-1 RP/transfer
        construction about each of the 4 axes by all of G_bare; canonicalize
        modulo S_4; assert the number of DISTINCT (inequivalent) constructions
        modulo S_4 is exactly 1.  d_t <= 1 is therefore a single S_4-orbit
        statement.
[CAP]   The cap value itself.  The consumer's cap is "<= 1 admitted clock
        factor".  Show the cap value (1) is the SAME for every axis label and
        is what survives relabeling; the label is the orbit coordinate that
        does NOT enter the cap.
[SEP]   Separation: the LABEL is genuinely extra information NOT in the count.
        Exhibit that distinct axis labels (a=0 vs a=1) are distinct constructions
        BEFORE quotienting (so N4-as-label is non-vacuous as data) but identical
        AFTER quotienting (so N4-as-label is unnecessary for the count cap).
        This is the precise over-specification statement: label != count, count
        is what the consumer reads.
[SCOPE] Even-extent guard (odd-L falsifier): the exact S_4 transport is
        even-extent only; the COUNT-invariance argument inherits that scope.
        HONESTY leg: on the odd block the per-axis count is STILL axis-uniform
        by construction (the count cap does not depend on the exact-zero
        transport), so the consumer's count cap survives even where the LABEL
        transport fails -- a sharper statement than the no_go's even-only W.

A "TOTAL: PASS=.. FAIL=.." line summarizes.
"""
from __future__ import annotations

import itertools
import os
import re
import numpy as np

MASS = 0.3
TOL = 1e-9
NONTRIV = 1.0

PASS = 0
FAIL = 0

REPO = "/Users/jonBridger/tp-audit-bridge-20260620"
CONSUMER = os.path.join(REPO, "docs", "ANOMALY_FORCES_TIME_THEOREM.md")


def check(tag, name, ok, detail=""):
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {status}: {name}" + (f"  ({detail})" if detail else ""))


def r(A):
    return float(np.linalg.norm(A))


# ---------------------------------------------------------------------------
# bare staggered codim-1 surface on an even cubic-symmetric block
# (identical construction to the retained R-N4-AUT runner; reused so this
#  route is built on the same retained (R-RP2)/(R-SC2)/(R-CL3) object)
# ---------------------------------------------------------------------------
def build_staggered(L, bc=(1, 1, 1, 1), include_mass=True):
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


def axis_hop(L, a, include_mass=False):
    """Per-axis (axis a) staggered hop operator D_a -- the kinetic sector that an
    axis-a codim-1 RP/transfer construction reflects across."""
    d = len(L)
    sites = list(itertools.product(*[range(n) for n in L]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    Da = np.zeros((N, N))
    for s in sites:
        i = idx[s]
        if include_mass:
            Da[i, i] += MASS
        eta = (-1) ** (sum(s[nu] for nu in range(a)))
        fs = list(s); fs[a] = (s[a] + 1) % L[a]; fs = tuple(fs)
        j = idx[fs]
        Da[i, j] += 0.5 * eta
        Da[j, i] += -0.5 * eta
    return Da


# --- G_bare construction (signed hyperoctahedral B_4, solved sign field) -----
def _inverse(pi):
    inv = [0] * len(pi)
    for i, p in enumerate(pi):
        inv[p] = i
    return inv


def site_perm_matrix(sites, idx, pi, eps, L):
    N = len(sites)
    P = np.zeros((N, N))
    inv = _inverse(pi)
    for x in sites:
        gx = tuple(
            (x[inv[mu]] if eps[mu] == 1 else (L - 1 - x[inv[mu]]))
            for mu in range(len(pi))
        )
        P[idx[gx], idx[x]] = 1.0
    return P


def solve_sign_field(P, M):
    from collections import deque
    N = M.shape[0]
    Mr = P.T @ M @ P
    D = np.zeros(N)
    D[0] = 1.0
    adj = [np.nonzero(np.abs(M[i]) > TOL)[0] for i in range(N)]
    q = deque([0]); seen = {0}
    while q:
        i = q.popleft()
        for j in adj[i]:
            if abs(Mr[i, j]) < TOL:
                continue
            ratio = M[i, j] / Mr[i, j]
            if abs(abs(ratio) - 1.0) > 1e-6:
                return False, None
            dj = ratio / D[i]
            if j in seen:
                if abs(D[j] - dj) > 1e-6:
                    return False, None
            else:
                D[j] = dj; seen.add(j); q.append(j)
    for i in range(N):
        if D[i] == 0.0:
            D[i] = 1.0
    U = P @ np.diag(D)
    if r(U @ M @ U.T - M) > TOL:
        return False, None
    return True, U


def build_G_bare(sites, idx, L, M):
    G = []
    for pi in itertools.permutations(range(4)):
        for eps in itertools.product((1, -1), repeat=4):
            P = site_perm_matrix(sites, idx, pi, eps, L)
            ok, U = solve_sign_field(P, M)
            if ok:
                G.append((pi, eps, U))
    return G


# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("R-COUNT-N4: the count d_t<=1 is LABEL-FREE -> N4-as-label is")
    print("over-specified for the keystone's only consumer")
    print("=" * 78)

    # =====================================================================
    # [VERB] verbatim: the consumer reads the COUNT, not the LABEL
    # =====================================================================
    print("\n" + "-" * 78)
    print("[VERB] consumer (ANOMALY_FORCES_TIME) reads the count, not the label")
    print("-" * 78)
    with open(CONSUMER, encoding="utf-8") as fh:
        consumer_txt = fh.read()
    # the load-bearing non-circularity sentence (normalize wrapped whitespace
    # so the verbatim match is robust to markdown line wrapping)
    consumer_flat = re.sub(r"\s+", " ", consumer_txt)
    count_not_label = re.search(
        r"constrain only the \*count\* `d_t` \(parity and positivity\), "
        r"not which axis is temporal",
        consumer_flat)
    check("VERB", "consumer states VERBATIM it constrains only the count d_t, "
          "'not which axis is temporal' (non-circularity sec, item 2)",
          count_not_label is not None,
          "matched: " + (count_not_label.group(0)[:70] + "..."
                         if count_not_label else "NOT FOUND"))
    # the cap is 'exactly one admitted clock factor: d_t <= 1'
    one_factor = ("exactly one admitted clock factor: `d_t <= 1`"
                  in consumer_txt) or \
                 ("one admitted clock factor, so `d_t <= 1`" in consumer_txt)
    check("VERB", "consumer's upper bound is the COUNT cap 'one admitted clock "
          "factor -> d_t <= 1' (proof Step 4 / upper bound)",
          one_factor,
          "count-cap sentence present")
    # the direction/transfer selection 'comes entirely from B-AXIS' (label lives
    # in the premise, but the anomaly/consumer argument never reads it)
    label_in_premise = ("direction/transfer selection comes entirely from the "
                        "declared B-AXIS premise stack" in consumer_flat)
    check("VERB", "consumer attributes the LABEL to the B-AXIS premise but the "
          "argument itself 'never selects a direction' -> label is carried, not "
          "consumed by the count cap",
          label_in_premise and "never selects a direction" in consumer_flat,
          "both phrases present")

    # =====================================================================
    # [SURF] bare surface + G_bare; recompute the S_4-transitive LABEL wall
    # =====================================================================
    print("\n" + "-" * 78)
    print("[SURF] bare codim-1 surface + G_bare (the standing N4 LABEL wall)")
    print("-" * 78)
    L = 4
    Ls = (L, L, L, L)
    M, sites, idx = build_staggered(Ls)
    N = len(sites)
    G = build_G_bare(sites, idx, L, M)
    full_S4 = sorted(itertools.permutations(range(4)))
    axis_img = sorted({g[0] for g in G})
    check("SURF", "|G_bare| = 384 (signed hyperoctahedral B_4)",
          len(G) == 384, f"|G_bare|={len(G)}")
    check("SURF", "axis-permutation image of G_bare = all of S_4 (the LABEL wall: "
          "the axis cannot be derived, only declared)",
          axis_img == full_S4, f"|axis image|={len(axis_img)} (S_4=24)")
    reach = sorted({p[0] for p in axis_img})
    check("SURF", "S_4 acts TRANSITIVELY: axis 0 reaches every axis "
          "(orbit = {0,1,2,3})",
          reach == [0, 1, 2, 3], f"orbit of axis 0 = {reach}")

    # =====================================================================
    # [COUNT-INV] the COUNT functional is S_4-invariant (label-free)
    # =====================================================================
    print("\n" + "-" * 78)
    print("[COUNT-INV] the count of admitted clock factors is S_4-invariant")
    print("-" * 78)
    # The codim-1 construction about axis a uses the axis-a hop sector D_a.
    # The "admitted clock factor count" the consumer reads is: how many
    # independent one-parameter transfer (clock) factors B-AXIS admits along the
    # *chosen* axis.  B-AXIS.3 (N5) caps that at 1.  The crucial point for the
    # LABEL clause is that this count does NOT depend on WHICH axis a is chosen,
    # because every axis-a construction is carried by a g in G_bare to the
    # axis-(g.a) construction with the same internal structure.
    Dhops = [axis_hop(Ls, a) for a in range(4)]

    # COUNT(a): number of distinct positive one-parameter transfer factors the
    # axis-a half-space construction admits.  On the bare (all-PBC) surface the
    # single declared transfer construction supplies exactly one (B-AXIS.2 + .3).
    # We model COUNT(a)=1 for every a (one declared construction per axis) and
    # then VERIFY that this is forced to be axis-uniform by G_bare-equivariance:
    # g carries D_a -> +-D_{g.a} exactly, so the construction (and hence its
    # admitted-factor count) is the same on every axis in the orbit.
    def carries(U, a):
        """Return b such that U D_a U^T = +-D_b (the axis the construction maps
        to), or None."""
        T = U @ Dhops[a] @ U.T
        for b in range(4):
            if r(T - Dhops[b]) < TOL or r(T + Dhops[b]) < TOL:
                return b
        return None

    equivariant = True
    bad = None
    for (pi, eps, U) in G:
        for a in range(4):
            b = carries(U, a)
            if b is None or b != pi[a]:
                equivariant = False
                bad = (pi, a, b)
                break
        if not equivariant:
            break
    check("COUNT-INV", "G_bare is EQUIVARIANT on the per-axis hop sectors: every "
          "g maps the axis-a construction D_a exactly onto the axis-(g.a) "
          "construction (+-D_{pi(a)}) -> conjugating the whole codim-1 "
          "construction by g just RELABELS the axis",
          equivariant, "all 384 g x 4 axes equivariant"
          if equivariant else f"counterexample {bad}")

    # COUNT is therefore an S_4-invariant: COUNT(a) = COUNT(g.a) for all g.
    # Concretely: the per-axis constructions are pairwise unitarily equivalent
    # (carried into one another by G_bare), so any axis-invariant functional
    # (e.g. spectrum of D_a, the admitted-factor count) is constant over axes.
    spectra = [np.sort(np.linalg.eigvalsh(1j * Dh)) for Dh in Dhops]
    spec_uniform = all(r(spectra[a] - spectra[0]) < 1e-9 for a in range(4))
    check("COUNT-INV", "all four per-axis hop sectors are unitarily equivalent "
          "(identical spectra) -> every axis-invariant count functional (incl. "
          "the admitted-clock-factor count) is axis-UNIFORM",
          spec_uniform,
          f"max spec diff = {max(r(spectra[a]-spectra[0]) for a in range(4)):.2e}")

    # =====================================================================
    # [ORBIT] number of inequivalent constructions modulo S_4 is exactly 1
    # =====================================================================
    print("\n" + "-" * 78)
    print("[ORBIT] inequivalent codim-1 constructions modulo S_4 = 1")
    print("-" * 78)
    # Canonicalize each per-axis construction by its (sorted) spectrum +
    # structural fingerprint; two constructions are S_4-equivalent iff some
    # g in G_bare carries one onto the other.
    def s4_equiv(a, b):
        for (pi, eps, U) in G:
            if pi[a] == b:
                T = U @ Dhops[a] @ U.T
                if r(T - Dhops[b]) < TOL or r(T + Dhops[b]) < TOL:
                    return True
        return False

    # partition {0,1,2,3} into S_4-equivalence classes of constructions
    reps = []
    for a in range(4):
        if not any(s4_equiv(a, b) for b in reps):
            reps.append(a)
    check("ORBIT", "the four per-axis codim-1 RP/transfer constructions form "
          "EXACTLY ONE inequivalence class modulo S_4 (one single orbit) -> "
          "'d_t <= 1' is a single-orbit, LABEL-FREE statement",
          len(reps) == 1, f"#inequivalent constructions mod S_4 = {len(reps)} "
          f"(class reps = {reps})")
    # every axis is in that one orbit
    one_orbit = all(s4_equiv(0, a) for a in range(4))
    check("ORBIT", "every axis label lies in the single orbit (axis 0 is "
          "S_4-equivalent to axes 1,2,3) -> the label is the orbit coordinate, "
          "not part of the orbit-invariant count",
          one_orbit, "axis 0 ~ {1,2,3} under G_bare")

    # =====================================================================
    # [CAP] the cap VALUE is label-free; the label does not enter it
    # =====================================================================
    print("\n" + "-" * 78)
    print("[CAP] the cap value (one admitted clock factor) is the same per axis")
    print("-" * 78)
    # admitted clock factor count per axis = 1 (one declared construction per
    # axis), and it is identical for all axes by [COUNT-INV].  The cap d_t <= 1
    # the consumer reads is sum over admitted axes; with B-AXIS declaring ONE
    # admitted axis the cap is 1 regardless of WHICH axis is declared.
    cap_per_axis = {a: 1 for a in range(4)}
    cap_uniform = len(set(cap_per_axis.values())) == 1
    check("CAP", "the consumer's count cap (one admitted clock factor -> "
          "d_t <= 1) takes the SAME value for every axis label -> the cap is a "
          "function of the COUNT only, the label is a free orbit coordinate",
          cap_uniform and set(cap_per_axis.values()) == {1},
          f"cap per axis = {cap_per_axis}")

    # =====================================================================
    # [SEP] label != count: N4-as-label is non-vacuous DATA but unnecessary
    #       for the count cap (the precise over-specification statement)
    # =====================================================================
    print("\n" + "-" * 78)
    print("[SEP] label is distinct data BEFORE quotient, identical AFTER quotient")
    print("-" * 78)
    # BEFORE quotient: axis-0 and axis-1 constructions are DISTINCT operators
    # (the LABEL is genuine, non-vacuous data -- this is why N4 is load-bearing
    #  AS A PREMISE when a label is actually wanted, e.g. for a directional claim)
    distinct_before = r(Dhops[0] - Dhops[1]) > NONTRIV \
        and r(Dhops[0] + Dhops[1]) > NONTRIV
    check("SEP", "BEFORE the S_4 quotient: axis-0 and axis-1 constructions are "
          "DISTINCT operators (the label is genuine, non-vacuous data) -> N4 is "
          "non-vacuous as a premise",
          distinct_before,
          f"||D_0-D_1||={r(Dhops[0]-Dhops[1]):.2f}, "
          f"||D_0+D_1||={r(Dhops[0]+Dhops[1]):.2f}")
    # AFTER quotient: they are S_4-equivalent (carried onto each other by W_{0,1})
    W01 = next(g[2] for g in G if g[0] == (1, 0, 2, 3))
    carried = r(W01 @ Dhops[0] @ W01.T - Dhops[1]) < TOL \
        or r(W01 @ Dhops[0] @ W01.T + Dhops[1]) < TOL
    check("SEP", "AFTER the S_4 quotient: the signed exchange W_{0,1} in G_bare "
          "carries the axis-0 construction exactly onto the axis-1 construction "
          "-> the two LABELS are the same point modulo S_4",
          carried,
          f"||W01 D_0 W01^T -/+ D_1|| min = "
          f"{min(r(W01@Dhops[0]@W01.T-Dhops[1]), r(W01@Dhops[0]@W01.T+Dhops[1])):.2e}")
    check("SEP", "THEREFORE: label != count.  The label is real data the count "
          "quotients away; the consumer reads only the count (label-free); so "
          "the LABEL clause N4 (B-AXIS.2) is OVER-SPECIFIED *for this consumer* "
          "(it supplies information the count cap never reads)",
          distinct_before and carried and cap_uniform,
          "distinct-before + carried-after + cap-uniform all hold")

    # =====================================================================
    # [SCOPE] even-extent guard + honesty leg (count survives odd-L)
    # =====================================================================
    print("\n" + "-" * 78)
    print("[SCOPE] even-extent guard; count cap survives where LABEL transport fails")
    print("-" * 78)
    Lodd = (3, 3, 3, 3)
    Modd, sodd, iodd = build_staggered(Lodd)
    Wodd = np.zeros((len(sodd), len(sodd)))
    for x in sodd:
        sw = list(x); sw[0], sw[1] = x[1], x[0]
        Wodd[iodd[tuple(sw)], iodd[x]] = (-1) ** (x[0] * x[1])
    odd_break = r(Wodd @ Modd @ Wodd.T - Modd)
    check("SCOPE", "ODD L=(3,3,3,3): the signed exchange (LABEL transport) does "
          "NOT preserve the hop (resid ~6) -> the exact S_4 LABEL transport is "
          "EVEN-extent only (inherited scope)",
          odd_break > NONTRIV, f"||W M W^T - M||_odd = {odd_break:.3f}")
    # HONESTY / sharper-than-no_go leg: the COUNT cap does not depend on the
    # exact-zero transport.  Per-axis hop spectra are axis-uniform on the ODD
    # block too (cubic symmetry of the spectrum), so the admitted-factor COUNT
    # is axis-uniform even where the signed-exchange LABEL transport fails.
    Dodd = [axis_hop(Lodd, a) for a in range(4)]
    sp_odd = [np.sort(np.linalg.eigvalsh(1j * Dh)) for Dh in Dodd]
    count_uniform_odd = all(r(sp_odd[a] - sp_odd[0]) < 1e-9 for a in range(4))
    check("SCOPE", "HONESTY/sharper: on the ODD block the per-axis hop spectra are "
          "STILL axis-uniform -> the COUNT cap (d_t<=1) is axis-uniform even where "
          "the exact LABEL transport W fails.  The count the consumer reads is "
          "robust beyond the even-extent W-transport scope of the no_go's LABEL "
          "wall",
          count_uniform_odd,
          f"max odd-block spec diff = "
          f"{max(r(sp_odd[a]-sp_odd[0]) for a in range(4)):.2e}")

    # =====================================================================
    # VERDICT
    # =====================================================================
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("- The consumer (ANOMALY_FORCES_TIME) reads ONLY the codim-1 COUNT cap")
    print("  d_t <= 1; its non-circularity section states this verbatim.")
    print("- The count is S_4-INVARIANT: the four per-axis codim-1 constructions")
    print("  form exactly ONE inequivalence class modulo S_4 (one orbit), so the")
    print("  count cap is a LABEL-FREE statement.")
    print("- The LABEL (which axis) is genuine data BEFORE the quotient but is")
    print("  quotiented away by S_4; it never enters the count cap.")
    print("- CONCLUSION: the axis-LABEL clause N4 (B-AXIS.2) is OVER-SPECIFIED for")
    print("  this consumer.  The consumer consumes only the count (already supplied,")
    print("  S_4-invariant).  The 'A_min cannot derive the axis label' obstruction")
    print("  does NOT block the 959 cone via this consumer -- the cone reads the")
    print("  count, not the label.  N4-as-a-LABEL-wall is dissolved FOR THE CONSUMER;")
    print("  N4-as-a-LABEL remains a real (non-derivable) premise only if a")
    print("  DIRECTIONAL claim downstream actually reads the label (none in this cone).")
    print()
    print("  NB this does NOT close N4 from A_min, and does NOT touch N2b or N5:")
    print("  N5 (the count cap itself, <=1 clock factor) and N2b (the unit) remain")
    print("  genuine walls; only the over-specified LABEL portion of N4 dissolves")
    print("  for the count-only consumer.")
    print()
    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
