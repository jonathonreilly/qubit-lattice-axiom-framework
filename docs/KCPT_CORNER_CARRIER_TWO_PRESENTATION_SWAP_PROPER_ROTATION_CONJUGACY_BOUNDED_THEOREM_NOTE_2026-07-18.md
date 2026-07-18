# KCPT corner carrier: the two-presentation swap is proper-rotation conjugacy on the delivered carrier — K-parity coincides with rotation parity on the Hermitian section (bounded theorem)

- **Registry id:** `kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_bounded_theorem_note_2026-07-18`
- **Date:** 2026-07-18
**Claim type:** bounded_theorem
- **Paired runner:** [kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.py](../scripts/kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.py)
- **Runner cache:** `logs/runner-cache/kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.txt`

**Abstract.** The spectral-pairing note supplies a corner carrier `(C, P_chi, K)` and the
mechanism note flags a two-model presentation pair — the entrywise-conjugate images
`(C, P_w, K)` and `(C, P_wbar, K)` — with an unfixed binary choice and a live
Qualification. On the same one-component staggered surface on the periodic `4^3` torus
that the landed hw=1 delivery note used, this note delivers the presentation-swap as the
proper cubic rotation `M`: the pi-rotation about `[1,-1,0]` (`det M = +1`), realized as a
lattice unitary whose hw=1 kernel action is the transposition `TS` (T1). Rotation
conjugation by `TS` acts on the supplied projector family exactly as entrywise conjugation
`K`, `TS P_chi TS = conj(P_chi)` for every channel, so the pair is a single 2-orbit of the
proper rotation and the canonical K-odd separator `D0 = P_w - P_wbar` is exchanged exactly
as by `K` (T2, T3). On the Hermitian probe section `W_H = a I + b C + conj(b) C^2` the
antilinear K-exchange coincides exactly with the linear rotation conjugation,
`conj(W_H) = TS W_H TS`; off the section the two gradings are inequivalent (witnesses
`C - C^2` and `i I`) (T4). The unfixed binary choice is thereby a rotation-frame
orientation at the `C_3[111]` axis; the note does not fix it and does not act on the
memo's live Qualification. An honest operator-level covariance report for a named dressed
class (T5) is included and consumed by no other claim. All lattice arithmetic is exact
integer; all carrier algebra is exact symbolic.

## Purpose

The mechanism note's two-model FLAG leaves an unfixed binary choice between the two
entrywise-conjugate presentations of the supplied corner carrier, and its live
Qualification keeps that choice conditional. This note asks a structural question about
that choice: is the exchange of the two presentations a symmetry named by the framework
axioms? It answers yes on the delivered carrier — the exchange is conjugation by a proper
cubic rotation named by the LATTICE axiom — and records exactly where the answer stops. It
reclassifies the unfixed choice as a rotation-frame orientation without fixing it, and it
leaves the memo's live Qualification untouched. The operator-level covariance report (T5)
is a separate hardening probe whose computed outcome is consumed by no claim here.

## Supplied objects and consumed readings

This note consumes only the sentences quoted verbatim below; each is reproduced from its
source without paraphrase, and the paired runner gates both the source text and these
blockquotes.

From the spectral-pairing note, the supplied corner carrier:

> The real cyclic `C` with `C^3 = I_3` and `C^T = C^2`, the character
> projectors `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for
> `chi in {1, w, conj(w)}`, `w = -1/2 + (sqrt(3)/2)*i`, and entrywise
> conjugation `K` in the canonical basis.

and its declared surface FLAG:

> **FLAG — supplied surface:** this is the mechanism note's declared
> corner surface, not a derived physical carrier.

From the mechanism note, the two-model FLAG and its live Qualification:

> **R2 — K-real derivable initial data.** Derivable initial data is K-real.
> **FLAG — two-model mechanism:** the entrywise-conjugate presentations in
> L-K2 satisfy the same named clauses and exchange every K-odd seed. The
> memo's live Qualification leaves the unfixed choice conditional/open.

From the framework axioms, the axiom-native proper-rotation symmetry set:

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic
> rotations about each site.

and

> There is one fixed nearest-neighbor admissibility rule, covariant under
> lattice translations and proper cubic rotations.

From the landed hw=1 delivery note, the delivered carrier this note reuses:

> the `C_3[111]` lattice rotation restricted to the hw=1 kernel triplet of
> the one-component staggered operator on the periodic `4^3` torus IS the
> real cyclic `C` (entries exactly `{0,1}`, `C^3 = I`, `C^T = C^2`), and
> ambient complex conjugation restricts to entrywise conjugation `K` in the
> corner basis (T1).

## Claims

Fix the one-component staggered operator `D` on the periodic `4^3` torus, its exact kernel
(dimension `8`, spanned by the corner plane waves graded `1+3+3+1`), and the hw=1 kernel
triplet carrying `V`. The supplied carrier `(C, P_chi, K)` is the real cyclic `C` with
`C^3 = I`, `C^T = C^2`, its character projectors, and entrywise conjugation `K`, exactly as
the landed delivery note placed it on this surface. Throughout, `TS` is the transposition
`[[0,1,0],[1,0,0],[0,0,1]]`, the hw=1 action of the swap.

### Lattice delivery of the presentation-swap rotation (T1, exact)

The swap `R2(x1,x2,x3) = (-x2,-x1,-x3) mod 4` has site matrix
`M = [[0,-1,0],[-1,0,0],[0,0,-1]]`, an integer orthogonal signed permutation with
`det M = +1` (PROPER), `M^2 = I`, and fixed axis `M [1,-1,0]^T = [1,-1,0]^T`: the
pi-rotation about `[1,-1,0]`, an element of the proper cubic rotation group named by the
LATTICE axiom. Its lattice unitary `U2` (site permutation by `R2`) is a symmetric
involution that conjugates the landed `C_3[111]` rotation to its inverse
(`U2 U_R U2 = U_R^T`), conjugates translations by `M`
(`U2 T1 U2 = T2^3`, `U2 T2 U2 = T1^3`, `U2 T3 U2 = T3^3`), and is sign-free covariant on the
corner waves (`U2 V8 = V8 PI`, `PI` a subset permutation). Restricted to the hw=1 triplet
it is the transposition, `U2 V = V TS`. This is the landed delivery standard — translation
conjugacy together with the kernel action — applied to the swap. A proper rotation that
acts trivially on the triplet (`diag(-1,-1,1)`) and the improper coordinate mirror
(`det = -1`, outside the axiom's proper set) are held as negative controls.

### Rotation conjugation equals entrywise conjugation on the supplied projector family (T2, exact)

On the supplied carrier, `TS C TS = C^T = C^2` and `C` is real. For every channel
`chi in {1, w, wbar}`, `TS P_chi TS = conj(P_chi)`; in particular `TS P_w TS = P_wbar` and
`TS P_1 TS = P_1`. The generator coherence `P_wbar(C) = P_w(C^2)` shows the rotation image
presents the same projector with its natural generator. Conjugation by the real `TS`
composed with `K` is an antilinear involution fixing every `P_chi`, and the probe transform
is `TS W(a,b,c) TS = W(a,c,b)`.

### The two-model pair is a proper-rotation orbit on the delivered carrier (T3, exact)

On the delivered carrier the entrywise-conjugate presentation pair lies on a single orbit of the proper cubic rotation group named by the LATTICE axiom; the unfixed binary choice in the two-model FLAG is a rotation-frame orientation at the `C_3[111]` axis, and any clause set that breaks the tie must break proper-rotation covariance at that orientation.
Concretely, `{P_w, P_wbar}` is a 2-orbit under `TS`-conjugation (`TS P_w TS = P_wbar`,
`TS P_wbar TS = P_w`, `TS P_1 TS = P_1`), this orbit coincides with the entrywise-conjugation
orbit, and the canonical K-odd separator `D0 = P_w - P_wbar` is exchanged exactly as by `K`:
`conj(D0) = -D0` and `TS D0 TS = -D0 = conj(D0)`. The memo's live Qualification remains live and unfixed; this note does not act on that slot.

### K-parity equals rotation parity on the Hermitian section (T4, exact)

Channel values are `lam_chi(W(a,b,c)) = a + b*chi + c*chi^2`, with doublet separation
`lam_w - lam_wbar = i*sqrt(3)*(b - c)`; the swap `b <-> c` fixes `lam_1` and exchanges the
doublet pair. On the Hermitian section `W_H = a I + b C + conj(b) C^2` (with `b = b1 + i*b2`),
the antilinear K-exchange coincides exactly with the linear rotation conjugation,
`conj(W_H) = TS W_H TS`. Off the section the two gradings are inequivalent: `C - C^2` is
K-even but rotation-odd and separates the doublet, while `i I` is K-odd but rotation-even
and does not separate. K-parity and rotation parity therefore coincide on the Hermitian
section and only there: for general complex `(a, b, c)` the difference `conj(W) - TS W TS`
decomposes as `(conj(a) - a) I + (conj(b) - c) C + (conj(c) - b) C^2` with `I`, `C`, `C^2`
linearly independent, so it vanishes exactly when `a` is real and `c = conj(b)`.

### Operator-level covariance report for the named dressed class (T5, computed report)

This block is an honest computed report and is consumed by no other claim; T1-T4 use only
the kernel-action and conjugation facts above and take nothing from it. As computed by the
paired runner: the undressed lattice unitaries `U2` and `U_R` each fail to commute with the
staggered operator `D`. Within the named class of `4096` candidates — the `64` diagonal
sign fields (linear plus bilinear in the site coordinates) times the `64` lattice
translations, applied to each unitary — exactly `64` members commute with `D` for `U2` and
`64` for `U_R`. Every commuting member preserves the full eight-dimensional corner-wave
kernel, yet none of the `64` in either class preserves the hw=1 triplet subspace (the
off-triplet residual of `U V` is nonzero in every case); a one-bit flip of an exemplar's
sign field breaks commutation, and the identity dressing has a nonzero commutator with `D`.
The report records that the operator-commutation standard and the T1 kernel-action standard
are met by different operator sets on this surface; it makes no claim used elsewhere.

## Gated controls

The paired runner gates, in exact arithmetic: the staggered construction and its exact rank
`56` / kernel dimension `8` (Block A); the T1 delivery items — `M` proper involution, fixed
axis, the group relation `M C M = C^T`, `U2` involution and its translation and rotation
conjugacies, sign-free corner-wave covariance, and the hw=1 transposition (B1); the T2
projector-family conjugation identities (B2); the T3 orbit and K-odd separator (B3); the T4
channel values, Hermitian-section coincidence, exact section characterization, and
off-section witnesses (B4); the
weight-neutrality guard (B5); the computed T5 report (B6); the verbatim source and note
quote pairs (B7); ledger shard existence (B8); and note hygiene (B9).

## Negative controls

Three controls separate the delivered result from look-alikes. The proper rotation
`diag(-1,-1,1)` acts trivially on the hw=1 triplet while permuting sites, so properness
alone does not deliver the swap. The improper coordinate mirror `x1 <-> x2` has `det = -1`
and lies outside the axiom's proper rotation set, so no improper element is consumed. The
witness `i I` is rotation-even yet K-odd, so the K-parity and rotation-parity coincidence is
a fact about the Hermitian section rather than an identity of all operators.

## No-Go Discipline Gate

This bounded theorem asserts a positive structural coincidence on a supplied carrier; the
discipline gate records what it does not claim and how each boundary is held.

### N1 — Alternative-presentation scope

The claim ranges over the two entrywise-conjugate presentations named by the FLAG and over
the proper cubic rotation group; it does not range over other supplied carriers or other
axes.

| Boundary | Status |
|---|---|
| presentation pair and proper rotations only | addressed |

### N2 — No status assertion

No dependency status is asserted or consumed; the note consumes only the quoted sentences.

| Boundary | Status |
|---|---|
| status set by the audit lane | addressed |

### N3 — Negative controls present

The trivial-restriction rotation, the improper mirror, and the rotation-even K-odd witness
separate the result from look-alikes.

| Boundary | Status |
|---|---|
| three explicit controls | addressed |

### N4 — Scope boundary stated

The coincidence of K-parity and rotation parity holds on the Hermitian section; off the
section the two gradings differ, as witnessed.

| Boundary | Status |
|---|---|
| Hermitian section only | addressed |

### N5 — Inherited FLAG preserved

The corner surface is the mechanism note's supplied surface; that inherited FLAG is carried
unchanged, not removed.

| Boundary | Status |
|---|---|
| supplied-surface FLAG carried | addressed |

### N6 — No weight selection

No weight `r` is referenced, forced, derived, or selected; the guard exhibits only the
swap-invariance of the doublet symmetric functions.

| Boundary | Status |
|---|---|
| weight-neutral | addressed |

### N7 — Exact arithmetic only

Every gate is exact integer or exact symbolic; the report uses no float, tolerance, or
randomness.

| Boundary | Status |
|---|---|
| exact arithmetic | addressed |

### N8 — Consumed readings are verbatim

Each consumed sentence is quoted without paraphrase and gated against both its source and
this note's blockquote.

| Boundary | Status |
|---|---|
| verbatim quote gates | addressed |

## Non-claims

This note does not fix the presentation choice and does not act on the memo's live
Qualification. It does not upgrade the supplied corner surface to physically derived status,
and it does not claim the delivered rotation is the sole operator implementing the exchange.
The T5 report is consumed by no claim here. No weight `r` is forced, derived, or selected.

## Dependency roles and status boundary

Each dependency supplies a specific object: the framework axioms name the proper cubic
rotation group and the admissibility covariance; the staggered realization gate names the
operator surface; the spectral-pairing note supplies the corner carrier and its declared
FLAG; the mechanism note supplies the two-model FLAG and its live Qualification; and the
landed hw=1 delivery note supplies the delivered carrier this note reuses. This note adds a
structural coincidence on that delivered carrier and consumes no status-dependent content
from any dependency. **Status authority:** independent audit lane only. Statuses of all dependencies are set by the independent audit lane; this note asserts no dependency status and consumes no status-dependent content.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md](KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md)
- [KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md](KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md)
- [KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md)

### Non-citation context handles

Two adjacent `AC_phi_lambda` notes are named for orientation only and are not consumed as
dependencies:

- `ACPHILAMBDA_C3_RESOLVENT_DETERMINANT_HOLONOMY_COUPLING_NARROW_THEOREM_NOTE_2026-07-12.md`
- `ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md`

Context orientation only; no content is consumed from either.

## Verification

**The paired runner re-derives every claim above in exact integer and exact symbolic
arithmetic, prints a PASS or FAIL line per gate, and exits nonzero if any gate fails.**
**No check passes by literal stipulation.**
