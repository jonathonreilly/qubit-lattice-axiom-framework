# KCPT bulk-block eigenvalue stratification: Hamming shells, the ker-pi carrier, and adjacency-native complex structures

Date: 2026-07-19

**Type:** bounded_theorem

**Claim boundary:** This is a bounded theorem on one fixed finite surface — the full `4^3` staggered lattice `C^64`, its bulk operator `M = D2 @ D2`, and the eigenvalue strata into which `M` resolves — established with exact integer and exact symbolic arithmetic only, with no floating point in any load-bearing gate. It stratifies the image block of [the ambient isolation note](KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md) into its Hamming shells, resolves each shell's ambient commutant by exact character sums, and exhibits the adjacency-native antisymmetric operators the shells carry. It fixes no free parameter, it selects no orientation, it chooses no dynamics, and it forces nothing pre-record; the paired runner recomputes every gated quantity from the construction rather than reading any value back.

## Setting

The surface is the one built in [the corner-carrier delivery note](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md): the staggered `4^3` Dirac graph with phases `eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`, whose antisymmetric integer adjacency `D2` carries an eight-dimensional kernel spanned by the corner waves `V8`. The delivery note records that this carrier is graded by Hamming weight as `1 + 3 + 3 + 1`, and states of `D2` that "its exact rank is `56`", so the kernel dimension is eight. The symmetry inputs are the lattice symmetries of [the minimal-axioms note](MINIMAL_AXIOMS_2026-06-29.md), the "standard translations, and proper cubic rotations", dressed by the staggered sign fields.

[The ambient isolation note](KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md) assembles those dressed symmetries into the ambient group `G_amb` of order `768` — the `D2`-commuting closure of three named base classes — and resolves the whole-lattice commutant as `dim_C End_{G_amb}(C^64) = 12`, splitting it by kernel and image blocks as "`12 = 2 + 2*0 + 10`: two dimensions on the kernel block ... ten on the image block; and each of the two kernel-image cross terms exactly zero", with the translation-only control `64 = 8 + 2*0 + 56`. The present note stratifies that image block. [The kernel note](KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md) and [the kernel K-real note](KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md) supply the kernel-block reading — the central complex structure `j` whose "exact commutant of `G` over the rationals is two-dimensional, `span{I, j}`", and the orientation-blind invariant Hermitian face — which reappears here as the `m = 0` shell.

The motivating question is what the ambient note's ten on the image block is made of. The bulk operator `M = D2 @ D2` is symmetric and commutes with every ambient member, so the ambient commutant on the image block distributes across the eigenvalue strata of `M`. Those strata turn out to be Hamming shells of a momentum label. This note resolves that distribution shell by shell and reads the antisymmetric content each shell carries. The bounded theorem has five parts.

## T1 — the ker-pi carrier and its eigenvalue stratification

The bulk operator is symmetric, `M = M^T`, because `D2` is antisymmetric. It is carried entirely by the even-translation subgroup: exactly `M = 2 (T_200 + T_020 + T_002) - 6 I`, where `T_2e` is the translation by two sites along axis `e`. So `M` lies in the group algebra of the elementary abelian `(Z/2)^3` of even translations and commutes with every one of its eight members — the `ker pi` carrier the ambient note names as the kernel of the compression onto `G`. Two rejectors pin the identity: the diagonal coefficient is `-6` and not `-5`, and the shifts are the even translations `T_200` and not the odd `T_100`.

The minimal polynomial factors exactly as `M (M + 4 I)(M + 8 I)(M + 12 I) = 0`, so `M` has four eigenvalue strata `lambda_m = -4 m` for `m = 0, 1, 2, 3`. The drop-one products `Q_m = prod_{m' != m}(M - lambda_{m'} I)` are the (unnormalized) stratum projectors, with integer normalizers `N_m = prod_{m' != m}(lambda_m - lambda_{m'}) = (384, -128, 128, -384)`. They satisfy `M Q_m = lambda_m Q_m`, the scaled idempotence `Q_m^2 = N_m Q_m`, mutual orthogonality `Q_m Q_{m'} = 0` for `m != m'`, and the pinned partition of unity `Q_0 - 3 Q_1 + 3 Q_2 - Q_3 = 384 I`. Each `Q_m` is real symmetric, and its entries are bounded integers, the stratum projector carried at exact integer scale.

The stratum dimensions are computed from `tr Q_m / N_m = (8, 24, 24, 8)`, not assumed. The kernel shell coincides with the corner frame, `Q_0 = 6 (V8 V8^T)`, recovering the eight-dimensional kernel of the Setting. The three bulk shells have exact ranks summing to `24 + 24 + 8 = 56`, the rank of `D2`, so the image block `56 = 24 + 24 + 8` is exactly the `m = 1, 2, 3` stratification and the kernel `8` is the `m = 0` shell.

## T2 — momentum diagonalization and the K-geometry

The strata are Hamming shells of a momentum label. For `k` in `(Z/4)^3` the wave `phi_k = i^{k . x}`, taken in split integer real and imaginary parts, is an `M`-eigenvector at `lambda = -4 m(k)`, where `m(k)` is the number of odd components of `k`. A wrong-eigenvalue rejector confirms `M phi_{(1,0,0)} = -4 phi_{(1,0,0)}`, neither zero nor `-8 phi`. The per-shell momentum counts are `(8, 24, 24, 8)`, matching the stratum dimensions exactly: the four Hamming weights of the momentum label enumerate the four eigenvalue strata.

The involution `K : k -> -k (mod 4)` preserves every shell, `m(-k) = m(k)`. It fixes exactly the eight kernel momenta — the components in `{0, 2}` that are their own negatives mod `4` — and every fixed momentum has `m = 0`. On the fifty-six bulk momenta `K` is fixed-point-free, partitioning them into twenty-eight conjugate pairs. So the kernel shell is the `K`-fixed locus and the bulk is `K`-paired, the momentum-side image of the same conjugation the kernel notes read entrywise.

## T3 — the ker-pi isotypic blocks and the ambient orbit structure

The even-translation carrier `(Z/2)^3` has eight characters `eps` in `{0, 1}^3`. Its isotypic idempotent pieces are the integer matrices `R8_eps = sum_{b in {0,1}^3} (-1)^{eps . b} T_{2b}`, one per character. Each eigenvalue stratum is the sum of the characters of its Hamming weight: exactly `8 Q_m = N_m sum_{wt(eps) = m} R8_eps` for every `m`. A wrong-weight rejector confirms the pairing is by weight — `8 Q_1` is not `N_1 sum_{wt(eps) = 2} R8_eps`. So the four strata are the four Hamming-weight isotypic sectors of the `ker pi` carrier, and the stratum dimensions `(8, 24, 24, 8)` are the binomial multiplicities `1, 3, 3, 1` each carried on an eight-dimensional character block.

Regenerating the ambient group `G_amb` independently — scanning the three dressed base classes over the sixty-four sign fields and sixty-four translations, keeping the `192` members that commute with `D2`, and closing to order `768` — every member commutes with `M` and hence with every `Q_m`, since each `Q_m` is a polynomial in `M`. Conjugation by `G_amb` permutes the eight `R8_eps` blocks by permuting the parity axes, and this permutation preserves Hamming weight, so the block orbits are exactly the weight classes, with sizes `1, 3, 3, 1`. The ambient group moves blocks only within a shell; it never mixes shells.

## T4 — the bulk commutant resolution and its Frobenius-Schur split

Exact character sums over the regenerated `768` members resolve each shell's ambient commutant. With `e_m = (1 / (768 N_m^2)) sum_{U in G_amb} tr(U Q_m)^2` computed as an exact rational and gated to be an integer, the per-shell commutant dimensions are `e_m = (2, 4, 4, 2)`, and every cross term `h_{m,m'} = (1 / (768 N_m N_{m'})) sum_U tr(U Q_m) tr(U Q_{m'})` vanishes, so the strata share no equivariant map. The ambient note's ten on the image block resolves across the three bulk shells as `10 = 4 + 4 + 2`, while the kernel shell keeps `e_0 = 2`, matching `span{I, j}`. The reconciliation `sum_m e_m + 2 sum_{m < m'} h_{m,m'} = 12` returns the ambient total. A group-is-load-bearing rejector confirms the resolution needs the full group: restricted to the eight `ker pi` translations alone the same sum gives `e_1 = 192`, not `4`.

The Frobenius-Schur indicators, `nu_m = (1 / (768 N_m)) sum_U tr(U^2 Q_m)` gated integer, are `nu_m = (0, 2, 0, 0)`. They split each commutant into its invariant antisymmetric and invariant symmetric parts, `a_m = (e_m - nu_m) / 2 = (1, 1, 2, 1)` and `s_m = (e_m + nu_m) / 2 = (1, 3, 2, 1)`, with `a_m + s_m = e_m` and `s_m - a_m = nu_m` on every shell. The combination `nu_m = s_m - a_m` records how each shell's invariant forms split: the kernel shell and shells `2`, `3` are balanced (`nu = 0`, equal symmetric and antisymmetric invariants), while shell `1` is symmetric-heavy (`nu_1 = 2`, three symmetric invariants to one antisymmetric). Every shell carries at least one invariant antisymmetric direction, and shell `2` carries two.

## T5 — adjacency-native complex structures and per-mode registration

Because `D2` is a polynomial-commuting square root of `M`, the products `D2 Q_m` are ambient-invariant and antisymmetric, and they square inside their shell: exactly `(D2 Q_m)^2 = -4 m N_m Q_m` for every `m`. On the kernel shell this vanishes, `D2 Q_0 = 0` — the adjacency has no action where it has no eigenvalue. Writing the shell idempotent as `P_m = Q_m / N_m`, the square is `(D2 Q_m)^2 = -4 m N_m^2 P_m` with `-4 m N_m^2 < 0` on every bulk shell, so `D2 Q_m` is a genuine adjacency-native complex structure: an antisymmetric ambient invariant whose square is a negative multiple of the shell idempotent, built from nearest-neighbor adjacency alone. (The raw coefficient against the unnormalized `Q_m` is `-4 m N_m = (0, 512, -1024, 4608)`, whose sign tracks `N_m`; the idempotent normalization is what carries the complex-structure sign.) Equivalently, on each bulk stratum `D2^2 = M = -4 m`, so `D2 / (2 sqrt(m))` squares to `-1`.

The invariant antisymmetric dimensions `a_m` say how rigidly the adjacency fixes that structure. Shells `1` and `3` are adjacency-pinned, `a_1 = a_3 = 1`: the invariant antisymmetric axis is exactly `span(D2 Q_m)`, and the discriminator shows it — a non-invariant antisymmetric perturbation fails membership in `span(D2 Q_1)`, yet its group average lands back on that single axis. Shell `2` is not adjacency-rigid, `a_2 = 2`: a structurally different rank-two adjacency seed, averaged over `G_amb` and compressed to the shell, produces a second invariant antisymmetric operator that is not proportional to `D2 Q_2`, exhibiting the extra axis the character count predicts.

The `m = 1` shell registers the pointer geometry the kernel notes carry, now on a bulk doublet. On the doublet `w` built from a stratum-`1` vector `v` by `J_1 = D2 / 2`, with `J_1 w = i w`, the norm is `|w|^2 = 8 |v|^2`. The K-odd separator `i (D2 Q_1)` registers opposite nonzero sesquilinear values on `w` and its conjugate; the raw projector pair `2 Q_1 -+ i (D2 Q_1)` is one-zero across the conjugate pair, the two rows exchanged by conjugation; and the K-real symmetric face `Q_1` registers the same value on `w` and its conjugate — blind to the doublet exactly as the invariant Hermitian norm form is blind on the kernel shell. The orientation binary `D2 Q_m -> -(D2 Q_m)` swaps the projector rows and flips the K-odd separator while fixing the symmetric face; the note does not choose the orientation.

## Negative controls

- Carrier-identity rejectors: the diagonal coefficient is pinned at `-6` (not `-5`), and the even shift `T_200` is pinned (not the odd `T_100`), so the `ker pi` carrier identity is exact and not approximate.
- Wrong-weight block rejector: `8 Q_1` is not `N_1 sum_{wt(eps) = 2} R8_eps`, so the Hamming-weight pairing of strata to characters is by weight, not free.
- Wrong-eigenvalue momentum rejector: `M phi_{(1,0,0)} = -4 phi`, neither `0` nor `-8 phi`, so the momentum label maps to the shell it should.
- Group-is-load-bearing rejector: restricting the character sum to the eight `ker pi` translations gives `e_1 = 192`, not `4` — the full `768`-member group does the work, not the carrier subgroup.
- Adjacency-axis discriminator: a non-invariant antisymmetric perturbation of `D2 Q_1` fails `span(D2 Q_1)`, while its group average returns to that axis; a single adjacency seed on shell `2` averages onto `span(D2 Q_2)` while a structurally different seed reaches the independent second axis, so `a_2 = 2` is exhibited and not asserted.

## Boundary

- It stratifies a commutant and reads antisymmetric content; it derives no `r` value and forces no weighting, normalization, or probability. The character sums and group averages are exact algebraic identities of the finite symmetry action — not a dynamical selection, not a measurement process, and not a probability-weight derivation.
- It does NOT select the orientation: `D2 Q_m` versus `-(D2 Q_m)` remains the two-presentation choice on every bulk shell; the note only classifies which faces register it, and it does not act on the upstream Qualification, which stays open.
- The ambient group is the `D2`-commuting dressed closure of the three named symmetry classes — a kinematic statement; no Hamiltonian, transfer operator, or admissibility dynamics is chosen.
- It is a finite fixed-surface statement (`L = 4` torus); no continuum or infinite-volume claim is made.
- It resolves the explicit named strata and their invariant faces only; the face list is deliberately non-complete, and genuinely antilinear functionals and interacting extensions are untested and outside the claim. It is NOT a universal-degeneracy or indistinguishability claim; no physical identification is made and nothing pre-record is forced.

## Gate map

| Block | What it checks | Gates |
|-------|----------------|-------|
| B1 | construction anchor: `D2` antisymmetry, exact rank `56`, `D2 @ V8 = 0`, `V8` orthogonality, Hamming grading `1 + 3 + 3 + 1` | 5 |
| B2 | `ker pi` carrier identity `M = 2 (T_200 + T_020 + T_002) - 6 I`, symmetry, even-translation commutation, diagonal/shift rejectors | 4 |
| B3 | minimal polynomial, four strata, projectors `Q_m`, normalizers `(384, -128, 128, -384)`, idempotence, orthogonality, dims `8, 24, 24, 8`, kernel = corner frame, bulk rank `56` | 11 |
| B4 | momentum diagonalization `phi_k`, per-stratum counts, wrong-eigenvalue rejector, `K : k -> -k` fixes the `8` kernel momenta, fixed-point-free on `56` bulk | 6 |
| B5 | `ker pi` isotypic blocks `8 Q_m = N_m sum_{wt(eps) = m} R8_eps`, wrong-weight rejector | 2 |
| B6 | regenerate `G_amb` at `768`, representation self-check, commutation with `M` and every `Q_m`, block permutation by axis, weight-class orbits `1, 3, 3, 1` | 8 |
| B7 | bulk commutant character sums `e_m = (2, 4, 4, 2)`, cross terms zero, `10 = 4 + 4 + 2`, reconciliation `12`, group-load-bearing rejector | 7 |
| B8 | Frobenius-Schur `nu_m = (0, 2, 0, 0)`, invariant antisymmetric `a_m = (1, 1, 2, 1)`, symmetric `s_m = (1, 3, 2, 1)`, consistency | 5 |
| B9 | adjacency-native complex structures `(D2 Q_m)^2 = -4 m N_m Q_m`, invariance, shell-1/3 pinned, shell-2 second axis, span discriminator, complex-structure sign | 11 |
| B10 | `m = 1` value tables: doublet norm, K-odd separator, projector pair one-zero with K swap, K-real symmetric face | 6 |
| B11 | note hygiene: links, required strings, pinned math, front matter | 4 |

## Runner and cache

The [paired runner](../scripts/kcpt_bulk_block_eigenvalue_stratification_2026_07_19.py) recomputes every gated quantity from the construction — the bulk operator and its `ker pi` carrier identity, the minimal polynomial and stratum projectors, the momentum diagonalization and `K`-geometry, the isotypic blocks, the regenerated `768`-member ambient group, the commutant and Frobenius-Schur character sums, the adjacency-native complex structures, and the value tables — and checks each identity with exact integer, exact `Fraction`, or exact `sympy` arithmetic, with no floating point in any load-bearing gate. Every commutant dimension is a character sum over the regenerated group, never a hardcoded target, and every completeness identity carries an explicit wrong-value rejector. It prints `TOTAL: PASS=N FAIL=0` and exits nonzero on any failure. Its cached output is stored at [logs/runner-cache/kcpt_bulk_block_eigenvalue_stratification_2026_07_19.txt](../logs/runner-cache/kcpt_bulk_block_eigenvalue_stratification_2026_07_19.txt).
