"""Authenticate unchanged PRE/author packets and bind this comparison."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE=Path(__file__).resolve().parent
BASE=HERE.parent


def row(path):
    path=Path(path).resolve();data=path.read_bytes()
    return {'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}


def verify(rows):
    for r in rows:
        assert row(r['path'])==r, r['path']


pre_path=HERE/'PRE_COMPARISON_SEAL.json'
author_path=BASE/'LARGE_SPIN_RECORD_AUTHOR_SEAL.json'
assert row(pre_path)['sha256']=='f8f457305153006eccda68740a518cfed0c11d3c28d1c77ad3ce6df71970e3c5'
assert row(author_path)['sha256']=='40797e4620ebb864744753ae5429a1727c7b407fc712bda4360e75ea295a1f3b'
pre=json.loads(pre_path.read_text());author=json.loads(author_path.read_text())
verify(pre['sources']+pre['artifacts']);verify(author['artifacts'])
context=json.loads((BASE/'LARGE_SPIN_RECORD_SOURCE_CONTEXT.json').read_text())
verify(context['dependencies'])
sources={r['path']:r for r in pre['sources']+author['artifacts']+context['dependencies']+[row(author_path)]}
artifacts={r['path']:r for r in pre['artifacts']}
excluded={'CHECKPOINT.md','FINAL_SEAL.json'}
for path in HERE.rglob('*'):
    if path.is_file() and path.name not in excluded and '__pycache__' not in path.parts:
        artifacts[str(path.resolve())]=row(path)
assert row(pre_path)['path'] in artifacts
result=json.loads((HERE/'COMPARISON_RESULTS.json').read_text())
receipt=json.loads((HERE/'COMPARISON_CHECK_RECEIPT.json').read_text())
assert result['status']=='PASS' and receipt['exit_code']==0
assert (HERE/'COMPARISON_CHECK.stderr').read_bytes()==b''
assert (HERE/'COMPARISON_CHECK.stdout').read_bytes()==(HERE/'COMPARISON_RESULTS.json').read_bytes()
seal={'created_utc':datetime.now(timezone.utc).isoformat(),
      'status':'Bounded independent post-seal source comparison complete; no formal audit or publication status.',
      'pre_comparison_seal':row(pre_path),'author_seal':row(author_path),
      'sources':sorted(sources.values(),key=lambda r:r['path']),
      'artifacts':sorted(artifacts.values(),key=lambda r:r['path']),
      'counts':{'sources':len(sources),'artifacts':len(artifacts),'total':len(sources)+len(artifacts)},
      'findings':[],
      'disposition':'No substantive correction identified. The finite-spin block-basis allowance is compatible with the specific canonical identification of the blind circuit. The local limit retains all stated preparation, moment, time and resource hypotheses.',
      'new_independent_evidence':'An explicit nonzero finite-spin analytic block-basis change with weighted vanishing limit; independently assembled spin-16 microscopic spectrum; exact comparison with presealed integer-spin H2/H4/loss calculations.',
      'authentication_limits':'All author results/logs/receipts authenticated; the other three large-spin spectra and the 7,440-row author screen were not rerun. No full-spectrum interval certificate or many-volume simulation is claimed.',
      'failures':'One optional bs4 extraction helper failed before any scientific assertion; exact attempted code and complete tool response retained. Standard-library extraction succeeded. No comparison scientific assertion failed.',
      'source_boundary':'Only the authorized 12-artifact large-spin packet, its pinned already-reviewed dependencies, prior independent evidence, and the credited primary arXiv Section VII.A were read. Other new author packets/checkpoint/registry remain unopened.',
      'mutable_exclusion':'CHECKPOINT.md is a recovery aid, excluded from all scientific bindings.'}
path=HERE/'FINAL_SEAL.json'
assert not path.exists(), 'Do not overwrite an existing final seal.'
path.write_text(json.dumps(seal,indent=2)+'\n')
check=json.loads(path.read_text());verify(check['sources']+check['artifacts'])
print(json.dumps({'final_seal':row(path),'comparison':row(HERE/'COMPARISON.md'),
                  'comparison_results':row(HERE/'COMPARISON_RESULTS.json'),
                  'counts':check['counts'],'all_bindings_verified':True},indent=2))
