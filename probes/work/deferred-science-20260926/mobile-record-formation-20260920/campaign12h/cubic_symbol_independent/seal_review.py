#!/usr/bin/env python3
"""Preserve initial seals and bind the complete post-comparison record."""
from pathlib import Path
import hashlib,json,datetime
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;REPO=ROOT.parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
def ident(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
for name,expected in [('BASE_PRE_COMPARISON_SEAL.json','5c3ad0cd053ea4822b1137953e6610300b25ed5f699867d410d7d943aa12a0a9'),('SELECTION_PRE_COMPARISON_SEAL.json','24eeaed4f6c837cef2c6b2cd4dd2fdae3a43165530305bc4e23632fa94a80c96')]:
 p=HERE/name;assert sha(p.read_bytes())==expected
 seal=json.loads(p.read_text());assert ident(Path(seal['source']['path']))==seal['source']
 for row in seal['artifacts']:assert ident(Path(row['path']))==row
comparison=json.loads((HERE/'AUTHOR_COMPARISON_RESULTS.json').read_text());assert comparison['all_checks_passed']
sources=[]
for row in comparison['identities']:
 assert ident(Path(row['path']))==row
 if not Path(row['path']).is_relative_to(HERE):sources.append(row)
procedures=[]
for path,expected in [(REPO/'AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
 (REPO/'docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
 (Path('/Users/jonreilly/.codex/skills/physics-claim-reviewer/SKILL.md'),'9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455')]:
 row=ident(path);assert row['sha256']==expected;procedures.append(row)
for name in ['INDEPENDENT.stderr','SELECTION_INDEPENDENT.stderr','AUTHOR_COMPARISON.stderr']:assert not (HERE/name).read_text()
read_boundary={'complete_source_reads':['187-line base theorem note','complete dependent addendum','187-line base author checker','42-line selection author checker','both author JSONs and full logs'],
 'independent_precomparison_controls':'Exact character projector decomposition, all48 species intertwiners, symbolic Gram and closure, actual 15^4-context currents per direction; separate symbolic selection and complete81-state stationary-adjoint generator.',
 'postcomparison_executions':'Two small author checkers from exact private copies; treated as source reproduction, not further independent proof.',
 'not_read':['unrelated numerical winding diagnostic','other new primary research'],
 'failed_independent_checks':[],'primary_or_git_mutations':[],'audit_verdict':None}
(HERE/'READ_BOUNDARY.json').write_text(json.dumps(read_boundary,indent=2)+'\n')
artifacts=[ident(p) for p in sorted(HERE.rglob('*')) if p.is_file() and p.name!='FINAL_SEAL.json']
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Bounded independent finite classification, local-generator and conditional selection review; not a new hydrodynamic theorem, physical identification or audit verdict.',
 'source_identities':sources,'procedure_dependencies':procedures,'artifact_identities':artifacts,
 'precomparison_seals_and_evidence_unchanged':True,'concurrent_source_identity_recheck_passed':True,
 'actionable_findings':[],'limits':['uniform fifteen-state background','full48 is stronger than proper24','ordinary nonaliased local context geometry','arbitrary-moment closure and divergence preservation are extra premises','no new macroscopic limit proof','no justified fast relaxation elimination or physical Maxwell claim'],
 'primary_or_git_mutations':[]}
p=HERE/'FINAL_SEAL.json';p.write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'sources':len(sources),'procedures':len(procedures),'artifacts':len(artifacts),
 'report_sha256':sha((HERE/'REPORT.md').read_bytes()),'seal_sha256':sha(p.read_bytes())},indent=2))
