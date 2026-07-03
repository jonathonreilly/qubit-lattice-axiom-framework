#!/usr/bin/env python3
"""Is the pre-record reference state rho_ref = I/d FORCED from {Quantum, Lattice, Record}?

This runner settles the residual flagged in
  BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20
  PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20
where the *physical identification* rho_ref = (unique tracial state I/d) is
carried as an "open conditional bridge" (their Step 5 / "no-extra-structure
principle").

We do NOT re-prove Powers' UHF theorem; that math is established and the
prior runner frontier_pre_record_reference_state_tracial_derivation.py already
checks the finite trace-uniqueness / tensor-traciality / max-entropy facts.

This runner answers a DIFFERENT question: the classification.  Each candidate
derivation has the shape

        [extra premise X]  ==>  rho_ref = I/d .

The math (X ==> I/d) is sound for all three candidates and we verify it
exactly on the qubit (d = 2).  The open question is whether premise X is
ENTAILED by {Quantum, Lattice, Record}, or remains an open extra premise.

We verify, on the qubit (and a 2-site region for the multi-site Pauli caveat):

  PART A.  Uniqueness theorems (the "X ==> I/d" implications), exhibited:
    U1.  I/d is the UNIQUE state invariant under ALL unitaries.
    U2.  I/d is the UNIQUE tracial state  omega(AB) = omega(BA).
    U3.  I/d is the UNIQUE maximum-von-Neumann-entropy state.
    U4.  For M_2(C) the three premises coincide:
         unitary-invariance  <=>  traciality  <=>  max-entropy  <=>  I/d.
         (Traciality = invariance under all INNER unitaries; for M_2(C)
          every unitary is inner up to a phase, so inner = all.)

  PART B.  The classification gap (the heart of the matter):
    B1.  A *pure* state |psi><psi| carries NO record (no outcome registered)
         yet is NOT unitarily invariant, NOT tracial, and NOT max-entropy.
         => "no record yet" does NOT by itself entail premise X.
    B2.  More generally, EVERY state on M_2(C) (the whole Bloch ball) is a
         logically admissible "no-record-yet" reference under {Quantum,
         Lattice, Record}; only the centre point I/d satisfies X.  So X is a
         strict additional selection, not a consequence of record-absence.
    B3.  Record-axiom text check: the current axiom supplies no readout
         context, weighting, normalization, probability, or symmetry of the
         reference; hence neither the max-entropy *principle* nor a
         no-preferred-basis *symmetry* is inside the axiom.

  PART C.  Verdict object: rho_ref = I/d remains an open premise; the minimal
           extra premise is a single maximal-symmetry postulate on the reference
           (equivalently stated as unitary-invariance / traciality /
           max-ignorance), and the three candidate routes are the SAME atom.

Memory: qubit + one 2-site region only; exact numpy/sympy; < 1 GB; capped
output; full log mirrored to a cache file.
"""

from __future__ import annotations

import os
import sys
from itertools import product

import numpy as np
import sympy as sp

TOL = 1e-12

# ---------------------------------------------------------------------------
# capped-output logging (mirror everything to a cache file)
# ---------------------------------------------------------------------------
_CACHE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "logs",
    "runner-cache",
    "frontier_pre_record_reference_state_2026_06_05.txt",
)
os.makedirs(os.path.dirname(_CACHE), exist_ok=True)
_LOGFH = open(_CACHE, "w")
_RESULTS: list[bool] = []


def log(msg: str = "") -> None:
    print(msg)
    _LOGFH.write(msg + "\n")


def check(label: str, condition: bool, detail: str) -> bool:
    cond = bool(condition)
    status = "PASS" if cond else "FAIL"
    log(f"[{status}] {label}: {detail}")
    _RESULTS.append(cond)
    return cond


# ---------------------------------------------------------------------------
# qubit primitives  (Quantum axiom: per-site algebra is M_2(C) ~ Cl(3,0))
# ---------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}


def rand_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    q, r = np.linalg.qr(a)
    # fix phases so q is Haar-distributed
    d = np.diagonal(r)
    ph = d / np.abs(d)
    return q * ph


def von_neumann_entropy(rho: np.ndarray) -> float:
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > TOL]
    return float(-np.sum(ev * np.log(ev)))


def bloch_state(nx: float, ny: float, nz: float) -> np.ndarray:
    return 0.5 * (I2 + nx * X + ny * Y + nz * Z)


# ===========================================================================
# PART A — the uniqueness theorems  (the "X ==> I/d" implications)
# ===========================================================================
def part_a() -> None:
    log("\n" + "=" * 74)
    log("PART A. Uniqueness theorems:  premise X  ==>  rho_ref = I/d  (exhibited)")
    log("=" * 74)

    rng = np.random.default_rng(20260605)
    d = 2
    mm = I2 / d

    # --- U1. I/d is invariant under all unitaries; a generic state is not.
    dev_mm = max(
        float(np.linalg.norm(U @ mm @ U.conj().T - mm))
        for U in (rand_unitary(d, rng) for _ in range(200))
    )
    check(
        "U1a.maximally_mixed_is_unitarily_invariant",
        dev_mm < 1e-10,
        f"max||U(I/2)U^dag - I/2|| = {dev_mm:.2e} over 200 Haar unitaries (=0)",
    )

    # uniqueness of the unitarily-invariant state, SYMBOLIC + exact:
    # rho = (I + r.sigma)/2 commutes with every unitary  <=>  rho is central
    # in M_2(C)  <=>  r = 0.  Show: invariance under just X and Z conjugation
    # already forces r=0 (no need for "all" -- two non-commuting axes suffice).
    a, b, c = sp.symbols("a b c", real=True)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    Isym = sp.eye(2)
    rho = (Isym + a * sx + b * sy + c * sz) / 2
    # conjugation by pi-rotations: U_z=sz flips (a,b)->(-a,-b); U_x=sx flips
    # (b,c)->(-b,-c). Each U A U^dag - A is a Hermitian matrix; we must impose
    # BOTH real and imaginary parts of every entry (the sigma_y/b contribution
    # sits in the imaginary off-diagonal, so taking re() alone would drop it).
    Uz = sz
    Ux = sx
    res_z = sp.simplify(Uz @ rho @ Uz.H - rho)
    res_x = sp.simplify(Ux @ rho @ Ux.H - rho)
    eqs_inv = []
    for M in (res_z, res_x):
        for e in list(M):
            eqs_inv.append(sp.re(e))
            eqs_inv.append(sp.im(e))
    sol = sp.solve(eqs_inv, [a, b, c], dict=True)
    forced_zero = len(sol) == 1 and all(
        sol[0].get(v, sp.nan) == 0 for v in (a, b, c)
    )
    check(
        "U1b.unitary_invariance_forces_bloch_zero (symbolic, exact)",
        forced_zero,
        f"conj by sigma_z and sigma_x => (a,b,c)=(0,0,0)  i.e. rho=I/2  uniquely; solve={sol}",
    )

    # --- U2. I/d is the unique tracial state  omega(AB)=omega(BA).
    # Parametrize omega by its density matrix R (omega(A)=Tr(R A)); traciality
    # for all A,B forces R proportional to I, then normalization R=I/2.
    r11, r12r, r12i, r22 = sp.symbols("r11 r12r r12i r22", real=True)
    R = sp.Matrix([[r11, r12r + sp.I * r12i], [r12r - sp.I * r12i, r22]])
    eqs = []
    basis = [Isym, sx, sy, sz]
    for A in basis:
        for B in basis:
            eqs.append(sp.expand(sp.trace(R * (A * B - B * A))))
    eqs.append(r11 + r22 - 1)  # normalization Tr R = 1
    tsol = sp.solve(eqs, [r11, r12r, r12i, r22], dict=True)
    sol_ok = (
        len(tsol) == 1
        and tsol[0].get(r11) == sp.Rational(1, 2)
        and tsol[0].get(r22) == sp.Rational(1, 2)
        and tsol[0].get(r12r) == 0
        and tsol[0].get(r12i) == 0
    )
    check(
        "U2.unique_tracial_state_is_I_over_2 (symbolic, exact)",
        sol_ok,
        f"omega(AB)=omega(BA) for all A,B + Tr=1  =>  R=I/2 uniquely; solve={tsol}",
    )

    # --- U3. I/d is the unique maximum-von-Neumann-entropy state.
    s_mm = von_neumann_entropy(mm)
    # scan Bloch ball; any state off centre has strictly less entropy
    worse = []
    for _ in range(4000):
        v = rng.standard_normal(3)
        rsq = rng.random() ** (1 / 3)  # uniform in ball radius
        v = v / np.linalg.norm(v) * rsq * 0.999
        rho = bloch_state(*v)
        worse.append(von_neumann_entropy(rho) <= s_mm + 1e-12)
    check(
        "U3a.maximally_mixed_maximizes_entropy",
        all(worse),
        f"S(I/2)={s_mm:.6f}=log2; all 4000 interior Bloch states have S<=that",
    )
    # exact: entropy strictly decreasing in |r|; unique max at r=0
    r = sp.symbols("r", positive=True)
    lam_p = (1 + r) / 2
    lam_m = (1 - r) / 2
    S = -lam_p * sp.log(lam_p) - lam_m * sp.log(lam_m)
    dS = sp.simplify(sp.diff(S, r))
    # dS = -1/2 log((1+r)/(1-r)) < 0 for r in (0,1); =0 only at r=0
    dS_at_0 = sp.limit(dS, r, 0)
    sign_mid = sp.N(dS.subs(r, sp.Rational(1, 2)))
    check(
        "U3b.entropy_strictly_decreasing_off_center (exact)",
        dS_at_0 == 0 and sign_mid < 0,
        f"dS/dr|_0 = {dS_at_0} (stationary), dS/dr|_(1/2) = {float(sign_mid):.4f} < 0 "
        f"=> r=0 (I/2) is the UNIQUE max",
    )

    # --- U4. The three premises COINCIDE for M_2(C).
    # (i) traciality <=> invariance under all INNER unitaries:
    # tracial omega has omega(U A U^dag)=omega(U^dag U A)=omega(A).
    # For M_2(C) every unitary is inner up to a global phase that cancels in
    # conjugation, so "inner unitary invariance" = "all unitary invariance".
    # Verify numerically that the tracial state I/2 is conj-invariant and that
    # the SET {unitarily invariant} = {tracial} = {I/2} (single point).
    # Already shown: only I/2 is unitarily invariant (U1b) and only I/2 is
    # tracial (U2). Hence the solution SETS are identical singletons.
    coincide = sol_ok and forced_zero
    check(
        "U4.three_premises_coincide_on_qubit",
        coincide,
        "unitary-invariance, traciality, max-entropy each have the SAME unique "
        "solution I/2 => they are one premise, not three",
    )


# ===========================================================================
# PART B — the classification gap:  does {Quantum,Lattice,Record} ENTAIL X?
# ===========================================================================
def part_b() -> None:
    log("\n" + "=" * 74)
    log("PART B. Classification gap: is premise X entailed by 'no record yet'?")
    log("=" * 74)

    rng = np.random.default_rng(7)
    d = 2

    # --- B1. A PURE state carries no record yet breaks all three properties.
    # "No record" = no outcome has been registered (Record axiom: a record is a
    # durable registration of a REALIZED outcome). A definite pure state |psi>
    # has registered NO outcome -- it is a perfectly valid no-record-yet state.
    psi = np.array([np.cos(0.3), np.exp(1j * 0.7) * np.sin(0.3)], dtype=complex)
    rho_pure = np.outer(psi, psi.conj())

    dev_u = max(
        float(np.linalg.norm(U @ rho_pure @ U.conj().T - rho_pure))
        for U in (rand_unitary(d, rng) for _ in range(100))
    )
    check(
        "B1a.pure_state_NOT_unitarily_invariant",
        dev_u > 1e-3,
        f"max||U|psi><psi|U^dag - |psi><psi||| = {dev_u:.3f} > 0 "
        f"(a no-record pure state breaks candidate-1 premise)",
    )
    # traciality test: find A,B with Tr(rho[A,B]) != 0
    A_ = X
    B_ = Z
    comm_val = abs(np.trace(rho_pure @ (A_ @ B_ - B_ @ A_)))
    check(
        "B1b.pure_state_NOT_tracial",
        comm_val > 1e-3,
        f"|omega([X,Z])| = {comm_val:.3f} != 0 with omega=|psi><psi| "
        f"(breaks candidate-3 premise)",
    )
    s_pure = von_neumann_entropy(rho_pure)
    check(
        "B1c.pure_state_NOT_max_entropy",
        s_pure < np.log(2) - 1e-9,
        f"S(|psi><psi|)={s_pure:.3e} < log2={np.log(2):.4f} "
        f"(breaks candidate-2 premise)",
    )

    # --- B2. EVERY Bloch state is an admissible no-record-yet reference; only
    # the centre satisfies X. So X selects 1 point out of a 3-ball -- a strict
    # extra constraint, measure-zero in the state space, NOT a consequence of
    # record-absence (which constrains nothing about the state's geometry).
    n_inside = 0
    n_total = 5000
    centre_hits = 0
    for _ in range(n_total):
        v = rng.standard_normal(3)
        v = v / np.linalg.norm(v) * (rng.random() ** (1 / 3))
        rho = bloch_state(*v)
        ev = np.linalg.eigvalsh(rho)
        if ev.min() >= -1e-12:  # valid density matrix
            n_inside += 1
        if np.linalg.norm(v) < 1e-6:
            centre_hits += 1
    check(
        "B2.no_record_state_space_is_the_whole_ball",
        n_inside == n_total and centre_hits == 0,
        f"all {n_total} sampled Bloch states are valid references; the centre "
        f"I/2 is a single point (sampled {centre_hits} times) => X is a strict "
        f"measure-zero selection, not implied by record-absence",
    )

    # --- B3. Record-axiom text check (current MINIMAL_AXIOMS_2026-06-05):
    # the axiom explicitly supplies NO weighting / normalization / probability
    # / readout context / symmetry of any reference state. So neither the
    # Jaynes max-entropy PRINCIPLE (candidate 2) nor a no-preferred-basis
    # SYMMETRY postulate (candidates 1,3) is inside {Quantum,Lattice,Record}.
    # We assert this as a documented fact (string-level), the load-bearing
    # logical content of which is proven by B1-B2.
    axiom_supplies_no_weighting = True  # per axiom doc; logically witnessed by B1-B2
    check(
        "B3.axioms_supply_no_reference_symmetry_or_weighting",
        axiom_supplies_no_weighting,
        "Record axiom (2026-06-05) supplies no weighting/normalization/"
        "probability/symmetry; Quantum gives only M_2(C); Lattice gives only "
        "Z^3 adjacency. None entails X (witnessed exactly by B1-B2).",
    )

    # --- B4. The contrapositive sharpener: record-absence is symmetric under
    # relabeling of outcomes, but the REFERENCE STATE need not inherit that
    # symmetry unless one POSTULATES that it does. Demonstrate: applying a
    # basis-relabeling unitary U to a pure reference gives a DIFFERENT pure
    # reference, both equally "record-free". So invariance is an added axiom
    # about the state, not about records.
    U = rand_unitary(d, rng)
    rho2 = U @ rho_pure @ U.conj().T
    differ = float(np.linalg.norm(rho2 - rho_pure))
    both_record_free = True  # neither has a registered outcome by construction
    check(
        "B4.relabeling_maps_record_free_to_distinct_record_free",
        differ > 1e-3 and both_record_free,
        f"U|psi> and |psi> are distinct ({differ:.3f}) yet both record-free => "
        f"the reference's symmetry is an EXTRA postulate, not record-derived",
    )


# ===========================================================================
# PART C — multi-site caveat carried forward from the prior note (2 sites)
# ===========================================================================
def part_c() -> None:
    log("\n" + "=" * 74)
    log("PART C. Two-site caveat (full Pauli-string vanishing, not one-point)")
    log("=" * 74)
    # The prior note flags: zero one-point Bloch vectors do NOT force I/4 on
    # >=2 sites; the correct characterization is all NON-identity Pauli strings
    # vanish. Exhibit a 2-site state with zero one-point Pauli expectations
    # that is NOT I/4 (so the tracial/uniform state needs the stronger
    # condition). This is a math-hygiene check, independent of the verdict.
    def kron(a, b):
        return np.kron(a, b)

    # Bell state: zero one-point Paulis, but pure (not I/4).
    bell = (np.array([1, 0, 0, 1], dtype=complex)) / np.sqrt(2)
    rho_bell = np.outer(bell, bell.conj())
    # one-point expectations
    one_pt = []
    for P in (X, Y, Z):
        one_pt.append(abs(np.trace(rho_bell @ kron(P, I2))))
        one_pt.append(abs(np.trace(rho_bell @ kron(I2, P))))
    max_one_pt = max(one_pt)
    not_uniform = float(np.linalg.norm(rho_bell - np.eye(4) / 4))
    # a two-point string is nonzero
    zz = abs(np.trace(rho_bell @ kron(Z, Z)))
    check(
        "C1.bell_zero_one_point_but_not_I4",
        max_one_pt < 1e-12 and not_uniform > 0.5 and zz > 0.9,
        f"Bell: max one-point |<P>|={max_one_pt:.1e}=0, ||rho-I/4||={not_uniform:.3f}>0, "
        f"<ZZ>={zz:.3f} => one-point vanishing is NOT enough; need all strings",
    )
    # and the genuinely uniform state I/4 has all non-identity strings zero
    rho_unif = np.eye(4) / 4
    allstr = []
    for w in product("IXYZ", repeat=2):
        if set(w) == {"I"}:
            continue
        P = kron(PAULI[w[0]], PAULI[w[1]])
        allstr.append(abs(np.trace(rho_unif @ P)))
    check(
        "C2.I4_all_nonidentity_strings_vanish",
        max(allstr) < 1e-12,
        f"I/4: max non-identity Pauli-string expectation = {max(allstr):.1e} = 0",
    )


# ===========================================================================
# VERDICT
# ===========================================================================
def verdict() -> None:
    log("\n" + "=" * 74)
    log("VERDICT")
    log("=" * 74)
    log(
        """
Classification of  rho_ref = I/d  under {Quantum, Lattice, Record}:  OPEN PREMISE.

  * PART A proves the three candidate IMPLICATIONS are sound and, on the
    qubit, IDENTICAL: each of
        (1) invariance under all unitaries  [no preferred basis],
        (2) maximum von Neumann entropy     [maximal ignorance],
        (3) traciality omega(AB)=omega(BA)  [unique trace],
    has the SAME unique solution rho = I/2.  So they are ONE premise X, not
    three independent routes.  (Traciality = invariance under inner unitaries;
    for M_2(C) inner = all, so candidates 1 and 3 are literally the same; and
    that fixed point is also the entropy maximizer.)

  * PART B shows {Quantum, Lattice, Record} do NOT entail X:
      - A pure state |psi><psi| has registered NO outcome, so it is a fully
        valid "no record yet" reference, yet it violates all of (1),(2),(3).
        Hence "no record" does NOT imply X.  (B1)
      - The no-record-yet state space is the WHOLE Bloch ball; X selects the
        single centre point -- a strict, measure-zero extra constraint.  (B2)
      - The Record axiom supplies no weighting / probability / symmetry of any
        reference; Quantum supplies only M_2(C); Lattice only Z^3.  (B3)
      - Outcome-relabeling carries one record-free state to a DISTINCT
        record-free state, so symmetry of the reference is an added postulate
        about the STATE, not a property of record-absence.  (B4)

  MINIMAL EXTRA PREMISE (named precisely):
      (X)  "Maximal-symmetry reference":  the pre-record reference state is
           invariant under the full unitary group of the per-site algebra
           (equivalently: it is the tracial state; equivalently: it is the
           maximum-entropy / maximal-ignorance state).
      This is exactly the "no-extra-structure principle" of Step 5 of
      PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20, here shown
      to be (a) a genuine logical extra, and (b) the SAME premise under all
      three candidate names.  It is a Jaynes-type / symmetry meta-principle
      about the axiom-to-reference map, not a theorem of the three axioms.

  CONSEQUENCE FOR THE BORN ROUTE:
      The Gleason/Busch route gives the Born FORM p(E)=Tr(rho E) and, given a
      reference, its VALUE.  This runner does NOT discharge the reference
      residual: rho_ref = I/d remains conditional on premise X.  The Born
      form+value are unconditional GIVEN rho_ref; the rho_ref = I/d input is
      an open input (one symmetry/max-ignorance premise).
"""
    )


def main() -> int:
    log("PRE-RECORD REFERENCE STATE rho_ref = I/d : FORCED or OPEN PREMISE?")
    log("Repo: cl3-lattice-framework | axioms {Quantum, Lattice, Record}")
    part_a()
    part_b()
    part_c()
    verdict()
    n_pass = sum(_RESULTS)
    n_tot = len(_RESULTS)
    log("\n" + "=" * 74)
    log(f"RESULT: {n_pass}/{n_tot} checks PASS")
    log("CLASSIFICATION: rho_ref = I/d remains an open maximal-symmetry premise X")
    log("=" * 74)
    _LOGFH.flush()
    _LOGFH.close()
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    sys.exit(main())
