# The Seed-Class Kernel Dissected: Spectrally-Constructed Weights Are Automatically Flip-Even, the Pure-Gauge Supplied Structure Is Exactly Conjugation-Symmetric, a Phased Seed's Odd Direction Is the Real Im-Trace Reweighting, and Conjugation-Odd Data of the Theta Type Live in Determinant-Phase (Mass-Side) Structures (Bounded Theorem)

**Date:** 2026-07-02
**Current premise authority (2026-07-11):** every Tier-A/admission/registry
reference below is superseded historical context. It supplies no premise and
makes no dependency ready; the scientific conditions remain conditional/open.
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite theorems plus a graded,
explicitly-named bridge candidate; not a terminal no-go and not a change to
the theta retirement record).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Historical posture (2026-07-07):** the repo then described theta as retired
under an older admission taxonomy. **Current posture (2026-07-11):** that
taxonomy has no premise authority. This note supplies conditional gauge-side
support only; the mass-side cross-sector determinant readout is an `open_gate`.
**Primary runner:**
[`scripts/theta_seed_spectral_reality_conjugation_symmetric_supplied_structure_2026_07_02.py`](../scripts/theta_seed_spectral_reality_conjugation_symmetric_supplied_structure_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_seed_spectral_reality_conjugation_symmetric_supplied_structure_2026_07_02.txt`](../logs/runner-cache/theta_seed_spectral_reality_conjugation_symmetric_supplied_structure_2026_07_02.txt)

## Question

The campaign seed lane historically localized the theta-side gauge surface to
one sentence:

```text
(ii'-seed): derive, from the axioms, that the framework's weighting seed
            class is real / flip-even.
```

Question answered here: how much of that sentence is derivable now, what
exactly would a violating (phased) seed be, and where do the data it needs
actually live?

## Answer

The kernel dissects into four exact pieces and one explicitly-graded bridge
candidate (runner 10/10; one design-time claim refuted by the computation
and replaced by the stronger true statement):

1. **The axioms supply no weighting; every current route is spectral — and
   spectral routes are automatically even (exact).** The axiom memo is
   explicit that Admissibility "does not choose a Hamiltonian or transfer
   operator, supply transition probabilities or weights" — the weighting is
   downstream construction. The framework-native constructions in the repo
   (the retained Wilson surface; the heat-kernel/Casimir candidates) build
   coefficients from spectral data, and the spectral data are **exactly
   conjugation-invariant**: `C2(p,q) = C2(q,p)` and `d(p,q) = d(q,p)`
   (exact rationals, runner A1). Hence the **spectral-reality theorem**:
   any class weight whose coefficients are a real function of `(C2, d)` is
   real and flip-even — instance-verified for three arbitrary such
   functions, with the phased seed breaking the same gates (discriminating
   contrast; runner B1-B2). Heat-kernel and Wilson coefficients verified
   real and conjugation-paired (runner A2-A3). **Conditional discharge:
   every spectrally-constructed weighting route yields an even seed.**

2. **The pure-gauge supplied structure cannot distinguish conjugate pairs
   (exact).** The retained recurrence's fusion rules are conjugation-
   symmetric — the channels of `chi_F x chi_(p,q)`, conjugated, are exactly
   the channels of `chi_Fb x chi_(q,p)` (runner C1) — and the joint
   supplied-structure profile (Casimir, dimension, fusion channels) of `R`
   equals the conjugate of `Rbar`'s profile across the window (runner C2).
   A phased seed must therefore distinguish conjugate representation pairs
   that nothing on the pure-gauge surface distinguishes: its datum is not
   pure-gauge-supplied.

3. **Refuted expectation, sharper theorem: a phased seed's odd direction is
   the real Im-trace reweighting.** The seed space splits under the
   outer flip; the phased seed's even part is the real `cos(alpha)` weight
   and its odd part equals `-2 c sin(alpha) Im(chi_F)` — a **real-valued**
   per-plaquette imaginary-trace reweighting, NOT an imaginary action (the
   design-time claim was refuted by the computation; runner D1-D2). This is
   the naive single-plaquette lattice-theta candidate direction. This note
   does not re-prove the separate flow/center-shadow conclusions from other
   campaign blocks; it only supplies the seed-kernel identification those
   conclusions would consume.

4. **Where conjugation-odd data of the needed type live (exact
   arithmetic + retired-registry match).** Determinant phases are conjugation-odd
   (`arg det conj(M) = -arg det M`; runner D3). Conjugation-asymmetric,
   orientation-correlated data are exactly the content of the
   determinant-phase structures that the retired theta registry's own
   decomposition places on the **mass side** (`arg det M` and the
   determinant-readout bridge). The gauge-side kernel thus hands off to the
   joint theta-bar assembly precisely where the retired registry routed it.

**Bridge candidate (named, graded, NOT claimed as a derivation).** The
clarified Qubit axiom states: "No possibility is privileged. Possibilities
are distinguished by the supplied algebraic structure alone." Result 2
shows a phased gauge seed distinguishes conjugate pairs that the supplied
pure-gauge structure does not distinguish. Whether this clause LICENSES
excluding phased seeds is a semantic identification for the audit lane —
the **outer-evenness bridge candidate** — and it must respect the honest
gap: the Admissibility covariance clause names PROPER rotations only
(reflections are deliberately outside the covariance group, leaving room
for downstream chirality), and the matter sector legitimately carries
conjugation-odd data (result 4). The candidate's precise shape: on the
pure-gauge seed surface, coefficient assignments beyond supplied-structure
functions introduce a distinction the axioms' no-privilege clauses do not
supply. Its adjudication is left to audit-lane semantics; the mathematics
above is exact either way.

## Source surface (named authorities)

1. **Retained character-recurrence surface**
   ([`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md),
   ledger `effective_status = retained`): the fusion rules whose
   conjugation-symmetry is verified, and the Wilson weight whose
   coefficients are checked real and paired.

2. **Axiom memo** (approved axiom node `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md); clauses
   quoted from the current landed text):

   > "No possibility is privileged. Possibilities are distinguished by the
   > supplied algebraic structure alone."

   and the Admissibility non-supply language ("... does not choose a
   Hamiltonian or transfer operator, supply transition probabilities or
   weights ..."). Used as quoted discipline; the bridge candidate is named,
   not asserted.

3. **Retired theta registry text** (docs/audit/data/premise_decision_history.json):
   the historical gauge-side/mass-side split (`theta_bar = theta_gauge +
   arg det M`) that result 4's hand-off lands on. The retired registry text
   is context only, not a proof premise.

Campaign chain context (landed PRs #4784/#4796/#4811; drafting-time in-flight PRs
#4832/#4858/#4869/#4875/#4876/#4877/#4884): flip tables, flow theorems, and
shadow structure are those blocks' objects. They are context here, not
load-bearing premises; every identity used for this note's claims is
re-earned inline. No unaudited note is consumed as a premise.

## Theorem statements (graded)

**T1 (spectral reality; exact + instance-verified).** Conjugation-invariance
of `(C2, d)` is exact; any real function of them yields a real flip-even
class weight; heat-kernel and Wilson members verified; the phased seed
breaks the gates (contrast).

**T2 (supplied-structure conjugation-symmetry; exact).** Fusion
conjugation-symmetry of the retained recurrence and equality of joint
supplied-structure profiles across conjugate pairs.

**T3 (odd-direction identification; exact, replacing a refuted design
claim).** The phased seed's odd part is the real-valued
`-2 c sin(alpha) Im chi_F` reweighting. Whether this direction is eliminated
or made moot by separate flow/center-shadow results is not proved here.

**T4 (conjugation-odd data location; exact arithmetic).** Determinant
phases are conjugation-odd; the registry's mass side is where such data are
tracked.

**Bridge candidate (graded, unadjudicated).** The outer-evenness bridge as
stated above — audit-lane semantics, not claimed.

## Checkpoint (gauge-side seed kernel)

```text
W_theta_Q_context (bounded seed-kernel decomposition reached here):
  (i-a)       defect closure (block 3; unchanged);
  (i-b''-a')  global-sheet proof sliver (block 7; unchanged);
  (i-b''-b)   sector-level closed-surface statement (block 6; unchanged);
  (ii'-seed)  DISSECTED:
     - spectral routes: even automatically (T1) — covers every current
       framework-native weighting construction;
     - phased single-plaquette seeds: their odd direction is the real
       Im-trace reweighting (T3); flow/source conclusions require the
       separate flow/shadow blocks;
     - the datum a genuine theta seed needs is conjugation-odd,
       orientation-correlated — pure-gauge-unsupplied (T2), living in
       determinant-phase structures (T4) = the historical registry's MASS side;
     - residual: the outer-evenness bridge candidate (audit semantics) OR
       equivalently the statement that the framework's eventual weighting
       derivation lies in the spectral/single-plaquette-seeded + glued
       pattern — one sentence, now narrowed by this seed-kernel result.

W_theta_bar_assembly: the hand-off target — the joint gauge/mass assembly
(landed bridge), where the mass-side determinant-phase content lives.
```

## Identification checkpoint (what objects these are)

The "seed surface" is the class-weight construction space of the gluing
calculus; no claim is made that the framework action is derived (the axioms
supply no weighting — that absence is itself the quoted discipline), that
records register any object here, or that the bridge candidate is settled.
The mass-side hand-off is a routing statement matching the registry's own
decomposition — no mass-side derivation is claimed or consumed (the
determinant-readout content remains its own historically tracked class).

## Relation to the RP-half no-go and the no-forcing row (route independence)

No reflection positivity appears here. The no-forcing sharpening source
(reality/positivity/CPT do not force theta = 0 among theories) is untouched
and consistent: nothing here forces theta = 0 in general theory space; the
theorems bound the spectral and pure-gauge supplied-structure routes to a
phased/odd seed, and name exactly what additional data such a seed would
need.

## What moves

| Prior state | After this note |
|---|---|
| (ii'-seed) — one sentence, underived in this historical support surface | dissected: spectral routes automatically even (exact); phased single-plaquette seed direction identified as real Im-trace reweighting; needed conjugation-odd datum located on the mass side (exact arithmetic + retired-registry match); residual = one named bridge candidate |
| "what would a phased seed even be" | answered exactly: its odd direction is the real Im-trace reweighting, not an imaginary action (design claim refuted, documented) |
| supplied-structure status of conjugate pairs | exact: fusion + spectral profiles are conjugation-symmetric — the pure-gauge surface cannot distinguish them |
| the historical theta-side gauge seed surface | seed-kernel mathematics derived; what remains here is an audit-level semantic adjudication (the outer-evenness bridge), the construction-pattern statement, and the separate flow/shadow/sliver inputs |

## What remains

```text
(i-a), (i-b''-a'), (i-b''-b): unchanged supporting slivers;
(ii'-seed residual): the outer-evenness bridge candidate — an audit-lane
    semantic adjudication of the no-privilege clauses against phased
    coefficient assignments — or the equivalent statement that the
    framework's weighting derivation lies in the spectral pattern;
mass side / assembly: the registry's own other half, where the
    conjugation-odd content lives (not this campaign's lane).
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- that the outer-evenness bridge is established (it is a named candidate
  for audit-lane semantics);
- that the framework action/weighting is derived, or that the axioms force
  a weighting class;
- that theta = 0 is forced in general theory space (the no-forcing row
  stands);
- any mass-side derivation (the determinant-phase content is routed, not
  derived — it remains the retired registry's historically tracked mass-side content);
- that records register any object here;
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**Gate result:** bounded scoping inside positive constructions. The
negative content: (a) phased seeds are not spectral-constructible (exact:
spectral data are conjugation-invariant); (b) the pure-gauge supplied
structure does not distinguish conjugate pairs (exact). Flow/source
exclusion for single-plaquette phases is left to the separate flow/shadow
blocks and is not claimed here.

### N1 — Alternative-route enumeration

| Route to a phased/odd gauge seed | Standing here |
|---|---|
| spectral construction (C2, d functions) | EXCLUDED for oddness (T1: automatically even) — covers all current framework-native routes |
| pure-gauge supplied-structure data | EXCLUDED (T2: conjugation-symmetric profiles) |
| single-plaquette phased seed as continuous-theta source | NOT DECIDED HERE; T3 identifies the real Im-trace seed direction, while flow/source exclusion requires the separate flow/shadow blocks |
| matter-sector conjugation-odd coupling | THE NAMED CHANNEL (T4): determinant phases — the registry's mass side; not this lane |
| direct multi-plaquette anisotropic weighting supply | would need its own framework derivation — no candidate route exists in the repo's current construction pattern (named, not foreclosed) |
| operational primitive registration | APPROVED-PRIMITIVE PROPOSAL, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

Nothing here binds the mass side or the assembly wall beyond routing to
them. The bridge candidate is explicitly unadjudicated; both adjudication
outcomes leave the mathematics intact. The no-forcing row and the RP-half
no-go are untouched.

### N3 — Hidden-wall scan

The spectral-reality theorem's hypothesis (coefficients = real functions of
conjugation-invariant data) is explicit and instance-verified with a
discriminating phased contrast. The refuted design claim (odd part as
imaginary action) and its correction are documented in the runner. The
proper-rotation gap is stated, not papered over. The bridge candidate is
labeled as semantics for the audit lane, not smuggled as a theorem.

### N4 — Residual matching

The (ii'-seed) kernel is dissected; the registry's gauge/mass split is
matched exactly (T4 routes the odd data where the registry already tracks
them); the landed no-forcing row and the conditional-reality lane are
respected and referenced without consumption.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The bridge candidate is graded;
the multi-plaquette-supply route is named as lacking a current candidate,
not foreclosed; the mass side is routed to, not claimed.

### N6 — Partial-closure path scan

Live paths: adjudicate the outer-evenness bridge (audit-lane semantics on
the no-privilege clauses); derive the framework weighting itself (the
bridge-gap lane's standing program — any spectral outcome inherits evenness
by T1); the mass-side determinant-phase lane and the joint assembly;
(i-a), (i-b''-a'), (i-b''-b).

### N7 — Steelman

A hostile reviewer can press: (1) "The spectral-reality theorem is a
tautology — real functions give real weights." The content is the exact
conjugation-INVARIANCE of the spectral data (so real functions of them are
automatically CONJUGATION-paired, which is the nontrivial half) plus the
verified coverage of every current framework route. (2) "The bridge
candidate is doing the real work and it is unproven." Correct and stated —
it is named for the audit lane; the note's exact content stands without
it, and the equivalent construction-pattern statement is available. (3)
"Routing the odd data to the mass side just moves the historical residual."
Yes — to exactly where the retired registry already put it: this seed-kernel
result shows the relevant conjugation-odd datum is mass-side content. The
other historical theta-side components remain governed by their own lanes.
All three absorbed into scope.

### N8 — Cross-cycle echo

Cumulative guards plus this block's additions: do not claim
the odd seed direction is an imaginary action (it is the real Im-trace
reweighting — refuted-claim guard); do not treat the outer-evenness bridge
as established; and route conjugation-odd content to the mass side rather
than re-hunting it on the pure-gauge surface. Future cycles citing this
chain must supply (i-a), (i-b''-a'), (i-b''-b), and the bridge adjudication
(or the construction-pattern statement), plus any separate flow/shadow
input they need, explicitly.

## Verification

Run:

```bash
python3 scripts/theta_seed_spectral_reality_conjugation_symmetric_supplied_structure_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=10 FAIL=0
```

Sections: A conjugation-invariant spectral data (exact rationals; HK and
Wilson coefficients real and paired); B the spectral-reality theorem
(three arbitrary real spectral functions flip-even; phased contrast breaks
the gate); C supplied-structure conjugation-symmetry (fusion channel map;
joint profiles); D seed-space splitting (even/odd decomposition; the odd
direction identified as the real Im-trace reweighting;
determinant phases conjugation-odd).
