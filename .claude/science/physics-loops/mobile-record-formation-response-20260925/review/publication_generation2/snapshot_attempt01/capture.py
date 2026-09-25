from pathlib import Path
import json,hashlib,datetime,difflib
E=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth');I=E/'formation-response-sum-independent';G1=I/'publication_comparison';D=I/'publication_comparison_generation2';P=E/'formation-response-publication'
assert not D.exists();D.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((E/'FORMATION_RESPONSE_GENERATION2_FROZEN_SOURCES.json').read_text())
assert manifest['source_files_sha256'][manifest['note']]=='fb7e648244754b469504f08aa4cd251148d3736740af4f55c7e5c63675c23d14'
entries=[]
for rel,expected in manifest['files_sha256'].items():
 origin=P/rel;assert sha(origin)==expected
 snapshot=D/'sources/publication'/rel;snapshot.parent.mkdir(parents=True,exist_ok=True);snapshot.write_bytes(origin.read_bytes());snapshot.chmod(0o444)
 entries.append({'origin':str(origin),'snapshot':snapshot.relative_to(D).as_posix(),'sha256':expected,'bytes':origin.stat().st_size,'scope':'Released generation2 canonical content or fresh evidence; read only.'})
for rel in ['FORMATION_RESPONSE_GENERATION2_REPAIR.json','FORMATION_RESPONSE_GENERATION2_CACHE_EXECUTION.json','FORMATION_RESPONSE_GENERATION2_FROZEN_SOURCES.json','FORMATION_RESPONSE_GENERATION2_PRIMARY_ROOT_VERIFICATION.json','repair_formation_response_publication_generation2.py','FORMATION_RESPONSE_GENERATION1_ROOT_REVIEW.json','FORMATION_RESPONSE_GENERATION1_READONLY_RESULT.json']:
 origin=E/rel;snapshot=D/'sources/external'/rel;snapshot.parent.mkdir(parents=True,exist_ok=True);snapshot.write_bytes(origin.read_bytes());snapshot.chmod(0o444)
 entries.append({'origin':str(origin),'snapshot':snapshot.relative_to(D).as_posix(),'sha256':sha(origin),'bytes':origin.stat().st_size,'scope':'Released repair/execution/review provenance; no program executed or imported.'})
seals=[]
for path,expected in [(I/'PRE_SEAL.json','d65cdc1e27cd6757c9437f62cec7c45bfa7a3c850da4c5f2f2fe510983c00dad'),(I/'POST_SEAL.json','79359f5d5cddd65d799a6eba47aec005a10d2b3f708a32264b263f9df5f0d9db'),(G1/'PUBLICATION_COMPARISON_SEAL.json','79e3d680e9316faa167b18f44a5f66f6a27cebb8ce33d8081f82c19b77fa55dd')]:
 assert sha(path)==expected;s=json.loads(path.read_text())
 for row in s['members']:assert sha(path.parent/row['path'])==row['sha256']
 seals.append({'origin':str(path),'sha256':expected,'members':len(s['members'])})
pins={'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'Focused corrected-generation correspondence only','sources':entries,'prior_seals':seals,'prior_proof_and_code_review_reused':True,'mutations_outside_this_new_directory':False}
(D/'SOURCE_PINS_INITIAL.json').write_text(json.dumps(pins,indent=2)+'\n')
old=(G1/'sources_initial/publication'/manifest['note']).read_text();new=(D/'sources/publication'/manifest['note']).read_text();replacement=json.loads((G1/'REQUIRED_FRONT_REPLACEMENT.json').read_text())
assert old.count(replacement['old'])==1;assert old.replace(replacement['old'],replacement['new'])==new
change=''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='sealed-generation1',tofile='corrected-generation2'))
(D/'SOLE_NOTE_CHANGE.diff').write_text(change)
print(json.dumps({'source_count':len(entries),'prior_members_preserved':sum(s['members'] for s in seals),'manifest_sha256':sha(E/'FORMATION_RESPONSE_GENERATION2_FROZEN_SOURCES.json'),'new_note_sha256':sha(D/'sources/publication'/manifest['note']),'initial_pins_sha256':sha(D/'SOURCE_PINS_INITIAL.json')},indent=2));print(change)
print((D/'sources/publication'/manifest['cache']).read_text())
oldreport=json.loads((G1/'verification_attempt01/VERIFICATION_REPORT.json').read_text());rootreport=json.loads((D/'sources/external/FORMATION_RESPONSE_GENERATION1_READONLY_RESULT.json').read_text());assert set(oldreport)==set(rootreport)
diff=[(k,oldreport[k],rootreport[k]) for k in oldreport if oldreport[k]!=rootreport[k]];assert len(diff)==1 and diff[0][0]=='verified_utc'
print(json.dumps({'root_generation1_report_delta':diff},indent=2))
