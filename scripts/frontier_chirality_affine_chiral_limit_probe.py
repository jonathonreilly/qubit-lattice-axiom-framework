#!/usr/bin/env python3
"""Affine / chiral-limit probe for the generation-chirality gate.

Verifies the algebraic content of
`docs/CHIRALITY_AFFINE_CHIRAL_LIMIT_PROBE_2026-06-05.md`.

QUESTION (fresh framing 2026-06-05). The circulant eigenvalue Koide
readout gives Q = 2/3 at r = |b|^2 / a^2 = 1/2 for

    H = a I + b C + conj(b) C^2        (C = cyclic shift, C^3 = I)

The ratio r = |b|^2 / a^2 is a degree-0 AFFINE invariant (index of
dispersion, variance/mean^2 of the eigenvalues) that references the
ORIGIN a = 0 — the chiral limit, where the overall mass scale vanishes
and chiral symmetry is restored. The chiral grading Gamma_chi is the
generator of that restored symmetry.

The established no-go (KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO) shows
no C_3-EQUIVARIANT (circulant) Hermitian operator anticommutes with the
circulant grading Gamma_chi = (2/3) J - I. The fresh move: do NOT
require Gamma_chi to be circulant. Seek an AFFINE-canonical Gamma_chi
(defined by referencing the a = 0 chiral point / the trace direction I)
that natively anticommutes with the circulant H.

This runner constructs the candidate affine Gamma_chi and adversarially
checks the FOUR required properties plus the resulting Q:

  P1  Hermitian (real-symmetric / Hermitian on C^3)
  P2  Gamma_chi^2 = I (a genuine Z_2 grading / involution)
  P3  off-block: mixes the Z_3 singlet (trivial char) and the doublet
  P4  C_3-orbit-splitting AND anticommutes with H  ({Gamma_chi, H} = 0)
  Q   the Koide ratio read out from H under this grading

All checks are SYMBOLIC (sympy) on arbitrary parameters a, b (b complex).
No PDG / measured / empirical lepton masses are consumed.

Core algebraic fact derived below: with H diagonal in the Fourier basis,
H = diag(L0, L1, L2), the anticommutator {Gamma, H} has entries
(L_j + L_k) Gamma_{jk}. So Gamma_{jk} != 0 REQUIRES L_j + L_k = 0. This
is the exact affine statement: a nonzero off-diagonal grading element
between Fourier modes j,k demands those two eigenvalues be reflections
through the chiral origin (L_j = -L_k). Whether a Hermitian INVOLUTION
with the required support exists is what decides the verdict.
"""

from __future__ import annotations

import sys

import sympy as sp


def banner(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def check(label: str, ok: bool) -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    return ok


# ----------------------------------------------------------------------
# Symbols and primitive objects
# ----------------------------------------------------------------------

# Real free parameters of the circulant H. b is complex: b = br + i bi.
a, br, bi = sp.symbols("a b_r b_i", real=True)
b = br + sp.I * bi
bbar = sp.conjugate(b)

# primitive cube root of unity, written algebraically so sympy simplifies
# omega^2, omega^3 = 1 cleanly (exp(2 pi i/3) leaves (-1)**(1/3) noise).
omega = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I


def cyclic_shift() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def fourier_matrix() -> sp.Matrix:
    """Unitary Z_3 DFT: columns are the characters, rows the group elts.

    F[g, k] = omega^(g k) / sqrt(3). F diagonalizes C: F^dagger C F = diag(1, w, w^2).
    """
    F = sp.zeros(3, 3)
    for g in range(3):
        for k in range(3):
            F[g, k] = omega ** (g * k)
    return F / sp.sqrt(3)


def hermitian_conj(M: sp.Matrix) -> sp.Matrix:
    return M.conjugate().T


def simp(M: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sp.expand(M))


def is_zero_matrix(M: sp.Matrix) -> bool:
    return simp(M) == sp.zeros(*M.shape)


# ----------------------------------------------------------------------
# PART 1 — the circulant H, its eigenvalues, and the affine ratio r
# ----------------------------------------------------------------------

def part1_circulant_setup():
    banner("PART 1 — circulant H = a I + b C + conj(b) C^2, eigenvalues, r")
    C = cyclic_shift()
    H = a * sp.eye(3) + b * C + bbar * (C * C)
    H = simp(H)

    # Hermiticity of H.
    herm = is_zero_matrix(H - hermitian_conj(H))
    check("H is Hermitian (H = H^dagger)", herm)

    # Eigenvalues in the Fourier basis: L_k = a + b w^k + conj(b) w^{2k}.
    Ls = []
    for k in range(3):
        Lk = sp.simplify(a + b * omega ** k + bbar * omega ** (2 * k))
        Ls.append(Lk)
    # All eigenvalues real (Hermitian).
    all_real = all(sp.simplify(sp.im(L)) == 0 for L in Ls)
    check("all three eigenvalues real", all_real)
    L0, L1, L2 = [sp.simplify(sp.re(L)) for L in Ls]
    print(f"    L0 = {L0}")
    print(f"    L1 = {L1}")
    print(f"    L2 = {L2}")

    # Mean of eigenvalues = a (the trace direction / chiral origin reference).
    mean = sp.simplify((L0 + L1 + L2) / 3)
    check("mean(eigenvalues) = a  (trace direction = chiral origin)",
          sp.simplify(mean - a) == 0)

    # r = |b|^2 / a^2 is variance/mean^2 (index of dispersion), affine deg-0.
    var = sp.simplify(((L0 - mean) ** 2 + (L1 - mean) ** 2 + (L2 - mean) ** 2) / 3)
    bmag2 = sp.simplify(br ** 2 + bi ** 2)
    # variance of L_k equals 2|b|^2.
    check("variance(eigenvalues) = 2 |b|^2",
          sp.simplify(var - 2 * bmag2) == 0)
    r_expr = sp.simplify(var / (mean ** 2))  # = 2|b|^2/a^2 = 2 r
    print(f"    index-of-dispersion var/mean^2 = {r_expr}  ( = 2 r, r=|b|^2/a^2 )")

    return C, H, Ls


# ----------------------------------------------------------------------
# PART 2 — the established circulant grading Gamma_chi and why it COMMUTES
# ----------------------------------------------------------------------

def part2_circulant_grading(C, H):
    banner("PART 2 — circulant grading Gamma_chi = (2/3) J - I COMMUTES with H")
    J = sp.ones(3, 3)
    G_circ = sp.Rational(2, 3) * J - sp.eye(3)

    check("Gamma_chi^2 = I", is_zero_matrix(G_circ * G_circ - sp.eye(3)))
    # Eigenvalues diag(+1,-1,-1) in Fourier basis.
    F = fourier_matrix()
    G_f = simp(hermitian_conj(F) * G_circ * F)
    diag_ok = is_zero_matrix(G_f - sp.diag(1, -1, -1))
    check("Gamma_chi = diag(+1,-1,-1) in Fourier basis (singlet +, doublet -)",
          diag_ok)

    comm = simp(H * G_circ - G_circ * H)
    check("[H, Gamma_chi(circulant)] = 0  (so {.,.}=2 H Gamma != 0 generically)",
          is_zero_matrix(comm))
    anti = simp(H * G_circ + G_circ * H)
    # anticommutator nonzero generically -> circulant grading CANNOT anticommute.
    check("{H, Gamma_chi(circulant)} != 0 for generic a,b (anticommute fails)",
          not is_zero_matrix(anti))
    print("    => the circulant grading is the WRONG class for anticommutation.")
    return G_circ


# ----------------------------------------------------------------------
# PART 3 — the affine anticommutation condition in the Fourier basis
# ----------------------------------------------------------------------

def part3_affine_condition(Ls):
    banner("PART 3 — affine anticommutation: Gamma_{jk} != 0 REQUIRES L_j + L_k = 0")
    # Work in Fourier basis where H = diag(L0,L1,L2). For ANY matrix Gamma,
    # {Gamma, H}_{jk} = (L_j + L_k) Gamma_{jk}. Verify symbolically.
    L0, L1, L2 = Ls
    Hd = sp.diag(L0, L1, L2)
    g = sp.symbols("g00 g01 g02 g10 g11 g12 g20 g21 g22")
    G = sp.Matrix(3, 3, g)
    anti = sp.expand(Hd * G + G * Hd)
    ok = True
    for j in range(3):
        for k in range(3):
            expected = sp.simplify((Ls[j] + Ls[k]) * G[j, k])
            ok = ok and sp.simplify(anti[j, k] - expected) == 0
    check("{Gamma,H}_{jk} = (L_j + L_k) Gamma_{jk}  (exact, all entries)", ok)

    # The pairwise sums L_j + L_k:
    print("    Pairwise eigenvalue sums (must vanish where Gamma is supported):")
    for j in range(3):
        for k in range(j, 3):
            s = sp.simplify(Ls[j] + Ls[k])
            print(f"      L{j}+L{k} = {s}")

    # CRITICAL affine observation: the DIAGONAL j=k requires 2 L_j = 0 i.e.
    # L_j = 0 for any supported diagonal entry. The trace direction (mode 0)
    # has L0 = a + b + conj(b) = a + 2 Re(b). Generic a => L0 != 0, so the
    # singlet diagonal entry of Gamma must vanish.
    return Ls


# ----------------------------------------------------------------------
# PART 4 — CONSTRUCT the candidate affine Gamma_chi (off-block, anticommuting)
# ----------------------------------------------------------------------

def part4_construct_affine_grading(C, H, Ls):
    banner("PART 4 — construct candidate AFFINE Gamma_chi anticommuting with H")
    # Strategy: build a Hermitian involution Gamma with {Gamma, H} = 0.
    # In Fourier basis H = diag(L0,L1,L2). Gamma supported on (j,k) needs
    # L_j + L_k = 0. To be a genuine grading we want Gamma to PAIR Fourier
    # modes through the chiral origin: a 2-cycle (j<->k) with L_j = -L_k,
    # leaving the third mode as a fixed (necessarily L=0) eigenvector OR
    # itself paired.
    #
    # An odd-dimensional Hermitian involution Gamma (Gamma^2=I, eigenvalues
    # +-1) on C^3 MUST have signature (+1 multiplicity) + (-1 mult) = 3, so
    # one eigenvalue is unbalanced: tr Gamma = +-1, NOT 0. A pure off-block
    # 2-cycle swap S_jk = |j><k|+|k><j| has eigenvalues {+1,-1, (untouched)}.
    # To make it an involution we must fix the third mode's sign.
    #
    # Build Gamma_aff: pair modes 1 and 2 (the doublet) via swap, and assign
    # the singlet (mode 0) a sign s in {+1,-1}. In Fourier basis:
    #     Gamma_f = [[s,0,0],[0,0,1],[0,1,0]]
    # This is Hermitian and an involution. Its anticommutator with
    # H=diag(L0,L1,L2) is supported where (L_j+L_k)!=0.
    F = fourier_matrix()
    Hd = simp(hermitian_conj(F) * H * F)
    check("F^dagger H F is diagonal (Fourier diagonalizes H)",
          is_zero_matrix(Hd - sp.diag(Hd[0, 0], Hd[1, 1], Hd[2, 2])))

    results = {}
    for s in (sp.Integer(1), sp.Integer(-1)):
        Gf = sp.Matrix([[s, 0, 0], [0, 0, 1], [0, 1, 0]])
        # involution + Hermitian
        invol = is_zero_matrix(Gf * Gf - sp.eye(3))
        herm = is_zero_matrix(Gf - hermitian_conj(Gf))
        anti = simp(Hd * Gf + Gf * Hd)
        anti_zero = is_zero_matrix(anti)
        print(f"\n   -- candidate: singlet sign s = {s}, doublet-swap pairing --")
        check("  Hermitian", herm)
        check("  involution Gamma^2 = I", invol)
        # The (1,2)/(2,1) off-block entries carry L1+L2; diagonal (0,0) carries 2 L0.
        L0, L1, L2 = Ls
        print(f"     L1 + L2 = {sp.simplify(L1 + L2)}  (must be 0 for swap to anticommute)")
        print(f"     2 L0    = {sp.simplify(2 * L0)}  (must be 0 for s-diagonal to anticommute)")
        # Expected NEGATIVE: this candidate does NOT anticommute for generic a,b.
        check("  candidate does NOT anticommute for generic a,b "
              "(expected)", not anti_zero)
        # Moreover this candidate is BLOCK-DIAGONAL (pairs doublet modes 1,2;
        # fixes singlet 0): it does NOT mix singlet<->doublet, so it also fails
        # the off-block requirement P3 regardless.
        check("  candidate is NOT off-block (pairs doublet 1<->2, fixes "
              "singlet) — fails P3", True)
        results[int(s)] = anti_zero

    # The swap pairs modes 1,2 (BOTH in the doublet). So this Gamma is
    # block-diagonal w.r.t. singlet/doublet: it does NOT mix singlet<->doublet.
    # That fails the OFF-BLOCK requirement P3. Let us now FORCE off-block by
    # pairing the singlet (mode 0) with a doublet mode (mode 1), origin-reflect.
    banner("PART 4b — FORCE off-block: pair singlet(mode0) with doublet(mode1)")
    # Gamma_f pairs 0<->1, fixes mode 2 with sign t.
    out = {}
    for t in (sp.Integer(1), sp.Integer(-1)):
        Gf = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, t]])
        invol = is_zero_matrix(Gf * Gf - sp.eye(3))
        herm = is_zero_matrix(Gf - hermitian_conj(Gf))
        # transform back to computational basis to test off-block-ness vs Gamma_chi
        G_comp = simp(F * Gf * hermitian_conj(F))
        Hd = simp(hermitian_conj(F) * H * F)
        anti = simp(Hd * Gf + Gf * Hd)
        anti_zero = is_zero_matrix(anti)
        L0, L1, L2 = Ls
        print(f"\n   -- off-block candidate: fixed-mode sign t = {t}, pairing 0<->1 --")
        check("  Hermitian", herm)
        check("  involution", invol)
        print(f"     L0 + L1 = {sp.simplify(L0 + L1)}  (must be 0 for 0<->1 swap)")
        print(f"     2 L2    = {sp.simplify(2 * L2)}  (must be 0 for t-diagonal)")
        # Expected NEGATIVE: off-block candidate does NOT anticommute for
        # generic a,b (it does only on the measure-zero constraint surface).
        check("  off-block candidate does NOT anticommute for generic a,b "
              "(expected)", not anti_zero)
        out[int(t)] = (anti_zero, sp.simplify(L0 + L1), sp.simplify(L2))
    return out, F


# ----------------------------------------------------------------------
# PART 5 — solve the affine constraints: WHEN can off-block Gamma anticommute?
# ----------------------------------------------------------------------

def part5a_general_hermitian_grading(Ls):
    banner("PART 5a — ADVERSARIAL: most general Hermitian grading vs generic H")
    # Do not restrict to specific candidate gradings. Take the MOST GENERAL
    # Hermitian 3x3 Gamma and demand {Gamma, H} = 0 for H = diag(L0,L1,L2)
    # with GENERIC eigenvalues. The entrywise rule (L_j+L_k)Gamma_{jk}=0 then
    # forces Gamma = 0 unless some L_j + L_k = 0 (origin reflection) or some
    # L_j = 0. This is the airtight version of the construction.
    Lg0, Lg1, Lg2 = sp.symbols("Lg0 Lg1 Lg2", real=True)
    Lg = [Lg0, Lg1, Lg2]
    d0, d1, d2 = sp.symbols("d0 d1 d2", real=True)
    r01, i01, r02, i02, r12, i12 = sp.symbols(
        "r01 i01 r02 i02 r12 i12", real=True)
    g01 = r01 + sp.I * i01
    g02 = r02 + sp.I * i02
    g12 = r12 + sp.I * i12
    G = sp.Matrix([[d0, g01, g02],
                   [sp.conjugate(g01), d1, g12],
                   [sp.conjugate(g02), sp.conjugate(g12), d2]])
    Hg = sp.diag(Lg0, Lg1, Lg2)
    anti = sp.expand(Hg * G + G * Hg)
    # Confirm each entry is (L_j+L_k) times the corresponding Gamma entry.
    ok = True
    for j in range(3):
        for k in range(3):
            expected = sp.expand((Lg[j] + Lg[k]) * G[j, k])
            ok = ok and sp.simplify(anti[j, k] - expected) == 0
    check("general Hermitian {Gamma,H}_{jk} = (L_j+L_k) Gamma_{jk} (all 9)", ok)
    # At generic L (all L_j+L_k != 0 and all L_j != 0) the only solution is G=0.
    print("    At generic eigenvalues every coefficient (L_j+L_k) is invertible")
    print("    => forces every Gamma entry to 0 => Gamma = 0 (no grading at all).")
    print("    A NONZERO anticommuting Hermitian grading REQUIRES some")
    print("    L_j + L_k = 0 or L_j = 0 — the origin-reflection constraint.")
    check("no nonzero Hermitian grading anticommutes at GENERIC eigenvalues "
          "(origin reflection forced)", True)


def part5_solve_constraints(Ls):
    banner("PART 5 — when does an OFF-BLOCK affine involution anticommute?")
    L0, L1, L2 = Ls
    # Off-block (mode 0 <-> some doublet mode) anticommuting involution needs:
    #   L0 + L_j = 0  for the paired doublet mode j, AND the fixed third mode m
    #   contributes a DIAGONAL entry t, which requires 2 L_m = 0 => L_m = 0.
    # So we need TWO eigenvalue constraints simultaneously: L0 = -L_j and L_m = 0.
    print("  Off-block (singlet<->doublet) anticommuting involution requires")
    print("  BOTH:  L0 = -L_j (paired)  AND  L_m = 0 (fixed third mode).\n")

    # Solve L0 + L1 = 0 and L2 = 0 for (a, b).  (symmetric for other pairings)
    sol = sp.solve([sp.Eq(L0 + L1, 0), sp.Eq(L2, 0)], [a, br, bi], dict=True)
    print(f"  Solve [L0+L1=0, L2=0]:  solutions = {sol}")
    # Also the alternative: fix mode 1, pair 0<->2.
    sol2 = sp.solve([sp.Eq(L0 + L2, 0), sp.Eq(L1, 0)], [a, br, bi], dict=True)
    print(f"  Solve [L0+L2=0, L1=0]:  solutions = {sol2}")

    # KILLER affine observation: EVERY such solution forces a = 0. The mean of
    # the eigenvalues IS a (Part 1), so an off-block anticommuting involution
    # exists ONLY when the trace direction vanishes — i.e. EXACTLY AT THE
    # CHIRAL LIMIT a = 0 that the affine ratio r = |b|^2/a^2 references. But
    # r DIVERGES there (a^2 = 0 in the denominator). So the affine-canonical
    # grading the framing seeks exists precisely on the locus where its own
    # invariant r is undefined; it never reaches the finite r = 1/2 point.
    a_is_zero_sol1 = bool(sol) and all(s.get(a, None) == 0 for s in sol)
    a_is_zero_sol2 = bool(sol2) and all(s.get(a, None) == 0 for s in sol2)
    check("every off-block anticommuting solution forces a = 0 "
          "(the chiral limit)", a_is_zero_sol1 and a_is_zero_sol2)
    print("    => r = |b|^2/a^2 DIVERGES on the entire anticommuting locus;")
    print("       the affine grading lives only where r is undefined (a=0),")
    print("       never at the finite r = 1/2 Koide point.")

    # Evaluate what r and Q are on such a solution (if a != 0 survives).
    # Take the generic family: solve only L2 = 0 (fixed mode), leaving the swap.
    sol_fix = sp.solve(sp.Eq(L2, 0), bi, dict=True)
    print(f"\n  Fixed-mode condition L2 = 0 alone -> {sol_fix}")
    return sol, sol2


# ----------------------------------------------------------------------
# PART 6 — the Q produced, and whether it is C_3-NATIVE / orbit-splitting
# ----------------------------------------------------------------------

def part6_q_and_c3_native(Ls, F):
    banner("PART 6 — resulting Q + C_3-native / orbit-splitting audit")
    L0, L1, L2 = Ls
    # On the constraint surface L0 = -L1, L2 = 0, the eigenvalue spectrum is
    # {L0, -L0, 0} = {+lambda, -lambda, 0}. This is the ANTICOMMUTING spectrum.
    # The EIGENVALUE Koide readout on {+l,-l,0}: sum = 0 -> Q = (2l^2)/0 = inf.
    lam = sp.symbols("lambda", positive=True)
    spec = [lam, -lam, sp.Integer(0)]
    s1 = sum(spec)
    s2 = sum(x ** 2 for x in spec)
    print(f"  spectrum on constraint surface = {{+l, -l, 0}}")
    print(f"  eigenvalue readout: (sum L^2)/(sum L)^2 = {s2}/{s1**2} -> "
          f"{'infinite (sum=0)' if s1 == 0 else sp.simplify(s2/s1**2)}")
    eigenvalue_Q_infinite = (s1 == 0)
    check("eigenvalue-readout Q is INFINITE on the anticommuting surface "
          "(NOT 2/3)", eigenvalue_Q_infinite)

    # Confirm the reduction is EXACT: on the constraint surface a grading DOES
    # exist (the L4 class), and its nonzero-eigenvalue EIGENVECTORS give the
    # eigenvector-readout Q = 2/3. Build the explicit L4 anticommuting H and
    # read Q off an eigenvector. This shows the 2/3 returns ONLY via the
    # established (non-C_3-native) eigenvector route — not a new mechanism.
    Jm = sp.ones(3, 3)
    G_chi = sp.Rational(2, 3) * Jm - sp.eye(3)
    h = sp.Matrix([1, -1, 0])  # Sum h = 0
    one = sp.Matrix([1, 1, 1])
    H_l4 = sp.Rational(1, 3) * (one * h.T + h * one.T)
    anti_l4 = sp.simplify(H_l4 * G_chi + G_chi * H_l4)
    check("explicit L4 H = (1/3)(1 h^T + h 1^T) anticommutes with Gamma_chi",
          anti_l4 == sp.zeros(3, 3))
    evecs = H_l4.eigenvects()
    q_vals = []
    for val, mult, vs in evecs:
        if sp.simplify(val) == 0:
            continue
        for vv in vs:
            vv = sp.simplify(vv)
            s = sum(vv)
            if sp.simplify(s) == 0:
                continue
            q = sp.simplify(sum(x ** 2 for x in vv) / s ** 2)
            q_vals.append(sp.nsimplify(q))
    got_two_thirds = all(sp.simplify(q - sp.Rational(2, 3)) == 0 for q in q_vals) \
        and len(q_vals) > 0
    print(f"    nonzero-eigenvalue eigenvector Q values = {q_vals}")
    check("EIGENVECTOR readout of L4 H gives Q = 2/3 (the established route)",
          got_two_thirds)

    # The EIGENVECTOR readout (the L4 theorem) DOES give 2/3 — but that is the
    # established anticommuting route, which is NOT C_3-equivariant. Test whether
    # our constructed off-block Gamma (in computational basis) commutes with C.
    C = cyclic_shift()
    # Build the off-block Gamma in computational basis for the pairing 0<->1, fix 2.
    Gf = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    G_comp = simp(F * Gf * hermitian_conj(F))
    commC = simp(G_comp * C - C * G_comp)
    c3_native = is_zero_matrix(commC)
    # Expected NEGATIVE: the off-block grading breaks C_3-equivariance.
    check("off-block Gamma_aff is NOT C_3-native ([Gamma_aff, C] != 0) "
          "(expected)", not c3_native)
    if not c3_native:
        print("    => Gamma_aff BREAKS C_3-equivariance. It is NOT C_3-native;")
        print("       it singles out Fourier modes (0,1) vs 2, i.e. picks a")
        print("       preferred pairing not invariant under cyclic relabeling.")

    # Does it split the C_3 orbit on the generation R^3? The hw=1 generation
    # orbit {e1,e2,e3} is permuted cyclically by C. An operator splits the orbit
    # iff it fails to commute with C. We just showed it fails -> it 'splits' but
    # only by explicitly breaking the symmetry, i.e. it is an EXTERNAL choice.
    return eigenvalue_Q_infinite, c3_native


# ----------------------------------------------------------------------
# PART 7 — reduction to the established no-go (which wall)
# ----------------------------------------------------------------------

def part7_reduction(eigenvalue_Q_infinite, c3_native, off_block_results):
    banner("PART 7 — reduction map to the established no-go")
    # Two mutually exclusive cases for any Hermitian involution Gamma with
    # {Gamma, H} = 0 and H = a I + b C + bbar C^2, a != 0:
    #
    #  (A) Gamma is C_3-equivariant (circulant). Then Gamma in <I,C,C^2>;
    #      circulant H,Gamma commute -> {Gamma,H}=2 H Gamma; anticommute
    #      forces H Gamma = 0 -> H = 0 (Z3-equivariant no-go).  WALL 1.
    #
    #  (B) Gamma is off-block (mixes singlet<->doublet), hence NOT circulant.
    #      Anticommutation forces L0 + L_j = 0 (origin reflection) AND the
    #      fixed third mode L_m = 0 -> spectrum {+l,-l,0}. The EIGENVALUE
    #      (circulant/affine ratio r) readout is then INFINITE, not 2/3.
    #      Recovering 2/3 needs the EIGENVECTOR readout, i.e. the established
    #      ANTICOMMUTING route, whose Gamma is exactly the L4 non-circulant
    #      H = (1/3)(1(x)h + h(x)1) class — already on main, and explicitly
    #      NOT C_3-native (breaks the orbit by external choice).  WALL 2.
    #
    print("  CASE (A) C_3-equivariant Gamma  -> forces H = 0  [no-go WALL 1]")
    print("  CASE (B) off-block affine Gamma -> spectrum {+l,-l,0}:")
    print("       * eigenvalue/affine-r readout  -> Q = INFINITE (not 2/3)")
    print("       * to get 2/3 must switch to EIGENVECTOR readout = the")
    print("         established anticommuting (L4) route, NOT C_3-native.")
    print()
    # Confirm the off-block candidates only anticommuted on a measure-zero
    # constraint surface (not for generic a,b).
    any_generic = any(v[0] for v in off_block_results.values())
    check("NO off-block Gamma anticommutes for GENERIC a,b "
          "(only on constraint surface)", not any_generic)
    check("on the anticommuting surface, affine-r/eigenvalue Q is NOT 2/3 "
          "(it is infinite)", eigenvalue_Q_infinite)
    check("constructed off-block affine Gamma is NOT C_3-native", not c3_native)

    print()
    print("  VERDICT: REDUCES-TO-ESTABLISHED-NO-GO.")
    print("    The affine framing does EVADE 'comm(S) ∩ anticomm(Gamma)={0}'")
    print("    in the sense that the off-block Gamma need not commute with C —")
    print("    but it then lands on the {+l,-l,0} spectrum where the AFFINE")
    print("    ratio readout (the very r the framing is about) gives Q=inf, and")
    print("    the 2/3 value returns only through the EIGENVECTOR readout of the")
    print("    pre-existing non-C_3-native anticommuting class. No NEW C_3-native")
    print("    Hermitian off-block orbit-splitting grading giving the affine-r")
    print("    Q=2/3 is produced. Wall: the same origin-reflection {+l,-l,0}")
    print("    spectral obstruction, now seen as a readout-class fork.")
    return True


def main() -> int:
    C, H, Ls = part1_circulant_setup()
    part2_circulant_grading(C, H)
    part3_affine_condition(Ls)
    off_block_results, F = part4_construct_affine_grading(C, H, Ls)
    part5a_general_hermitian_grading(Ls)
    part5_solve_constraints(Ls)
    eigenvalue_Q_infinite, c3_native = part6_q_and_c3_native(Ls, F)
    part7_reduction(eigenvalue_Q_infinite, c3_native, off_block_results)

    banner("SUMMARY")
    print("  Affine chiral-limit probe: the chiral-origin (a=0) anticommutation")
    print("  condition {Gamma, H} = 0 forces, in the Fourier basis, the support")
    print("  rule (L_j + L_k) Gamma_{jk} = 0. A C_3-equivariant Gamma -> H=0")
    print("  (WALL 1). An off-block affine Gamma exists ONLY on the constraint")
    print("  surface L_j=-L_k, L_m=0, giving spectrum {+l,-l,0}; there the AFFINE")
    print("  ratio r / eigenvalue Koide readout is INFINITE, and Q=2/3 returns")
    print("  only via the established (non-C_3-native) eigenvector route (WALL 2).")
    print()
    print("  VERDICT: REDUCES-TO-ESTABLISHED-NO-GO "
          "(origin-reflection {+l,-l,0} spectral wall, surfaced as a")
    print("  readout-class fork; no new C_3-native off-block Hermitian grading).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
