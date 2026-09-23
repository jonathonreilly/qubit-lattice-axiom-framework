from pathlib import Path
import ast,hashlib,json
R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p))
report=R/'drain8172-early-review-v1.json';review=json.loads(report.read_text());assert sha(report)=='fe87a74880688bbfcc113cb932943ee206dd7aa069882397e0b2c0abfa0ea503'
b=(R/'drain8170-build-staged-draft-v1.py').read_text().replace('8170','8172').replace("W=R/'drain-author-slot'","W=R/'review-meta-slot'").replace("R/'drain-author-slot.json'","R/'review-meta-slot.json'")
b=b.replace('author-prepared-v2','author-prepared-v1').replace('prepared-v2-source-freeze','prepared-v1-source-freeze').replace('author-input-resource-plan-v2','author-input-resource-plan-v1').replace('author-discovery-v2','author-discovery-v1').replace('early-review-v2','early-review-v1')
b=b.replace('len(f)==30','len(f)==31').replace("{'EARLY SOURCE CLEARANCE for staged draft, cold read and bounded capture; NOT final landing PASS'}",repr({review['verdict']})).replace("'01bc3b8aadb5231e4145b7d9fd423727c058de7bf186ea30053abba16707d3e4'",repr(sha(report))).replace("a.review_verdict_pointer=='/decision'","a.review_verdict_pointer=='/verdict'")
b=b.replace("review['source_freeze_sha256']==sha(R/'drain8172-prepared-v1-source-freeze.json') and review['source_files']==f and not review['material_new_findings']","review['source_files']==f and not review['new_findings'] and ref(R/'drain8172-prepared-v1-source-freeze.json') in review['references']")
b=b.replace("R/'drain8172-original/manifest.json'","R/'drain8172-original/inventory.json'").replace("len(originals)==len(mapping)==len(manifest['entries'])==25","len(originals)==len(mapping)==len(manifest['entries'])==24")
b=b.replace("o['head_entry'].split()[:3]==[e['original_mode'],'blob',e['git_blob']]","[o['original']['mode'],'blob',o['original']['blob']]==[e['original_mode'],'blob',e['git_blob']]").replace("o['sha256']==e['raw_sha256']","o['original']['sha256']==e['raw_sha256']")
b=b.replace('import argparse,ast,gzip,hashlib,json,re,subprocess,sys,traceback','import argparse,ast,gzip,hashlib,io,json,re,subprocess,sys,tarfile,traceback')
needle="        sys.path[:0]=[str(W/'scripts'),str(W/'docs/audit/scripts')]"
insert='''        inherited=manifest['inherited_packet'];ip=W/archive/inherited['path'];assert sha(ip)==inherited['stored_sha256']
        tarraw=gzip.decompress(ip.read_bytes());assert hashlib.sha256(tarraw).hexdigest()==inherited['raw_tar_sha256']
        inventory_path=W/archive/inherited['inventory_path'];assert sha(inventory_path)==inherited['inventory_sha256']
        inherited_rows=json.loads(inventory_path.read_text());assert len(inherited_rows)==79
        with tarfile.open(fileobj=io.BytesIO(tarraw)) as tar:
            members={m.name:m for m in tar.getmembers() if m.isfile()}
            assert set(members)=={e['path'] for e in inherited_rows}
            for e in inherited_rows:
                m=members[e['path']];raw=tar.extractfile(m).read()
                assert hashlib.sha256(raw).hexdigest()==e['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\\0'+raw).hexdigest()==e['blob']
                assert (m.mode&0o111)==(int(e['mode'],8)&0o111)
        # Original tar headers are preserved; Git modes in inventory are the restoration authority.
'''
b=b.replace(needle,insert+needle)
b=b.replace("claims=json.loads((R/'drain8172-author-final-read-v2.json').read_text())['claim_dispositions']","claims=json.loads((R/'drain8172-author-finding-dispositions-v1.json').read_text())['claims']")
b=b.replace('One SymPy/standard-library primary plus three literal proof inputs; historical fit/simulation programs and raw histories are never executed','One SymPy/standard-library primary plus three literal proof inputs; historical simulations and all79 inherited entries remain recovery only')
b=b.replace('Complete valid auxiliary obstruction remains readable but its formal negative promotion is deferred; historical failed fits and stronger claims are preserved with branch retention.','Original threshold, sphere coupling and broader scientific claims remain readable with exact failures; formal negative promotion is deferred with branch retention.')
b=b.replace("branch_retention_required=True,registry_changes=[]","branch_retention_required=True,inherited_dispositions=[dict(e,recovery=str(archive/inherited['path'])+' member '+e['path'],mode_recovery='Restore original Git mode from pinned inventory') for e in inherited_rows],registry_changes=[]")
# Pin all external evidence; canonical cache paths remain source/input bindings, never external reviewer references.
names=['drain8172-review-original.json','drain8172-review-original.md','drain8172-author-prepared-v1.json','drain8172-prepared-v1-source-freeze.json','drain8172-author-full-mapping-v2.json','drain8172-author-input-resource-plan-v1.json','drain8172-author-discovery-v1.json','drain8172-author-preservation-v1.json','drain8172-author-finding-dispositions-v1.json','drain8172-author-correction-v2.diff','drain8172-original/inventory.json','drain8172-original/complete-packet-inventory.json','drain8172-original/complete-inherited-packet.tar','drain8172-early-review-v1.json','drain8172-early-review-v1.md']
refs=[ref(R/n) for n in names]+review['references']
refs=list({e['path']:e for e in refs}.values());bp=R/'drain8172-builder-bindings-v1.json';assert not bp.exists();bp.write_text(json.dumps(refs,indent=2)+'\n')
b=b.replace('7046f77df395bbbf136a19b6f2fbd8f5c0d511bb83826ec28c92ff8f23181bdf',sha(bp))
p=R/'drain8172-build-staged-draft-v1.py';assert not p.exists();p.write_text(b)
# v1 captures are intentionally non-dispatchable until a new revision binds actual cold evidence.
for oldname,newname in [('drain8170-capture-v2.py','drain8172-capture-v1.py'),('drain8170-mutation-capture-v1.py','drain8172-mutation-capture-v1.py')]:
 s=(R/oldname).read_text().replace('8170','8172').replace("W=R/'drain-author-slot'","W=R/'review-meta-slot'").replace("R/'drain-author-slot.json'","R/'review-meta-slot.json'")
 s=s.replace('author-input-resource-plan-v2','author-input-resource-plan-v1').replace('early-review-v2','early-review-v1').replace('prepared-v2','prepared-v1')
 s=s.replace('481eb44a14431361852b6cebaa6ba9a9fee33619297a1c2b8b5734c74c3b8c04','8a6c0b8da6c3575158a8c6a5728c977275afce0dbe85083144858404c76ef7a7').replace('01bc3b8aadb5231e4145b7d9fd423727c058de7bf186ea30053abba16707d3e4',sha(report))
 s=s.replace('PASS=17 FAIL=0','PASS=11 FAIL=0').replace("==17","==11").replace('len(mutations)==14','len(mutations)==8')
 s=s.replace("R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'","R=Path('/private/tmp/review-drain-20260915');W=R/'review-meta-slot'\nCOLD_REPORT_BINDING = None  # Future immutable revision must bind actual report path, SHA, verdict pointer/value and tree.")
 # Fail before any reservation, process launch, generated output or staging.
 s=s.replace('def main():\n',"def main():\n    assert COLD_REPORT_BINDING is not None, 'PROPOSED ONLY: root must create new immutable adapter revision binding actual cold clearance'\n",1)
 # New revision cannot gain approval merely by replacing None; exact binding must match actual report.
 marker="assert cold['reviewer_session']=='/root/review_8172' and cold['tree']==record['source']['tree']"
 s=s.replace(marker,marker+"\n    assert COLD_REPORT_BINDING==dict(path=str(cp),sha256=sha(cp),tree=cold['tree'],verdict_pointer=a.cold_verdict_pointer,verdict="+('at' if oldname.endswith('capture-v2.py') else 'pointer')+"(cold,a.cold_verdict_pointer))")
 p=R/newname;assert not p.exists();p.write_text(s)
for name in ['drain8172-build-staged-draft-v1.py','drain8172-capture-v1.py','drain8172-mutation-capture-v1.py']:
 p=R/name;compile(ast.parse(p.read_text()),str(p),'exec')
print(json.dumps([ref(R/n) for n in ['drain8172-build-staged-draft-v1.py','drain8172-capture-v1.py','drain8172-mutation-capture-v1.py','drain8172-builder-bindings-v1.json']],indent=2))
