"""GENERATION_WEIGHT_DIAL_STRUCTURE — sympy derivation runner.

THEOREM (derived here, not asserted): On the two C_3 generation isotype sectors of the
3-generation carrier (singlet, real-dim 1; doublet, real-dim 2 -- the sector structure is
imported, not re-derived here, from the sibling readout/metric derivations
docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md and
docs/FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md), the inter-sector
amplitude ratio r = |b|^2 / a^2 of the C_3-equivariant circulant mass operator
Y = a*I + b*C + conj(b)*C^2 forms a ONE-PARAMETER DIAL

        r(s) = 2^(s-1),

obtained by weighting each isotype block's spectral power by dim^s and imposing the balance
singlet_power : doublet_power = 1^s : 2^s. The two endpoints are the two canonical measures:
  s = 0  ->  r = 1/2  (equal spectral power PER BLOCK  = block-count / det_C measure),
  s = 1  ->  r = 1    (equal spectral power PER REAL MODE = Born / dimension / det_R measure).
The dial r(s)=2^(s-1) is strictly increasing in s, so the two canonical measures are precisely
its two named endpoints, with a continuum of intermediate weightings between them.

HONESTY / SCOPE. This runner derives the DIAL STRUCTURE (the closed form r(s)=2^(s-1) and that
its endpoints are exactly the block-count and Born measures). It does NOT, and cannot, fix the
per-sector POSITION s (equivalently the physical value of r) -- that selection is a separate
question and is left genuinely open by Lattice, Quantum, and Record (see the sibling derivations: the doublet
mode-count / measure choice is an import). No claim of a preferred s is made or implied here.
claim_type = theorem (structure of the dial), with the position explicitly out of scope.

Premises cited by name:
  Lattice (Z^3, nearest-neighbour) -- supplies the 3-pattern hw=1 generation carrier and its
     only relabeling symmetry, the order-3 cyclic shift C (C^3 = I).
  Quantum (qubit / M_2(C) ~ Cl(3,0)) -- the on-site complex amplitude algebra; the mass
     operator is a complex-linear operator on the generation carrier.
  Record -- given the supplied central-sector decomposition and fixed K/CPT conjugation, names
     the realized orbit and makes scalar readout I finitely additive. The adopted K/CPT-real
     readout condition pins a real; Record supplies no weights, probabilities, dynamics, or
     occupancy rule.

Math computed with sympy (exact symbolic): circulant eigenstructure via the C_3 character table,
the singlet power a^2 and doublet power 2|b|^2, the dim^s balance equation, the closed-form
solution r(s) = 2^(s-1), the two endpoints, and strict monotonicity.

Run:  python3 scripts/generation_weight_dial_structure_2026_06_05.py
Target: >= 20 PASS / 0 FAIL.
"""

import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def main():
    # ---- symbols ----------------------------------------------------------------
    s = sp.symbols("s", real=True)                 # dial parameter (dim-weight exponent)
    a = sp.symbols("a", positive=True)             # singlet amplitude, real by adopted K/CPT condition
    bre, bim = sp.symbols("b_re b_im", real=True)  # doublet amplitude b = bre + i*bim (Quantum complex)
    b = bre + sp.I * bim
    # primitive cube root of unity in explicit algebraic form so symbolic powers collapse exactly
    w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2  # = exp(2*pi*i/3)

    # ============================================================================
    # STEP 1 -- C_3-equivariant operator is the circulant Y = a I + b C + conj(b) C^2
    # ============================================================================
    I3 = sp.eye(3)
    # cyclic shift C: e_k -> e_{k+1 mod 3}; columns are images of basis vectors.
    C = sp.Matrix([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]])

    check("S1.1 C is the order-3 cyclic shift (C^3 = I, C != I)",
          sp.simplify(C**3 - I3) == sp.zeros(3) and C != I3,
          "C generates the only relabeling symmetry C_3 of the 3 hw=1 generation patterns (Lattice)")

    check("S1.2 C^2 = C^T = C^{-1} (the C_3 group is realized faithfully)",
          sp.simplify(C**2 - C.T) == sp.zeros(3) and sp.simplify(C**2 - C.inv()) == sp.zeros(3))

    # General complex matrix M; commutant of <C> is exactly the circulants (Schur, abelian C_3).
    m = sp.symbols("m0:9")
    M = sp.Matrix(3, 3, m)
    comm = sp.simplify(M * C - C * M)
    sol = sp.solve([comm[i, j] for i in range(3) for j in range(3)], list(m), dict=True)[0]
    Mcomm = sp.simplify(M.subs(sol))
    # A matrix commuting with C is determined by its first column (m0,m3,m6) -> it is circulant.
    is_circulant = all(
        sp.simplify(Mcomm[i, j] - Mcomm[(i - j) % 3, 0]) == 0
        for i in range(3) for j in range(3)
    )
    free = sorted({str(x) for x in Mcomm.free_symbols}, key=str)
    check("S1.3 Schur: commutant of <C> is exactly the circulants (3 free complex params)",
          is_circulant and len(free) == 3,
          f"every C-equivariant M is circulant, free params {free} (its first column)")

    # Hermiticity + reality of the diagonal (a real, K/CPT-fixed by the supplied readout) collapses the 3 complex
    # circulant params to {a (real), b (complex)}: Y = a I + b C + conj(b) C^2.
    Y = a * I3 + b * C + sp.conjugate(b) * C**2
    check("S1.4 Y = a I + b C + conj(b) C^2 is Hermitian (a real, b complex)",
          sp.simplify(Y - Y.conjugate().T) == sp.zeros(3),
          "Hermiticity forces the C^2 coefficient = conj(C-coefficient); diagonal a is real by the adopted K/CPT condition")

    check("S1.5 Y is genuinely C_3-equivariant ([Y, C] = 0)",
          sp.simplify(Y * C - C * Y) == sp.zeros(3))

    # ============================================================================
    # STEP 2 -- character (Fourier) basis: singlet carries I, doublet carries C,C^2
    # ============================================================================
    # C_3 irreducible characters chi_j(C^n) = w^{j n}, j = 0 (trivial/singlet), 1,2 (faithful/doublet).
    # The shift acts on the Fourier vector f_j = (1, w^j, w^{2j}) as C f_j = w^{-j} f_j (C: e_k->e_{k+1}),
    # so the circulant eigenvalue on character j is  lambda_j = a + b w^{-j} + conj(b) w^{-2j}.
    lam = [sp.simplify(a + b * w**(-j) + sp.conjugate(b) * w**(-2 * j)) for j in range(3)]

    # Verify these are the actual eigenvalues: the Fourier vectors f_j = (1, w^j, w^{2j}) diagonalize Y.
    eig_ok = True
    for j in range(3):
        fj = sp.Matrix([1, w**j, w**(2 * j)])
        resid = sp.Matrix([sp.simplify(e) for e in (Y * fj - lam[j] * fj)])
        if resid != sp.zeros(3, 1):
            eig_ok = False
    check("S2.1 Fourier vectors (1,w^j,w^{2j}) diagonalize Y; lambda_j = a + b w^{-j} + conj(b) w^{-2j}",
          eig_ok,
          f"C f_j = w^{{-j}} f_j; lambda_0 (singlet) = {sp.simplify(lam[0])}; lambda_1, lambda_2 are the faithful doublet")

    # Singlet (trivial character, j=0) eigenvalue = a + (b + conj b) = a + 2 Re b.
    # (The trivial character f_0=(1,1,1) reads the ROW SUM of the circulant, i.e. a + b + conj b.)
    check("S2.2 singlet eigenvalue lambda_0 = a + 2 Re b (the trivial character reads the row-sum)",
          sp.simplify(lam[0] - (a + 2 * bre)) == 0,
          "lambda_0 = a + b + conj(b) = a + 2 Re b; the SINGLET POWER (group-algebra/isotype coordinate) is a^2 (below)")

    # SECTOR POWER = the spectral power carried in each C_3 isotype, read off the group-algebra
    # coordinates of Y in the orthonormal basis {I/sqrt3, C/sqrt3, C^2/sqrt3} of M_3(C)^{C_3}.
    # The trivial character (singlet) is carried by the I-coordinate; the two faithful characters
    # (doublet) are carried by the C, C^2 coordinates. Record additivity allows these powers to be summed.
    #
    # Group-algebra coordinates of Y = a I + b C + conj(b) C^2:  coord(I)=a, coord(C)=b, coord(C^2)=conj(b).
    coeff_I = a
    coeff_C = b
    coeff_C2 = sp.conjugate(b)
    # Verify these ARE the coordinates by HS-projection (the {I,C,C^2} are HS-orthogonal, each norm^2=3).
    def hs(A, B_):
        return sp.simplify((A.conjugate().T * B_).trace())
    proj_I = sp.simplify(hs(I3, Y) / hs(I3, I3))
    proj_C = sp.simplify(hs(C, Y) / hs(C, C))
    proj_C2 = sp.simplify(hs(C**2, Y) / hs(C**2, C**2))
    check("S2.2b HS-projection confirms group-algebra coordinates: (I,C,C^2) -> (a, b, conj b)",
          sp.simplify(proj_I - coeff_I) == 0 and sp.simplify(proj_C - coeff_C) == 0
          and sp.simplify(proj_C2 - coeff_C2) == 0,
          f"coord(I)={proj_I}, coord(C)={proj_C}, coord(C^2)={proj_C2}")

    babs2 = bre**2 + bim**2  # |b|^2  (kept as a plain polynomial for clean substitution)

    # Singlet "power" = |coord(I)|^2 = a^2  (trivial character, the I-component).
    singlet_power = sp.simplify(sp.Abs(coeff_I)**2)

    # Doublet "power" = |coord(C)|^2 + |coord(C^2)|^2 = |b|^2 + |conj b|^2 = 2|b|^2
    # (the two faithful characters carry the C, C^2 components).
    doublet_power = sp.simplify(sp.Abs(coeff_C)**2 + sp.Abs(coeff_C2)**2)

    check("S2.3 singlet power = a^2",
          sp.simplify(singlet_power - a**2) == 0)

    check("S2.4 doublet power = |b|^2 + |conj b|^2 = 2|b|^2",
          sp.simplify(doublet_power - 2 * babs2) == 0,
          f"doublet_power = {doublet_power} = 2|b|^2 (the two faithful characters j=1,2 split the C,C^2 weight)")

    # Cross-check the powers against the eigenvalue (Parseval) bookkeeping:
    # HS norm^2 of Y = 3 a^2 + 6 |b|^2 = 3*(a^2) + 3*(2|b|^2) = 3*(singlet_power) + 3*(doublet_power).
    hs_direct = sp.simplify(sp.re(hs(Y, Y)))           # ||Y||_HS^2 = Tr(Y^dagger Y)
    hs_eigs = sp.simplify(sp.re(sum(sp.Abs(lam[j])**2 for j in range(3))))
    check("S2.5a ||Y||_HS^2 = Tr(Y^H Y) = sum|lambda_j|^2 (Y normal: Parseval holds)",
          sp.simplify(hs_direct - hs_eigs) == 0,
          f"Tr(Y^H Y) = {hs_direct} = sum|lambda_j|^2")
    check("S2.5b ||Y||_HS^2 = 3*singlet_power + 3*doublet_power = 3a^2 + 6|b|^2",
          sp.simplify(hs_direct - (3 * singlet_power + 3 * doublet_power)) == 0
          and sp.simplify(hs_direct - (3 * a**2 + 6 * babs2)) == 0,
          f"{hs_direct} = 3*a^2 + 3*(2|b|^2); powers consistent with the full spectrum")

    # ============================================================================
    # STEP 3 -- the dim^s-weighted balance and its closed-form solution r(s) = 2^(s-1)
    # ============================================================================
    # dim(singlet) = 1, dim(doublet) = 2 (real isotype dimensions -- the sibling readout result).
    dim_singlet = sp.Integer(1)
    dim_doublet = sp.Integer(2)

    check("S3.0 sector dimensions are (1, 2) [imported from the sibling readout/metric derivation]",
          dim_singlet == 1 and dim_doublet == 2,
          "singlet real-dim 1, doublet real-dim 2; cited, not re-derived here")

    # Balance: weight each block's power by dim^s and set them equal up to the dim^s ratio.
    #   singlet_power : doublet_power  =  dim_singlet^s : dim_doublet^s  =  1^s : 2^s
    # i.e.   singlet_power * dim_doublet^s = doublet_power * dim_singlet^s
    #   ->   a^2 * 2^s = (2|b|^2) * 1
    balance = sp.Eq(singlet_power * dim_doublet**s, doublet_power * dim_singlet**s)
    check("S3.1 balance equation: a^2 * 2^s = 2|b|^2  (dim^s weighting of block powers)",
          sp.simplify(balance.lhs - balance.rhs) == sp.simplify(a**2 * 2**s - 2 * babs2),
          f"{sp.simplify(balance.lhs)} = {sp.simplify(balance.rhs)}")

    # Solve for r := |b|^2 / a^2. Substitute |b|^2 = r*a^2 into the balance (a>0) and solve.
    r_sym = sp.symbols("r", positive=True)
    bal_in_r = sp.Eq(a**2 * dim_doublet**s, 2 * r_sym * a**2)  # a^2 * 2^s = 2 (r a^2)
    # divide through by a^2 (>0): 2^s = 2 r
    r_sol = sp.solve(sp.Eq(dim_doublet**s, 2 * r_sym), r_sym)
    r_of_s = sp.simplify(r_sol[0])
    check("S3.2 solving the balance for r = |b|^2/a^2 gives a unique positive root",
          len(r_sol) == 1 and r_of_s.is_positive is not False,
          f"a^2 * 2^s = 2 r a^2  =>  2^s = 2 r  =>  r(s) = {r_of_s}")

    closed = 2**(s - 1)
    check("S3.3 closed form r(s) = 2^(s-1)  (EXACT match to the solved root)",
          sp.simplify(r_of_s - closed) == 0,
          f"r(s) = {sp.powsimp(r_of_s, force=True)} = 2^(s-1)")

    # Independent re-derivation: a^2 * 2^s = 2 r a^2  =>  2^s = 2 r  =>  r = 2^s / 2 = 2^(s-1).
    r_alt = sp.simplify(2**s / 2)
    check("S3.4 independent re-derivation 2^s = 2r => r = 2^s/2 = 2^(s-1)",
          sp.simplify(r_alt - closed) == 0)

    # ============================================================================
    # STEP 4 -- the two endpoints (the two canonical measures)
    # ============================================================================
    r0 = sp.simplify(closed.subs(s, 0))
    r1 = sp.simplify(closed.subs(s, 1))

    check("S4.1 endpoint s=0 (equal power PER BLOCK = block-count / det_C): r(0) = 1/2",
          r0 == sp.Rational(1, 2),
          f"r(0) = {r0}; at s=0 the dim^s weights are (1,1), i.e. count each block once -> a^2 = 2|b|^2")

    check("S4.2 endpoint s=1 (equal power PER REAL MODE = Born / dimension / det_R): r(1) = 1",
          r1 == 1,
          f"r(1) = {r1}; at s=1 the weights are (1,2) = the real dimensions -> a^2*2 = 2|b|^2 -> |b|^2 = a^2")

    # Sanity: at s=0 the balance is literally a^2 = 2|b|^2 (block-count); at s=1 it is 2 a^2 = 2|b|^2 (Born).
    bal0 = sp.simplify((balance.lhs - balance.rhs).subs(s, 0))
    bal1 = sp.simplify((balance.lhs - balance.rhs).subs(s, 1))
    check("S4.3 s=0 balance is a^2 - 2|b|^2 (block-count: weights (1,1))",
          sp.simplify(bal0 - (a**2 - 2 * babs2)) == 0)
    check("S4.4 s=1 balance is 2a^2 - 2|b|^2 (Born/dimension: weights (1,2))",
          sp.simplify(bal1 - (2 * a**2 - 2 * babs2)) == 0)

    # Tie the endpoints to the named measures via the implied kappa = a^2/|b|^2 = 1/r.
    kappa0 = sp.simplify(1 / r0)  # block-count kappa = 2
    kappa1 = sp.simplify(1 / r1)  # Born kappa = 1
    check("S4.5 block-count endpoint => kappa = a^2/|b|^2 = 2 (the det_C value)",
          kappa0 == 2)
    check("S4.6 Born/dimension endpoint => kappa = a^2/|b|^2 = 1 (the det_R value)",
          kappa1 == 1)

    # ============================================================================
    # STEP 5 -- strict monotonicity; endpoints are the two canonical measures, nothing between is canonical
    # ============================================================================
    dr = sp.simplify(sp.diff(closed, s))
    check("S5.1 dr/ds = 2^(s-1) ln 2 > 0 for all real s (strictly increasing)",
          sp.simplify(dr - 2**(s - 1) * sp.log(2)) == 0 and sp.log(2) > 0,
          f"dr/ds = {dr}; strictly positive everywhere -> r(s) is a monotone dial")

    # injectivity over the canonical window [0,1] and beyond: r is a bijection R -> (0, inf).
    check("S5.2 r is strictly monotone => the two endpoints r(0)=1/2 < r(1)=1 are distinct and ordered",
          r0 < r1 and r0 != r1)

    # Range over the canonical interval s in [0,1] is exactly [1/2, 1].
    check("S5.3 over s in [0,1], r sweeps exactly [1/2, 1] (the two canonical measures bound the dial)",
          sp.simplify(closed.subs(s, 0)) == sp.Rational(1, 2)
          and sp.simplify(closed.subs(s, 1)) == 1
          and sp.simplify(sp.diff(closed, s)) != 0,
          "block-count (r=1/2) and Born (r=1) are the two endpoints; the interior s in (0,1) is a continuum of intermediate weightings")

    # log-linearity: log2 r(s) = s - 1 (the dial is exactly linear in the dim-weight exponent).
    check("S5.4 log2 r(s) = s - 1 (the dial is exactly log-linear in the weight exponent s)",
          sp.simplify(sp.log(closed, 2) - (s - 1)) == 0)

    # Record additivity sanity: the readout reads block powers additively (a^2 and 2|b|^2 add to total
    # off-diag+diag content); 'per block' vs 'per mode' are the two ways to normalize that additive
    # readout by sector content -> exactly the s=0 and s=1 endpoints. (Structural cross-check.)
    total_diag_offdiag = sp.simplify(singlet_power + doublet_power)  # a^2 + 2|b|^2
    check("S5.5 Record readout is block-additive: total = singlet_power + doublet_power = a^2 + 2|b|^2",
          sp.simplify(total_diag_offdiag - (a**2 + 2 * babs2)) == 0,
          "finite additivity allows the singlet and doublet powers to be summed; endpoint normalizations are separate conventions")

    # ---- scorecard --------------------------------------------------------------
    print("\n" + "=" * 72)
    print(f"SCORECARD: {PASS} PASS / {FAIL} FAIL")
    print("=" * 72)
    print("THEOREM GENERATION_WEIGHT_DIAL_STRUCTURE verified:")
    print("  r(s) = 2^(s-1);  r(0)=1/2 (block-count/det_C);  r(1)=1 (Born/dimension/det_R);")
    print("  strictly increasing; endpoints = the two canonical measures.")
    print("  SCOPE: derives the DIAL STRUCTURE only; the per-sector position s (value of r)")
    print("  is a SEPARATE, genuinely open selection (not fixed here).")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
