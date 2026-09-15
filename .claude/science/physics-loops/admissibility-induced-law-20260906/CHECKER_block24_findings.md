# Refuting pass — block 24 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block24_unrecorded_sites.py`, refuting pass `specs/supervisor_control_block24_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the plaquette and cube witnesses (Q4) | exact enumeration with integer weights and rational normalization | floating-point tensor contraction (`einsum`) of the same laws | agree to `10^{−9}` at all three triples and on the cube |
| one-attachment constancy (Q2) | pendant paths of two and three sites, symbolically in `(p, q, r)` | six random connected pendant components of two to four sites on `Z³`, attached to the origin through all their bonds to it, at random positive weights | constant to relative `6·10^{−15}` |
| two-attachment nonconstancy (Q3) | `φ²`, `φ^{k+2}` and the two-corner square, symbolically | six random bridging components between the origin and `(2,0,0)` at random positive weights, through the isotypic eigenvalues `λ_odd`, `λ_even` of the `6×6` factor; the degenerate rule `p = q = r` | a nonzero sector eigenvalue in every random case; both vanish at `p = q = r` |
| the sphere factor (Q3 e) | the closed form symbolically; the series positivity | Gauss quadrature at `v_x·v_y ∈ {−1, 0, 1/2, 1}` at `β = 13/10` | agrees to nine digits (`4π` at `v_x·v_y = −1`) |
| the average identity (Q1) | exact on the plaquette-plus-site | floats on the same window | residual `9·10^{−19}` |

Findings: none in the primary. The control's first draft used a `3×3` window with three pendant sites for the forest witness, which is `6^{12}` configurations and infeasible; it was replaced by the plaquette with a pendant path and a pendant site before the contract. The note's first wording called the two unrecorded corners of a plaquette "a two-site component"; they are two single-site components attached to the same pair of recorded sites, and the wording was corrected before the census.

Attempts to refute (nothing refuted): the one-attachment argument when the component is attached through several bonds to the same recorded site (the substitution `u → gu` acts on all of them at once); the same argument for a component that is a cycle rather than a tree (nothing in the argument uses acyclicity); the covariance of the two-attachment factor when the attachments are at the same exterior site (`φ²`) or at distinct sites (`φTφ`); the case `p + q = 2r` at `(3,1,2)`, where the even sector of `φ` vanishes but the odd one does not; the R3-average identity as a definition rather than a theorem (it is the definition of the conditional law, stated for the record). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
