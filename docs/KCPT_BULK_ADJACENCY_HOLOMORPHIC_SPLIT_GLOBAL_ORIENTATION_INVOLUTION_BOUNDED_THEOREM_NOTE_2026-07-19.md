# KCPT bulk-adjacency holomorphic split: the staggered `D2` complex spectrum and one global entrywise-conjugation FLAG on the adjacency-native bulk

Date: 2026-07-19

**Type:** bounded_theorem

**Claim boundary:** This is a bounded theorem on one fixed finite surface — the `56`-dimensional bulk of the `4^3` staggered lattice `C^64`, the image on which the antisymmetric integer adjacency `D2` acts invertibly — established with exact integer, rational, and symbolic arithmetic only, with no floating point in any load-bearing gate. On that bulk `D2` assembles, stratum by stratum, into an adjacency-native complex structure with spectrum `±2 i sqrt(m)` for `m in {1, 2, 3}`, giving a `28 (+) ⊕ 28 (-) ⊕ 8` holomorphic / antiholomorphic / kernel split, and a single entrywise complex conjugation `K` exchanges the two `28`-dimensional halves on every stratum at once — one binary FLAG orientation for the whole adjacency-native bulk. The kernel complex structure is not adjacency-native: `D2` vanishes identically on the kernel, so that structure is the group-central `j` supplied by the dressed group of the kernel note, distinct in origin yet fixed by the same `K`. The theorem fixes no free parameter, selects no orientation, weights no readout, and invokes no dynamics; it is `r`-neutral and orientation-neutral, and the paired runner recomputes every gated quantity from the construction rather than reading any value back.

## Setting

The surface is the one built in [the delivery note](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md): the staggered `4^3` Dirac graph with phases `eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`, whose antisymmetric integer adjacency `D2` has entries in `{-1, 0, 1}` and an eight-dimensional kernel spanned by the corner waves `V8`. That note states of `D2` that "its exact rank is `56`", so the kernel dimension is eight and the complementary bulk — the image of `D2`, where it acts invertibly — is fifty-six dimensional. This unit works inside that bulk.

Squaring the adjacency gives the symmetric integer operator `M = D2 @ D2`, negative semidefinite because `D2` is real antisymmetric, with the four stratum eigenvalues `lam_m = -4 m` for `m in {0, 1, 2, 3}`. The drop-one Lagrange products `Q_m = prod_{m' != m} (M - lam_{m'} I)` and their scalar normalizers `N_m = prod_{m' != m} (lam_m - lam_{m'}) = [384, -128, 128, -384]` produce the exact rational idempotents `P_m = Q_m / N_m`, whose ranks are the stratum multiplicities `d_m = [8, 24, 24, 8]` summing to sixty-four. That squared-adjacency stratification is the landed content of [the bulk-block stratification note](KCPT_BULK_BLOCK_EIGENVALUE_STRATIFICATION_ADJACENCY_NATIVE_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md), which records that "The stratum dimensions are computed from `tr Q_m / N_m = (8, 24, 24, 8)`, not assumed"; this unit lifts those squared-adjacency shells from `M` to `D2` itself. The stratum adjacency operators are `A_m = D2 P_m`; the case `m = 0` is the kernel stratum and `m in {1, 2, 3}` are the three bulk shells. Every object below is rebuilt from these definitions in the paired runner, with the stratum eigenvalues serving only as the interpolation nodes of the drop-one construction, never as a target read back into a gate.

The complex structure lifted here has a kernel-level ancestor. [The kernel central-structure note](KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md) dresses the ambient lattice symmetries onto the corner-wave carrier and isolates a distinguished central complex structure `j`, recording that "entrywise complex conjugation fixes the entire real induced" group — the same entrywise involution that reappears at bulk scale as `K`. The motivating complement is the direct-parent result. [The ambient kernel-isolation note](KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md) observes that "the bulk operator `D2 @ D2.T` registers exactly zero on both `w0` and its conjugate though it is not the zero matrix, so bulk additions are invisible on the kernel doublet by kernel support, not by triviality." Bulk operators are invisible *on the kernel*; the next path that opens is to go *into* the bulk and read the adjacency-native structure that lives there. The pattern that structure realizes is the standing two-presentation FLAG carried by [the two-presentation mechanism note](KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md), whose entrywise-conjugate presentations "satisfy the same named clauses and exchange every K-odd seed" — here the two presentations are the holomorphic and antiholomorphic halves, `K` exchanges them, and the K-odd seed is the imaginary part of each `±i` eigenvector. The symmetry inputs, the register-not-read discipline, and the no-import framework are those of [the minimal-axioms note](MINIMAL_AXIOMS_2026-06-29.md) (registry id `minimal_axioms`).

Two neighbouring units are context here and carry no dependency edge: the antilinear K-real classification `KCPT_CORNER_CARRIER_ANTILINEAR_NONHERMITIAN_KREAL_READOUT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md` and the kernel K-real faces classification `KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md`. The bounded theorem has five parts.

## T1 — per-stratum adjacency complex structure

The projectors `P_m` are exact rational orthogonal idempotents: each satisfies `P_m^2 = P_m`, they sum to the identity, and each commutes with `D2`, so the stratification respects the adjacency. The stratum operators `A_m = D2 P_m` are then real antisymmetric, `A_m + A_m^T = 0`, and satisfy the defining square

`A_m @ A_m = -4 m P_m`   for `m in {0, 1, 2, 3}`,

recomputed exactly from the built matrices rather than assumed. The kernel stratum carries no adjacency operator at all, `A_0 = 0`: the adjacency-native complex structure exists only on the bulk. On the bulk the three stratum operators reassemble the full adjacency, `A_1 + A_2 + A_3 = D2`. Thus `J_m = A_m / (2 sqrt(m))` obeys `J_m^2 = -P_m` on each bulk shell, an adjacency-native complex structure stratum by stratum.

## T2 — the complex spectrum of `D2` is `±2 i sqrt(m)`

Because `M = D2 @ D2` acts as `-4 m` on stratum `m`, the adjacency `D2` itself has purely imaginary spectrum `±2 i sqrt(m)` on each bulk shell — the staggered dispersion of the graph. Each bulk stratum splits into equal conjugate halves, the per-shell `+i` multiplicities being `[d_1/2, d_2/2, d_3/2] = [12, 12, 4]`, which sum to the holomorphic bulk dimension `28`; the antiholomorphic half is equal by conjugation, and with the eight-dimensional kernel the bookkeeping totals `28 + 28 + 8 = 64`. This multiplicity count is confirmed by a second, independent construction: assigning each momentum `k in {0,1,2,3}^3` the weight `m(k) = (k_0 mod 2) + (k_1 mod 2) + (k_2 mod 2)` and counting momenta per weight reproduces `[8, 24, 24, 8]` exactly, matching the stratum dimensions `d_m` obtained from the projector traces. The two constructions — drop-one projector ranks and plane-wave weight counts — agree without either being fed the other.

## T3 — global-K holomorphic / antiholomorphic split (one FLAG orientation)

Each bulk stratum carries an explicit conjugate eigenpair. Taking a nonzero column `u` of `P_m` (so `P_m u = u`) and `A_m u`, the vectors

`v(+) = u - i A_m u / (2 sqrt(m))`,   `v(-) = u + i A_m u / (2 sqrt(m))`

satisfy `A_m v(+) = +2 i sqrt(m) v(+)` and `A_m v(-) = -2 i sqrt(m) v(-)` — verified over `Q(i)` for `m = 1` and with `sqrt(m)` kept symbolic for `m = 2, 3`. They are genuine, distinct, nonzero vectors, not a degenerate real ray. Entrywise complex conjugation sends one to the other, `conj(v(+)) = v(-)`: the single involution `K` exchanges the holomorphic and antiholomorphic eigenvectors on every bulk shell simultaneously. This is exactly the mechanism note's clause realized at bulk-adjacency level — the two entrywise-conjugate presentations `v(±)` satisfy the same eigenvalue clause (up to the sign of the imaginary eigenvalue) and exchange the K-odd seed, which is precisely the imaginary part `A_m u / (2 sqrt(m))` of each eigenvector.

The same `K` has a global momentum realization as `k -> -k (mod 4)`. The fifty-six bulk momenta (those with weight `m(k) >= 1`) organize into exactly twenty-eight conjugate pairs, matching the `S^+`/`S^-` dimension, and the entrywise conjugate of every bulk plane wave is its momentum partner, `conj(psi_k) = psi_{-k}`. So the adjacency-native bulk carries exactly one binary FLAG orientation, registered by this single entrywise conjugation across all three shells at once.

## T4 — the kernel complex structure is group-derived, not adjacency-native

The two kernel faces register exactly zero: `A_0 = 0` and `D2 V8 = 0`. The adjacency operator vanishes identically on the kernel, so the kernel's complex structure cannot be adjacency-native — there is no `D2`-built operator to carry it. That structure is instead the group-central `j` supplied by the dressed group `G` of the kernel central-structure note. The origins are distinct: the bulk structure is adjacency-native (built from `D2`), the kernel structure is group-central (built from the dressed symmetry group), yet both are fixed by the **same** `K`. This note therefore does not claim a single `J` spanning kernel and bulk — the unifying object across the two blocks is the involution `K`, not one complex structure.

## T5 — boundary: single bulk `J`, `r`-neutral, orientation-neutral

Summing the shell structures gives one adjacency-native complex structure on the whole bulk,

`J_bulk = sum_{m in {1,2,3}} A_m / (2 sqrt(m))`,

which satisfies `J_bulk @ J_bulk = -P_bulk` on the fifty-six-dimensional image, with `P_bulk = P_1 + P_2 + P_3`, and is real, `J_bulk = conj(J_bulk)`. Being real, `J_bulk` commutes with the entrywise conjugation `K`, and `K` reverses the `±i` grading `J_bulk` induces. No `r` value is derived, assumed, or forced anywhere in this note; the statement is `r`-neutral. Neither the holomorphic half `S^+` nor the antiholomorphic half `S^-` is canonical — they have equal dimension twenty-eight and `K` exchanges them — so the split is orientation-neutral and no dynamics, weighting, or measurement is invoked. The next path this opens is to fix the orientation physically and to interrogate interacting extensions on the bulk, building on the single `K`-fixed complex structure established here.

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
| `t2a`–`t2d` | per-shell `+i` multiplicities `[12, 12, 4]`; holomorphic dimension `28`; `28 + 28 + 8 = 64` bookkeeping; independent momentum-weight count `[8, 24, 24, 8]` |
| `t3.1a`–`t3.3d` | per-stratum `±i` eigenvectors `v(±) = u ∓ i A_m u / (2 sqrt m)`; eigenvalues `±2 i sqrt(m)`; `conj(v(+)) = v(-)`; genuine distinct nonzero pair |
| `t3g1`–`t3g3` | `56` bulk momenta form `28` conjugate `K`-pairs; `conj(psi_k) = psi_{-k}` on every bulk momentum; each bulk plane wave has unit modulus at every site |
| `t4a`, `t4b` | `A_0 = 0` and `D2 V8 = 0`: `D2` vanishes on the kernel, so kernel structure is not adjacency-native |
| `t5a`–`t5c` | `J_bulk^2 = -P_bulk`; `J_bulk` real; twenty-eight holomorphic degrees of freedom |
| `w1`–`w5` | wrong-value rejectors: wrong-shell eigenvalues, wrong-shell eigenvector, dropped stratum, perturbed dim vector |
| `v1`–`v5` | verbatim source-quote greps in the delivery, kernel central-structure, ambient kernel-isolation, two-presentation, and bulk-block stratification notes |

## Runner and cache

The [paired runner](../scripts/kcpt_bulk_adjacency_holomorphic_split_2026_07_19.py) recomputes every gated quantity from the construction — the adjacency `D2`, the kernel frame `V8`, the squared operator `M`, the drop-one products `Q_m`, the normalizers `N_m`, the idempotents `P_m`, the stratum operators `A_m`, the explicit `±i` eigenvectors, the summed bulk complex structure `J_bulk`, and the independent momentum-weight count — and checks each identity with exact integer, rational, or symbolic arithmetic, with no floating point in any load-bearing gate. It prints `TOTAL: PASS=46 FAIL=0` and exits nonzero on any failure. Its cached output belongs at [logs/runner-cache/kcpt_bulk_adjacency_holomorphic_split_2026_07_19.txt](../logs/runner-cache/kcpt_bulk_adjacency_holomorphic_split_2026_07_19.txt).
