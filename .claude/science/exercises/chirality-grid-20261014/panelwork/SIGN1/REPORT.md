# SIGN-1: is the X2 corner-package Hamiltonian sign-free for QMC?

**Provenance.** Written by a same-family agent and not refereed. The harness blocked the worker from writing report files, so the supervisor saved this from the worker's final message, lightly condensed. The numbers and file references are the worker's.

## Reading

X2 leaves the two quartic coefficients free. The scan takes (λ1, λ2) = (cos θ, sin θ).

- **SIGN-FREE** where λ1 ≤ 0 and |λ2|/|λ1| is at least about 0.15–0.18 (λ2 ≠ 0). This holds for the ungauged model with global Spin(10). The decomposition is written out below.
- **OPEN** where λ1 > 0.

**Memory breach.** The first run peaked at 586 MiB resident (249 MiB footprint), over the 0.2 GB cap. Every run exceeded the cap on resident memory, which on macOS counts shared library pages. Footprints after the first run were 128–192 MiB. All runs were single-process and lasted at most 61 s.

## Plain words

**The model.** X2's Hamiltonian is the walker plus the filtered Spin(10) quartic:

Q = λ1 Σ B†B + λ2 Σ (BB + h.c.)

**The result.** Standard determinant QMC can run it with no sign problem when:
- the B†B part is attractive or absent (λ1 ≤ 0), **and**
- the fermion-number-breaking BB part is present and not too small.

That region includes the pure BB + h.c. interaction, which is the term that gives the symmetric-mass-generation gap.

**Why.**
1. Pick the rotation plane through Spin(10)'s 9th and 10th directions. It splits each 16 into 8_s ⊕ 8_c.
2. Swap particles and holes in one half. Every piece of the Hamiltonian now conserves particle number.
3. Spin time reversal iσ_y K is then a Kramers symmetry with T² = −1.

That is Wu–Zhang Kramers positivity, i.e. Li–Jiang–Yao's Kramers class.

**How it was checked.**
- A symmetry-reduced semidefinite search found the decomposition.
- On a 4-site cluster (256 Majoranas), every auxiliary-field weight is real and positive: to 1e-13 at weak coupling, and to 4e-7 at strong coupling (W = 8, stabilised).
- Decoupling directly in the ten B channels gives complex weights.

**What this does not cover.**
- λ1 > 0. The other pairs of time-reversal symmetries were not tested.
- Dynamical Standard Model gauge links. The 10 is irreducible as 6 + 4 under G_SM, so there is no invariant 2-plane (proved).
- Whether the mirrors gap symmetrically. The sign-free region is exactly where the 10-vector channel is attractive, which is where GPR and K1 predict symmetry breaking. What QMC can now do is measure that order parameter directly.

## Criteria (comparators)

- Wu–Zhang, PRB 71, 155115 (2005).
- Li–Jiang–Yao, PRB 91, 241117 (2015) and PRL 117, 267002 (2016). The Majorana and Kramers classes each need two anticommuting Majorana time reversals.
- Wei–Wu–Li–Zhang–Xiang, PRL 116, 250601 (2016): Majorana reflection positivity and Majorana Kramers positivity.
- He–You–Xu, arXiv:2603.18278.
- Slagle–You–Xu, PRB 91, 115121 (2015).
- Equivalence (proved): ψ → e^{iπ/4}ψ maps (λ1, λ2) to (λ1, −λ2).

## Results

**P1 (proved; checked).**
- The filter has mixed even- and odd-offset parts, so any symmetry must act the same on every site.
- A uniform Majorana time reversal that preserves the walker conserves particle number: Θ = (iσ_y⊗V)K.
- Preserving Q forces V to implement an O(10) reflection with an odd number k of flipped directions. This gives T− for k ∈ {1, 5, 9} and T+ for k ∈ {3, 7}.
- So the natural 10-channel decomposition has mixed parities and fails every criterion.

**P2/P3.** A single time-reversal symmetry is not restrictive: the linear programs are feasible at all 72 angles for k = 1, 3, 5. For T+ the condition is vacuous (proved). The pre-registered expectation was wrong here, so the work moved to the full two-symmetry criteria under dated follow-up A.

**The Kramers pair with U(1)_c (the main result; checked).**
- The pair is T2 = iσ_y K and T1 = (1⊗iΓ⁹)T2. Both square to −1 and they anticommute. U = 1⊗iΓ⁹ generates U(1)_c, which rotates the (9,10) plane.
- There are 1024 U(1)_c-neutral bilinears in 20 families, each of pure parity. Their 4-forms span an 11-dimensional space, and Q lies in it to 1e-15.
- **SDP scan:** feasible for θ ∈ [190°, 270°] (residual ≤ 3e-8), hence also for θ ∈ [90°, 170°] by the equivalence. Infeasible elsewhere (0.017–0.81).
- **Exactness:** after a minimal-norm correction the residuals are 2e-16 on the sample and ≤ 1e-11 on 20,000 fresh components. All coefficients are strictly inside their allowed signs (margins 0.016–0.32). The sampled map is injective.
- **λ1 = 0 is an exact Fierz identity.** The pure −Σ(BB + h.c.) term decomposes with coefficients (−34, +2, −2, +2) on the Re pairing channels and the opposite on the Im channels (residual 7e-16, margin 2).

**Cluster weights (checked).**
- **Natural decomposition:** not real-positive in 97–100% of configurations, with phases up to 3.0. It has a phase problem.
- **Kramers decomposition:** phase ≤ 4e-13, Kramers pairs to 7e-15, real positive weight; at strong coupling (stabilised) phase ≤ 4e-7.
- **Why the weights are positive (proved, given the decomposition):** every term respects both T1 and T2, and T2 restricted to U(1)_c's +i eigenspace is a Kramers symmetry with T² = −1. So det(1+M_d) = Π|1+λ|² ≥ 0. The argument uses only that the filter is real and flavour-blind, so it covers f_NN, f_F1 and the 3D walker.

## The decomposition

**Channel families.** All are U(1)_c-neutral and orthonormalised within each family:

| Kind | Form | Ranges |
|---|---|---|
| Density | ψ†(σ⊗X)ψ | σ ∈ {1} or {σ_x, σ_y, σ_z}; X ∈ {P_b}, {iP_bΓ^{ab}P_b}, or traceless symmetric on 8_b |
| Pairing, singlet 8v | Re/Im ψ^T(iσ_y⊗Γ^a)ψ | a ≤ 8 |
| Pairing, triplet 8v | Re/Im ψ^T(iσ_yσ_i⊗Γ^aΓ⁹)ψ | i = x, y, z; a ≤ 8 |
| Pairing, singlet 56v | Re/Im ψ^T(iσ_y⊗Γ^{abc}Γ⁹)ψ | a < b < c ≤ 8 |
| Pairing, triplet 56v | Re/Im ψ^T(iσ_yσ_i⊗Γ^{abc})ψ | i = x, y, z; a < b < c ≤ 8 |

**Rule.** Q = Σ c_k O_k² + R, with c ≤ 0 on T2-even channels (real auxiliary field) and c ≥ 0 on T2-odd channels (imaginary auxiliary field).

**Coefficients at θ = 230°:**

| Family | Coefficient |
|---|---|
| singlet-35 | −0.710 |
| triplet-35 | +0.613 |
| singlet-8v Re / Im | −33.58 / +12.50 |
| triplet-8v Re / Im | +0.374 / −0.404 |
| singlet-56v Re / Im | −0.318 / +0.410 |
| triplet-56v Re / Im | +2.227 / −2.230 |

## Open items and consequences

- **λ1 > 0** is open. The untested routes are partners iΓ^A with |A| = 2, 3, 4; pairs built on the k = 5 symmetry; and Wei's Theorem 1. A U(1)_F partner is impossible whenever λ2 ≠ 0.
- **The gauged model** breaks the construction.
- **Lattice panel gate 2** passes for the λ1 ≤ 0 sub-family, via the Kramers class in a particle–hole frame. X2:286 ("establish sign-freeness first") is done for that sub-family.
- **Not affected:** K1's G1/G2, L_X2, NT-3.
- **Cost (suggested):** the d-frame matrix is 32·L³ per time slice, about 16,000 at L = 8, which means cluster scale.

## Files

`PREREG.md`, and `scripts/`:
- `common.py`, `kramers_fams.py`
- `p1_p2_p3_lp`, `pair_kramers_u1c`, `p4_cluster_weights`, `p4c_stable`, `p5_exact_margin`, `p6_fierz_lambda1_zero` (each `.py` / `.out`)
- `kramers_solutions.npy`
