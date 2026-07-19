# KCPT ambient lattice symmetry: kernel-block isolation, the averaged complex structure, and lattice-wide K-real registration

Date: 2026-07-19

**Type:** bounded_theorem

**Claim boundary:** This is a bounded theorem on one fixed finite surface — the full `4^3` staggered lattice `C^64` read over its corner-wave kernel — established with exact integer and exact symbolic arithmetic only, with no floating point in any load-bearing gate. It is a statement about the ambient lattice symmetry group, the action that group induces on the kernel, and the explicit named lattice-wide readout faces. It fixes no free parameter, it selects no orientation, it chooses no dynamics, and it forces nothing pre-record; the paired runner recomputes every gated quantity from the construction rather than reading any value back.

## Setting

The surface is the one built in [the delivery note](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md): the staggered `4^3` Dirac graph with phases `eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`, whose antisymmetric integer adjacency `D2` carries an eight-dimensional kernel spanned by the corner waves `V8`. The delivery note records that this carrier is graded by Hamming weight as `1 + 3 + 3 + 1`, and states of `D2` that "its exact rank is `56`", so the kernel dimension is eight.

[The kernel note](KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md) induces those lattice symmetries onto the corner-wave carrier, producing the real integer group `G` of order `96`, and isolates the distinguished central complex structure `j`. Two of its facts frame the present lift: "The exact commutant of `G` over the rationals is two-dimensional, `span{I, j}`", and "entrywise complex conjugation fixes the entire real induced group `G`". [The kernel K-real note](KCPT_KERNEL_KREAL_READOUT_FACE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md) classifies the named readout faces on the kernel carrier `C^8` under that entrywise conjugation, fixing the invariant Hermitian face and forcing a norm form when K-reality is imposed.

Because `V8` is a real matrix, entrywise conjugation on the carrier commutes with the embedding: `conj(V8 c) = V8 conj(c)`. Kernel-level conjugation is therefore exactly the restriction of ambient conjugation, and the faces registered below are the lattice-wide reading of that same involution in corner-wave coordinates.

The motivating question is the delivery note's own untested row. That note states plainly: "Antilinear and non-Hermitian functionals, interacting extensions, and lattice-wide readouts are untested and outside the claim." The K-real classification leaves the same clause open: "Genuinely antilinear readout functionals remain untested, as do interacting and lattice-wide readouts." The present note addresses the "lattice-wide readouts" part of that clause at the ambient level `C^64` — which lattice symmetries survive dressing, what they induce on the kernel, and how lattice-wide invariant readouts register. The bounded theorem has five parts.

## T1 — the ambient symmetry group

The symmetry inputs are the lattice symmetries of [the minimal-axioms note](MINIMAL_AXIOMS_2026-06-29.md), the "standard translations, and proper cubic rotations", dressed by the staggered sign fields. Taking the three named base classes — the identity base, one order-two proper rotation whose kernel action swaps the first two parity axes, and one order-three proper rotation — each dressed by one of the sixty-four sign fields and composed with one of the sixty-four translations, the members that commute exactly with `D2` number exactly `192`, sixty-four per class. Their closure under composition is the ambient group `G_amb` of order `768`.

Every member of `G_amb` commutes with `D2` and preserves its kernel, so compression by the corner-wave frame `V8` induces a homomorphism onto exactly the landed `96`-element group `G`; the runner checks this by regenerating `G` independently from the compressed generators and gating set equality. The kernel of the homomorphism consists of exactly the eight pure even translations indexed by `{0, 2}^3` — an elementary abelian `(Z/2)^3` with every member squaring to the identity — and it is normal in `G_amb` under full conjugation. Each ambient member is a signed permutation, orthogonal at unit scale. The count identity `768 = 8 * 96` ties the three counts together; the next path this opens is the ambient lift of the kernel's complex structure.

## T2 — the ambient lift of the complex structure

With the raw integer objects `Jr = V8 @ J64 @ V8.T` and `Pr = V8 @ V8.T`, the lift of the central structure `J64` satisfies exactly: `Jr` is an antisymmetric integer matrix with `Jr @ Jr = -(64^3) * Pr`; it annihilates the image block on both sides, `Jr @ D2 = 0 = D2 @ Jr`; it commutes with all `768` ambient members; it is kernel-supported, `Pr @ Jr = 64 * Jr = Jr @ Pr`; and it compresses back to the found structure, `V8.T @ Jr @ V8 = (64^2) * J64`. A generic integer test operator confirms the lift is a bijection between kernel-supported operators and their compressions.

In normalized language, `J = V8 j V8^T / 64` satisfies `J^2 = -P_ker` with `P_ker = V8 V8^T / 64`. The two ambient lifts `+J` and `-J` are the lattice-level images of "the two normalized central complex structures `+j` and `-j`" the kernel note carries; the present note does not choose between them.

## T3 — kernel-block isolation and the averaged complex structure

Exact character sums over all `768` members give the total commutant dimension `dim_C End_{G_amb}(C^64) = 12`, which splits by kernel and image blocks as `12 = 2 + 2*0 + 10`: two dimensions on the kernel block, matching the rational commutant `span{I, j}`; ten on the image block; and each of the two kernel-image cross terms exactly zero. The vanishing of the cross terms is representation-theoretic — on this finite surface the kernel block admits no nonzero equivariant map to the image block. The translation-only control has the exact split `64 = 8 + 2*0 + 56`: translations already isolate the kernel and image blocks, while the full dressed group sharpens their internal commutants from eight and fifty-six dimensions to two and ten. The two proper-rotation classes are load-bearing for that internal rigidity, not for cross-block isolation.

The isolation has an explicit averaging discriminator, a pair of group sums computed by the same code. The sum of the kernel-to-image transition `E_cross = outer(V8[:, 0], D2[:, 0])` — a nonzero integer matrix — over the whole group vanishes identically. The sum of the kernel-internal corner transition `E = outer(V8[:, 0], V8[:, 2])` does not vanish: it lands exactly on the lifted complex structure, `sum_{U in G_amb} U E U^T = 96 * (V8 @ j @ V8.T)`, equivalently `2 * sum = 3 * Jr`. The group average is therefore `Phi(E) = 8 J`. This identity is a group-average computation stated register-not-read: because `E` is traceless the identity coefficient `alpha = 0` is forced, so the average registers no identity component and its entire surviving content is the central complex structure. The pairing of the two sums shows the cross vanishing is a fact of the group action, not a code artifact.

## T4 — lattice-wide K-real registration

Take the deterministic Hermitian ambient readout carried by the integer pair `F_re = outer(V8[:, 0], V8[:, 0])` (symmetric) and `F_im = E - E.T` (antisymmetric), encoding `F0 = F_re + i F_im` with no floating point. The group sum, compressed by `V8`, lands exactly in the invariant Hermitian face: `V8.T @ (sum_U U F_re U^T) @ V8 = a_c * I8` and `V8.T @ (sum_U U F_im U^T) @ V8 = c_c * J64` with exact rational `a_c` and `c_c` both nonzero, so both axes are live. This is the lattice-side realization of the kernel classification: "The `G`-invariant Hermitian face is exactly `{a I + c (i j)}` with `a, c` real, a two-dimensional real space."

Restricting to the explicit K-real member — the entrywise-real readout `F_re`, whose imaginary part is zero — the averaged compression is `a_c * I8` with the `(i j)`-coefficient exactly zero. Ambient invariance together with K-reality forces the norm form, reproducing from the lattice side the kernel-level forcing: "K-reality of `a I + c (i j)` forces `c = 0`, since `conj(F) - F = -2 c (i j)` is nonzero whenever `c` is." The same forcing is re-derived locally in the runner by exact symbolic conjugation. A rejector confirms invariance is load-bearing: the unaveraged compression `V8.T @ F_re @ V8` is not a multiple of `I8` (its diagonal entries differ), so K-reality alone does not produce the norm form — the averaging is doing the work.

## T5 — value tables, flag registration, and bulk-blindness

On the ambient doublet member `w0 = 64 * V8[:, 0] - i * (V8 @ J64)[:, 0]` and its entrywise conjugate, the sesquilinear value tables are computed exactly on the split integer parts. The pair shares a norm, `|w0|^2 = 2 * 64^3`. The K-odd separator registers conjugate values, `E_{i Jr}(w0) = -2 * 64^5` and `E_{i Jr}(conj w0) = +2 * 64^5`. The raw ambient `W`-projector `PW_raw = 64 * Pr - i * Jr` registers `E_{PW_raw}(w0) = 4 * 64^5` and `E_{PW_raw}(conj w0) = 0`, and the conjugate projector `PWbar_raw = 64 * Pr + i * Jr` swaps the two values.

Sending `Jr -> -Jr` swaps the two projector rows and flips the sign of the K-odd separator value, while the averaged K-real readout value is unchanged. So the orientation binary registers on the K-odd separator and the projector pair at ambient scale exactly as at kernel scale, and it cannot be carried by the K-real invariant face. This is the same two-presentation freedom the upstream notes hold open; the kernel note's Boundary records it — "It does NOT select the orientation: `+j` versus `-j` remains the two-presentation choice" — and [the mechanism note](KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md) carries it as its standing FLAG and Qualification:

> **FLAG — two-model mechanism:** the entrywise-conjugate presentations in L-K2 satisfy the same named clauses and exchange every K-odd seed.

> The memo's live Qualification leaves the unfixed choice conditional/open.

The averaged K-real readout registers identical values on the conjugate pair, `E_{S_re}(w0) = E_{S_re}(conj w0) = a_c * 2 * 64^2`, its own computed coefficient linking the sesquilinear value, the compressed coefficient, and the compressed doublet norm — norm-form blindness that names its mode: the K-real invariant Hermitian face takes the same value under either orientation, while the sharp separators are K-odd or non-K-real. Finally, the bulk operator `D2 @ D2.T` registers exactly zero on both `w0` and its conjugate though it is not the zero matrix, so bulk additions are invisible on the kernel doublet by kernel support, not by triviality. The next named faces to interrogate, once an orientation is physically fixed, are the interacting extensions the untested clause still holds open.

## Negative controls

- Translation-only commutant split is `64 = 8 + 2*0 + 56`: the pure translations already isolate the kernel and image blocks, while the full dressed group sharpens the two internal commutants to dimensions two and ten.
- The unaveraged K-real compression `V8.T @ F_re @ V8` is not a multiple of `I8` (two unequal diagonal entries): invariance, not K-reality alone, produces the norm form.
- The cross transition sum vanishes while the corner transition sum does not, computed by the same summation code: the pair discriminates, so the cross vanishing is representation-theoretic and not a code artifact.
- The identity coefficient `alpha = 0` is forced in the corner average because `E` is traceless: there is no identity admixture in `Phi(E) = 8 J`.
- The bulk operator `D2 @ D2.T` registers zero on the doublet while being a nonzero matrix: the blindness is kernel support, not triviality.

## Boundary

- It does NOT select the orientation: `+j` versus `-j` — equivalently `+J` versus `-J` — remains the two-presentation choice; the ambient average produces the structure only up to this named binary, and the note only classifies which faces register it.
- It does not act on the mechanism note's live Qualification, which stays conditional/open.
- It derives no `r` value and forces no weighting, normalization, or probability. The group average is an exact algebraic identity of the finite symmetry action — not a dynamical selection, not a measurement process, and not a probability-weight derivation; no update law and no time evolution is invoked. The average forces the coefficients `alpha = 0` and `c = 0` in the named algebraic identities, nothing about a physical outcome.
- The ambient group is the `D2`-commuting dressed closure of the three named symmetry classes — a kinematic statement; no Hamiltonian, transfer operator, or admissibility dynamics is chosen.
- It is a finite fixed-surface statement (`L = 4` torus); no continuum or infinite-volume claim is made.
- It classifies the explicit named lattice-wide faces only; the face list is deliberately non-complete; genuinely antilinear functionals and interacting extensions are untested and outside the claim. It is NOT a universal-degeneracy or indistinguishability claim; no physical identification is made and nothing pre-record is forced.

## Gate map

| Block | What it checks | Gates |
|-------|----------------|-------|
| B1 | construction re-gated: `D2` antisymmetry, exact rank, kernel frame, Hamming grading, ambient-restriction identity | 6 |
| B2 | ambient group: scan of `192`, representation self-check, closure to `768`, kernel preservation, `ker pi` = `(Z/2)^3`, normality, orthogonality, count identity | 11 |
| B3 | induced image equals `G` at `96` by independent regeneration, central roots, `J64` selection and closed form | 9 |
| B4 | ambient lift `Jr`, `Pr`: square, annihilation, centrality, kernel support, compression, lift bijection | 6 |
| B5 | character sums `12 = 2 + 2*0 + 10`, translation split `64 = 8 + 2*0 + 56`, cross vanishing, corner average `Phi(E) = 8 J`, forced `alpha` | 12 |
| B6 | lattice-wide K-real face, both axes live, forced `c = 0`, value tables, flag registration, bulk-blindness | 13 |
| B7 | verbatim source quotes present in both source and note | 14 |
| B8 | dependency ledger shard existence | 3 |
| B9 | note hygiene: links, required strings, pinned math | 5 |

## Runner and cache

The [paired runner](../scripts/kcpt_ambient_lattice_symmetry_kernel_isolation_2026_07_19.py) recomputes every gated quantity from the construction — the ambient group by scan and closure, the induced homomorphism against an independent regeneration, the central `J64` by selection, the lift `Jr`, the character sums, the group averages, and the value tables — and checks each identity with exact integer or exact symbolic arithmetic, with no floating point in any load-bearing gate. It prints `TOTAL: PASS=N FAIL=0` and exits nonzero on any failure. Its cached output is stored at [logs/runner-cache/kcpt_ambient_lattice_symmetry_kernel_isolation_2026_07_19.txt](../logs/runner-cache/kcpt_ambient_lattice_symmetry_kernel_isolation_2026_07_19.txt).
