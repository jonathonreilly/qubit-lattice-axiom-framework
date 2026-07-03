# The Retained Character Surface Carries Exactly One Finite Additive Sector-Record Context — the Center Z_N Grading — and No Z-Valued or (for SU(3)) Parity-Valued Refinement: the Theta Q-Context Wall Localizes onto the Multi-Plaquette / Large-Gauge-Winding Account (Bounded Theorem)

**Date:** 2026-07-01
**Claim type:** bounded_theorem
**Scope:** positive finite construction plus an exact finite obstruction that
localizes a named wall; not a terminal no-go.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/gauge_center_sector_record_context_character_grading_obstruction_2026_07_01.py`](../scripts/gauge_center_sector_record_context_character_grading_obstruction_2026_07_01.py)
**Runner cache:**
[`logs/runner-cache/gauge_center_sector_record_context_character_grading_obstruction_2026_07_01.txt`](../logs/runner-cache/gauge_center_sector_record_context_character_grading_obstruction_2026_07_01.txt)

## Question

The gauge side of the Tier-A theta admission asks for an emergent integer
sector label. The in-flight theta sector Born-measure bridge (PR #4766) names
the residual wall in the form

```text
W_theta_Q_context:
  derive or supply an emergent integer Q as a physical sharp sector-record
  context, with nonzero odd-sector support on the relevant surface.
```

Question answered here: does the retained character/winding structure of the
finite Wilson surface supply a finite central integer-valued sector
decomposition `{P_Q}` that the Record axiom can register sharply, with the
label additive over disjoint regions?

## Answer

Yes and no, as an exact finite dichotomy — and both halves are theorems on the
retained surface:

- **Yes (construction).** The retained character surface carries exactly one
  nontrivial finite sharp additive central sector decomposition (up to
  relabeling of the label group): the **center grading**.
  For `SU(3)` it is the triality decomposition `{P_0, P_1, P_2}`,
  `t(p,q) = (p - q) mod 3`, diagonal in the retained character basis, with the
  retained recurrence operator `J` acting as an exact sector-shift (grading-odd)
  operator, labels additive over disjoint regions, conjugation pairing
  `k <-> -k`, and strictly positive conjugation-paired sector weights on every
  sector for an explicit witness-state family (`beta = 1, 6, 12`). This is a finite sharp sector-record context in exactly the
  interface shape the Record axiom registers: finitely many mutually exclusive
  alternatives, one locked per record, scalar readout additive over disjoint
  record collections.

- **No (obstruction).** The label of that context is valued in `Z_N`
  (`Z_3` for `SU(3)`), and this is not a truncation artifact: **every**
  fusion-additive sector label on the surface factors through the center
  grading. In particular, on the finite `SU(3)` character surface there is

  - **no nontrivial Z-valued additive sector label** (the homogeneous grading
    system has nullity `0` over `Q`), and
  - **no nontrivial parity label** — no `Z_2`-valued additive label exists
    (nullity `0` over `GF(2)`), so the CP-even pointwise selector input
    `(-1)^Q` cannot be supplied by any additive sector label of this surface.

  Therefore `W_theta_Q_context` is **not discharged** by this note; it is
  **narrowed and localized**: the emergent integer `Q` cannot be an additive
  character-sector label of the retained per-plaquette/per-region class-function
  surface. The Tier-A registry's own gauge-side decomposition already points at
  the surviving carrier, and this note gives it a theorem-grade reason:
  the residual account is the multi-plaquette / large-gauge-winding account,
  quoted below.

`SU(2)` is kept as the structural contrast: there the center grading **is** a
parity (`n mod 2`), the odd sector has strictly positive witness-state weight,
and the full pointwise-selector input interface is populated — the interface
is constructible exactly when `N` is even. No identification of the `SU(2)`
center parity with a topological-charge parity is claimed (see the
identification checkpoint below).

## Source surface (named retained authorities)

1. **Retained character-recurrence surface.**
   [`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
   (ledger `effective_status = retained`, claim scope quoted from the live
   ledger):

   > "On the finite periodic SU(3) Wilson 3+1 source surface, the marked
   > plaquette source is the explicit self-adjoint character-recurrence
   > operator J and finite plaquette expectations are represented by its
   > spectral measure in the transfer state; beta=6 Perron/thermal data are
   > outside scope."

   The retained recurrence used here, verbatim from that note:

   ```text
   chi_(1,0) chi_(p,q) = chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
   chi_(0,1) chi_(p,q) = chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q)
   ```

   (negative-label terms omitted), with
   `X = (chi_(1,0) + chi_(0,1))/6` the marked plaquette source and `J` the
   multiplication operator by `X` on the class-function space.

2. **Record axiom** (approved axiom node `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)), quoted:

   > "When present, a record locks exactly one local possibility from the
   > subset available at that site under Admissibility; records are permanent.
   > Only records are readable. A readout
   > value is determined by record content alone. For any finite collection of
   > pairwise-disjoint records, scalar readout `I` is additive, with
   > `I(empty)=0`."

   Per the axiom's non-supply clause and the Tier-A registry description,
   central-sector decompositions are downstream readout-context content: they
   must be **derived**, and this note derives one. Record contributes only the
   registration and additivity interface; no new admission is introduced.

3. **Tier-A theta registry text**
   ([`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json),
   gauge side, quoted exactly):

   > "(a) gauge side -- theta_gauge = 0 in the topological-sector weighting,
   > residual localized to the multi-plaquette / large-gauge-winding account
   > (within the supplied per-plaquette class the local cross-plane F Ftilde
   > slot is derived-absent; RP, reality, positivity, CPT, parity-measure, and
   > arrow-orientation are tracked in landed source notes as
   > non-forcing/non-sourcing route surfaces)"

Standard finite representation-theory facts used (Weyl character values at
maximal-torus points, center covariance of characters) are earned inline by
the runner at exact-identity resolution; no external comparator, measured
value, or fitted number enters anywhere.

## Definitions

Work on the retained surface: the class-function space of the marked plaquette
variable with orthonormal character basis `{chi_(p,q)}` (`SU(3)`), the
retained recurrence/fusion structure above, and the transfer state. Disjoint
regions carry independent copies whose class functions compose by tensor
product; repeated marked-plaquette source insertions compose by pointwise
multiplication (this is the retained note's own composition law: `J` is a
multiplication operator, and stacked insertions are `J`-words).

**Admissible sector label.** A pair (orthogonal sharp decomposition `{P_a}` of
the character surface with each sector spanned by a subset of the character
basis — i.e., respecting the retained surface's own spectral basis — and an
abelian-group-valued label `g` constant on each sector and separating
sectors) such that:

- (i) *multiplicative sharpness* — the product of a sector-sharp class
  function with label `a` and a sector-sharp class function with label `b` is
  sector-sharp with label `a + b` (label additivity under the surface's own
  source-composition law);
- (ii) *disjoint-region additivity* — on disjoint regions, the composite label
  is the sum of the regional labels.

**Lemma (sharpness = grading).** Condition (i) holds for basis characters iff
`g` is a grading of the fusion structure: for every channel `c` appearing in
`chi_a chi_b` with nonzero multiplicity, `g(c) = g(a) + g(b)`. (If some
channel violated it, the product of the two sharp sources would spread across
sectors with different labels and could not be registered as one locked
alternative with an additive readout.) The unit label is forced:
`chi_(0,0)` is the multiplicative unit, so `g(0,0) = 0`.

**Remark (non-diagonal decompositions).** The character-basis restriction is
where the classification lives, not where the labels hide. The natural
non-diagonal alternative — sectors given by support sets of conjugacy-class
subsets (indicator-type decompositions) — forces the trivial label outright:
a function `f` supported in a sector satisfies `supp(f^2) = supp(f)`, so
multiplicative sharpness puts `f^2` in the same sector while assigning it
label `2 g(a)`, whence `g(a) = 2 g(a) = 0` for every sector. Decompositions
neither character-diagonal nor support-type are not classified here and are
listed as an open boundary, not consumed by any claim.

This definition is the exact transcription of what the wall's own interface
asks a sector-record context to do: sharp lock, additive readout — composed
with the retained surface's own source law (class-function multiplication).

## Theorem 1 (center sector-record context on the retained surface)

On the retained `SU(3)` character surface:

1. **Center action and sharp projectors.** The center
   `Z(SU(3)) = {1, omega, omega^2}`, `omega = e^(2 pi i/3)`, acts on class
   functions by `(Delta_z f)(U) = f(zU)`. On characters this action is exactly
   diagonal:

   ```text
   chi_(p,q)(omega U) = omega^(t(p,q)) chi_(p,q)(U),   t(p,q) = (p - q) mod 3.
   ```

   The spectral projectors

   ```text
   P_k = (1/3) sum_(j=0..2) omega^(-jk) Delta_(omega^j),   k in {0, 1, 2}
   ```

   are orthogonal, idempotent, complete (`sum_k P_k = I`), and **finite in
   number** (three sectors) even though the surface is infinite-dimensional.
   The decomposition is canonical — it is the spectral resolution of the
   center-translation unitaries of the retained surface's own group variable,
   not a partition invented to fit an answer.

2. **The retained recurrence is the exact sector-shift structure.** Each
   `chi_(1,0)`-channel of the retained recurrence shifts `t` by exactly `+1`
   and each `chi_(0,1)`-channel by exactly `-1`. Hence the retained operator
   `J` is grading-odd:

   ```text
   P_k' J P_k = 0   unless k' = k +- 1 (mod 3),
   ```

   with no diagonal block, and an insertion word with `#F` fundamental and
   `#Fb` antifundamental factors shifts the sector by `(#F - #Fb) mod 3`.
   The character-recurrence surface is, sector-wise, a ladder.

3. **Additivity and conjugation pairing.** On disjoint regions the center acts
   as `Delta x Delta` and the labels add mod 3; products of sector-sharp
   functions are sector-sharp with added labels (multiplicative sharpness
   holds for `t` identically). Complex conjugation maps `chi_(p,q)` to
   `chi_(q,p)`, i.e. `k <-> -k`; the pairing `g(R) + g(Rbar) = 0` is forced
   for every admissible label because `chi_R chi_Rbar` contains the unit.

4. **Sector weights: state-independent structure plus an explicit witness
   family.** Sharpness, finiteness, disjoint-region additivity, and the
   grading-odd shift are state-independent; and for every conjugation-invariant
   state the sector weights pair, `Z_k = Z_(-k)`. As an explicit witness
   family, take the single-plaquette slice-weight vectors
   `psi_beta = e^((beta/2) X) 1` (the same within-slice half-weighting shape
   as the retained kernel's spatial factor) on the truncated dominant-weight
   cone. The weights `Z_k = ||P_k psi_beta||^2 / ||psi_beta||^2` satisfy, at
   `beta in {1, 6, 12}` (framework point `beta = 6` included):

   ```text
   Z_k > 0 for every k;   Z_1 = Z_2 exactly;   sum_k Z_k = 1;
   beta = 6: Z = (0.572386, 0.213807, 0.213807);
   ```

   truncation-stable to `< 1e-8` between cones `p + q <= 30` and
   `p + q <= 24` (observed drift `<= 1.1e-16`). The positivity mechanism is
   structural: `(chi_F + chi_Fb)^m` applied to the unit has nonnegative
   coefficients and supports every triality for `m >= 2`, so no cancellation
   can empty a sector at any `beta > 0` for any state whose character
   coefficients arise from such nonnegative expansions. These witnesses are
   not the retained note's full transfer state: the `beta = 6` Perron/thermal
   data of `T_(L_s,beta)` are outside retained scope there and remain outside
   scope here; what carries over to any conjugation-invariant state on this
   surface is the finite sharp context, the additivity, and the pairing.

5. **Record registration (interface match, bounded).** `{P_0, P_1, P_2}` is a
   finite family of mutually exclusive alternatives with `sum_k P_k = I`. That
   is exactly the shape the Record axiom registers: a record, when present,
   locks exactly one available alternative, invariant under repeated readout,
   and the scalar readout is additive over finite pairwise-disjoint record
   collections — carrying the mod-3-additive sector label over disjoint
   regions. The weights `Z_k` are nonnegative, normalized, conjugation-paired,
   and finite-sector — the interface shape the in-flight theta-sector
   Born-measure bridge (PR #4766) consumes from a supplied sharp context.
   Record occurrence (whether a record forms on this surface) is not derived
   and not claimed; the decomposition itself is derived, not supplied by
   Record.

So the retained character/winding structure **does** supply a finite central
sector-record context with an integer-mod-N label, additive over disjoint
regions, and it supplies it canonically.

## Theorem 2 (maximality and the integer-grading obstruction)

Every admissible sector label on the retained `SU(3)` character surface
factors through the center grading `t`. Concretely, with `a := g(1,0)`:

1. `chi_(1,0) chi_(0,0) = chi_(1,0)` forces `g(0,0) = 0` (unit).
2. `chi_(1,0) chi_(1,0) = chi_(2,0) + chi_(0,1)` forces
   `g(2,0) = g(0,1) = 2a`.
3. `chi_(1,0) chi_(0,1) = chi_(1,1) + chi_(0,0)` forces `0 = a + 2a`, i.e.
   **`3a = 0`**.
4. Induction along the retained recurrence graph (which is connected from the
   unit) forces `g(p,q) = (p - q) a`.

All four steps are channels of the retained recurrence quoted above.
Consequences:

- **Over `Z`:** `3a = 0` forces `a = 0`; the only `Z`-valued admissible label
  is trivial. An "emergent integer Q" in the `Z`-valued sense **cannot be an
  admissible sector label of this surface at all** — not for any truncation,
  any region size, or any relabeling. The tempting concrete candidate — the
  dominant-weight integer `p - q` — is sharp per irrep but provably not
  additive: the two `fund x fund` channels carry `p - q = 2` and `p - q = -1`;
  only its mod-3 shadow is sharp on products.
- **Over `Z_2` (the selector parity):** a nontrivial parity label solves
  `3a = 0, a != 0` in `Z_2`, which is impossible; nullity over `GF(2)` is `0`.
  So on the physical `SU(3)` surface **no additive sector label can feed the
  CP-even pointwise selector input `(-1)^Q`**.
- **Over `Z_3`:** the solution space is exactly one-dimensional and is the
  triality line — the center grading of Theorem 1, and only it.
- **`SU(2)` contrast:** the same system for the `SU(2)` recurrence
  (`chi_1 chi_n = chi_(n-1) + chi_(n+1)`) forces `2 g(1) = 0`; over `Z` only
  trivial, over `GF(2)` exactly the parity `n mod 2`. The parity interface
  exists exactly when `N` is even, and its odd sector carries strictly
  positive witness-state weight (`Z_odd(beta=6) = 0.4755`).

The runner verifies the obstruction two independent ways: symbolic replay of
the four named relations, and machine nullity computations of the full
truncated relation system over `Q`, `GF(2)`, `GF(3)` with kernel
identification.

## Corollary (wall localization for W_theta_Q_context)

On the retained finite `SU(3)` character surface, the sharp-Q context asked
for by `W_theta_Q_context` — a `Z`-valued sharp sector-record label with odd
support feeding `(-1)^Q` — cannot be constructed as an additive
character-sector label: no `Z`-valued label exists (Theorem 2), and no parity
shadow exists for `N = 3`. Within the classified scope (character-diagonal
decompositions; support-type decompositions force the trivial label), the
center context of Theorem 1 is the whole of the additive sector-record
content of this surface, and its label is natively `Z_3`-valued — it is not
the truncation of any integer charge.

Therefore the emergent integer `Q` must be carried by structure **beyond**
per-plaquette/per-region character grading — exactly the surviving account the
Tier-A registry already names: "residual localized to the multi-plaquette /
large-gauge-winding account." This note upgrades that localization from a
bookkeeping split to a theorem-grade exclusion of the character-grading side.

This is route localization inside a positive construction, not a terminal
no-go: the definition of admissible label binds exactly (i) sharpness under
the surface's own multiplicative source composition and (ii) disjoint-region
additivity. Constructions that step outside the class-function fusion surface
— branch/log data of holonomies, multi-plaquette winding functionals,
scaling-limit sector functionals, emergent abelian dual surfaces (where the
dual of `U(1)` is `Z` and a `Z`-valued additive label is not obstructed) —
are untouched and are the live paths.

## Identification checkpoint (what object this is)

The constructed context is the **center / N-ality readout context** of the
retained gauge surface. It is not claimed to be the theta topological-sector
context: for `SU(3)` it provably cannot feed the theta selector's parity
input, which is the sharpest available statement that the two are distinct
objects on this surface. Likewise, the `SU(2)` center parity is an interface
witness (a finite surface where a sharp parity-with-odd-support context
exists), not an identification of center parity with topological-charge
parity. The headline of this note is a theory of the character-surface
sector-record context — not a claim that the physical theta angle's `Q` has
been registered.

## Relation to the RP-half no-go (route independence)

The retained no-go row
[`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
has live claim scope (quoted from the ledger):

> "Within the finite/compact measure-preserving involution setting of the
> retained RP half-square identity, a real Theta-anti-invariant imaginary
> addition S_CP = i c h is invisible to the symmetric reflected expectation
> for every reflection-Hermitian F; therefore that RP identity alone cannot
> derive a no-bare-theta-slot exclusion."

This note does not re-run that route: no reflection-positivity identity is
used, nothing here forbids a CP-odd action term, and no no-bare-theta-slot
exclusion is asserted. The construction concerns which sector decompositions
the character surface supplies, a disjoint question.

## What moves

| Prior state | After this note |
|---|---|
| "Does the retained character/winding structure supply a finite sharp integer-labeled sector-record context?" — open question | answered exactly: yes for the integer-mod-N center label (canonical, unique up to relabeling); provably no for a Z-valued label |
| generic hope that a per-plaquette / per-region character construction could supply the theta `Q` | excluded by an exact finite obstruction (`3a = 0`; nullities 0/0/1 over `Q`/`GF(2)`/`GF(3)`) |
| pointwise-selector parity input `(-1)^Q` on `SU(3)` | provably not suppliable by any additive character-sector label; must come from the winding account |
| sector-shift structure of the retained recurrence | made explicit: `J` is grading-odd; sector ladder with word rule `(#F - #Fb) mod 3` |
| sector weights on the retained surface | explicit, strictly positive, conjugation-paired, truncation-stable at `beta = 1, 6, 12` |

## What remains

```text
W_theta_Q_context (narrowed):
  derive the emergent integer Q as a sharp sector-record context on the
  multi-plaquette / large-gauge-winding account — beyond additive
  character-sector labels, which Theorem 2 classifies: they all factor
  through Z_N. Live paths:
  (a) multi-plaquette winding functionals whose branch/section datum is
      derived rather than supplied;
  (b) scaling-limit / effective-action sector functionals;
  (c) emergent abelian dual surfaces (U(1) dual = Z, not obstructed);
  (d) even-N subsurface interfaces as structural witnesses.

W_theta_bar_assembly:
  unchanged; tracked by the in-flight assembly interface bridge (PR #4768).
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- derivation of the emergent integer `Q` or of odd-sector support for it;
- that the center context is the theta topological-sector context;
- that the `SU(2)` center parity is instanton/topological parity;
- conservation of the center label under the marked-source dynamics (the
  retained `J` is grading-odd — it shifts sectors; the context is a readout
  decomposition on which states assign weights, and the conserved-flux
  upgrade on noncontractible/multi-plaquette surfaces is an open path, not
  claimed);
- identification of the explicit slice-weight witness vectors with the
  retained note's full transfer state (its `beta = 6` Perron/thermal data
  remain outside scope);
- record occurrence on the gauge surface;
- exclusion of sector constructions that use non-class-function data
  (branch/log/section data, multi-plaquette winding functionals);
- any continuum-limit statement; any use of measured constants, fitted
  values, or lattice-MC comparators;
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

This checklist supports bounded route localization inside a positive theorem.
The negative content is exactly: additive sector labels of the retained character
surface are `Z_N`-valued, so neither `Z`-valued `Q` nor (for `N = 3`) the
parity `(-1)^Q` can be carried by them.

### N1 — Alternative-route enumeration

| Route to a sharp integer-Q context | Standing here |
|---|---|
| additive character-sector label on the retained surface | EXCLUDED by Theorem 2 (exact finite obstruction, both symbolic and machine-verified) |
| center `Z_N` context | CONSTRUCTED (Theorem 1) — supplies the mod-N label, not `Z` |
| dominant-weight integer `p - q` as label | EXCLUDED: sharp per irrep, provably not additive (fund x fund witness) |
| multi-plaquette winding functional (branch/section datum derived) | OPEN — named live path (a) |
| scaling-limit / effective-action sector functional | OPEN — named live path (b) |
| emergent abelian dual surface (`U(1)` dual = `Z`) | OPEN — named live path (c); the obstruction vanishes in the abelian dual |
| even-N structural witness (`SU(2)` parity with odd support) | CONSTRUCTED as interface witness; no physical identification claimed |
| operational primitive registration | OWNER-GOVERNANCE ROUTE, not proposed here (standing direction is 2 -> 0) |

### N2 — Wall-independence audit

The obstruction binds only the character-grading route. It does not touch
`W_theta_bar_assembly` (mass side, anomaly bookkeeping), does not weaken the
retained character-recurrence note (it consumes it), and does not interact
with the RP-half no-go (route independence shown above). Supplying the
winding-account `Q` later would not contradict anything here: this surface's
own additive labels remain `Z_N`.

### N3 — Hidden-wall scan

"Admissible sector label" is an explicit two-condition definition transcribing
the wall's own interface (sharp lock + additive readout), stated before the
theorems and enforced in the runner; it is not a hidden strengthening. The
lemma converts condition (i) into the fusion-grading equation — the only place
where "sharp" does work — and that conversion is itself displayed. No
positivity, reality, RP, or CPT input is used anywhere.

### N4 — Residual matching

The Tier-A registry text localizes the gauge-side residual to "the
multi-plaquette / large-gauge-winding account"; this note's corollary lands on
exactly that account and nothing else. A landed but unaudited substrate
no-winding-carrier note points in the same direction, but it is
non-load-bearing context here and is not consumed as a premise. The obstruction
here stands on the retained character-recurrence surface alone: the per-region
character route is excluded by an exact finite obstruction rather than by
absence of a construction. The in-flight bridges (PRs #4766, #4768) keep
`W_theta_Q_context` and `W_theta_bar_assembly` explicit; this note narrows the
former and leaves the latter untouched.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing is used for the wall. The exclusion
is scoped to additive character-sector labels of this surface; live paths are
named. The positive theorem does not claim more than the interface it
verifies.

### N6 — Partial-closure path scan

Live paths (a)-(d) under "What remains," plus: deriving record occurrence on
gauge surfaces; upgrading the center context to the conserved-flux context on
noncontractible/multi-plaquette surfaces; and any derivation making an
abelian dual surface emergent, where the grading group is `Z` and the
construction of Theorem 1 goes through verbatim with integer labels.

### N7 — Steelman

A hostile reviewer can press three points. (1) "The obstruction only binds
your definition of admissible label." Correct — and the definition is the
wall's own interface (sharp + additive); anything weaker is not a
sector-record context in the sense the theta chain consumes, and anything
using non-class-function data is expressly left open. (2) "The center context
is not conserved by the source dynamics, so calling it a sector context
oversells." The note states grading-oddness explicitly and claims only the
readout-decomposition interface (sharpness, weights, additivity), which is
what the wall's consumer bridge requires; the conserved-flux upgrade is
declared open. (3) "The `SU(2)` parity witness invites the realist slip of
identifying center parity with instanton parity." The identification
checkpoint refuses that identification explicitly; the witness only shows the
interface is constructible at even `N`. All three objections are absorbed
into scope rather than contradicted.

### N8 — Cross-cycle echo

Earlier theta cycles repeatedly tried to source `theta = 0` from surface
properties that could not carry the sector structure (reality, positivity,
CPT, parity-measure — all tracked in the registry as non-forcing). The echo
risk here is the inverse: sourcing a fake `Q` from a structure that cannot
carry integers. The obstruction theorem is the guard against that echo: it
proves the character surface's additive content is `Z_N` and nothing more, so
no future cycle should retry integer-`Q`-from-character-grading in any
disguise (relabeled irrep integers, truncation-dependent lifts, per-region
integer sums). The `fund x fund` non-additivity witness is the canonical
counterexample to keep.

## Verification

Run:

```bash
python3 scripts/gauge_center_sector_record_context_character_grading_obstruction_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=56 FAIL=0
```

Sections: A center-action diagonality (Weyl-exact); B retained recurrence
verified at Weyl level + grading shift + projector algebra + word rule;
C transfer-vector sector weights (positive, paired, truncation-stable;
`beta = 1, 6, 12`) and the nonnegativity/coverage structure; D the grading
obstruction (nullities over `Q`/`GF(2)`/`GF(3)`, kernel = triality line,
hand-relation replay, fund x fund witness); E record-interface arithmetic
(disjoint-region additivity, sector-sharp products, weight shape); F
source-note discipline (canonical metadata, graph links, fail-closed hygiene).
