# Dynamics-Form From Record-Preservation: the Gauge-Invariant-Local (Wilson) Class (Bounded Theorem)

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-05
**Type:** bounded theorem
**Claim type:** bounded_theorem
**Status:** source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_dynamics_form_from_record_preservation_2026_06_05.py`](../scripts/frontier_dynamics_form_from_record_preservation_2026_06_05.py)
**Cached log:**
[`logs/runner-cache/frontier_dynamics_form_from_record_preservation_2026_06_05.txt`](../logs/runner-cache/frontier_dynamics_form_from_record_preservation_2026_06_05.txt)

This is the **composition** of two upstream finite-model results:

- the timeless gauge-structure boundary in
  [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  (observables = gauge-invariant records; the observable algebra `A_inv` is the
  commutant of the per-vertex Gauss generators `{G_v}`);
- the temporal record-formation constraint in
  [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  (record formation forces a conserved pointer/charge and locality on the
  transfer step).

The composition asks: does requiring the dynamics to **preserve the
record/observable algebra** (a time-evolved record is still a gauge-invariant
record) force the dynamics FORM into the gauge-invariant-local class whose
leading terms are the Wilson plaquette + covariant hopping + mass, leaving only
the couplings supplied?

## Claim

Condition on the explicit finite lattice gauge models in the runner:

- a two-link-end `U(1)` carrier (matter `A`, link-ends `a`, `b`, matter `B`)
  with endpoint Gauss generators `G_A = sz(A)+sz(a)`, `G_B = sz(b)+sz(B)` --
  the same carrier and generators as the upstream TWO_ENDPOINT note;
- a single-plaquette `Z2` lattice gauge model (4 corner sites + 4 link spins, 8
  qubits) with standard Kogut-Susskind / Fradkin-Shenker conventions (link
  gauge field `sz(link)`, matter field `sz(site)`, Gauss generator
  `G_s = sx(site) * prod_{l~s} sx(l)`);
- an `SU(2)` endpoint cross-check on the same four-qubit carrier.

Under record-preservation + locality + Hermiticity, the following hold.

1. **Gauge-covariance from record-preservation (exact equivalence).** For a
   Hermitian `H`, the Heisenberg evolution maps the observable algebra into
   itself (`O(t) = e^{iHt} O e^{-iHt}` stays in `A_inv` for every record
   `O in A_inv` and every `t`) **if and only if** `H` is gauge-covariant,
   `[H, G_v] = 0` for all `v` (equivalently `H in A_inv`). The runner certifies
   this at theorem level by a **dimension count**: the space
   `{Hermitian H : ad_H preserves A_inv}` has dimension exactly `dim(A_inv)`
   (no "normalizer slack"). The control `[H, G_v] != 0` (e.g. a bare on-site
   `sx`) maps a gauge-invariant record to a gauge-**variant** operator -- the
   evolved object is not a record.

2. **Gauge-invariant LOCAL Hermitian basis; plaquette and covariant hopping are
   the leading terms.** With `[H, G_v] = 0` + finite range + Hermiticity, the
   allowed local terms are: closed Wilson loops (`Re Tr` of link products around
   a loop), covariant matter paths (`chi-bar U...U chi`), on-site mass /
   charge-parity, and the on-link electric term. The **smallest closed
   pure-gauge loop is the plaquette** (support 4 = the minimum to close a loop
   on a cubic lattice; a single link or an open path is **not** gauge-invariant)
   and the **smallest matter term is the covariant nearest-neighbour hopping**
   (support 3 = two sites + one connecting link; the **undressed** hop is
   **not** gauge-invariant -- dressing by the link is forced). Larger loops and
   longer matter paths are strictly higher operator-range.

3. **Record-broadcast = covariant hopping.** The interaction that broadcasts
   the matter record (the matter pointer/charge) **gauge-covariantly** is
   exactly the covariant hopping `chi-bar U chi`: it conserves the total charge
   (the record), it is gauge-invariant (so it broadcasts a *gauge-invariant*
   record), and it actually spreads the charge along the gauge link. The bare
   (undressed) hop conserves total charge but is gauge-**variant** (broadcasts a
   non-record); an on-site flip does not even conserve the charge.

4. **The framework's `H` is the leading element of the forced class.** The
   Wilson plaquette + covariant staggered hopping + on-site mass (the
   framework's gauge-matter Hamiltonian / reflection-positive OS transfer
   `T = e^{-H}`) is Hermitian, gauge-invariant term-by-term, local, and built
   only from the leading-range invariants (plaquette + nearest-neighbour hop +
   on-site). It therefore lies in, and is the leading element of, the forced
   gauge-invariant-local class.

5. **Residual (NOT forced).** Gauge-covariance + locality + Hermiticity supply
   the **basis** of allowed local terms, not the combination. Explicitly NOT
   forced:
   - the **couplings** (`beta` / `g_bare`, the matter coupling, the mass, the
     relative weights) -- every choice yields a valid class member;
   - the **minimality / lowest-order truncation** -- a larger loop or a longer
     matter path is equally gauge-invariant-local, so "only the plaquette and
     the nearest-neighbour hop" is a truncation choice, not a forced one;
   - **non-triviality** -- the trivial `H = 0` is in the class, so
     gauge-covariance + locality + Hermiticity do not force any nonzero
     dynamics.

This is **bounded** because the upstream identifications it composes are bounded
model conventions: the two-endpoint Gauss generators (TWO_ENDPOINT note) and the
quantum-Darwinism reading of a *record* together with pointer-non-demolition
(RECORD_FORMATION note) are not supplied by the Lattice, Quantum, and Record
axioms. The form-class constraint is forced **given** those bridges.

## The honest verdict

The dynamics **FORM is forced to the gauge-invariant-local (Wilson) class** --
Wilson plaquette + covariant hopping + on-site mass as the leading terms -- by
`{record-preservation (TWO_ENDPOINT) + locality (RECORD_FORMATION) +
Hermiticity}`. The **residual is exactly (i) the couplings and (ii) the
lowest-order / minimality truncation** (plus the trivial-`H` ambiguity).

This is **not** "the action is derived." It **reconciles** with, and sharpens,
the framework's standing
[`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md):
that no-go shows Wilson, heat-kernel, and Manton actions cannot be distinguished
by the retained primitives. **All three candidates are gauge-invariant-local**,
so the no-go operates *entirely inside* the forced class. The composition closes
the question one level up (the **form-class** is forced) while the action-form
no-go remains the precise residual one level down (the **specific action** --
the coupling and the truncation -- is not). The framework's "action hand-added"
finding is thus relocated, not contradicted: what is hand-added is the
selection *within* the forced class, not the class itself.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  repo baseline Lattice + Quantum + Record language. The axiom baseline
  chain-satisfies as an approved premise; it is not a source of bounded status.
- [`TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md`](TWO_ENDPOINT_GAUSS_LAW_INVARIANCE_PROFILE_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  supplies the gauge-structure boundary (`A_inv` = commutant of `{G_v}`,
  endpoint Gauss conventions, the `dim = 36` `U(1)` invariant algebra reused
  here). This note does not enlarge that result.
- [`RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md`](RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  supplies the temporal record-formation constraint (conserved pointer/charge +
  locality). This note does not enlarge that result.
- The two-endpoint Gauss generators and the quantum-Darwinism record reading are
  the bounded model conventions inherited from the two notes above.
- The Hermitian inner-derivation reasoning behind the exact equivalence
  (every derivation of a finite-dimensional von Neumann algebra is inner, so
  `ad_H` preserving `A_inv` forces `H in A_inv`) is an elementary,
  reproven-in-runner fact, not an import.

## What This Does Not Claim

- It does **not** derive the action, the gauge action functional, gauge bosons,
  coupling values, beta functions, electroweak symmetry breaking, or color
  `SU(3)`. It constrains only the dynamics **form-class**.
- It does **not** pin the coupling strength or the transfer magnitude: any
  coupling yields a valid class member. In particular it says **nothing** about
  `beta = 6`.
- It does **not** force minimality / the lowest-order truncation: larger loops
  and longer matter paths are equally admissible local invariants.
- It does **not** force non-trivial dynamics: `H = 0` is in the class.
- It does **not** derive the upstream bridges (two-endpoint Gauss generators;
  the quantum-Darwinism record reading) from Lattice + Quantum + Record; those
  remain supplied bounded inputs.
- It does **not** establish the lattice/continuum, the non-abelian dynamical
  equivalence beyond the static `SU(2)` invariance cross-check, or any
  interacting-field generalization; the theorem is on the explicit finite
  models.
- It does **not** identify the gauge-invariant algebra with physical
  observables, nor does it enlarge the companion timeless/temporal results.

The safe downstream use is only the bounded finite-model statement: under the
stated conventions, record-preservation + locality + Hermiticity forces the
dynamics into the gauge-invariant-local class with the Wilson plaquette +
covariant hopping + mass as the leading terms, and the residual is exactly the
couplings + the minimality/truncation (plus the trivial-`H` ambiguity).

## Reconciliation With the Action-Form No-Go (one paragraph)

`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06` shows the retained
primitives cannot select among Wilson / heat-kernel / Manton actions, which
differ at finite `beta`. Each of those three is a gauge-invariant functional of
the link variables -- i.e. each lives **inside** the gauge-invariant-local class
this note forces. So the two results are complementary, not in tension: this
note forces the **class** (a positive form-derivation modulo couplings); the
no-go names the **residual selection within the class** (couplings + the action
functional's finite-`beta` shape) as not forced. Together they give a precise
"`X` is forced, `Y` is not": `X` = the gauge-invariant-local form-class with
Wilson/hopping/mass leading; `Y` = the couplings and the lowest-order
truncation.

## Runner Certificate

The runner verifies, on the explicit `U(1)` two-link-end carrier, the `Z2`
single-plaquette model, and the `SU(2)` endpoint cross-check (numpy, exact dense
operators, peak RSS well under 2 GB):

1. **S1** -- `A_inv` is the commutant of `{G_v}` (`dim = 36` on the `U(1)`
   carrier, matching the upstream note); a gauge-covariant `H` keeps a record a
   record for all `t` (and infinitesimally), while a `[H,G_v] != 0` control maps
   a record to a gauge-variant operator; and the **exact** dimension count
   `dim{Hermitian H : ad_H preserves A_inv} = dim(A_inv)` certifies the
   equivalence `records->records <=> [H,G_v]=0` at theorem level (no normalizer
   slack), with random-Hamiltonian cross-checks and an **exhaustive** Pauli-
   string cross-check (the two predicates agree on all 256 basis elements).
2. **S2** -- the plaquette is the smallest gauge-invariant closed loop (a single
   link / open path is not invariant); the covariant nearest-neighbour hopping
   is the smallest gauge-invariant matter term (the undressed hop is not
   invariant); on-site mass / charge-parity and on-link electric terms are
   invariant; support sizes confirm the range ordering; the `SU(2)` cross-check
   confirms the same dressed-loop-only invariance non-abelianly.
3. **S3** -- the covariant hopping conserves the total charge (the record), is
   gauge-invariant, and broadcasts the charge along the link; the bare hop is
   gauge-variant; the on-site flip does not conserve charge.
4. **S4** -- the framework `H` (Wilson plaquette + covariant staggered hopping +
   mass + electric) is Hermitian, gauge-invariant term-by-term, and built only
   from leading-range invariants -- the leading element of the forced class.
5. **S5** -- the residual ledger: couplings not forced, minimality/truncation
   not forced (longer loops/paths admissible), trivial `H = 0` in the class;
   plus the explicit reconciliation with the action-form no-go.

Run:

```text
python3 scripts/frontier_dynamics_form_from_record_preservation_2026_06_05.py
```

Expected result:

```text
SUMMARY: PASS=62 FAIL=0
```
