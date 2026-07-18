# KCPT corner carrier: the two-presentation swap is proper-rotation conjugacy on the delivered carrier — K-parity coincides with rotation parity on the Hermitian section (bounded theorem)

- **Registry id:** `kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_bounded_theorem_note_2026-07-18`
- **Date:** 2026-07-18
**Claim type:** bounded_theorem
- **Paired runner:** [kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.py](../scripts/kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.py)
- **Runner cache:** `logs/runner-cache/kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.txt`

**Abstract.** The spectral-pairing note supplies a corner carrier `(C, P_chi, K)`. The
mechanism note's two-model comparison is a joint Pauli/corner comparison; its
corner-projector restriction contains the entrywise-conjugate pair `P_w`, `P_wbar`.
On the same one-component staggered surface on the periodic `4^3` torus
that the landed hw=1 delivery note used, this note delivers the presentation-swap as the
proper cubic rotation `M`: the pi-rotation about `[1,-1,0]` (`det M = +1`), realized as a
lattice unitary whose hw=1 kernel action is the transposition `TS` (T1). Rotation
conjugation by `TS` acts on the supplied projector family exactly as entrywise conjugation
`K`, `TS P_chi TS = conj(P_chi)` for every channel, so the projector pair is a single
2-orbit of the proper rotation and the canonical K-odd separator `D0 = P_w - P_wbar` is exchanged exactly
as by `K` (T2, T3). On the Hermitian probe section `W_H = a I + b C + conj(b) C^2` the
antilinear K-exchange coincides exactly with the linear rotation conjugation,
`conj(W_H) = TS W_H TS`; off the section the two gradings are inequivalent (witnesses
`C - C^2` and `i I`) (T4). Thus the `w` versus `wbar` projector labeling is a
rotation-frame orientation at the `C_3[111]` axis. This does not reclassify the full
Pauli/corner two-model comparison: `sigma_2 tensor I_3` is K-odd but fixed by the
corner rotation. The note does not fix the mechanism's choice and does not act on its
live Qualification. An honest operator-level covariance report for a named dressed
class (T5) is included and consumed by no other claim. All lattice arithmetic is exact
integer; all carrier algebra is exact symbolic.

## Purpose

The mechanism note's two-model FLAG compares a supplied joint Pauli/corner presentation
with its entrywise-conjugate presentation, and its live Qualification keeps the unfixed
choice conditional. This note asks a narrower structural question: is the induced exchange
of the two corner projectors a symmetry named by the framework axioms? It answers yes on
the delivered carrier — that projector exchange is conjugation by a proper cubic rotation
named by the LATTICE axiom — and records exactly where the answer stops. It reclassifies
only the `w` versus `wbar` projector labeling as a rotation-frame orientation; it neither
implements entrywise conjugation on the full joint presentation nor changes the memo's
live Qualification. The operator-level covariance report (T5) is a separate hardening
probe whose computed outcome is consumed by no claim here.

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

### The corner-projector pair is a proper-rotation orbit on the delivered carrier (T3, exact)

On the delivered carrier the entrywise-conjugate corner-projector pair is exchanged by an
element of the proper cubic rotation group named by the LATTICE axiom. Thus, on this
restricted surface, the `w` versus `wbar` label is a rotation-frame orientation at the
`C_3[111]` axis. A carrier-only tie-breaker invariant under the delivered rotation cannot
distinguish the two; a larger joint construction may consume additional internal or
co-transforming orientation data and is not classified here.
Concretely, `{P_w, P_wbar}` is a 2-orbit under `TS`-conjugation (`TS P_w TS = P_wbar`,
`TS P_wbar TS = P_w`, `TS P_1 TS = P_1`), this orbit coincides with the entrywise-conjugation
orbit, and the canonical K-odd separator `D0 = P_w - P_wbar` is exchanged exactly as by `K`:
`conj(D0) = -D0` and `TS D0 TS = -D0 = conj(D0)`. This is not the full
Pauli/corner orbit of the mechanism note: under the natural joint lift `I_2 tensor TS`,
`sigma_2 tensor I_3` is fixed by rotation conjugation but is K-odd. The memo's live
Qualification remains live and unfixed; this note does not act on that slot.

### K-parity equals rotation parity on the Hermitian section (T4, exact)

Channel values are `lam_chi(W(a,b,c)) = a + b*chi + c*chi^2`, with doublet separation
`lam_w - lam_wbar = i*sqrt(3)*(b - c)`; the swap `b <-> c` fixes `lam_1` and exchanges the
doublet pair. On the Hermitian section `W_H = a I + b C + conj(b) C^2` (with `b = b1 + i*b2`),
the antilinear K-exchange coincides exactly with the linear rotation conjugation,
`conj(W_H) = TS W_H TS`. Off the section the two gradings are inequivalent within the
carrier algebra: `C - C^2` is
K-even but rotation-odd and separates the doublet, while `i I` is K-odd but rotation-even
and does not separate. K-parity and rotation parity therefore coincide on the Hermitian
section of the carrier algebra and only there: for general complex `(a, b, c)` the difference
`conj(W) - TS W TS`
decomposes as `(conj(a) - a) I + (conj(b) - c) C + (conj(c) - b) C^2` with `I`, `C`, `C^2`
linearly independent, so it vanishes exactly when `a` is real and `c = conj(b)`.
On the larger mechanism surface, `sigma_2 tensor I_3` is a second escape: it is K-odd
but rotation-even under `I_2 tensor TS`, so the full joint K action is not delivered by
this corner rotation.

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

Four controls separate the delivered result from look-alikes. The proper rotation
`diag(-1,-1,1)` acts trivially on the hw=1 triplet while permuting sites, so properness
alone does not deliver the swap. The improper coordinate mirror `x1 <-> x2` has `det = -1`
and lies outside the axiom's proper rotation set, so no improper element is consumed. The
witness `i I` is rotation-even yet K-odd, so the K-parity and rotation-parity coincidence is
a fact about the Hermitian section rather than an identity of all carrier operators. The
joint-factor witness `sigma_2 tensor I_3` is K-odd but fixed by `I_2 tensor TS`, so the
corner-projector orbit is not silently promoted to the mechanism's full Pauli/corner
presentation.

## No-Go Discipline Gate

This gate covers the bounded negative content: the carrier-algebra `if and only if` in T4,
the zero triplet-preserving count inside T5's named finite class, and the boundary between
the corner-projector result and the mechanism's larger joint presentation.

### N1 — Alternative-route enumeration

| Route attacking the scoped boundary | Marker | Result |
|---|---|---|
| delivered proper site rotation | ATTEMPTED | `M` has determinant `+1`, and its exact kernel action is `TS`, which exchanges the projector pair (B1 and B2) |
| bare coordinate mirror | ATTEMPTED | it also induces the transposition but has determinant `-1`; it is outside the axiom's proper set (B1 item 11) |
| different proper rotation with trivial restriction | ATTEMPTED | `diag(-1,-1,1)` is proper and moves sites but acts as the identity on the triplet, so properness alone is insufficient (B1 item 10) |
| general carrier algebra | ATTEMPTED | rotation and K agree exactly on the Hermitian section and differ off it; `C-C^2` and `iI` witness both directions (B4 items 4 through 7) |
| full joint Pauli/corner presentation | ATTEMPTED | `sigma_2 tensor I_3` is K-odd but fixed by `I_2 tensor TS`; the full mechanism comparison is an explicit escape (B4 item 8) |
| operator-commuting dressings of `U2` | ATTEMPTED | the complete named `4096`-candidate enumeration has `64` commuting members and zero triplet-preserving members (B6 U2 block) |
| operator-commuting dressings of `U_R` | ATTEMPTED | the second complete named enumeration also has `64` commuting members and zero triplet-preserving members (B6 UR block) |

The last two rows close only the named finite classes. Other sign-field families, internal
spin lifts, interacting extensions, and larger joint constructions remain untested and are
not ruled out.

### N2 — Wall-independence audit

The note has three explicit scope boundaries rather than a universal no-go:

| Boundary pair | Does the first close the second? | Does the second close the first? | Disposition |
|---|---|---|---|
| inherited supplied/gate carrier surface; projector-family restriction | no: a lattice carrier does not identify the full K action with rotation | no: the projector identity does not derive the carrier at the mechanism-note origin | independent and stated |
| projector-family restriction; Hermitian carrier section | no: projector exchange holds while general carrier operators still separate the actions | no: the Hermitian-section identity does not enlarge the claim to the joint presentation | independent and stated |
| Hermitian carrier section; named dressed operator class | no: carrier-algebra equality does not imply commutation with `D` | no: commuting dressings do not preserve the hw=1 triplet in the searched class | independent and stated |

No inflated wall count is used; T1-T4 consume none of T5.

### N3 — Hidden-wall scan

The scan terms are “we assume”, “by construction”, “as is standard”, “the framework
provides”, “bridge context”, “background”, “naturally”, “obviously”, “standard QFT”,
“registered”, and “canonical”. “Canonical” occurs only in the supplied-basis and
separator names; “framework axioms” is accompanied by the two verbatim Lattice and
Admissibility quotations. The periodic `4^3` surface, corner basis, projector-family
restriction, Hermitian section, and `4096`-candidate dressing class are all explicit.
No hidden spin lift, action, readout, measure, or weight rule is consumed.

### N4 — Residual matching

| Cited source | Source residual or role | Residual addressed here | Match? |
|---|---|---|---|
| spectral-pairing note | supplied abstract corner carrier and its supplied-surface FLAG | proper-rotation delivery of the projector exchange on the gate-note carrier | yes, at the gate note's bounded surface; the origin FLAG remains |
| mechanism note | full joint Pauli/corner two-model comparison and live Qualification | corner-projector restriction only | partial, not full; the joint-factor witness prevents use as a closure or reclassification of the full FLAG |
| landed carrier-delivery note | `C`, projector family, and entrywise `K` on the hw=1 carrier | same `V`, `C`, and periodic `4^3` surface | yes |
| T5 finite-class report | no prior negative witness is cited | direct complete count in two named classes | direct computation; no residual substitution |

### N5 — Rhetoric and resolution audit

The equality `TS P_chi TS = conj(P_chi)` is tested at projector resolution. The stronger
carrier-algebra comparison is tested exactly and holds only on the Hermitian section. The
joint Pauli/corner comparison is not claimed and has an explicit counter-witness. At the
lattice-operator resolution, only the two named dressing classes are enumerated; no
lattice-wide or all-operator nonexistence statement is made. T5's “zero” therefore always
means zero among the `64` commuting members of the stated `4096`-candidate class.

### N6 — Partial-closure paths

| Candidate path | Current treatment | What it could change |
|---|---|---|
| internal spin lift or another joint representation of the rotation | untested | could act nontrivially on the Pauli factor; outside the corner-only proof |
| co-transforming orientation datum or larger covariant clause set | untested | could select a joint orientation without being a carrier-only invariant |
| wider sign-field, translation, or interacting dressing class | untested | could contain an operator that both commutes with `D` and preserves the hw=1 triplet |
| a physical action/readout selector | open outside this note | could fix the mechanism's presentation choice or a weight without contradicting the projector orbit |

These are ordinary downstream theorem paths, not new axioms, and none is foreclosed.

### N7 — Steelman

Strongest objection: the mechanism's entrywise-conjugate presentations include the Pauli
factor and every K-odd seed, while the rotation proved here acts only on the corner carrier.
The objection is decisive against reclassifying the full FLAG: `sigma_2 tensor I_3` is the
exact counterexample. The claim is therefore restricted to the corner projectors and, for
general carrier probes, to the Hermitian section. A second objection is that the failure of
the searched commuting dressings may be an artifact of the six-bit sign-field ansatz. That
is also granted; T5 reports only its named finite class and is consumed by no theorem claim.

### N8 — Cross-cycle echo

The closest echo is the landed carrier-delivery note: its N1 scan already records that joint
qubit/corner observables escape a bare-carrier classification. The spectral-pairing note
keeps entrywise `K` distinct from the adjoint and requires an extra declared reading before
moving the mechanism to the coupling slot. The mechanism note itself constructs a jointly
K-even qubit/corner witness whose factors are separately K-odd. The older carrier-orbit
ledger at `.claude/science/physics-loops/carrier-orbit-invariance-2026-05-03/NO_GO_LEDGER.md`
likewise warns that adding an antisymmetric carrier primitive would break a carrier-only
swap reduction. Those precedents are respected here by keeping the joint, internal-lift,
and larger-dressing routes open.

**Gate result: PASS.** The exact projector orbit and Hermitian-section characterization
survive; the full mechanism FLAG and all operator classes outside T5's finite search remain
explicitly unclassified.

## Non-claims

This note does not fix the mechanism's presentation choice and does not act on the memo's
live Qualification. It reclassifies only the `w` versus `wbar` corner-projector label, not
the full Pauli/corner comparison or every K-odd seed. It does not upgrade the supplied
corner surface to physically derived status, and it does not claim the delivered rotation
is the sole operator implementing the exchange. A larger joint construction may use
internal or co-transforming orientation data. The T5 report is consumed by no claim here.
No weight `r` is forced, derived, or selected.

## Dependency roles and status boundary

Each dependency supplies a specific object: the framework axioms name the proper cubic
rotation group and the admissibility covariance; the staggered realization gate names the
operator surface; the spectral-pairing note supplies the corner carrier and its declared
FLAG; the mechanism note supplies the broader two-model FLAG and its live Qualification,
which bound rather than enlarge the projector-family result; and the
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
