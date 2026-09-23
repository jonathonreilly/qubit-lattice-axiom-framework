"""Read only the explicitly authorized science sources and own frozen packet."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;CAMP=HERE.parent
def ident(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
own=CAMP/'actual_first_output_independent'
fixed=[(own/'FINAL_SEAL.json','c5ed54dd73a633a433f51cba08c5221e6cad58ea306219a3002e2104e53ea69a'),
       (CAMP.parent/'campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md','002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e'),
       (CAMP/'cube_point_spectrum_independent/REPORT.md','20303cc9320deb32799bdc98befc986c856943ac632d0245ace929c8140a7d7d'),
       (CAMP/'cube_point_spectrum_independent/PRE_COMPARISON_SEAL.json','8c29f173d14a983a0c6273560712c32685d48429d7482c5dcff152e426d05c0a')]
sources=[]
for p,h in fixed:
    item=ident(p);assert item['sha256']==h;sources.append(item)
sealed=json.loads((own/'FINAL_SEAL.json').read_text())
for item in sealed['independent_artifacts']:
    assert ident(Path(item['path']))==item
report=ident(own/'REPORT.md')
assert any(report==item for item in sealed['independent_artifacts'])
sources.append(report)
result={'science_sources':sources,'own_frozen_artifacts_authenticated':len(sealed['independent_artifacts']),
        'provisional_dependency':'The cube six-record P-space point-spectrum result is supplied under an independent PRE seal, with candidate comparison pending as of the dispatch. This packet does not audit or rerun that spectral certificate. Its local-escape theorem is explicitly conditional on that premise.',
        'independent_builder':'cube_controls.py is new. No ring, prior cube, spectral-certificate, or author builder is imported.',
        'read_boundary':'No cube_unprepared_author, cube_point_spectrum_author, LOCAL_COUNTERTERM_PROPOSAL.md, other new research, campaign plan, checkpoint, registry, or Git was opened. Only the authorized cube REPORT and PRE manifest were read from that packet; its transitive source paths were not followed.',
        'procedure_status':'Applicable instructions and current workflow were already read at the unchanged inherited revision. The scoped N1-N8 questions are reused from the own frozen packet; no Git freshness check or wider source scan is performed under this dispatch. No formal audit/no-go packet PASS is asserted.'}
(HERE/'SOURCE_IDENTITIES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
