"""Validate and freeze the analytical review; no scientific execution."""
import datetime,hashlib,json,os,re
from pathlib import Path
R=Path(__file__).resolve().parent
def digest(data):return hashlib.sha256(data).hexdigest()
def record(p):
    data=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(data),sha256=digest(data))
def save(p,data):
    with p.open('x') as out:
        json.dump(data,out,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
manifest=json.loads((R/'SOURCE_MANIFEST.json').read_text())
pairs=[]
for e in manifest['entries']:
    snapshot=R/e['snapshot'];original=Path(e['original'])
    for p in (snapshot,original):
        data=p.read_bytes();assert len(data)==e['bytes'] and digest(data)==e['sha256'],str(p)
    pairs.append(dict(snapshot=e['snapshot'],original=e['original'],sha256=e['sha256'],bytes=e['bytes'],matching=True))
composite=json.loads((R/'inputs/composition_freeze.json').read_text())
assert composite['candidate']['sha256']==record(R/'inputs/composition.md')['sha256']
assert composite['candidate']['bytes']==record(R/'inputs/composition.md')['bytes']
product=json.loads((R/'inputs/product_acceptance.json').read_text())
assert product['candidate']['sha256']==record(R/'inputs/product.md')['sha256']
runtime=json.loads((R/'inputs/resonance_acceptance.json').read_text())
assert runtime['candidate']['sha256']==record(R/'inputs/resonance.md')['sha256']
assert runtime['review']['sha256']==record(R/'inputs/resonance_review.md')['sha256']
staged=json.loads((R/'inputs/staged_freeze.json').read_text())
assert staged['sha256']==record(R/'inputs/staged.md')['sha256']
assert staged['source_candidate_sha256']==record(R/'inputs/interacting.md')['sha256']
known={record(p)['sha256'] for p in R.rglob('*') if p.is_file()}
refs=set(re.findall(r'\b[0-9a-f]{64}\b',(R/'REVIEW.md').read_text()))
assert refs<=known,sorted(refs-known)
assert not any(p.name=='__pycache__' or p.suffix=='.pyc' for p in R.rglob('*'))
validation=dict(validated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    type='Source identity and bookkeeping only; no numerical, symbolic or dynamics computation.',
    source_pairs=pairs,source_count=len(pairs),all_source_bytes_unchanged=True,
    exact_source_qualification_bindings_verified=True,
    composition_source_repair_required=False,alternative_I_source_still_conditional=True,
    mathematical_disposition='P composition supported from qualified sources; I implication supported conditional on its pending source/addendum premises.',
    scientific_executions=0,scientific_source_replays=0,editable_prompt_files_changed=[])
save(R/'VALIDATION.json',validation)
files=[record(p) for p in sorted(R.rglob('*')) if p.is_file() and p not in (R/'FILE_MANIFEST.json',R/'FREEZE.json')]
save(R/'FILE_MANIFEST.json',dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    scope='All review files except top-level FILE_MANIFEST.json and FREEZE.json',files=files))
freeze=dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    status='Selective source-exposed interface review; qualified-P composition supported; I remains conditional on pending separate source review. No retained/canonical/root acceptance implied.',
    review=record(R/'REVIEW.md'),source_manifest=record(R/'SOURCE_MANIFEST.json'),
    file_manifest=record(R/'FILE_MANIFEST.json'),validation=record(R/'VALIDATION.json'),
    candidate=record(R/'inputs/composition.md'),candidate_freeze=record(R/'inputs/composition_freeze.json'),
    source_snapshots=len(pairs),packet_files_including_manifest_and_freeze=len(files)+2,
    scientific_executions=0,source_replays=0,same_model_and_effort=True,subdelegation=False,
    required_source_repairs=[],open_source_dependency='Alternative I interacting preparation and staged-release source qualification; not discharged by this review.',
    write_scope=str(R),editable_prompt_files_changed=[])
save(R/'FREEZE.json',freeze)
print(json.dumps(dict(review=record(R/'REVIEW.md'),freeze=record(R/'FREEZE.json'),
    packet_files=len(files)+2,source_pairs=len(pairs),scientific_executions=0),indent=2))
