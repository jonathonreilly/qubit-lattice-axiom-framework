"""Preserve historical payload bytes in gzip when Git flags their whitespace."""
from pathlib import Path
import subprocess,json,hashlib,gzip,shutil,re,sys
pr=sys.argv[1];root=Path.cwd().parent;mapfile=root/f'{pr}-archive-map.json'
rows=json.loads(mapfile.read_text());by_path={r['final_path']:r for r in rows}
check=subprocess.run(['git','diff','--cached','--check'],text=True,capture_output=True)
paths=sorted(set(re.findall(r'^(.+?):\d+: (?:trailing whitespace|new blank line at EOF)\.',check.stdout,re.M)))
assert paths,check.stdout
assert all(p in by_path and Path(p).suffix in ['.md','.diff','.py','.patch','.txt'] for p in paths),paths
backup=root/f'{pr}-archive-map-before-compression.json';assert not backup.exists();shutil.copy2(mapfile,backup)
for name in paths:
 p=Path(name);raw=p.read_bytes();row=by_path[name];assert hashlib.sha256(raw).hexdigest()==row['sha256']
 q=Path(name+'.gz');assert not q.exists();q.write_bytes(gzip.compress(raw,mtime=0));p.unlink()
 row.update(final_path=str(q),encoding='gzip',stored_sha256=hashlib.sha256(q.read_bytes()).hexdigest())
 assert hashlib.sha256(gzip.decompress(q.read_bytes())).hexdigest()==row['sha256']
archive=Path(paths[0]).parts[:5];readme=Path(*archive)/'README.md';assert readme.exists(),readme
readme.write_text(readme.read_text()+'\nHistorical files stored with an added `.gz` suffix preserve exact original whitespace: '+', '.join('`'+p+'`' for p in paths)+'. Decompression restores original bytes; historical references retain original spelling.\n')
mapfile.write_text(json.dumps(rows,indent=2)+'\n')
subprocess.run(['git','add',str(readme.parent)],check=True)
subprocess.run(['git','diff','--cached','--check'],check=True)
print('COMPRESSED',len(paths))
