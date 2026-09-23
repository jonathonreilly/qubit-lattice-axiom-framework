"""Seal authorized post-PRE comparison while preserving all earlier evidence."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
OUT=HERE/'FINAL_SEAL.json';assert not OUT.exists()
def row(p):
    p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r):
    a=row(r['path']);assert a['bytes']==r['bytes'] and a['sha256']==r['sha256'],(r,a)
p=HERE/'PRE_COMPARISON_SEAL.json';a=BASE/'CHARGED_BAND_AUTHOR_SEAL.json'
assert row(p)['sha256']=='4c13933f96f93217a20683f9b229d50c7e97fab28a556f90cce0226858ad3e48'
assert row(a)['sha256']=='c1c6420437307f014d547aaab23e261547d667e15eec0e736a600b0d75abf581'
pre=json.loads(p.read_text());auth=json.loads(a.read_text());bindings={}
def add(r,role):
    verify(r)
    if r['path'] not in bindings:bindings[r['path']]={**r,'roles':[role]}
    else:
        assert bindings[r['path']]['sha256']==r['sha256']
        if role not in bindings[r['path']]['roles']:bindings[r['path']]['roles'].append(role)
for r in pre['sources']:add(r,'unchanged_PRE_dependency')
for r in pre['artifacts']:add(r,'unchanged_PRE_artifact')
for r in auth['artifacts']:add(r,'authorized_author_artifact')
context=json.loads((BASE/'CHARGED_BAND_SOURCE_CONTEXT.json').read_text())
add(context['target_source'],'author_context');add(context['target_source_seal'],'author_context')
new=['COMPARISON.md','comparison_check.py','COMPARISON_RESULTS.json','COMPARISON_CHECK.stdout','COMPARISON_CHECK.stderr','COMPARISON_CHECK_RECEIPT.json','seal_comparison.py']
for name in new:add(row(HERE/name),'new_comparison_evidence')
r=json.loads((HERE/'COMPARISON_CHECK_RECEIPT.json').read_text());assert r['exit_code']==0
for k in ['runner','stdout','stderr']:verify(r[k])
assert (HERE/'COMPARISON_CHECK.stderr').read_bytes()==b''
assert (HERE/'COMPARISON_RESULTS.json').read_bytes()==(HERE/'COMPARISON_CHECK.stdout').read_bytes()
data={'created_utc':datetime.now(timezone.utc).isoformat(),
 'status':'Bounded author-source comparison complete; no material error or required source correction found. No audit/publication status.',
 'pre_seal':row(p),'author_seal':row(a),'bindings':[bindings[k] for k in sorted(bindings)],
 'counts':{'listed_unique_bindings':len(bindings),'top_level_seals':2,'including_top_level':len(bindings)+2,'new_comparison_files':len(new)},
 'comparison_results':['Author M_J=2J times the blind Q; path average Theta=T/2.',
 'All-direction local-star bound independently reconstructed and checked on full 6x10 physical tangent space.',
 'Physical compact packet retains twists, Coulomb matrix and O(sqrt(h)) band-derivative residual.',
 'Exact even-torus overall-sign equivalence independently reconstructed, with 3776 new even-box sign checks.',
 'One auxiliary packet row rebuilt: time-one error agrees within7.4e-13.'],
 'read_coverage':'Complete bound note, three current scientific checkers, all result fields and source context; complete receipts/streams and preserved failed-source delta/diagnostics.',
 'execution_limits':['No full author suite replay.','No full neutral matter matrix or time evolution on the cubic torus.',
 'Floating checks are not interval enclosures.','Uniform Hessian bound does not give volume-uniform packet estimates or a full many-body gap.',
 'Finite-rate/repeated-formation/locality author work, checkpoint and registry remain unopened.'],
 'preserved_failures':'Both blind failed/interrupted attempts unchanged; archived author cutoff-refinement failure authenticated; no new failed comparison execution.',
 'mutable_exclusion':'CHECKPOINT.md is an unsealed recovery aid.'}
OUT.write_text(json.dumps(data,indent=2)+'\n')
for r in data['bindings']:verify(r)
verify(data['pre_seal']);verify(data['author_seal'])
print(json.dumps({'FINAL':row(OUT),'COMPARISON':row(HERE/'COMPARISON.md'),'RESULTS':row(HERE/'COMPARISON_RESULTS.json'),'counts':data['counts'],'all_bindings_verified':True},indent=2))
