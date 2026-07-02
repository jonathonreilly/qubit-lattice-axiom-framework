# One-Parameter Reduced Sewing-Shell Law (Bounded Finite Replay)

**Date:** 2026-04-13 (2026-05-18: claim_scope formalized as conditional
bounded witness on the imported reduced-shell surface per prior audit
boundary instruction; 2026-06-16: audit-packet helper-source
repair and source/cache packet recorded, with no status promotion;
2026-06-17: self-contained finite replay added, still with no status
promotion)
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-18 tightening):** the load-bearing content
of this note is **a conditional bounded witness on the imported
reduced-shell surface**. The current primary path uses the
self-contained finite-operator replay added on 2026-06-17; the five
older helper modules (star_shell_projector,
same_source_metric_ansatz_scan, coarse_grained_exterior_law,
sewing_shell_source, radial_shell_matching_law; all wrapped via
ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md
as a helper-wrapper registry only in PR #1520) remain
historical/provenance context rather than opaque live imports in the
primary runner. On that bounded reduced surface, the seven
star-support point-Green columns reproduce the reduced one-parameter
law to machine precision on the finite replay
`sigma_red(Q) = Q · (k_rad + c_aniso · m_orb)` with
`c_aniso = 0.081435402995901`, and the two admitted source-family
comparators (local O_h, finite-rank) match this law to machine
precision. This
is **NOT retained gravity closure**: the umbrella helper wrapper
remains bounded; full nonlinear shell-stress / junction
interpretation and the lift from reduced orbit/shell-mean data to
the full 4D spacetime theorem are explicitly out of scope and remain
the named open work. The prior audit repair sub-target ("wire
retained-grade authority notes for the five imported helper modules,
OR inline their operator/source constructions so the bounded
one-parameter law is self-contained from the axiom alone") is
partially answered by the self-contained replay and the umbrella
wrapper from PR #1520, but neither performs independent audit signoff
or promotes the helper surface to retained authority.
**Status authority:** independent audit lane only.
**Script:** `scripts/frontier_one_parameter_reduced_shell_law.py`
**Helper source/cache packet:** `scripts/one_parameter_shell_helper_packet_2026_06_16.py`
**Helper packet cache:** `logs/runner-cache/one_parameter_shell_helper_packet_2026_06_16.txt`
**Self-contained replay:** `scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py`
**Self-contained replay cache:** `logs/runner-cache/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.txt`
**Status:** Bounded reduced-shell finite replay plus bounded shell-stress interpretation

## Purpose

The gravity line had already established:

- the radial DtN shell kernel is fixed on the reduced finite shell surface
- the anisotropic shell sector is one reduced DtN mode on that surface

That still left one genuine open question:

> is the amplitude of that anisotropic mode an additional free datum, or is it
> already fixed by the microscopic source law on the current constructed source class?

This note answers that question on the reduced shell surface.

## Machine-Precision One-Parameter Replay

Take the seven star-support point-Green columns and compute their
finite-lattice sewing-shell source at cutoff `R = 4`.

For each unit-charge point column, the script finds:

- the same radial shell kernel per unit charge
- the same anisotropic orbit-mode vector per unit charge
- the same shell-mean exterior response per unit charge

Within the finite replay, the exterior projector, lattice Laplacian, and Green
solve give the bounded support statement:

> on the reduced shell surface, the sewing-shell law is fixed entirely by total
> charge `Q`

Equivalently,

`sigma_red(Q) = Q * (k_rad + c_aniso * m_orb)`

where, on this finite reduced surface:

- `k_rad` is the replayed radial DtN shell kernel
- `m_orb` is the replayed reduced anisotropic DtN mode
- `c_aniso` is the computed finite-lattice constant

The script finds:

`c_aniso = 0.081435402995901`

so the anisotropic anchor amplitude obeys

`A_aniso = c_aniso * Q`

with no extra family-dependent parameter on this reduced surface.

## Machine-Precision Agreement With Current Source Families

The script then checks the two admitted source-family comparators already used
in the gravity line:

1. the local `O_h` family
2. the broader finite-rank family

and finds machine-precision agreement with the same reduced one-parameter law.

So the current admitted source-family comparators are not introducing an additional
independent anisotropic amplitude. They realize the same charge-fixed reduced
shell law already latent in the star-support DtN problem.

The local `O_h` constants, finite-rank base/correlation/scaling, and finite-rank
masses are admitted current source-family definitions copied into the replay
from the prior helper path. They are not observational inputs, fitted target
values, retained authorities, or axiom-derived selectors.

## Interpretation

This is the cleanest strong-field gravity statement so far about the sewing
shell:

> on the reduced surface relevant to the current gravity program, the finite
> replay supports one isotropic shell-density kernel plus one cubic shear mode,
> both tied to the same scalar charge

That is still not full nonlinear GR, but it removes one more degree of freedom
from the matching problem.

## What this narrows

This narrows another real ambiguity on the finite reduced replay:

> on the current constructed star-supported source class, the anisotropic
> shell-mode amplitude is not an extra independent parameter in the replay; it
> is tied to total charge to machine precision

## What this still does not close

This note still does **not** close:

1. the full shell-stress / junction interpretation of the reduced shell law
2. the lifting from reduced orbit/shell-mean data to the full nonlinear 4D
   spacetime theorem
3. the final Einstein/Regge closure

## Updated gravity target

After this note, the gravity target tightens again:

- the reduced sewing-shell law is now replayed as one-parameter on the finite
  surface
- the remaining blocker is no longer the radial kernel, the anisotropic mode,
  or its amplitude
- the remaining blocker is the nonlinear shell-stress / junction
  interpretation that lifts this bounded reduced shell law into the full 4D
  closure

## Audit dependency repair links

This graph-bookkeeping section records the explicit upstream operators
the load-bearing linearity step relies on, in response to the
2026-05-05 audit repair target for a missing dependency edge
(audit row: `one_parameter_reduced_shell_law_note`). It does not
promote this note or change the audited claim scope, which remains the
linearity-from-identical-normalized-columns argument plus the two
source-family checks at cutoff `R = 4`.

Before the 2026-06-17 self-contained replay repair, the runner
`scripts/frontier_one_parameter_reduced_shell_law.py` imported five frontier
helper modules as static Python imports:

- `frontier_star_shell_projector.py` — exterior projector and
  shell-mean operator.
- `frontier_same_source_metric_ansatz_scan.py` — source-family
  constructors (the local `O_h` family and the broader finite-rank family
  checked in §"Machine-Precision Agreement With Current Source Families").
- `frontier_coarse_grained_exterior_law.py` — coarse-grained exterior
  law on the truncated star.
- `frontier_sewing_shell_source.py` — sewing-shell projection at
  cutoff `R = 4`.
- `frontier_radial_shell_matching_law.py` — radial shell kernel
  `k_rad` and the radial-shell average operator.

The current primary runner now uses the self-contained 2026-06-17 replay module
for these finite operator/source constructions instead of importing the five
helper modules directly. The list above remains the historical/provenance
surface whose constructions are inlined by the replay, not a set of opaque
load-bearing imports in the current primary runner.

The helper packet runner
`scripts/one_parameter_shell_helper_packet_2026_06_16.py` checks that
the five helper source files exist, expose the functions consumed by the
legacy helper-path runner, have fresh runner caches under `logs/runner-cache/`,
exit cleanly, and report passing output.

None of these helper modules currently has a dedicated retained-grade
source note registered as a one-hop authority for this row. The recorded
repair issue is either a missing dependency edge or, if no retained
authority exists at all, a missing bridge theorem.

Open registration targets (class D gaps):

- A retained source note for the `star_shell_projector` exterior
  projector and shell-mean operator.
- A retained source note for the `same_source_metric_ansatz_scan`
  source-family constructors covering both the local `O_h` family
  and the broader finite-rank family.
- A retained source note for the `coarse_grained_exterior_law`.
- A retained source note for the `sewing_shell_source` projection at
  cutoff `R = 4`.
- A retained source note for the `radial_shell_matching_law` exact
  radial DtN shell kernel `k_rad` and the radial-shell average
  operator.

The five class-D registration targets now have a citeable one-hop
authority via the bounded umbrella wrapper added 2026-05-17:

- [ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md](ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md) — bounded umbrella wrapper documenting the five frontier helper modules above (exterior projector / source-family constructors / coarse-grained exterior law / sewing-shell projection / radial DtN kernel) so the citation graph carries an explicit one-hop edge.

The runner-checked content of this note (seven point-Green columns
carrying unit total charge to machine precision; identical radial
profile, identical orbit-mode vector, identical shell-mean
exterior response per unit charge across all seven; the resulting
reduced one-parameter law `sigma_red(Q) = Q * (k_rad + c_aniso *
m_orb)` with `c_aniso = 0.081435402995901`; machine-precision
agreement of the two admitted source-family comparators with the same one-parameter
law) is finite-lattice computation to machine precision on the constructed objects and is
independent of the registration status of the underlying helper
modules. The cite-chain repair simply records that those operators
and source families currently sit as runner-defined inputs rather than
independent retained-grade authorities, matching the prior repair target.

## Honest Repair Boundary

The prior repair finding observed that the runner produced classified passing
lines on the reduced shell calculation, but the load-bearing operators —
exterior projector, lattice Laplacian encoded in the Green solve,
source-family constructors, and the radial DtN shell kernel — were imported
from frontier modules that were not yet visible as a complete source/cache
packet and still were not certified as independent retained-grade authorities.
The repair target is either (a) wire those modules to retained authority notes,
or (b) recognize that no retained authority currently exists, in which case the
gap is a real missing bridge theorem. The explicit registration and helper
packet above make the source/cache evidence inspectable while preserving the
open authority question. Independent audit owns any downstream signoff.

## Scope of this rigorization

This rigorization is class D (gap registration and packet repair). It
does not change any algebraic content or load-bearing step
classification. The primary runner output remains `PASS=7 FAIL=0`; the
helper packet records the five frontier helper modules as provenance and open
one-hop dependency targets matching the prior audit repair's named missing
dependency edges. Mirrors the live cite-chain pattern used by the
`DM_NEUTRINO_SCHUR_SUPPRESSION_THEOREM_NOTE_2026-04-15.md` cluster
(commit `02ad4fadd`).

## 2026-06-16 audit-packet helper-source repair

The post-audit blocker on this row became narrower after the bounded
umbrella wrapper was retained: the remaining mechanical issue was that
the audit packet dependency resolver exposed only `_frontier_loader.py`
for this runner, so the restricted packet still treated the five
frontier helper modules as opaque dynamic imports.

The resolver repair exposed the helper source chain for dynamic loader
calls. The 2026-06-16 source/cache packet repair made the same helper surface
explicit through static imports and added fresh caches for the helper runners.
The 2026-06-17 primary runner no longer consumes that helper-import route, but
the provenance chain remains inspectable:

- `scripts/frontier_star_shell_projector.py`
- `scripts/frontier_same_source_metric_ansatz_scan.py`
- `scripts/frontier_coarse_grained_exterior_law.py`
- `scripts/frontier_sewing_shell_source.py`
- `scripts/frontier_radial_shell_matching_law.py`

and the transitive helper sources reached through those modules:

- `scripts/frontier_finite_rank_gravity_residual.py`
- `scripts/frontier_flux_fixed_matching_theorem.py`

This addendum is an audit-packet artifact repair only. It does not
promote the theorem, assert a retained derivation of the helper
operators, or alter the claim scope. A re-audit should now be able to
inspect the actual helper sources rather than treating the reduced-shell
operators as hidden runtime premises; the auditor still decides whether
that closes the runner-artifact issue or leaves a genuine retained
helper-authority gap.

## 2026-06-17 self-contained reduced-shell replay

The source packet now also includes
[`scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py`](../scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py).
This runner is a stronger audit-packet repair for the same blocker: it inlines
the finite Dirichlet negative-Laplacian, star-support point-Green columns,
local `O_h` source-family constructor, finite-rank source-family constructor,
exterior projection, shell-source extraction, radial averaging, and shell-mean
readout consumed by the primary bounded replay.

The self-contained replay has no `_frontier_loader` dependency and no imports
of the five contested helper modules. It independently recomputes the same
seven point-column checks, the same two source-family checks, and the same
registered reduced-shell constant
`c_aniso = 0.081435402995901`.

The primary runner `scripts/frontier_one_parameter_reduced_shell_law.py` now
uses this self-contained replay module as its finite-operator source while
preserving the original seven-check scorecard. This makes the audit packet's
primary path inspectable without following the old helper-import route.

This does not promote this row, does not add a new axiom or admission, and does
not claim retained nonlinear gravity closure. It only removes the avoidable
opaque-helper artifact from the re-audit packet: the remaining scientific
boundary is still the bounded reduced `R = 4` shell surface plus the open
nonlinear shell-stress / junction lift.

Verification:

```bash
python3 scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py
```

Expected scorecard: `PASS=10 FAIL=0 TOTAL=10`.
