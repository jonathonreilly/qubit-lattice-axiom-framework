# KCPT corner-carrier lattice delivery: the gate-note hw=1 triplet realizes the supplied corner surface, and doublet-pair separation is K-gated (bounded theorem)

- **Registry id:** `kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_bounded_theorem_note_2026-07-17`
- **Date:** 2026-07-17
- **Claim type:** `bounded_theorem`
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
exactly equal; doublet separation is identically the K-odd component of the
observable. Under the mechanism note's R2 reading (derivable initial data is K-real
— a reading that note itself leaves conditional), no derivable equivariant Hermitian
observable in the named classes separates the doublet pair: the doublet enters as one
paired channel with one free dial. Nothing here forces or derives a value of that
dial; `r` in `{0, 1/2, 1}` remains a registered, sector-dependent setting.

## Purpose

The spectral-pairing note (2026-07-16) proved fixed-point-versus-2-orbit structure on
a corner triple it had to assume, and said so with a FLAG. The gate note has carried,
since 2026-05-03, a composed lattice surface whose hw=1 kernel triplet has exactly
the required shape. This note joins the two: it computes the identification exactly
(so the pairing results now live on a lattice-delivered carrier at the gate note's
declared premise set), and then asks the polarization question one level down — which
channels of the delivered carrier can K-real data distinguish? The answer (none
within the named classes, without K-odd data) is the doublet-pair analogue of the
gate note's own corner-labeling result, and it gives the paired-channel reading of
the doublet dial a computed footing.

## Supplied objects and consumed readings

Four sentences are consumed verbatim; the runner (block B6) gates each against its
source text and against the blockquotes below.

From the spectral-pairing note, the supplied carrier (R1c):

> The real cyclic `C` with `C^3 = I_3` and `C^T = C^2`, the character projectors
> `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for `chi in {1, w, conj(w)}`,
> `w = -1/2 + (sqrt(3)/2)*i`, and entrywise conjugation `K` in the canonical basis.

From the same note, the supplied-surface FLAG this note addresses:

> **FLAG — supplied surface:** this is the mechanism note's declared corner surface,
> not a derived physical carrier.

From the mechanism note, the derivability reading consumed conditionally by T4,
together with that note's own qualification:

> **R2 — K-real derivable initial data.** Derivable initial data is K-real.
> **FLAG — two-model mechanism:** the entrywise-conjugate presentations in L-K2
> satisfy the same named clauses and exchange every K-odd seed. The memo's live
> Qualification leaves the unfixed choice conditional/open.

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

### Doublet-pair separation is K-gated on the delivered carrier (T4, bounded negative)

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
   `H - K H K = (beta - gamma) * (P_w - P_wbar)`: doublet separation IS the K-odd
   component of the observable, exactly.
5. The canonical separator `P_w - P_wbar` is Hermitian, equivariant, and K-odd,
   and separates the channels with difference two.
6. Hardening: dropping equivariance entirely, every real symmetric operator has
   exactly equal expectation values on the two conjugate doublet lines.
7. Therefore, UNDER the consumed R2 reading (derivable initial data is K-real), no
   derivable Hermitian observable in the named classes — equivariant or, at the
   expectation level, general real symmetric — separates the two doublet channels.
   The doublet pair enters as one paired channel.
8. **Conditionality.** Item 7 is conditional on R2, which the mechanism note
   itself leaves conditional (two-model FLAG, quoted above). The unconditional
   content of T4 is items 1 through 6: exact linear algebra on the delivered
   carrier.

**Physics reading (bounded).** The delivered carrier polarizes into a K-fixed
singlet channel and one K-paired doublet channel. Any K-real registered pattern on
this carrier carries one singlet value and one doublet value: the doublet enters
through one dial, not two. The classification leaves that dial completely free
(runner block B5): the map `(a, b) -> (a + 2b, a - b)` has determinant `-3`, so the
K-real family realizes every (singlet, doublet) channel-value pair exactly once, and
exact witnesses with doublet-to-singlet ratios `1`, `1/2`, and `1/4` are computed.
Nothing here forces or derives a value of the dial; `r = 0`, `r = 1/2`, `r = 1`
remain distinguished settings registered per sector (guardrail G3: weights are
registered by the realized state, never delivered by the partition).

## Gated controls

- The K-odd separator `P_w - P_wbar` exists inside the equivariant Hermitian class
  and separates (channel difference two): the wall in T4 is the K-parity gate, not
  matrix algebra.
- The witness `P_w` (Hermitian, with nonzero K-odd part) separates the two doublet
  lines with expectations one and zero: once K-odd data is admitted, separation is
  immediate.
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

The gate applies to the bounded negative T4.

### N1 — Alternative-route enumeration (non-closing)

Named routes to doublet separation:

1. K-real equivariant Hermitian observables — classified (T4 items 1 through 3);
   cannot separate. Computed.
2. K-odd equivariant Hermitian observables — separate (`P_w - P_wbar`); excluded
   from the derivable class conditionally by the consumed R2 reading, not by
   algebra. Computed as a gated control.
3. Non-equivariant Hermitian observables — a general real symmetric operator still
   cannot separate the conjugate lines at the expectation level (T4 item 6,
   computed); complex Hermitian operators with K-odd part can. Same K-parity gate.
4. Antilinear or non-Hermitian readout functionals — declared untested; outside
   the named classes.
5. Spectral functions of the K-real family — cannot separate: the doublet
   eigenvalues are equal, and any function of the operator preserves that
   equality.

The enumeration names routes; it does not assert the list is complete.

### N2 — Wall-independence audit

T4 rests on two walls of different kinds, and needs both: (i) the algebraic
classification (unconditional, computed on the three-dimensional carrier,
independent of the lattice construction — the lattice enters through T1 delivery
alone); (ii) the R2 derivability reading (conditional, consumed from the mechanism
note). Neither wall substitutes for the other, and the note keeps them separate:
items 1 through 6 stand without R2; item 7 does not.

### N3 — Hidden-wall scan

Declared load-bearing premises: the four gate-note residuals inherited below; the
corner-basis ordering convention (slot `mu` carries character `-1` in direction
`mu`) — computed exact and, per the gate note's labeling clause, a convention; the
periodic-sector choice (the boundary-holonomy residual). No other premises are
consumed.

### N4 — Residual matching

The four gate-note residuals are inherited verbatim and printed as RESIDUAL lines
by the runner: the kinetic-class / P-FLUX supply line; the spin-statistics support
tier; the boundary-holonomy convention (this runner computes the periodic sector);
the species labeling convention (whose derivability negative is the gate runner's
own computation). Because of these inherited residuals and the R2 conditionality,
the claim type is `bounded_theorem`.

### N5 — Rhetoric audit

The negative is scoped: "no derivable equivariant Hermitian separates" is asserted
under the R2 reading and for the named classes. The note nowhere asserts that the
doublet channels are physically indistinguishable, that K-odd data is underivable
in every extension of the framework, or that the corner surface is underivable at
the mechanism-note origin.

### N6 — Partial-closure path scan

Live openings, each of which would move this note's boundary: derive R2 (item 7
becomes unconditional); derive the corner surface on the mechanism-note side (the
FLAG dissolves at its origin, not merely at the gate note's premise set); classify
antilinear and non-Hermitian functionals (route 4 becomes computed); extend beyond
the free composed kernel to an interacting surface.

### N7 — Steelman

Strongest objection: "the separator `P_w - P_wbar` is algebraically constructible
from the delivered data, so the doublet channels ARE distinguishable." Granted —
constructible. The claim concerns derivable initial data under R2:
constructibility of an operator is not derivability of a K-odd registered seed.
The objection is incorporated as the first gated control (the wall is K-parity,
not existence).

Second steelman: "the hw=1 ordering was chosen so the restriction comes out as `C`;
T1 is a convention." The ordering is a labeling convention (the gate note's
residual), and the delivered content is ordering-independent: `U_R` permutes the
three corner states in a single 3-cycle with `+1` coefficients, and any relabeling
of a 3-cycle on three slots yields `C` or `C^T = C^2` — the same supplied triple,
since `K` exchanges the `w` and `wbar` channels.

### N8 — Cross-cycle echo

The gate note's own labeling negative (no canonical map from the hw=1 triplet to a
labeled SM-generation 3-set is derivable from the minimal axiom baseline; labels
enter only via the labeling-convention external premise) is this mechanism one
level up: there the rotation 3-orbit blocks deriving a labeling of the triplet;
here the conjugation 2-orbit blocks splitting the doublet with K-real data.
Consistent echo of one structure, not a new wall.

## Non-claims

- No species-labeling derivation: the gate note's labeling residual is untouched.
- No value of `r` is forced, derived, or preferred. The dial stays free per sector,
  and the runner computes distinct-ratio witnesses to keep it so.
- No measure, weighting, or probability content: guardrail G3 untouched.
- No claim that the mechanism note's surface is derived at its origin: the FLAG
  stands there; this note supplies a lattice realization at the gate note's bounded
  premise set.
- No interacting-theory claim: everything lives on the free composed kernel of the
  gate note's surface.
- No claim about antilinear or non-Hermitian readout functionals (declared
  untested, route 4 of N1).

## Dependency roles and status boundary

Roles: the gate note is the parent surface (construction consumed verbatim and
recomputed exactly); the spectral-pairing note supplies the carrier specification
(R1c), the FLAG this note addresses, and the T3 pairing license; the mechanism note
supplies the R2 reading (consumed conditionally, with its own qualification
quoted); the minimal-axioms note is the framework foundation. Statuses of all
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
ends `TOTAL: PASS=99 FAIL=0`.

**No check passes by literal stipulation.** Every equality is computed from the
constructed objects; the quote gates compare source text to this note's blockquotes
character-for-character after whitespace flattening.

**Status authority:** independent audit lane only. This note carries no
self-assigned status beyond its claim type, and citing notes should consult the
live ledger, not this text, for standing.
