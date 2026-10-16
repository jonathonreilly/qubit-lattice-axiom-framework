"""Metadata-only capture for the exposed recovery check; no scientific execution."""
from pathlib import Path
import datetime, hashlib, json
OUT=Path(__file__).resolve().parent
N=OUT.parent
ITEMS=[
 ('root_sketch',N/'bus_memory_recovery_root_proposal/PRE_RESULT_SKETCH.md','43fc957f7c1937091d8755365eb4da550fc171cc02083f0c74d034901a9c3340','Complete current read; unaccepted exposed root sketch.'),
 ('slew_qualifications',N/'bus_bounded_slew_preparation_root_review/FINAL_QUALIFICATIONS.md','1c3714faadd94da6cc7789eb3472406ea2a5195b453ad941dbb163bb606ecc25','Complete current read; accepted endpoint, error, caps and memory contract.'),
 ('preparation_qualifications',N/'bus_preparation_root_review/FINAL_QUALIFICATIONS.md','1c94a58239c1bd9d168c837cf961522264a1f2d1705f3897ef541a3c8ced788e','Complete current read; inherited physical premises and complete-output contract.'),
 ('preparation_derivation',N/'bus_installed_preparation_candidate/DERIVATION.md','71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29','Complete prior same-revision read reused; current lines1-83 and155-166 refreshed for complement, full SWAP, positive rotation and scalar definitions. Other historical sources were not opened.')]
def sha(data): return hashlib.sha256(data).hexdigest()
records=[]
for key,src,expected,coverage in ITEMS:
 data=src.read_bytes()
 if sha(data)!=expected: raise RuntimeError(f'Source changed: {src}')
 dest=OUT/'sources'/(key+src.suffix)
 dest.parent.mkdir(exist_ok=True)
 if dest.exists() and dest.read_bytes()!=data: raise RuntimeError(f'Capture changed: {dest}')
 dest.write_bytes(data)
 records.append(dict(key=key,source=str(src),capture=str(dest.relative_to(OUT)),bytes=len(data),sha256=expected,coverage=coverage))
inventory=dict(captured_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),kind='metadata-only source capture',scientific_executions=0,sources=records)
(OUT/'SOURCE_IDENTITIES.json').write_text(json.dumps(inventory,indent=2)+'\n')
print(json.dumps(dict(status='four expected source identities captured',scientific_executions=0)))
