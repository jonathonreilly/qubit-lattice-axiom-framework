"""Metadata-only capture of the three sources authorized for this exposed review."""
from pathlib import Path
import datetime, hashlib, json
OUT=Path(__file__).resolve().parent
N=OUT.parent
ITEMS=[
 ('derivation',N/'shrinking_bias_resource_candidate/DERIVATION.md','2bfb24cce9760be23d750b3b2a190b3110bc0326c035488aae004d1de7849a74','Complete final text, sections1-10, read in this task.'),
 ('author_source_manifest',N/'shrinking_bias_resource_candidate/SOURCE_MANIFEST.json',None,'Read for identities and author exposure only; its other listed sources were not opened.'),
 ('fixed_plant_qualifications',N/'reachable_bus_resource_root_review/FINAL_QUALIFICATIONS.md','e50497e74e2022f97e6b1a42ff8bf176c2c7b30cd16b68d22b18f503457e541b','Complete controlling qualifications read; not a full parent revalidation.')]
def sha(data): return hashlib.sha256(data).hexdigest()
rows=[]
for key,source,expected,scope in ITEMS:
 data=source.read_bytes(); actual=sha(data)
 if expected is not None and actual!=expected: raise RuntimeError(f'Identity changed: {source}')
 dest=OUT/'sources'/(key+source.suffix)
 dest.parent.mkdir(exist_ok=True)
 if dest.exists() and dest.read_bytes()!=data: raise RuntimeError(f'Capture changed: {dest}')
 dest.write_bytes(data)
 rows.append(dict(key=key,source=str(source),capture=str(dest.relative_to(OUT)),bytes=len(data),sha256=actual,read_scope=scope,externally_pinned=expected is not None))
record=dict(captured_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),kind='metadata source identity capture only',scientific_executions=0,source_count=len(rows),sources=rows)
(OUT/'SOURCE_IDENTITIES.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
