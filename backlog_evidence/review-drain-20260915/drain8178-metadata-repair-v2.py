from pathlib import Path
import copy,difflib,hashlib,json,os,shutil,subprocess,sys
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=h(p))
def save(n,d):
 p=R/n
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
 return p
D=json.loads((R/'drain8178-author-prepared-v1.json').read_text());oldfreeze=json.loads((R/'drain8178-prepared-v1-source-freeze.json').read_text());assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8178-author'
for e in oldfreeze['files']:assert h(W/e['path'])==e['sha256']
p=W/D['note'];old=p.read_text();anchor='# Supplied torus auxiliary field: mode variance and a finite bracket\n';assert old.count(anchor)==1;new=old.replace(anchor,anchor+'\n**Type:** bounded_theorem\n',1);p.write_text(new)
# No scientific code or mathematical prose was changed.
assert new.replace('\n**Type:** bounded_theorem\n','',1)==old
proc=subprocess.run(['python3',str(W/'scripts/vocab_lint.py'),'--fix','--report-path',str(R/'drain8178-vocab-report-v2.json'),*[str(W/e['path']) for e in oldfreeze['files']]],cwd=W,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});assert proc.returncode==0 and p.read_text()==new
F=R/'drain8178-prepared-v2-source';assert not F.exists();f=[]
for e in oldfreeze['files']:
 q=W/e['path'];v=dict(e,sha256=h(q),bytes=q.stat().st_size);f.append(v);target=F/e['path'];target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(q,target)
 if e['path']!=D['note']:assert v==e
fp=save('drain8178-prepared-v2-source-freeze.json',dict(oldfreeze,files=f));D['source_files']=f;D['status']='Author metadata repair only; explicit native Type added, same-session affected confirmation pending';dp=save('drain8178-author-prepared-v2.json',D)
vp=save('drain8178-vocab-verification-v2.json',{'command':'vocab_lint.py --fix all43 owned paths','exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr,'before':f,'after':f,'changed':[],'exact_metadata_change':{'path':D['note'],'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':h(p)}})
patch=R/'drain8178-author-v1-to-v2.diff'
with patch.open('x') as o:o.write(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=D['note']+'@v1',tofile=D['note']+'@v2')))
sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]
import runner_cache as c,build_citation_graph as g,audit_packet_script_deps as a
assert g.extract_claim_type_hint(new)==('bounded_theorem','bounded_theorem')
dis=json.loads((R/'drain8178-author-discovery-v1.json').read_text());dis['ordered_inputs']=[dict(path=i,sha256=h(W/i)) for i in D['runtime_inputs']];dis['actual_input_fingerprint']=c.declared_input_fingerprint(W/D['runner']);dis['actual_type_extractor']=list(g.extract_claim_type_hint(new));dis['metadata_revision']='v2; Type only; runtime program unchanged';dis['resolved_citations']=sorted(q.relative_to(W).as_posix() for q in g.extract_citations(new,p))
assert dis['resolved_citations']==json.loads((R/'drain8178-author-discovery-v1.json').read_text())['resolved_citations']
for e in dis['context']:
 if e['path']==D['note']:e.update(sha256=h(p),immutable_copy=str(F/D['note']))
disp=save('drain8178-author-discovery-v2.json',dis)
plan=json.loads((R/'drain8178-author-input-resource-plan-v1.json').read_text());plan['ordered_inputs']=dis['ordered_inputs'];plan['status']='v2 native Type metadata repair; source reviewer confirmation and later cold clearance pending';planp=save('drain8178-author-input-resource-plan-v2.json',plan)
oldhandoff=json.loads((R/'drain8178-author-handoff-v1.json').read_text());hand=dict(oldhandoff,source_files=f,status='V2 TYPE METADATA REPAIR FOR SAME-SESSION AFFECTED CONFIRMATION; no mathematical or program changes',actual_api_discovery=ref(disp),resource_plan=ref(planp),prior_handoff=ref(R/'drain8178-author-handoff-v1.json'),early_source_review=ref(R/'drain8178-early-review-v1.json'),metadata_affected_confirmation=None)
hand['references']=oldhandoff['references']+[ref(x) for x in [fp,dp,vp,patch,disp,planp]]
hp=save('drain8178-author-handoff-v2.json',hand)
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only','HEAD'],text=True).strip()
print(json.dumps({'handoff':ref(hp),'prepared':ref(dp),'freeze':ref(fp),'discovery':ref(disp),'vocab':ref(vp),'diff':ref(patch)},indent=2))
