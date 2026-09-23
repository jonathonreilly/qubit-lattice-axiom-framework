from pathlib import Path
import json,hashlib,gzip,subprocess,shutil,difflib
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
freeze=json.loads((R/'drain8169-prepared-v2-source-freeze.json').read_text())['files'];paths=[e['path'] for e in freeze]
assert json.loads((R/'author-draft-slot.json').read_text())['owner']=='PR8169-author'
assert git('rev-parse','HEAD')=='a9f71131f2772035c55fa4a851c0832a5cb82d00'
assert not git('diff','--name-only')
assert set(git('diff','--cached','--name-only').splitlines())==set(paths)
assert all(line.startswith('A\t') for line in git('diff','--cached','--name-status').splitlines())
for e in freeze:
 assert sha(W/e['path'])==sha(Path(e['immutable_copy']))==e['sha256']
 assert oct((W/e['path']).stat().st_mode&0o777)==e['mode']
 assert hashlib.sha256(subprocess.check_output(['git','-C',str(W),'show',':'+e['path']])).hexdigest()==e['sha256']
assert not (R/'drain8169-author-prepared-v3.json').exists()
subprocess.run(['git','-C',str(W),'restore','--staged','--',*paths],check=True)
assert not git('diff','--cached','--name-only') and not git('diff','--name-only','HEAD')
prep=json.loads((R/'drain8169-author-prepared-v2.json').read_text());mp=W/prep['archive_manifest']['path'];manifest=json.loads(mp.read_text());archive=mp.parent
entry=next(e for e in manifest['entries'] if e['original_path'].endswith('.txt'))
old=archive/entry['stored_path'];raw=old.read_bytes();assert hashlib.sha256(raw).hexdigest()==entry['raw_sha256'];new=old.with_suffix(old.suffix+'.gz');assert not new.exists()
new.write_bytes(gzip.compress(raw,mtime=0));new.chmod(0o644);assert gzip.decompress(new.read_bytes())==raw
oldrelative=old.relative_to(W).as_posix();newrelative=new.relative_to(W).as_posix();entry.update(encoding='gzip',stored_path=new.relative_to(archive).as_posix(),stored_sha256=sha(new));mp.write_text(json.dumps(manifest,indent=2)+'\n')
readme=archive/'README.md';txt=readme.read_text().replace('are stored byte-for-byte with distinct modes, blobs and SHA-256 hashes in archive-manifest.json.','are recoverable byte-for-byte with distinct modes, blobs and SHA-256 hashes in [archive-manifest.json](archive-manifest.json).')
txt+='\nThe [original historical stdout log]('+entry['stored_path']+') uses deterministic gzip (mtime 0). Decompression reproduces its complete original bytes, including the final blank line; raw SHA-256, Git blob and mode remain unchanged. This storage-only change addresses the staged whitespace check without trimming historical evidence. Other original payloads remain uncompressed.\n';readme.write_text(txt)
old.unlink()
mapping=json.loads((R/'drain8169-author-full-mapping-v2.json').read_text())
for e in mapping:
 if e['recovery']==oldrelative:e['recovery']=newrelative;e['recovery_encoding']='gzip'
def dump(name,value):
 p=R/name;assert not p.exists();p.write_text(json.dumps(value,indent=2)+'\n');return p
mappingpath=dump('drain8169-author-full-mapping-v3.json',mapping)
prep['status']='UNTRACKED_PREPARED_V3_STORAGE_ONLY_CHANGE_REQUIRES_ORIGINAL_REVIEWER_CONFIRMATION';prep['archive_manifest']['sha256']=sha(mp);prep['base']=git('rev-parse','HEAD');prep['prior_preparation']=dict(path=str(R/'drain8169-author-prepared-v2.json'),sha256=sha(R/'drain8169-author-prepared-v2.json'));prep['archive_change']='Historical stdout payload deterministic gzip; raw original bytes/blob/mode unchanged; mathematical note and runner unchanged.'
prepared=dump('drain8169-author-prepared-v3.json',prep)
snapshot=R/'drain8169-prepared-v3-source';assert not snapshot.exists();snapshot.mkdir();newpaths=sorted((set(paths)-{oldrelative})|{newrelative});entries=[]
for path in newpaths:
 p=W/path;q=snapshot/path;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);entries.append(dict(path=path,mode=oct(p.stat().st_mode&0o777),sha256=sha(p),immutable_copy=str(q)))
fp=dump('drain8169-prepared-v3-source-freeze.json',dict(files=entries,count=len(entries)))
diff=[]
for path in sorted(set(paths)|set(newpaths)):
 before=R/'drain8169-prepared-v2-source'/path;after=W/path
 if path.endswith('.gz'):diff.append('Added deterministic gzip '+path+' SHA256 '+sha(after)+'\n');continue
 a=before.read_text().splitlines(True) if before.exists() else [];b=after.read_text().splitlines(True) if after.exists() else []
 diff.extend(difflib.unified_diff(a,b,fromfile='prepared-v2/'+path,tofile='prepared-v3/'+path))
p=R/'drain8169-author-v2-to-v3.diff';assert not p.exists();p.write_text(''.join(diff))
for e in prep['notes']+prep['runners']+[prep['deferred_corrected_proof']]:assert sha(W/e['path'])==e['sha256']
assert set(git('ls-files','--others','--exclude-standard').splitlines())==set(newpaths)
report=dump('drain8169-archive-preservation-v3.json',dict(status='STORAGE ONLY; AFFECTED REVIEW PENDING',base=git('rev-parse','HEAD'),owned_paths_unstaged=13,original_payload=entry,raw_bytes_preserved=True,proof_runner_deferred_proof_unchanged=True,index_clean=not git('diff','--cached','--name-only'),failure_preserved=dict(path=str(R/'drain8169-builder-failure-v1.json'),sha256=sha(R/'drain8169-builder-failure-v1.json')),artifacts=[dict(path=str(p),sha256=sha(p)) for p in [prepared,fp,mappingpath,R/'drain8169-author-v2-to-v3.diff']]))
print(report.read_text());print('report SHA '+sha(report))
