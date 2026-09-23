import hashlib,json,subprocess
from pathlib import Path
here=Path(__file__).resolve().parent;campaign=here.parent;root=here.parents[4]
prepared=campaign/'finite_spin_flat_independent'
def ident(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
seal=prepared/'FINAL_SEAL.json';assert ident(seal)['sha256']=='4bbbdcf3fa5a12181ccaf4e9ad09ec5dfb82fe4a078d5256ccad67caedf10cfe'
data=json.loads(seal.read_text())
for a in data['independent_artifacts']:
    assert ident(Path(a['path']))['sha256']==a['sha256']
paths=[seal,prepared/'REPORT.md',prepared/'COMPARISON.md',prepared/'FINITE_SPIN_LOSS_CLARIFICATION.md',prepared/'physical_builder.py',prepared/'flat_probe.py',prepared/'decisive_controls.py',campaign.parent/'campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md',campaign.parent/'campaign12h_third/fast_matter_formation_independent/REPORT.md',campaign.parent/'campaign12h_third/fast_matter_formation_independent/FINAL_SEAL.json',campaign/'post_birth_ring_spectrum_author/AUTHOR_SEAL.json',campaign/'post_birth_ring_spectrum_author/EXACT_FAST_SPECTRUM_AND_FORMATION_OUTPUTS_ON_RINGS.md',campaign/'post_birth_ring_spectrum_independent/REPORT.md',campaign/'post_birth_ring_spectrum_independent/COMPARISON.md',campaign/'post_birth_ring_spectrum_independent/FINAL_SEAL.json']
procedures=[]
for path in ('docs/ai_methodology/skills/no-go-discipline/SKILL.md','docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md','docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md'):
    b=subprocess.check_output(['git','show','origin/main:'+path],cwd=root)
    procedures.append({'source':'origin/main:'+path,'sha256':hashlib.sha256(b).hexdigest()})
    if 'no-go-discipline' in path:assert b==Path('/Users/jonreilly/.codex/skills/no-go-discipline/SKILL.md').read_bytes()
    if 'proof-search-governance' in path:assert b==Path('/Users/jonreilly/.codex/skills/physics-loop/references/proof-search-governance.md').read_bytes()
result={'science_sources':[ident(p) for p in paths],'prepared_artifacts_authenticated':len(data['independent_artifacts']),'procedures':procedures,'origin_main':subprocess.check_output(['git','rev-parse','origin/main'],cwd=root,text=True).strip(),'source_boundary':'No actual_first_output_author, unprepared author/follow-up folder, tail folder, campaign plan or checkpoint has been opened. The candidate seal hash was supplied by the coordinator only. No author code imported.','process_scope':'No Git fetch or other mutation; no cross-repository science search because the dispatch expressly restricts sources. The no-go skill is used for scoped stress testing, not a formal publication/audit packet PASS.'}
(here/'SOURCE_IDENTITIES.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
