"""Author assembly/provenance checks; not independent scientific review."""
from pathlib import Path
import hashlib,json,subprocess,sys,py_compile

HERE=Path(__file__).resolve().parent
EV=HERE.parent
ROOT=EV.parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
import runner_cache
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
note=ROOT/'docs/MOBILE_RECORDS_CUBIC_SYMBOL_SELECTION_AND_GAUSS_CLOSURE_BOUNDED_THEOREM_NOTE_2026-09-21.md'
runner=ROOT/'scripts/mobile_records_cubic_symbol_selection_and_gauss_closure_2026_09_21.py'
claim='mobile_records_cubic_symbol_selection_and_gauss_closure_bounded_theorem_note_2026-09-21'
text=note.read_text();transform=json.loads((EV/'PUBLICATION_TRANSFORM.json').read_text())
for i,row in enumerate(transform['parts']):
    source=EV/'primary_sources'/row['source'];assert sha(source)==row['source_sha256']
    body=source.read_text().split('\n',2)[2].rstrip()
    if row['replacement']:
        old,new=row['replacement']['old'],row['replacement']['new']
        assert body.count(old)==1;body=body.replace(old,new)
    body='\n'.join('#'+line if line.startswith('#') else line for line in body.splitlines())
    assert hashlib.sha256(body.encode()).hexdigest()==row['published_body_sha256']
    prefix='## Part '+chr(65+i)+'. '
    start=text.index('\n\n',text.index(prefix))+2
    end=text.index('\n\n## '+('Part B.' if i==0 else 'Evidence and outstanding work'),start)
    assert text[start:end]==body
assert 'periodic sides of at least four sites' in text
assert sha(EV/'independent/REPORT.md')=='433dce9a4d9986aed9d262f97f393d4b1428fda7678e7373181eb0ad2b72265d'
verified=subprocess.run([sys.executable,str(EV/'verify_evidence.py')],cwd=ROOT,capture_output=True,text=True)
assert verified.returncode==0
capsule=json.loads(verified.stdout)
assert (capsule['bundled_members'],capsule['bundled_source_bindings'],capsule['seal_rows'])==(62,38,51)
assert capsule['external_reference_exclusions']==[]
author=json.loads((EV/'AUTHOR_RESULTS.json').read_text())
assert author['passed'] and author['control_count']==3
for name,digest in author['identities'].items():assert sha(ROOT/name)==digest
mutations=json.loads((EV/'MUTATION_RESULTS.json').read_text())
assert len(mutations['mutations'])==6 and mutations['all_rejected']
for row in mutations['mutations']:
    path=EV/'mutation_results'/(row['name']+'.json');assert sha(path)==row['result_sha256']
    record=json.loads(path.read_text());assert not record['passed'] and record['mutation']==row['name']
    for name,digest in record['identities'].items():assert sha(ROOT/name)==digest
    suite=record['suites'][-1]
    assert suite['returncode']==1 and 'AssertionError' in suite['stderr']
    assert suite['source_sha256']!=suite['executed_source_sha256']
relative=str(runner.relative_to(ROOT));assert runner_cache.cache_status(relative)=='fresh'
manifest=ROOT/'docs/audit/data/citation_graph_manifest.json'
old=json.loads(subprocess.check_output(['git','show','c26b0171974c456f68dd92a4c8661ade1cc5ddbd:'+str(manifest.relative_to(ROOT))],cwd=ROOT))
new=json.loads(manifest.read_text())
assert new['node_count']==old['node_count']+1 and new['edge_count']==old['edge_count']+2
assert set(new['nodes'])-set(old['nodes'])=={claim}
assert all(new['nodes'][k]==v for k,v in old['nodes'].items())
graph=json.loads((ROOT/'docs/audit/data/citation_graph.json').read_text())
assert graph['nodes'][claim]['note_hash']==sha(note)
vocab=json.loads((EV/'VOCAB_REPORT.json').read_text());assert vocab['summary']['files_with_violations']==0
compile_paths=[runner,EV/'verify_evidence.py',Path(__file__),*(EV/'author_checks').glob('*.py')]
for p in compile_paths:py_compile.compile(str(p),doraise=True)
result={'scope':'Author publication assembly verification, distinct from independent mathematics and formal audit.',
        'note_sha256':sha(note),'runner_sha256':sha(runner),
        'independent_report_sha256':sha(EV/'independent/REPORT.md'),
        'two_complete_source_bodies_match':True,'capsule':capsule,
        'source_scope_check_and_assertion_suites':3,'mutation_rejections':6,
        'cache_status':'fresh','vocabulary_violations':0,'python_sources_compiled':len(compile_paths),
        'graph':{'nodes_added':1,'edges_added':2,'unchanged_prior_manifest_entries':len(old['nodes']),'manifest_sha256':sha(manifest)},
        'pending_before_landing':['combined pipeline','strict audit lint','negative-claim schema','changed-evidence integration']}
(HERE/'AUTHOR_ASSEMBLY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
