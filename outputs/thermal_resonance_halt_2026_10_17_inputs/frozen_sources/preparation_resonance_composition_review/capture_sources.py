"""Read-only source binding and snapshot copying; no scientific computation."""
import datetime,hashlib,json,os
from pathlib import Path
R=Path(__file__).resolve().parent
N=R.parent
sources=[
 ('composition.md','preparation_resonance_composition/CANDIDATE.md','250d431f3b818e08225b97b9d65d539c447ddd7b6ab00a36f5f7c7a7cc3868ca'),
 ('composition_freeze.json','preparation_resonance_composition/FREEZE.json',None),
 ('resonance.md','resonant_family_candidate/CANDIDATE.md','401e5c2389ef99bd9980898ec118f2476e49dd627d3cf9f32deb812ffc5498f0'),
 ('resonance_freeze.json','resonant_family_candidate/FREEZE.json','8cdf10121e4c42247d4aba730a48413817a62b9ada420adfc6bc70df7df64879'),
 ('resonance_review.md','resonant_family_review/REPORT.md','70eaca751449653eb33255a8b6c0509cde2d4f69de14d39d353c5b96b838c172'),
 ('resonance_review_freeze.json','resonant_family_review/FREEZE.json','6ead24431690a1b62f549d1adca9d7250ac92231cb0103cfe6953dee56be17b7'),
 ('resonance_acceptance.json','resonant_family_root_qualification/ACCEPTANCE.json','bb280c96d290e28b42c45994cab3fe9871d671b0d20d39a36ae09d211ef98686'),
 ('product.md','emitter_preparation_independent/CANDIDATE.md','b7ef6e98b16bcffb609cbf8a9cca2aee03d4bb20ac6295e99c744f488ad14227'),
 ('product_freeze.json','emitter_preparation_independent/FREEZE.json','fb4b80aada7275e110fc76ea0c4ac49974daf123db79a5639156e9332e958855'),
 ('product_acceptance.json','preparation_product_root_qualification/ACCEPTANCE.json','43e1609d6e38b2220e35e1637428263e49b38d1ac22ed282ee64f3d7d3f60ca5'),
 ('product_review.md','preparation_product_root_qualification/REVIEW.md','5e4cc2c916d9240ec5bb0b2a84559ae38fd2b20959e63c52d6b3c0bda04a2d69'),
 ('interacting.md','emitter_preparation_root/CANDIDATE.md','416a0cd7155a60517bae6944368d9f9619f0f59274b6634004e0c4962d921fa0'),
 ('interacting_freeze.json','emitter_preparation_root/FREEZE.json',None),
 ('staged.md','emitter_preparation_root/STAGED_RELEASE_ADDENDUM.md','1c021b815445bbfc8146b7b37d21b3475769f065a21247bda86563f649f90885'),
 ('staged_freeze.json','emitter_preparation_root/STAGED_RELEASE_FREEZE.json',None),
 ('SCIENCE_WORKFLOW.md','resonant_family_review/inputs/SCIENCE_WORKFLOW.md','71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3')
]
entries=[]
for name,rel,expected in sources:
    original=N/rel;data=original.read_bytes();digest=hashlib.sha256(data).hexdigest()
    if expected is not None:assert digest==expected,str(original)
    dest=R/'inputs'/name
    with dest.open('xb') as out:out.write(data);out.flush();os.fsync(out.fileno())
    st=original.stat()
    entries.append(dict(snapshot=str(dest.relative_to(R)),original=str(original),sha256=digest,bytes=len(data),
                        original_device=st.st_dev,original_inode=st.st_ino,original_mtime_ns=st.st_mtime_ns))
record=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            purpose='Source-exposed analytical interface review. No scientific executable copied or replayed.',
            runtime_status='Qualified exact resonance-family theorem reused at unchanged identity.',
            product_status='Qualified conditional preparation source reused.',
            interacting_status='Unaccepted source and staged-release premise remain conditional as assigned.',entries=entries)
with (R/'SOURCE_MANIFEST.json').open('x') as out:
    json.dump(record,out,indent=2);out.write('\n');out.flush();os.fsync(out.fileno())
print(json.dumps(dict(source_count=len(entries),manifest_sha256=hashlib.sha256((R/'SOURCE_MANIFEST.json').read_bytes()).hexdigest(),
                     composition_freeze=entries[1],interacting_freeze=entries[12],staged_freeze=entries[14]),indent=2))
