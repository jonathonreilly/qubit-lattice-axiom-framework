# CPT Exact Preservation in the Cl(3) Staggered Framework

**Status:** audited_conditional. Retained scope (post-2026-05-19 narrowing):
the Theta_H-odd Hamiltonian-sector identities that the primary runner
verifies on the real anti-Hermitian D-level and on the Hermitian lift
H = iD. The all-SME-coefficients corollary is demoted to bounded /
admitted-bridge status pending a retained SME bilinear-operator-basis
derivation (see audit-conditional repair block below).
**Bridge:** [PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md](./PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md)

## 2026-05-19 audit-conditional repair

The 2026-05-18 audit verdict (`audited_conditional`, terminal) on
`cpt_exact_note` recorded:

> missing_bridge_theorem: add a retained SME bilinear-operator-basis-on-
> staggered-substrate derivation proving canonical normalization and basis
> completeness, OR narrow this note to the exact finite-lattice Theta_H/CP
> identity without the all-SME-coefficients corollary.

This repair takes the second branch. The retained statement of this note
is now restricted to the Theta_H-odd Hamiltonian-sector identities that the
primary runner verifies directly. The SME-coefficient identification step
-- the claim that "`a_mu`, `b_mu`, `d_{mu nu}`, `e_mu`, `f_mu`, `g_{mu nu rho}`
all vanish identically" as canonical SME coefficients -- is an **admitted
bridge** pending a separate retained derivation. What the runner actually
computes are residuals `(np.trace(H^{odd}_mu) / N, ||H^{odd}_mu||_F)` of
the CPT-odd part of the finite-lattice Hamiltonian. These are the
**Theta_H-odd Hamiltonian-sector residuals**, and they vanish; this is
the retained content. The identification of those residuals with the
canonical SME coefficients `a_mu`, `b_mu`, ... requires a retained
operator-basis bridge that this note no longer claims to supply.

This narrowing is a demotion of the SME-corollary statement, not a
promotion of new content. The runner output and `D`-level identities
are unchanged.

## Status
**Primary runner:** `scripts/frontier_cpt_exact.py`


Retained: the Theta_H-odd Hamiltonian-sector identities on even periodic
lattices. All checks pass on `L = 4, 6, 8`
(`PASS=53 FAIL=0`), and the runner now rejects odd `L`.

The original runner proves the `D`-level identities for the real
anti-Hermitian staggered hopping operator. The physical Hermitian
Hamiltonian claim is now carried by the bridge note above, which
explicitly handles the antiunitary `i -> -i` step in `H = iD` and verifies
the Theta_H-odd zero sector on the Hermitian lift. The SME-coefficient
labeling of that zero sector is admitted, not retained, pending a
canonical operator-basis derivation.

## Theorem / Claim

**Retained theorem (Theta_H-odd Hamiltonian-sector identities).**
The staggered Cl(3) Hamiltonian on Z^3 with periodic boundary conditions
and even side length `L` satisfies, at the finite-lattice operator level,
the identities `C H C = -H`, `P H P = -H`, `T H T^{-1} = H`,
`[CPT, H] = 0`, and `H^{odd} := (H - CPT*H*(CPT)^{-1})/2 = 0`. All
direction-resolved Hamiltonian-sector residuals
`trace(H^{odd}_mu)/N` and `||H^{odd}_mu||_F` vanish identically on
the lattice sizes verified by the runner.

**Admitted (not retained here):** the identification of these vanishing
Hamiltonian-sector residuals with the canonical SME coefficients
`a_mu, b_mu, d_{mu nu}, e_mu, f_mu, g_{mu nu rho}`. That identification
requires a retained SME bilinear-operator-basis-on-staggered-substrate
derivation proving canonical normalization and basis completeness, which
this note does not supply.

**Discrete symmetry pattern:**

| Symmetry | Action on H | Status |
|----------|-------------|--------|
| C        | H -> -H     | NOT a symmetry of H (spectral flip) |
| P        | H -> -H     | NOT a symmetry of H (spectral flip) |
| T        | H -> H      | IS a symmetry (H is real) |
| CP       | H -> H      | IS a symmetry |
| CT       | H -> -H     | NOT a symmetry |
| PT       | H -> -H     | NOT a symmetry |
| CPT      | H -> H      | IS a symmetry (EXACT) |

This pattern matches the Standard Model: C and P are individually
violated, CP is preserved at tree level, and CPT is exactly preserved.

## Assumptions

1. Cl(3) staggered framework on Z^3 with periodic boundary conditions.
2. Even lattice size L (required for parity to be well-defined).
3. No additional interactions beyond the free staggered Hamiltonian.
4. The physical-Hamiltonian statement uses the bridge theorem's Hermitian
   lift `H = iD` and antiunitary representative `Theta_H = P K`.

## What Is Actually Proved

### Exact (theorem-grade):

1. **C operator**: The sublattice parity epsilon(x) = (-1)^{x1+x2+x3}
   is a real, diagonal, involutory operator satisfying C H C = -H exactly.

2. **P operator**: Spatial inversion x -> -x mod L is a real, involutory
   permutation satisfying P H P = -H exactly.

3. **T operator**: Complex conjugation acts trivially on H because all
   staggered phases and hoppings are real: T H T^{-1} = H* = H.

4. **CPT combined**:
   - CPT * H * (CPT)^{-1} = C * P * H * P * C = C * (-H) * C = -(-H) = H.
   - [CPT, H] = 0 verified numerically to machine precision on L = 4, 6, 8.
   - All residuals are exactly 0.00e+00 (not just small -- identically zero).

5. **Theta_H-odd Hamiltonian-sector residuals** (narrowed 2026-05-19):
   The CPT-odd part of the (Hermitian-lifted) Hamiltonian vanishes
   identically as a finite-lattice operator residual:
   - H^{odd} = (H - CPT*H*(CPT)^{-1})/2 = 0.
   - The direction-resolved Hamiltonian-sector residuals
     `trace(H^{odd}_mu)/N` vanish (denoted `a_mu` in the runner output;
     this is a runner-internal label, **not** an identification with the
     canonical SME `a_mu` coefficient -- see "Admitted" above and the
     audit-conditional repair block).
   - The Frobenius norm ||H^{odd}|| = 0 at every lattice size tested.

   The promotion of these vanishing residuals to "all CPT-odd SME
   coefficients vanish identically" is **admitted, not retained**,
   pending a canonical bilinear-operator-basis bridge.

6. **Taste-space verification**: CPT invariance verified at 7 BZ points
   including all high-symmetry points and a generic point.

7. **Cl(3) automorphism**: The combined CP operator maps each KS gamma
   to minus itself (G_mu -> -G_mu), acting as the grading automorphism
   of the Clifford algebra. (CP)^2 = I.

## What Remains Open

1. Extension to the interacting theory (gauge fields, Yukawa couplings).
   The free-field CPT theorem proved here is necessary but not sufficient
   for the full interacting framework.

2. CP violation from CKM-type phases. The free staggered Hamiltonian has
   exact CP, but physical CP violation requires complex phases in the
   interaction sector. The framework must accommodate this without
   breaking CPT.

3. Connection to the CPT theorem in continuum QFT (Jost 1957, Streater-
   Wightman). The lattice proof is self-contained but the relationship
   to the axiomatic continuum proof should be clarified.

## How This Changes The Paper

This is a clean exact result on the Hamiltonian-sector identities that
can appear in the paper's symmetry section. The retained statement is:

> The staggered Cl(3) Hamiltonian on even periodic `Z^3` lattices is
> exactly CPT-invariant at the finite-lattice operator level.
> C and P individually map H -> -H, while T acts trivially on the real
> Hamiltonian. The product CPT preserves H identically, and the
> CPT-odd part `H^{odd}` vanishes identically as a finite-lattice
> operator on all sizes tested.

The further statement "all CPT-odd Standard-Model Extension coefficients
vanish" is **admitted, not retained**, pending a canonical SME
operator-basis bridge (see the 2026-05-19 audit-conditional repair block
at the top of this note).

This is a useful structural consistency check: any framework claiming
to reproduce SM physics must have exact CPT. The Cl(3) staggered
framework achieves this automatically from the reality of the staggered
phases and the algebraic structure of C and P.

The individual C and P violation (both send H -> -H) is also
physically correct: it reflects the chiral nature of the staggered
fermion, which is the lattice origin of parity violation.

## Commands Run

```
python3 scripts/frontier_cpt_exact.py
# Exit code: 0
# PASS=53  FAIL=0   (for L = 4, 6, 8; odd L rejected by design)
```
