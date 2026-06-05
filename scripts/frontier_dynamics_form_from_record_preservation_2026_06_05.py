#!/usr/bin/env python3
"""Frontier check: does composing the two record-corollaries force the dynamics
FORM to the gauge-invariant-local (Wilson) class, leaving only the coupling
admitted?

THE COMPOSITION (the claim under test)
--------------------------------------
Two finite-model results sit upstream:

  * #2667 family / gauge structure (TWO_ENDPOINT_GAUSS_LAW_INVARIANCE...):
    observables = gauge-invariant records; the observable algebra A_inv is the
    commutant of the per-vertex Gauss generators {G_v}.

  * #2701 / dynamics class (RECORD_FORMATION_POINTER_NON_DEMOLITION...):
    record formation forces a transfer step that conserves a pointer/charge and
    is local; necessity is exact via the Heisenberg equation.

Compose them: dynamics must PRESERVE the record/observable algebra (a
time-evolved record is still a gauge-invariant record). For the
transfer/Hamiltonian H this means H maps A_inv -> A_inv, i.e.
[H, G_v] = 0 for all v (H is gauge-covariant). With locality (#2701/Lattice)
and Hermiticity (OS self-adjointness), H is a sum of finite-range
gauge-invariant Hermitian operators.

WHAT IS HONESTLY TARGETED
-------------------------
NOT "the action is derived." The realistic target the framework's own track
record allows ("the action form is hand-added even in quantum-link models") is:

    the dynamics FORM is constrained to the gauge-invariant-local Hermitian
    class, whose leading pure-gauge term is the Wilson plaquette and whose
    leading matter term is the covariant nearest-neighbour hopping (+ on-site
    mass); the COUPLINGS and the lowest-order/minimality truncation are
    admitted, and trivial H = 0 is in the class.

This runner establishes exactly that, on small explicit Z2 and SU(2)/U(1)
lattice gauge systems with link variables + matter qubits.

MEMORY DISCIPLINE
-----------------
Small patches (<= 8 qubits/links), exact dense numpy. Peak RSS capped well
under 2 GB (reported at the end). Output is capped.

Sections (each self-checking, PASS/FAIL):
  S1. Gauge-covariance from record-preservation: [H,G_v]=0 <=> records->records,
      with the violating control (an H with [H,G_v]!=0 maps a gauge-invariant
      observable to a gauge-variant one = not a record).
  S2. Gauge-invariant LOCAL Hermitian operator basis enumeration: plaquette =
      smallest pure-gauge loop; covariant hopping (+ on-site mass) = smallest
      matter term; bare/short objects are NOT in the commutant.
  S3. Record-broadcast -> covariant hopping: the interaction that broadcasts the
      matter pointer/charge gauge-covariantly is the covariant hopping.
  S4. Framework H is the leading element of the forced class (Wilson plaquette +
      covariant staggered hopping + mass).
  S5. Residual ledger (NOT forced): couplings (beta), minimality/truncation,
      trivial H=0 -- demonstrated explicitly.
"""

from __future__ import annotations

import os
import resource
import sys
from itertools import product

import numpy as np

# ----------------------------------------------------------------------------
# bookkeeping
# ----------------------------------------------------------------------------
PASS = 0
FAIL = 0
_FAILED_LABELS: list[str] = []


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        _FAILED_LABELS.append(label)
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


# ----------------------------------------------------------------------------
# single-qubit operators and tensor helpers
# ----------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SP = np.array([[0, 1], [0, 0]], dtype=complex)   # sigma^+ = |0><1|
SM = np.array([[0, 0], [1, 0]], dtype=complex)   # sigma^- = |1><0|
# Convention used throughout: the sigma_z eigenvalue is the U(1) charge
# (|0> -> +1, |1> -> -1). sigma^+ = |0><1| raises sigma_z by +2 (sends the |1>
# component to the |0> component); sigma^- lowers it by 2.


def kron_list(mats: list[np.ndarray]) -> np.ndarray:
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def embed(single: dict[int, np.ndarray], n: int) -> np.ndarray:
    """Embed single-qubit operators (given as {site: 2x2}) into n-qubit space."""
    mats = [single.get(i, I2) for i in range(n)]
    return kron_list(mats)


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def is_zero(a: np.ndarray, atol: float = 1e-10) -> bool:
    return float(np.linalg.norm(a)) < atol


def commutes(a: np.ndarray, b: np.ndarray, atol: float = 1e-10) -> bool:
    return is_zero(comm(a, b), atol)


def is_hermitian(a: np.ndarray, atol: float = 1e-10) -> bool:
    return np.allclose(a, a.conj().T, atol=atol)


# ----------------------------------------------------------------------------
# Pauli-string basis tools (for commutant / algebra dimension)
# ----------------------------------------------------------------------------
def pauli_basis(n: int) -> list[np.ndarray]:
    paulis = [I2, SX, SY, SZ]
    out = []
    for choice in product(range(4), repeat=n):
        out.append(kron_list([paulis[c] for c in choice]))
    return out


def commutant_dim(generators: list[np.ndarray], n: int) -> int:
    """dim of the commutant {X : [X, G]=0 for all G} inside M_{2^n}(C).

    Equivalently 4^n minus the rank of the stacked adjoint maps ad_G on the
    Pauli (Hilbert-Schmidt) basis. Exact.
    """
    basis = pauli_basis(n)
    d = len(basis)  # 4^n
    norm = 2 ** n   # <P,P>_HS = 2^n
    rows = []
    for g in generators:
        ad = np.empty((d, d), dtype=complex)
        for j, right in enumerate(basis):
            cg = comm(g, right)
            for i, left in enumerate(basis):
                ad[i, j] = np.trace(left.conj().T @ cg) / norm
        rows.append(ad)
    stacked = np.vstack(rows)
    rank = int(np.linalg.matrix_rank(stacked, tol=1e-8))
    return d - rank


def in_commutant(op_: np.ndarray, generators: list[np.ndarray]) -> bool:
    return all(commutes(op_, g) for g in generators)


# ----------------------------------------------------------------------------
# SECTION 1
#   Gauge-covariance from record-preservation: [H,G_v]=0 <=> records->records
# ----------------------------------------------------------------------------
def section1() -> None:
    section("S1  Gauge-covariance from record-preservation: [H,G_v]=0 <=> "
            "records map to records")

    # --- Explicit small U(1) lattice gauge patch ----------------------------
    # 4 qubits, same carrier as the TWO_ENDPOINT note so this composes cleanly:
    #   site A (0) - link-end a (1) - link-end b (2) - site B (3)
    # Per-vertex U(1) Gauss generators (a charge at each endpoint vertex):
    #   G_A = sz(A) + sz(a),   G_B = sz(b) + sz(B).
    n = 4
    A, a, b, B = 0, 1, 2, 3
    G_A = embed({A: SZ}, n) + embed({a: SZ}, n)
    G_B = embed({b: SZ}, n) + embed({B: SZ}, n)
    gens = [G_A, G_B]

    # The observable algebra A_inv = commutant of {G_A, G_B}.
    dim_inv = commutant_dim(gens, n)
    record("S1.0 A_inv = commutant({G_v}) is a proper nontrivial subalgebra",
           0 < dim_inv < 4 ** n, f"dim(A_inv)={dim_inv} of {4**n}")
    # cross-check against the upstream TWO_ENDPOINT certificate value 36
    record("S1.0b A_inv dimension matches upstream gauge-structure note (36)",
           dim_inv == 36, f"dim={dim_inv}")

    # A concrete gauge-invariant record O in A_inv (the fully-dressed Wilson
    # line is invariant; pick a Hermitian invariant observable). Use the
    # Hermitian part of the dressed line, plus a manifestly-invariant on-link
    # charge correlator.
    full_line = (embed({A: SM}, n) @ embed({a: SP}, n)
                 @ embed({b: SM}, n) @ embed({B: SP}, n))
    O_inv = full_line + full_line.conj().T            # Hermitian, gauge-invariant
    record("S1.1 chosen O is Hermitian", is_hermitian(O_inv))
    record("S1.1b chosen O is a gauge-invariant record (in A_inv)",
           in_commutant(O_inv, gens))

    # === GAUGE-COVARIANT H (record-preserving candidate) ====================
    # A finite-range gauge-invariant Hermitian H. Use the covariant "hopping"
    # along the chain dressed by the link, which commutes with both G_v.
    H_cov = (embed({A: SM}, n) @ embed({a: SP}, n)
             + embed({A: SP}, n) @ embed({a: SM}, n)      # A<->a covariant
             + embed({b: SM}, n) @ embed({B: SP}, n)
             + embed({b: SP}, n) @ embed({B: SM}, n))     # b<->B covariant
    record("S1.2 gauge-covariant H is Hermitian", is_hermitian(H_cov))
    record("S1.2b gauge-covariant H commutes with every G_v ([H,G_v]=0)",
           commutes(H_cov, G_A) and commutes(H_cov, G_B))

    # Heisenberg-evolve O under H_cov and check it stays in A_inv for several t.
    def heisenberg(H: np.ndarray, O: np.ndarray, t: float) -> np.ndarray:
        # exact matrix exponential via eigardecomposition (H Hermitian)
        w, V = np.linalg.eigh(H)
        U = V @ np.diag(np.exp(1j * w * t)) @ V.conj().T
        return U @ O @ U.conj().T

    stays_inv = all(
        in_commutant(heisenberg(H_cov, O_inv, t), gens)
        for t in (0.13, 0.37, 0.8, 1.6, 2.9)
    )
    record("S1.3 covariant H: Heisenberg-evolved record STAYS a record "
           "(O(t) in A_inv for all t)", stays_inv)

    # Derivative-level test: d/dt O(t)|0 = i[H,O] must itself be in A_inv.
    dO = 1j * comm(H_cov, O_inv)
    record("S1.3b covariant H: dO/dt = i[H,O] is in A_inv (record stays a "
           "record infinitesimally)", in_commutant(dO, gens))

    # === DEMOLITION CONTROL: an H with [H,G_v] != 0 ========================
    # Bare (undressed) hopping that violates the Gauss law at a vertex; a single
    # sigma_x on site A also works as the minimal violator.
    H_bad = embed({A: SX}, n) + embed({B: SX}, n)        # local, Hermitian
    record("S1.4 control H_bad is Hermitian and local", is_hermitian(H_bad))
    record("S1.4b control H_bad does NOT commute with the Gauss generators "
           "([H_bad,G_v]!=0)",
           (not commutes(H_bad, G_A)) or (not commutes(H_bad, G_B)))

    # Under H_bad, a gauge-invariant record evolves OUT of A_inv (it becomes
    # gauge-variant = not a record). Show at the derivative level (clean) AND at
    # finite t.
    dO_bad = 1j * comm(H_bad, O_inv)
    record("S1.5 control: dO/dt = i[H_bad,O] LEAVES A_inv "
           "(record maps to a gauge-VARIANT operator)",
           not in_commutant(dO_bad, gens))
    leaves_inv = any(
        not in_commutant(heisenberg(H_bad, O_inv, t), gens)
        for t in (0.2, 0.5, 1.0)
    )
    record("S1.5b control: finite-t evolved O(t) is gauge-VARIANT (not a "
           "record)", leaves_inv)

    # === THE EQUIVALENCE, exact, over RANDOM local Hermitian H =============
    # Claim: for Hermitian H, [H maps A_inv -> A_inv at the derivative level for
    # ALL O in A_inv] <=> [H, G_v] = 0 for all v.
    #
    # Proof of the nontrivial direction operationally: A_inv = commutant(M)
    # where M = algebra generated by {G_v}. The map O -> i[H,O] preserves the
    # commutant of M (for ALL O in the commutant). Sufficiency is immediate:
    # if [H,G_v]=0 then H in A_inv = M', and M' is a *-algebra (closed under the
    # commutator), so ad_H(A_inv) subset A_inv. Necessity is the nontrivial
    # direction: must ad_H preserving A_inv force H in A_inv (i.e. [H,G_v]=0),
    # or could there be a strictly larger "normalizer" of Hermitians that
    # preserve A_inv without being in it?
    #
    # We settle this EXACTLY (theorem-level, not by sampling) below in S1.7 via a
    # dimension count: we solve the linear system {Hermitian H : ad_H(O) in
    # A_inv for all O in A_inv} and compare dim to dim(A_inv). They are EQUAL
    # (no normalizer slack), so for this model
    #     ad_H preserves A_inv  <=>  H in A_inv  <=>  [H,G_v]=0,
    # which is exactly "records evolve to records <=> H gauge-covariant".
    basis_inv = _commutant_basis(gens, n)         # spanning set of A_inv
    rng = np.random.default_rng(20260605)

    def preserves_Ainv(H: np.ndarray) -> bool:
        # i[H,O] in A_inv for every O in a spanning set of A_inv  <=>  H
        # preserves A_inv at the derivative level.
        for O in basis_inv:
            if not in_commutant(1j * comm(H, O), gens):
                return False
        return True

    suff_ok = 0
    nec_ok = 0
    TRIALS = 40
    for _ in range(TRIALS):
        # random gauge-covariant Hermitian H (built from A_inv basis) -> should
        # preserve A_inv.
        coeffs = rng.normal(size=len(basis_inv))
        H_inv = sum(c * O for c, O in zip(coeffs, basis_inv))
        H_inv = H_inv + H_inv.conj().T
        if commutes(H_inv, G_A) and commutes(H_inv, G_B) and preserves_Ainv(H_inv):
            suff_ok += 1
        # random general local Hermitian H -> preserves A_inv  <=> [H,G_v]=0.
        M = rng.normal(size=(2 ** n, 2 ** n)) + 1j * rng.normal(size=(2 ** n, 2 ** n))
        H_gen = M + M.conj().T
        gauge_cov = commutes(H_gen, G_A) and commutes(H_gen, G_B)
        pres = preserves_Ainv(H_gen)
        if gauge_cov == pres:
            nec_ok += 1

    record("S1.6 sufficiency over random gauge-covariant H: all preserve A_inv",
           suff_ok == TRIALS, f"{suff_ok}/{TRIALS}")
    record("S1.6b equivalence over random general Hermitian H: "
           "(preserves A_inv) <=> ([H,G_v]=0)",
           nec_ok == TRIALS, f"{nec_ok}/{TRIALS}")

    # === S1.7  EXACT theorem-level certificate of the equivalence ===========
    # Solve {Hermitian H : ad_H(A_inv) subset A_inv} as a real linear system in
    # the full Pauli basis and compare its dimension to dim(A_inv). Equality =
    # "no normalizer slack" = the necessity direction is a THEOREM on this model.
    #
    # WHY equality is expected (not luck), for honesty: A_inv = M' is a finite-
    # dimensional von Neumann algebra containing the identity. Every derivation
    # of a finite-dim vN algebra is INNER, so ad_H restricted to A_inv equals
    # ad_h for some h in A_inv; then ad_{H-h} kills all of A_inv, i.e. H-h lies
    # in the center of B(H) (the commutant of A_inv together with... ) = C*I.
    # Hence H in A_inv + C*I = A_inv (since I in A_inv). So
    # {Hermitian H : ad_H preserves A_inv} = Hermitian part of A_inv, exactly.
    # We still scope the NOTE as bounded on this explicit finite carrier, per
    # repo convention; the dimension count is the relocation-resistant witness.
    full_basis = pauli_basis(n)                       # 256 Hermitian Pauli strings
    comp_basis = [P for P in full_basis
                  if not in_commutant(P, gens)]       # complement of A_inv
    norm = 2 ** n

    def hs(x: np.ndarray, y: np.ndarray) -> complex:
        return np.trace(x.conj().T @ y) / norm

    rows = []
    for O in basis_inv:                               # for each O in A_inv
        for C in comp_basis:                          # require <C,[P_k,O]>=0
            rows.append([hs(C, comm(P, O)) for P in full_basis])
    Mmat = np.array(rows, dtype=complex)
    Mr = np.vstack([Mmat.real, Mmat.imag])            # real coeffs (Hermitian H)
    rank = int(np.linalg.matrix_rank(Mr, tol=1e-8)) if Mmat.size else 0
    preserving_dim = len(full_basis) - rank
    record("S1.7 EXACT: dim{Hermitian H : ad_H preserves A_inv} == dim(A_inv) "
           "(no normalizer slack => necessity is a theorem)",
           preserving_dim == len(basis_inv),
           f"preserving_dim={preserving_dim}, dim(A_inv)={len(basis_inv)}")
    record("S1.7b EXACT: hence ad_H preserves A_inv  <=>  H in A_inv  <=>  "
           "[H,G_v]=0 (records->records <=> gauge-covariant)",
           preserving_dim == len(basis_inv))

    # === S1.7c  EXHAUSTIVE cross-check on a full Hermitian basis =============
    # The two predicates (preserves A_inv) and ([P,G_v]=0) must AGREE on every
    # Pauli string (a full Hermitian basis); since both are linear conditions on
    # H, agreement on a basis = agreement everywhere. This is an independent,
    # enumeration-based witness of the same equivalence (no rank tolerance).
    disagree = 0
    for P in full_basis:
        gauge_cov = in_commutant(P, gens)
        pres = preserves_Ainv(P)
        if gauge_cov != pres:
            disagree += 1
    record("S1.7c EXHAUSTIVE: (preserves A_inv) == ([P,G_v]=0) on ALL "
           f"{len(full_basis)} Pauli strings (full Hermitian basis)",
           disagree == 0, f"disagreements={disagree}")


def _commutant_basis(generators: list[np.ndarray], n: int) -> list[np.ndarray]:
    """Return a spanning set (Pauli strings) of the commutant of the
    generators. Sufficient as a spanning set for the derivative-level test."""
    basis = pauli_basis(n)
    out = [P for P in basis if all(commutes(P, g) for g in generators)]
    return out


# ----------------------------------------------------------------------------
# SECTION 2
#   Gauge-invariant LOCAL Hermitian operator basis: plaquette = smallest loop;
#   covariant hopping (+ mass) = smallest matter term; short objects excluded.
# ----------------------------------------------------------------------------
def section2() -> None:
    section("S2  Gauge-invariant LOCAL Hermitian basis: plaquette smallest "
            "loop; covariant hopping smallest matter term")

    # ----- Z2 lattice gauge theory on a single plaquette --------------------
    # The cleanest fully-discrete gauge model. Sites at the 4 corners of a unit
    # square; a Z2 gauge spin on each of the 4 edges. Matter Z2 charge on each
    # corner site.
    #
    #   site0 --l01-- site1
    #     |             |
    #   l30           l12
    #     |             |
    #   site3 --l23-- site2
    #
    # CONVENTIONS (standard Z2 LGT, Kogut-Susskind / Fradkin-Shenker):
    #   * link "gauge field" operator = sigma_z(link); the plaquette (magnetic)
    #     operator is the product of sigma_z around the loop.
    #   * link "electric field" operator = sigma_x(link) (flips the gauge field).
    #   * matter "field" at a site = sigma_z(site); the matter charge-parity
    #     (number) operator = sigma_x(site).
    #   * Gauss-law generator at site s (the local gauge transformation):
    #         G_s = sigma_x(site_s) * prod_{l ~ s} sigma_x(l).
    #     By  sigma_x sigma_z sigma_x = -sigma_z, conjugation by G_s flips the
    #     SIGN of the matter field sigma_z(s) and of the incident link fields
    #     sigma_z(l) -- exactly a local Z2 gauge transformation. A term is
    #     gauge-invariant iff it COMMUTES with every G_s.
    #
    # The gauge field (sigma_z) and the gauge generator (sigma_x products) live
    # in DIFFERENT Pauli directions, so commutation is nontrivial (no degeneracy)
    # -- a term is invariant iff it shares an EVEN number of sites with each G_s
    # in the conjugate (sigma_z) direction.
    #
    # We use 4 sites + 4 links = 8 qubits.
    n = 8
    s0, s1, s2, s3 = 0, 1, 2, 3
    l01, l12, l23, l30 = 4, 5, 6, 7
    inc = {s0: (l01, l30), s1: (l01, l12), s2: (l12, l23), s3: (l23, l30)}

    def Gauss_Z2(site: int) -> np.ndarray:
        single = {site: SX}                  # flip matter field sign
        for l in inc[site]:
            single[l] = SX                   # flip incident link field sign
        return embed(single, n)

    G = {s: Gauss_Z2(s) for s in (s0, s1, s2, s3)}
    gens = list(G.values())
    record("S2.0 (Z2) Gauss generators mutually commute",
           all(commutes(G[i], G[j]) for i in G for j in G))

    # --- smallest PURE-GAUGE invariant: the plaquette -----------------------
    # The plaquette is the product of the gauge-field (sigma_z) variables around
    # the square. Each site touches exactly 2 of the 4 plaquette links, so each
    # G_s anticommutes an EVEN number (2) of times -> the plaquette commutes.
    plaquette = (embed({l01: SZ}, n) @ embed({l12: SZ}, n)
                 @ embed({l23: SZ}, n) @ embed({l30: SZ}, n))
    record("S2.1 plaquette is Hermitian", is_hermitian(plaquette))
    record("S2.1b plaquette (smallest closed loop) is gauge-invariant "
           "([plaq,G_s]=0)", in_commutant(plaquette, gens))

    # smaller pure-gauge candidates are NOT invariant (open lines):
    single_link = embed({l01: SZ}, n)            # one link gauge field
    two_link_open = embed({l01: SZ}, n) @ embed({l12: SZ}, n)  # open 2-link path
    record("S2.2 single link gauge field is NOT gauge-invariant "
           "(no smaller pure-gauge loop)",
           not in_commutant(single_link, gens))
    record("S2.2b open two-link path is NOT gauge-invariant (an OPEN line is "
           "not a record)", not in_commutant(two_link_open, gens))
    # the link "electric" energy sigma_x(link) is on-link & invariant; it is the
    # conjugate (electric) term, also in the class but NOT a Wilson loop.
    elec = embed({l01: SX}, n)
    record("S2.2c on-link electric term sigma_x(link) is gauge-invariant "
           "(allowed local term, the conjugate/electric energy)",
           in_commutant(elec, gens))

    # --- smallest MATTER invariant: covariant hopping (+ on-site mass) ------
    # Covariant hopping along link l01 between sites s0,s1: the matter field at
    # the two endpoints tied together by the link gauge field. The gauge-
    # covariant nearest-neighbour hopping is
    #     sigma_z(s0) * sigma_z(l01) * sigma_z(s1)
    # (the link variable Wilson-connects the two endpoint matter fields). G_{s0}
    # anticommutes with sigma_z(s0) AND with sigma_z(l01) = 2 (even) -> commutes.
    hop = embed({s0: SZ}, n) @ embed({l01: SZ}, n) @ embed({s1: SZ}, n)
    record("S2.3 covariant nearest-neighbour hopping is Hermitian",
           is_hermitian(hop))
    record("S2.3b covariant hopping (smallest matter term) is gauge-invariant",
           in_commutant(hop, gens))

    # on-site mass / charge-parity term: sigma_x(site) is invariant (it commutes
    # with its own G_s = sigma_x(s)... and with the link sigma_x factors).
    mass = embed({s0: SX}, n)
    record("S2.4 on-site mass (charge-parity) sigma_x(site) is gauge-invariant",
           in_commutant(mass, gens))

    # smaller / undressed matter candidates are NOT invariant:
    bare_charge_flip = embed({s0: SZ}, n)        # bare matter field, no link
    bare_hop = embed({s0: SZ}, n) @ embed({s1: SZ}, n)   # hop w/o the link
    record("S2.5 bare on-site matter field sigma_z(site) is NOT gauge-invariant",
           not in_commutant(bare_charge_flip, gens))
    record("S2.5b UNdressed hop sigma_z(s0)sigma_z(s1) (no link) is NOT "
           "gauge-invariant -> dressing by the link is FORCED",
           not in_commutant(bare_hop, gens))

    # --- range ordering: plaquette < larger loop; nn-hop < longer path ------
    # A larger (2x1) loop needs 6 links; a longer matter path needs 2 links.
    # On this single-plaquette patch we certify the *ordering principle*: the
    # plaquette uses 4 link factors (the minimum to close a loop on Z^2/Z^3),
    # the nn-hop uses 1 link factor (the minimum to connect two sites). Larger
    # invariants are strictly higher operator-range. We verify the COUNTS.
    def support_size(op_: np.ndarray, n_: int) -> int:
        # number of sites where op acts nontrivially (support of the Pauli
        # string). Works because all S2 operators are single Pauli strings.
        cnt = 0
        for site in range(n_):
            red = _reduced_acts_nontrivially(op_, site, n_)
            if red:
                cnt += 1
        return cnt

    record("S2.6 plaquette support = 4 links (minimal closed loop on a cubic "
           "lattice)", support_size(plaquette, n) == 4,
           f"support={support_size(plaquette, n)}")
    record("S2.6b covariant nn-hop support = 3 (two sites + one connecting "
           "link = minimal matter term)", support_size(hop, n) == 3,
           f"support={support_size(hop, n)}")
    record("S2.6c on-site mass support = 1 (minimal matter on-site term)",
           support_size(mass, n) == 1)

    # ----- SU(2)/U(1) cross-check of the loop/hopping invariance -----------
    _section2_continuous()


def _reduced_acts_nontrivially(op_: np.ndarray, site: int, n: int) -> bool:
    """True if op_ acts nontrivially on `site` (op_ is a single Pauli string /
    product). Tests by checking commutation with sigma_z and sigma_x on the
    site: a Pauli string is trivial on a site iff it commutes with BOTH."""
    sz = embed({site: SZ}, n)
    sx = embed({site: SX}, n)
    return not (commutes(op_, sz) and commutes(op_, sx))


def _section2_continuous() -> None:
    """SU(2)/U(1) cross-check that the same hierarchy holds with genuine
    non-abelian link variables (here on the TWO_ENDPOINT 4-qubit carrier with
    SU(2) endpoint generators, matching the upstream note)."""
    n = 4
    A, a, b, B = 0, 1, 2, 3
    # SU(2) endpoint generators (spin-sum at each vertex), as in the upstream
    # note.
    SAi = tuple((embed({A: s}, n) + embed({a: s}, n)) / 2 for s in (SX, SY, SZ))
    SBi = tuple((embed({b: s}, n) + embed({B: s}, n)) / 2 for s in (SX, SY, SZ))
    gens = list(SAi) + list(SBi)

    # double-singlet Wilson-type invariant (closed, dressed at both ends).
    singlet = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    sp = np.outer(singlet, singlet.conj())
    wilson_type = np.kron(sp, sp)          # invariant at both endpoints
    record("S2.7 (SU2) double-singlet Wilson-type observable is invariant at "
           "both endpoints", in_commutant(wilson_type, gens))

    # bare link transport variant at both ends (no smaller invariant).
    bare = embed({a: SP}, n) @ embed({b: SM}, n)
    record("S2.7b (SU2) bare link transport is NOT invariant (no smaller "
           "invariant than the dressed loop)", not in_commutant(bare, gens))


# ----------------------------------------------------------------------------
# SECTION 3
#   Record-broadcast -> covariant hopping
# ----------------------------------------------------------------------------
def section3() -> None:
    section("S3  Record-broadcast -> covariant hopping: the gauge-covariant "
            "charge-broadcasting interaction IS the covariant hopping")

    # Physical content (connecting to #2701 record-formation): the matter
    # record is the matter pointer/charge. To BROADCAST it gauge-covariantly,
    # the interaction must (a) be gauge-invariant ([H_int,G_v]=0), (b) move
    # matter charge between a site and its neighbourhood while CONSERVING total
    # charge, and (c) carry the charge along the gauge link (so the broadcast is
    # of the *gauge-invariant* record, not a gauge-variant one). The unique
    # leading local operator with these properties is the covariant hopping
    # chi-bar U chi.
    #
    # We use the SAME two-link-end U(1) carrier as S1 and the upstream
    # TWO_ENDPOINT note (4 qubits): matter A (0), link-ends a (1), b (2), matter
    # B (3). Per-vertex U(1) Gauss generators G_A = sz(A)+sz(a),
    # G_B = sz(b)+sz(B). Total U(1) charge Q = sum of sz.
    n = 4
    A, a, b, B = 0, 1, 2, 3
    G_A = embed({A: SZ}, n) + embed({a: SZ}, n)
    G_B = embed({b: SZ}, n) + embed({B: SZ}, n)
    gens = [G_A, G_B]
    Q = sum(embed({q: SZ}, n) for q in (A, a, b, B))   # total U(1) charge

    # candidate broadcasting interactions (all local, Hermitian):
    # (i) covariant hopping = the fully dressed Wilson line chi-bar(A) U(a,b)
    #     chi(B) + h.c.:  sigma^-(A) sigma^+(a) sigma^-(b) sigma^+(B) + h.c.
    #     Charge raised at a,B and lowered at A,b; each Gauss vertex stays
    #     balanced (G_A: -2 at A, +2 at a = 0; G_B: -2 at b, +2 at B = 0).
    hop = (embed({A: SM}, n) @ embed({a: SP}, n)
           @ embed({b: SM}, n) @ embed({B: SP}, n))
    hop = hop + hop.conj().T
    # (ii) bare hop (no link dressing): sigma^-(A) sigma^+(B) + h.c. -- conserves
    #      total Q but is NOT gauge-covariant (does not transport along the link;
    #      unbalanced at each vertex).
    bare_hop = embed({A: SM}, n) @ embed({B: SP}, n)
    bare_hop = bare_hop + bare_hop.conj().T
    # (iii) on-site charge non-conserving flip: sigma_x(A) -- breaks Q.
    flip = embed({A: SX}, n)

    record("S3.1 covariant hopping conserves total U(1) charge ([H,Q]=0)",
           commutes(hop, Q))
    record("S3.1b covariant hopping is gauge-invariant ([H,G_v]=0) -> it "
           "broadcasts a *gauge-invariant* record", in_commutant(hop, gens))

    record("S3.2 bare hop conserves charge but is NOT gauge-covariant "
           "(broadcasts a gauge-VARIANT quantity = not a record)",
           commutes(bare_hop, Q) and not in_commutant(bare_hop, gens))
    record("S3.3 on-site flip does NOT even conserve charge (cannot broadcast "
           "a conserved record)", not commutes(flip, Q))

    # The broadcasting property: the dressed hop connects the two configs
    #   |A=0,a=1,b=0,B=1>  <->  |A=1,a=0,b=1,B=0>
    # (forward term sigma^-(A)sigma^+(a)sigma^-(b)sigma^+(B) maps the first to
    # the second). Starting in the first, the covariant hop spreads charge along
    # the link (local <sz(A)> moves) while the TOTAL charge (the record) is
    # fixed.
    psi0 = np.zeros(2 ** n, dtype=complex)
    psi0[_basis_index([0, 1, 0, 1])] = 1.0

    def evolve(H: np.ndarray, psi: np.ndarray, t: float) -> np.ndarray:
        w, V = np.linalg.eigh(H)
        U = V @ np.diag(np.exp(-1j * w * t)) @ V.conj().T
        return U @ psi

    psi_t = evolve(hop, psi0, 0.7)
    Q_init = float(np.real(psi0.conj() @ Q @ psi0))
    Q_fin = float(np.real(psi_t.conj() @ Q @ psi_t))
    szA = embed({A: SZ}, n)
    locA_init = float(np.real(psi0.conj() @ szA @ psi0))
    locA_fin = float(np.real(psi_t.conj() @ szA @ psi_t))
    record("S3.4 broadcast: TOTAL charge (the record) is conserved under "
           "covariant hop", abs(Q_init - Q_fin) < 1e-9,
           f"Q:{Q_init:.6f}->{Q_fin:.6f}")
    record("S3.4b broadcast: charge actually SPREADS along the link "
           "(local <sz(A)> moves) -> the record is copied via the connection",
           not np.isclose(locA_fin, locA_init),
           f"<sz(A)>:{locA_init:.4f}->{locA_fin:.4f}")


def _basis_index(bits: list[int]) -> int:
    """Index into the kron(|.>) basis for given qubit bit values (qubit 0 is the
    most significant, matching numpy.kron ordering; |0>=[1,0], |1>=[0,1])."""
    idx = 0
    for b in bits:
        idx = idx * 2 + b
    return idx


# ----------------------------------------------------------------------------
# SECTION 4
#   Framework H is the leading element of the forced class
# ----------------------------------------------------------------------------
def section4() -> None:
    section("S4  Framework H (Wilson plaquette + covariant staggered hopping + "
            "mass) is the LEADING element of the forced class")

    # Reassemble the framework's leading gauge-matter Hamiltonian on the Z2
    # single-plaquette + 4-site carrier and certify every term is
    # gauge-invariant, Hermitian, local, and that this is exactly
    # {smallest loop} + {smallest matter term} + {on-site mass}.
    n = 8
    s0, s1, s2, s3 = 0, 1, 2, 3
    l01, l12, l23, l30 = 4, 5, 6, 7
    inc = {s0: (l01, l30), s1: (l01, l12), s2: (l12, l23), s3: (l23, l30)}

    def Gauss_Z2(site: int) -> np.ndarray:
        single = {site: SX}
        for l in inc[site]:
            single[l] = SX
        return embed(single, n)

    gens = [Gauss_Z2(s) for s in (s0, s1, s2, s3)]

    # corrected Z2 conventions (gauge field = sigma_z, charge-parity = sigma_x):
    plaq = (embed({l01: SZ}, n) @ embed({l12: SZ}, n)
            @ embed({l23: SZ}, n) @ embed({l30: SZ}, n))
    hop01 = embed({s0: SZ}, n) @ embed({l01: SZ}, n) @ embed({s1: SZ}, n)
    hop12 = embed({s1: SZ}, n) @ embed({l12: SZ}, n) @ embed({s2: SZ}, n)
    hop23 = embed({s2: SZ}, n) @ embed({l23: SZ}, n) @ embed({s3: SZ}, n)
    hop30 = embed({s3: SZ}, n) @ embed({l30: SZ}, n) @ embed({s0: SZ}, n)
    mass = sum(embed({s: SX}, n) for s in (s0, s1, s2, s3))         # charge-parity
    elec = sum(embed({l: SX}, n) for l in (l01, l12, l23, l30))     # electric energy

    # The leading framework Hamiltonian (couplings beta, kappa, m, g as free
    # positive numbers -- they are the residual, see S5):
    beta, kappa, mfrac, gfrac = 6.0, 1.0, 0.3, 1.0
    H_frame = (-beta * plaq
               - kappa * (hop01 + hop12 + hop23 + hop30)
               + mfrac * mass
               + gfrac * elec)

    record("S4.1 framework H is Hermitian", is_hermitian(H_frame))
    record("S4.2 framework H is gauge-invariant ([H,G_s]=0 for all s)",
           in_commutant(H_frame, gens))
    # term-by-term membership in the forced class:
    for name, term in [("plaquette", plaq), ("hop01", hop01), ("hop12", hop12),
                       ("hop23", hop23), ("hop30", hop30), ("mass", mass),
                       ("electric", elec)]:
        record(f"S4.3 framework term '{name}' is in the gauge-invariant-local "
               f"Hermitian class", is_hermitian(term) and in_commutant(term, gens))

    # leading = smallest in each channel: pure-gauge leading term = plaquette
    # (support 4 = minimal loop); matter leading term = nn covariant hop
    # (support 3 = minimal); on-site mass support 1. Higher terms (2x1 loop,
    # next-nn hop) are strictly higher range and absent at leading order.
    def support_size(op_: np.ndarray) -> int:
        return sum(_reduced_acts_nontrivially(op_, s, n) for s in range(n))

    record("S4.4 pure-gauge leading term is the plaquette (support 4)",
           support_size(plaq) == 4)
    record("S4.4b matter leading term is the nn covariant hop (support 3)",
           support_size(hop01) == 3)
    record("S4.5 the framework H is built ONLY from leading-range invariants "
           "(plaquette + nn-hop + on-site) -> it is the leading element of the "
           "forced class",
           support_size(plaq) == 4 and support_size(hop01) == 3
           and support_size(mass) == 4)  # mass = sum of 4 on-site (each supp 1)


# ----------------------------------------------------------------------------
# SECTION 5
#   Residual ledger: what is NOT forced
# ----------------------------------------------------------------------------
def section5() -> None:
    section("S5  Residual ledger (NOT forced): couplings (beta) + "
            "minimality/truncation + trivial H=0")

    n = 8
    s0, s1, s2, s3 = 0, 1, 2, 3
    l01, l12, l23, l30 = 4, 5, 6, 7
    inc = {s0: (l01, l30), s1: (l01, l12), s2: (l12, l23), s3: (l23, l30)}

    def Gauss_Z2(site: int) -> np.ndarray:
        single = {site: SX}
        for l in inc[site]:
            single[l] = SX
        return embed(single, n)

    gens = [Gauss_Z2(s) for s in (s0, s1, s2, s3)]
    plaq = (embed({l01: SZ}, n) @ embed({l12: SZ}, n)
            @ embed({l23: SZ}, n) @ embed({l30: SZ}, n))
    hop01 = embed({s0: SZ}, n) @ embed({l01: SZ}, n) @ embed({s1: SZ}, n)
    mass = sum(embed({s: SX}, n) for s in (s0, s1, s2, s3))

    # (i) COUPLINGS not forced: any positive beta gives an equally valid
    #     member of the class.
    couplings_ok = all(
        in_commutant(-beta * plaq - kappa * hop01 + m * mass, gens)
        and is_hermitian(-beta * plaq - kappa * hop01 + m * mass)
        for (beta, kappa, m) in [(6.0, 1.0, 0.3), (1.0, 0.5, 2.0),
                                 (12.0, 3.0, 0.0), (0.01, 0.01, 0.01)]
    )
    record("S5.1 RESIDUAL: the COUPLINGS (beta, kappa, m) are NOT forced -- "
           "every choice yields a valid class member", couplings_ok)

    # (ii) MINIMALITY/TRUNCATION not forced: a larger loop / longer matter path
    #      is ALSO gauge-invariant-local Hermitian; nothing in {covariance,
    #      locality, Hermiticity} excludes adding it. Demonstrate with the
    #      "electric" term and an adjoint/doubled-plaquette-like invariant.
    elec = embed({l01: SX}, n)
    # a genuinely different higher invariant: product of two adjacent covariant
    # hops (a longer matter path s0->s1->s2, still gauge-invariant). The shared
    # site s1 appears twice (sigma_z(s1)^2 = I), so this is the dressed line
    # sigma_z(s0) sigma_z(l01) sigma_z(l12) sigma_z(s2).
    long_matter = hop01 @ (embed({s1: SZ}, n) @ embed({l12: SZ}, n)
                           @ embed({s2: SZ}, n))
    record("S5.2 RESIDUAL: minimality/truncation NOT forced -- the on-link "
           "electric term is an admissible extra local invariant",
           is_hermitian(elec) and in_commutant(elec, gens))
    record("S5.2b RESIDUAL: a LONGER matter path (s0->s1->s2) is ALSO a valid "
           "gauge-invariant-local term -> 'only the plaquette/nn-hop' is a "
           "truncation choice, not forced",
           is_hermitian(long_matter) and in_commutant(long_matter, gens))

    # (iii) TRIVIAL H=0 in the class: gauge + locality + Hermiticity do NOT
    #       force nontrivial dynamics.
    H0 = np.zeros((2 ** n, 2 ** n), dtype=complex)
    record("S5.3 RESIDUAL: trivial H=0 is in the class (gauge+locality+"
           "Hermiticity do not force nontrivial dynamics)",
           is_hermitian(H0) and in_commutant(H0, gens))

    # Summary statement of what IS forced vs NOT.
    print("\n  --- RESIDUAL LEDGER (explicit) ---")
    print("  FORCED by {record-preservation (#2667) + locality (#2701) + "
          "Hermiticity}:")
    print("    * H is gauge-covariant: [H,G_v]=0 (records evolve to records).")
    print("    * H is a sum of FINITE-RANGE gauge-invariant Hermitian terms.")
    print("    * the BASIS of allowed local terms: closed Wilson loops "
          "(leading=plaquette),")
    print("      covariant matter paths (leading=nn hopping), on-site mass, "
          "on-link electric.")
    print("    => the dynamics FORM lies in the gauge-invariant-local class, "
          "with the")
    print("       Wilson plaquette + covariant hopping + mass as the LEADING "
          "terms.")
    print("  NOT forced (the residual / admissions):")
    print("    * the COUPLINGS (beta / g_bare, kappa, m, relative weights) -- "
          "any values.")
    print("    * MINIMALITY / lowest-order TRUNCATION (why ONLY plaquette+nn, "
          "not + larger")
    print("      loops / longer paths) -- larger invariants are equally "
          "admissible.")
    print("    * NONtriviality: H=0 is in the class; dynamics need not be "
          "nonzero.")
    print("  RECONCILES WITH 'action hand-added': the FORM-CLASS is forced; "
          "the specific")
    print("    action (Wilson vs heat-kernel vs Manton; the coupling; the "
          "truncation) is")
    print("    NOT -- exactly the BRIDGE_GAP_ACTION_FORM_UNIQUENESS no-go, "
          "which lives")
    print("    ENTIRELY INSIDE this forced class (all 3 candidates are "
          "gauge-invariant-local).")


# ----------------------------------------------------------------------------
# SECTION 6
#   Note firewall: confirm the companion note carries the honest non-claims.
# ----------------------------------------------------------------------------
def section6_firewall() -> None:
    section("S6  Companion-note firewall: the honest non-claims are present")
    from pathlib import Path
    note = (Path(__file__).resolve().parents[1] / "docs"
            / "DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_"
              "CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md")
    if not note.exists():
        record("S6.0 companion note exists", False, str(note))
        return
    record("S6.0 companion note exists", True)
    text = note.read_text(encoding="utf-8")
    for phrase in [
        "does **not** derive the action",
        "says **nothing** about\n  `beta = 6`",
        "does **not** force minimality",
        "does **not** force non-trivial dynamics",
        "the dynamics **form-class**",
        "inside** the gauge-invariant-local class",
    ]:
        record(f"S6 firewall present: {phrase[:48].strip()}...",
               phrase in text)


# ----------------------------------------------------------------------------
def main() -> int:
    print("=" * 74)
    print("FRONTIER: dynamics FORM from record-preservation "
          "(gauge-invariant-local / Wilson class)")
    print("composition: #2667 gauge structure  x  #2701 record-formation "
          "dynamics class")
    print("=" * 74)

    section1()
    section2()
    section3()
    section4()
    section5()
    section6_firewall()

    section("SELF-CHECK SUMMARY")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if _FAILED_LABELS:
        print("FAILED LABELS:")
        for lab in _FAILED_LABELS:
            print(f"  - {lab}")

    # peak RSS
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes; Linux reports KiB.
    if sys.platform == "darwin":
        peak_mb = ru / (1024 * 1024)
    else:
        peak_mb = ru / 1024
    print(f"PEAK_RSS_MB: {peak_mb:.1f}")

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
