from pathlib import Path
import hashlib,json,ast,re
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ref=lambda p:dict(path=str(p),sha256=sha(p))
def write(name,s):
 p=R/name
 with p.open('x') as f:f.write(s)
 return p
refs=[R/f'drain8174-author-{n}-v3.json' for n in ['prepared','full-mapping','discovery','input-resource-plan','finding-dispositions','handoff']]+[R/'drain8174-prepared-v3-source-freeze.json',R/'drain8174-packaging-v2-to-v3.diff',R/'drain8174-basename-collision-check-v3.json',R/'drain8174-author-correction-v2.diff',R/'drain8174-author-preservation-v1.json',R/'drain8174-review-original.json',R/'drain8174-early-review-v2.json',R/'drain8174-original/inventory.json',R/'drain8174-original/original.patch']
bp=write('drain8174-builder-bindings-v1.json',json.dumps([ref(p) for p in refs],indent=2)+'\n')
s=(R/'drain8172-build-staged-draft-v1.py').read_text().replace('8172','8174').replace('review-meta-slot','author-draft-slot')
s=s.replace('author-prepared-v1','author-prepared-v3').replace('prepared-v1-source-freeze','prepared-v3-source-freeze').replace('author-input-resource-plan-v1','author-input-resource-plan-v3').replace('author-discovery-v1','author-discovery-v3').replace('author-full-mapping-v2','author-full-mapping-v3').replace('author-finding-dispositions-v1','author-finding-dispositions-v3')
s=s.replace('849643a316435ba1b5c22f5ab2a63eaba02e74b12e7b8a077245c28f96874473',sha(bp))
a=s.index('def report(');b=s.index('\ndef main():',a)
s=s[:a]+'''# Must be bound in a new immutable revision to the actual v3 affected approval.
EARLY_REVIEW_BINDING = None
def report(path,digest,verdict_pointer):
    b=EARLY_REVIEW_BINDING
    assert isinstance(b,dict), 'PROPOSED ONLY: actual v3 same-session approval binding absent'
    p=Path(path);assert p.is_absolute() and p.resolve().is_relative_to(R) and not p.resolve().is_relative_to(W) and not p.is_symlink()
    assert str(p)==b['path'] and sha(p)==digest==b['sha256']
    d=json.loads(p.read_text());assert b['same_session_provenance']=='/root/review_8174'
    assert verdict_pointer==b['verdict_pointer'] and pointer(d,verdict_pointer)==b['verdict_value']
    assert b['prepared_sha256']==sha(R/'drain8174-author-prepared-v3.json') and b['freeze_sha256']==sha(R/'drain8174-prepared-v3-source-freeze.json')
    assert b['required_predicates']
    for key,value in b['required_predicates'].items():assert pointer(d,key)==value
    return p,d
''' +s[b:]
a=s.index('        rp,review=report(');b=s.index('        owner=',a)
s=s[:a]+'        rp,review=report(a.review,a.review_sha256,a.review_verdict_pointer)\n'+s[b:]
s=s.replace("plan['ordered_inputs']+plan['context_only']","plan['ordered_inputs']")
s=s.replace("==24 and set(originals)","==25 and set(originals)")
s=s.replace("[o['original']['mode'],'blob',o['original']['blob']]","o['head'].split('\\t')[0].split()")
s=s.replace("o['original']['sha256']","o['head_sha256']")
a=s.index("        inherited=manifest['inherited_packet']");b=s.index('        sys.path[:0]',a)
s=s[:a]+'''        delta=manifest['delta'];delta_path=W/archive/delta['path']
        assert sha(delta_path)==delta['stored_sha256']
        assert hashlib.sha256(gzip.decompress(delta_path.read_bytes())).hexdigest()==delta['raw_sha256']==inv['delta_sha256']
        # Global basename collision check against the actual expected current main.
        existing=git('ls-tree','-r','--name-only',a.expected_base,'--','docs').splitlines()
        for e in f:
            if e['path'].endswith('.md') and Path(e['path']).name not in ('README.md','SKILL.md'):
                assert not any(Path(p).name.casefold()==Path(e['path']).name.casefold() for p in existing), 'New Markdown basename collision'
''' +s[b:]
s=s.replace("{e['path'] for e in plan['context_only']}|",'')
s=s.replace("runtime_scope='One SymPy/standard-library primary plus three literal proof inputs; historical simulations and all79 inherited entries remain recovery only'","runtime_scope=plan['runtime_read_set']")
a=s.index(',inherited_dispositions=');b=s.index(',registry_changes=',a);s=s[:a]+s[b:]
s=s.replace('Original threshold, sphere coupling and broader scientific claims','Original threshold, route-ceiling and broader scientific claims')
s=s.replace("evidence=refs+[ref(rp)]","evidence=refs+[ref(rp),ref(bp),ref(Path(__file__).resolve())]")
# bp is scoped path used above, keep one concrete name.
s=s.replace("        assert sha(R/'drain8174-builder-bindings-v1.json')", "        bp=R/'drain8174-builder-bindings-v1.json'\n        assert sha(R/'drain8174-builder-bindings-v1.json')")
builder=write('drain8174-build-staged-draft-v1.py',s)
# Generic actual-schema cold binding copied from 8173; no speculative verdict enum.
coldtemplate=(R/'drain8173-capture-v1.py').read_text();a=coldtemplate.index('# Deliberately unbound:');b=coldtemplate.index('\ndef main():',a);cold=coldtemplate[a:b].replace('8173','8174')
planpath=R/'drain8174-author-input-resource-plan-v3.json';plsha=sha(planpath)
for name in ['capture','mutation-capture']:
 s=(R/f'drain8172-{name}-v1.py').read_text().replace('8172','8174').replace('review-meta-slot','author-draft-slot').replace('author-input-resource-plan-v1','author-input-resource-plan-v3')
 s=s.replace("COLD_REPORT_BINDING = None  # Future immutable revision must bind actual report path, SHA, verdict pointer/value and tree.\n",'')
 s=s.replace("    assert COLD_REPORT_BINDING is not None, 'PROPOSED ONLY: root must create new immutable adapter revision binding actual cold clearance'\n",'')
 s=s.replace("'cold-verdict-pointer',",'')
 a=s.index("    assert cold['reviewer_session']");b=s.index('\n    assert ',s.index('Unknown cold verdict' if name=='mutation-capture' else 'Unrecognized cold verdict',a))
 s=s[:a]+"    confirm_cold(cp,cold,record['source']['tree'])"+s[b:]
 s=s.replace('\ndef main():','\n'+cold+'\ndef main():',1)
 s=s.replace('8a6c0b8da6c3575158a8c6a5728c977275afce0dbe85083144858404c76ef7a7',plsha)
 s=s.replace("    early=R/'drain8174-early-review-v1.json';assert sha(early)=='fe87a74880688bbfcc113cb932943ee206dd7aa069882397e0b2c0abfa0ea503'\n",'')
 s=s.replace('PASS=11','PASS=17').replace("['passed']==11","['passed']==17").replace("['checks'])==11","['checks'])==17").replace('len(checks)==11','len(checks)==17').replace("['failed']==11","['failed']==17").replace('len(mutations)==8','len(mutations)==11')
 s=s.replace('prepared-v1-attempt','prepared-v3-attempt').replace('prepared-v1-{name}','prepared-v3-{name}')
 write(f'drain8174-{name}-v1.py',s)
for p in [builder,R/'drain8174-capture-v1.py',R/'drain8174-mutation-capture-v1.py']:compile(p.read_text(),str(p),'exec')
plan=json.loads(planpath.read_text())
plan.update(status='PROPOSED ONLY: all adapters unexecuted; new immutable revisions must bind actual v3 early approval and actual staged cold report schemas',baseline_runs_planned=1,mutation_runs_planned=11,baseline_retry=False,mutation_retry=False,adapters=[ref(p) for p in [builder,R/'drain8174-capture-v1.py',R/'drain8174-mutation-capture-v1.py']],ordering=['Actual v3 packaging confirmation; new immutable builder revision binding exact approval','Root guarded advance and staging, cheap receipt, actual same-session cold/new-main clearance','New immutable capture revisions binding actual cold schema, report hash, exact tree and predicates','One primary, full execute_runner return saved externally before API postidentity checks','Eleven serial once-only mutation attempts reuse unchanged successful primary; no baseline rerun','No cache staging until all source-bound captures complete'],raw_preservation='Primary raw execute_runner return persisted immediately before original execute_and_write_cache identity/cache publication logic; mutation stdout/stderr stream to exclusive external files before any postrun rejection; all actual JSON paths are retained',limit_policy='900seconds and768MiB sampled aggregate RSS of supervisor and descendants, 20ms polling; kill observed process group/children on violation; no automatic retry or raised cap',scratch='None. Runner emits distinct exclusive JSON per mutation name.',cold_binding=None,early_v3_binding=None)
pp=write('drain8174-capture-plan-v1.json',json.dumps(plan,indent=2)+'\n')
print(json.dumps([ref(p) for p in [builder,R/'drain8174-capture-v1.py',R/'drain8174-mutation-capture-v1.py',bp,pp]],indent=2))
