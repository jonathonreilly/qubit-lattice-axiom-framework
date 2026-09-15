from pathlib import Path
import json,hashlib,subprocess,sys,ast
w=Path.cwd();r=w.parent;j=json.loads((r/'check8071/inventory.json').read_text())
g=lambda *a:subprocess.check_output(['git',*a],text=True).strip()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not g('status','--porcelain');base=g('rev-parse','HEAD')
patch=subprocess.check_output(['git','diff','--binary',j['original_base'],j['head'],'--',*j['canonical']])
(r/'8071-author-original-source.patch').write_bytes(patch);subprocess.run(['git','apply','--index'],input=patch,check=True)
sys.path.insert(0,'/Users/jonBridger/.codex/skills/review-loop/scripts');import review_workspace as op
dest=w/'docs/work_history/repo/review_feedback/pr8071-evidence'
m=op.archive(w,j['head'],'.claude/science/physics-loops/native-mixed-gaussian-transition-20260909/',dest,['REVIEW_HISTORY.md','HANDOFF.md'],'pr8071')
(r/'8071-author-archive.json').write_text(json.dumps(m,indent=2)+'\n');op.verify_archive(dest,sha(dest/'archive-manifest.json'))
stem='native_mixed_gaussian_transition_2026_09_09';manifest=w/f'outputs/{stem}_inputs/SOURCE_MANIFEST.json'
pins=json.loads(manifest.read_text())['inputs']
for p in [f'outputs/{stem}.json',str(manifest.relative_to(w))]:
 q=dest/('original-'+Path(p).name);q.write_bytes((w/p).read_bytes())
primary=w/f'scripts/{stem}.py';s=primary.read_text()
s=s.replace('import argparse, contextlib, hashlib, io, json','import argparse, contextlib, hashlib, io, json, importlib.util')
boot="import os,sys\nif __name__=='__main__' and not (sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site and sys.flags.optimize==2):\n os.execv(sys.executable,[sys.executable,'-I','-B','-S','-OO',__file__,*sys.argv[1:]])\n"
s=s.replace('import argparse,',boot+'import argparse,',1)
loaders=[]
for name in ['fock','fast']:
 rel=f'scripts/{stem}_{name}.py'
 loaders.append(f"def _capture_{name}(root):\n path=root/{rel!r}\n out=io.StringIO()\n with contextlib.redirect_stdout(out):\n  spec=importlib.util.spec_from_file_location('__main__',root/{rel!r});module=importlib.util.module_from_spec(spec)\n  exec(compile((root/{rel!r}).read_bytes(),str(path),'exec'),module.__dict__)\n return json.loads(out.getvalue())\n")
metadata='AUDIT_TIMEOUT_SEC=30\nAUDIT_INPUT_PATHS='+repr(tuple([*pins,str(manifest.relative_to(w))]))+'\n\n'
s=s.replace('def main():',metadata+'\n'.join(loaders)+'\ndef main():',1)
old=" for name,count in [('fock',716),('fast',16)]:\n  path=root/('scripts/native_mixed_gaussian_transition_2026_09_09_'+name+'.py')\n  out=io.StringIO()\n  with contextlib.redirect_stdout(out):exec(compile(path.read_bytes(),str(path),'exec'),{'__name__':'__main__','__file__':str(path)})\n  row=json.loads(out.getvalue())"
new=" for loader,count in [(_capture_fock,716),(_capture_fast,16)]:\n  row=loader(root)"
assert s.count(old)==1;s=s.replace(old,new)
old=" print(json.dumps(result,sort_keys=True,indent=2))"
new=f" payload=json.dumps(result,sort_keys=True,indent=2)+'\\n';(root/'outputs/{stem}.json').write_text(payload);print(payload,end='')\n print('TOTAL: PASS='+str(sum(row['predicates'] for row in reports))+' FAIL=0')\n print('per_element: literal synthetic ordered CAR and rational identities are checked; no native matrix is evaluated.')\n print('per_site: only declared two-mode and four-mode synthetic fixtures execute; no native spatial propagation is performed.')\n print('per_mode: relative pairing frames and Majorana signs are analytical obligations and synthetic finite controls, not computed native orbitals.')\n print('per_block:716 Fock predicates include one resource predicate;16 exact fast controls check finite arithmetic, not physical solver mutants.')\n print('lattice_wide: infinite overlap positivity and tail estimates are conditional analytical results; no alpha value, amplitude floor or native evolution is computed.')"
assert s.count(old)==1;s=s.replace(old,new);ast.parse(s);primary.write_text(s)
helper=w/f'scripts/{stem}_fock.py';s=helper.read_text();s=s.replace('import json,signal,time,resource','import json,signal,time,resource,sys');old='rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss';assert s.count(old)==1;s=s.replace(old,old+"*(1 if sys.platform=='darwin' else 1024)");helper.write_text(s)
note=w/'docs/NATIVE_MIXED_GAUSSIAN_TRANSITION_NOTE_2026-09-09.md';s=note.read_text();marker='# Positive mixed Gaussian overlaps and certified transition arithmetic\n';assert s.count(marker)==1;s=s.replace(marker,marker+'\n**Type:** bounded_theorem\n',1)
s+='''

## Canonical evidence and original recovery

The [canonical cache](../logs/runner-cache/native_mixed_gaussian_transition_2026_09_09.txt) records the actual finite supporting controls under the original isolated 30-second and 384MiB contract. Memory supervision samples the executing process tree. No native evolution or physical oracle is launched.

The [original packet](work_history/repo/review_feedback/pr8071-evidence/README.md) preserves source history and historical review statements. The raw paired provenance remains readable and hash-bound. Historical review labels are provenance, not a current source verdict. Current parent and helper pins are refreshed only after their scope and source changes are reviewed.

## No-Go Discipline Gate

**N1 — Tested and analytical alternatives.** Literal finite CAR controls distinguish contraction order and signs. The proof separately controls positive overlap phase, inverse residuals, determinant signs, logarithm enclosures and omitted Hilbert–Schmidt tails. These are finite controls and explicit analytical obligations, not completed native physical attempts.

**N2 — Common scope.** The conclusions concern real skew pairings in one common reference disk and supplied certified approximations. They do not exclude other frames or computational representations.

**N3 — Premises.** The linked imaginary-time reference-chart and Ward Fock/scalar results supply the stated model premises. No Green scalar certificate, new framework axiom or physical encoding is inferred.

**N4 — Provenance.** Preserved proof snapshots and prior reviews document the original derivation. Current claims are stated in this canonical argument and require the actual common frame, pairing norms and error allocations.

**N5 — Coverage.** The primary executes716 literal Fock predicates including one resource predicate and16 rational arithmetic predicates. Infinite-volume overlap and convergence are analytical. No native matrix or overlap is computed.

**N6 — Remaining routes.** Certified native pairings, residuals and Hilbert–Schmidt tails could instantiate the conditional formulas. A positive overlap alone gives no dimension-independent amplitude floor or positive inserted kernel.

**N7 — Next obligation.** Certify the common finite frame, matrix inputs, residuals, scalar enclosures and omitted tails before reporting physical transition kernels or algorithmic cost.

**N8 — Result boundary.** The construction supplies bounded overlap and transition arithmetic within the stated chart. It supplies neither an alpha value nor an autonomous interacting phase.
''';note.write_text(s)
# Keep the original source manifest unchanged until independent parent/source confirmation.
subprocess.run(['git','add','--',*j['canonical'],str(dest)],check=True);paths=g('diff','--cached','--name-only').splitlines()
subprocess.run(['python3','scripts/vocab_lint.py','--fix','--report-path',str(r/'8071-author-vocab.json'),*paths],check=True);subprocess.run(['git','add','--',*paths],check=True)
for a in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git',*a],check=True)
out={'base':base,'draft_tree':g('write-tree'),'source_paths':{p:sha(w/p) for p in paths},'archive_manifest_sha256':sha(dest/'archive-manifest.json'),'capture':'not executed','original_cap':'30seconds/384MiB, isolated-I-B-S-OO','pending':'Original manifest pins intentionally stale pending independent current-parent/source confirmation; then refresh exact pins and freeze before preflight. Supporting-proof classification belongs to full independent review.'}
(r/'8071-author-draft.json').write_text(json.dumps(out,indent=2)+'\n');print(len(paths),out['draft_tree'])
