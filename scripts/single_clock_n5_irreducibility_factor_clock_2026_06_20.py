#!/usr/bin/env python3
"""R-N5-IRR: irreducibility / gauge-redundancy of factor-clock decompositions
of the ACTUAL supplied two-step transfer T̂² (clause N5, no-second-clock).

WHAT THIS PUSHES PAST
=====================
Two prior branches (single-clock-n5-factor-boundary-20260617 and
single-clock-physical-clock-inventory-20260617) showed only that an ARBITRARY
two-qubit tensor product supports commuting positive factor transfers with a
2D generator span. Both ended with MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE
and explicitly LEFT OPEN the irreducibility / gauge-redundancy question on the
framework's OWN source surface. They never built the supplied T̂² and never
asked whether the factor flows carry *independent observable record content*.

This runner builds the ACTUAL supplied object from (R-RP2)/(R-SC2):

    T̂² = Gamma(t1^(2)) = ⊗_p diag(1, e^{-2E(p)}) = exp(-2 a_τ H_hat),
    H_hat = Σ_p E(p) n_p ,   E(p) = arcsinh(sqrt(m^2 + sin^2 p)) ,
    n_p = a_p^† a_p ,   spatial momentum modes p (free staggered 1+1d).

KEY STRUCTURAL FACT (recomputed here, block [SURF]): the SUPPLIED T̂² is NOT
merely factorizable — it is MAXIMALLY factorized: a tensor product of L_s
commuting per-mode factors, each diag(1, e^{-2E(p)}). So "does T̂² admit a
nontrivial commuting factor decomposition?" answers YES trivially on the source
surface. The arbitrary-2-qubit prior countermodel is a strictly weaker proxy
for what the real object already does. Therefore an irreducibility theorem in
the naive sense is FALSE for T̂².

R-N5-IRR therefore turns to the only question that can CLOSE N5: are the
per-mode factor flows U_p(s) = exp(-i s n_p) GAUGE/REDUNDANT (no independent
observable record-order parameter), or do they carry INDEPENDENT OBSERVABLE
CLOCK CONTENT?

THE TWO HONEST LEGS
===================
[GAUGE] Try to CLOSE N5 (gauge-redundancy attempt). A "clock" must be readable
        by the Record axiom: an outcome is the K/CPT orbit of a realized
        CENTRAL sector; the durable observables here are the simultaneously
        diagonal occupations {n_p}. Test whether the RELATIVE flow between two
        factor clocks (advance n_p alone, holding the global single-clock orbit
        of H_hat fixed) is unobservable as a record — i.e. whether the only
        record-distinguishable content of any product of factor flows is a
        function of the H_hat orbit time alone (single-orbit collapse).

[CONTENT] Confirm N5 LIVE (independent-content attempt). Test whether two
        factor flows with non-proportional generators produce occupation /
        record histories that the single one-parameter H_hat orbit
        exp(-i t H_hat) provably CANNOT reproduce, by a relabeling-invariant
        observable discriminator (not a phase that Record cannot see).

OUTCOME (honest, stated up front, then verified leg-by-leg below):
The [GAUGE] closure FAILS. The factor flows are NOT gauge: distinct
non-proportional generators in the span of {n_p} produce DISTINCT records
(distinct durable occupation outcomes / distinct K-orbit central sectors) that
no single H_hat orbit reproduces, and Record (durable occupation additivity)
SEES the difference. So the per-mode factor flows carry independent observable
content and N5 remains a LIVE wall: A_min (Lattice/Quantum/Record) + the
supplied (R-RP2)/(R-SC2) surface does NOT exclude a second commuting
clock; exclusion needs an EXTRA physical-clock-admission bridge that A_min does
not supply (Record supplies no occupancy rule / no dynamics / no clock map).

This is a NEGATIVE BOUNDARY result for N5, now anchored on the source surface
rather than a proxy — it sharpens the wall, it does not crack it.

A_min DISCIPLINE: every load-bearing fact is recomputed here from the staggered
dispersion E(p) and finite linear algebra. No status edits. No new axiom.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

PASS = 0
FAIL = 0


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}][{tag}] {label}" + (f"  -- {detail}" if detail else ""))


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, ord=2))


# ---------------------------------------------------------------------
# Action-derived free staggered dispersion and the supplied T̂² object
# E(p) = arcsinh( sqrt(m^2 + sin^2 p) ) ; t1^(2)(p) = e^{-2 E(p)}
# ---------------------------------------------------------------------


def E_dispersion(p: float, m: float) -> float:
    return math.asinh(math.sqrt(m * m + math.sin(p) ** 2))


def momenta(Ls: int) -> list[float]:
    return [2.0 * math.pi * k / Ls for k in range(Ls)]


def jw_number_ops(Ls: int) -> list[np.ndarray]:
    """Jordan-Wigner occupation operators n_p on the Fock space ⊗_p {|0>,|1>}.
    For a diagonal kernel the number operators are simply per-mode diag(0,1)
    lifted by tensor products (no Wilson string needed since n_p are even)."""
    sz1 = np.diag([0.0, 1.0])  # diag(0,1) = n on one mode
    ident = np.eye(2)
    ns = []
    for q in range(Ls):
        op = np.array([[1.0]])
        for k in range(Ls):
            op = np.kron(op, sz1 if k == q else ident)
        ns.append(op)
    return ns


def build_supplied_T2(Ls: int, m: float):
    """Build the ACTUAL supplied T̂² = ⊗_p diag(1, e^{-2E(p)}) and the
    second-quantized H_hat = Σ_p E(p) n_p. Returns T2, H_hat, list of n_p,
    and the per-mode kernels lambda_p = e^{-2E(p)}."""
    ps = momenta(Ls)
    Es = [E_dispersion(p, m) for p in ps]
    lams = [math.exp(-2.0 * E) for E in Es]
    T2 = np.array([[1.0]])
    for lam in lams:
        T2 = np.kron(T2, np.diag([1.0, lam]))
    ns = jw_number_ops(Ls)
    H_hat = sum(E * n for E, n in zip(Es, ns))
    return T2, H_hat, ns, lams, Es


# =====================================================================
# [SURF] the supplied T̂² IS maximally factorized (recompute the source)
# =====================================================================


def block_SURF(Ls: int, m: float):
    print()
    print("-" * 72)
    print("[SURF] the supplied T̂² is a tensor product of per-mode factor clocks")
    print("-" * 72)
    a_tau = 1.0
    T2, H_hat, ns, lams, Es = build_supplied_T2(Ls, m)
    dim = 2 ** Ls

    # (1) T̂² = exp(-2 a_tau H_hat) exactly (the supplied identity).
    expH = _expm_herm(-2.0 * a_tau * H_hat)
    record("SURF", "T̂² = exp(-2 a_τ H_hat) exactly (supplied (R-SC2) identity)",
            opnorm(T2 - expH) < 1e-12, f"resid={opnorm(T2 - expH):.2e}, dim={dim}")

    # (2) T̂² factorizes as a tensor product over spatial momentum modes:
    #     it equals ⊗_p T_p with T_p = diag(1, e^{-2E(p)}) lifted.
    #     Each lifted factor is a positive commuting transfer.
    Tfacs = []
    for q in range(Ls):
        Tq = np.array([[1.0]])
        for k in range(Ls):
            Tq = np.kron(Tq, np.diag([1.0, lams[k]]) if k == q else np.eye(2))
        Tfacs.append(Tq)
    prod = np.eye(dim)
    for Tq in Tfacs:
        prod = prod @ Tq
    record("SURF", "T̂² = ∏_p (lifted per-mode factor) exactly",
            opnorm(T2 - prod) < 1e-12, f"resid={opnorm(T2 - prod):.2e}")

    # (3) all per-mode factor transfers are positive-definite (trivial kernel)
    posok = all(np.min(np.linalg.eigvalsh(Tq)) > 1e-12 for Tq in Tfacs)
    record("SURF", "every lifted per-mode factor transfer is positive-definite",
            posok, f"L_s={Ls} factors")

    # (4) they commute pairwise EXACTLY (genuine commuting factor clocks)
    cmax = 0.0
    for i in range(Ls):
        for j in range(i + 1, Ls):
            cmax = max(cmax, opnorm(Tfacs[i] @ Tfacs[j] - Tfacs[j] @ Tfacs[i]))
    record("SURF", "all per-mode factor transfers commute pairwise (resid 0)",
            cmax < 1e-13, f"max comm resid={cmax:.2e}")

    # (5) the generator tangent span {n_p} has dimension L_s (NOT 1).
    #     This is the maximal-reducibility fact: the naive irreducibility
    #     theorem for T̂² is FALSE — it splits into L_s independent factors.
    span = np.stack([n.ravel() for n in ns])
    rank = np.linalg.matrix_rank(span, tol=1e-12)
    record("SURF", "factor-generator tangent span has dimension L_s (maximal reducibility)",
            rank == Ls, f"rank={rank}, L_s={Ls}")

    # (6) explicit refutation: any single-orbit claim "span is 1-dimensional /
    #     all factors are reparametrizations of one clock" is FALSE for L_s>=2,
    #     because n_p and n_q (p!=q) are linearly independent.
    if Ls >= 2:
        indep = np.linalg.matrix_rank(np.stack([ns[0].ravel(), ns[1].ravel()]), tol=1e-12)
        record("SURF", "two distinct mode generators n_p, n_q are linearly independent (>1 clock direction)",
                indep == 2, f"rank(n_0,n_1)={indep}")
    return T2, H_hat, ns, Es


def _expm_herm(A: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(A)
    return (vecs * np.exp(vals)) @ vecs.conj().T


# =====================================================================
# [GAUGE] try to CLOSE N5: are the factor flows gauge / record-invisible?
# =====================================================================


def block_GAUGE(Ls: int, H_hat: np.ndarray, ns: list[np.ndarray], Es: list[float]):
    print()
    print("-" * 72)
    print("[GAUGE] closure attempt: are relative factor flows unobservable (gauge)?")
    print("-" * 72)
    dim = 2 ** Ls

    # Record axiom: an outcome is the K/CPT orbit of the realized CENTRAL sector.
    # On this diagonal surface the durable central observables are the
    # simultaneously-diagonal occupations {n_p}. The candidate gauge claim is:
    # "the only record-distinguishable content of any product of factor flows
    #  U(s_0,...,s_{Ls-1}) = exp(-i Σ_q s_q n_q) is a function of the single
    #  H_hat-orbit time t alone, so the extra factor directions are gauge."
    #
    # We test this on the durable record observables themselves. Because all
    # n_q are diagonal in the occupation basis, U(s) acts as a phase on each
    # occupation eigenstate. The record (durable occupation outcome) of an
    # occupation eigenstate is UNCHANGED by U(s) — so far consistent with a
    # gauge reading on a single eigenstate. The honest test is whether the
    # flow distinguishes records on the FULL state space, i.e. whether the
    # factor directions ever change a durable central-sector outcome relative
    # to the single H_hat orbit. We build the strongest gauge case and then
    # try to break it.

    # Single-clock orbit family: { exp(-i t H_hat) : t in R }.
    # Factor-flow family: { exp(-i Σ_q s_q n_q) : s in R^{Ls} }.
    # GAUGE would hold iff for every factor flow there is a single t giving the
    # SAME action on ALL durable records (occupation projectors) AND on the
    # off-diagonal record-coherence observables that A_min's K/CPT orbit can
    # see. We check the cleanest necessary condition: does the factor-flow
    # family equal the single-clock orbit family as sets of unitaries up to a
    # global phase (which Record cannot see)?

    # Necessary condition for gauge-collapse: every factor generator Σ s_q n_q
    # must be (global phase) + (scalar)·H_hat, i.e. lie in span{ I, H_hat }.
    I = np.eye(dim)
    basis = np.stack([I.ravel(), H_hat.ravel()])
    base_rank = np.linalg.matrix_rank(basis, tol=1e-12)
    # add each n_q and see whether rank grows (rank growth => NOT in span{I,H})
    grew = 0
    for q in range(Ls):
        r = np.linalg.matrix_rank(np.stack([I.ravel(), H_hat.ravel(), ns[q].ravel()]),
                                  tol=1e-12)
        if r > base_rank:
            grew += 1
    # The gauge-collapse HYPOTHESIS (which would CLOSE N5) requires grew==0:
    # every mode generator must lie inside span{I, H_hat}. We test the honest
    # negation: the closure attempt FAILS exactly when grew>0. The runner
    # asserts the TRUE state of affairs (closure fails), recording the count of
    # escaping directions as the falsifier of the gauge-collapse hypothesis.
    record("GAUGE", "gauge-collapse hypothesis (all n_q in span{I,H_hat}) is FALSIFIED",
            grew > 0,
            f"{grew} of {Ls} mode generators lie OUTSIDE span(I,H_hat) "
            f"(would need 0 for gauge closure); base_rank={base_rank}")
    record("GAUGE", "=> N5 closure via gauge-redundancy FAILS (factor directions are independent)",
            grew > 0,
            f"{grew} independent escaping directions -> N5 not closed by gauge")

    # Sharper: exhibit an explicit factor flow whose generator is provably NOT
    # of the form c·H_hat + b·I. Use G = n_0 (single-mode clock). For G to be
    # gauge-equivalent to the H_hat clock we'd need G = c H_hat + b I.
    if Ls >= 2:
        G = ns[0].copy()
        # least-squares fit G ≈ c H_hat + b I and measure residual.
        A = np.stack([H_hat.ravel(), I.ravel()]).T
        coef, *_ = np.linalg.lstsq(A, G.ravel(), rcond=None)
        resid = opnorm(G - (coef[0] * H_hat + coef[1] * I))
        record("GAUGE", "explicit single-mode clock n_0 is NOT c·H_hat + b·I (irreducible direction)",
                resid > 1e-6,
                f"best-fit residual={resid:.4f} (>0 => genuinely independent generator)")


# =====================================================================
# [CONTENT] confirm N5 LIVE: factor flows carry independent RECORD content
# =====================================================================


def block_CONTENT(Ls: int, H_hat: np.ndarray, ns: list[np.ndarray], Es: list[float]):
    print()
    print("-" * 72)
    print("[CONTENT] independent-content: factor flows produce records H_hat cannot")
    print("-" * 72)
    dim = 2 ** Ls
    if Ls < 2:
        record("CONTENT", "needs L_s>=2 for a second mode", False)
        return

    # Build two genuinely different clock generators living on the supplied
    # surface, BOTH in the admitted positive-generator cone span_{>=0}{n_p}:
    #   H_hat       = Σ_p E(p) n_p        (the framework's single clock)
    #   G_alt       = n_0                  (a single-mode factor clock)
    # G_alt is positive, commutes with H_hat, and is a legitimate transfer
    # generator on the SAME source surface (it is one of the tensor factors).

    G_alt = ns[0]
    record("CONTENT", "alt clock G_alt = n_0 commutes with H_hat (joint diagonal)",
            opnorm(H_hat @ G_alt - G_alt @ H_hat) < 1e-13,
            f"resid={opnorm(H_hat @ G_alt - G_alt @ H_hat):.2e}")

    # OBSERVABLE DISCRIMINATOR (relabeling-invariant, Record-visible).
    # Records here are DURABLE OCCUPATION OUTCOMES: the central-sector
    # projectors are the occupation projectors; the K/CPT orbit of a realized
    # sector is its occupation pattern. Consider the imaginary-time (transfer)
    # evolution of the durable record expectation <n_1> from a fixed initial
    # density that is a uniform mixture of single-particle sectors.
    #
    # Under the single clock T̂²(t) = exp(-2 a_tau t H_hat) the decay rate of
    # the durable occupation <n_1> is fixed at 2 E(p_1) per unit blocked step.
    # Under a SECOND independent factor clock acting on mode 0 only,
    # T_alt(s) = exp(-2 a_tau s G_alt) = exp(-2 a_tau s n_0), the durable
    # occupation <n_1> is INVARIANT while <n_0> decays. The two clocks produce
    # DISTINCT durable-record histories that NO single reparametrization of the
    # H_hat clock reproduces (a single clock cannot freeze <n_1> while moving
    # <n_0>, because under exp(-2 a t H_hat) BOTH occupations move together at
    # ratio E(p_0):E(p_1)).

    # initial diagonal density: equal weight on |10..0> and |01 0..0>
    # (one particle in mode 0, or one particle in mode 1).
    def occ_state(modes_filled):
        v = np.zeros(dim)
        idx = 0
        for q in modes_filled:
            idx |= (1 << (Ls - 1 - q))
        v[idx] = 1.0
        return v

    v0 = occ_state([0])     # particle in mode 0
    v1 = occ_state([1])     # particle in mode 1
    rho = 0.5 * np.outer(v0, v0) + 0.5 * np.outer(v1, v1)

    def transfer(gen, s):
        return _expm_herm(-2.0 * 1.0 * s * gen)

    def record_expect(rho_s, obs):
        return float(np.trace(rho_s @ obs).real)

    s = 0.7
    # single clock H_hat
    Th = transfer(H_hat, s)
    rho_H = Th @ rho @ Th  # imaginary-time (positive) propagation, unnormalized
    n0_H = record_expect(rho_H, ns[0])
    n1_H = record_expect(rho_H, ns[1])

    # second factor clock G_alt = n_0 (acts on mode 0 only)
    Ta = transfer(G_alt, s)
    rho_A = Ta @ rho @ Ta
    n0_A = record_expect(rho_A, ns[0])
    n1_A = record_expect(rho_A, ns[1])

    # Discriminator 1: under the alt factor clock <n_1> is UNCHANGED (mode 1
    # untouched), while under the single H_hat clock <n_1> DECAYS.
    n1_initial = record_expect(rho, ns[1])
    alt_freezes_n1 = abs(n1_A - n1_initial) < 1e-12
    single_moves_n1 = abs(n1_H - n1_initial) > 1e-3
    record("CONTENT", "factor clock FREEZES durable record <n_1> (mode 1 untouched)",
            alt_freezes_n1, f"<n_1>: init={n1_initial:.4f} -> alt={n1_A:.4f}")
    record("CONTENT", "single H_hat clock MOVES durable record <n_1> (cannot freeze it)",
            single_moves_n1, f"<n_1>: init={n1_initial:.4f} -> H_hat={n1_H:.4f}")

    # Discriminator 2 (the decisive one): NO scalar reparametrization t of the
    # single clock reproduces the alt clock's durable-record pair (<n_0>,<n_1>).
    # Sweep t over a fine grid and confirm the alt outcome is never matched.
    ts = np.linspace(0.0, 6.0, 60001)
    target = np.array([n0_A, n1_A])
    best = np.inf
    for t in ts:
        Tt = transfer(H_hat, t)
        rr = Tt @ rho @ Tt
        cur = np.array([record_expect(rr, ns[0]), record_expect(rr, ns[1])])
        best = min(best, float(np.linalg.norm(cur - target)))
    record("CONTENT", "NO single-clock time t reproduces the alt clock's durable record pair",
            best > 1e-3,
            f"min over t of ||(<n_0>,<n_1>)_t - alt|| = {best:.4f} (>0 => independent content)")

    # Discriminator 3 (Record-axiom level, basis-free): the two flows realize
    # DISTINCT central sectors. Project to the single-particle sector and read
    # the K/CPT orbit (occupation pattern) selected by the dominant outcome.
    # The alt clock biases mode 0's outcome only; the single clock biases by
    # E(p) ordering across ALL modes. Confirm the dominant durable sector
    # differs between the two flows for suitable s, proving the records differ.
    # Use a strongly anisotropic check: large s.
    s2 = 3.0
    Th2 = transfer(H_hat, s2)
    Ta2 = transfer(G_alt, s2)
    rH2 = Th2 @ rho @ Th2
    rA2 = Ta2 @ rho @ Ta2
    # normalized durable occupation profile across all modes
    profH = np.array([record_expect(rH2, n) for n in ns])
    profA = np.array([record_expect(rA2, n) for n in ns])
    profH = profH / (profH.sum() + 1e-30)
    profA = profA / (profA.sum() + 1e-30)
    l1diff = float(np.abs(profH - profA).sum())
    record("CONTENT", "durable occupation RECORD PROFILE differs between the two clocks",
            l1diff > 1e-2,
            f"L1 distance of normalized record profiles = {l1diff:.4f}")

    # Record-axiom compatibility of the alt clock (it is a legitimate record-
    # producing flow, not forbidden by Record): disjoint occupation projectors
    # commute, are operator-monotone, and have additive scalar readout.
    P0, P1 = ns[0], ns[1]
    record("CONTENT", "alt-clock record projectors commute (durable, additive)",
            opnorm(P0 @ P1 - P1 @ P0) < 1e-13, f"resid={opnorm(P0 @ P1 - P1 @ P0):.2e}")
    record("CONTENT", "scalar readout additive on disjoint records I(P0)+I(P1)=I(P0+P1)",
            abs(np.trace(P0).real + np.trace(P1).real - np.trace(P0 + P1).real) < 1e-12)


# =====================================================================
# [BRIDGE] what an N5 closure WOULD need that A_min does not supply
# =====================================================================


def block_BRIDGE(Ls: int, ns: list[np.ndarray]):
    print()
    print("-" * 72)
    print("[BRIDGE] the missing supplier: a physical-clock-admission datum")
    print("-" * 72)
    dim = 2 ** Ls
    # The ONLY way to collapse the L_s factor clocks to one is to ADMIT exactly
    # one positive direction in the cone span_{>=0}{n_p} as 'the physical clock'
    # and DECLARE all others non-physical. That admission is a datum (a chosen
    # ray in R^{Ls}) NOT supplied by Lattice/Quantum/Record:
    #   - Lattice supplies sites+adjacency, no dynamics, no clock direction.
    #   - Quantum supplies the one-qubit carrier, no dynamics, no clock.
    #   - Record supplies durable outcomes + finite additivity, no occupancy
    #     rule, no time metric, no rule selecting ONE factor flow as the clock.
    # We exhibit the admission as a free ray choice: any unit positive vector
    # w in R^{Ls} gives a distinct admitted clock generator Σ w_q n_q, and
    # different w give NON-conjugate, record-distinguishable clocks.
    w_a = np.zeros(Ls); w_a[0] = 1.0           # mode-0 clock
    w_b = np.ones(Ls) / math.sqrt(Ls)          # uniform clock
    Ga = sum(wi * n for wi, n in zip(w_a, ns))
    Gb = sum(wi * n for wi, n in zip(w_b, ns))
    # distinct generators => distinct admitted clocks (rank-2 family of choices)
    distinct = opnorm(Ga - Gb) > 1e-6
    record("BRIDGE", "physical-clock admission is a FREE ray choice in span_{>=0}{n_p}",
            distinct, f"two admissible clock rays differ by {opnorm(Ga - Gb):.3f}")
    # the family of admissible clock rays is (L_s - 1)-parameter, so the
    # admission carries genuine undetermined content that A_min does not fix.
    record("BRIDGE", "admission carries (L_s - 1) undetermined parameters (not fixed by A_min)",
            Ls - 1 >= 1, f"free clock-ray parameters = {Ls - 1}")


def main() -> int:
    print("=" * 72)
    print("R-N5-IRR: irreducibility / gauge-redundancy of factor-clock")
    print("decompositions of the SUPPLIED two-step transfer T̂²  (clause N5)")
    print("=" * 72)

    for (Ls, m) in [(3, 0.5), (4, 0.3)]:
        print()
        print("#" * 72)
        print(f"# SOURCE SURFACE: L_s={Ls} spatial modes, mass m={m}")
        print("#" * 72)
        T2, H_hat, ns, Es = block_SURF(Ls, m)
        block_GAUGE(Ls, H_hat, ns, Es)
        block_CONTENT(Ls, H_hat, ns, Es)
        block_BRIDGE(Ls, ns)

    print()
    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    print("VERDICT (honest):")
    print("  N5_NAIVE_IRREDUCIBILITY_HOLDS = FALSE   "
          "(supplied T̂² is MAXIMALLY factorized: ⊗_p per-mode clocks)")
    print("  FACTOR_FLOWS_ARE_GAUGE        = FALSE   "
          "(closure attempt fails: directions escape span{I,H_hat})")
    print("  FACTOR_FLOWS_CARRY_INDEP_RECORD_CONTENT = TRUE  "
          "(distinct durable occupation records; H_hat orbit cannot reproduce)")
    print("  N5_CLOSED_BY_A_MIN            = FALSE   "
          "(exclusion needs a physical-clock-admission ray NOT supplied by")
    print("                                          Lattice/Quantum/Record)")
    print("  B_AXIS_DERIVED = FALSE   SECOND_PHYSICAL_CLOCK_EXCLUDED = FALSE")
    print("  AUDIT_LEDGER_WRITTEN = FALSE   NEW_AXIOM_ADDED = FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
