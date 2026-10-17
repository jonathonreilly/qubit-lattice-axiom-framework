"""Capture newly root-qualified moment implication before scientific execution."""
from pathlib import Path
import datetime, hashlib, json
D=Path(__file__).resolve().parent
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
files={
 'moment.md':('ballistic_emitter_escape_candidate/CANDIDATE.md','31449e982b27e623491f4e9cb0c8239e2ff15ebc9605668b8e4684055c52410f'),
 'moment_review.md':('ballistic_emitter_escape_review/REPORT.md','cf6507b8b0dc3c9075b424602ab4969202c6e6bd665cabda4dc016125a21ee77'),
 'moment_qualification.md':('ballistic_emitter_root_qualification/QUALIFICATION.md','0b0ce9eaba582d878b982ecd0f86a53857c5f394b9a42b4e27306e58bb405102'),
 'moment_acceptance.json':('ballistic_emitter_root_qualification/ACCEPTANCE.json','bd2059184e105bd41437b1c28ca3f106a441215e09eac7a2b3ec316cbd674318'),
 'moment_freeze.json':('ballistic_emitter_escape_candidate/FREEZE.json','962038fee412c3a173689660236083519b08177b61163d5f1990ce00842f1197'),
}
manifest=json.loads((D/'SOURCE_MANIFEST.json').read_text())
(D/'SOURCE_MANIFEST_BEFORE_MOMENT.json').write_bytes((D/'SOURCE_MANIFEST.json').read_bytes())
for name,(relative,expected) in files.items():
    original=D.parent/relative
    assert digest(original)==expected
    dest=D/'inputs'/name; dest.write_bytes(original.read_bytes())
    manifest['sources'].append({'snapshot':'inputs/'+name,'original_path':str(original),'sha256':expected,'bytes':dest.stat().st_size,'scope':'Qualified fixed-kappa analytic implication only; all changed-kappa premises require new proof. Joint-box conclusion excluded.'})
manifest['new_moment_dependency']={'added_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'coverage':'Complete candidate, independent report, root qualification and acceptance read. No author/reviewer executable replay or new certification of their historical checks. Fixed-kappa theorem is not treated as parameter-interval approval.'}
(D/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
p=D/'RESOURCE_PLAN.json'; old=p.read_bytes(); (D/'RESOURCE_PLAN_BEFORE_MOMENT.json').write_bytes(old)
plan=json.loads(old)
plan['excluded'].remove('ballistic candidate as a checked premise')
plan['excluded'].append('fixed-kappa acceptance as automatic approval of changed-kappa premises')
plan['new_qualified_dependency']='Moment implication accepted by root at pinned identity; rederive every actual-envelope L2 bound over proposed kappa interval. Preserve weighted decay-to-zero proof for exact isometry normalization.'
plan['new_obligation'] += ' Also re-establish H1 and L2 derivative bounds needed by the newly qualified moment implication; retain weighted fallback and separate both cost comparisons.'
plan['amendment_before_any_scientific_run']=datetime.datetime.now(datetime.timezone.utc).isoformat()
p.write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps({'sources':len(manifest['sources']),'resource_caps_unchanged':True,'scientific_runs_so_far':0}))
