"""Bookkeeping freeze before author scientific-code/output exposure."""
import datetime,hashlib,json,os
from pathlib import Path
root=Path(__file__).resolve().parent
entries=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='INDEPENDENT_FREEZE.json':
        data=p.read_bytes()
        entries.append(dict(path=str(p.relative_to(root)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
record=dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            exposure_boundary='New author checker/launcher/scalar inputs/output not inspected at this freeze. Full argument and exact source snapshots exposed.',
            scientific_runs=1,failed_scientific_runs=0,entries=entries)
dest=root/'INDEPENDENT_FREEZE.json'
with dest.open('x') as out:
    json.dump(record,out,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
print(json.dumps(dict(files=len(entries),freeze_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),frozen_utc=record['frozen_utc'])))
