---
actual_current_surface_status: no-go
target_claim_type: no_go
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact finite-dimensional calculation proves that the stated scalar corner-profile q/tau maps do not descend to the projected eigenoperator line."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: pass
---

# Claim Status Certificate

The candidate is an exact narrow no-go about the displayed maps on the
projected eigenoperator line, not a positive or negative theorem about every
physical PMNS carrier. It uses no observed or fitted PMNS values. The physical
carrier/inter-sector bridges are exposed as open and are not used in the proof.

## No-Go Discipline Gate

The executable evidence referenced below is the paired
[`frontier_pmns_commutant_eigenoperator_selector.py`](../../../../scripts/frontier_pmns_commutant_eigenoperator_selector.py)
runner.

### N1 — alternative routes

| Route against the no-go | Attempt | Result | Marker |
|---|---|---|---|
| Fix a trace-positive representative | Add `Tr M > 0` as the representative rule | this is a new normalization rule; the target note and runner instead start from an unoriented projected eigendirection. Evidence: [source, Obstruction 1](../../../../docs/PMNS_COMMUTANT_EIGENOPERATOR_SELECTOR_NOTE.md) and runner Part 3 | ATTEMPTED |
| Use a deterministic eigensolver sign | Treat a LAPACK/SVD sign as mathematical data | basis-vector signs in a degenerate singular space are implementation choices, not invariant input. The repaired runner removes this route by using an explicit witness and still tests `M` versus `-M` | ATTEMPTED |
| Replace the maps by sign-invariant formulas | Use absolute values or ratios of Fourier modes | these would be different maps, so they do not refute the no-go for the stated formulas. The exact ray `(2t/3,t/6,t/6)` is verified in runner Parts 1-2 | ATTEMPTED |
| Restrict the domain to an oriented carrier graph | Let a future physical carrier select one sign of each line | this can evade the no-go, but no such carrier theorem is in the current construction; it is the explicit reopen condition, not a counterexample on the current line domain | ATTEMPTED |
| Treat `M` rather than `[M]` as the supplied object | Declare an oriented matrix to be input data | this changes the theorem domain and makes the labels conditional on supplied orientation, not derived from the projected eigendirection | ATTEMPTED |
| Use a non-Hermitian eigenoperator phase | Let phase carry orientation | `M -> exp(i alpha) M` rotates the phase continuously unless a phase section is supplied, so the descent defect persists | ATTEMPTED |

N1 passes for the narrow claim. Each route is tested against the displayed
source theorem and paired runner. Matrix-valued enlarged observables and
carrier-constrained domains remain open and are explicitly outside the no-go.

### N2 — independence/collapse

The collapsed no-go wall set contains one item:

`W1`: the stated maps change under `M -> -M` and therefore do not descend to
the projected eigenoperator line.

With one wall, there is no pairwise wall table to populate. The cyclic and
reflection calculations are diagnostics, not additional no-go walls. The
passive and sector intertwiners are open positive bridge obligations, not
negative walls. No inflated independence count remains.

### N3 — hidden-wall scan

The revised proof was scanned for `assume`, `by construction`, `standard`,
`framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `registered`, and `canonical`. The only load-bearing inputs are
displayed matrices/projectors and displayed selector maps. Terms such as
"current construction" delimit scope and do not import authority. The
staggered corner Hamiltonians are explicitly displayed finite-matrix
conditions, not called four-axiom consequences. Corner-cycle/passive-offset
and corner-reflection/sector-exchange intertwiners are explicitly absent and
non-load-bearing. No hidden condition remains.

### N4 — residual matching

| Target/witness | Residual | Present residual | Match? |
|---|---|---|---:|
| [GOAL.md](GOAL.md), quoted archived audit target | specific Fourier-to-`q/tau` maps lack an internal theorem | whether those exact formulas are intrinsic to the projected eigendirection | yes, as target only |

No prior no-go is used as scientific evidence. The exact matrix proof and
runner are the evidence; the archived audit text only identifies the repair
target.

The archived audit residual identifies the target only; it is not a scientific
witness. Adjacent notes are likewise non-load-bearing context. Closure evidence
comes only from the displayed finite-matrix proof and paired runner linked
above.

### N5 — rhetoric audit

The claim is per displayed finite construction: the specified scalar trace
profile of an operator lifted from one `hw=1` corner, the projected
eigenoperator line, and the two stated extraction formulas. It does not claim
a per-operator no-go for all commutant observables, a per-block no-go for
matrix-valued overlaps, a no-go on a future carrier-constrained domain, or a
lattice-wide PMNS impossibility. All broader resolutions are untested and
excluded.

### N6 — partial-closure paths

An operational convention can orient every eigenoperator line and name the
outputs of the old maps `q_op` and `tau_op`; this changes the domain and closes
only labeling. A genuine positive path remains: prove a sign/phase section
from a carrier, then separately prove any passive-block and inter-sector
intertwiners. None requires a new axiom in principle; they are ordinary open
derivation obligations. The no-go does not call them impossible.

### N7 — steelman

A hostile reviewer should argue that the mathematical input is an oriented
matrix `M`, not an eigenoperator line: the runner can choose a deterministic
signed representative, or a future carrier graph may contain only one sign.
On that restricted domain the old formulas are well-defined, so the no-go
would fail if it claimed impossibility on all carriers. The source theorem
answers by making its domain explicit: the current commutant construction
supplies no invariant sign/phase section, and the no-go is only failure to
descend on that line domain. A carrier-constrained signed section is the exact
reopen condition, not foreclosed.

### N8 — cross-cycle echo

| Similar surface | Current status | Retirement mechanism seen | Applied here? |
|---|---|---|---|
| `docs/PMNS_SELECTOR_BANK_NONREALIZATION_NOTE.md` | bounded/unaudited current-bank domain mismatch | not retired; needs a PMNS-specific bridge | yes: carrier bridge stays open |
| `docs/PMNS_SCALAR_BRIDGE_NONREALIZATION_NOTE.md` | unaudited scalar-grammar boundary | not retired; would need a mixed observable | yes: no broad scalar no-go claimed |
| `.claude/science/physics-loops/lane3-quark-mass-retention-20260428/NO_GO_LEDGER.md` `C_3` Fourier entries | historical exact carrier/readout boundary | reopen only with derived source/readout law | yes: Fourier algebra preserved, readout bridge open |
| `.claude/science/physics-loops/hypercharge-identification-name-free-closure/NO_GO_LEDGER.md` | commutant-line identification boundary | physical identification requires more than a commutant line | yes: line descent is tested explicitly |

The cross-cycle search found no analogous wall retired by treating an
implementation sign as intrinsic. The known retirement mechanisms—supply a
carrier/section or narrow to algebra—are both considered.

**N1-N8 disposition:** PASS for the narrow current-construction no-go.

Independent audit remains required before the repository may treat this
candidate no-go as retained-grade.
