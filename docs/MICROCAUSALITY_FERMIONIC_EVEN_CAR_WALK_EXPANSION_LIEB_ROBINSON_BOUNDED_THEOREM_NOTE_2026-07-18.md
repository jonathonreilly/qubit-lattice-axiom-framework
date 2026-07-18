---
claim_id: microcausality_fermionic_even_car_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional CAR half of the family's named fermionic transfer bridge, on a supplied fermionic class (the axioms supply no dynamics and no fermionic carrier; the CAR algebra, the even Hermitian bond terms, and the finite region are supplied objects; same Heisenberg convention and declared finite-matrix ODE context as the sibling chain), under the standing scoping hypothesis X ∩ Y = ∅ (d ≥ 1 — it gives the series start its content and matches the sibling's clean-form scope; the sibling's d = 0 counterexample refutes the clean form only, and the d = 0 case is out of scope here, not claimed false): (F1) the CAR relations, gated in the faithful Jordan-Wigner representation used as the computational device; (F2) the graded locality lemma, PROOF-CARRIED and REBUILT from the CAR relations — disjoint-support even elements commute with arbitrary disjoint elements, odd-odd disjoint pairs anticommute — with the generator-level anticommutation, the even/odd table, the odd-term necessity exhibit, AND the exhaustive 256-pair homogeneous-basis sign-law gate with an explicit p·q-vs-p+q discrimination clause; (F3) the motivation exhibit: hopping/pairing terms (odd local parity at each endpoint) between JW-nonadjacent sites acquire a string (the image fails to commute with an intermediate qubit operator) while CAR locality holds (the image commutes with the odd intermediate generators and the even intermediate density) — endpoint-parity-dependent, so no uniform representation transfer exists and the graded lemma is the required replacement; (F4) the chain carry-over: the sibling chain uses locality in exactly three places (boundary reduction, base-term vanishing, initial-term deletion); the graded lemma supplies the first two for arbitrary-parity observables and the third only when at least one observable is even, so every post-initial-term step applies to even bond Hamiltonians — the algebra-dependent steps re-gated at exact fermionic instances (reduction, self-drop, Hermitian generator sums, below-cone vanishing at d = 3 against both even and odd probes, arrival at k = d on both, parity preservation exhibit) and the algebra-independent steps (Jacobi, conjugation, norm transport, iterated integrals, walk combinatorics, coefficient assembly, tail and μ-reweighting lemmas) cited to the sibling where they are natively gated, with the coefficient identity re-gated here; (F5) the theorem: for even Hermitian bond terms with ||h_b|| ≤ J on the CAR algebra over finite Λ ⊂ Z^3, arbitrary-parity A, B with d ≥ 1, ||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A||||B||(n_X/10) Σ_{k≥d} (20J|t|)^k/k!, all t, volume-uniform, with the zeroth term ||[A, B]|| vanishing whenever A or B is even (L-F) — the clean sibling form on the even sector, the explicit-zeroth-term form for odd-odd pairs (gated nonvanishing instance) — and with the μ-reweighted exponential form and the 20eJ readout inherited. The transfer-operator identification (Berezin/log-transfer) is NOT attempted and remains open; neither 20J nor 20eJ is claimed sharp; nothing physical is selected and no parity superselection is claimed."
upstream_dependencies:
  - minimal_axioms
  - microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
  - microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_fermionic_even_car_walk_expansion_2026_07_18.py
---

# Microcausality: Fermionic Even-CAR Walk-Expansion Lieb-Robinson Bound

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; supplied fermionic class (CAR algebra,
even Hermitian bond terms, finite region); the axioms supply no
dynamics and no fermionic carrier; same conventions and declared ODE
context as the sibling chain.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_fermionic_even_car_walk_expansion_2026_07_18.py`](../scripts/microcausality_fermionic_even_car_walk_expansion_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_fermionic_even_car_walk_expansion_2026_07_18.txt`](../logs/runner-cache/microcausality_fermionic_even_car_walk_expansion_2026_07_18.txt)

## Purpose

The sibling
[`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
closes the family's walk-expansion task for qubit bond Hamiltonians and
names, in its Non-Claims, "the fermionic transfer bridge" as open. That
bridge has two halves: (i) extend the Lieb-Robinson chain to a
**supplied CAR algebra** (no identification of this algebra with any
framework matter sector is made or needed here), and (ii) identify a
transfer-operator-generated Hamiltonian to which it applies. This note supplies half (i) only. Half (ii)
(Berezin/log-transfer identification) is **not attempted** and remains
open.

The extension is not a representation transfer. An allowed even bond
term need not stay two-factor-local under Jordan-Wigner: terms whose
local parity at each endpoint is odd — hopping and pairing — acquire a
`Z`-string through the JW-intermediate sites when the two sites are
not adjacent in the chosen JW order (terms with even local parity at
each endpoint, such as `n_i n_j`, stay two-factor-local; the
obstruction is endpoint-parity-dependent, which is exactly why a
uniform representation transfer is unavailable). The runner gates this
concretely: the JW image of the hop between JW-nonadjacent sites fails
to commute with an intermediate qubit operator (it is not supported on
the two qubit factors), while CAR locality holds (it commutes with the
odd intermediate generators `c_2, c_2^†` and the even intermediate
element `n_2`). So the qubit-bond
theorem does not apply as stated, and the correct replacement is an
intrinsic **graded locality lemma** on the CAR algebra — the one new
load-bearing ingredient here. The lemma is **proof-carried** (its short
induction is written in full below) and supported by an exhaustive
exact gate: the runner verifies the graded commutation sign
`(−1)^{p·q}` over the complete homogeneous monomial basis of two
disjoint two-site regions (256 pairs), including an explicit
discrimination clause showing the exponent `p·q` — not `p + q` — is
forced. With the lemma, every **post-initial-term** step of the
sibling chain carries over; the initial-term deletion (`[A, B] = 0`)
carries only when at least one observable is even, and the theorem
below keeps the zeroth term explicitly in the general case.

## Hypotheses (all supplied, none derived)

A finite region `Λ ⊂ Z^3` with induced nearest-neighbor bond set
`E(Λ)` (assumed nonempty; at `E(Λ) = ∅` set `J = 0`, `H = 0`, and every
statement is trivial); the CAR algebra `CAR(Λ)` with generators
`c_x, c_x^†` (`x ∈ Λ`)
and relations `{c_x, c_y^†} = δ_{xy}`, `{c_x, c_y} = {c_x^†, c_y^†} =
0`; for `S ⊆ Λ`, `CAR(S)` is the subalgebra generated by the `c_x,
c_x^†` with `x ∈ S`, and an element is **even** (resp. **odd**) when it
is a sum of monomials with an even (resp. odd) number of generators. A
supplied bond Hamiltonian `H = Σ_{b∈E(Λ)} h_b` with each `h_b` **even**,
Hermitian, in `CAR(b)`, and `J = max_b ||h_b||` (evenness is
load-bearing: the graded lemma requires it, and the runner exhibits an
odd term breaking the reduction step). Observables `A ∈ CAR(X)`,
`B ∈ CAR(Y)` of **arbitrary parity**, with `X ∩ Y = ∅`, equivalently
`d ≥ 1` — required throughout, as a **scoping hypothesis**: it gives
the series start `k ≥ d` its content (the reach lemma) and matches the
sibling's clean-form scope. Stated precisely: the sibling's gated
`d = 0` counterexample refutes the **clean** form (no zeroth term);
the general-parity form below keeps `||[A, B]||` explicitly and is not
refuted by that instance — the `d = 0` case is simply **out of scope**
here, not claimed false. `d = d(X, Y)` is the `Z^3` graph distance; `n_X = #{b ∈ E(Λ) : b ∩ X ≠ ∅} ≤ 6·|X|`;
Heisenberg convention `τ_t(A) = e^{itH} A e^{−itH}`.

Computation and norms: the finite CAR algebra is realized faithfully by
the Jordan-Wigner construction `c_j = (Π_{k<j} Z_k) σ^-_j` (declared
context; the CAR relations are gated in the representation, and the
operator norm is representation-level matrix analysis). The declared
finite-matrix ODE context of the sibling (exponential calculus,
time-ordered propagator existence, Riemann limit passage) is reused
unchanged, including the directed-time discipline: bounds are proved
for `t ≥ 0` and extended to `t < 0` by the `H → −H` symmetry, under
which the even Hermitian bond class is invariant with the same `J`,
bonds, and walks. The axioms supply no dynamics (needled) and no
fermionic carrier (the axiom memo's four-axiom surface contains no
fermion axiom; the CAR algebra enters only as a supplied object here);
everything is bridge-conditional exactly as in the siblings. No literature statement is load-bearing; the
Lieb-Robinson line for lattice fermions is a comparator class only.

## Results

**Graded locality lemma (rebuilt from the CAR relations; local alias
L-F).** This lemma is **proof-carried**: the following induction is the
proof, and the runner supports it with an exhaustive exact gate rather
than replacing it. Let `S ∩ T = ∅`, let `A ∈ CAR(S)` be a monomial of
`p` generators and `B ∈ CAR(T)` a monomial of `q` generators.
Cross-site generators anticommute: for `x ≠ y`, every pair among
`c_x, c_x^†, c_y, c_y^†` taken across the two sites anticommutes
(`δ_{xy} = 0` in the relations; gated at the generator level). Moving
one generator of `B` across all of `A` therefore gives the sign
`(−1)^p`; iterating over `B`'s `q` generators,

> `A·B = (−1)^{p·q} B·A`.

By bilinearity: **even `A` commutes with every disjoint `B`** (any
parity), and **odd-odd disjoint pairs anticommute** (so their
commutator is generically nonzero — gated with a Majorana pair). The
graded table is gated (runner group C), the full sign law is gated
exhaustively over the complete homogeneous monomial basis of two
disjoint two-site regions — 256 ordered pairs, with a discrimination
clause proving the exponent is `p·q` and **not** `p + q` (the mixed
even-odd pairs separate the two laws) — and the odd-term necessity
exhibit (gate C5) shows the reduction step below genuinely fails
without evenness.

**Motivation exhibit (JW strings; why L-F is needed).** On four sites
with JW order `0 < 1 < 2 < 3`, the even hop `h = c_1^† c_3 + c_3^† c_1`
between JW-nonadjacent sites has JW image carrying `Z_2`: it fails to
commute with the qubit operator `X_2` (gated), so it is **not** a qubit
bond term on the factors `{1, 3}` — the sibling's hypothesis class does
not contain it representation-wise. Its CAR locality is nevertheless
exact: it commutes with the odd site-2 generators `c_2, c_2^†` and
with the even site-2 element `n_2` (gated) — precisely the graded
lemma. So the fermionic theorem is not a corollary of the qubit
theorem by JW transfer; it needs the graded argument.

**Chain carry-over (every post-initial disjointness step replaced by
the graded lemma).** The sibling chain uses locality in exactly three
places: the boundary reduction, the base-term vanishing, and the
initial-term deletion `[A, B] = 0`. The graded lemma supplies the
first two for even bond terms against arbitrary-parity observables;
the third it supplies only when at least one observable is even, which
is why the theorem keeps the zeroth term in the general case:

1. *Boundary reduction:* `[H, O] = [H_{∂Z}, O]` for `O ∈ CAR(Z)`, since
   each `h_b` with `b ∩ Z = ∅` is even and disjoint (L-F; gated at the
   fermionic instance `[H, n_0] = [hop_{01}, n_0]` on the four-site
   chain, with the two far hops commuting exactly). The self-drop
   `[h_b, h_b] = 0` and the per-bond re-derivation with the reduced
   generator `H̃_b` (self term dropped **before** the Jacobi step) are
   as in the sibling (gated).
2. *Base-term vanishing:* `[h_{b_k}, B] = 0` unless `b_k ∩ Y ≠ ∅`
   (`h_{b_k}` even and disjoint from `Y`; L-F — same gate family), and
   `[A, B] = 0` at `d ≥ 1` for arbitrary parities? **No** — this is
   the one place arbitrary parity matters: for odd `A` and odd `B`
   disjoint, `[A, B] = 2AB ≠ 0` in general. The theorem's series
   nevertheless starts at `k ≥ d ≥ 1` with **no** `||[A, B]||` term
   only when that term vanishes; for odd-odd pairs it does not, and
   the honest statement keeps it: the bound proved is

   > `||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| ||B|| (n_X/10)
   > Σ_{k≥d} (20J|t|)^k / k!`,

   with `||[A, B]|| = 0` whenever `A` or `B` is even (L-F), i.e. the
   sibling's clean form holds for the even-observable sector, and the
   general-parity form carries the exact `t = 0` commutator as its
   zeroth term (which any correct bound must, since `τ_0 = id`). Both
   cases are gated (even probe: clean; odd-odd: `t = 0` term nonzero,
   exhibited).

All remaining steps of the sibling chain are algebra-independent matrix
analysis or `Z^3` geometry, unchanged: Jacobi and
conjugation-distribution, the directed-time norm-transport lemma and
`H → −H` extension, the commutator norm bound, iterated integrals
`|t|^k/k!`, the walk combinatorics (bonds per site `6`, bond-adjacency
degree `10`, `|𝒲_k| ≤ n_X·10^{k−1}`, reach `k ≥ d`), the coefficient
assembly `(2J)^k n_X 10^{k−1} = (n_X/10)(20J)^k` (re-gated here), the
factorial tail lemma, the `μ`-reweighted exponential form, and the
vanishing remainder. They are cited to the sibling where they are
natively gated; this note re-gates the algebra-adjacent instances in
the fermionic representation:

- below-cone vanishing at `d = 3` for `k = 0, 1, 2` against **both** an
  even probe (`n_3`) and an odd probe (`c_3 + c_3^†`) — the graded
  lemma in action, since the evolved observable here is even and L-F
  kills both parities of disjoint probe;
- cone arrival at `k = d = 3` against both probes (the family's
  reaching-instance discipline);
- parity preservation of the adjoint chain for even `H` (exhibit);
- Hermiticity of generator sums (`H̃` self-adjoint, as G2 requires);
- an even **pairing** term `c_x^† c_y^† + c_y c_x` alongside hopping
  (Hermitian, even, disjoint-commuting — the class is not
  hopping-only; gated).

**Theorem (fermionic all-time volume-uniform Lieb-Robinson bound).**
For the supplied even-CAR class above with `d ≥ 1`, for all `t` and
every finite `Λ`:

> `||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| ||B|| (n_X/10)
> Σ_{k≥d} (20J|t|)^k / k!`
> `≤ ||[A, B]|| + 2||A|| ||B|| (n_X/10) · ((20J|t|)^d/d!) · e^{20J|t|}`,

with `||[A, B]|| = 0` whenever `A` or `B` is even. Constants depend
only on `||A||`, `||B||`, `n_X ≤ 6|X|`, `J`, `d` — not on `|Λ|`. The
`μ`-reweighted exponential tail form and the `μ = 1` velocity-type
readout `20eJ` carry over verbatim (the tail factor is
algebra-independent) — with the precise reading that for odd-odd
pairs they control the **dynamical tail** (the series term) only: the
zeroth term `||[A, B]||` is `t`- and distance-independent and is not
claimed to decay. Neither `20J` (walk-series activity scale) nor
`20eJ` is claimed sharp.

## No-Go Discipline Gate

- **N1 route inventory (the named residuals, then the positive
  routes).** The three residuals this note does NOT take, with why
  each is neither smuggled nor foreclosed: (i) transfer-operator
  identification — NOT ATTEMPTED: no transfer operator, Berezin
  kernel, or log-transfer object appears anywhere in the hypotheses or
  proof; the supplied `H` is an abstract even bond Hamiltonian, so
  nothing here quietly identifies it with a transfer generator, and
  nothing forecloses that identification later; (ii) sharp rate — NOT
  ATTEMPTED: the constants inherit the sibling's `20J`/`20eJ` with
  non-sharpness restated; no optimization is performed or blocked;
  (iii) `U`-integrated statement — NOT ATTEMPTED: no gauge measure or
  link integration appears; the class is background-free. Positive
  routes weighed for the extension itself: (1) transfer the qubit
  theorem through JW — ATTEMPTED and REFUTED as a route (string
  exhibit, gated); (2) restrict to JW-adjacent bonds — ATTEMPTED as a
  scoping and rejected (covers only one-dimensional orderings); (3)
  hopping-only lemma — ATTEMPTED and widened (the `(−1)^{p·q}` law
  covers all even monomials; pairing gate); (4) odd bond terms —
  ATTEMPTED and EXCLUDED with the gated necessity exhibit; (5) odd
  observables — ATTEMPTED and INCLUDED at the price of the explicit
  zeroth term, gated.
- **N2 hypothesis independence (pairwise).** Four supplied conditions;
  each pair separates at a named proof step: evenness vs Hermiticity —
  an odd Hermitian term (Majorana `c_x + c_x^†`) satisfies the second
  and breaks the reduction (gate C5), while an even non-Hermitian term
  (`c_x^† c_y`) satisfies the first and breaks `H̃^† = H̃`; evenness
  vs `J` — the norm bound never enters the graded lemma, and evenness
  never enters the majorization; evenness vs `d ≥ 1` — evenness kills
  the zeroth term regardless of `d`, while `d` sets the series start
  regardless of parity; Hermiticity vs `J` — `H̃^† = H̃` is used only
  in the cited norm transport, `J` only in the walk majorization;
  Hermiticity vs `d ≥ 1` and `J` vs `d ≥ 1` — disjoint proof
  locations (norm transport / majorization vs series start). No
  condition implies another.
- **N3 hidden-wall scan.** New load-bearing content beyond the sibling
  chain is exactly one lemma (the graded locality lemma) plus the
  faithfulness of the JW realization (declared context, with the CAR
  relations gated in the representation). No superselection, vacuum,
  number conservation, or ground-state structure is used anywhere. The
  `d ≥ 1` condition is a scoping hypothesis whose precise status
  (clean-form necessity only) is stated in Hypotheses; the
  directed-time discipline is inherited explicitly.
- **N4 dependency roles, per citation (links are the load-bearing
  citation-graph edges).**
  - [`MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    supplies the entire algebra-independent chain (norm transport,
    walks, assembly, tail, `μ`-form) where it is natively gated; this
    note re-gates the coefficient identity and every algebra-adjacent
    instance fermionically. Residual: none — the split is the
    carry-over section's table of steps.
  - [`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    supplies the family class conventions (Hermitian bond terms, `J`)
    and the commutator norm bound (rebuilt there; used
    representation-level here). Residual: none.
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only. The absence of a fermionic
    carrier in the four-axiom surface is stated as prose (it is an
    absence, not a needlable sentence); the CAR algebra is a supplied
    object.
  - Lattice-fermion Lieb-Robinson literature: comparator class only;
    no cited statement is load-bearing.
- **N5 rhetoric audit.** "Bridge" is used only with its two halves
  named and half (ii) explicitly not attempted; "fermionic" refers to
  a supplied CAR class with no framework-matter identification;
  "carries over" is scoped to post-initial-term steps with the
  initial-term caveat stated; scales inherit the sibling's
  non-sharpness language.
- **N6 partial-closure scan.** Closed here: the CAR half of the
  fermionic bridge. Still open, named: the transfer-operator
  identification (Berezin/log-transfer — the other half), the sharp
  rate, and the `U`-integrated statement. Nothing here forecloses
  them.
- **N7 steelman (strongest counterarguments found in review,
  answered).** (a) "The general-parity claim is false: odd-odd
  disjoint observables have `[A, B] ≠ 0` at `t = 0`, contradicting a
  series starting at `k ≥ d`." Correct against the sibling's clean
  form — the theorem keeps the explicit zeroth term, gates the
  odd-odd nonvanishing instance, and claims the clean form only on
  the even sector. (b) "The lemma's sign law was never formally gated
  — a `(−1)^{p+q}` law would pass the instance gates." Correct as
  found in review; repaired: the exhaustive 256-pair basis gate with
  the explicit `p·q`-vs-`p+q` discrimination clause now separates the
  two laws. (c) "Prior repo notes about JW strings and CAR locality
  might already wall this off." Checked and dispositioned in N8: both
  prior notes concern whether the framework can **derive** CAR
  statistics (answer: those routes cannot); this note **supplies**
  CAR and derives only locality bounds — orthogonal, and consistent
  with this note's no-carrier boundary. (d) "Evenness is physics
  smuggled in." No: a mathematical hypothesis with a gated necessity
  exhibit; no superselection claim.
- **N8 prior-wall echo (repo-wide disposition).** Repo search for
  CAR/JW/graded-locality surfaces found two prior no-go notes, both
  orthogonal and both reinforcing this note's supplied-CAR boundary:
  `KS_ETA_VS_JW_STRING_CAR_LOCALITY_NO_GO_NOTE_2026-06-02.md` (the
  staggered `eta` signs neither supply nor need the JW string — the
  statistics object is not derived from matter-attachment locality;
  backticked deliberately: dispositioned, not load-bearing) and
  `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`
  (the rotation-exchange route cannot force CAR over hard-core-boson
  statistics; same disposition). Neither forecloses locality bounds
  on a **supplied** CAR algebra, and this note derives no statistics.
  The CT note's open tasks (`U`-integrated, sharp rate) are untouched;
  the sibling's Non-Claims sentence naming this bridge is the needled
  authority for the task taken here. The family's exhibit-pair
  discipline is repeated (arrival gated at `k = d` on both probe
  parities; non-sharpness inherited).

**Status: PASS** (all eight items answered above after the review
round's repairs: residual-directed N1, pairwise N2, linked N4,
review-sourced N7 including the repaired sign-law gate gap, and the
repo-wide N8 disposition of the two prior CAR-statistics no-go notes).

## Non-Claims

- Does **not** attempt the transfer-operator identification
  (Berezin/log-transfer) — the other half of the named bridge, still
  open.
- Does **not** claim `20J` or `20eJ` is sharp, any physical velocity,
  or the `U`-integrated statement.
- Does **not** derive a fermionic carrier, claim parity
  superselection, or use number conservation; the CAR class is
  supplied.
- Does **not** claim the clean (no zeroth term) bound for odd-odd
  observable pairs — the exact `t = 0` commutator is kept explicitly.
- Does **not** cover `d = 0` — out of scope, not claimed false: the
  sibling's gated necessity exhibit binds the clean (no zeroth term)
  form only, and this note's general-parity form keeps the zeroth term.
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_fermionic_even_car_walk_expansion_2026_07_18.py`](../scripts/microcausality_fermionic_even_car_walk_expansion_2026_07_18.py)
— sympy-exact throughout, on four-site JW matrices containing
three-site subchains. Gate kinds, honestly distinguished: **exhaustive
finite gates** (the graded sign law over the complete 256-pair
homogeneous monomial basis of two disjoint two-site regions, with the
`p·q`-vs-`p+q` discrimination clause), **exact representation gates**
(CAR relations, graded table, norms, reductions, cone instances,
string exhibit, pairing term, odd-odd zeroth term — exact at the named
instances, supporting the proof-carried lemma and chain rather than
replacing them), and **symbolic identity gates** (the coefficient
assembly re-gate). The runner also structurally checks this note
itself: the theorem inequality with its zeroth term is pinned in both
the frontmatter and the body, a clean arbitrary-parity form is
rejected if it ever reappears, and the No-Go section's eight items and
Status line are parsed. The gate count is enforced against a manifest
(`finish` fails on any count drift). The algebra-independent chain is
cited to the sibling's runner where it is natively gated, not
re-proved here. The runner prints one `PASS`/`FAIL` line per gate and
a final total; the cached transcript is committed at the path in the
header at landing time.
