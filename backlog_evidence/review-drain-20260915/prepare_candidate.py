"""Replay independently frozen source units and verify integration identities.
No scientific verdict is generated here; immutable reviewer evidence is required.
Run in a fresh detached worktree at current origin/main after prior fallback lands.
"""
from pathlib import Path
import subprocess,json,hashlib,sys,collections,re
import yaml
root=Path.cwd();out=root.parent;label=sys.argv[1]
collection=json.loads((out/(label+'-collected-units.json')).read_text())
inventory={str(p['number']):p for p in json.loads((out/'inventory.json').read_text())['topology']['prs']}
def git(*args):return subprocess.check_output(['git',*args],text=True).strip()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
base=git('rev-parse','HEAD');assert base==git('rev-parse','origin/main') and not git('status','--porcelain')
assert 1<=len(collection['units'])<=8
owners={};inputs={};reviews={};heads={}
for u in collection['units']:
 for name,h in u['review_evidence_hashes'].items():assert sha(out/name)==h,(name,'review changed');reviews[name]=h
 for p,h in u['source_paths'].items():assert p not in owners,('source overlap',p);owners[p]='review-'+u['unit']
 for p,h in u['inputs'].items():
  assert p not in inputs or inputs[p]==h,('input disagreement',p)
  inputs[p]=h
 for n in u['prs']:heads[str(n)]=inventory[str(n)]['headRefOid']
 for commit in u['commits']:subprocess.run(['git','cherry-pick',commit],check=True)
for p,h in inputs.items():assert sha(root/p)==h,('integrated input drift',p)
assert set(git('diff','--name-only',base+'...HEAD').splitlines())==set(owners)
# Every current-main path outside the accepted source set is preserved by the exact delta assertion.
for args in [('diff','--check'),('diff','--cached','--check'),('diff',base+'...HEAD','--check')]:subprocess.run(['git',*args],check=True)
counts=collections.Counter(Path(p).name for p in git('ls-files','docs').splitlines() if p.endswith('.md'))
assert not {k:v for k,v in counts.items() if v>1 and k not in ['README.md','SKILL.md']}
sys.path[:0]=[str(root/'docs/audit/scripts'),str(root/'scripts')]
import build_citation_graph as graph
import runner_cache
expectations={};preflight={}
for u in collection['units']:
 for p in u['source_paths']:
  if p.endswith('.md'):
   s=(root/p).read_text();assert not re.search(r'\]\((?:/Users/|/home/|/private/|/tmp/|/var/|/opt/|file://)',s),('nonportable',p)
  if not (p.startswith('docs/') and not p.startswith('docs/work_history/') and p.endswith('.md')):continue
  hint=graph.extract_claim_type_hint(s);assert hint[0]=='bounded_theorem',(p,hint)
  citations=graph.extract_citations(s,Path(p));meta=yaml.safe_load(s.split('---',2)[1]) if s.startswith('---') else {}
  required=meta.get('upstream_dependencies',[])
  required=u.get('required_repository_claim_ids',{}).get(p,required)
  if required:assert citations,('declared but unlinked',p)
  if u['unit']=='8111':required=list(set(required+['kinetic_isotropy_primitive']))
  expectation={'required_claim_ids':required}
  if u.get('dependency_scope'):
   scope=json.loads((out/u['dependency_scope']).read_text())
   expectation.update(allow_empty_repository_deps=True,independent_review=u['dependency_scope'],reason=u.get('dependency_reason',scope.get('rationale',scope.get('reason'))))
  expectations[p]=expectation
  preflight[p]={'primary_runner':graph.extract_runner(s,p),'helper_runner_paths':graph.resolve_helper_runner_paths(graph.extract_runner(s,p)),'type_hint':hint,'actual_citations':[str(x.relative_to(root)) for x in citations],'required_claim_ids':required}
 for p in u['source_paths']:
  if p.startswith('scripts/') and p.endswith('.py') and p in {entry['primary_runner'] for entry in preflight.values()}:
   status=runner_cache.cache_status(Path(p));assert status=='fresh',('cache not fresh',p,status)
assert len(preflight)==collection['science_notes']
record={'base':base,'source_head':git('rev-parse','HEAD'),'source_tree':git('rev-parse','HEAD^{tree}'),'heads':heads,'source_owners':owners,'inputs':inputs,'review_evidence_hashes':reviews,'dependency_expectations':expectations,'cheap_preflight':preflight,'units':[u['unit'] for u in collection['units']],'departure':collection['collection_closed'],'current_main_preservation':'Exact integrated delta equals accepted source path union; every other base path preserved. All reviewed source/input hashes match.'}
(out/(label+'-record.json')).write_text(json.dumps(record,indent=2)+'\n')
print('FROZEN',record['source_head'],'sources',len(owners),'inputs',len(inputs),'notes',len(preflight),flush=True)
