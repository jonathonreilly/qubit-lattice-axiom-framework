from pathlib import Path
import json,gzip,hashlib,subprocess
r=Path('/private/tmp/review-drain-20260915');w=r/'review-slot-one';src=r/'check8075/required-forensic-payloads.json';d=json.loads(src.read_text());assert not d['missing_scientific_inputs'];dest=w/'docs/work_history/repo/review_feedback/pr8075-evidence/scientific-recovery';dest.mkdir(parents=True,exist_ok=False);obj=dest/'objects';obj.mkdir();sha=lambda b:hashlib.sha256(b).hexdigest();objects={}
for digest,x in d['objects'].items():
 raw=Path(x['raw_path']).read_bytes();assert sha(raw)==digest and len(raw)==x['raw_bytes'];compressed=gzip.compress(raw,mtime=0);assert gzip.decompress(compressed)==raw;q=obj/(digest+'.gz');q.write_bytes(compressed);objects[digest]={'path':q.relative_to(dest).as_posix(),'raw_bytes':len(raw),'compressed_bytes':len(compressed),'compressed_sha256':sha(compressed)}
lookup={}
for commit in sorted({x['commit'] for x in d['rows']}):
 needed={x['path'] for x in d['rows'] if x['commit']==commit};raw=subprocess.check_output(['git','ls-tree','-r','-z',commit],cwd=w)
 for row in raw.split(b'\0'):
  if not row:continue
  meta,path=row.split(b'\t',1);p=path.decode()
  if p in needed:mode,kind,blob=meta.decode().split();lookup[(commit,p)]=(mode,kind,blob)
 assert needed<=set(p for c,p in lookup if c==commit)
rows=[]
for x in d['rows']:
 mode,kind,blob=lookup[x['commit'],x['path']];assert kind=='blob' and mode in ['100644','100755'];raw=Path(d['objects'][x['sha256']]['raw_path']).read_bytes();gitblob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();assert gitblob==blob;rows.append({**x,'git_mode':mode,'git_blob':blob,'object':objects[x['sha256']]['path']})
manifest={'schema_version':1,'scope':'Exact scientific producer/checker/input and declared checkpoint recovery; historical environment remains external, no execution or independent verdict created.','source_inventory_sha256':sha(src.read_bytes()),'rows':rows,'objects':objects,'external_historical_runtime':d['external_runtime'],'boundary':d['boundary']};(dest/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(dest/'README.md').write_text('# Scientific recovery for PR8075\n\nThe manifest maps every preserved source/data path to its original commit, Git mode/blob and decoded SHA-256. Objects use deterministic gzip; decode the named object and verify its SHA-256 before use. These exact historical scientific bytes support the current independent source review. Installed/system runtime hashes remain explicitly external historical environment provenance. This recovery does not execute old workers or grant a review/audit verdict.\n')
note=w/'docs/NATIVE_RHO4_MOMENT_CERTIFICATES_NOTE_2026-09-09.md';s=note.read_text();old='The compact local bundle omits large raw catalogs and installed runtimes deliberately; it is sufficient for the stated compact identity/binding verifier, not a standalone full scientific replay. Reconstructing that larger replay requires the exact recovery paths and a separate execution contract.';assert old in s;s=s.replace(old,'The original compact bundle omitted large raw catalogs and installed runtimes. The current [scientific recovery](work_history/repo/review_feedback/pr8075-evidence/scientific-recovery/README.md) now preserves the exact required scientific source, catalog, saved-stage and checker payloads with their commit, Git mode/blob and decoded hashes. Installed/system runtime hashes remain external historical environment provenance. The compact verifier still does not replay the contractions; a larger replay requires a separately specified environment and execution contract.');note.write_text(s)
mp=w/'outputs/native_rho4_moment_certificates_2026_09_09_inputs/SOURCE_MANIFEST.json';m=json.loads(mp.read_text());changes={}
for p in m:
 h=sha((w/p).read_bytes())
 if m[p]!=h:changes[p]={'prior':m[p],'current':h};m[p]=h
assert set(changes)=={'docs/NATIVE_RHO4_MOMENT_CERTIFICATES_NOTE_2026-09-09.md','scripts/native_rho4_moment_certificates_2026_09_09.py'};mp.write_text(json.dumps(m,indent=2)+'\n');subprocess.run(['git','add',str(dest),str(note),str(mp)],cwd=w,check=True);subprocess.run(['git','diff','--cached','--check'],cwd=w,check=True)
g=lambda *a:subprocess.check_output(['git',*a],cwd=w,text=True).strip();paths=g('diff','--cached','--name-only').splitlines();inputs={p:sha((w/p).read_bytes()) for p in [*m,str(mp.relative_to(w))]};sources={p:sha((w/p).read_bytes()) for p in paths};f={'role':'Author current source/input binding; independent review pending','base':g('rev-parse','HEAD'),'tree':g('write-tree'),'source_paths':sources,'nonoutput_sources':sources,'inputs':inputs,'outputs':[],'pin_changes':changes,'forensic_recovery':{'rows':len(rows),'objects':len(objects),'compressed_bytes':sum(x['compressed_bytes'] for x in objects.values()),'manifest_sha256':sha((dest/'manifest.json').read_bytes())}};(r/'8075-author-preexecution.json').write_text(json.dumps(f,indent=2)+'\n');print(f['tree'],len(sources),f['forensic_recovery'])
