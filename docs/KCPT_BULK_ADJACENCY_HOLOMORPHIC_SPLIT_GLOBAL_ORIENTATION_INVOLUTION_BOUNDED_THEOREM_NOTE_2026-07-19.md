# KCPT bulk-adjacency holomorphic split: the staggered `D2` complex spectrum and one global entrywise-conjugation pairing on the adjacency-native bulk

Date: 2026-07-19

**Type:** bounded_theorem

**Claim boundary:** This is a bounded theorem on one fixed finite surface — the `56`-dimensional bulk of the `4^3` staggered lattice `C^64`, the image on which the antisymmetric integer adjacency `D2` acts invertibly — established with exact integer, rational, and symbolic arithmetic only, with no floating point in any load-bearing gate. On that bulk `D2` assembles, stratum by stratum, into an adjacency-native complex structure with spectrum `±2 i sqrt(m)` for `m in {1, 2, 3}`, giving a `28 (+) ⊕ 28 (-) ⊕ 8` holomorphic / antiholomorphic / kernel split, and a single entrywise complex conjugation `K` exchanges the two `28`-dimensional halves of the constructed split on every stratum at once. On the kernel, `D2` and the spectral operator `A_0` vanish identically, so this specific `D2`-spectral construction supplies no kernel complex structure; the group-central `j` used there is supplied separately by the dressed group of the kernel note and is fixed by the same `K`. This does not exclude constructions that add structure beyond `D2`. The theorem fixes no free parameter, selects no orientation, weights no readout, and invokes no dynamics; it is `r`-neutral and orientation-neutral, and the paired runner recomputes every gated quantity from the construction rather than reading any value back.

**Conditions and import inventory:** The periodic `4^3` staggered graph, its phase convention, `D2`, and the kernel frame are bounded model conditions supplied by the linked delivery note, not consequences of the minimal axioms. The squared-adjacency strata and the cited kernel/group structure are likewise named bounded dependencies. The two-presentation `FLAG` name is contextual terminology and adds no theorem content here. No measured, fitted, literature, observational, readout-weight, externally supplied normalization, or dynamical value is used.

## Setting

The surface is the one built in [the delivery note](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md): the staggered `4^3` Dirac graph with phases `eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`, whose antisymmetric integer adjacency `D2` has entries in `{-1, 0, 1}` and an eight-dimensional kernel spanned by the corner waves `V8`. That note states of `D2` that "its exact rank is `56`", so the kernel dimension is eight and the complementary bulk — the image of `D2`, where it acts invertibly — is fifty-six dimensional. This unit works inside that bulk.

Squaring the adjacency gives the symmetric integer operator `M = D2 @ D2`, negative semidefinite because `D2` is real antisymmetric, with the four stratum eigenvalues `lam_m = -4 m` for `m in {0, 1, 2, 3}`. The drop-one Lagrange products `Q_m = prod_{m' != m} (M - lam_{m'} I)` and their scalar normalizers `N_m = prod_{m' != m} (lam_m - lam_{m'}) = [384, -128, 128, -384]` produce the exact rational idempotents `P_m = Q_m / N_m`, whose ranks are the stratum multiplicities `d_m = [8, 24, 24, 8]` summing to sixty-four. That squared-adjacency stratification is the landed content of [the bulk-block stratification note](KCPT_BULK_BLOCK_EIGENVALUE_STRATIFICATION_ADJACENCY_NATIVE_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md), which records that "The stratum dimensions are computed from `tr Q_m / N_m = (8, 24, 24, 8)`, not assumed"; this unit lifts those squared-adjacency shells from `M` to `D2` itself. The stratum adjacency operators are `A_m = D2 P_m`; the case `m = 0` is the kernel stratum and `m in {1, 2, 3}` are the three bulk shells. Every object below is rebuilt from these definitions in the paired runner, with the stratum eigenvalues serving only as the interpolation nodes of the drop-one construction, never as a target read back into a gate.

The complex structure lifted here has a kernel-level ancestor. [The kernel central-structure note](KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md) dresses the ambient lattice symmetries onto the corner-wave carrier and isolates a distinguished central complex structure `j`, recording that "entrywise complex conjugation fixes the entire real induced" group — the same entrywise involution that reappears at bulk scale as `K`. The motivating complement is the direct-parent result. [The ambient kernel-isolation note](KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md) observes that "the bulk operator `D2 @ D2.T` registers exactly zero on both `w0` and its conjugate though it is not the zero matrix, so bulk additions are invisible on the kernel doublet by kernel support, not by triviality." Bulk operators are invisible *on the kernel*; the next path that opens is to go *into* the bulk and read the adjacency-native structure that lives there. In the terminology of the context-only mechanism note `KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md`, this K-pairing is called a two-presentation `FLAG`. That name is contextual: the theorem content here is the explicit eigenspace construction and K exchange, not a new identification principle or a dependency on that mechanism note. The framework boundary is [the minimal-axioms note](MINIMAL_AXIOMS_2026-06-29.md) (registry id `minimal_axioms`); it does not supply the staggered carrier, `D2`, K/CPT structure, or the cited kernel/group construction.

Two neighbouring units are context here and carry no dependency edge: the antilinear K-real classification `KCPT_CORNER_CARRIER_ANTILINEAR_NONHERMITIAN_KREAL_READOUT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md` and the kernel K-real faces classification `KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md`. The bounded theorem has five parts.

## T1 — per-stratum adjacency complex structure

The projectors `P_m` are exact rational orthogonal idempotents: each satisfies `P_m^2 = P_m`, they sum to the identity, and each commutes with `D2`, so the stratification respects the adjacency. The stratum operators `A_m = D2 P_m` are then real antisymmetric, `A_m + A_m^T = 0`, and satisfy the defining square

`A_m @ A_m = -4 m P_m`   for `m in {0, 1, 2, 3}`,

recomputed exactly from the built matrices rather than assumed. The kernel stratum carries no adjacency operator at all, `A_0 = 0`: this `D2`-spectral adjacency-native complex structure exists only on the bulk. On the bulk the three stratum operators reassemble the full adjacency, `A_1 + A_2 + A_3 = D2`. Thus `J_m = A_m / (2 sqrt(m))` obeys `J_m^2 = -P_m` on each bulk shell, an adjacency-native complex structure stratum by stratum.

## T2 — the complex spectrum of `D2` is `±2 i sqrt(m)`

Because `M = D2 @ D2` acts as `-4 m` on stratum `m`, the adjacency `D2` itself has purely imaginary spectrum `±2 i sqrt(m)` on each bulk shell — the staggered dispersion of the graph. Each bulk stratum splits into equal conjugate halves, the per-shell `+i` multiplicities being `[d_1/2, d_2/2, d_3/2] = [12, 12, 4]`, which sum to the holomorphic bulk dimension `28`; the antiholomorphic half is equal by conjugation, and with the eight-dimensional kernel the bookkeeping totals `28 + 28 + 8 = 64`. This multiplicity count is confirmed by a second, independent construction: assigning each momentum `k in {0,1,2,3}^3` the weight `m(k) = (k_0 mod 2) + (k_1 mod 2) + (k_2 mod 2)` and counting momenta per weight reproduces `[8, 24, 24, 8]` exactly, matching the stratum dimensions `d_m` obtained from the projector traces. The two constructions — drop-one projector ranks and plane-wave weight counts — agree without either being fed the other.

## T3 — global-K holomorphic / antiholomorphic split (one K-paired presentation)

Each bulk stratum carries an explicit conjugate eigenpair. Taking a nonzero column `u` of `P_m` (so `P_m u = u`) and `A_m u`, the vectors

`v(+) = u - i A_m u / (2 sqrt(m))`,   `v(-) = u + i A_m u / (2 sqrt(m))`

satisfy `A_m v(+) = +2 i sqrt(m) v(+)` and `A_m v(-) = -2 i sqrt(m) v(-)` — verified over `Q(i)` for `m = 1` and with `sqrt(m)` kept symbolic for `m = 2, 3`. They are genuine, distinct, nonzero vectors, not a degenerate real ray. Entrywise complex conjugation sends one to the other, `conj(v(+)) = v(-)`: the single involution `K` exchanges the holomorphic and antiholomorphic eigenvectors on every bulk shell simultaneously. Algebraically, their signed imaginary components are `∓ A_m u / (2 sqrt(m))`, the two orientations of the same K-odd line. Calling this a `FLAG` instance uses the cited mechanism note's terminology only; it does not enlarge the eigenvector claim.

The same `K` has a global momentum realization as `k -> -k (mod 4)`. The fifty-six bulk momenta (those with weight `m(k) >= 1`) organize into exactly twenty-eight conjugate pairs, matching the `S^+`/`S^-` dimension, and the entrywise conjugate of every bulk plane wave is its momentum partner, `conj(psi_k) = psi_{-k}`. Thus one entrywise involution registers the global K-pairing of the constructed split across all three shells at once. This statement does not claim uniqueness among complex structures obtained by independently reversing the signs of shellwise `J_m`.

## T4 — the submitted `D2`-spectral construction vanishes on the kernel

The two kernel faces register exactly zero: `A_0 = 0` and `D2 V8 = 0`. The adjacency operator vanishes identically on the kernel, so the specific spectral formula used here, `A_m / (2 sqrt(m))`, supplies no kernel complex structure at `m = 0`. The kernel note instead supplies the group-central `j` from its dressed group `G`. The submitted constructions therefore have distinct inputs: the bulk structure is built from `D2`, while the cited kernel structure is built from the dressed symmetry group, and both are fixed by the **same** `K`. This note neither rules out every construction that combines `D2` with additional structure nor claims a single `J` spanning kernel and bulk — the shared object established across the two submitted blocks is the involution `K`, not one complex structure.

## T5 — boundary: single bulk `J`, `r`-neutral, orientation-neutral

Summing the shell structures gives one adjacency-native complex structure on the whole bulk,

`J_bulk = sum_{m in {1,2,3}} A_m / (2 sqrt(m))`,

which satisfies `J_bulk @ J_bulk = -P_bulk` on the fifty-six-dimensional image, with `P_bulk = P_1 + P_2 + P_3`, and is real, `J_bulk = conj(J_bulk)`. Being real, `J_bulk` commutes with the entrywise conjugation `K`, and `K` reverses the `±i` grading `J_bulk` induces. No `r` value is derived, assumed, or forced anywhere in this note; the statement is `r`-neutral. Neither the holomorphic half `S^+` nor the antiholomorphic half `S^-` is selected physically — they have equal dimension twenty-eight and `K` exchanges them — so the constructed split is orientation-neutral and no dynamics, weighting, or measurement is invoked. The theorem establishes this summed `J_bulk`; it does not assert uniqueness against independently signed shellwise complex structures. The next path this opens is to fix an orientation physically and to interrogate interacting extensions on the bulk, building on the single constructed `K`-fixed complex structure established here.

## Negative controls

The runner carries wrong-value rejectors that make each true identity discriminating rather than tautological.

- Mislabeling a bulk shell's eigenvalue fails: `A_1 @ A_1` is `-4 P_1`, not `-8 P_1`, and `A_2 @ A_2` is `-8 P_2`, not `-12 P_2`; the wrong-shell targets do not vanish.
- The stratum-one eigenvector is not a `+2 i sqrt(2)` eigenvector: applying the wrong-shell eigenvalue leaves a nonzero residual.
- Dropping any single stratum breaks the adjacency identity: `A_1 + A_2 - D2` is nonzero, so all three bulk strata are required to reassemble `D2`.
- A perturbed multiplicity vector `[8, 24, 24, 9]` is rejected against the recomputed `d_m = [8, 24, 24, 8]`.

## Gate map

| Gate tags | What it verifies |
|-----------|------------------|
| `a1`–`a5` | drop-one normalizers `N_m = [384, -128, 128, -384]`; stratum multiplicities `d_m = [8, 24, 24, 8]`; `D2` real antisymmetric; exact rank `56`; `D2 V8 = 0` (kernel frame) |
| `t1a`–`t1g` | `P_m` orthogonal idempotents completing to `I` and commuting with `D2`; `A_m` real antisymmetric; `A_m^2 = -4 m P_m`; `A_0 = 0`; `A_1 + A_2 + A_3 = D2` |
| `t2a`–`t2d` | per-shell `+i` multiplicities `[12, 12, 4]`; holomorphic dimension `28`; `28 + 28 + 8 = 64` bookkeeping; exact plane-wave stratum equation and independent momentum-weight count `[8, 24, 24, 8]` |
| `t3.1a`–`t3.3d` | per-stratum `±i` eigenvectors `v(±) = u ∓ i A_m u / (2 sqrt m)`; eigenvalues `±2 i sqrt(m)`; `conj(v(+)) = v(-)`; genuine distinct nonzero pair |
| `t3g1`–`t3g3` | `56` bulk momenta form `28` conjugate `K`-pairs; `conj(psi_k) = psi_{-k}` on every bulk momentum; each bulk plane wave has unit modulus at every site |
| `t4a`, `t4b` | `A_0 = 0` and `D2 V8 = 0`: the submitted `D2`-spectral formula supplies no kernel complex structure |
| `t5a`–`t5c` | `J_bulk^2 = -P_bulk`; `J_bulk` real and orthogonal on the bulk; twenty-eight holomorphic degrees of freedom |
| `w1`–`w5` | wrong-value rejectors: wrong-shell eigenvalues, wrong-shell eigenvector, dropped stratum, perturbed dim vector |
| `v1`–`v5` | verbatim source-quote greps in the delivery, kernel central-structure, ambient kernel-isolation, minimal-axioms, and bulk-block stratification notes |

## Runner and cache

The [paired runner](../scripts/kcpt_bulk_adjacency_holomorphic_split_2026_07_19.py) recomputes every gated quantity from the construction — the adjacency `D2`, the kernel frame `V8`, the squared operator `M`, the drop-one products `Q_m`, the normalizers `N_m`, the idempotents `P_m`, the stratum operators `A_m`, the explicit `±i` eigenvectors, the summed bulk complex structure `J_bulk`, and the independent momentum-weight count — and checks each identity with exact integer, rational, or symbolic arithmetic, with no floating point in any load-bearing gate. It prints `TOTAL: PASS=46 FAIL=0` and exits nonzero on any failure. Its cached output belongs at [logs/runner-cache/kcpt_bulk_adjacency_holomorphic_split_2026_07_19.txt](../logs/runner-cache/kcpt_bulk_adjacency_holomorphic_split_2026_07_19.txt).
