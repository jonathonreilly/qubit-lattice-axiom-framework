import hashlib,json,datetime
from pathlib import Path
here=Path(__file__).resolve().parent
author=here.parent/'finite_spin_post_birth_author'
def identity(p):
    b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
pre=here/'PRE_COMPARISON_SEAL.json';ap=author/'AUTHOR_SEAL.json'
assert identity(pre)['sha256']=='97aa84106b6ca88adcb4bd4c6286ada6d24087740da767fded03485590df495b'
assert identity(ap)['sha256']=='dfc55f6eac748bb11130fe3a8e5544194c6babd810c0c06d45e177c56c72df7e'
pd=json.loads(pre.read_text());ad=json.loads(ap.read_text())
for row in pd['artifacts']+pd['sources']['sources']:
    assert identity(Path(row['path']))['sha256']==row['sha256'],row['path']
for row in ad['artifacts']:
    assert Path(row['path']).parent==author
    assert identity(Path(row['path']))['sha256']==row['sha256'],row['path']
allowed={x['path'] for x in pd['sources']['sources']}
permitted=[];unopened=[]
for row in ad['sources']:
    if row['path'] in allowed:
        assert identity(Path(row['path']))['sha256']==row['sha256'];permitted.append(row)
    else:unopened.append(row['path'])
artifacts=[identity(p) for p in sorted(here.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
seal={'stage':'FINAL_SOURCE_COMPARISON','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'disposition':'PASS for the exact frozen candidate prepared-flat-sector theorem; no required candidate correction, no formal audit or retention verdict.','candidate_author_seal':identity(ap),'candidate_note':identity(author/'PREPARED_FLAT_SECTOR_WITH_ELECTRIC_DYNAMICS_AND_FORMATION.md'),'candidate_artifacts_authenticated':ad['artifacts'],'candidate_permitted_source_bindings':permitted,'candidate_excluded_source_bindings_not_opened_or_hashed':unopened,'independent_PRE_seal':identity(pre),'independent_PRE_preservation':{'artifacts_unchanged':len(pd['artifacts']),'sources_unchanged':len(pd['sources']['sources'])},'independent_artifacts':artifacts,'read_coverage':'Complete current proof, all three current scripts, exact tables and probe rows, dynamic result objects and receipts/streams, and complete historical script deltas. No author code imported or executed. Excluded second-event loss source replaced by a direct independent reconstruction of its one cited operator identity.','post_PRE_checks':'All twelve electric/leakage polynomials and H4 terms after explicit b-sign map; all 36 rational probe rows; full rotor loss on all 36 matter words; H4 fiber spectrum; finite-S resolved/coherent cross-Grams at S=1,2,4,8; all 48 stored dynamic bookkeeping rows; four independent S=8,32 endpoint propagations; exact rational reference-tail bound.','checker_clarification':'Frozen decisive_controls.py line 116 incorrectly suggested finite-spin instrument total losses can differ. FINITE_SPIN_LOSS_CLARIFICATION.md supersedes that comment by the exact orthogonality proof, with PRE bytes preserved. No computed result or theorem changed.','quantitative_result':'Candidate eta^(-1/7) core bound verified by h=eta^(-2/7); independent PRE used a valid weaker nonoptimal exponent.','independence_timeline':'PRE proof and calculations were sealed before candidate access. Candidate proof was reported written before checker progress arrived, but the author seal came after those messages; no claim of seal-before-all-feedback is made.','scope_limits':['Prepared normalizable physical flat inputs with convergent physical spin embeddings at fixed graph.','Entire actual first-mark output joint ordinary-time dynamics remains unproved here.','No microscopic random-event/flat-selection conditioning theorem.','No volume limit, native selection, empirical matching, photon phase or TOE conclusion.'],'actions':'Only assigned independent directory written; no Git mutation, external messaging, onward delegation, audit application or publication.'}
p=here/'FINAL_SEAL.json';p.write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'final_seal':str(p),'sha256':identity(p)['sha256'],'own_artifacts_bound':len(artifacts),'PRE_artifacts_unchanged':len(pd['artifacts']),'author_artifacts_authenticated':len(ad['artifacts'])},indent=2))
