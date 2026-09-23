from pathlib import Path
import hashlib
import json
import sys
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
OUT = HERE / 'PRE_COMPARISON_SEAL.json'
assert not OUT.exists(), 'A PRE seal is immutable; do not overwrite it.'

def bind(path):
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())

def verify(row):
    actual = bind(Path(row['path']))
    assert actual['bytes'] == row['bytes'], (row['path'], 'size mismatch')
    assert actual['sha256'] == row['sha256'], (row['path'], 'hash mismatch')
    return actual

original = json.loads((HERE / 'SOURCE_BINDINGS.json').read_text())
update = json.loads((HERE / 'SOURCE_UPDATE_BINDINGS.json').read_text())
sources = original['sources'] + original['instructions'] + update['sources']
for row in sources: verify(row)
assert len({r['path'] for r in sources}) == len(sources)
receipt_summary = []
for name in ['capture_sources_run', 'finite_path_run', 'periodic_dark_run',
             'capture_volume_update_run']:
    path = HERE / (name + '.receipt.json')
    receipt = json.loads(path.read_text())
    assert receipt['returncode'] == 0
    for key in ('script', 'stdout', 'stderr'): verify(receipt[key])
    assert receipt['stderr']['bytes'] == 0
    receipt_summary.append(dict(name=name, receipt=bind(path),
                                returncode=receipt['returncode']))

path_result = json.loads((HERE / 'FINITE_PATH_RESULTS.json').read_text())
dark_result = json.loads((HERE / 'PERIODIC_DARK_RESULTS.json').read_text())
assert path_result['physical_dimension'] == 52
assert path_result['dark_first_mark_weight'] == '1/3'
assert path_result['exact_number_balance'] and path_result['resolved_coherent_loss_equal']
assert all(r['resolved_birth_paths'] == r['overlapping_pair_double_hop_paths'] == r['D'] == 0
           for r in dark_result)

artifacts = [bind(path) for path in sorted(HERE.rglob('*')) if path.is_file()]
result = dict(
    created_utc=datetime.now(timezone.utc).isoformat(),
    procedure_argv=sys.argv,
    scope='Independent record-number consequences and physical stationary countercontrols for the supplied compensated rotor target.',
    formation_capacity_author_read=False,
    unrelated_frontier_checkpoint_Git_or_publication_access=False,
    onward_delegation=False,
    source_update='Volume comparison was authorized and closed before this PRE; original provisional capture remains preserved with its additive update.',
    claims=[
        'Finite exact number/count balance and finite total expected formation.',
        'Finite-graph pointwise formation-rate extinction from trace-class C0 contractivity, without field moments.',
        'Translation-invariant infinite density balance, finite integrated rate per cell, zero long-time averaged rate.',
        'Stationary physical states need not be fully occupied, including a finite empty-B initialization trapping branch of weight one third.',
        'Gauss-legal translation-invariant locally normal dark states of positive vacancy density exist for every d>=2.',
        'A physical formation-free two-energy state need not have a density limit.'
    ],
    unresolved_strengthenings=[
        'Unconditional pointwise formation-rate extinction for all locally normal infinite states.',
        'Uniform future electric tightness, full-state relaxation from empty B, and classification of stationary states.',
        'Microscopic/large-spin limit uniform in volume or resource replenishment.'
    ],
    read_scope='Full permitted finite notes, bound volume theorem and independent report; full authorized volume comparison, F1 acknowledgment and clarification. Selected final-seal metadata read and whole-file authenticated. No capacity-author argument or control read.',
    execution_scope='Two new standard-library exact controls, both first-run successful; source capture/update and receipt authentication. No inherited physical builder or author scientific runner imported or rerun.',
    preserved_rejected_routes='ATTEMPTS.json',
    formal_audit_or_publication_verdict=False,
    actual_run_receipts=receipt_summary,
    sources=sources,
    artifacts=artifacts,
)
OUT.write_text(json.dumps(result, indent=2) + '\n')
identity = bind(OUT)
print(json.dumps(dict(PRE=identity, source_bindings=len(sources),
                     artifact_bindings=len(artifacts), all_source_and_receipt_bindings_verified=True), indent=2))
