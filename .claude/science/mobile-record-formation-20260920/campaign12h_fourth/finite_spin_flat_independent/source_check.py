import hashlib,json,subprocess
from pathlib import Path
here=Path(__file__).resolve().parent
root=here.parents[4]
campaign=here.parent
third=campaign.parent/'campaign12h_third'
supplied={
 third/'FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md':'002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e',
 campaign/'post_birth_ring_spectrum_author/AUTHOR_SEAL.json':'c2e0e2adcff2dee95c682da2789c19f3113445e7f3e53f20d95936ab25ec07b9',
 campaign/'post_birth_ring_spectrum_independent/FINAL_SEAL.json':'6beaa587833b2d626154ffdd8fd2729ad844f164ee4be6b0c607b3f9b4402851',
}
paths=list(supplied)+[third/'fast_matter_formation_independent/REPORT.md',third/'fast_matter_formation_independent/FINAL_SEAL.json',campaign/'post_birth_ring_spectrum_author/EXACT_FAST_SPECTRUM_AND_FORMATION_OUTPUTS_ON_RINGS.md',campaign/'post_birth_ring_spectrum_independent/REPORT.md',campaign/'post_birth_ring_spectrum_independent/COMPARISON.md',root/'AGENTS.md',root/'docs/ai_methodology/SCIENCE_WORKFLOW.md']
result=[]
for p in paths:
 b=p.read_bytes();h=hashlib.sha256(b).hexdigest()
 if p in supplied:assert h==supplied[p],(str(p),h)
 result.append({'path':str(p),'bytes':len(b),'sha256':h,'supplied_match':h==supplied[p] if p in supplied else None})
planning=subprocess.check_output(['git','show','origin/ai/execution:AGENTS.md'],cwd=root)
workflow=subprocess.check_output(['git','show','origin/main:docs/ai_methodology/SCIENCE_WORKFLOW.md'],cwd=root)
assert workflow==(root/'docs/ai_methodology/SCIENCE_WORKFLOW.md').read_bytes()
data={'sources':result,'instruction_planning_sha256':hashlib.sha256(planning).hexdigest(),'origin_main':subprocess.check_output(['git','rev-parse','origin/main'],cwd=root,text=True).strip(),'workflow_matches_origin_main':True,'authorization_boundary':'Only listed allowed science source bodies read; no forbidden fourth-campaign source or transitive science file accessed. Seals are reused as source-bound evidence, not relabelled as fresh verification of all transitive files.'}
(here/'SOURCE_IDENTITIES.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
