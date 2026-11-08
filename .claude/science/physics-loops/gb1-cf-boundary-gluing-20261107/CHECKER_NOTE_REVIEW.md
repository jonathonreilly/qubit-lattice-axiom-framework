# Focused mathematical source review

Reviewed source, in full (387 lines):
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/docs/SU2_FINITE_BOUNDARY_FLUX_ASSOCIATIVE_GLUING_BOUNDED_THEOREM_NOTE_2026-11-07.md`

Exact SHA-256:
`b647a3d91afbd17c1b99d0ea512f3cef69cf77d87b79d4ee69fbc32a5615fe98`.

This is a focused mathematical review against the already frozen independent
derivation, not a landing decision, audit verdict, or retained-status decision.
No mathematical error was identified in the stated finite-model theorem at
this hash. Two optional clarifications are listed below. Implementation,
cache, primary-runner mutation, and handoff receipts are outside this review.

## Checked argument

1. **Cut normalization and completeness, sections 1–2.** Haar invariance
   makes `S f(g1,g2)=f(g2 g1)` an isometry. The coefficient formula has the
   required `d_j^(-1/2)` factor and the correct reversed traversal order.
   At the new vertex, `Inv(V_j1 tensor V_j2^*)` is one-dimensional exactly
   when `j1=j2`; the remaining endpoint indices give `1+4=5` states.
   Thus the whole new-vertex invariant space is the image, not merely a
   space containing five proposed vectors. The spin-zero sector and
   repeated cuts are covered. In the coordinate formula the cross term is
   correctly positive in tensor order segment 1 then segment 2: the Pauli
   product initially gives `-epsilon_abc x_b(g2)x_c(g1)`, and exchanging the
   two displayed tensor indices produces the plus sign. Both cut orders
   yield `f(g3 g2 g1)`.

2. **Compressed transporter identity, section 2.** Extending `S` to the
   full Haar space makes `QS=SP` valid on every representation sector,
   including the discarded sectors. Componentwise,
   `Q M_(g2 g1) Q = sum_k (P2 M_(g2,ak) P2)(P1 M_(g1,kb) P1)`:
   projectors and multipliers on different links commute, so no missing
   intermediate projection is hidden in this equality. On retained inputs,
   `Q M_(g2 g1) S = QS M_g = S P M_g P` proves the strong identity
   `(U2 U1)S=SU`. Repeating it with the adjoint multiplication function proves
   `(U2 U1)^dagger S=S U^dagger`. Hence the image is reducing for these
   specified reconstructed operators, and their words and color traces
   intertwine. This agrees with the frozen checker's separate epsilon-index
   contraction proof; no primary implementation was inspected.

3. **Electric accounting, section 2.** Each segment has the same spin label,
   so each Casimir separately intertwines `E^2`, while the unweighted sum
   gives twice that operator. Since the retained nonconstant sector has
   nonzero eigenvalue `3/4`, preservation of one original term requires
   `lambda1+lambda2=1`. The stated repeated-subdivision weight rule follows.
   This is an operator identity, not a derivation of a physical coupling or
   metric. The note preserves that distinction.

4. **General regional associativity and open boundaries, section 3.** Let
   `Pi_A` be the product of vertex Haar projectors for `I(A)`. Embedded in
   the edge space of `A union B`, the already imposed projectors in
   `Pi_A tensor Pi_B` are among those defining `Pi_(A union B)`. All commute,
   and applying exactly the newly internal ones therefore has range
   `im Pi_(A union B)`. Induction over any binary grouping proves the claimed
   subspace identity. This argument remains valid for disconnected regions,
   empty regions, and isolated vertices; the latter projectors are identities.
   A vertex outside `V0` is never projected, even after its complete star is
   present. The final-interface representation decomposition uses only the
   group whose constraints are newly required. Other boundary group actions
   commute with that group and act on the multiplicity spaces. They are not
   erased by the displayed dimension formula. Schur contraction contributes
   one invariant for each matched irrep pair, not an additional irrep
   dimension. The cubic-valence spin bound is also correct for the stated
   cubic graph, without being asserted for arbitrary-valence graphs.

5. **Four-spin witness, section 3.** Writing
   `t0=(|01>+|10>)/sqrt(2)`, the displayed vector is
   `|00>|11> + |11>|00> - |t0>|t0>`. Its three orthogonal terms give norm
   squared 3. Every term has total magnetic quantum number zero; direct
   application of the total raising operator gives coefficients
   `1-1/2-1/2=0` for each possible three-up basis vector. The lowering
   operator vanishes by the same calculation or global bit reversal.
   Thus the total spin is zero. Its first pair is symmetric and hence
   spin one, so a premature first-pair singlet projector annihilates it.
   The other four-spin invariant comes from singlet times singlet. This
   checks both the two-dimensional invariant space and the explicitly lost
   state, without a new numeric job.

6. **Graph counts, section 4.** The boundary characters
   `T=1+xy+yz+xz` and `T(1+xy)(1+yz)` coincide with the frozen derivation,
   as do dimensions 13 and 325 and matching-sector multiplicities
   `4,5,5,4`. The full-graph count independently follows from 16 even
   subgraphs and the extra singlet in each of the two degree-four center
   configurations: 18. The three-piece grouping retains the same full
   character. For center-only Gauss law the star rank is
   `1+6*4+16*2=57`, leaving eight unconstrained five-state links and total
   dimension `57*5^8=22,265,625`. The losses 14 from zeroing all interface
   flux and 2 from deleting invariant multiplicity refer to different
   specified counting mistakes. No universal impossibility is inferred.

7. **Operators and axiom scope, sections 5–6.** Commutation with the imposed
   constraints suffices for restricting an operator to the glued invariant
   subspace. Shared edges use shared tensor factors, so the overlap discussion
   does not duplicate physical links or assert overlapping-operator
   commutativity. Counting each term once and restricting a fixed global
   operator is independent of regional bookkeeping. Covariance of a
   symmetry-invariant sum passes to its exponential, without establishing
   a finite-depth local schedule or equality of ordered patch exponentials.
   The initialized five-word code in three qubits is a valid finite embedding;
   zero-extended operators preserve it, while a trivial gauge action on the
   unused words cannot remove those words by Gauss law. The note expressly
   leaves homogeneous native allocation, the required local law, Record
   realization, state/clock/coupling identifications, and continuum claims
   open. This agrees with the frozen current-axiom memo. The construction
   is not presented as selected by the four physical axioms.

## Optional clarity improvements, not mathematical errors

- **Line 133:** after stating the adjoint identity, add that the same
  argument is repeated with `M_g^dagger`. Merely taking the adjoint of
  `AS=SU` would yield `S^dagger A^dagger=U^dagger S^dagger`, which alone
  does not prove `A^dagger S=S U^dagger`. The required stronger identity
  does follow from the proof's existing hypotheses, as checked above.
- **Lines 305–306:** qualify the matching sentence as applying to
  boundary charge **at vertices where Gauss law is being imposed**.
  Unconstrained outer-boundary actions need no such compensating action.
  Section 3 and the immediately preceding operator sentence already make
  the intended convention clear; this change would prevent reading the
  sentence as a blanket statement about every open boundary.

## Provenance and limits

The independently derived comparison packet was frozen before this source
was read: `CHECKER.md` SHA-256
`bf7e6f3150d29ffd8d872a8d896dda97405e6e49b07097305aae7aeadb66df1d`;
runner SHA-256
`e4291452252f60610eb40526d055e400bb3ef09a23c65d08c7b2918eba03044e`;
raw evidence SHA-256
`8a02e6e6809e53b89df99e9ab8ce44f0cadccf01d18aa62b0a35bee224c31956`.
Those artifacts were not altered. This review retains the inherited model
and reasoning configuration; it is a fresh-context same-family derivation
followed by a source comparison, not a cross-family or formal-audit check.

The cited [Donnelly paper](https://arxiv.org/pdf/1109.0036), section II,
equations (8)–(14), does discuss the multiplication embedding, open boundary
representation states, and normalized contractions. The finite-cutoff and
operator conclusions here were checked from their stated hypotheses, rather
than accepted from that citation.

The entire note, including front matter and evidence prose, was read. The
claims about primary-runner execution, helper invocation/import timing,
cache manifests, final cache outputs, primary mutations, handoff contents,
PR history, and repository integration checks were not verified and are
outside this review's scope. The primary implementation and comparison
artifacts were not inspected. No new numerical computation, commit, push,
status change, or edit to the reviewed source was made. The only new file
written for this follow-up is this exact-hash review.
