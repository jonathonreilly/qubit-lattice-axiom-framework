"""Freeze the reconstruction without opening any new author volume artifact."""
import datetime
import hashlib
import json
from pathlib import Path
import sys


base = Path(__file__).resolve().parent
target = base/'PRE_COMPARISON_SEAL.json'
if target.exists():
    raise FileExistsError(target)


def binding(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


source_record = json.loads((base/'SOURCE_BINDINGS.json').read_text())
sources = []
for row in source_record['fixed_dependencies']:
    actual = binding(Path(row['path']))
    assert actual['sha256'] == row['sha256'] and actual['bytes'] == row['bytes']
    sources.append(actual)
for name in ('exact_control_run', 'support_control_run', 'capture_sources_run'):
    receipt = json.loads((base/f'{name}.receipt.json').read_text())
    assert receipt['exit_code'] == 0
    assert hashlib.sha256((base/f'{name}.stdout').read_bytes()).hexdigest() == receipt['stdout_sha256']
    assert hashlib.sha256((base/f'{name}.stderr').read_bytes()).hexdigest() == receipt['stderr_sha256']
    script = Path(receipt['command_argv'][1])
    assert binding(script)['sha256'] == receipt['source_sha256']
artifacts = [binding(p) for p in sorted(base.iterdir()) if p.is_file() and p != target]
seal = {
    'scope': 'Blind bounded independent reconstruction: local infinite-volume dynamics of the compensated rotor target',
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'procedure_argv': [sys.executable, str(Path(__file__).resolve())],
    'new_author_volume_packet_read': False,
    'other_new_frontier_checkpoint_or_registry_read': False,
    'scientific_disposition': 'Spatial norm limit and locally normal evolution proved with an explicit electric-cutoff construction; full norm time continuity and universal global-folium normality rejected by physical countercontrols.',
    'independent_controls': ['exact integer formation paths in d=2,3,4',
                             'exact decorated support geometry in d=2,3,4',
                             'physical Wilson-loop norm-continuity countercontrol',
                             'separated-plaquette global representation countercontrol'],
    'unresolved_requested_proof_obligations': [],
    'scope_limits': ['No volume-uniform microscopic spin/epsilon approximation.',
                     'No global first-event unravelling on the infinite lattice.',
                     'No phase, native-axiom, field-identification or audit/publication claim.'],
    'sources': sources, 'artifacts': artifacts,
    'literature_receipts_in': 'SOURCE_BINDINGS.json',
}
target.write_text(json.dumps(seal, indent=2)+'\n')
for row in sources+artifacts:
    assert binding(Path(row['path'])) == row
print(json.dumps({'PRE_COMPARISON_SEAL': binding(target),
                  'REPORT': binding(base/'REPORT.md'),
                  'verified_source_count': len(sources),
                  'verified_artifact_count': len(artifacts)}, indent=2))
