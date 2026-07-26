#!/usr/bin/env python3
"""Cycle 709 - what A2's missing bridge theorem actually is.

The critical root row `gravity_full_self_consistency_note` carries the gap:

    "missing_bridge_theorem: supply a retained derivation of `L^{-1} = G_0`
     from the accepted framework premises"

This runner does not supply it. It identifies it, exactly, and shows why the
route as posed cannot close.

Setup, all inside the SUPPLIED range-1 proper-cubic covariant family
(landed classification: L = A*I + B*Delta):

    A_adj      the nearest-neighbour adjacency operator on the Z^3 torus
    Delta      = A_adj - 6I          (lattice Laplacian, coordination 6)
    H(mu)      = mu*I - A_adj        (one-body diagonal mu, hopping -A_adj)
    G(E)       = (H - E)^{-1}        (the matter resolvent at reference energy E)

A2 generalized to the resolvent reads `L^{-1} = G(E)`, hence `L = H - E`, hence

    A = mu - 6 - E,     B = -1.

So A2 as written (`G_0 = H^{-1}`, i.e. E = 0, with mu = 6) is exactly the
statement `A = 0`. Two readings of the same one number:

    A = mu - 6   the on-site term minus the coordination number
    A = -E       minus the resolvent's reference energy

and `min spec(L) = A` makes A the mass gap of the field operator, which fixes
the force range at 1/sqrt(A). Meanwhile a landed note records that shifting H
by a multiple of the identity "has no observable effect because it contributes
only a global phase". A2 therefore carries an unobservable input to an
observable output.

Rows:

  R1  Delta = A_adj - 6I and H(mu) = (mu-6)I - Delta, so A = mu - 6, exact
  R2  A2 on the resolvent gives A = mu - 6 - E, exact
  R3  min spec(L) = A exactly: A is the mass gap, hence observable
  R4  the energy-origin shift is spectrally pure: identical eigenvectors,
      identical gaps, unitary for every mu -- no observable consequence
  R5  mu = 6 <=> zero row sums <=> H annihilates the uniform state
  R6  the discriminator: zero row sums are FORCED for a Markov generator
      (probability conservation) and NOT forced for a self-adjoint quantum
      Hamiltonian (unitary for every mu)
  R7  the band of L is [A, A+12]; A = 0 is where its bottom touches zero,
      with the finite-torus caveat exhibited rather than hidden
  R8  finite-volume corollary: at A = 0 the field equation needs a zero-mean
      source, which a non-negative record density cannot supply
"""

from fractions import Fraction
from itertools import product

FAILURES = []
PASSES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASSES if ok else FAILURES).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# lattice operators, exact
# ---------------------------------------------------------------------------

COORD = 6  # nearest-neighbour coordination number of Z^3


def adjacency(L):
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    A = [[Fraction(0)] * n for _ in range(n)]
    for s in sites:
        i = idx[s]
        for ax in range(3):
            for d in (1, -1):
                t = list(s)
                t[ax] = (t[ax] + d) % L
                A[i][idx[tuple(t)]] += 1
    return A, sites, idx


def laplacian(L):
    """Delta = A_adj - 6I."""
    A, sites, idx = adjacency(L)
    n = len(sites)
    D = [[A[i][j] - (COORD if i == j else 0) for j in range(n)] for i in range(n)]
    return D, sites, idx


def H_of_mu(L, mu):
    """H(mu) = mu*I - A_adj."""
    A, sites, idx = adjacency(L)
    n = len(sites)
    return [[(mu if i == j else Fraction(0)) - A[i][j] for j in range(n)]
            for i in range(n)], sites, idx


def add(M, N):
    return [[M[i][j] + N[i][j] for j in range(len(M))] for i in range(len(M))]


def scal(c, M):
    return [[c * M[i][j] for j in range(len(M))] for i in range(len(M))]


def ident(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


# exact torus symbol: A_adj eigenvalue = 2*sum cos(2 pi n_i / L)
def adj_eigenvalues(L):
    """Exact adjacency eigenvalues for L where all cosines are rational."""
    assert L in (2, 4), "use L in {2,4} so the cosines are exact rationals"
    cos_tab = {2: {0: Fraction(1), 1: Fraction(-1)},
               4: {0: Fraction(1), 1: Fraction(0), 2: Fraction(-1), 3: Fraction(0)}}[L]
    out = []
    for nk in product(range(L), repeat=3):
        out.append(2 * sum(cos_tab[x] for x in nk))
    return out


# ---------------------------------------------------------------------------
# rows
# ---------------------------------------------------------------------------


def r1_A_equals_mu_minus_six():
    """H(mu) = (mu - 6) I - Delta, exactly, so A = mu - 6."""
    L = 2
    D, sites, _ = laplacian(L)
    n = len(sites)
    ok = True
    checked = []
    for mu in (Fraction(0), Fraction(6), Fraction(13, 2), Fraction(-3)):
        H, _, _ = H_of_mu(L, mu)
        rebuilt = add(scal(mu - COORD, ident(n)), scal(Fraction(-1), D))
        if H != rebuilt:
            ok = False
        checked.append(f"mu={mu} -> A={mu - COORD}")
    check(
        "R1 H(mu) = (mu-6)*I - Delta exactly, so the covariant coefficient is A = mu - 6",
        ok,
        "; ".join(checked),
    )


def r2_A_equals_mu_minus_six_minus_E():
    """A2 on the resolvent: L = H - E, hence A = mu - 6 - E."""
    L = 2
    D, sites, _ = laplacian(L)
    n = len(sites)
    ok = True
    rows = []
    for mu in (Fraction(6), Fraction(4)):
        for E in (Fraction(0), Fraction(1), Fraction(-5, 2)):
            H, _, _ = H_of_mu(L, mu)
            Lop = add(H, scal(-E, ident(n)))          # L = H - E
            A_pred = mu - COORD - E
            rebuilt = add(scal(A_pred, ident(n)), scal(Fraction(-1), D))
            if Lop != rebuilt:
                ok = False
            rows.append(f"(mu={mu},E={E})->A={A_pred}")
    # A2 as written is mu = 6, E = 0, i.e. A = 0
    a2_is_zero = (Fraction(6) - COORD - Fraction(0)) == 0
    check(
        "R2 A2 on the resolvent gives L = H - E and A = mu - 6 - E; A2 as written is A = 0",
        ok and a2_is_zero,
        "; ".join(rows[:4]) + " ...",
    )


def r3_A_is_the_mass_gap():
    """min spec(L) = A exactly, so A is observable as the field's mass gap."""
    L = 4
    adj = adj_eigenvalues(L)
    ok = True
    rows = []
    for A in (Fraction(0), Fraction(1), Fraction(7, 2), Fraction(13)):
        # L = A*I - Delta = A*I - (A_adj - 6I) = (A+6) I - A_adj
        spec = sorted((A + COORD) - a for a in adj)
        rows.append(f"A={A}: min spec = {spec[0]}")
        if spec[0] != A:
            ok = False
    # the top of the band is A + 12
    top_ok = sorted((Fraction(0) + COORD) - a for a in adj)[-1] == 12
    check(
        "R3 min spec(L) = A exactly, so A is the field's mass gap and is observable",
        ok and top_ok,
        "; ".join(rows) + "; band top at A+12",
    )


def r4_energy_origin_shift_is_unobservable():
    """H -> H + cI shifts the spectrum rigidly, keeps eigenvectors, stays unitary.

    The landed SINGLE_AXIOM_HILBERT_NOTE records the same fact in words: the
    shift "has no observable effect because it contributes only a global phase".
    Here it is re-earned exactly: identical eigenvectors, identical gaps, and
    real spectrum (hence unitary evolution) for every mu.
    """
    L = 4
    adj = adj_eigenvalues(L)
    c = Fraction(9, 2)

    base = sorted(COORD - a for a in adj)           # spec H(6)
    shifted = sorted((COORD + c) - a for a in adj)  # spec H(6 + c)
    rigid = all(y - x == c for x, y in zip(base, shifted))

    gaps_base = [b - a for a, b in zip(base, base[1:])]
    gaps_shift = [b - a for a, b in zip(shifted, shifted[1:])]
    gaps_same = gaps_base == gaps_shift

    # eigenvectors of mu*I - A_adj are those of A_adj, for every mu:
    # (mu I - A)v = mu v - A v, so v is an eigenvector of H iff of A_adj.
    # Verified structurally on an explicit matrix by comparing commutators.
    Amat, sites, _ = adjacency(2)
    n = len(sites)
    same_eigenbasis = True
    for mu in (Fraction(0), Fraction(6), Fraction(-2)):
        H, _, _ = H_of_mu(2, mu)
        # H commutes with A_adj for every mu, so they share an eigenbasis
        HA = [[sum(H[i][k] * Amat[k][j] for k in range(n)) for j in range(n)]
              for i in range(n)]
        AH = [[sum(Amat[i][k] * H[k][j] for k in range(n)) for j in range(n)]
              for i in range(n)]
        if HA != AH:
            same_eigenbasis = False

    # Real spectrum for every mu => unitary evolution => probabilities preserved.
    # An earlier draft "checked" this with isinstance(..., Fraction), which is a
    # type test and cannot fail. The mathematical content is self-adjointness,
    # so that is what is verified: H(mu) = H(mu)^T exactly, for every mu.
    real_spectrum = True
    for mu_t in (Fraction(0), Fraction(6), Fraction(9), Fraction(-4), Fraction(5, 3)):
        Ht, st, _ = H_of_mu(2, mu_t)
        m = len(st)
        if any(Ht[i][j] != Ht[j][i] for i in range(m) for j in range(m)):
            real_spectrum = False

    check(
        "R4 the energy-origin shift is spectrally rigid: same eigenbasis, same gaps, "
        "real spectrum for every mu -- no observable consequence",
        rigid and gaps_same and same_eigenbasis and real_spectrum,
        f"shift c={c} moves every eigenvalue by exactly c; {len(gaps_base)} gaps identical; "
        f"[H(mu), A_adj] = 0 for every mu tested",
    )


def r5_mu_six_is_zero_row_sums():
    """mu = 6 <=> zero row sums <=> H annihilates the uniform state."""
    L = 2
    ok = True
    rows = []
    for mu in (Fraction(0), Fraction(6), Fraction(15, 2)):
        H, sites, _ = H_of_mu(L, mu)
        n = len(sites)
        sums = {sum(row) for row in H}
        one = [Fraction(1)] * n
        annihilates = all(x == 0 for x in matvec(H, one))
        rows.append(f"mu={mu}: row sum {sums.pop() if len(sums)==1 else sums}")
        if (mu == COORD) != annihilates:
            ok = False
    check(
        "R5 mu = 6 exactly iff the row sums vanish iff H annihilates the uniform state",
        ok,
        "; ".join(rows),
    )


def r6_markov_forces_it_quantum_does_not():
    """The discriminator.

    A continuous-time Markov generator Q must conserve total probability:
    d/dt sum(p) = sum(Q p) = 0 for every p, which holds iff every COLUMN of Q
    sums to zero. For Q = -(mu I - A_adj) = A_adj - mu I the column sums are
    6 - mu, so probability conservation FORCES mu = 6.

    A self-adjoint quantum Hamiltonian conserves probability by unitarity,
    which requires only H = H^dagger -- true for every real mu. So the quantum
    reading does NOT force mu = 6.
    """
    L = 2
    # Markov side: column sums of Q = A_adj - mu I
    markov_forced = None
    markov_rows = []
    for mu in (Fraction(0), Fraction(6), Fraction(9)):
        Amat, sites, _ = adjacency(L)
        n = len(sites)
        Q = [[Amat[i][j] - (mu if i == j else 0) for j in range(n)] for i in range(n)]
        colsums = {sum(Q[i][j] for i in range(n)) for j in range(n)}
        conserves = colsums == {Fraction(0)}
        markov_rows.append(f"mu={mu}: col sum {sorted(colsums)[0]}, conserves={conserves}")
        if mu == COORD:
            markov_forced = conserves
        elif conserves:
            markov_forced = False  # a non-6 mu also conserving would break the claim

    # Quantum side: H is self-adjoint for every mu
    self_adjoint_all_mu = True
    for mu in (Fraction(0), Fraction(6), Fraction(9), Fraction(-4)):
        H, sites, _ = H_of_mu(L, mu)
        n = len(sites)
        if any(H[i][j] != H[j][i] for i in range(n) for j in range(n)):
            self_adjoint_all_mu = False

    check(
        "R6 zero row sums are forced for a Markov generator and not for a self-adjoint "
        "quantum Hamiltonian",
        bool(markov_forced) and self_adjoint_all_mu,
        "; ".join(markov_rows) + "; H self-adjoint for every mu tested",
    )


def r7_A_zero_is_a_boundary_point():
    """The band of L is [A, A+12]; A = 0 is where its bottom touches zero.

    Care is needed about which lattice. On INFINITE Z^3 the symbol
    `Dhat(k) = 2*sum cos k_i - 6` sweeps [-12, 0] continuously, so
    spec(L) = [A, A+12] is an interval and L is singular for every
    A in [-12, 0]. On a FINITE torus only finitely many Dhat values are
    attained, so L can be nonsingular at interior points of that interval --
    at L = 4 and A = -1, for instance. An earlier draft asserted the
    continuum "iff" and then tested only A in {-13,-6,0,1}, which quietly
    excluded exactly the counterexamples. Both statements are checked
    separately here.
    """
    L = 4
    adj = adj_eigenvalues(L)

    # (i) the band endpoints are exact and attained: Dhat_min = -12, Dhat_max = 0
    dhats = sorted(a - COORD for a in adj)          # Dhat = adj - 6
    endpoints_exact = dhats[0] == -12 and dhats[-1] == 0

    # (ii) at A = 0 the bottom of the band is exactly 0, so L is singular
    spec0 = sorted((Fraction(0) + COORD) - a for a in adj)
    bottom_touches_zero = spec0[0] == 0

    # (iii) outside [-12, 0] the whole band misses zero, on any lattice
    outside_ok = True
    for A in (Fraction(1), Fraction(-13), Fraction(1, 2)):
        spec = [(A + COORD) - a for a in adj]
        if any(s == 0 for s in spec):
            outside_ok = False

    # (iv) the finite-torus caveat, exhibited rather than hidden: A = -1 lies
    # inside the continuum band yet L is nonsingular at L = 4
    spec_m1 = [(Fraction(-1) + COORD) - a for a in adj]
    finite_caveat = all(s != 0 for s in spec_m1)

    check(
        "R7 the band of L is [A, A+12] with both endpoints exact; A = 0 is where its "
        "bottom touches zero (with the finite-torus caveat exhibited)",
        endpoints_exact and bottom_touches_zero and outside_ok and finite_caveat,
        f"Dhat range [{dhats[0]}, {dhats[-1]}]; min spec at A=0 is {spec0[0]}; "
        f"A=-1 nonsingular on the L=4 torus though inside the continuum band",
    )


def r8_finite_volume_corollary():
    """At A = 0 on a finite torus the source must be zero-mean.

    Scoped as a finite-volume corollary: the parent theorem is formulated on
    infinite Z^3, where a compactly supported non-negative source is fine. On a
    finite covariant lattice the constant is a genuine kernel vector, so
    `L phi = -rho` is solvable only for zero-mean rho -- which a non-negative
    record density supplies only by being identically zero.
    """
    L = 2
    D, sites, _ = laplacian(L)
    n = len(sites)
    Lop = scal(Fraction(-1), D)  # A = 0, B = -1  =>  L = -Delta
    one = [Fraction(1)] * n
    kernel_has_const = all(x == 0 for x in matvec(Lop, one))

    # solvability: rho must be orthogonal to the kernel of L^T = L
    rho_uniform = [Fraction(1)] * n
    obstruction = sum(rho_uniform)  # <1, rho> != 0 blocks solvability
    blocked = obstruction != 0

    # A non-negative rho with zero sum must vanish. An earlier draft tested an
    # equivalence on two hand-picked vectors, both of which satisfied it
    # trivially. Here every non-negative integer source in a bounded box is
    # enumerated, and the only zero-sum one is the empty configuration.
    forces_empty = True
    zero_sum_witnesses = 0
    for rho in product(range(3), repeat=4):        # 3^4 non-negative sources
        if sum(rho) == 0:
            zero_sum_witnesses += 1
            if any(r != 0 for r in rho):
                forces_empty = False
    forces_empty = forces_empty and zero_sum_witnesses == 1

    check(
        "R8 finite-volume corollary: at A = 0 solvability needs a zero-mean source, which "
        "a non-negative record density supplies only when empty",
        kernel_has_const and blocked and forces_empty,
        f"<1,rho> = {obstruction} for uniform rho blocks solvability; of 81 non-negative sources enumerated, exactly {zero_sum_witnesses} has zero sum",
    )


def main() -> int:
    print("Cycle 709 - A2's missing bridge theorem, identified exactly")
    print("=" * 74)
    r1_A_equals_mu_minus_six()
    r2_A_equals_mu_minus_six_minus_E()
    r3_A_is_the_mass_gap()
    r4_energy_origin_shift_is_unobservable()
    r5_mu_six_is_zero_row_sums()
    r6_markov_forces_it_quantum_does_not()
    r7_A_zero_is_a_boundary_point()
    r8_finite_volume_corollary()
    print("=" * 74)
    print(f"{len(PASSES)} PASS / {len(FAILURES)} FAIL")
    for f in FAILURES:
        print(f"  FAILED: {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
