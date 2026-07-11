# Multi-Plaquette Character Gluing Derives the Emergent Integer Sector-Record Context Exactly on the Finite 2D U(1) Surface — Branch-Datum-Free, With the Theta Pairing Coming From the Action Slot — and Sharpens the Remaining Theta Q-Context Wall to Action-Level Pairing Selection on the Physical 4D SU(3) Surface (Bounded Theorem)

**Date:** 2026-07-02
**Claim type:** bounded_theorem
**Scope:** exact finite witness-surface constructions plus wall-sharpening; not
a terminal no-go and not a discharge of the theta open problem.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit premise registries, register primitives, change axioms, or
claim Strong-CP closure.
**Primary runner:**
[`scripts/gauge_multiplaquette_character_gluing_emergent_integer_sector_2026_07_02.py`](../scripts/gauge_multiplaquette_character_gluing_emergent_integer_sector_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/gauge_multiplaquette_character_gluing_emergent_integer_sector_2026_07_02.txt`](../logs/runner-cache/gauge_multiplaquette_character_gluing_emergent_integer_sector_2026_07_02.txt)

## Question

The gauge side of the theta open problem needs an emergent integer sector
label. The campaign theta sector Born-measure bridge states the wall as

```text
W_theta_Q_context:
  derive or supply an emergent integer Q as a physical sharp sector-record
  context, with nonzero odd-sector support on the relevant surface.
```

The companion center-grading context says that on the per-plaquette character
surface no additive sector label can be `Z`-valued (and none can carry the
`SU(3)` parity), localizing the wall onto the
multi-plaquette / large-gauge-winding account named by the current route map.
The landed substrate no-winding-carrier note (2026-06-11, unaudited; not
consumed as a premise here) had already relocated the gauge side to an
emergent integer sector functional, and recorded that the geometric
per-plaquette charge consumes a supplied log-branch choice — a readout-context
input the Record axiom does not supply.

Question answered here: on the multi-plaquette account itself, does character
gluing derive an emergent integer sector-record context — and if so, exactly
which part of `W_theta_Q_context` is still missing for the physical surface?

## Answer

Three exact finite results and a sharpening:

1. **The gluing mechanism derives label matching.** Integrating a shared link
   (Haar orthogonality) multiplies dual coefficients and forces the dual
   labels of the two glued plaquettes to match. On finite closed 2D tori the
   full link-constraint system forces a single matched label — derived here by
   explicit enumeration of the constraint solutions, not assumed.

2. **On the finite 2D `U(1)` surface the emergent integer context is exact
   and branch-datum-free.** The matched dual label is an integer `n in Z`
   (flux form), the sector weights are strictly positive on every sector with
   odd support and conjugation pairing, and in the branch-summed
   (heat-kernel) weight class the winding decomposition
   `Z(theta) = sum_Q e^{i theta Q} Z_Q` is exact with `Q = sum_p k_p` an
   integer that consumes **no branch choice**: the branch integers are summed
   dual variables, and the total is invariant under refundamentalizing any
   link chart. The theta pairing `e^{i theta Q}` is **derived from the action
   slot** (theta enters as the dual-label shift), not supplied.

3. **The same gluing on `SU(2)`/`SU(3)` yields matched sector labels too** —
   the label is the dominant weight, every sector weight is positive and
   conjugation-paired — and `Z`-valued conjugation-odd label functions exist
   post-gluing (e.g. `p - q`) **and are non-unique**.

**Sharpening.** Point 3 shows the missing content of `W_theta_Q_context` on
the physical `4D SU(3)` surface is **not** integer-label existence, sharpness,
odd support, positivity, or pairing mechanics — all of those are cheap or
derivable post-gluing, and non-uniquely so. The load-bearing residual is the
**action-level pairing selection**: deriving that the physical multi-plaquette
action class supplies a theta slot that weights sectors by `e^{i theta Q}`
for one specific label — the step that on the 2D `U(1)` witness surface is
done by the branch-summed action slot, and that for the physical surface
lives exactly in the multi-plaquette / large-gauge-winding account named by
the Tier-A registry.

## Source surface (named authorities)

1. **Record axiom** (approved axiom node `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)), quoted:

   > "When present, a record locks exactly one admissible local possibility. A
   > site never carries more than one record; records are permanent. Only
   > records are readable. A readout value is determined by record content
   > alone. For any finite collection of pairwise-disjoint records, scalar
   > readout `I` is additive, with `I(empty)=0`."

2. **Retained `SU(3)` character surface**
   ([`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md),
   current retained source): supplies the `SU(3)` Wilson weight
   `exp((beta/3) Re Tr W)` and character basis used for the nonabelian
   contrast (Section F of the runner).

3. **Historical theta decision text** (`docs/audit/data/premise_decision_history.json`,
   gauge side, quoted as provenance only):

   > "(a) gauge side -- theta_gauge = 0 in the topological-sector weighting,
   > residual localized to the multi-plaquette / large-gauge-winding account
   > (within the supplied per-plaquette class the local cross-plane F Ftilde
   > slot is derived-absent; ...)"

All `U(1)`/`SU(2)` representation-theory identities are earned inline by the
runner at quadrature-exact resolution (Fourier coefficients, shared-link
gluing, Schur orthogonality, `S^3`-quadrature gluing identity). No external
comparator, measured value, fitted number, or randomness enters anywhere.
The heat-kernel member used for the winding form is defined inline by its
positive Gaussian dual coefficients; its wrapped-Gaussian position form is a
Poisson identity checked by quadrature. (The Poisson form of this weight has
a standard literature name; nothing here depends on that naming.)

## Setup

Finite closed oriented 2D lattice surfaces (`L_x x L_y` tori). Plaquette
weights are members of the positive 2pi-periodic class-weight family
`w(theta) = sum_n c_n e^{i n theta}` with `c_n > 0`, `c_n = c_(-n)` — the
Wilson member has `c_n(beta) = I_n(beta)` and the heat-kernel member has
Gaussian `c_n`; both are runner-verified. Each link borders exactly two
plaquettes with opposite orientation (the incidence matrix has exactly one
`+1` and one `-1` per link column — runner-verified). This two-sided incidence
is the 2D-specific structure: in three and four dimensions a link borders
`2(d-1)` plaquettes and the dual becomes intertwiner-valued (the recoupling
wall recorded by the landed beta-6 tensor-network note, 2026-06-04, unaudited;
referenced for orientation, not consumed).

## Theorem 1 (gluing derives label matching)

1. **Shared link.** For two plaquettes glued along one link,

   ```text
   int dV w(A + V) w(B - V) = sum_n c_n^2 e^{i n (A + B)}
   ```

   (runner B1, quadrature-exact at three angle pairs): the coefficients
   multiply on the matched label; cross-labels vanish by orthogonality.

2. **Closed torus.** Writing each plaquette weight in dual form and
   integrating every link, the surviving dual assignments `{n_p}` are exactly
   the solutions of the incidence constraint system. On the `2x2` and `2x3`
   tori the runner **enumerates** all assignments in a window and finds
   exactly the fully matched ones (`n_p` identical on every plaquette; 7 of 7
   in the tested window each) — matching is a derived consequence of the
   constraint structure, not an ansatz.

3. **Partition function.** The constrained enumeration reproduces

   ```text
   Z = sum_n c_n^V        (2x2 Wilson member at beta = 2: Z = 40.261474)
   ```

   to machine precision (runner B5).

So on a finite closed 2D surface the multi-plaquette gluing *produces* a
single sharp matched dual label — the emergent sector label of the glued
surface.

## Theorem 2 (the exact integer sector-record context on the 2D U(1) surface)

**Flux form.** The matched label is an integer `n in Z`. The sector family
`{P_n}` (dual-label projectors) is sharp and countable, with every finite
truncation a finite sharp context; conjugation maps `n <-> -n`. The closed-
surface sector weights `Z_n = c_n^V / sum_m c_m^V` satisfy (runner C1-C3,
Wilson member):

```text
Z_n > 0 for every n;   Z_n = Z_(-n);   odd support;
beta = 6, V = 4:  Z_0 = 0.339725, Z_1 = 0.235392, Z_2 = 0.079665;
beta = 1, V = 4:  Z_0 = 0.926203, Z_1 = 0.036776, Z_2 = 0.000122;
truncation drift (|n| <= 30 vs 60): 0 at double precision;  tail mass at
|n| > 10 (beta 6, V 4): 2.4e-16 (explicit tail bound).
```

**Record registration (interface match, bounded).** Each finite truncation is
a finite family of mutually exclusive alternatives summing to the identity —
the shape the Record axiom registers (lock exactly one admissible alternative,
records are permanent, and readout is determined by record content); the
matched label's stability is exactly the superselection behavior of the glued
surface. Record occurrence is not
derived and not claimed; the decomposition is derived here, not supplied by
Record.

**Winding form and the branch-datum discharge.** In the branch-summed
(heat-kernel) member, the plaquette variable enters as a real angle summed
over `2 pi` shifts with shift integers `k_p` — dual summation variables, not
choices. On the closed surface:

- `sum_p theta_p = 0` identically (each link appears once with each sign;
  runner D4), so

  ```text
  Q = (1/2pi) sum_p (theta_p + 2 pi k_p) = sum_p k_p in Z    exactly;
  ```

- refundamentalizing any single link chart adds that link's incidence column
  to `{k_p}`; every column sums to zero, so the **total `Q` is
  chart-invariant** (runner D5). Regional sub-sums `Q_A` are chart-covariant:
  an interior-link shift leaves `Q_A` fixed, a boundary-link shift moves
  `Q_A -> Q_A +- 1` with the complementary region compensating exactly —
  the regional integer is defined relative to a boundary chart, the closed-
  surface total absolutely. For any fixed chart the regional integers sum to
  the invariant total: plaquette-sum additivity in exactly the Record
  additivity shape.

- the winding decomposition is exact with strictly positive paired weights
  and odd support (runner D2-D3):

  ```text
  Z(theta) = sum_Q e^{i theta Q} Z_Q,
  Z_Q > 0, Z_Q = Z_(-Q);
  heat-kernel member at bt = 2, V = 16:
  Z_0 = 0.886227, Z_1 = 0.075156, Z_2 = 0.000046;
  ```

  and the flux and winding forms are the same partition function (Poisson
  equality, machine precision across the tested `(bt, V, theta)` grid).

This discharges, **on this surface and in this weight class**, the supplied-
branch objection recorded by the landed no-winding-carrier note for the
geometric per-plaquette functional: here no log-branch is chosen anywhere —
the integers are summed, and the total sector label is chart-invariant. The
Wilson-class geometric insertion remains exactly as that note recorded it
(branch-consuming); no equivalence between the two insertions is claimed.

## Theorem 3 (the theta pairing is action-derived on this surface)

Inserting theta in the branch-summed action slot multiplies each shift term
by `e^{i (theta/2pi)(theta_p + 2 pi k_p)}`. The runner verifies (D1) that the
resulting dual coefficients are the label-shifted Gaussian profile — i.e.

```text
theta enters as the dual-label shift  n -> n - theta/2pi,
```

equivalently, after Poisson resummation, as the pointwise sector weighting
`e^{i theta Q}`. On this surface the pairing between theta and the emergent
integer is therefore **derived from the action slot**, not supplied as an
interface input. The pointwise selector arithmetic then runs end-to-end on
the derived context (runner E1): at `theta = pi` every odd winding sector
carries negative weight while at `theta = 0` all sector weights are
nonnegative — the interface the campaign theta chain consumes, populated
here entirely by derivation.

## Theorem 4 (nonabelian matched labels and the non-uniqueness fact)

The same gluing runs on `SU(2)`/`SU(3)` (runner F1-F4): the gluing identity
`int dV chi_a(A V) chi_b(V^dag B) = delta_ab chi_a(A B) / d_a` is quadrature-
verified for `SU(2)`; character orthogonality likewise; the one-cell torus
decomposition `Z = sum_j c_j / d_j` has every matched-label sector weight
positive (`beta = 6`: `Z = 56.032398`); and the `SU(3)` Wilson dual
coefficients at `beta = 6` are positive and conjugation-paired on the tested
labels (`c_(0,0) = 3.44144`, `c_(1,0) = c_(0,1) = 4.36235`,
`c_(1,1) = 4.46726`, `c_(2,0) = c_(0,2) = 2.80743`).

On the glued surface the matched `SU(3)` label is the dominant-weight pair
`(p, q)`. `Z`-valued conjugation-odd functions of it exist — `Q = p - q` is
one — with positive odd-label support, and they are **non-unique**
(`(p - q)^3` is another, differing already at `(2,0)`; runner F5). The
companion obstruction (PR #4784) is not contradicted: that theorem binds
fusion-additive labels under same-plaquette source stacking; the glued-
surface composition law is **matching**, and under matching the label
constraint disappears. What matching does *not* supply is any distinguished
`Z`-valued function or any theta slot pairing with it: in the supplied 2D
class-function weight class there is no shift-sum index for `SU(N)` — the
plaquette weight is a single-valued class function with no branch structure —
so no analogue of Theorem 3's action-derived pairing exists on this surface.
(Nothing here contradicts the registry-tracked per-plaquette cross-plane
absence result: the 2D `U(1)` theta slot is a single-plane flux object; the
`4D` topological density is cross-plane and outside this note entirely.)

## Corollary (what W_theta_Q_context still needs — sharpened)

On the witness surface every element of the wall's stated interface is
derived: sharp integer sectors, conjugation pairing, strictly positive
weights with odd support, Record-shape additivity of the closed-surface
total, and the `e^{i theta Q}` pairing from the action slot. What does not
transfer by this note to the physical `4D SU(3)` surface is exactly two
things:

```text
(i)  the carrier: a derived multi-plaquette structure on the 4D SU(3)
     surface playing the role the branch-summed abelian slot plays in 2D
     (a shift-sum / abelianized index in the glued effective weight — the
     large-gauge-winding account of the registry text);
(ii) the pairing selection: that the physical action class weights sectors
     by e^{i theta Q} for THE label carried by (i) — Theorem 4 shows label
     existence alone is cheap and non-unique, so (ii), not label existence,
     is the load-bearing residual.
```

This narrows `W_theta_Q_context` without discharging it: the unknown is no
longer "can a finite lattice surface carry a sharp integer sector-record
context with odd support at all" (it can, exactly, and branch-datum-free) but
"derive the 4D carrier and its action-level pairing." Live paths: the glued
effective-weight shift-sum route; center-dual / abelianized multi-plaquette
structures; the scaling-limit sector functional route; and the pairing-
selection question posed directly on candidate labels.

## Identification checkpoint (what objects these are)

The 2D `U(1)` torus is a witness surface: it is not the physical gauge
sector, and no claim is made that its flux or winding label is the physical
theta `Q`. The flux label `n` and the winding total `Q` are Fourier-conjugate
descriptions of the same partition function; which (if either) a physical
record registers is not claimed — both are exhibited as derived sharp
contexts with the stated properties. The `SU(3)` matched label `(p, q)` is
the glued surface's superselection label, not a topological charge; the
non-uniqueness of `Z`-valued functions on it is precisely why no
identification is asserted. The headline is a theory of the glued-surface
sector contexts and of what the theta pairing requires — not a registration
of the physical theta angle's `Q`.

## Relation to the RP-half no-go (route independence)

The retained no-go row
strong_cp_rp_half_cannot_forbid_cp_odd_imaginary_no_go_note_2026-05-16
forecloses only the route "the RP half-square identity alone derives a
no-bare-theta-slot exclusion." No reflection-positivity identity is used
here, nothing forbids a CP-odd term, and no bare-theta-slot exclusion is
asserted; the theta-slot content here is constructive (where the slot acts in
the branch-summed class), the opposite direction from the foreclosed one.

## What moves

| Prior state | After this note |
|---|---|
| multi-plaquette / large-gauge-winding account = named unknown | mechanism exhibited exactly: gluing derives matched labels; on the abelian member the matched label is `Z`-valued with the full interface |
| geometric integer functional consumes a supplied log-branch (landed note's record) | branch-summed class: integers are summed dual variables; closed-surface total chart-invariant — no branch datum in this class |
| theta pairing `e^{i theta Q}` as a supplied interface input | derived from the action slot on the witness surface (label-shift form) |
| "derive an emergent integer Q" read as label-existence problem | label existence shown cheap and non-unique post-gluing; residual sharpened to carrier + action-level pairing selection on the physical surface |
| regional additivity of a winding total | exact statement: closed-surface total invariant; regional splits chart-covariant with compensating boundary shifts |

## What remains

```text
W_theta_Q_context (sharpened):
  on the physical 4D SU(3) multi-plaquette surface,
  (i)  derive the carrier (shift-sum / abelianized index of the glued
       effective weight — the large-gauge-winding account), and
  (ii) derive the action-level pairing selection: that the physical theta
       slot weights sectors by e^{i theta Q} for that carrier's label.
  The 2D U(1) construction here is the exact finite template for both.

W_theta_bar_assembly:
  unchanged; tracked outside this note by the assembly interface bridge.
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- that the 2D `U(1)` surface is the physical gauge sector, or that its flux
  or winding label is the physical theta `Q`;
- a derivation of the 4D `SU(3)` carrier or of the physical pairing
  selection (that is the sharpened residual);
- any statement about the 4D cross-plane topological density (outside scope;
  the registry-tracked per-plaquette absence result is untouched);
- equivalence of the branch-summed theta slot with the Wilson-class geometric
  insertion (the latter remains branch-consuming as the landed note records);
- that matching-derived `SU(3)` labels are topological charges, or that any
  particular `Z`-valued function of them is distinguished (non-uniqueness is
  the point);
- a continuum limit, Perron/thermal data at `beta = 6` (outside the retained
  note's scope and outside scope here), record occurrence, or measurement
  dynamics;
- any new axiom, import, primitive, or admission (the heat-kernel member is
  defined inline by positive dual coefficients and used as a witness member
  of the 2pi-periodic weight class, not adopted as the framework action).

## No-Go Discipline Gate (for the negative boundary)

This checklist supports bounded scoping inside positive constructions. The
negative content is exactly: (a) in the supplied 2D `SU(N)` class-function
weight class there is no shift-sum index and hence no analogue of the
action-derived theta pairing of Theorem 3; (b) matched-label `Z`-valued
functions are non-unique, so label existence cannot be the load-bearing
residual of `W_theta_Q_context`.

### N1 — Alternative-route enumeration

| Route to the physical sharp integer-Q context | Standing here |
|---|---|
| per-plaquette character grading | EXCLUDED in the companion obstruction context; not used as a dependency here |
| geometric per-plaquette integer functional | SUPPLIED-DATUM route as recorded by the landed no-winding note (branch choice); untouched here |
| branch-summed abelian slot on the glued 2D surface | CONSTRUCTED (Theorems 1-3): exact, branch-datum-free, pairing action-derived — witness template |
| nonabelian matched labels on glued 2D surfaces | CONSTRUCTED (Theorem 4): sharp, positive, paired — but no distinguished `Z` function and no theta slot in the supplied class |
| 4D SU(3) glued effective-weight shift-sum / abelianized index | OPEN — the sharpened carrier residual (i) |
| action-level pairing selection on a derived carrier | OPEN — the sharpened residual (ii) |
| scaling-limit sector functional | OPEN — unchanged live path |
| operational primitive registration | APPROVED-PRIMITIVE PROPOSAL, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

The constructions here bind nothing on the mass side
(`W_mass_determinant_action`) and do not touch `W_theta_bar_assembly`. The
negative boundary (a) is class-scoped (the supplied 2D class-function weight
class); it does not assert that no 4D structure can carry a slot — the
opposite: the sharpened residual (i) is exactly the derivation of such a
structure. Supplying (i)+(ii) later contradicts nothing here.

### N3 — Hidden-wall scan

"Branch-datum-free" means: no log-branch selection appears anywhere in the
construction; the only convention is the link-angle fundamental domain, and
the closed-surface total is invariant under changing it (runner D5) — the
regional boundary covariance is stated, not hidden. "Matched label" means the
enumerated solution set of the link-constraint system (runner B2/B3), not an
assumption. The heat-kernel member is an explicit positive-coefficient
member of the same 2pi-periodic weight class as Wilson, introduced inline;
no property of the framework action is inferred from it.

### N4 — Residual matching

The Tier-A registry localizes the gauge-side residual to "the multi-plaquette
/ large-gauge-winding account"; this note works ON that account and returns
its sharpened form (carrier + pairing selection). The landed no-winding-
carrier note's relocation ("emergent integer sector functional with
nonvacuous weighting") is refined consistently: nonvacuous weighting and
integer sectors are exhibited exactly on the witness surface; what its 2D
contrast check treated as the supplied branch datum is shown removable in the
branch-summed class. The companion obstruction context and this note's
Theorem 4 fit as fusion-vs-matching: no contradiction, and jointly they
explain why the wall lives on the multi-plaquette account. The campaign
bridges keep their walls explicit; this note sharpens the Q-context wall and
leaves the assembly wall untouched.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The negative statements are scoped
to the supplied 2D class-function weight class and to the non-uniqueness
fact; live paths are named; the wall is sharpened, not discharged.

### N6 — Partial-closure path scan

Live paths: derive the 4D glued effective weight's shift-sum/abelianized
index (carrier); derive pairing selection on a candidate carrier; the
scaling-limit route; center-dual/abelianized multi-plaquette structures;
record-occurrence derivation on gauge surfaces; even-N structural witnesses
(companion note). Each is a forward derivation target, none is foreclosed
here.

### N7 — Steelman

A hostile reviewer can press: (1) "2D U(1) is a toy; nothing about the
physical surface follows." Correct as to transfer — and stated; what the
witness surface supplies is an exact existence template plus the sharpening
that label existence is not the residual. The wall's stated interface, minus
the word "physical," is satisfiable on a finite lattice surface, so the
honest residual had to be restated — that restatement is the note's main
value. (2) "The branch-datum discharge just moves the
choice into the weight class." The class member is explicit and
positive-coefficient; within it there is provably no branch selection, and
the Wilson-class geometric route is left exactly as recorded — the discharge
is class-scoped and says so. (3) "Non-uniqueness of Z-valued functions on
matched labels is trivial." It is elementary — and load-bearing: it converts
the wall from an existence question to a selection question, which is a
different derivation target. All three objections are absorbed into scope.

### N8 — Cross-cycle echo

Earlier theta cycles overclaimed by sourcing theta = 0 from structures that
could not carry sectors; the companion note guards the inverse echo (fake
integer from character grading). The echo risk specific to this note is
treating the witness-surface success as physical-surface progress. The guard
is the Corollary's explicit two-item residual: any future cycle citing this
note must supply (i) the 4D carrier and (ii) the pairing selection — the
witness template substitutes for neither.

## Verification

Run:

```bash
python3 scripts/gauge_multiplaquette_character_gluing_emergent_integer_sector_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=30 FAIL=0
```

Sections: A dual coefficients (Wilson quadrature = Bessel; heat-kernel
Gaussian profile); B gluing mechanism (shared-link identity; constraint
enumeration on 2x2 and 2x3 tori; incidence column structure; Z from
constrained enumeration); C flux-form sector weights (positivity, pairing,
odd support, truncation stability, tail bound); D winding form (theta
slot as label shift; Poisson flux=winding equality; positive paired winding
weights; closed-surface angle cancellation; chart invariance of the total and
regional covariance); E selector interface arithmetic; F nonabelian contrast
(SU(2) gluing identity and orthogonality by quadrature; one-cell torus
matched-label decomposition; SU(3) beta=6 dual coefficients; non-uniqueness
of conjugation-odd Z-valued label functions).
