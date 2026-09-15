from pathlib import Path
import json,hashlib,subprocess,copy
r=Path('/private/tmp/review-drain-20260915');w=r/'author-pool/author-backlog';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));f=json.loads((r/'8061-author-recapture-preexecution.json').read_text());old=json.loads((r/'8061-author-preexecution.json').read_text());rec=json.loads((r/'8061-unit-preexecution-v2.json').read_text());report=json.loads((r/'review-8061-provisional.json').read_text())
assert subprocess.check_output(['git','-C',str(w),'write-tree'],text=True).strip()==f['tree']
for p,h in (f['source_paths']|f['inputs']).items():assert sha(w/p)==h,p
changed=[p for p,h in old['nonoutput_sources'].items() if sha(w/p)!=h];assert set(changed)=={'scripts/native_l6_nonlinear_star_vertex_2026_09_09.py','outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/SOURCE_MANIFEST.json'}
report.update(tree=f['tree'],source_hashes=f['source_paths'],actual_inputs=f['inputs'],status='Affected source cold confirmation complete;8059 actual capture retained,8061 corrected capture pending; no final verdict',previous_provisional_report=ref(r/'review-8061-provisional.json'),failure=ref(r/'8061-first-capture-failure.json'),failure_independent_binding=ref(r/'check8061/failed-capture-binding.json'),capture_wrapper=ref(r/'8061-author-recapture.py'),correction='Only8061 progress/failure diagnostics moved outside input ancestors and manifest source pin refreshed. Source diagnostics reject in-repo destinations; fallback temporary path remains external. External capture persists watchdog/error even cache API raises. Mathematical computations unchanged.8059 source/input/cache/receipt unchanged and not rerun.')
for rows in report['constituent_dispositions'].values():
 for row in rows:
  if row['final_path']:row['final_sha256']=sha(w/row['final_path'])
p=r/'review-8061-affected-provisional.json';assert not p.exists();p.write_text(json.dumps(report,indent=2)+'\n');rr=ref(p)
rec['source']['tree']=f['tree'];rec['source']['paths']=[dict(path=p,sha256=h) for p,h in sorted(f['source_paths'].items())]
for c in rec['constituents']:c['dispositions']=dict(rr,json_pointer='/constituent_dispositions/'+c['id'][2:])
rec['reviewer']['report']=rr;rec['reviewer']['references'] += [ref(r/'review-8061-provisional.json'),ref(r/'8061-first-capture-failure.json'),ref(r/'check8061/failed-capture-binding.json'),ref(r/'8061-author-recapture.py'),ref(r/'8059-author-final-execution.json')]
for section in ['supporting_proofs','non_science_notes']:
 for item in rec[section]:item['review_reference']=rr
for items in rec['inputs'].values():
 for item in items:item['sha256']=sha(w/item['path'])
p=r/'8061-unit-recapture-preexecution-v2.json';assert not p.exists();p.write_text(json.dumps(rec,indent=2)+'\n');print(f['tree'],changed)
