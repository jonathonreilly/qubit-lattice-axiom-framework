from pathlib import Path
import json,hashlib,subprocess,gzip,sys
r=Path('/private/tmp/review-drain-20260915');w=r/'resume-author8077';old='fb13597955e3b167866d02276a7c7794eef83d1c';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));g=lambda *a:subprocess.check_output(['git',*a],cwd=w)
draft=json.loads((r/'resume8077-recovery-draft-report.json').read_text());rec=json.loads((r/'resume8077-unit-draft-v2.json').read_text());assert g('write-tree').decode().strip()=='256f5f598ae9c712b13e27da13d6f9f27de54899';assert not g('diff','--name-only')
paths=rec['source']['paths'];assert len(paths)==529
# Exact frozen-commit byte comparison, independent of recovered helper assertions.
allpaths=sorted(set(x['path'] for x in paths+rec['inputs']['runtime']+rec['inputs']['parents']))
for start in range(0,len(allpaths),64):
 chunk=allpaths[start:start+64];raw=subprocess.check_output(['git','cat-file','--batch','-z'],cwd=w,input=b''.join((old+':'+p).encode()+b'\0' for p in chunk));off=0
 for p in chunk:
  end=raw.index(b'\n',off);fields=raw[off:end].split();assert fields[1]==b'blob';n=int(fields[2]);data=raw[end+1:end+1+n];assert raw[end+1+n:end+2+n]==b'\n';off=end+2+n;assert data==(w/p).read_bytes(),p
 assert off==len(raw)
for group in rec['inputs'].values():
 for x in group:assert sha(w/x['path'])==x['sha256'],x['path']
for x in paths:assert sha(w/x['path'])==x['sha256']
for e in rec['reviewer']['references']:assert sha(Path(e['path']))==e['sha256']
fr=json.loads((w/'docs/work_history/repo/review_feedback/pr8077-forensic-evidence/recovery-manifest.json').read_text());assert len(fr['entries'])==460
for e in fr['entries']:
 p=w/e['stored_repository_path'];data=p.read_bytes();assert sha(p)==e['stored_sha256'];raw=gzip.decompress(data) if e['encoding']=='gzip' else data;assert hashlib.sha256(raw).hexdigest()==e['sha256'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['blob']
# Original complete mode/blob path inventory, including excluded generated manifest.
const=rec['constituents'][0];orig=g('diff','--name-only','--no-renames',const['delta_base'],const['head']).decode().splitlines();assert set(orig)=={x['original_path'] for x in draft['original_dispositions']} and len(orig)==77
for row in draft['original_dispositions']:
 p=row['original_path'];data=g('show',const['head']+':'+p);assert hashlib.sha256(data).hexdigest()==row['original_sha256'];metadata=g('ls-tree',const['head'],'--',p).decode().split('\t')[0].split();row['original_mode']=metadata[0];row['original_git_blob']=metadata[2]
 if row['final_path']:assert sha(w/row['final_path'])==row['final_sha256']
proofs={x['path'] for x in rec['supporting_proofs']};assert len(proofs)==5
for row in draft['original_dispositions']:
 if row['final_path'] in proofs:row['disposition']='Current owned supporting proof fully reviewed in this original session under the canonical projector note; formulas load-bearing, historical worker plans not current executions.'
changes=[]
for category in ('context','tooling'):
 for x in rec['inputs'][category]:
  v=subprocess.run(['git','show',old+':'+x['path']],cwd=w,capture_output=True);oldhash=hashlib.sha256(v.stdout).hexdigest() if v.returncode==0 else None
  if oldhash!=x['sha256']:changes.append(dict(path=x['path'],old_sha256=oldhash,new_sha256=x['sha256'],role='Routed review methodology; complete applicable reference read. No scientific premise or executable evidence change.'))
assert all(x['path'].startswith('docs/ai_methodology/skills/review-loop/') for x in changes)
# Actual source discovery and historical cache status, no scientific imports/runs.
sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')];import build_citation_graph as graph,audit_packet_script_deps as packet,runner_cache
note=rec['notes'][0];p=note['primary_runner'];assert graph.extract_claim_type_hint((w/note['path']).read_text())[1]=='bounded_theorem';assert not graph.helper_runner_paths_for_claim(note['claim_id'],p);assert not packet.transitive_helpers(Path(p).stem);assert runner_cache.declared_timeout_for(p)==30;assert runner_cache.cache_status(p)=='fresh'
actualcites=sorted(x.relative_to(w).as_posix() for x in graph.extract_citations((w/note['path']).read_text(),w/note['path']));assert actualcites==note['citations']
# Current upstream bytes identical, no lost current-main source in this replay.
main='dee2310d375f37a0ca4c8641e9a12aa7fabb8577'
for x in rec['inputs']['parents']:
 if '/work_history/' not in x['path']:assert g('show',main+':'+x['path'])==(w/x['path']).read_bytes()
assert all(l.startswith('A\t') for l in g('diff','--cached','--name-status').decode().splitlines())
limits='Old temporary final report/record/preflight bytes were lost and are NOT reconstructed or represented as recovered. Their prior hashes and authentic original tool log remain provenance. This new report is my genuine same-session new-context confirmation, not a replacement historical receipt. Original primary61/0 capture remains unchanged historical evidence; no primary, oracle, assembly or full pipeline rerun.'
report=dict(draft);report.update(status='FINAL VERDICT: PASS WITH BOUNDED CLAIMS',reviewer='/root/review_8012',original_session='01a0a48b-6cae-7360-a91a-1b93802b0aeb',confirmation_date='2026-09-22',source_tree=rec['source']['tree'],source_base=rec['source']['base'],recovery_limits=limits,methodology_changes=changes,independent_confirmation='I confirm my original scientific reading, proof obligations, independent arithmetic controls and affected packaging conclusions continue to hold for these exact restored bytes and current premises. All529source/cache paths,80declared runtime inputs,77original dispositions,5owned proofs and460recovery rows verified. External elliptic identity remains an explicit supplied mathematical import, not framework-derived law.',lenses={'code':'PASS exact unchanged runner/evidence','physics':'BOUNDED supplied model only','proof':'CONDITIONAL on explicit Hamiltonian/reference/elliptic inputs, analytical descriptor proof closed within them','imports':'DISCLOSED','retention':'BOUNDED, no audit retention','no_go':'PASS scope limits, no universal impossibility','labeling':'PASS algebraic theorem','governance':'PASS ownedproof identity retained, no generated authority imported','methodology':'PASS current routed references consumed; tool bytes unchanged'},remaining='One designated final --cache follows this immutable record. Coordinator separately owns fresh head/current-main integration and combined gate; no audit or publication authority from this source verdict.',new_reads='Original-session recovery request, authentic command evidence and recovery drafts; all applicable routed methodology references; exact input/source/current-parent comparisons and actual discovery/cache APIs. Original complete scientific read reused only for identical hypotheses/bytes.',recovery_draft=ref(r/'resume8077-recovery-draft-report.json'),recovery_record_draft=ref(r/'resume8077-unit-draft-v2.json'),confirmation_script=ref(Path(__file__)),new_primary_or_oracle_runs=0,new_science_source_edits=0,new_full_pipeline_runs=0,new_cache_preflights=0)
md=r/'resume8077-original-session-final.md';jp=r/'resume8077-original-session-final.json';assert not md.exists() and not jp.exists();md.write_text('# PR8077 — FINAL VERDICT: PASS WITH BOUNDED CLAIMS\n\nSame original reviewer session; new-context confirmation on 2026-09-22. Final staged tree `'+rec['source']['tree']+'`.\n\n'+report['scope']+'\n\n'+report['independent_confirmation']+'\n\n'+limits+'\n\nHistorical compact execution:61/0,0.0440907478s,30s/384MiB contract, sampled61,849,600bytes. Current cache bytes remain unchanged and fresh. No new scientific execution.\n\nThe skill now routes detailed requirements to separate references; those applicable references were read fully. Science, dependencies and executable tooling match the preserved reviewed commit. No material new finding. Final mechanical cache check and integration remain separate.\n');report['science_report']=ref(md);jp.write_text(json.dumps(report,indent=2)+'\n');rr=ref(jp)
rec['reviewer']['session']='/root/review_8012 original session01a0a48b-6cae-7360-a91a-1b93802b0aeb';rec['reviewer']['report']=rr;rec['reviewer']['references'] +=[ref(md),ref(Path(__file__)),ref(r/'resume8077-recovery-draft-report.json')];rec['constituents'][0]['dispositions']=dict(rr,json_pointer='/original_dispositions')
for item in rec['supporting_proofs']+rec['non_science_notes']:
 item['review_reference']=rr
 if item in rec['supporting_proofs']:item['rationale']='Current owned analytical proof fully reviewed in original session and same-session exact-byte/current-context confirmation; historical worker language remains provenance, not a new execution.'
fp=r/'resume8077-original-session-final-v2.json';assert not fp.exists();fp.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps({'report':ref(jp),'record':ref(fp),'tree':rec['source']['tree'],'changes':len(changes)},indent=2))
