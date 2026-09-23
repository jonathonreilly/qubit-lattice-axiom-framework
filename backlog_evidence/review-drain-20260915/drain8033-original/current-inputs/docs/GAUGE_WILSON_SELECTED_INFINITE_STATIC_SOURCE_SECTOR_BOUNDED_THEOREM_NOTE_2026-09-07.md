---
claim_id: gauge_wilson_selected_infinite_static_source_sector_bounded_theorem_note_2026-09-07
claim_type: bounded_theorem
runner: scripts/gauge_wilson_selected_infinite_static_source_sector_2026_09_07.py
upstream_dependencies:
  - gauge_wilson_uniform_static_source_energy_bounds_bounded_theorem_note_2026-09-07
claim_scope: "Selected neutral full-local-algebra GNS static charged sector; inherited uniform separation bounds, without convergence of finite charged minima."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The [finite charged-sector parent](GAUGE_WILSON_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md) supplies the uniform estimate. The neutral GNS representation below is built from the **full local link bounded-operator algebra**, not merely its gauge-invariant observable subalgebra. The [exact adverse-control helper](../scripts/gauge_wilson_selected_infinite_static_source_sector_2026_09_07.py) has15 scientific checks and a separate resource guard. It tests the excluded limit inferences and a finite Z3 gauge-projection toy; it does not numerically verify the imported infinite-volume theorem. Both complete original proofs and all three cross-reviews remain in the [historical recovery archive](work_history/review_loop/pr8029/README.md), with exact original identities in its [manifest](work_history/review_loop/pr8029/original-manifest.json). Their independence and timing statements describe the original campaign, not this repair.

# Selected infinite-volume static charged sector

**Type:** bounded_theorem. Conditional on the fixed compact interaction, supplied external color spaces, the reviewed finite charged-sector bound, and Yarotsky's ground-state/resolvent theorems. Historical provenance: the original author recorded freezing this derivation before reading the completed root draft; the candidate route had already been exposed. The exact prospective contract and later reviews are archived. This is not a new independence claim.

Fix one interaction on the infinite cubic link lattice, grouped into three outgoing links per cell, and its nested empty/whole-range finite restrictions. Put h_z=(a/4)K_cell,z and center each four-cell plaquette group so its norm is at most delta=3av/4. Work in the common weak-coupling window of the finite sector estimate and the ground-state theorems. Fix distinct vertices x,y with lattice distance d. Every sufficiently large restriction contains one fixed shortest path between them, so its actual graph distance is d. All finite boundary vertices retain their actual Gauss transformations.

Let (Hcal,pi,Omega) be the neutral limiting ground GNS representation of the full local bounded-operator algebra. Let H>=0 be its Hamiltonian, with H Omega=0, using physical energy units. Tensor with the supplied nine-dimensional fundamental/antifundamental source space E. There is a strongly continuous unitary implementation U(g) of each finite set of local gauge transformations on Hcal, fixing Omega. Define

 C_xy = {xi in Hcal tensor E: (U(g) tensor D_xy(g))xi=xi for every finite-support gauge assignment g}.

This is a closed reducing subspace of H tensor I_E. It is nonzero. Its restricted operator H_xy satisfies

 (4/a)(1-kappa)d <= inf Spec H_xy <= 4d/a,

where kappa is the same uniform finite-sector constant as the linked finite charged-sector parent; in particular kappa<=1/2 gives 2d/a as a lower bound. This is the bottom in a specified neutral-vacuum representation with two external probes. It is not a claim that finite-volume charged minima converge to that bottom.

## 1. Local normality and gauge continuity

The following argument supplies a regularity point that weak-star convergence on the local B(H_local) algebra alone should not silently replace. A cell kinetic operator has compact resolvent: each finite energy window contains finitely many SU(3) Peter-Weyl irreps with finite matrix multiplicity. In a finite volume remove h_z and the at most four interaction groups touching z. The remaining Hamiltonian acts trivially on that cell; denote its bottom by E_rest. The ground expectation obeys E_Lambda>=E_rest+<h_z>-4delta. A product trial with the cell vacuum gives E_Lambda<=E_rest+4delta. Hence <h_z><=8delta, uniformly in volume once z is included.

For any fixed finite collection F of cells, <sum_F h_z><=8delta|F|. Let P_R be its finite-rank spectral projection below energy R. Each reduced density matrix rho obeys Tr((I-P_R)rho)<=8delta|F|/R. The gentle-compression inequality

    ||rho-P_R rho P_R||_1 <= 2 sqrt(Tr((I-P_R)rho))
                          <= 2 sqrt(8delta|F|/R)

controls the off-diagonal coherences as well as the discarded mass. The finite-dimensional compressions form a compact bounded set, and their uniform trace-norm approximation proves trace-norm precompactness of the density matrices. Every subsequential trace-norm limit has the prescribed local weak-star expectations; uniqueness of the limiting state therefore identifies it and proves that the local restriction is normal. This works on every enlarged finite cell set, not just on a single cell.

The GNS restriction to each local B(H_F) is normal as well: matrix elements on the dense local-vector domain pi(A)Omega are expectations on a larger finite normal algebra; extend to arbitrary vectors by boundedness. A finite gauge assignment acts on a finite union of incident links by strongly continuous left/right regular translations. Gauge invariance of all finite ground states passes to omega. Thus U(g)pi(A)Omega=pi(alpha_g(A))Omega is an isometry and extends to a unitary. Its strong continuity follows from normality on an enlarged finite algebra and the strong continuity of the underlying link translations; then density gives it on all vectors. No norm continuity of alpha_g on all bounded local operators is asserted.

Finite Hamiltonians commute with these gauge transformations. Yarotsky Theorem3, applied to local matrix elements, transfers this commutation to the limiting resolvent. Thus H commutes with U(g), and the intersection of the combined fixed spaces reduces H tensor I_E.

## 2. Dense charged local vectors

Start with any finite sum zeta=sum_alpha pi(A_alpha)Omega tensor e_alpha. Its gauge orbit involves only vertices incident on the finite link support of the A_alpha and the two source vertices. Average over that finite product of SU(3)'s. The average is a vector sum of bounded local operators applied to Omega: the operator integrals exist ultraweakly in the finite local B(H_F), and their action on Omega agrees with the strong vector integral by local normality. It is invariant under all remaining vertices automatically, because their actions are trivial on the support and fix Omega. The resulting vector is therefore in C_xy.

For any xi in C_xy and local zeta approximating xi, that finite gauge average fixes xi and is a contraction. Its result remains within ||zeta-xi|| of xi. Consequently these bounded local covariant vector sums are dense in C_xy. This argument does not presume that an arbitrary local reduced state is supported on the zero-boundary-flux sector.

For each such averaged operator vector use precisely the same local operators and external basis in a sufficiently large finite volume, replacing Omega by Omega_Lambda. The finite ground is gauge invariant and all support vertices are present. This gives an exactly charged finite vector, not merely an approximately charged one. Its norm tends to the limiting norm by Theorem2.

## 3. Transfer of the sector exclusion

The precise imported statement is Yarotsky0411042 Theorem3, equation(6): local-vector matrix elements of (H_Lambda-E_Lambda-z)^(-1) converge for every nonreal z. Finite sums of external components preserve this statement by linearity. There is no appeal here to the paper's unlabelled spectral circles to infer a charged bound.

For a local charged vector let mu_Lambda be its finite positive spectral measure. The linked finite charged-sector estimate puts its support in [b,infinity), b=(4/a)(1-kappa)d. Resolvent convergence gives vague convergence of these measures to the spectral measure mu of the corresponding GNS vector: the resolvent functions generate C_0(R), or equivalently use their Poisson transforms. In particular every nonnegative compactly supported test function below b has zero limiting integral. Hence mu is supported in [b,infinity). Applying this to the dense charged local vectors proves that the spectral projection of H_xy on (-infinity,b) vanishes. Positivity and density are sufficient; no uniform norm bound on the finite dressed similarity is needed.

## 4. A normalized path vector and its limiting form energy

Choose one fixed shortest path gamma, with SU(3) transporter W_gamma. Use its nine matrix entries as multiplication operators and set Psi=(W_gamma/ sqrt(3))Omega in the normalized tensor-vector source convention of the linked finite charged-sector parent. Pointwise Tr W_gamma^*W_gamma/3=1, so ||Psi||=1 exactly, both finitely and in the limiting GNS representation. Its endpoint covariance places it in C_xy and proves this space nonzero.

For every sufficiently large finite volume the finite trial identity is exact:

 <Psi_Lambda,(H_Lambda-E_Lambda)Psi_Lambda>=4d/a.

The bounded potential is unchanged. On each path link the kinetic cross term vanishes by Tr(W^*D W)=0 for each traceless SU(3) generator, and the fundamental Casimir adds 4/a. The finite ground is in the kinetic form domain and smooth on the finite compact configuration space; the bounded smooth transporter preserves that domain. This is the same exact all-v finite trial identity, not an assertion about an infinite total energy expectation.

The positive spectral measures of these normalized vectors converge vaguely by Theorem3. Their limit is the spectral measure of Psi and has total mass one, because the pointwise transporter normalization passes exactly to the GNS state. Vague convergence of probability measures to a probability measure implies weak convergence. Alternatively, their common first-moment bound supplies tightness directly. For each R, integrate min(t,R) on the nonnegative spectrum and pass to the weak limit. Monotone convergence then yields

 integral t dmu_Psi(t) <= liminf integral t dmu_Lambda(t)=4d/a.

Therefore Psi belongs to the form domain of H and its form energy is at most4d/a. The variational principle yields the upper bound on inf Spec H_xy. Equality of the limiting first moment is not required and is not claimed; weak convergence can lose first moment at high energies.

## Scope and failed inferences excluded

The construction uses one fixed infinite interaction and its consistent finite restrictions. Toggling a near-source plaquette along the volume sequence is outside the limit theorem. The coupling window is existential and inherited; no numerical physical coupling is certified. The external color spaces and zero external Hamiltonian are supplied.

This result defines a selected charged GNS-sector energy bottom relative to the neutral GNS vacuum. It does not prove convergence of the finite charged ground energies: their minimizing vectors may escape every local-vector family. Nor does it prove existence of a charged bottom eigenvector, an infinite-volume potential defined by a temporal Wilson loop, a string tension limit as d tends to infinity, or a continuum/QCD claim. No conclusion is inferred from the spatial-area theorem. Local normality is used for gauge averages, not to impose false boundary singlet conditions.

Primary mathematical import: D.A. Yarotsky, https://arxiv.org/pdf/math-ph/0411042, Theorems2–3 and equation(6), read directly. The paper explicitly attributes these ground-state results to prior work; no novelty is claimed for generic GNS or spectral-measure limit principles.


## No-Go Discipline Gate

N1: this is a positive selected-representation energy-bound theorem. The finite spectral-measure, moving-eigenvector and combined-charge examples challenge particular limit inferences; they do not supply five exhaustive routes for a universal exclusion.

N2: no physical no-go wall is a premise. The sector spectral exclusion is the quantitative lower bound transferred from the linked finite-sector theorem under its explicit hypotheses.

N3: one fixed interaction, its consistent finite restrictions, sufficiently small coupling, full local bounded-operator algebra, exact boundary Gauss action and supplied endpoint spaces remain essential. An attained charged minimum and convergence of minimizing vectors are not assumed.

N4: the linked finite-sector parent supplies the actual uniform estimate and normalized path trial. Yarotsky Theorems2–3 and equation6 supply the neutral local state and local-vector resolvent limit, with cell gap1 and interaction norm3av/4. The general imported theorems are not proved by the finite runner.

N5: per_element covers three exact rational spectral-measure examples; per_site covers three finite Z3 charge labels, explicitly a toy; per_mode covers two fixed local resolvent modes; per_block covers three adverse-control families. Local normality, continuous SU3 averaging, spectral support transfer and the limiting form-domain bound are analytical, not executed infinite-volume simulations. The resource guard is separate from the fifteen scientific predicates.

N6: the conditional construction supplies no new axiom, primitive, physical quark dynamics or selected coupling.

N7: finite charged-minimum convergence, other boundary-selected representations, a bottom eigenvector, temporal Wilson potential, tension limit and continuum behavior remain open questions here, not disproved alternatives.

N8: the original two proofs and three reviews are historical corroboration. Present source confirmation and execution require their own identities; no broad negative certificate or audit verdict is asserted.

## Canonical execution evidence

The [canonical runner cache](../logs/runner-cache/gauge_wilson_selected_infinite_static_source_sector_2026_09_07.txt) must bind the current runner and its literal own-note and finite-sector-parent inputs. The expected scientific total is `TOTAL: PASS=15 FAIL=0`; the resource check remains separate. This expected output is not a claim of a new execution. Original failed attempts, proof variants, outputs and review records are preserved in the linked archive.
