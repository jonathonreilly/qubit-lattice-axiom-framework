"""Authenticate unchanged PRE and exact authorized author inputs, then seal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

D = Path(__file__).resolve().parent
A = D.parent / 'post_birth_ring_spectrum_author'


def row(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


pre_path = D / 'PRE_COMPARISON_SEAL.json'
author_path = A / 'AUTHOR_SEAL.json'
assert row(pre_path)['sha256'] == 'cffc3495e440045bd73077e8be1a5e231ff39a07e53889a22336c204f60f5c37'
assert row(author_path)['sha256'] == 'c2e0e2adcff2dee95c682da2789c19f3113445e7f3e53f20d95936ab25ec07b9'
pre = json.loads(pre_path.read_text())
author = json.loads(author_path.read_text())
for saved in pre['sources'] + pre['artifacts']:
    assert row(Path(saved['path'])) == saved
sources = {r['path']: r for r in pre['sources']}
sources[str(author_path)] = row(author_path)
for rel, sha in author['files'].items():
    p = A / rel
    r = row(p)
    assert r['sha256'] == sha
    sources[str(p)] = r
for rel, sha in author['parent_source'].items():
    p = D.parent.parent / rel
    r = row(p)
    assert r['sha256'] == sha
    sources[str(p)] = r
receipt = json.loads((D / 'comparison_run_RECEIPT.json').read_text())
assert receipt['exit_code'] == 0
for key in ('runner', 'stdout', 'stderr'):
    assert row(Path(receipt[key]['path'])) == receipt[key]
assert (D / 'comparison_run.stdout').read_bytes() == (D / 'COMPARISON_RESULTS.json').read_bytes()
assert (D / 'comparison_run.stderr').read_bytes() == b''
target = D / 'FINAL_SEAL.json'
assert not target.exists()
artifacts = [row(p) for p in sorted(D.iterdir()) if p.is_file() and p != target]
seal = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'Completed bounded post-seal scientific comparison; no required correction found; not a formal audit or publication status.',
    'pre_comparison_seal': row(pre_path),
    'authorized_author_seal': row(author_path),
    'sources': sorted(sources.values(), key=lambda r: r['path']),
    'artifacts': artifacts,
    'prior_evidence': 'All six PRE source and 29 PRE artifact bindings plus PRE itself remain unchanged.',
    'new_evidence': 'Independent legal-hop matrices at L=3,4,6,9: 28 angle controls of lowest energies, crossing eigenspaces and weights; zero-angle gaps; five-size angle-cancellation controls. No author builder imported or executed.',
    'read_coverage': 'Complete authorized note, final and initial-probe scripts, both full result objects, receipts and streams read and authenticated. A truncated L=7 display was repaired by targeted complete read.',
    'execution_limits': 'Author runs authenticated, not rerun. One new independent comparison command completed successfully with full stdout/stderr/receipt. Earlier helper failure remains preserved.',
    'excluded': 'No second_event_author artifact, fourth-campaign checkpoint, registry or other new author derivation was read.',
    'scientific_scope': 'General-L unit-rotor spectrum, specified formation-output measures, lowest-band/gap formulas and stated compact-fast-time transfer at fixed graph; no subsequent ordinary-time formation law or conditioned microscopic-history theorem.',
}
target.write_text(json.dumps(seal, indent=2) + '\n')
for saved in seal['sources'] + seal['artifacts']:
    assert row(Path(saved['path'])) == saved
print(json.dumps({'report': row(D / 'COMPARISON.md'), 'final_seal': row(target),
                  'source_bindings': len(seal['sources']),
                  'artifact_bindings': len(seal['artifacts'])}, indent=2))
