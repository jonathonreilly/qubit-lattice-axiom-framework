"""Root source-publication review with actual metadata checks; no science execution."""
from pathlib import Path
from datetime import datetime,timezone
import ast,difflib,hashlib,json
N=Path(__file__).resolve().parents[1];B=N/'local_bias_publication_draft';W=N.parent/'correlation_worktree'
R=N/'local_bias_root_publication_review';PACK='.claude/science/physics-loops/toe-local-bias-gibbs-sources-20261015'
NOTE='docs/LOCAL_CONDITIONAL_BIAS_AND_ROTATED_GIBBS_BOUNDED_THEOREM_NOTE_2026-10-15.md'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def read(p):return json.loads(p.read_bytes())
def same(p,r):assert (p.stat().st_size,sha(p.read_bytes()))==(r['bytes'],r['sha256']),str(p)
def put(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
assert not R.exists()
assert pin(B/'FINAL_FREEZE.json')['sha256']=='520767eb22da03e4348edb27fa2c60550e7869aff92c3381e5d012c5192ff4f5'
f=read(B/'FINAL_FREEZE.json')
for r in f['files']:same(B/r['path'],r)
assert len(f['files'])==176
assert {str(p.relative_to(B)) for p in B.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
for r in read(B/'SOURCE_FRESHNESS.json')['identities']:same(Path(r['original']),r)
reuse=read(B/'REUSE_MAP.json');diff=[]
for r in reuse['references']:
 same(Path(r['path']),r);same(B/r['captured'],r)
 name=Path(r['path']).name;a=Path(r['path']).read_text();b=(B/name).read_text();ast.parse(b)
 diff.extend(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='reference/'+name,tofile='current/'+name))
assert ''.join(diff)==(B/'CHANGED_CODE.patch').read_text()
for r in reuse['functions']:
 p=B/r['script'];lines=p.read_text().splitlines(True);c=r['current'];b=''.join(lines[c['line_start']-1:c['line_end']]).encode()
 assert (len(b),sha(b))==(c['bytes'],c['sha256'])
out=B/'proposal';packet=out/PACK;note=(out/NOTE).read_bytes();bm=read(packet/'BODY_MAP.json')['bodies'];parents=read(packet/'DEPENDENCIES.json')['dependencies']
assert len(bm)==8 and len(parents)==1
for r in bm:
 b=note[r['start_byte_inclusive']:r['end_byte_exclusive']]
 assert (len(b),sha(b),note.count(b))==(r['bytes'],r['sha256'],1)
for r in parents:
 same(W/r['path'],r);b=(W/r['path']).read_bytes()
 for q in r['accepted_body_intervals']:
  v=b[q['start_byte_inclusive']:q['end_byte_exclusive']]
  assert (len(v),sha(v),b.count(v))==(q['bytes'],q['sha256'],1)
sources=read(packet/'SOURCE_MANIFEST.json')['sources']
for r in sources:
 q=r['recovery']
 if q['kind']=='blob':b=(out/q['path']).read_bytes()
 elif q['kind']=='external_pinned':b=(W/q['path']).read_bytes()
 else:
  p=out/q['container'];p=p if p.exists() else W/q['container']
  b=p.read_bytes()[q['start_byte_inclusive']:q['end_byte_exclusive']]
 assert (len(b),sha(b))==(r['bytes'],r['sha256'])
for r in read(packet/'INPUT_MANIFEST.json')['inputs']:same(out/r['path'],r)
idx=read(B/'PAYLOAD_CHANGE_INDEX.json')
for r in idx['current_files']:same(out/r['path'],r)
assert {r['path'] for r in idx['current_files']}=={str(p.relative_to(out)) for p in out.rglob('*') if p.is_file()}
receipts=[]
for label in ('build','inspection'):
 folder=B/'metadata_runs'/label;e=read(folder/'EXECUTION.json');assert e['exit_code']==0 and e['scientific_execution'] is False and e['timed_out'] is False
 for k in ('child_source_at_launch','stdout','stderr','recorder'):same(Path(e[k]['path']),e[k])
 for r in read(folder/'LAUNCH.json')['inputs']:
  same(Path(r['original']['path']),r['original']);same(Path(r['captured']['path']),r['captured'])
 assert not (folder/'stderr').read_bytes();receipts.append(pin(folder/'EXECUTION.json'))
accepts={'local_bias':N/'conditional_sources_root_review/LOCAL_BIAS_ACCEPTANCE.md','rotated_gibbs':N/'conditional_sources_root_review/ROTATED_GIBBS_ACCEPTANCE.md','noncommuting_boundary':N/'local_bias_noncommuting_boundary_root_review/ACCEPTANCE.md'}
assert {pin(p)['sha256'] for p in accepts.values()}=={r['sha256'] for r in sources if r['role']=='root_conditional_source_acceptance'}
R.mkdir()
review={'kind':'root_source_publication_review','utc':datetime.now(timezone.utc).isoformat(),'root_read_complete':True,
 'source_draft_freeze':pin(B/'FINAL_FREEZE.json'),'sealed_members_verified':176,'source_rows_verified':len(sources),
 'body_pins':bm,'parents':parents,'existing_source_acceptances':{k:pin(p) for k,p in accepts.items()},
 'scientific_programs_run':0,'primary_runs':0,'historical_programs_replayed':0,'actual_metadata_receipts':receipts,
 'full_current_files_read':[pin(B/x) for x in ('wrapper.md','primary_template.py','build_proposal.py','inspect_proposal.py','record_metadata.py','seal_packet.py')]+[pin(p) for p in sorted((B/'packet_text').iterdir())],
 'reading_scope':'Complete current wrapper, all module-level assembly and helper code, primary template and all nine packet texts read. Initial combined reuse-map/wrapper output truncated; complete separate wrapper/primary read repaired coverage. Exact earlier eight scientific body and parent readings reused at verified identities. Full old-to-new code diff and all payload identities checked mechanically, not counted as a fresh independent proof.',
 'current_qualifications':['Fixed local equilibrium-class tolerances are distinct from global delivery errors and coherent nominal-target dynamic accuracy.','Lower inverse-temperature bound, r>=1, logical Dmax and genuinely full-rank-only rank witness retained.','Collected Ising conditional formula does not transfer physical reserve/scalar/channel costs; bounded c,k0 and profile factors needed for O(L) resources.','Product-basis Gibbs family remains mutually commuting. Full reduced density or full reduced trace tolerance needed through its non-diagonal quench.','Every actual quench/guard/readiness segment, reference, record, scalar, phase, covariance and old K_Z then H0 aging retained.','Two-qubit XX boundary is narrow; it does not exclude the separate prospective onsite transverse-field class.'],
 'independence':'The independent local-bias source predates root-candidate exposure; later comparison, rotated/boundary checks and publication assembly are source exposed on the same selected model. Root authored initial proposals; this packaging review adds no independent mathematical derivation.',
 'base_binding':'Source draft names PR9611/9369 as requested ancestry. Root may bind the coherent later checked stack after bank publication, but must explicitly update current wrapper, primary base observation and receipt schema. Sole mathematical parent remains correlated12bd18b0; no bank import.',
 'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.',
 'remaining':'Actual base/source binding, primary/cache/semantic mutations/focused graph and stage gates, regular PR/attachment. No retained audit, native source/control supply or physical energy/detector identification.'}
put(R/'ROOT_REVIEW.json',review)
put(R/'FINAL_FREEZE.json',{'utc':datetime.now(timezone.utc).isoformat(),'scope':'Root publication interpretation only','files':[pin(R/'ROOT_REVIEW.json')]})
print(json.dumps({'review':pin(R/'ROOT_REVIEW.json'),'freeze':pin(R/'FINAL_FREEZE.json'),'sealed_members':176,'source_rows':len(sources),'scientific_programs_run':0}))
