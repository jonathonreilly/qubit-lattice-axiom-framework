# Scalar-Trace-Only Tensor Completion No-Go

**Date:** 2026-04-14 (2026-05-18: claim_scope formalized as conditional
diagnostic on the imported `O_h` and finite-rank classes per audit
verdict boundary instruction; 2026-06-16: source/cache packet repair for
the three load-bearing helper modules).
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-18 narrowing):** the load-bearing content
of this note is **a valid conditional diagnostic** ruling out scalar-
only completion on the **imported `O_h` and finite-rank source classes**
that the runner consumes — given the imported boundary functional,
probe families, and Einstein-residual computation as inputs (each
wrapped by helper notes per PR #1520), the constructed probes show
scalar boundary data is unchanged while the tensorial Einstein
channels are active. This **is NOT** a retained-grade no-go: the
conditional diagnostic depends on the imports being correct, and the
class of scalar-only completions ruled out is restricted to those
factoring through the imported scalar boundary data. The audit
verdict's repair sub-target ("attach retained-grade notes/dependency
edges for the three imported runner authorities, or inline their
scalar-functional, probe-family, and Einstein-residual constructions")
is partially answered by the helper-note wrappers added in PR #1520;
making the no-go itself retained-grade requires those helper-note
wrappers to themselves be retained, which remains separate open work.
**Script:** `scripts/frontier_scalar_trace_tensor_nogo.py`
**Helper source/cache packet:** `scripts/scalar_trace_tensor_helper_packet_2026_06_16.py`
**Helper packet cache:** `logs/runner-cache/scalar_trace_tensor_helper_packet_2026_06_16.txt`
**Status:** exact scalar-data degeneracy plus bounded tensor-channel witness

**Status authority and audit hygiene (2026-05-10):**
The audit lane has classified this note `audited_conditional`. The
algebraic implication itself is sound — a map that factors only through
identical scalar boundary data cannot distinguish completions whose
tensorial Einstein channels differ — but the runner delegates the
construction of the boundary functional, the probe families, and the
Einstein-residual computation to upstream helper modules. The
2026-06-16 repair makes those helper modules static imports and adds a
source/cache packet runner for their current source files and cached outputs.
Audit verdict and effective status are set by the independent audit lane only;
nothing in this rigorization edit promotes status.

## Purpose

The current gravity branch already has a real restricted strong-field package:

- exact shell source
- exact same-charge bridge
- exact local static-conformal lift
- exact microscopic Schur boundary action
- exact microscopic Dirichlet principle
- exact restricted discrete Einstein/Regge lift

The remaining gap is no longer “find a better scalar bridge.” The real
question is narrower:

> can any completion principle that depends only on the current scalar shell
> trace / Schur boundary data determine the full `3+1` metric?

This note answers that sharply.

## Exact statement

On the current branch, the microscopic boundary functional is scalar:

- it depends only on the shell trace `f`
- equivalently, only on the Schur-complement scalar boundary data

The tensorial completion probes already added on the branch keep that scalar
boundary data fixed by construction while turning on:

- a shift-vector mode
- a traceless spatial shear mode
- a mixed vector+tensor mode

Therefore any purported completion principle that factors only through the
current scalar shell trace / Schur data must assign the same output to all of
those probes.

That is the exact degeneracy.

## Tensorial witness

The companion verifier evaluates the full `3+1` Einstein tensor on those probes.

Result:

- the scalar boundary action is unchanged across the scalar, vector, tensor,
  and mixed perturbations on both the exact local `O_h` and finite-rank
  source classes
- but the tensorial Einstein channels are not unchanged
  - vector perturbations activate independent `G_{0i}` residuals
  - traceless shear perturbations activate independent traceless
    `G_{ij}` residuals
  - mixed perturbations activate both

So the scalar data are insufficient to determine the full `3+1` metric.

## Why this is a no-go theorem

This is not just a bounded “the scalar bridge is incomplete” statement.

It is a genuine no-go for a whole class of hoped-for completions:

> no completion principle that factors only through the current scalar shell
> trace / Schur boundary data can determine the full `3+1` metric on this branch.

Equivalently:

> the remaining gravity gap cannot be closed by another scalar repackaging of
> the existing microscopic boundary action.

The next principle, if it exists, must be genuinely tensor-valued.

## What this closes

This closes one more tempting escape hatch:

1. the gravity gap is **not** hidden inside another scalar bridge channel
2. the gravity gap is **not** hidden inside the current scalar shell action
3. the gravity gap is **not** merely a better scalar completion of the same
   shell data

## What still remains open

This still does **not** close:

1. a genuinely tensor-valued microscopic matching / completion law
2. full nonlinear GR in full generality

## Practical conclusion

The gravity search space is now much tighter:

- restricted strong-field closure is real
- restricted Einstein/Regge lift is real
- broader support-class widening is real
- scalar-only completion is now sharply ruled out by the witness
  construction — conditional on the imports below being correct

So the only honest positive route left is a new tensor-valued matching law
beyond the current scalar shell data.

## Imported authorities

The companion runner `scripts/frontier_scalar_trace_tensor_nogo.py`
loads its scalar boundary functional, probe families, and Einstein
residual computations from three upstream modules as ordinary static
Python imports, so the restricted audit helper packet can inspect the
load-bearing source edges:

| Imported module | Role in the no-go witness | Wrapper note |
|---|---|---|
| [`scripts/frontier_tensorial_einstein_regge_completion.py`](../scripts/frontier_tensorial_einstein_regge_completion.py) | constructs the vector-shift, traceless-shear, and mixed probe families and computes their `G_{0i}` and traceless `G_{ij}` Einstein residuals | [TENSORIAL_EINSTEIN_REGGE_COMPLETION_PROBE_HELPER_NOTE_2026-04-14.md](TENSORIAL_EINSTEIN_REGGE_COMPLETION_PROBE_HELPER_NOTE_2026-04-14.md) |
| [`scripts/frontier_same_source_metric_ansatz_scan.py`](../scripts/frontier_same_source_metric_ansatz_scan.py) | builds the exact local `O_h`-symmetric `phi` grid against which scalar-data invariance is verified | [ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md](ONE_PARAMETER_REDUCED_SHELL_LAW_HELPERS_UMBRELLA_NOTE_2026-04-13.md) (`same_source_metric_ansatz_scan` row of the helper-wrapper registry only; not a derivation of that helper) |
| [`scripts/frontier_coarse_grained_exterior_law.py`](../scripts/frontier_coarse_grained_exterior_law.py) | builds the finite-rank `phi` grid on which the same scalar-data invariance is independently verified | [COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md](COARSE_GRAINED_EXTERIOR_LAW_HELPER_NOTE_2026-04-14.md) |

These modules are imported authorities for this bounded witness. Each
of the three runner-imported helpers now has a citeable one-hop
helper-wrapper registry authority via the wrapper-note column above
(added 2026-05-17); no helper derivation is imported from that wrapper. The
audit-conditional status of this no-go reflects the bounded-helper-
character of those wrappers, not a defect in the algebraic argument.
Promoting any helper wrapper itself to a stronger upstream tier is a
separate audit-lane question.

## 2026-06-16 source/cache packet repair

The primary no-go runner now exposes the three load-bearing helper modules as
static imports rather than dynamic `_frontier_loader` imports:

```python
import frontier_tensorial_einstein_regge_completion as tcomp
import frontier_same_source_metric_ansatz_scan as same_source
import frontier_coarse_grained_exterior_law as coarse
```

The helper packet runner
`scripts/scalar_trace_tensor_helper_packet_2026_06_16.py` checks:

- the three helper source files exist and expose the exact functions consumed
  by the no-go runner;
- the helper caches in `logs/runner-cache/` are present, SHA-fresh, exit
  cleanly, and contain passing output;
- the primary no-go runner contains the three static imports above.

This repairs the runner-packet artifact issue by making source and cache
evidence explicit. It does not set an audit verdict and does not broaden the
no-go beyond the stated scalar-functional/probe-family surface.

## Audit-aware repair path

Per `audit_ledger.json`, `notes_for_re_audit_if_any` for
`scalar_trace_tensor_no_go_note`: the cheapest path to a stronger audit
verdict is to attach retained-grade cited notes for the three modules
listed above, include their full load-bearing source/cache packet, or inline
the construction of the scalar functional, the probe families, and the Einstein
residual computation directly in the runner. The 2026-06-16 source/cache
packet implements the source/cache path; independent re-audit must decide
whether that is sufficient for the row's effective status.

The re-audit packet also includes cached outputs for the helper runners
where they are executable:

- `logs/runner-cache/frontier_tensorial_einstein_regge_completion.txt`
- `logs/runner-cache/frontier_same_source_metric_ansatz_scan.txt`
- `logs/runner-cache/frontier_coarse_grained_exterior_law.txt`
- `logs/runner-cache/frontier_scalar_trace_tensor_nogo.txt`

## Boundaries

This note does not close:

- a positive tensor-valued microscopic matching / completion law;
- full nonlinear GR;
- any retained-grade promotion of the imported probe-family or
  Einstein-residual modules listed above;
- any chain closure beyond the explicit scalar-data degeneracy plus
  the bounded tensor-channel witness reported by the runner.
