import pathlib,json,gzip,hashlib,ast,subprocess
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'review-draft-slot';sha=lambda b:hashlib.sha256(b).hexdigest(); p=r/'drain8031-author-prepared-v2.json'; d=json.loads(p.read_text());assert sha(p.read_bytes())=='f206fc8429d05078570eb74b21a14b6b7ed025e10ffb5284b3848bba8bcc181d'
for x in d['source']:assert sha((w/x['path']).read_bytes())==x['sha256']
for x in d['historical_v1_snapshots']:assert sha(pathlib.Path(x['path']).read_bytes())==x['sha256']
o=json.loads((r/'drain8031-original-manifest.json').read_text());old={x['path']:x for x in o['files']};assert old.keys()=={x['path']for x in d['original_dispositions']}
for x in d['original_dispositions']:
 a=old[x['path']]
 for k in ['mode','blob','sha256','size']:assert a[k]==x[k]
 b=gzip.decompress((w/x['recovery']).read_bytes());assert b==(r/'drain8031-originals'/x['path']).read_bytes()
np=d['source'][0]['path'];new=(w/np).read_text();v1=(r/'drain8031-canonical-note-snapshot-v1.md').read_text();part=lambda s:s[s.index('## 2. Actual'):s.index('## Appendix A.')];assert part(new)==part(v1)
runner='scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py';nr=(w/runner).read_text();vr=(r/'drain8031-canonical-runner-snapshot-v1.py').read_text();assert vr.replace('e5f9b9071129565678e8be8a84e5a20d1dd5c9eac3c4d1dc8fdfa14d2575da1e','1bec26d34646291914bd8a2b980103bf7ca5bf07815a10f76b945c97fb4ecade')==nr;ast.parse(nr)
for p,h in d['runtime_inputs'].items():assert sha((w/p).read_bytes())==h
repo=r/'integration-resume';main=subprocess.check_output(['git','-C',str(repo),'rev-parse','ea403fe1']).decode().strip();parent='docs/GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md';b=subprocess.check_output(['git','-C',str(repo),'show',main+':'+parent]);assert sha(b)==d['runtime_inputs'][parent]
result={'prepared_sha256':sha((r/'drain8031-author-prepared-v2.json').read_bytes()),'verified_source_paths':74,'exact_archive_paths':70,'v1_external_snapshots_verified':2,'positive_sections_2_through_5_byte_identical':True,'runner_changed_only_note_pin':True,'parent_current_main':main,'parent_sha256':sha(b),'runtime_inputs':d['runtime_inputs'],'runner_sha256':sha(nr.encode()),'scope':'read-only hash/archive/AST verification, no primary execution'}
(r/'drain8031-early-verification-v2.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
