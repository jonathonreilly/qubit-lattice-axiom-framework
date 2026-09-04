# Defect Closure Is Necessary on the Tested Single-Plaquette Family: the Sector-Stability Obstruction Is Exactly the Defect-Shift Linking Pairing and Is Defect-Supported (Bounded Theorem)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite identity plus a necessity
statement on the tested family; not a terminal no-go).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Current-main posture (2026-07-07):** theta's Tier-A admission is already
retired on main by the retained 2026-07-05 retirement decision. This note is
banked only as bounded historical/supporting science for the defect-closure
escape route; it does not reopen, modify, or supply authority for that
retirement record.
**Primary runner:**
[`scripts/theta_defect_closure_necessity_linking_obstruction_2026_07_02.py`](../scripts/theta_defect_closure_necessity_linking_obstruction_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_defect_closure_necessity_linking_obstruction_2026_07_02.txt`](../logs/runner-cache/theta_defect_closure_necessity_linking_obstruction_2026_07_02.txt)

## Question

The landed 4D carrier note (PR #4811) proved the flux-sector structure and
the cross-plane charge exist exactly on the closed-branch subsurface
(`dn = 0`) of `T^4`, with an explicit witness that branch defects destroy
class-invariance of the cup square. The campaign's residual (i-a) asked for
the defect-closure derivation. Question answered here: is closure merely
sufficient for sector structure, or necessary — and what exactly is the
obstruction when a defect is present?

## Answer

Three exact results on `T^4` at `L = 2` (runner 7/7; the identity's sign
pattern is derived from the data by four-way discrimination, not assumed —
and the derived pattern corrected a sign-parity slip in the dispatch spec's
own sketch, documented in the runner):

1. **The obstruction is exactly a linking pairing.** For an integer branch
   2-cochain `n` with defect current `J = dn` and any exact shift
   `n -> n + d lambda`:

   ```text
   Delta(lambda) := Q_raw(n + d lambda) - Q_raw(n)
                  = - sum(J u lambda) + sum(lambda u J),
   ```

   with `sum(d lambda u d lambda) = 0` confirmed on every trial. The
   identity follows from the pinned Leibniz convention
   (`d(a u b) = da u b + (-1)^p a u db`, verified exactly) applied to the
   two cross terms; the `(-,+)` sign pattern is the unique one of four that
   matches all 36 (open-`n`, `lambda`) trials (runner A1-A2, B1). For
   closed `n` the change vanishes identically, with the discriminating
   contrast that the same shifts move open cochains (B2).

2. **Necessity.** Every nonzero single-plaquette defect current (one per
   plane) admits a unit-link `lambda` with `|Delta| >= 1` (runner C1): on
   the tested family, sector structure — a branch-move-invariant charge —
   exists **iff** `dn = 0`. The landed sufficiency is thereby upgraded to
   an equivalence on this family.

3. **The obstruction is defect-supported.** For a fixed single-plaquette
   defect, a nearby unit-link shift produces `Delta = -1` while a maximally
   distant one produces `Delta = 0` (runner C2): the linking pairing is
   local to the defect, as its form requires. The closed-subfamily
   arithmetic (`Q = Q_raw/2` = the intersection form) is re-earned in the
   same conventions (D1).

**Consequence for (i-a).** The defect-closure residual is now two-sided on
the tested single-plaquette family: closure is not a convenience assumption
for this sector construction but the observed boundary of sector existence.
Any derivation of the sector-record surface must either supply `dn = 0`
(as constraint or suppression) or explain why the local linking obstruction
does not apply. The obstruction's exact form (a local pairing with `J`) is
the quantitative target any suppression mechanism must beat.

## Source surface (named authorities)

**Record axiom** (approved axiom node `minimal_axioms`,
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)) —
background discipline only; record occurrence is not claimed. The cochain
machinery conventions are those of the landed 4D carrier runner, re-earned
inline (dd = 0; Leibniz pinned; flux representatives re-verified closed).
No unaudited note is consumed as a premise. No external comparator,
measured value, fitted number, or Monte Carlo enters anywhere.

## What moves

| Prior state | After this note |
|---|---|
| defect closure sufficient for sectors (landed); necessity open | equivalence on the tested single-plaquette family: sectors exist iff `dn = 0` |
| defect breakdown witnessed by value-instability (landed) | the instability identified exactly: `Delta = -sum(J u lambda) + sum(lambda u J)`, sign derived by discrimination |
| (i-a) as an assumption to justify | (i-a) as a quantitative target: any closure/suppression mechanism must control a local linking pairing with `J` |

## What remains

```text
(i-a residual): derive the closure constraint or the suppression of
    defect-carrying branches from the framework surface (the necessity
    theorem shows the tested sector construction cannot avoid it); whether
    the Admissibility axiom bears on it remains an open question, not
    asserted.
```

## Non-claims

This note does not claim: Strong-CP closure or theta retirement; a
derivation of defect suppression (that is the residual); extension of the
necessity statement beyond the tested family (single-plaquette defect
currents on `T^4_2` with unit-link and random shifts); that records
register any object here; any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**Gate result:** bounded scoping only. Negative content: with `dn != 0` in
the tested single-plaquette family, the
cup-square is not branch-move invariant, quantitatively by the linking
identity; every tested nonzero defect is obstructed.

**N1 routes:** unrestricted branch sums — obstructed (this note, exact);
closed-branch surface — the landed positive; suppression mechanisms — open
(the residual); defect-relative sector data (charges defined modulo the
linking pairing) — logically open, named, not pursued.
**N2:** binds nothing on the mass side or assembly; scoped to the branch
calculus. **N3:** the sign pattern is derived by four-way discrimination;
the spec-sketch parity slip is documented in the runner; locality is
witnessed, not assumed. **N4:** consumes the campaign's (i-a) and returns
it sharpened; matches the landed carrier note's defect witness exactly.
**N5:** no closure rhetoric; the family scope is stated. **N6:** live
paths: constraint-level closure from the framework surface; dynamical
suppression; defect-relative sector data. **N7:** steelman — "linking
obstructions for defects are classical": the deliverable is the exact
finite identity in audit format with derived signs and the necessity scan,
wired to (i-a). "The family is small": stated; single-plaquette currents
generate the local defect geometry at `L = 2`. **N8:** echo guard — do not
re-attack unrestricted-sum sectors (now two-sided); check Leibniz
p-parities before trusting any cochain-identity sketch (the spec slip).

## Verification

Run:

```bash
python3 scripts/theta_defect_closure_necessity_linking_obstruction_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=7 FAIL=0
```

Sections: A machinery ground (dd = 0; Leibniz convention pinned); B the
linking identity (four-way sign discrimination over 36 trials; telescoping
term zero; closed contrast); C necessity (all six planes obstructed at
unit-link level; locality witness); D closed-subfamily intersection-form
arithmetic.
