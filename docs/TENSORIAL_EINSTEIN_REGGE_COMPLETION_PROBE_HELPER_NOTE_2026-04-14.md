# Tensorial Einstein-Regge Completion Probe Helper Module

**Date:** 2026-04-14 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded helper-module wrapper for the vector-shift,
traceless-shear, and mixed probe families plus their `G_{0i}` and
traceless `G_{ij}` Einstein-residual computation used by the
scalar-trace-tensor no-go witness.
**Status authority:** independent audit lane only. This wrapper note
is audit-lane infrastructure for the corresponding helper module.
**Primary runner:** `scripts/frontier_tensorial_einstein_regge_completion.py`

## 2026-05-29 Packet-Completeness Repair

The conditional audit blocker was a runner packet issue, not a new tensorial
physics premise: the primary runner loaded the scalar-field helper modules
through `_frontier_loader`, so the restricted audit packet exposed only the
top-level stdout plus the dynamic loader. This made the same-source scalar
field and an unused microscopic-Dirichlet helper look like opaque runtime
premises.

This repair keeps the bounded tensorial-probe claim unchanged and makes the
load-bearing helper sources explicit:

- the runner now statically imports `frontier_same_source_metric_ansatz_scan.py`,
  `frontier_coarse_grained_exterior_law.py`, and
  `frontier_oh_schur_boundary_action.py`;
- the unused dynamic `frontier_microscopic_dirichlet_bridge_principle.py` load
  was removed from the tensorial probe runner;
- the existing retained-bounded dependency links to the coarse-grained
  exterior helper and the O_h Schur boundary action remain the only theorem
  dependencies.

No new axiom is introduced. No full Einstein/Regge completion, nonlinear GR
closure, all-source theorem, or framework-level tensor-matching theorem is
claimed here.

## Purpose

This wrapper note documents the tensorial Einstein-Regge completion
probe helper module so downstream notes (notably
`SCALAR_TRACE_TENSOR_NO_GO_NOTE.md`)
can register a one-hop dependency rather than carry the helper as an
unattributed Python `_frontier_loader.load_frontier(...)` runner
import. The downstream cite is backticked: the load-bearing citation
direction is *no-go → this helper*, not vice versa; the helper
imports no content from the no-go.

## What this module provides

The helper module constructs three tensorial probe families:

- **Vector-shift probes:** activate independent shift-vector
  components of the `3 + 1` metric perturbation while keeping the
  scalar shell trace fixed.
- **Traceless-shear probes:** activate independent traceless spatial
  shear modes of the metric perturbation while keeping the scalar
  shell trace fixed.
- **Mixed vector+tensor probes:** activate combined shift-vector and
  traceless-shear modes while keeping the scalar shell trace fixed.

For each probe, the helper computes the full `3 + 1` Einstein tensor
components on the perturbed metric and reports:

- the `G_{0i}` mixed time-space residual (active under vector
  shifts);
- the traceless `G_{ij}` spatial residual (active under traceless
  shears);
- the combined residual on mixed probes.

## What this is used for

In the scalar-trace-tensor no-go witness, this probe machinery is the
load-bearing object: the scalar boundary action is verified to be
unchanged across all three probe families, while the Einstein tensor
channels are verified to be **active** on the vector and shear
channels. The contrast between "scalar action unchanged" and "Einstein
channel active" is what gives the no-go its strength.

## Boundary

This wrapper note records the bounded helper-module character of the
tensorial Einstein-Regge completion probe module. It does not claim:

- a framework-level derivation of the probe families or the Einstein
  tensor formula from `Cl(3)` on `Z^3` axioms;
- a positive Einstein/Regge identification of the scalar-generator
  Hessian (this is exactly what the no-go forecloses for scalar-only
  completions);
- closure of any downstream gravity theorem.

Its only function is to provide a citeable one-hop authority for the
probe families and Einstein-residual computation so downstream notes
register the import cleanly instead of carrying it as a
`_frontier_loader` runner import without a wrapper.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [coarse_grained_exterior_law_helper_note_2026-04-14](COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md)
- [oh_schur_boundary_action_note](OH_SCHUR_BOUNDARY_ACTION_NOTE.md)
