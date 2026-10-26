# Three-loop beta-function Casimirs: imported coefficient check

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** supplied polynomial identity; not a per-graph theorem.
**Primary runner:** `scripts/cl3_closure_c_l1c_2026_05_10_cL1c.py`

## Convention and checked statement

Take a = g²/(16π²), μ² da/dμ² = −Σ β_k a^(k+2), with n_f Dirac
fundamentals and Tr(Ta Tb)=T_F δab. The imported MS result is

β₂ = (2857/54) C_A³
 + [2 C_F² − (205/9) C_F C_A − (1415/27) C_A²] T_F n_f
 + [(44/9) C_F + (158/27) C_A] (T_F n_f)².

At C_A=3, C_F=4/3, T_F=1/2 this gives
β₂=2857/2−5033 n_f/18+325 n_f²/54; at n_f=6 it is −65/2.
These are supplied group and flavor choices, not deductions of physical color
or flavor counts. The runner checks the polynomial with exact arithmetic.

The normalization follows Larin and Vermaseren, hep-ph/9302208, Eqs. (1),
(9), (10), whose Eq. (9) absorbs T_F=1/2. In particular the C_F² T_F n_f
coefficient is 2, not 1/2. All six coefficients must use the same convention.
[Primary reference](https://arxiv.org/abs/hep-ph/9302208).

## Limits of the color-algebra argument

An invariant two-adjoint tensor can be proportional to δab while its scalar
coefficient is a sum of Casimir monomials. For example the fundamental SU(N)
completeness identity gives Σa Ta Tb Ta=(C_F−C_A/2)Tb. Tracing an additional
Tb and summing b yields d_F C_F(C_F−C_A/2), which has two formal channels.
This contraction is an algebraic control, not an enumerated three-loop graph.
It invalidates the inference from external δab to one unique monomial.

The beta function is a renormalized combination of vertex and field
renormalizations (Eq. (4) of the reference), not the gluon self-energy alone
in a general covariant gauge. The latter is gauge dependent. Individual
periods divided by graph automorphism orders do not by themselves supply
counterterms, tensor numerators, statistics signs, or the required combination.
The published cancellation of higher invariants in β₂ does not establish
absence in every diagram. Even absence of n_f³ would not logically exclude
quartic group invariants: flavor degree and invariant degree differ.

## Open obligations and recovery

The old exhaustive per-graph Casimir theorem, single-channel assignment,
period-weight closure and physical Cl₃ derivation are withdrawn here. A full
proof would require a specified diagram set, gauge and subtraction scheme,
explicit contractions and renormalization. No such enumeration is performed.
The historical version remains at baseline f24d17d97d372df977476e4a69674577f31af575
at this path. The finite polynomial check does not certify that historical
claim or any downstream physical identification. No repository premise is
needed for the present supplied-variable identity.
