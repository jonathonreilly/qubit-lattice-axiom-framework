# KCPT kernel K-real readout faces: the invariant Hermitian face is orientation-blind

Date: 2026-07-18

**Type:** bounded_theorem

**Claim boundary:** This is a bounded theorem on one fixed finite surface — the `4^3` staggered kernel carrier of the delivery note — established with exact integer and exact symbolic arithmetic only, with no floating point in any load-bearing gate. It classifies the explicit named readout faces on the kernel carrier `C^8` under entrywise complex conjugation `K`. It fixes no free parameter, it does NOT select an orientation, and it forces nothing pre-record; the paired runner recomputes every gated quantity from the construction rather than reading any value back.

## Setting

The surface is the one built in [the delivery note](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md): the staggered `4^3` Dirac graph with phases `eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`, whose antisymmetric adjacency `D2` carries an eight-dimensional kernel spanned by the corner waves `V8`. The delivery note records that this carrier is graded by Hamming weight as `1 + 3 + 3 + 1`, and of `D2` that "its exact rank is `56`", so the kernel dimension is eight. The symmetry inputs are the lattice symmetries of [the minimal-axioms note](MINIMAL_AXIOMS_2026-06-29.md) — "standard translations, and proper cubic rotations" — dressed by the staggered sign fields.

[The kernel note](KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md) induces those symmetries onto the corner-wave carrier, producing the real integer group `G` of order `96`, and isolates the distinguished central complex structure `j` with Pauli word `Z (x) iY (x) Z`. Two facts from that note frame the present classification: "The exact commutant of `G` over the rationals is two-dimensional, `span{I, j}`", and "entrywise complex conjugation fixes the entire real induced group `G`". The kernel note also leaves a two-presentation freedom open — "the two normalized central complex structures `+j` and `-j`" — the same freedom [the mechanism note](KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md) carries as its live FLAG.

Because `V8` is a real matrix, entrywise conjugation on the carrier commutes with the embedding: `conj(V8 c) = V8 conj(c)`. So kernel-level `K` is exactly the restriction of ambient complex conjugation, and the classification below is a statement about that ambient involution read in corner-wave coordinates.

The motivating question is the delivery note's own untested row. That note states plainly: "Antilinear and non-Hermitian functionals, interacting extensions, and lattice-wide readouts are untested and outside the claim." The present note addresses one part of that first clause at the induced-kernel level: it classifies the named linear matrix faces by K-reality and includes the non-Hermitian witness `j`. Genuinely antilinear readout functionals remain untested, as do interacting and lattice-wide readouts. The bounded theorem has five parts.

## T1 — Hermitian bridge

A complex matrix `A` on `C^8` is entrywise real iff it splits rigidly as `A = H1 + i H2` with `H1 = (A + A^T)/2` Hermitian and K-even and `H2 = -i (A - A^T)/2` Hermitian and K-odd. The split is a parameter count: `36` symmetric plus `28` antisymmetric entries give `36 + 28 = 64`. On any vector the sesquilinear value decomposes as `Re E_A = E_{H1}` and `Im E_A = E_{H2}`, and for real `A` the conjugate-values lemma holds — the value on the conjugate vector is the conjugate value. Block B3 gates each clause symbolically over the `64` free real entries.

## T2 — the invariant Hermitian face

The `G`-invariant Hermitian face is exactly `{a I + c (i j)}` with `a, c` real, a two-dimensional real space. Its K-real part is the real line `R I` alone: K-reality of `a I + c (i j)` forces `c = 0`, since `conj(F) - F = -2 c (i j)` is nonzero whenever `c` is. So every `G`-invariant Hermitian readout that is explicitly K-real is a norm form — orientation-blind, fixed pointwise under the orientation swap. Block B4 gates the face, the forced `c = 0`, and the Hermitian rejectors.

## T3 — spectral polarization and per-mode registration

The K-odd generator polarizes the carrier: `i j = P_Wbar - P_W` with `P_W = (I - i j)/2` and `P_Wbar = (I + i j)/2` orthogonal idempotents of rank `4`, on which `j` acts as `+i` and `-i` respectively; the projectors are non-K-real, `conj(P_W) = P_Wbar`. On the doublet pair `(w, conj w)` with `w = u - i j u` and `u` real, `|w|^2 = 2 u^T u`; on `v0 = e_0 - i j e_0` the value table reads `E_{P_W} -> (2, 0)`, `E_{P_Wbar} -> (0, 2)`, and `E_{i j} -> (-2, +2)`.

Registration is per-mode, and the mode must be named. The K-real Hermitian invariant face `R I` registers identical values on `w` and `conj w` — genuinely blind to the doublet. The matrix `j` itself is the K-real NON-Hermitian linear witness: `E_j(w) = i |w|^2`, so it registers conjugate complex values `(2i, -2i)` on the pair — distinguishable as complex numbers, degenerate only in the (vanishing) real part. Every Hermitian separator of the doublet is therefore non-K-real; the named invariant example `i j` is K-odd, and the sharp projectors `P_W`, `P_Wbar` are exchanged by K. Outside the Hermitian face, `j` is the explicit K-real non-Hermitian escape. Block B4 gates the projector algebra, the eigenaction, the ranks, and the full value table.

## T4 — group-algebra bilinear nullity

Under the real bilinear (transpose, non-conjugating) pairing, the eigenspace `W = {u - i j u}` is totally isotropic, and for every `g` in `G` the form `v^T g v'` vanishes identically on `W` and on `Wbar`. The exact integer certificate is `g j = j g` together with `g + j g j = 0`, both holding for all `96` members — centrality and `j^2 = -I` force the second. Real vectors are not null (`A = I` registers `1` on `e_0`), and the non-invariant compression `E_00 = e_0 e_0^T` fails the certificate yet registers `1` on `W`, so the certificate discriminates. The consequence is restricted to the group-algebra bilinear face: every transpose-paired form with coefficient in `span_C(G)` vanishes on `W` and on `Wbar`, so registration within that face must instead use the conjugating (sesquilinear) pairing, where the K-parity split of T1-T3 governs. The `E_00` control is the explicit non-invariant bilinear escape, so no universal bilinear-pairing necessity is claimed. Block B5 gates the isotropy, the all-`96` certificate, and the `E_00` discriminator.

## T5 — orientation-flag registration and neutrality

The orientation binary is exactly the two-presentation freedom the upstream notes carry. The kernel note's Boundary records it: "It does NOT select the orientation: `+j` versus `-j` remains the two-presentation choice". The mechanism note carries the same freedom as its standing FLAG and Qualification:

> **FLAG — two-model mechanism:** the entrywise-conjugate presentations in L-K2 satisfy the same named clauses and exchange every K-odd seed.

> The memo's live Qualification leaves the unfixed choice conditional/open.

Sending `j -> -j` swaps `P_W <-> P_Wbar`, flips both `i j` and `E_j`, and fixes the K-real invariant Hermitian face `R I` pointwise; `-j` (raw representative `-J64` in the paired runner) is the other normalized central square root of `-I`. Thus the orientation flag registers on all three named orientation-sensitive presentations: as a sign in the K-real non-Hermitian witness `j` through `E_j`, as a sign in the K-odd Hermitian separator `i j`, and as a swap of the non-K-real projector pair. The K-real invariant Hermitian face, being `R I`, takes the same value under either orientation and is in that exact sense orientation-blind. These are the next named faces to interrogate once an orientation is physically fixed.

Neutrality: the graded (diagonal) members of `G` restrict to the `hw=1` triplet as diagonal matrices commuting with any `diag(w1, w2, w3)`, so no per-slot weight relation is forced — the classification is r-neutral. Block B6 gates the swap, the other root, the graded restriction, and r-neutrality.

## Negative controls

- Wrong-axis words: the axis-`1` and axis-`3` central-word candidates built from the same axis construction fail centrality against `G`, so only the `x2`-axis word is central.
- Wrong-sign polarization: `P_W - P_Wbar` equals `-(i j)`, not `+(i j)` — the sign of the polarization is fixed.
- Wrong-eigenvalue: `j v0` equals `i v0`, not `-i v0` — `v0` lies in `W`, not in `Wbar`.
- K-reality membership: the entrywise-real test passes for `j` and `I` and fails for `i j` and `P_W`, so the K-parity labels are not interchangeable.
- The `E_00 = e_0 e_0^T` discriminator fails the group certificate yet registers on `W`, confirming the certificate is not vacuous.

## Boundary

- It does NOT select the orientation: `+j` versus `-j` remains the two-presentation choice; this note only classifies which faces register the choice.
- It does not act on the mechanism note's live Qualification, which stays conditional/open.
- It derives no `r` value and forces no weighting, normalization, or probability; the classification is r-neutral.
- It is a finite fixed-surface statement (`L = 4` torus); no continuum or infinite-volume claim is made.
- It classifies the explicit named linear matrix faces only, on a finite algebraic carrier; genuinely antilinear readout functionals are not classified. It is NOT a universal-degeneracy or indistinguishability claim. The list of faces is deliberately non-complete, and the K-odd, non-K-real, non-Hermitian, and non-invariant bilinear escapes are explicit in the classification itself; no physical identification is made and nothing pre-record is forced.

## Gate map

| Block | What it checks | Gates |
|-------|----------------|-------|
| B1 | construction and ambient-K compatibility (`D2`, kernel, `V8` frame, grading, `conj(V8 c) = V8 conj(c)`) | 6 |
| B2 | group of order `96`, central `j` found by selection, closed form, Pauli word, rational commutant `span{I, j}` | 15 |
| B3 | T1 Hermitian bridge and conjugate-values lemma (symbolic) | 7 |
| B4 | T2 invariant face `{a I + c (i j)}` and T3 spectral polarization with value table | 14 |
| B5 | T4 bilinear nullity, all-`96` certificate `g + j g j = 0`, `E_00` discriminator | 7 |
| B6 | T5 neutrality, negative controls, ambient evaluation scale | 11 |
| B7 | verbatim source quotes present in both note and source | 11 |
| B8 | dependency ledger shard existence | 3 |
| B9 | note hygiene (links, required strings, pinned math) | 5 |

## Runner and cache

The [paired runner](../scripts/kcpt_kernel_kreal_readout_face_classification_2026_07_18.py) recomputes every gated quantity from the construction — the group, the central `j`, the projectors, the certificates, and the ambient scale — and checks each identity with exact integer or exact symbolic arithmetic. It prints `TOTAL: PASS=N FAIL=0` and exits nonzero on any failure. Its cached output is stored at [logs/runner-cache/kcpt_kernel_kreal_readout_face_classification_2026_07_18.txt](../logs/runner-cache/kcpt_kernel_kreal_readout_face_classification_2026_07_18.txt).
