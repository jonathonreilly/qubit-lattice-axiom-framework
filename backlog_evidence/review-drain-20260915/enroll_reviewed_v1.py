"""Local drain adapter: preserve checked v1 identities in the existing train format.

The coordinator must first receive the independent reviewer's final verdict.
This adapter makes no scientific decision and never executes runners or pushes.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys

ap = argparse.ArgumentParser()
ap.add_argument('label')
ap.add_argument('unit')
ap.add_argument('--record', required=True)
ap.add_argument('--preflight', required=True)
ap.add_argument('--report-md', required=True)
ap.add_argument('--departure', required=True)
a = ap.parse_args()
w = Path.cwd()
# Pool author slots can be nested; evidence root follows the explicit record.
rp = Path(a.record).resolve()
out = rp.parent
target = out / (a.label + '-collected-units.json')
assert not target.exists(), 'Never overwrite a prior collection'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
git = lambda *args: subprocess.check_output(['git', *args], text=True).strip()
r = json.loads(rp.read_text())
pp = Path(a.preflight).resolve()
p = json.loads(pp.read_text())
assert p['mechanical_status'] == 'ok' and p['cache_checked']
assert p['record_sha256'] == sha(rp)
assert git('write-tree') == r['source']['tree'] == p['tree']
assert git('rev-parse', 'HEAD') == r['source']['commit']
assert not git('diff', '--name-only') and not git('ls-files', '--others', '--exclude-standard')
assert not r['source']['deleted_paths'], 'Deletion-aware integration requires explicit mapping'
sources = {x['path']: x['sha256'] for x in r['source']['paths']}
inputs = dict(sources)
for rows in r['inputs'].values():
    for x in rows:
        assert x['path'] not in inputs or inputs[x['path']] == x['sha256']
        inputs[x['path']] = x['sha256']
for name, h in inputs.items():
    assert sha(w / name) == h, name
refs = [r['reviewer']['report'], *r['reviewer']['references'],
        *(x['dispositions'] for x in r['constituents']),
        *(x['review_reference'] for x in r['non_science_notes'])]
reports = {}
for ref in refs:
    q = Path(ref['path'])
    assert sha(q) == ref['sha256']
    reports[q.relative_to(out).as_posix()] = ref['sha256']
for q in (rp, pp, Path(a.report_md).resolve()):
    reports[q.relative_to(out).as_posix()] = sha(q)
sys.path.insert(0, str(w / 'docs/audit/scripts'))
import build_citation_graph as graph
required = {n['path']: [graph.claim_id_from_path(w / d) for d in n['repository_dependencies']]
            for n in r['notes']}
scope = Path(r['reviewer']['report']['path']).relative_to(out).as_posix()
prs = []
for row in r['constituents']:
    match = re.fullmatch(r'(?:PR|#)?(\d+)', str(row['id']))
    assert match, row['id']
    prs.append(int(match.group(1)))
subprocess.run(['git', 'commit', '-q', '-m', 'Preserve independently reviewed source unit PR' + a.unit], check=True)
head = git('rev-parse', 'HEAD')
assert git('rev-parse', 'HEAD^{tree}') == r['source']['tree']
u = {'unit': a.unit, 'prs': prs,
     'commits': [head], 'final_head': head, 'source_paths': sources,
     'inputs': inputs, 'reports': list(reports), 'review_evidence_hashes': reports,
     'canonical_unit_record': rp.name, 'required_repository_claim_ids': required,
     'dependency_scope': scope,
     'dependency_reason': ' '.join(dict.fromkeys(n['dependency_rationale'] for n in r['notes'])),
     'validated_source_tree': r['source']['tree'],
     'commit_mapping': 'Root committed exactly the independently confirmed and mechanically checked staged tree; original v1 report/check identities preserved.'}
collection = {'units': [u], 'science_notes': len(r['notes']), 'source_count': len(sources),
              'collection_closed': a.departure}
target.write_text(json.dumps(collection, indent=2) + '\n')
print('ENROLLED', head, len(sources), len(inputs), len(reports))
