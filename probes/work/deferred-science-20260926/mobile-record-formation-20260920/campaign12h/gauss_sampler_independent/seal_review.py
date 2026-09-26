#!/usr/bin/env python3
"""Recheck source bytes and preserve the already-created pre-comparison seal."""
from pathlib import Path
import datetime,hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
REPO=ROOT.parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
def ident(p):
 raw=p.read_bytes();return {'path':str(p),'bytes':len(raw),'sha256':sha(raw)}
pre=HERE/'PRE_COMPARISON_SEAL.json'
assert sha(pre.read_bytes())=='61db44bcef855bee635114f7055b4d8ab4e33c1d6aae642e723c75508af42e5a'
initial=json.loads(pre.read_text())
for row in initial['sources']+initial['artifacts']:
 i=ident(Path(row['path']));assert i==row
comparison=json.loads((HERE/'COMPARISON_RESULTS.json').read_text())
assert comparison['all_checks_passed']
sources=[]
for path,old in comparison['source_identities'].items():
 i=ident(Path(path));assert i['bytes']==old['bytes'] and i['sha256']==old['sha256']
 if not Path(path).is_relative_to(HERE):sources.append(i)
procedures=[]
for path,expected in [(REPO/'AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
 (REPO/'docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
 (Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),'9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455')]:
 i=ident(path);assert i['sha256']==expected;procedures.append(i)
for name in ['INDEPENDENT.stderr','COMPARISON.stderr']:assert not (HERE/name).read_text()
artifacts=[ident(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
raw_claims=[{k:v for k,v in case.items() if k in ('folder','tag','raw_recorded_sha256','raw_bytes','full_raw_hash_independently_recomputed','raw_prefix_payload_sha256','raw_tail_payload_sha256','raw_rows_checked','limitation')} for case in comparison['cases']]
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Independent mathematical/source/statistical review of auxiliary finite Gauss sampler and separate staggered/adjoint operator comparison; no audit verdict or phase claim.',
 'source_identities':sources,'procedure_dependencies':procedures,'artifact_identities':artifacts,
 'pre_comparison_seal_sha256':sha(pre.read_bytes()),'pre_comparison_evidence_unchanged':True,
 'raw_data_recorded_claims_not_complete_rehashes':raw_claims,
 'raw_bytes_selectively_read':comparison['raw_window_bytes_read'],
 'production_executions':0,'bootstrap_reexecutions':0,
 'no_actionable_source_defect_found':True,'unproved':['quantitative mixing','equilibrium of finite runs','bootstrap interval coverage','thermodynamic phase or asymptotic exponent','microscopic realization of adjoint operator','physical photon count'],
 'concurrent_source_recheck_passed':True,'primary_source_or_git_mutations':[]}
final=HERE/'FINAL_SEAL.json';final.write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'sources':len(sources),'procedures':len(procedures),'artifacts':len(artifacts),
 'report_sha256':sha((HERE/'REPORT.md').read_bytes()),'seal_sha256':sha(final.read_bytes())},indent=2))
