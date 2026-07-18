---
claim_id: microcausality_finite_range_plaquette_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional extension of the family walk-expansion chain to the finite-range term class on Z^3 (axioms supply no dynamics; the term family, the Hermitian terms, the finite region, and the finite site dimensions are supplied objects; same Heisenberg convention and declared finite-matrix ODE context as the siblings), under the standing scoping hypothesis X ∩ Y = ∅ (d ≥ 1; tensor class, so the clean form holds): (P1) the supplied class — H = Σ_{S∈𝒮} h_S with 𝒮 contained in {nearest-neighbor bonds} ∪ {unit faces}, each h_S Hermitian on its tensor factors, ||h_S|| ≤ J, sites carrying ARBITRARY finite dimensions (dimension-blindness gated on mixed-dimension bond AND face instances), the family set-indexed with at most one term per support (same-support terms summed into one h_S; no single-site subsumption is claimed — electric link terms in the gauge remark are bond terms on their own geometric bonds); (P2) the exact term-adjacency geometry, natively re-enumerated and box-stable: 6 bonds and 12 faces per site (n_X^𝒮 ≤ 18|X|), degrees bond→30, face→52, D = 52, diameters 1 and 2; (P3) the dilated reach lemma — a length-k mixed walk reaches at most distance 2k, exactly attained at k = 1, 2, 3, so the series starts at k ≥ ⌈d/2⌉ and one face step genuinely jumps distance 2 (sharpness exhibit gated); (P4) the chain carry-over — every locality step is tensor-factor disjointness exactly as in the qubit siblings, so the Duhamel walk expansion applies with the term-adjacency graph replacing the bond graph, per-step degree ≤ 52, coefficient identity (2J)^k n 52^(k−1) = (n/52)(104J)^k gated; (P5) the theorem: ||[τ_t(A), B]|| ≤ 2||A||||B||(n_X^𝒮/52) Σ_{k≥⌈d/2⌉} (104J|t|)^k/k!, all t, volume-uniform, μ-reweighted exponential tail inherited, activity scale 104J and readout v ≤ 208eJ (cone dilation factor 2 is real), NEITHER claimed sharp; (P6) the gauge-shaped coverage remark, gated at a Z_2 instance: assigning each link's Hilbert space to one endpoint makes Kogut-Susskind-form magnetic plaquette terms face-supported and electric link terms bond-supported, so KS-form Hamiltonians with DYNAMICAL finite-dimensional links lie in the class — while the CT note's U-integrated item (gauge measure, transfer kernel, gauge-field correlation control, continuous groups) is NOT touched and remains open. Longer-range terms (diameter > 2) are outside the class, named."
upstream_dependencies:
  - minimal_axioms
  - microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
  - microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - gauged_log_transfer_quasilocality_combes_thomas_narrow_theorem_note_2026-06-13
runner: scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py
---

# Microcausality: Finite-Range Plaquette-Class Walk-Expansion Lieb-Robinson Bound

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; supplied finite-range class (bonds and
unit faces, arbitrary finite site dimensions); the axioms supply no
dynamics; same conventions and declared ODE context as the siblings.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py`](../scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.txt`](../logs/runner-cache/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.txt)

## Purpose

The cited gauged quasilocality note
[`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md)
names its dynamical case open: "The `U`-integrated / dynamical
gauge-measure case — the fixed-`U` resolvent bound does not control
gauge-field correlations; **open**." That item has a Hamiltonian-level
many-body prerequisite the family can now supply: a Lieb-Robinson
bound for a term class wide enough to contain gauge-shaped
Hamiltonians whose links are **dynamical quantum degrees of freedom**
— which requires plaquette (four-site) terms and arbitrary finite
local dimensions, neither of which the qubit siblings' bond class
covers. This note supplies exactly that: the walk-expansion chain of
[`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
carries over verbatim — every locality input is tensor-factor
disjointness, exactly as in the qubit case — with the bond-adjacency
graph replaced by the term-adjacency graph of bonds and unit faces,
whose exact local geometry is enumerated and gated here. What this
note does **not** touch, stated plainly: the gauge measure, the
transfer kernel, gauge-field correlation control, and
continuous/compact link groups — the `U`-integrated item itself
remains open exactly as the CT note states it.

## Hypotheses (all supplied, none derived)

A finite region `Λ ⊂ Z^3`; each site `x` carries a supplied Hilbert
space of **arbitrary finite dimension** `q_x ≥ 1`; a supplied term
family `𝒮 ⊆ {nearest-neighbor bonds} ∪ {unit faces}` over `Λ` and a
supplied Hamiltonian `H = Σ_{S∈𝒮} h_S`, each `h_S` Hermitian on the
tensor factors of `S`, `J = max_S ||h_S||` (`𝒮` assumed nonempty; at
`𝒮 = ∅` set `J = 0`, `H = 0`, and every statement is trivial).
The family is set-indexed: at most one term per support, and if a
supplied Hamiltonian presents several terms with the same support,
their **sum** is the single `h_S` (with `J` the maximum of the summed
norms) — no relabeling across distinct supports is used anywhere. In
particular no blanket single-site subsumption is claimed: a genuinely
single-site term is simply outside the stated family (the gauge
application below needs none — electric link terms are bond terms on
their own geometric bonds). Observables `A`, `B` on disjoint supports `X`, `Y`
(`d = d(X, Y) ≥ 1` as the standing scoping hypothesis; this is a
tensor-product class, so `[A, B] = 0` holds and the clean form is
claimed — no CAR grading is involved anywhere in this note).
Heisenberg convention and the declared finite-matrix ODE context of
the sibling chain, unchanged, including directed time with the
`H → −H` extension (the class is invariant with the same `J`, terms,
and walks). The axioms supply no dynamics (needled); everything is
bridge-conditional. No literature statement is load-bearing.

## Results

**Exact term-adjacency geometry (natively enumerated, box-stable).**
Two **distinct** terms are adjacent iff their site supports intersect. On `Z^3`,
enumerated at two box radii and stable:

- bonds incident to one site: `6`; faces containing one site: `12` —
  so `n_X^𝒮 := #{S ∈ 𝒮 : S ∩ X ≠ ∅} ≤ 18·|X|`;
- from a bond: `10` adjacent bonds, `20` adjacent faces (degree `30`);
- from a face: `20` adjacent bonds, `32` adjacent faces (degree `52`);
- per-step degree bound `D = 52`; support diameters: bond `1`, face
  `2`.

A mixed length-2 walk count from a single site is `804`, below the
product bound `18·52 = 936` (both gated) — the per-step bound is not
tight, and no tightness is claimed.

**Dilated reach lemma (exact, with a sharpness exhibit).** The sites
of the `k`-th term of a walk lie within distance `2k` of `X`
(induction: each term shares a site with its predecessor and has
diameter at most `2`), and the value `2k` is exactly attained at
`k = 1, 2, 3` (enumerated). Hence a walk whose last term touches `Y`
needs `k ≥ ⌈d/2⌉`, and the series below starts there. The dilation is
real, not an artifact: one adjoint step through a face term moves
information distance `2` — gated: for the four-qubit face term
`X⊗X⊗X⊗X`, the single commutator `[H, Z_corner]` already fails to
commute with `Z` at the **opposite** corner (distance 2).

**Chain carry-over.** Every locality input of the sibling chain is
tensor-factor disjointness — the same mechanism, verbatim: the
boundary reduction `[H, O] = [H_{∂ supp O}, O]`, the self-drop, the
per-term re-derivation with the reduced generator (self term dropped
before the Jacobi step), the base-term vanishing unless the last term
touches `Y`, and the initial `[A, B] = 0`. The algebra-independent
steps (Jacobi, conjugation, directed-time norm transport with the
`H → −H` extension, iterated integrals, factorial tail, μ-reweighting,
vanishing remainder) are cited to the sibling where they are natively
gated. The walk now lives on the term-adjacency graph: first term at
most `n_X^𝒮` choices, each later term at most `D = 52` choices, and
the coefficient identity `(2J)^k · n · 52^{k−1} = (n/52)(104J)^k` is
gated symbolically. Dimension-blindness is not just asserted: the
reduction and the below-cone/arrival instances are gated on a
**mixed-dimension** chain (site dimensions `2, 3, 2`), where nothing
in the chain refers to qubits.

**Theorem (finite-range all-time volume-uniform Lieb-Robinson
bound).** For the supplied class above with `d ≥ 1`, for all `t` and
every finite `Λ`:

> `||[τ_t(A), B]|| ≤ 2||A|| ||B|| (n_X^𝒮/52) Σ_{k≥⌈d/2⌉}
> (104J|t|)^k / k!`
> `≤ 2||A|| ||B|| (n_X^𝒮/52) · ((104J|t|)^{⌈d/2⌉}/⌈d/2⌉!) ·
> e^{104J|t|}`,

with constants depending only on `||A||`, `||B||`, `n_X^𝒮 ≤ 18|X|`,
`J`, `d` — not on `|Λ|` and not on the site dimensions. The
μ-reweighted exponential tail form carries over verbatim (the tail
factor is algebra-independent): `Σ_{k≥⌈d/2⌉} x^k/k! ≤
e^{−μ⌈d/2⌉ + xe^μ}` for every `μ > 0`, giving decay once
`⌈d/2⌉ > e·104J|t|`, i.e. a velocity-type readout `v ≤ 208eJ` in site
units — the factor `2` from the real face-jump dilation, the `104J`
from the crude degree bound. **Neither `104J` (the class activity
scale) nor `208eJ` is claimed sharp**; the bond-only siblings'
constants (`20J`, `20eJ`) remain the sharper statement on the smaller
class, and this note does not modify them.

**Gauge-shaped coverage (remark, gated at a `Z_2` instance).** Assign
each lattice link's Hilbert space to one chosen endpoint site. Then a
Kogut-Susskind-form magnetic plaquette term (product of the four link
variables around a face) becomes a term whose **site** support lies
inside that face's four sites — a face term of the class — and an
electric single-link term is a bond term directly: it acts on the
link factor assigned to one endpoint of its own geometric bond and by
the identity on the other endpoint — its support is that bond, no
subsumption involved. Gated concretely at `Z_2` link dimension: the four-link
magnetic term `X⊗X⊗X⊗X` commutes exactly with everything on sites
outside its face (including a fifth, far link qubit), the electric
term `Z` on one link commutes with everything off its bond, and the
two do not commute with each other (the gauge dynamics is nontrivial).
Hence KS-form Hamiltonians with **dynamical links of fixed finite
dimension** lie in the supplied class, and the theorem applies to them
with the same constants. What this does **not** give — stated plainly
— is the CT note's `U`-integrated item itself: no gauge measure is
integrated, no transfer kernel is controlled, no gauge-field
correlation bound is derived, and continuous link groups
(infinite-dimensional link spaces) are outside the class.

## No-Go Discipline Gate

- **N1 route inventory (residuals first).** Not attempted and not
  smuggled: (i) the `U`-integrated item itself — no measure, kernel,
  or correlation object appears; the coverage remark is a class
  statement about Hamiltonians, needled against the CT note's own
  open-item sentence; (ii) sharp rates for this class — `104J`/`208eJ`
  are crude degree bounds, stated so; (iii) longer-range terms
  (diameter `> 2`) — outside the class, named; (iv) the transfer
  identification and the bond-class tilt refinement — separate
  surfaces, untouched. Positive routes weighed: (1) reduce faces to
  pairs of bonds — ATTEMPTED and REJECTED: a four-site term is not a
  product or sum of two-site terms in general, and no such
  decomposition is assumed; (2) treat faces as range-2 bonds on a
  coarser lattice — ATTEMPTED and REJECTED as lossy (it would inflate
  `d` bookkeeping unnecessarily); the direct term-adjacency walk is
  exact.
- **N2 hypothesis independence (pairwise).** Hermiticity (norm
  transport only) vs `J` (majorization only) vs `d ≥ 1` (series start
  and `[A, B] = 0`) vs the class membership `𝒮 ⊆` bonds ∪ faces
  (adjacency degrees and reach dilation only): each pair separates at
  the named proof steps; no condition implies another. The site
  dimensions enter nowhere (gated on the mixed-dimension instance) —
  dimension-independence is itself one of the theorem's claims.
- **N3 hidden-wall scan.** New load-bearing content beyond the
  sibling chain: the term-adjacency geometry (natively enumerated,
  box-stable, gated) and the dilated reach lemma with its sharpness
  exhibit. Everything else is the sibling chain cited where natively
  gated. The `d ≥ 1` condition is the same scoping hypothesis as in
  the siblings (tensor class: clean form, so the sibling's `d = 0`
  counterexample applies verbatim here and the exclusion is
  necessary for the clean form).
- **N4 dependency roles, per citation (links are the load-bearing
  citation-graph edges).**
  - [`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    the full algebra-independent chain (Duhamel, norm transport,
    iterated integrals, tail, μ-form, remainder) where natively
    gated; this note re-gates the coefficient identity, a tail
    instance, and every geometry-adjacent fact for the new class.
  - [`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    family class conventions and the commutator norm bound (rebuilt
    there, used representation-level).
  - [`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md):
    the open-item sentence this note's Purpose is scoped against
    (needled); nothing mathematical is imported from it.
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
  - Lattice-gauge / Lieb-Robinson literature: comparator class only.
- **N5 rhetoric audit.** "Gauge-shaped coverage" is a class-membership
  remark with its non-claims enumerated in place; "dynamical links"
  means link factors inside the Hilbert space, not any measure
  statement; the dilation factor is exhibited, not narrated; nothing
  is called sharp.
- **N6 partial-closure scan.** Closed here: the many-body
  Hamiltonian-level LR input for finite-dimensional-link gauge-shaped
  classes — the prerequisite side of the `U`-integrated item. Still
  open, named: the `U`-integrated item itself (measure/kernel/
  correlations/continuous groups), the sharp rates (both classes),
  the transfer identification, and the bond-class tilt refinement.
- **N7 steelman (strongest counterarguments, answered).** (a) "The
  face degree 52 might be box-size-dependent." Enumerated at two
  radii, stable, and cross-checked by hand inclusion-exclusion
  (`48 − 18 + 4 − 1 = 33` faces meeting a face, minus itself, is 32).
  (b) "The dilated cone makes the bound weaker than the bond-only
  sibling on bond-only Hamiltonians." Correct and stated: on the
  smaller class the sibling's constants are sharper and are not
  modified; this theorem's value is the wider class. (c) "Gauge
  coverage is a smuggled U-integrated claim." No: the coverage remark
  is needled directly against the CT note's open-item sentence, and
  the measure/kernel/correlation content is explicitly not derived.
  (d) "The set-indexed family might hide same-support collisions."
  Handled by convention: same-support terms are summed into one `h_S`
  before `J` is taken; distinct supports are never relabeled (an
  earlier draft's blanket single-site subsumption sentence was refuted
  in review — counterexamples: a one-site region has no bond, and
  relabeling onto an occupied bond either duplicates a support or
  doubles the norm — and was removed; genuinely single-site terms are
  outside the stated family).
- **N8 prior-wall echo.** The family's walls: block01's region-level
  scope marker (crossed openly by block03, cited); the CT note's
  fixed-background scope (this note stays Hamiltonian-level, touching
  neither resolvent nor measure); the CAR no-go notes dispositioned
  in the block04 sibling concern statistics derivation and are
  irrelevant to this tensor-class note. No landed no-go touches
  finite-range spin locality. The family's exhibit-pair discipline is
  repeated (face-jump arrival gated at `k = 1`, `d = 2`;
  non-sharpness stated for both new constants).

**Status: PASS** (all eight items answered; the two honest weaknesses
— crude degree constants and the dilated cone — are stated in the
theorem and steelman rather than hidden).

## Non-Claims

- Does **not** derive the `U`-integrated statement: no gauge measure,
  transfer kernel, or gauge-field correlation control; continuous
  link groups are outside the class.
- Does **not** claim `104J` or `208eJ` is sharp, and does **not**
  modify the bond-only siblings' sharper constants on their class.
- Does **not** cover terms of diameter greater than `2`.
- Does **not** cover `d = 0` (inherited clean-form exclusion; the
  sibling's counterexample applies verbatim to this tensor class).
- Does **not** involve CAR grading (tensor class only; the fermionic
  sibling stands separately).
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py`](../scripts/microcausality_finite_range_plaquette_class_walk_expansion_2026_07_18.py)
— exact throughout. Gate kinds, honestly distinguished: **exhaustive
finite gates** (the term-adjacency degrees for **every** bond and face
orientation at two box radii; the reach values at `k = 1, 2, 3`; the
mixed length-2 walk count — finite enumerations over the stated
ranges, with cubic symmetry thereby checked rather than assumed),
**exact representation gates** (the mixed-dimension chain reduction
and cone instances, including a four-site mixed-dimension face term
with its own one-step opposite-corner arrival; the face-jump
sharpness exhibit; the `Z_2` KS-shaped instance), and **symbolic
identity gates** (the coefficient assembly; the `⌈d/2⌉` arithmetic in
symbolic even/odd cases with the boundary failure exhibited; the tail
mechanism via binomial domination, supported by an exact partial-sum
instance — the infinite-tail statement itself is the sibling's, cited
where natively gated). The `N`-group gates are **presence needles**:
they pin quoted sentences and structure, and are not correctness
oracles for the quoted content. The enumeration code is written
natively for this runner — the loop-pack worker analysis was
scaffolding and is not executed or cited by the runner. The gate
sequence is enforced against an ordered label manifest (drift fails
the run). The runner prints one `PASS`/`FAIL` line per gate and a
final total; the cached transcript is committed at the path in the
header at landing time.
