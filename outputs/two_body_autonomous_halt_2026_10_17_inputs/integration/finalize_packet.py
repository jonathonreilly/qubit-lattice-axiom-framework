"""Record actual source and execution outcomes in the publication packet."""
from pathlib import Path
import hashlib
import json
import shutil

N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree'
D=N/'two_body_integration'
F=W/'outputs/two_body_autonomous_halt_2026_10_17_inputs'
Q=W/'.claude/science/physics-loops/toe-two-body-autonomous-halt-20261017'
execution=json.loads((D/'CANONICAL_EXECUTION.json').read_text())
assert execution['status']=='ok' and execution['exit_code']==0 and execution['cache_status']=='fresh'
mut=json.loads((D/'mutations/RESULTS.json').read_text())
assert len(mut['cases'])==7 and all(r['scientific_assertion_rejected'] for r in mut['cases'])
shutil.copyfile(D/'CANONICAL_EXECUTION.json',Q/'CANONICAL_EXECUTION.json')

(Q/'TRACE_GATE.md').write_text('''# Trace gate: strict two-body autonomous reflection

```yaml
trace_class: upstream_support
target_claim_id: product_source_controlled_stop_bounded_theorem_note_2026-10-16
target_blocker_text: "Mathematical target: realize the fixed old-pair operation with a static controller and complete output contract, using supplied positive nearest-neighbor two-body added blocks."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Publish this checked conditional construction; continue packet supply and native physical identification, preserving their open status."
```

This is a mathematical target inferred from the authorized autonomous-halt
campaign. The construction is a distinct supplied source ladder for the same
fixed K and W as PR9657; it does not autonomize that mediator's control ramps.
It removes the three-body boundary premise of PR9659 by a different conditional
two-body model, with larger source/contact loads and a fixed calibration ceiling.
The generic packet proof and interval certificate retain full old aging,
scalar phase, all source/clock outputs and passive references.

Infinite blank sites are required for the stated all-future bound. A finite
apparatus has only its declared observation horizon. Independently supplying
the finite clock vector and exact local coefficients remains a physical
premise. No native preparation, reset/reuse, Record or energy identification
is inferred. The preceding boundary theorem is cited as context; its small
loads and arbitrary-accuracy family are not imported.

See the [claim-status certificate](CLAIM_STATUS_CERTIFICATE.md) and
[handoff](HANDOFF.md). No audit verdict or retained status is supplied.
''')
(Q/'CLAIM_STATUS_CERTIFICATE.md').write_text('''# Claim-status certificate: two-body autonomous reflection

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "Supplied exact positive nearest-neighbor two-body ladder, one-head clock, finite incoming clock vector independent of old/reference input, and an infinite blank tail for every later time. Fixed calibration residual and old-only added cap two; finite apparatus has a stated horizon."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional complete-output realization of a fixed target by a static two-body ladder, with exact finite certificates and analytic packet bounds."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Source-note request: `proposed_retained`. Actual status remains
`conditional-support`; no audit-derived effective status is stated.
Root's [source decision](../../../../outputs/two_body_autonomous_halt_2026_10_17_inputs/root/SOURCE_ACCEPTANCE.json)
and [qualification](../../../../outputs/two_body_autonomous_halt_2026_10_17_inputs/root/QUALIFICATION.md)
permit conditional provisional reuse. Root separately read and approved the
complete canonical wrapper and its four unchanged mathematical bodies.
The [execution record](CANONICAL_EXECUTION.json) records a successful actual
canonical run with a fresh input-bound cache. Focused publication outcomes
are separately recorded in [PUBLISH_CHECKS.json](PUBLISH_CHECKS.json).

| Dependency | Checked scope | Remaining limitation |
|---|---|---|
| Exact stationary coefficients and source ladder | Positive local blocks, darkness, parity and complete channel closure; exact point residual certificates with a separate full-basis check | Supplied coefficients and sector, fixed nonzero residual; no general noise or native supplier |
| Generic finite-channel theorem | Full source argument and separate exposed mathematical check; V2 bound convention qualified | Conditional interval and readiness hypotheses; no spectral completeness assumption |
| Concrete interval composition | Non-grid gap/inverse bounds, exact Schur and phase conversion, finite resource inequalities; separate full32 Frobenius route | Infinite-time conclusion is analytic; no large-clock evolution |
| Prior independent point states/reflection | Reused unchanged, source-pinned earlier full-basis residual calculation | Not recomputed by the new helper; new helper checks root/inverse certificates and interval composition |
| Preparation and apparatus extent | Finite Fourier-integral vector, truncation and separate finite horizon | Ready vector supplied exactly in the example; native emission, finite precision and infinite blank supply remain conditions |
| Portable programs | Distinct checked implementations, complete static portability comparison and actual canonical execution | Same model and source exposure; no formal audit, proof assistant or laboratory verification |

The modeled old added loads are below2; source/contact loads are larger and
the existing old edge norm3 is separate. The physical vacancy scalar and
literal full elapsed old aging remain in the comparator. All clock/source
amplitudes and passive references remain in the norm contract. Capture,
reset/reuse, Record formation and laboratory energy costs are open.

Full pipeline, strict lint and changed-evidence checks belong to the exact
combined-current-main landing candidate under conformance section12. They
have not been asserted here. No landing, science merge, main push, audit
verdict, physical axiom or editable prompt change is authorized or performed.
Historical process snapshots are immutable evidence, not editable prompts.
''')
(Q/'REVIEW_HISTORY.md').write_text(f'''# Review and execution history

The selected old-cap point is an exact fixed rational witness with separately
checked full physical-basis root, inverse and state residual certificates.
The original larger-load witness and failed search starts remain historical
source evidence, not an arbitrary-accuracy claim or exclusion of alternatives.
The inherited stationary review is SHA256
23b78506dc56fe141f9e19347b60ed0e420b4e817b599cafa246a502a2a3f830.

The complete generic proof received a separate source-exposed review at
bba09ef378466a3787ebfbbbd942a81fbe200031a24d04f799d2543e510673f6.
V2 clarifies certified derivative bounds without changing its estimates.
Historical executions remain pinned to their actual input versions.

The concrete interval review is SHA256
a3ab8c94ce4c842980e2144766be0994b5f5d783f29d14d1cd25a7a2567dfe8a.
Its new full32 Frobenius path rechecks root/inverse residuals and the complete
interval/Schur/phase/resource composition. Old point-state/reflection
certificates remain explicitly inherited. Its actual run exited0 in2.465seconds,
with maximum matrix32; no large state, grid or time evolution was executed.
Root read the full candidate, code and review before accepting the source
under the separately archived qualification. This is not a retained audit.

The canonical wrapper preserves all four mathematical bodies byte for byte.
Root read its complete new prose and refined only the product-state meaning,
old-dependent total-energy columns, status separation and canonical paths.
The capped result's historical relative links remain inside a literal source
transcript. The separately rendered source is preserved at its proper path.
[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records exact ranges and hashes.

The separate [portability report](../../../../outputs/two_body_autonomous_halt_2026_10_17_inputs/portability/REPORT.md)
checks the complete program adaptation: all60 author and66 helper assertions
are unchanged,45 declared inputs cover the data reads, and frozen inputs
are never written. The report is a static check, not a claim of executing
the adapted programs. Root subsequently supplied the note and executed them.

Actual canonical execution exited0 in{execution['elapsed_sec']:.6f}seconds under
the shared120-second wall envelope and120-second process CPU cap. Its cache
is source/input bound and was fresh after execution. Both missing output
slots were explicitly marked not_executed before identity capture; the actual
run replaced them. No failed cache attempt or guard bypass occurred here.
The full output, point witnesses, cache and receipt are retained.

Seven copied-source scientific mutations were actually rejected at their
expected mathematical assertions: target conjugation, common phase sign,
closed-root underbound, interval overextension, an unjustified localized-column
maximum, too-small finite ready support, and too-short finite observation
clock. Original inputs/canonical outputs were unchanged. Their complete
sources, streams, receipts and exact mutation definitions are preserved.

Current-main was refreshed to2bb6c1a54721e70512922fb10d4495adf8ea3042 after
external landings. Ten relevant instruction files and the original target
mathematical body are unchanged. The complete narrow publication/provenance
changes were inspected; no external science/audit status was imported. An
initial fetch failed because the recorder's cwd was outside a repository;
the explicit git-C retry succeeded. Both receipts remain in campaign evidence.

Focused graph/publication results are [separately recorded](PUBLISH_CHECKS.json).
Shared combined-main landing gates and independent retained audit remain
pending. No science merge, main push, editable prompt or physical axiom change
was performed by this milestone.
''')
(Q/'HANDOFF.md').write_text('''# Publication handoff: two-body autonomous reflection

This is a milestone publication packet, not the campaign's current recovery
checkpoint. The science parent is PR9659 at
f5f5eda7427453aac726b394381c965f9e28ac03. Current-main instruction authority
was refreshed at2bb6c1a54721e70512922fb10d4495adf8ea3042; this branch did not
merge that science. Review the new child delta separately from inherited work.

The qualified result replaces the supplied three-body boundary with a distinct
positive nearest-neighbor two-body source ladder. It retains the complete
old/source/clock/reference comparison, phase and actual old aging. The fixed
point residual, old-only load cap and supplied coefficients are explicit.
A finite ready vector of22e12 sites gives isometry error<0.011 for every
t>=2e13 on an infinite clock. A9e14-site finite clock gives<0.012 only through
4e13. These enormous analytic sufficient costs were not simulated.

Sources, exact certificates, separate checks, original failures, portability
review and actual canonical execution are included. The new helper inherits
earlier point-state/reflection certificates by pin; its new inverse/composition
calculations do not silently replace that evidence. Root source acceptance,
wrapper approval, execution and publication are separate decisions.

Next physical obligations are actual clock-packet supply, exact local coefficient
realization and precision, feasible resources, and reset/reuse with all outputs.
No Markovian emitter, one-way sink, native vacuum, Record mechanism or energy
identification is assumed supplied by this result. Current exploratory routes
are not premises. Infinite blank sites remain necessary for the all-future
half-line statement; a finite device has its declared horizon.

Full combined-current-main pipeline, strict lint, changed-evidence checks and
independent retained audit remain future gates. Do not merge or apply an audit
verdict on the basis of this packet. See [claim status](CLAIM_STATUS_CERTIFICATE.md),
[source manifest](SOURCE_MANIFEST.json), [review history](REVIEW_HISTORY.md),
[execution](CANONICAL_EXECUTION.json) and [focused checks](PUBLISH_CHECKS.json).
''')

artifact=json.loads((F/'ARTIFACT_MANIFEST.json').read_text())
items=[]
for name in ['prepare_code.py','integrate_note.py','run_canonical.py','mutations.py',
             'finalize_packet.py','CANONICAL_EXECUTION.json']:
    items.append((D/name,'integration/'+name))
for src in (D/'mutations').rglob('*'):
    if src.is_file():items.append((src,'mutations/'+str(src.relative_to(D/'mutations'))))
for src,rel in items:
    dst=F/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
    b=dst.read_bytes();artifact['files'][rel]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
(F/'ARTIFACT_MANIFEST.json').write_text(json.dumps(artifact,indent=2)+'\n')
print(json.dumps({'companion_files_written':5,'artifact_entries':len(artifact['files']),
                  'canonical_seconds':execution['elapsed_sec'],'mutations':len(mut['cases'])}))
