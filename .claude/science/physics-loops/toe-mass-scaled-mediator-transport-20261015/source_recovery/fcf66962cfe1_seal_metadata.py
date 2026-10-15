#!/usr/bin/env python3
"""Seal the completed analytic review and actual metadata receipts."""
from pathlib import Path
import datetime,hashlib,json,sys
ROOT=Path(__file__).resolve().parent
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(p):
    b=p.read_bytes(); return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
started=now()
assert not (ROOT/'FINAL_FREEZE.json').exists()
execution=json.loads((ROOT/'metadata_runs/final/EXECUTION.json').read_text())
assert execution['returncode']==0
check=json.loads((ROOT/'FINAL_SOURCE_RECHECK.json').read_text())
assert ident(ROOT/'REPORT.md')['sha256']==check['report']['sha256']
assert ident(ROOT/'READ_COVERAGE.md')['sha256']==check['coverage']['sha256']
receipt={'started_utc':started,'preseal_checks_completed_utc':now(),'command':[sys.executable,str(Path(__file__).resolve())],'source_at_launch':ident(Path(__file__).resolve()),'scope':'In-process preseal checks and source record; final sealing completion is confirmed by the successful tool exit. Not an independent scientific launcher.','scientific_execution':False,'preseal_metadata_execution':ident(ROOT/'metadata_runs/final/EXECUTION.json')}
(ROOT/'SEAL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
rows=[ident(p) for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='FINAL_FREEZE.json']
freeze={'frozen_utc':now(),'scope':'Same-family source-exposed analytic review of root-origin mass-scaled transport; not audit or retained status.','conclusion':'No blocking mathematical defect in the stated three-axis conditional resource construction. Optional sampled identity U requires the additional u_bound prices specified in REPORT.md.','target_sha256':'785e56e3f8e667750b1f54da8963274096ac3ddac9fb8c56db3d6460846773e7','report':ident(ROOT/'REPORT.md'),'source_manifest':ident(ROOT/'SOURCE_MANIFEST.json'),'files':rows}
(ROOT/'FINAL_FREEZE.json').write_text(json.dumps(freeze,indent=2)+'\n')
for row in rows: assert ident(ROOT/row['path'])==row
print(json.dumps({'frozen_utc':freeze['frozen_utc'],'member_count':len(rows),'report':freeze['report'],'final_freeze':ident(ROOT/'FINAL_FREEZE.json'),'scientific_execution':False},indent=2))
