"""Staggered-Dirac substep 4 — AC narrowing verification (repaired 2026-06-10).

Verifies the AC-narrowing claim that the prior single-clause AC

    AC_narrow := "physical-species reading of joint-translation-character-
                  distinct hw=1 corners as SM matter generations"

decomposes as

    AC_narrow = AC_phi  AND  AC_lambda  AND  AC_phi_lambda

with explicit fates for each atom:

    AC_phi        "a physical observable distinguishes the three hw=1
                   corner states"
                  (blocked for C3-symmetric self-adjoint observables:
                   commuting with the corner 3-cycle forces equal
                   corner-basis expectation values, indeed equal moments
                   of every order)

    AC_lambda     "free staggered kinetic operator and regulated free
                   propagator have NO inter-corner matrix elements on the
                   hw=1 corner basis" (corner-block no-mixing statement;
                   computed first-principles from the upstream
                   Kawamoto-Smit phases, NOT assumed)

    AC_phi_lambda "framework 3-fold structure IS SM flavor-generation
                   structure" (genuine residual; semantic identification,
                   not machine-checkable; any axiom addition requires
                   explicit user approval)

2026-06-10 REPAIR (science fix). The 2026-05-07 runner (a) hard-coded the
AC_lambda conclusion as `np.diag([0,0,0])`, (b) hard-coded the Section-1
independence countermodels as boolean literals, and (c) scored a string
self-test ("NO STANDARD QFT AXIOM EQUIVALENT" in its own constant) as a
check. All three are replaced by genuine computations. In addition, the
2026-05-07 note and the 2026-05-09 rigorization addendum justified
AC_lambda block-diagonality via "the Kawamoto-Smit kinetic operator K
commutes with the lattice translations (T_x, T_y, T_z) + simultaneous
diagonalization". That premise is FALSE for the position-dependent
Kawamoto-Smit phases: this runner computes ||[D, T_1]|| and ||[D, T_2]||
and shows they are NONZERO (the true invariances are [D, T_mu^2] = 0 and
[D, T_3] = 0). The AC_lambda conclusion nevertheless survives by the
direct corner-annihilation argument:

    D e^{i p.x} = -sum_mu i sin(p_mu) e^{i (p + pi m_mu).x},
        m_1 = 0, m_2 = e_1, m_3 = e_1 + e_2  (phase momentum shifts),

so at every BZ-corner momentum p in {0, pi}^3 every sin(p_mu) vanishes
and D annihilates the corner plane wave EXACTLY (local identity,
verified here in exact integer arithmetic). Hence the hw=1 corner block
of D is the zero matrix and the regulated propagator satisfies
<c_a|(D + m)^{-1}|c_b> = delta_ab / m exactly.

Check classes are annotated per the audit rubric:
  [A] algebraic identity check on existing inputs
  [B] cross-note input verification (value read from an upstream note)
  [C] first-principles compute from the framework baseline (Cl(3) on Z^3
      plus accepted normalizations) producing numbers not present in any
      input

Section 5 (standard-QFT axiom catalog comparison for AC_phi_lambda) is a
DOCUMENTATION ECHO ONLY: it is printed for audit context and is NOT
scored as a PASS — the SM-generation identification is a semantic claim
that no runner can verify.

Upstream inputs (one hop):
  - Kawamoto-Smit phases eta_1=1, eta_2(x)=(-1)^{x_1},
    eta_3(x)=(-1)^{x_1+x_2} and the staggered kinetic form
    D = (1/2) sum_{x,mu} eta_mu(x) (chibar_{x+mu} chi_x - chibar_x chi_{x+mu})
    per docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md
    (bounded on its declared substep-1 Grassmann + spin-diagonalization
    premises; finite-boundary wrap is holonomy convention data there, so
    the even-L periodic-wrap representative used here is admissible and
    makes the BZ-corner momenta exactly representable at finite L).
  - hw=1 corner triplet, translation characters diag(-1,1,1) etc., and
    C_3[111] 3-cycle per
    docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md and
    docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md.

No PDG values, no lattice MC values, no fitted coefficients.

Companion: docs/STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md
Loop: staggered-dirac-substep4-ac-narrow-20260507 (repair 2026-06-10)
"""
from __future__ import annotations

import itertools
from typing import Dict, List, Tuple

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    cond = bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(cond)
    FAIL += int(not cond)
    return cond


# ---------------------------------------------------------------------------
# Geometry: hw=1 BZ corners on Z^3
# ---------------------------------------------------------------------------

HW1_CORNERS: List[Tuple[int, int, int]] = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
ALL_CORNERS: List[Tuple[int, int, int]] = list(
    itertools.product((0, 1), repeat=3)
)


def translation_eigenvalues(corner: Tuple[int, int, int]
                            ) -> Tuple[int, int, int]:
    """Joint eigenvalues of (T_x, T_y, T_z) on a BZ corner plane wave.

    T_mu acts as exp(i k_mu) = (-1)^{n_mu} on the plane wave with
    k_mu = n_mu * pi.
    """
    return tuple((-1) ** n for n in corner)


def c3_111_action(corner: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """C_3[111] cyclic shift of coordinate axes: (x,y,z) -> (y,z,x).

    On hw=1 BZ corners: (1,0,0) -> (0,1,0) -> (0,0,1) -> (1,0,0).
    """
    return (corner[2], corner[0], corner[1])


# ---------------------------------------------------------------------------
# Kawamoto-Smit staggered kinetic operator on a finite even-L Z^3 torus
# ---------------------------------------------------------------------------

def ks_phase(mu: int, x: Tuple[int, int, int]) -> int:
    """Kawamoto-Smit phases, read from the upstream substep-2 note ([B]):

        eta_1(x) = 1, eta_2(x) = (-1)^{x_1}, eta_3(x) = (-1)^{x_1+x_2}

    per STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md,
    eq. (6).
    """
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** x[0]
    return (-1) ** (x[0] + x[1])


class Lattice:
    """Even-L periodic Z^3 torus carrying the staggered operator.

    Even L keeps eta_mu well defined on the wrap; periodic wrap is the
    boundary-holonomy representative on which the corner momenta
    k_mu in {0, pi} are exactly representable (the upstream substep-2 note
    classifies finite-boundary wrap phases as convention data, not part of
    the forced local gauge class).
    """

    def __init__(self, L: int):
        assert L % 2 == 0, "even L required for eta periodicity"
        self.L = L
        self.sites = list(itertools.product(range(L), repeat=3))
        self.index = {s: i for i, s in enumerate(self.sites)}
        self.N = len(self.sites)

    def shift(self, x: Tuple[int, int, int], mu: int, s: int
              ) -> Tuple[int, int, int]:
        y = list(x)
        y[mu] = (y[mu] + s) % self.L
        return tuple(y)

    def staggered_D2(self) -> np.ndarray:
        """2*D as an exact integer matrix, with

        D = (1/2) sum_{x,mu} eta_mu(x) (chibar_{x+mu} chi_x - chibar_x chi_{x+mu})

        read as the matrix D[a,b] = coefficient of chibar_a chi_b
        (upstream Kawamoto-Smit note, Theorem 2 kinetic form).
        """
        D2 = np.zeros((self.N, self.N), dtype=np.int64)
        for x in self.sites:
            for mu in range(3):
                e = ks_phase(mu, x)
                D2[self.index[self.shift(x, mu, 1)], self.index[x]] += e
                D2[self.index[x], self.index[self.shift(x, mu, 1)]] -= e
        return D2

    def translation(self, mu: int) -> np.ndarray:
        T = np.zeros((self.N, self.N), dtype=np.int64)
        for x in self.sites:
            T[self.index[self.shift(x, mu, 1)], self.index[x]] = 1
        return T

    def corner_wave_int(self, n: Tuple[int, int, int]) -> np.ndarray:
        """Unnormalized BZ-corner plane wave with k = pi*n: entries +-1."""
        return np.array(
            [(-1) ** (n[0] * x[0] + n[1] * x[1] + n[2] * x[2])
             for x in self.sites],
            dtype=np.int64,
        )

    def corner_wave(self, n: Tuple[int, int, int]) -> np.ndarray:
        v = self.corner_wave_int(n).astype(float)
        return v / np.linalg.norm(v)

    def corner_mixing_perturbation(self) -> np.ndarray:
        """Countermodel operator W (NOT of the forced Kawamoto-Smit class):

            (W chi)(x) = (-1)^{x_1 + x_2} (chi(x + e_3) + chi(x - e_3)) / 2

        A local, self-adjoint, one-link operator whose phase shifts
        momentum by pi (e_1 + e_2): on a plane wave,
        W e^{i p.x} = cos(p_3) e^{i (p + pi(e_1+e_2)).x}, which maps the
        hw=1 corner (pi,0,0) to (0,pi,0) with amplitude cos(0) = 1.
        Returns 2*W as an exact integer matrix.
        """
        W2 = np.zeros((self.N, self.N), dtype=np.int64)
        for x in self.sites:
            ph = (-1) ** (x[0] + x[1])
            W2[self.index[x], self.index[self.shift(x, 2, 1)]] += ph
            W2[self.index[x], self.index[self.shift(x, 2, -1)]] += ph
        return W2


# ---------------------------------------------------------------------------
# Section 1: AC_lambda first-principles compute
# ---------------------------------------------------------------------------

def section1_ac_lambda(L: int) -> None:
    print()
    print("=" * 78)
    print(f"Section 1 (L={L}): AC_lambda — corner-block no-mixing computed")
    print("from the upstream Kawamoto-Smit phases (NOT hard-coded)")
    print("=" * 78)

    lat = Lattice(L)
    D2 = lat.staggered_D2()                  # exact 2*D, integer
    D = D2.astype(float) / 2.0

    # [B] cross-note input: the phase table itself (spot-verified against
    # the closed-form expressions quoted from the upstream note).
    spot = all(
        ks_phase(0, x) == 1
        and ks_phase(1, x) == (-1) ** x[0]
        and ks_phase(2, x) == (-1) ** (x[0] + x[1])
        for x in lat.sites
    )
    check(f"[B] lambda.{L}.a Kawamoto-Smit phase table matches upstream "
          "substep-2 note eq.(6) on all sites", spot,
          f"eta_1=1, eta_2=(-1)^x1, eta_3=(-1)^(x1+x2) on {lat.N} sites")

    # [A] antisymmetry of the kinetic matrix (Grassmann bilinear form).
    check(f"[A] lambda.{L}.b D is real antisymmetric (D^T = -D), exact integer "
          "arithmetic on 2D", bool(np.array_equal(D2.T, -D2)))

    # [C] corner plane waves are joint translation eigenvectors with the
    # declared characters diag(-1,1,1) / diag(1,-1,1) / diag(1,1,-1).
    Ts = [lat.translation(mu) for mu in range(3)]
    ok_chars = True
    for n in HW1_CORNERS:
        v = lat.corner_wave_int(n)
        want = translation_eigenvalues(n)
        for mu in range(3):
            ok_chars &= bool(np.array_equal(Ts[mu] @ v, want[mu] * v))
    check(f"[C] lambda.{L}.c hw=1 corner waves are exact joint (T_x,T_y,T_z) "
          "eigenvectors with characters (-1,1,1),(1,-1,1),(1,1,-1)",
          ok_chars)
    triples = {n: translation_eigenvalues(n) for n in HW1_CORNERS}
    check(f"[A] lambda.{L}.d the three hw=1 character triples are pairwise "
          "distinct", len(set(triples.values())) == 3, f"{triples}")

    # [C] LOAD-BEARING: D annihilates every BZ-corner plane wave EXACTLY
    # (integer arithmetic; the sin(p_mu)=0 corner identity).
    max_resid = 0
    for n in ALL_CORNERS:
        v = lat.corner_wave_int(n)
        r = int(np.abs(D2 @ v).max())
        max_resid = max(max_resid, r)
    check(f"[C] lambda.{L}.e LOAD-BEARING: D|c_n> = 0 EXACTLY for all 8 BZ "
          "corner waves (integer residual)", max_resid == 0,
          f"max |2D @ c| over 8 corners = {max_resid} (exact integers)")

    # [C] hw=1 corner block of D is the zero 3x3 matrix.
    waves = {n: lat.corner_wave(n) for n in HW1_CORNERS}
    block = np.array([[waves[a] @ (D @ waves[b]) for b in HW1_CORNERS]
                      for a in HW1_CORNERS])
    off = np.abs(block - np.diag(np.diag(block))).max()
    check(f"[C] lambda.{L}.f hw=1 corner block of D is the zero matrix "
          "(in particular: NO inter-corner matrix elements)",
          np.abs(block).max() == 0.0,
          f"max |<c_a|D|c_b>| = {np.abs(block).max():.3e}, "
          f"off-diagonal residual = {off:.3e}")

    # [C] regulated free propagator block: <c_a|(D+m)^{-1}|c_b> = d_ab/m.
    for m in (1.0, 0.1):
        G = np.linalg.inv(D + m * np.eye(lat.N))
        Gb = np.array([[waves[a] @ (G @ waves[b]) for b in HW1_CORNERS]
                       for a in HW1_CORNERS])
        offG = np.abs(Gb - np.diag(np.diag(Gb))).max()
        diag_err = np.abs(np.diag(Gb) - 1.0 / m).max()
        check(f"[C] lambda.{L}.g(m={m}) regulated propagator corner block "
              "= delta_ab/m (free 2-pt fn has NO inter-corner mixing "
              "at the corners)",
              offG < 1e-12 and diag_err < 1e-9,
              f"off-diag residual = {offG:.3e}, diag residual = "
              f"{diag_err:.3e} (load-bearing residuals)")

    # [C] HONESTY / repair record: the retired 2026-05-07/09 justification
    # "[D, T_mu] = 0 for all mu" is FALSE; the true invariances are
    # [D, T_mu^2] = 0 (and [D, T_3] = 0 since no eta depends on x_3).
    c1 = np.abs(D2 @ Ts[0] - Ts[0] @ D2).max()
    c2 = np.abs(D2 @ Ts[1] - Ts[1] @ D2).max()
    c3 = np.abs(D2 @ Ts[2] - Ts[2] @ D2).max()
    check(f"[C] lambda.{L}.h repair record: [D, T_1] != 0 and [D, T_2] != 0 "
          "(the 2026-05-07/09 commutation premise FAILS; conclusion "
          "survives via direct corner annihilation)",
          c1 > 0 and c2 > 0,
          f"max|[2D,T_1]| = {c1}, max|[2D,T_2]| = {c2}, "
          f"max|[2D,T_3]| = {c3} (exact integers)")
    sq_ok = all(
        int(np.abs(D2 @ (T @ T) - (T @ T) @ D2).max()) == 0 for T in Ts
    )
    check(f"[A] lambda.{L}.i true lattice invariance: [D, T_mu^2] = 0 exactly "
          "for all mu (two-site translations)", sq_ok)


# ---------------------------------------------------------------------------
# Section 2: AC_phi — C3-symmetric observables cannot distinguish corners
# ---------------------------------------------------------------------------

def c3_unitary_on_hw1() -> np.ndarray:
    """The C_3[111] unitary on H_{hw=1}: |c_1> -> |c_2> -> |c_3> -> |c_1>."""
    return np.array([[0, 0, 1],
                     [1, 0, 0],
                     [0, 1, 0]], dtype=float)


def hermitian_basis_3() -> List[np.ndarray]:
    """Real basis of the 9-dim real vector space of 3x3 Hermitian matrices."""
    basis: List[np.ndarray] = []
    for i in range(3):
        E = np.zeros((3, 3), dtype=complex)
        E[i, i] = 1.0
        basis.append(E)
    for i in range(3):
        for j in range(i + 1, 3):
            E = np.zeros((3, 3), dtype=complex)
            E[i, j] = 1.0
            E[j, i] = 1.0
            basis.append(E)
            F = np.zeros((3, 3), dtype=complex)
            F[i, j] = 1.0j
            F[j, i] = -1.0j
            basis.append(F)
    return basis


def section2_ac_phi() -> None:
    print()
    print("=" * 78)
    print("Section 2: AC_phi — equal-corner-expectation lemma for")
    print("C_3[111]-symmetric self-adjoint observables on H_{hw=1}")
    print("=" * 78)

    U = c3_unitary_on_hw1()
    check("[A] phi.a U_C3 is the 3-cycle permutation unitary "
          "(U^3 = I, U U^T = I)",
          bool(np.array_equal(np.linalg.matrix_power(U, 3), np.eye(3)))
          and bool(np.array_equal(U @ U.T, np.eye(3))))

    cyc = [HW1_CORNERS[0]]
    for _ in range(3):
        cyc.append(c3_111_action(cyc[-1]))
    check("[A] phi.b C_3[111] axis shift is a 3-cycle on the hw=1 corners",
          cyc[0] == cyc[3] and len(set(cyc[:3])) == 3,
          f"{cyc[0]} -> {cyc[1]} -> {cyc[2]} -> {cyc[3]}")

    # [A] LEMMA, full generality: the commutant of U inside the Hermitian
    # 3x3 matrices is EXACTLY 3-dimensional over R, and every element of
    # it has equal diagonal entries. By linearity this proves equal corner
    # expectations for EVERY C3-symmetric self-adjoint observable, not
    # just sampled instances.
    basis = hermitian_basis_3()
    rows = []
    for B in basis:
        C = B @ U - U @ B
        rows.append(np.concatenate([C.real.flatten(), C.imag.flatten()]))
    Mmap = np.array(rows).T            # (18, 9) real linear map
    s = np.linalg.svd(Mmap, compute_uv=False)
    null_dim = int(np.sum(s < 1e-12)) + max(0, 9 - len(s))
    check("[A] phi.c commutant {H = H^dagger : [H, U_C3] = 0} has real "
          "dimension EXACTLY 3 (= span{I, U+U^2, i(U-U^2)})",
          null_dim == 3,
          f"singular values of H -> [H,U] map: {np.round(s, 6)}")

    _, _, vt = np.linalg.svd(Mmap)
    null_vecs = vt[-3:]
    equal_diag = True
    for vec in null_vecs:
        H = sum(c * B for c, B in zip(vec, basis))
        d = np.real(np.diag(H))
        equal_diag &= bool(np.abs(d - d.mean()).max() < 1e-12)
    check("[A] phi.d every Hermitian commutant basis element has equal "
          "diagonal entries => equal corner expectations for the WHOLE "
          "family (by linearity)", equal_diag)

    # [A] orbit-transport identity (the lemma's one-line proof):
    # <c_{sigma(a)}|A|c_{sigma(a)}> = <c_a|U^dag A U|c_a> = <c_a|A|c_a>.
    rng = np.random.default_rng(20260610)
    ok_sample = True
    distinct_spec_seen = False
    for _ in range(50):
        a = rng.normal()
        b = rng.normal() + 1j * rng.normal()
        H = a * np.eye(3, dtype=complex) + b * U + np.conj(b) * U.T
        comm = np.abs(H @ U - U @ H).max()
        diag = np.real(np.diag(H))
        exp_eq = np.abs(diag - diag.mean()).max() < 1e-12
        # higher moments: H^2, H^3 are also in the commutant
        m2 = np.real(np.diag(H @ H))
        m3 = np.real(np.diag(H @ H @ H))
        mom_eq = (np.abs(m2 - m2.mean()).max() < 1e-10
                  and np.abs(m3 - m3.mean()).max() < 1e-10)
        herm = np.abs(H - H.conj().T).max() < 1e-12
        ok_sample &= (comm < 1e-12) and exp_eq and mom_eq and herm
        ev = np.linalg.eigvalsh(H)
        if np.min(np.diff(np.sort(ev))) > 1e-3:
            distinct_spec_seen = True
    check("[A] phi.e 50 random C3-symmetric self-adjoint H = aI + bU + "
          "conj(b)U^2: [H,U]=0 and ALL corner expectations AND 2nd/3rd "
          "moments equal", ok_sample,
          "equal moments of every order: H^n stays in the commutant")
    check("[A] phi.f the family is NOT spectrally trivial: instances with "
          "3 distinct eigenvalues occur (obstruction is about corner "
          "expectations, not about H being scalar)", distinct_spec_seen)

    # [A] canonical instance quoted in the note: a=1.5, b=0.7.
    a0, b0 = 1.5, 0.7
    H0 = a0 * np.eye(3) + b0 * U + b0 * U.T
    ev0 = np.sort(np.linalg.eigvalsh(H0))
    exp0 = np.diag(H0)
    check("[A] phi.g canonical instance (a=1.5, b=0.7): eigenvalues "
          "{0.8, 0.8, 2.9}, all three corner expectations = 1.5",
          np.allclose(ev0, [0.8, 0.8, 2.9], atol=1e-12)
          and np.allclose(exp0, [1.5, 1.5, 1.5], atol=1e-12),
          f"eigenvalues = {np.round(ev0, 12)}, "
          f"corner expectations = {np.round(exp0, 12)}")

    # [A] sharpness: dropping C3 symmetry restores distinguishability,
    # so the obstruction is exactly the symmetry restriction, not a
    # triviality of the hw=1 sector.
    Hbreak = np.diag([1.0, 2.0, 3.0])
    comm_b = np.abs(Hbreak @ U - U @ Hbreak).max()
    diag_b = np.diag(Hbreak)
    check("[A] phi.h sharpness: the C3-BREAKING observable diag(1,2,3) "
          "([H,U] != 0) distinguishes all three corners by expectation "
          "value", comm_b > 0.5 and len(set(diag_b.tolist())) == 3,
          f"|[H,U]|_max = {comm_b}, expectations = {diag_b.tolist()}")


# ---------------------------------------------------------------------------
# Section 3: decomposition independence — COMPUTED countermodels
# ---------------------------------------------------------------------------

def section3_independence(L: int) -> None:
    print()
    print("=" * 78)
    print(f"Section 3 (L={L}): decomposition independence — computed")
    print("countermodels (replacing the retired hard-coded booleans)")
    print("=" * 78)

    lat = Lattice(L)
    D2 = lat.staggered_D2()
    D = D2.astype(float) / 2.0
    waves = {n: lat.corner_wave(n) for n in HW1_CORNERS}

    # CM1: AC_phi is blocked in the C3-symmetric family while AC_lambda holds.
    # This is the framework's
    # actual free sector: Section 1 shows the corner block of D is zero
    # (AC_lambda holds) and Section 2 shows C3-symmetric observables give
    # equal corner expectations (AC_phi blocked on that family).
    blockD = np.array([[waves[a] @ (D @ waves[b]) for b in HW1_CORNERS]
                       for a in HW1_CORNERS])
    U = c3_unitary_on_hw1()
    H_sym = 1.5 * np.eye(3) + 0.7 * U + 0.7 * U.T
    diag_sym = np.diag(H_sym)
    cm1 = (np.abs(blockD).max() == 0.0
           and np.abs(diag_sym - diag_sym.mean()).max() < 1e-12)
    check("[C] independence.a CM1 (AC_phi blocked in the symmetric family): in the actual KS free "
          "sector AC_lambda HOLDS (zero corner block) while C3-symmetric "
          "expectation readout CANNOT distinguish corners", cm1)

    # CM2: AC_lambda fails for a non-KS local operator while corner
    # distinguishability content is untouched: W = (-1)^{x1+x2} symmetric
    # one-link hop in direction 3 has NONZERO inter-corner elements.
    W2 = lat.corner_mixing_perturbation()
    W = W2.astype(float) / 2.0
    check("[A] independence.b countermodel operator W is local, one-link and "
          "self-adjoint (W^T = W, real)", bool(np.array_equal(W2.T, W2)))
    blockW = np.array([[waves[a] @ (W @ waves[b]) for b in HW1_CORNERS]
                       for a in HW1_CORNERS])
    offW = np.abs(blockW - np.diag(np.diag(blockW))).max()
    check("[C] independence.c CM2 (AC_lambda can fail separately): the non-Kawamoto-Smit "
          "perturbation W mixes hw=1 corners: <c_2|W|c_1> != 0 — so "
          "corner-block no-mixing is NOT automatic for local lattice "
          "operators; it load-bears on the upstream KS phase class",
          offW > 0.5,
          f"hw=1 block of W = {np.round(blockW, 12).tolist()}, "
          f"max off-diagonal = {offW}")

    # CM3: AC_phi can hold once the C3-symmetric restriction is dropped,
    # with AC_lambda untouched (D unchanged): diag(1,2,3) on H_{hw=1}
    # distinguishes the corners (Section 2.h) while the corner block of D
    # is still zero. So AC_phi and AC_lambda vary independently.
    cm3 = np.abs(blockD).max() == 0.0
    check("[C] independence.d CM3 (AC_phi holds without touching AC_lambda): a "
          "C3-breaking observable distinguishes corners while the "
          "KS corner block stays zero — the two atoms vary independently",
          cm3)

    # AC_phi_lambda independence support: the labeling-convention count.
    # Between two free C3 orbits of size 3 there are exactly 3
    # C3-equivariant bijections out of 6 — one cyclic-relabeling class.
    sigma = {0: 1, 1: 2, 2: 0}
    equivariant = 0
    total = 0
    for perm in itertools.permutations(range(3)):
        total += 1
        f = dict(enumerate(perm))
        if all(f[sigma[x]] == sigma[f[x]] for x in range(3)):
            equivariant += 1
    check("[A] independence.e AC_phi_lambda parameter count: exactly 3 of 6 "
          "bijections {hw=1 corners} -> {3 SM generations} are "
          "C3-equivariant (one cyclic-relabeling class)",
          equivariant == 3 and total == 6,
          f"equivariant = {equivariant} / {total}; the semantic "
          "identification itself is NOT machine-checkable and stays "
          "an admitted residual")


# ---------------------------------------------------------------------------
# Section 4 (documentation echo — NOT SCORED)
# ---------------------------------------------------------------------------

def section4_documentation() -> None:
    print()
    print("=" * 78)
    print("Section 4: AC_phi_lambda standard-QFT catalog comparison")
    print("(DOCUMENTATION ECHO ONLY — printed for audit context, NOT")
    print(" scored as a check; a string comparison cannot verify a")
    print(" semantic identification claim)")
    print("=" * 78)
    catalog = [
        "W1-W6 (Wightman 1957): domain, spectrum, vacuum, covariant "
        "fields, locality, cyclicity — no generation-count axiom",
        "HK1-HK4 (Haag-Kastler 1964): net, isotony, locality, covariance "
        "— no generation-count axiom",
        "SM inputs: three matter generations / gauge group / Higgs / "
        "Yukawa / CKM-PMNS are empirical or structural INPUTS, not "
        "axioms or theorems of standard QFT",
    ]
    for line in catalog:
        print(f"  - {line}")
    print()
    print("  AC_phi_lambda therefore has no standard-QFT axiom equivalent")
    print("  to inherit: the identification 'framework hw=1 triplet IS the")
    print("  SM generation triplet' is the open admitted residual of this")
    print("  note. No PASS is recorded for this section.")


# ---------------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 78)
    print("Staggered-Dirac Substep 4 — AC Narrowing Verification")
    print("(repaired 2026-06-10: de-stubbed runner + corrected AC_lambda")
    print(" justification; see module docstring)")
    print("=" * 78)
    print()
    print("Loop: staggered-dirac-substep4-ac-narrow-20260507")
    print("Companion theorem note:")
    print("  docs/STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_"
          "2026-05-07_substep4ac.md")

    # Section 0: corner setup
    print()
    print("=" * 78)
    print("Section 0: hw=1 BZ corner setup")
    print("=" * 78)
    triples = {n: translation_eigenvalues(n) for n in HW1_CORNERS}
    for n, t in triples.items():
        print(f"  |{n}>: (T_x, T_y, T_z) = {t}")
    check("[A] setup.a the three hw=1 corners carry pairwise-distinct joint "
          "(T_x,T_y,T_z) characters", len(set(triples.values())) == 3)
    hw_counts = {h: sum(1 for n in ALL_CORNERS if sum(n) == h)
                 for h in range(4)}
    check("[A] setup.b BZ-corner Hamming-weight census is 1+3+3+1 "
          "(hw=1 triplet exists and is the unique odd-parity triplet)",
          hw_counts == {0: 1, 1: 3, 2: 3, 3: 1}, f"{hw_counts}")

    # Sections 1 and 3 at two lattice sizes; Section 2 size-independent.
    for L in (4, 6):
        section1_ac_lambda(L)
    section2_ac_phi()
    for L in (4, 6):
        section3_independence(L)
    section4_documentation()

    # Final summary
    print()
    print("=" * 78)
    print("FINAL VERIFICATION SUMMARY")
    print("=" * 78)
    print()
    print("AC_narrow = AC_phi AND AC_lambda AND AC_phi_lambda, with:")
    print("  AC_lambda: corner-block no-mixing COMPUTED first-principles")
    print("             from the upstream Kawamoto-Smit phases")
    print("             (D|c_n> = 0 exactly; propagator block = I/m;")
    print("             retired commutation premise exposed in direct commutator check)")
    print("  AC_phi:    blocked for C3-symmetric self-adjoint observables")
    print("             on H_{hw=1} (full commutant lemma, phi.c-phi.e),")
    print("             sharp under C3 breaking (phi.h)")
    print("  AC_phi_lambda: admitted residual (documentation echo only,")
    print("             unscored; labeling count 3-of-6 in independence.e)")
    print()
    print("Substep 4 status: bounded_theorem (UNCHANGED; AC sharpened)")
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
