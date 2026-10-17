"""Narrow read-only source capture; not a scientific calculation."""
from pathlib import Path
import datetime, hashlib, json, subprocess

D = Path(__file__).resolve().parent
W = D.parent.parent / 'correlation_worktree'
COMMIT = '0f1022e03dbbed8085035f2a378be8ae1aca02e8'
F = 'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/'
FILES = {
 'installed.md': F+'emitter_installed_certificate/CANDIDATE.md.txt',
 'weighted.md': F+'weighted_emitter_escape_candidate/CANDIDATE.md.txt',
 'route.md': F+'autonomous_emitter_route/ROUTE.md.txt',
 'generic_v2.md': F+'autonomous_emitter_route/inputs/THEOREM_V2.md.txt',
 'interval.md': F+'emitter_installed_certificate/inputs/two_body_interval_bridge__CANDIDATE.md.txt',
 'interval.json': F+'emitter_installed_certificate/inputs/two_body_interval_bridge__CERTIFICATE.json',
 'stationary.json': F+'emitter_installed_certificate/inputs/two_body_interval_bridge__inputs__rational_point_certificate.json',
 'installed_review.md': F+'emitter_installed_review/REPORT.md.txt',
 'weighted_review.md': F+'weighted_emitter_escape_review/REPORT.md.txt',
 'installed_qualification.md': F+'emitter_installed_root_review/QUALIFICATION.md.txt',
 'weighted_qualification.md': F+'weighted_emitter_root_qualification/QUALIFICATION.md.txt',
 'local_qualification.md': F+'emitter_root_qualification/QUALIFICATION.md.txt',
 'installed_acceptance.json': F+'emitter_installed_root_review/ACCEPTANCE.json',
 'weighted_acceptance.json': F+'weighted_emitter_root_qualification/ACCEPTANCE.json',
 'publication.md': 'docs/PRODUCT_SEED_EMITTER_BOUNDED_THEOREM_NOTE_2026-10-17.md',
 'publication_inventory.json': 'outputs/product_seed_emitter_2026_10_17_inputs/SOURCE_INVENTORY.json',
 'workflow.md': 'docs/ai_methodology/SCIENCE_WORKFLOW.md',
 'physics_loop_skill.md': 'docs/ai_methodology/skills/physics-loop/SKILL.md',
}
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip()==COMMIT
out = D/'inputs'; out.mkdir()
rows=[]
for name,relative in FILES.items():
    original=W/relative
    data=original.read_bytes()
    assert data==subprocess.check_output(['git','show',COMMIT+':'+relative],cwd=W)
    (out/name).write_bytes(data)
    rows.append({'snapshot':'inputs/'+name,'repository_path':relative,
                 'commit':COMMIT,'sha256':hashlib.sha256(data).hexdigest(),
                 'bytes':len(data),'scope':'inherited source; not a new independent certificate'})
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'source_commit':COMMIT,'sources':rows,
          'read_scope':'Installed and weighted arguments, their separate reports and root qualifications completely read. Local route/generic/ladder proofs were previously fully read by this source-exposed agent; unchanged identities are reused, with affected optical, physical-model and radius sections refreshed. Publication statement sections 1-2 and frontmatter read; full publication and inventory copied for provenance only. Exact interval parameter and finite-radius fields are read by the new checker, not recertified here.',
          'independence':'This agent authored stationary-ladder work, reviewed the generic and installed emitter arguments, and adapted the product-seed publication. New work is author mathematics; no blind/model-diverse or independent acceptance is claimed.'}
(D/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
queries=[
 ['git','grep','-n','-i','-e','arctan','-e','variance normalization','-e','reference mass',COMMIT,'--','docs/PRODUCT_SEED_EMITTER_BOUNDED_THEOREM_NOTE_2026-10-17.md','docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md'],
 ['rg','-n','-i','kappa|normaliz|variance',str(D.parent/'emitter_calibration_candidate/CALIBRATION.md')],
 ['rg','-n','-i','kappa =|Altering kappa|position|moment|prior',str(D.parent/'ballistic_emitter_escape_candidate/CANDIDATE.md')],
]
logs=[]
for command in queries:
    r=subprocess.run(command,cwd=W,capture_output=True,text=True)
    logs.append({'command':command,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
(D/'MATCHING_PREMISE_SEARCH.json').write_text(json.dumps({'scope':'Narrow local matching-premise search only; no literature novelty conclusion, network query, or remote freshness claim. The ballistic proposal remains excluded as a theorem premise. An earlier attempted calibration filename CANDIDATE.md was absent; the actual CALIBRATION.md was located without scientific execution.','queries':logs},indent=2)+'\n')
print(json.dumps({'sources':len(rows),'manifest_sha256':hashlib.sha256((D/'SOURCE_MANIFEST.json').read_bytes()).hexdigest(),'search_exit_codes':[r['exit_code'] for r in logs]}))
