"""Final immutable inventory; read-only validation of source/evidence, no physics execution."""
import datetime,hashlib,json,os,re
from pathlib import Path
R=Path(__file__).resolve().parent
def h(b):return hashlib.sha256(b).hexdigest()
def entry(p):
    data=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(data),sha256=h(data))
def save(p,obj):
    with p.open('x') as out:
        json.dump(obj,out,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
def check_entry(x,p):
    b=p.read_bytes();assert len(b)==x['bytes'] and h(b)==x['sha256'],str(p)

freeze=json.loads((R/'INDEPENDENT_FREEZE.json').read_text())
for x in freeze['entries']:check_entry(x,R/x['path'])
for name in ('INITIAL_SOURCE_BINDINGS.json','AUTHOR_CAPTURE_BINDINGS.json'):
    for x in json.loads((R/name).read_text())['entries']:
        check_entry(x,R/x['snapshot']);check_entry(x,Path(x['original']))
        if 'upstream_original' in x:check_entry(x,Path(x['upstream_original']))

known={h(p.read_bytes()) for p in R.rglob('*') if p.is_file()}
for p in (R/'run01/PRELAUNCH.json',R/'author_packet/run01/PRELAUNCH.json'):
    data=json.loads(p.read_text())
    for x in data['bindings']:
        known.add(x['sha256'] if 'sha256' in x else x['identity']['sha256'])
report=(R/'REPORT.md').read_text()
claims=set(re.findall(r'\b[0-9a-f]{64}\b',report))
assert claims<=known,sorted(claims-known)
assert (R/'check_independent.py').read_bytes()==(R/'run01/executed_source.py').read_bytes()
assert (R/'RESOURCE_PLAN.json').stat().st_mtime_ns<(R/'run01/PRELAUNCH.json').stat().st_mtime_ns
assert len(list(R.glob('run[0-9][0-9]')))==1
assert not any(p.suffix=='.pyc' or p.name=='__pycache__' for p in R.rglob('*'))

validation=dict(validated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    kind='Bookkeeping only, no scientific program invocation',
    independent_freeze_unchanged=True,original_snapshot_pairs_unchanged=65,
    upstream_pairs_unchanged=21,report_hash_references_resolve=len(claims),
    scientific_attempts=1,failed_scientific_attempts=0,author_checker_replayed=False,
    source_repair_required=False,editable_prompt_files_changed=[],
    scope='Exact nominal ladder, fixed apparatus kappa in[1e-12,1e-8], sigma1e-6,L12; infinite all t>=kappa^-2; finite M=ceil(50/kappa^2) only t in[T,2T].')
save(R/'FINAL_VALIDATION.json',validation)
files=[entry(p) for p in sorted(R.rglob('*')) if p.is_file() and p not in (R/'FILE_MANIFEST.json',R/'FREEZE.json')]
save(R/'FILE_MANIFEST.json',dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    scope='All regular review-packet files except top-level FILE_MANIFEST.json and FREEZE.json; source packet preserved byte-for-byte.',files=files))
result=dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    status='Selective source-exposed mathematical review supports the conditional theorem at the pinned exact scope; no retained audit/canonical execution/root acceptance implied.',
    report=entry(R/'REPORT.md'),file_manifest=entry(R/'FILE_MANIFEST.json'),
    candidate=entry(R/'inputs/author_CANDIDATE.md'),candidate_freeze=entry(R/'inputs/author_FREEZE.json'),
    independent_derivation=entry(R/'INDEPENDENT_DERIVATION.md'),independent_freeze=entry(R/'INDEPENDENT_FREEZE.json'),
    independent_program=entry(R/'check_independent.py'),prelaunch=entry(R/'run01/PRELAUNCH.json'),
    receipt=entry(R/'run01/RECEIPT.json'),output=entry(R/'run01/stdout.json'),
    evidence_validation=entry(R/'EVIDENCE_VALIDATION.json'),final_validation=entry(R/'FINAL_VALIDATION.json'),
    packet_files_including_manifest_and_freeze=len(files)+2,author_packet_files=41,
    independent_prefreeze_members=39,scientific_runs=1,failed_scientific_runs=0,
    author_checker_replayed=False,same_model_and_effort=True,subdelegation=False,
    write_scope=str(R),editable_prompt_files_changed=[],
    campaign_deadline_utc='2026-10-17T23:07:27Z')
save(R/'FREEZE.json',result)
print(json.dumps(dict(report=entry(R/'REPORT.md'),freeze=entry(R/'FREEZE.json'),
    manifest=entry(R/'FILE_MANIFEST.json'),packet_files=len(files)+2,science_runs=1),indent=2))
