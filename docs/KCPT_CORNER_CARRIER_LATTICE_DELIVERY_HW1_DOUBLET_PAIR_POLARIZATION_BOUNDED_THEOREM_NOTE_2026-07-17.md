# KCPT corner-carrier lattice delivery: the gate-note hw=1 triplet realizes the supplied corner surface, and doublet-pair separation is K-gated (bounded theorem)

- **Registry id:** `kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_bounded_theorem_note_2026-07-17`
- **Date:** 2026-07-17
**Claim type:** bounded_theorem
- **Paired runner:** [kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_2026_07_17.py](../scripts/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_2026_07_17.py)
- **Runner cache:** `logs/runner-cache/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_2026_07_17.txt`

**Abstract.** The 2026-07-16 spectral-pairing note consumes a supplied corner triple
`(C, P_chi, K)` and flags it as a supplied surface, not a lattice object. This note
computes, in exact integer and symbolic arithmetic, that the staggered gate note's
composed surface delivers that triple verbatim: the `C_3[111]` lattice rotation
restricted to the hw=1 kernel triplet of the one-component staggered operator on the
periodic `4^3` torus IS the real cyclic `C` (entries exactly `{0,1}`, `C^3 = I`,
`C^T = C^2`), and ambient complex conjugation restricts to entrywise conjugation `K`
in the corner basis (T1). On the delivered carrier, `K` fixes the singlet channel and
pairs the two doublet channels into a single 2-orbit (T2); the spectral-pairing
license instantiates exactly, negative control included (T3). The bounded negative
(T4): the Hermitian, K-real members of the equivariant class are exactly the
two-parameter real family `a*I + b*(C + C^2)`, whose doublet channel values are
exactly equal; separation is nonzero exactly when the observable has a nonzero K-odd
component. This is a classification of explicitly K-real carrier observables, not a
nonderivability statement. The mechanism note itself constructs the unlabeled spectral
PVM of a K-odd separator and calls that PVM derivable and registrable; this note
reproduces the separator exactly. The classification
leaves the singlet and shared-doublet channel values free, so nothing here forces,
derives, or prefers any value of `r`.

## Purpose

The spectral-pairing note (2026-07-16) proved fixed-point-versus-2-orbit structure on
a corner triple it had to assume, and said so with a FLAG. The gate note has carried,
since 2026-05-03, a composed lattice surface whose hw=1 kernel triplet has exactly
the required shape. This note joins the two: it computes the identification exactly
(so the pairing results now live on a lattice-delivered carrier at the gate note's
declared premise set), and then asks the polarization question one level down — which
channels of the delivered carrier can explicitly K-real Hermitian observables
distinguish? The answer is that their expectations on the two conjugate doublet lines
are equal, even without equivariance. K-odd observables do separate the lines. The
result is therefore a carrier-algebra boundary, not a restriction on which observables
are derivable or registrable.

## Supplied objects and consumed readings

Four source passages are consumed verbatim; the runner (block B6) gates each against its
source text and against the blockquotes below.

From the spectral-pairing note, the supplied carrier (R1c):

> The real cyclic `C` with `C^3 = I_3` and `C^T = C^2`, the character projectors
> `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for `chi in {1, w, conj(w)}`,
> `w = -1/2 + (sqrt(3)/2)*i`, and entrywise conjugation `K` in the canonical basis.

From the same note, the supplied-surface FLAG this note addresses:

> **FLAG — supplied surface:** this is the mechanism note's declared corner surface,
> not a derived physical carrier.

From the mechanism note, the observable-face boundary that limits T4:

> The observable face is not closed. Doublet-resolving PVMs and registrations are
> derivable and registrable: the unlabeled spectral PVM of `i(C-C^2)` and the joint
> witness `W` are explicit examples. Nothing here forecloses them. The theorem is
> about registered **weights**.

From the gate note, the species-surface clause naming the parent surface on which
delivery happens:

> the hw=1 triplet is three pairwise orthogonal, translation-character-distinct
> states in one physical Hilbert space, connected by the `C_3[111]` lattice unitary

## Claims

**Setting (runner block A, exact integer arithmetic).** `D` is the one-component
staggered operator on the periodic `4^3` torus with the Kawamoto-Smit phases
`eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}`. `2D` is an
integer antisymmetric matrix with entries in `{-1, 0, 1}`; its exact rank is `56`,
so `dim ker D = 8`, and the eight corner plane waves `(-1)^{sum_{mu in S} x_mu}`
(for `S` a subset of the three axes) are exact, mutually orthogonal null vectors —
they span the kernel, graded by Hamming weight as `1 + 3 + 3 + 1`. The hw=1 triplet
is `v_mu(x) = (-1)^{x_mu}`, ordered so slot `mu` carries translation character `-1`
in direction `mu` (joint characters `(-1,+1,+1)`, `(+1,-1,+1)`, `(+1,+1,-1)`,
computed exactly). `U_R` is the proper-rotation permutation
`(U_R f)(x) = f(R^{-1} x)` with `R^{-1}(x_1, x_2, x_3) = (x_2, x_3, x_1)`; it is a
permutation matrix with `U_R^3 = I` conjugating the translations cyclically.

### Lattice delivery of the supplied corner carrier (T1, exact)

1. `U_R V = V C` exactly on the integer lattice, where `V` is the ordered hw=1
   corner triplet and `C = [[0,0,1],[1,0,0],[0,1,0]]`. The matrix of the
   `C_3[111]` lattice unitary restricted to the hw=1 kernel triplet, in the corner
   basis, has entries exactly `{0,1}` — no signs, no phases — and is the real
   cyclic `C` of the supplied triple. In particular `U_R` maps corner `1` to
   corner `2` with coefficient `+1`.
2. `C^3 = I` and `C^T = C^2` exactly — the supplied relations.
3. Because the corner basis is entrywise real, ambient complex conjugation on the
   lattice Hilbert space restricts to entrywise conjugation `K` in the corner
   basis: `conj(V z) = V conj(z)` for every coefficient vector `z`.
4. The character projectors built from the delivered `C` are Hermitian rank-one,
   mutually orthogonal, resolve the identity, and carry the exact
   channel-eigenvalue association `C P_chi = chi P_chi`.
5. **Scope.** This is a lattice realization of the spectral-pairing note's supplied
   triple on the gate note's composed surface, at the gate note's declared premise
   set (residuals inherited below). On the mechanism-note side the corner surface
   remains supplied: nothing here converts the mechanism note's declaration into a
   derivation of its own surface. The FLAG is answered at the gate note's premise
   set, not erased at its origin.

### K-polarization of the delivered channels (T2, exact)

1. `K P_1 K = P_1`: the singlet channel is K-fixed, and its democratic direction
   `(1,1,1)/sqrt(3)` is entrywise real (a K-fixed vector).
2. `K P_w K = P_wbar` and `K P_wbar K = P_w`: the two doublet channels form a
   single K 2-orbit.
3. At the vector level, `vw = (1, wbar, wbar^2)/sqrt(3)` satisfies `C vw = w vw`,
   `K` maps the `w`-eigenline to the `wbar`-eigenline, and `P_w = vw vw^dagger`
   exactly.

### Spectral-pairing license instantiated on the delivered carrier (T3, exact)

1. For entrywise-real `(a, b, c)`, the operator `a*I + b*C + c*C^2` on the
   delivered carrier has channel eigenvalues `lam_0 = a + b + c` (real) and
   `lam_1, conj(lam_1)` on the doublet pair, with
   `det = lam_0 * |lam_1|^2` exactly — the count-once form of the
   spectral-pairing note, now on the lattice-delivered carrier.
2. The pairing is a property of the entrywise-real locus, not of the carrier: the
   negative control below reproduces the spectral-pairing note's failure witness.

### Doublet-pair separation is K-gated on the delivered carrier (T4, exact negative boundary)

1. The commutant of `C` in the full complex matrix algebra has dimension exactly
   three and is spanned by `{I, C, C^2}` (exact rank computations).
2. The Hermitian, K-real members of the commutant are exactly the two-parameter
   real family `a*I + b*(C + C^2)` (exact linear-system computation: constraint
   rank four, kernel spanned by `I` and `C + C^2`).
3. Every member of that family has characteristic polynomial
   `(x - (a + 2b)) * (x - (a - b))^2`: the two doublet channel values are exactly
   equal. The separation functional `tr(P_w H) - tr(P_wbar H)` is identically zero
   on the family.
4. The general equivariant Hermitian is `alpha*P_1 + beta*P_w + gamma*P_wbar` with
   `alpha, beta, gamma` real, and satisfies the identity
   `H - K H K = (beta - gamma) * (P_w - P_wbar)`. Thus its K-odd component is
   `(H - K H K)/2 = ((beta - gamma)/2) * (P_w - P_wbar)`, and doublet separation
   is nonzero exactly when that component is nonzero.
5. The canonical separator `P_w - P_wbar` is Hermitian, equivariant, and K-odd,
   and separates the channels with difference two.
6. Hardening: dropping equivariance entirely, every real symmetric operator has
   exactly equal expectation values on the two conjugate doublet lines.
7. Therefore every explicitly K-real Hermitian observable on the bare carrier has
   equal expectations on the two conjugate doublet lines; in the equivariant class
   this equality is also the exact doublet eigenvalue degeneracy of item 3.
8. **Scope.** This is not an observable nonderivability claim. The mechanism note's
   `A_odd = i(C-C^2)` is a doublet resolver and calls its unlabeled spectral PVM
   derivable and registrable; on the delivered carrier
   `A_odd = -sqrt(3) * (P_w - P_wbar)` exactly. Its R2 reading concerns initial data
   and is not consumed as an observable restriction here.

**Physics reading (bounded).** The delivered carrier polarizes into a K-fixed
singlet channel and one K-paired doublet orbit. An explicitly K-real Hermitian
carrier observable has one singlet channel value and one shared doublet channel
value. The classification leaves those two values completely free
(runner block B5): the map `(a, b) -> (a + 2b, a - b)` has determinant `-3`, so the
K-real family realizes every (singlet, doublet) channel-value pair exactly once, and
exact witnesses with doublet-to-singlet ratios `1`, `1/2`, and `1/4` are computed.
No physical readout bridge identifies these witness ratios with `r`; the algebra
neither forces nor derives an `r` value.

## Gated controls

- The K-odd separator `P_w - P_wbar` exists inside the equivariant Hermitian class
  and separates (channel difference two): the boundary in T4 is the explicit K-real
  class, not matrix algebra or observable derivability.
- The mechanism note's derivable/registrable PVM is generated by the same carrier
  separator up to exact normalization:
  `i(C-C^2) = -sqrt(3) * (P_w - P_wbar)`.
- The witness `P_w` (Hermitian, with nonzero K-odd part) separates the two doublet
  lines with expectations one and zero: once a K-odd carrier observable is allowed,
  separation is immediate.
- The determinant `-3` computation above: the K-real family pins no channel values
  and no ratio — the classification constrains the shape of the pattern (one
  singlet value, one doublet value), never its magnitudes.

## Negative controls

- The spectral-pairing note's failure witness `(a, b, c) = (1, i, 0)` reproduces
  exactly on the delivered carrier: `lam_2 - conj(lam_1) = sqrt(3) - i` and
  `det = 1 - i`, so the conjugation pairing fails off the entrywise-real locus.
  The pairing license is a property of real couplings, not an artifact of the
  carrier construction.

## No-Go Discipline Gate

The gate applies to T4's exact negative boundary on explicitly K-real bare-carrier
Hermitian observables.

### N1 — Alternative-route enumeration

| Route | Marker | Result |
|---|---|---|
| K-real, `C`-equivariant carrier Hermitians | ATTEMPTED | The commutant classification gives `a*I+b*(C+C^2)` and equal doublet eigenvalues (T4 items 1 through 3; runner B4 items 1 through 5). |
| K-real, non-equivariant carrier Hermitians | ATTEMPTED | Every real symmetric matrix has equal expectations on the conjugate lines (T4 item 6; runner B4 item 8). |
| Spectral functions of the K-real equivariant family | ATTEMPTED | Equal doublet eigenvalues remain equal under functional calculus; this is a corollary of the computed characteristic polynomial. |
| K-odd equivariant carrier Hermitians | ATTEMPTED | They separate: `P_w-P_wbar` is the exact boundary witness (runner B4 item 7). This route lies outside the explicitly K-real class. |
| General complex carrier Hermitians, equivariance not required | ATTEMPTED | They separate: `P_w` gives expectations one and zero (runner B4 item 9). This is a second explicit escape from the scoped class. |
| Unordered three-atom PVM registration | ATTEMPTED | It resolves the two atoms and is derivable/registrable in the mechanism note; T4 makes no PVM-availability claim. |
| Joint qubit/corner observables | ATTEMPTED | The mechanism note's jointly K-even witness `W` resolves the doublet on its larger supplied surface; T4 is only a bare-carrier statement. |

Antilinear and non-Hermitian functionals, interacting extensions, and lattice-wide
readouts are untested and outside the claim. The list is deliberately non-complete.

### N2 — Wall-independence audit

T4 has two explicit scope boundaries rather than a claim that a physical route is
closed:

| Boundary pair | Does the first imply the second? | Does the second imply the first? | Disposition |
|---|---|---|---|
| explicitly K-real / bare-carrier observable surface | no: K-reality does not exclude joint factors or permuted PVM labels | no: the bare carrier contains K-odd separators | independent and stated |

Equivariance is not a hidden third wall because item 6 drops it. R2 is not a wall
for this claim and supplies no observable restriction.

### N3 — Hidden-wall scan

The scan covers "we assume", "by construction", "as is standard", "the framework
provides", "bridge context", "background", "naturally", "obviously", "standard
QFT", "registered", and "canonical". The canonical hits either fix the stated
entrywise-conjugation presentation or describe an explicit escape. The registered
hits occur in the verbatim mechanism boundary and the preserved PVM escape; none is
imported as a readout theorem. The periodic
sector, bare-carrier surface, explicit K-real class, and corner-basis ordering are
all stated. The corner ordering is a presentation convention distinct from the
gate note's physical species-labeling convention.

### N4 — Residual matching

| Cited source | Source residual or role | Residual addressed here | Match? |
|---|---|---|---|
| spectral-pairing note | supplied abstract corner carrier | lattice delivery at the gate note's premise set | yes; T1 computes the identification without erasing the origin FLAG |
| mechanism note | observable face remains open; the unordered PVM of the K-odd generator resolves | escape boundary for the K-real carrier classification | yes; the same separator is reproduced exactly |
| gate note | kinetic, spin-statistics, holonomy, and species-label residuals | inherited bounds on the delivered parent surface | yes for T1's bounded carrier; they are not evidence for T4's algebra |

No prior no-go is used as proof of the carrier classification. The four gate-note
residuals remain visible in runner stdout. They and the supplied parent surfaces,
not R2, keep the overall claim type `bounded_theorem`.

### N5 — Rhetoric audit

The negative is at the operator/expectation resolution on the delivered
three-dimensional carrier. It covers equivariant K-real Hermitians and general
real-symmetric carrier expectations. It does not cover K-odd observables, unordered
PVM atoms, equivariant labels, joint-factor observables, antilinear or non-Hermitian
functionals, interacting surfaces, or lattice-wide readouts. It makes no physical
indistinguishability or observable-nonderivability claim.

### N6 — Partial-closure path scan

Existing partial closures are preserved rather than relabeled as new axioms:
K-odd carrier observables and the unordered PVM already resolve the doublet;
the joint witness resolves it on the larger supplied qubit/corner surface. Further
paths include classifying antilinear and non-Hermitian functionals, extending beyond
the free composed kernel, and deriving the corner surface at the mechanism-note
origin. No approved primitive supplies an observable K-reality restriction, and no
new primitive is proposed.

### N7 — Steelman

Strongest objection: "the separator `P_w - P_wbar` is not merely constructible;
the mechanism note's `i(C-C^2)` is the same operator up to `-sqrt(3)`, and that note
calls its PVM derivable and registrable. Therefore the doublet is resolvable." Granted.
That objection defeats an observable-nonderivability claim, so this note does not
make one. It leaves only the exact statement that explicitly K-real bare-carrier
Hermitian expectations are doublet-constant.

Second steelman: "the hw=1 ordering was chosen so the restriction comes out as `C`;
T1 is a presentation convention." The delivered invariant content is ordering-independent:
`U_R` permutes the
three corner states in a single 3-cycle with `+1` coefficients, and any relabeling
of a 3-cycle on three slots yields `C` or `C^T = C^2` — the same supplied triple,
since `K` exchanges the `w` and `wbar` channels.

### N8 — Cross-cycle echo

The closest prior echo is the mechanism note itself: K-real initial states give
orbit-constant ensemble weights while its K-odd observable and unordered PVM still
resolve branches. That precedent is applied here by separating K-real carrier
expectation constancy from observable availability. The spectral-pairing note also
required a separately declared extension before moving R2 to a new coupling slot;
this note makes no such slot move. The gate note's three-cycle labeling result is a
more distant symmetry-orbit echo, not evidence for the T4 negative.

## Non-claims

- No species-labeling derivation: the gate note's labeling residual is untouched.
- No value of `r` is forced, derived, or preferred. The runner's distinct channel-
  ratio witnesses are algebraic nonselection checks, not a physical `r` dictionary.
- No record/write/readout bridge, measure, weighting, or probability content.
- No claim that K-odd observables or doublet-resolving PVMs are underivable; the
  mechanism note's explicit positive examples are preserved.
- No claim that the mechanism note's surface is derived at its origin: the FLAG
  stands there; this note supplies a lattice realization at the gate note's bounded
  premise set.
- No interacting-theory claim: everything lives on the free composed kernel of the
  gate note's surface.
- No claim about antilinear or non-Hermitian readout functionals (explicitly listed
  as untested after the N1 table).

## Dependency roles and status boundary

Roles: the gate note is the parent surface (construction consumed verbatim and
recomputed exactly); the spectral-pairing note supplies the carrier specification
(R1c), the FLAG this note addresses, and the T3 pairing license; the mechanism note
supplies the explicit observable-face boundary and doublet-resolving escape quoted
above; R2 is not consumed as an observable restriction. The minimal-axioms note is
the framework foundation. Statuses of all
dependencies are set by the independent audit lane; this note asserts no dependency
status and consumes no status-dependent content.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
- [STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
- [KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md](KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md)
- [KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md](KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md)

### Non-citation context handles

`ACPHILAMBDA_C3_RESOLVENT_DETERMINANT_HOLONOMY_COUPLING_NARROW_THEOREM_NOTE_2026-07-12.md`
(real-cyclic resolvent and determinant algebra on the same corner triple) and
`ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md`
(realification transform-law context). Context orientation only; no content is
consumed from either.

## Verification

Paired runner:
[kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_2026_07_17.py](../scripts/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_2026_07_17.py).
All lattice arithmetic is exact integer (the operator, its rank, the null vectors,
the rotation restriction); all carrier algebra is exact symbolic. No floats, no
tolerances, no randomness. Blocks: A construction, B1 delivery, B2 K-polarization,
B3 pairing instantiation with negative control, B4 classification and K-gate, B5
r-neutrality guard, B6 verbatim quote gates, B7 ledger shard existence gates
(timeless, no status pins), B8 note hygiene. Cached output:
`logs/runner-cache/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_2026_07_17.txt`
ends with the current exact PASS/FAIL total printed by the runner.

**No check passes by literal stipulation.** Every equality is computed from the
constructed objects; the quote gates compare source text to this note's blockquotes
character-for-character after whitespace flattening.

**Status authority:** independent audit lane only. This note carries no
self-assigned status beyond its claim type, and citing notes should consult the
live ledger, not this text, for standing.
