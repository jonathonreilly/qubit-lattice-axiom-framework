from pathlib import Path
import json,hashlib,difflib,ast,shutil,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();pin=lambda p:dict(path=p,sha256=sha(W/p));d=json.loads((R/'drain8169-author-prepared-v1.json').read_text());changes=[]
p=W/d['deferred_corrected_proof']['path'];old=p.read_text();new=old.replace('This proof has not\nyet received affected-source confirmation or formal negative certification.','The conditional mathematical proof below is valid under its supplied\nhypotheses. Formal negative certification and active claim promotion are\ndeferred because the actual packet is incomplete; the proof is not rejected\nas false or unproved. Independent affected-source confirmation of these\ncorrected bytes remains required.');assert old!=new;p.write_text(new);changes.append((p,old,new))
p=W/d['notes'][0]['path'];old=p.read_text();new=old.replace('argument is preserved as deferred scientific source; no universal negative','valid conditional argument is preserved as deferred scientific source; no universal negative').replace('The original\nbranch remains a recovery handle for deferred negative certification.','The original\nbranch remains a recovery handle for deferred negative certification. Reopen\nactive promotion only after an honestly complete negative packet and original\nreviewer confirmation; the valid supplied-process proof is not thereby\nrejected as false or unproved.');assert old!=new;p.write_text(new);changes.append((p,old,new))
p=W/d['runners'][0]['path'];old=p.read_text();new=old.replace("{apply_matrix(M,q):Fraction(1)}=={apply_matrix(M,q):Fraction(1)}","{apply_matrix(M,s):v for s,v in {q:Fraction(1)}.items()}=={apply_matrix(M,q):Fraction(1)}")
tree=ast.parse(new);node=next(n for n in tree.body if isinstance(n,ast.Assign) and n.targets[0].id=='EXPECTED_INPUT_SHA256');pins=ast.literal_eval(node.value);pins[d['notes'][0]['path']]=sha(W/d['notes'][0]['path']);lines=new.splitlines(True);lines[node.lineno-1]='EXPECTED_INPUT_SHA256='+repr(pins)+'\n';new=''.join(lines);assert old!=new;compile(new,str(p),'exec');p.write_text(new);changes.append((p,old,new))
patch=''.join(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='v1/'+str(p.relative_to(W)),tofile='v2/'+str(p.relative_to(W)))) for p,a,b in changes);(R/'drain8169-author-v1-to-v2.diff').write_text(patch)
# Update only new versions of reports, retaining every original report/snapshot.
for key in ['notes','runners']:
 d[key]=[pin(x['path']) for x in d[key]]
d['deferred_corrected_proof']=pin(d['deferred_corrected_proof']['path']);d['status']='PROVISIONAL_UNTRACKED_PREPARED_V2_REQUIRES_INDEPENDENT_AFFECTED_REVIEW';d['prior_preparation']=dict(path=str(R/'drain8169-author-prepared-v1.json'),sha256=sha(R/'drain8169-author-prepared-v1.json'));d['scope_guidance']='Original reviewer confirmed proposed split; valid conditional endpoint proof retained, only formal certification/active promotion deferred.'
(R/'drain8169-author-prepared-v2.json').write_text(json.dumps(d,indent=2)+'\n')
m=json.loads((R/'drain8169-author-full-mapping-v1.json').read_text())
for row in m:
 if row['final_path']:row['final_sha256']=sha(W/row['final_path'])
(R/'drain8169-author-full-mapping-v2.json').write_text(json.dumps(m,indent=2)+'\n')
plan=json.loads((R/'drain8169-author-input-resource-plan-v1.json').read_text());plan['runner']=pin(plan['runner']['path']);plan['ordered_inputs']=[pin(x['path']) for x in plan['ordered_inputs']];(R/'drain8169-author-input-resource-plan-v2.json').write_text(json.dumps(plan,indent=2)+'\n')
print('Preserved v1; wrote v2 explicit valid-proof boundary and non-tautological singleton pushforward control.')
