# Newton's Law Conditional Worked Example on the Z^3 Spatial Substrate

**Date:** 2026-04 (audit-narrowing refresh 2026-05-10); 2026-05-28
(register the test-mass force coupling as a third named admission BA-3
per audit verdict).
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane. The
`bounded_theorem` label is a source-side claim-boundary declaration,
not an audit verdict. A prior independent audit of the unconditional
framing found that the load-bearing Poisson equation was supported only
by a cited authority itself conditional on a stipulated `L^{-1}=G_0`
closure identity. This scope narrowing implements that audit's repair
target: narrow the note to a bounded theorem conditional on the named
admissions below.
**Primary runner:** [`scripts/frontier_distance_law_definitive.py`](./../scripts/frontier_distance_law_definitive.py)
is numeric support for the distance-law scaling after the named
admissions are supplied. Legacy "closure" wording in runner output is
not load-bearing; this source note's three-admission boundary controls
the claim.

## 2026-05-28 Audit Repair (register the test-mass force coupling)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The BA-2 Green normalization dependency is now retained-bounded, but
> BA-1 remains a stipulated closure/equation-of-motion input via
> gravity_full_self_consistency_note rather than a retained derivation
> from the framework axiom. The no-go/admission discipline hidden-wall
> scan also exposes an unregistered force/test-mass coupling step,
> F=-M_test grad(phi)."*

Two things are addressed:

1. **BA-1 stays an explicitly admitted premise**, not a retained
   derivation. The note already records (BA-1) as conditional on the
   `L^{-1}=G_0` closure supplied by `gravity_full_self_consistency_note`;
   this revision reaffirms that BA-1 is an admitted input, not a
   framework-axiom derivation. (Supplying a retained equation-of-motion
   derivation for BA-1 is substantive new work, out of scope here.)
2. **The previously-unregistered force/test-mass coupling step
   `F = −M_test ∇φ` is now registered as a third named admission
   (BA-3) below.** The auditor's hidden-wall scan correctly flagged that
   the inverse-square *force* law (as opposed to the `1/r` potential)
   consumes a test-mass response rule that was not in the BA-1/BA-2
   admission list.

The load-bearing claim is therefore the **conditional worked example**:
GIVEN the three named admissions (BA-1) lattice Poisson EoM, (BA-2)
retained `Z³` Green normalization, and (BA-3) test-mass force coupling,
THEN the inverse-square force law follows as class-A algebra/calculus.
None of BA-1 / BA-3 is derived from the framework axiom here. No new
axiom, import, or retained bridge is introduced by this repair.

## Bounded admissions

The load-bearing claim is **conditional on the three bounded admissions**
below. None is derived in this note; each is admitted as a named input.
The `1/r` potential closes class-A algebraically from (BA-1) plus (BA-2)
plus elementary calculus on `Z^3`; the inverse-square *force* law
additionally consumes (BA-3).

(BA-1) **Lattice Poisson equation as equation of motion.** The
staggered scalar field obeys

```text
(-Delta_lat) phi = rho                                                    (BA-1)
```

on the `Z^3` spatial substrate. The identification with the equation of
motion of the canonical staggered scalar action is currently bounded by
the `L^{-1} = G_0` self-consistency closure supplied in
[`GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md);
the present note admits (BA-1) and does not re-derive it.

(BA-2) **Maradudin et al. 1971 lattice Green's function asymptotic.**
The Green's function of the lattice Laplacian on `Z^3` satisfies

```text
G(r) = (-Delta_lat)^{-1}(r)  ->  1 / (4 pi |r|)    as |r| -> infinity.   (BA-2)
```

This is a standard result of lattice potential theory (Maradudin,
Montroll, Weiss, *Theory of Lattice Dynamics in the Harmonic
Approximation*, 1971; also Spitzer, *Principles of Random Walk*,
§29; Lawler, *Intersections of Random Walks*, §1.5). Recorded as a
framework-applied `Z^3` graph-Laplacian normalization certificate via
[LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md);
the coefficient is not re-derived in this note.

(BA-3) **Test-mass force/source coupling.** A test mass `M_test` in the
scalar potential `phi` experiences the force

```text
F = -M_test grad(phi)                                                    (BA-3)
```

This Newtonian test-mass response rule is the step that converts the
`1/r` potential `phi(r) ~ M / (4 pi r)` (from BA-1 + BA-2) into the
inverse-square *force* `|F| ~ M_test M / (4 pi r^2)`. It is a named
admitted input, not derived from the framework axiom in this note.
(Registered 2026-05-28 per the audit hidden-wall scan, which correctly
flagged it as the previously-unregistered force/test-mass coupling
step.)

(BA-1), (BA-2), and (BA-3) are the only bounded admissions. Conditional
on those three admissions, the remaining calculation of Newton's
inverse-square law is class-A algebra/calculus and needs no further
import.

## Theorem / Claim (conditional on BA-1, BA-2, BA-3)

**Theorem.** Given (BA-1), (BA-2), and (BA-3), let `(-Delta_lat)` be the
lattice Laplacian on `Z^3`. Then:

1. The Green's function G(r) of (-Delta_lat) satisfies
   G(r) -> 1 / (4 pi |r|) as |r| -> infinity, by (BA-2).

2. A point source of strength M produces potential
   phi(r) = M * G(r) -> M / (4 pi r), by linearity of (BA-1).

3. The force on a test mass M_test is F = -M_test * grad(phi) = M * M_test / (4 pi r^2)
   by the admitted test-mass coupling (BA-3),
   which is the conditional inverse-square force law with
   G_N = 1/(4 pi) in lattice units.

4. The product M1 * M2 arises from two independent Poisson solves with
   cross-coupling. It is computed from Poisson linearity (BA-1), not
   imposed as a bilinear ansatz.

5. The exponent 2 in 1/r^2 equals d - 1 = 3 - 1, where d = 3 is
   the spatial dimension of the `Z^3` spatial substrate. In general d
   dimensions, the Poisson Green's function plus the admitted test-mass
   response rule gives F ~ 1/r^{d-1}.

## Assumptions

1. **Framework baseline:** the one-qubit operator algebra on the
   `Z^3` spatial substrate.
2. **(BA-1):** The staggered scalar field obeys the lattice Poisson
   equation `(-Delta_lat) phi = rho` (admitted; not derived here; see
   §"Bounded admissions" above).
3. **(BA-2):** Maradudin asymptotic theorem for the lattice Green's
   function (admitted as textbook math input; not derived here).
4. **(BA-3):** Test-mass force coupling `F = -M_test grad(phi)`
   (admitted Newtonian response rule; not derived here; registered
   2026-05-28 per the audit hidden-wall scan).

No additional physics is imported beyond (BA-1), (BA-2), and (BA-3).
Under those admissions, the coupling constant G_N, the product law, the
inverse-square exponent, and the distance dependence all follow as
class-A consequences.

## What Is Actually Proved

**Exact results (mathematical theorems):**

- The lattice Laplacian Green's function on Z^3 converges to 1/(4 pi r)
  for large r. This is a theorem of lattice potential theory.
- Poisson linearity: phi(M) = M * phi(1) exactly.
- The potential is linear in source strength by Poisson linearity. The
  force product law F ~ M_source * M_test follows after the admitted
  test-mass force coupling (BA-3).
- The force exponent d - 1 follows from the dimension of the Poisson
  equation plus (BA-3). In d = 3: F ~ 1/r^2 conditionally.

**Numerical confirmations (bounded checks):**

- Green's function ratio 4 pi r G(r) -> 1.0 confirmed to < 1% for r >= 5
  on a 64^3 lattice.
- Deflection exponent alpha -> -1.0 confirmed to < 5% on 32^3 to 64^3
  lattices (consistent with sub-1% at 128^3 from frontier_distance_law_definitive.py).
- Product law gamma = 1.0 confirmed to < 5% on 32^3 lattice.
- Dimensionality check: d=1 (constant force), d=2 (1/r force), d=3 (1/r^2 force)
  all confirmed numerically.

## What Remains Open

This note does not remove the bounded admissions. The open pieces are
exactly the independently auditable status of:

- (BA-1): the Poisson equation as the equation of motion on the
  intended lattice field surface.
- (BA-2): the admitted lattice Green's-function asymptotic as the
  external textbook input used here.
- (BA-3): the admitted test-mass force coupling
  `F = -M_test grad(phi)`.

Once (BA-1), (BA-2), and (BA-3) are admitted, the product law and
exponent are not additional open assumptions; they are consequences of
linearity, the `d = 3` Poisson Green's-function asymptotic, and the
test-mass response rule. The finite-lattice numerical checks remain
verification support, not theorem authority.

## How This Can Be Used

This derivation can be used as a bounded worked example of how a
macroscopic force law follows after the three admissions are supplied:

> The inverse-square gravitational force law F = G M1 M2 / r^2 is a
> consequence of the admitted lattice Poisson equation on `Z^3` plus the
> admitted lattice Green's-function asymptotic plus the admitted
> test-mass force coupling. The potential's source dependence emerges from
> Poisson linearity; the force product M1 M2 then uses BA-3. The exponent
> 2 = d - 1 follows from the spatial dimension d = 3.

This does not claim an unconditional closure from the framework baseline
alone. The overall coupling normalization and the three bounded admissions
remain explicit.

This is a bounded weak-field gravity claim pending independent audit of
the narrowed source and its dependency chain. Broader GR-signature notes
(WEP, time dilation, light bending, geodesics, strong-field extension)
should still be carried separately with their actual bounded status.

## Commands Run

```bash
cd /Users/jonreilly/Projects/Physics
python3 scripts/frontier_newton_derived.py
```

## Supporting Evidence

The distance law and product law have been independently verified at
higher precision in:

- `scripts/frontier_distance_law_definitive.py` (sub-1% at 128^3)
- `scripts/frontier_product_law_no_ansatz.py` (product law without bilinear ansatz)
- `scripts/frontier_dm_coulomb_from_lattice.py` (Green's function theorem + numerics)

This note synthesizes those results into a single derivation chain.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [gravity_full_self_consistency_note](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
  — supplies the `L^{-1} = G_0` self-consistency closure that justifies
  treating `(-Delta_lat)` as THE field operator (Theorem assumption 2:
  the lattice Poisson equation is the equation of motion). Correct
  upstream.

### Direction-corrected cycle break (2026-05-05)

The earlier link to `gravity_clean_derivation_note` is removed because
gravity_clean is a **parallel presentation** of the same Newton-from-Z^3
derivation, not an upstream supplier. Both this note and gravity_clean
independently consume the Maradudin et al. 1971 lattice Green's function
asymptotic theorem (an external math theorem, not an internal repo dep).
Neither note derives the other's content; they are alternate conditional
routes to `F = G_N M_1 M_2 / r^2` on the `Z^3` spatial substrate.

The earlier back-link from this note to gravity_clean was added by a
prior audit-bookkeeping pass and created a length-2 citation cycle
`newton_law ↔ gravity_clean` in the graph. Removing the back-link breaks
the cycle without losing science content (the inline mathematical
justification — Maradudin's theorem — remains in the Theorem section).
