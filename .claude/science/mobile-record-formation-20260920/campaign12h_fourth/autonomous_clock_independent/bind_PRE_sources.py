#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json
HERE=Path(__file__).resolve().parent;CAMPAIGN=HERE.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
AUTHOR=CAMPAIGN/'full_instrument_energy_supply_author'
assert sha(AUTHOR/'AUTHOR_SEAL.json')=='469d1f35340e2615d7c7e9d4bbad4a18a111fc04bdb49105fb9120cdb0c7ee83'
seal=json.loads((AUTHOR/'AUTHOR_SEAL.json').read_text())
rows=[]
def snapshot(src,dst,expected,role):
 assert sha(src)==expected,(str(src),sha(src),expected)
 dst=HERE/'sources'/dst;dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_bytes(src.read_bytes())
 rows.append({'alias':str(dst.relative_to(HERE/'sources')),'snapshot_path':str(dst.relative_to(HERE)),'bytes':dst.stat().st_size,'sha256':expected,'role':role})
snapshot(AUTHOR/'AUTHOR_SEAL.json',Path('full_instrument_energy_supply_author/AUTHOR_SEAL.json'),'469d1f35340e2615d7c7e9d4bbad4a18a111fc04bdb49105fb9120cdb0c7ee83','sealed supplied premise packet')
for row in seal['files']:
 snapshot(AUTHOR/row['path'],Path('full_instrument_energy_supply_author')/row['path'],row['sha256'],'supplied battery and scheduled collision premise; existing controls inspected, not imported')
prior=CAMPAIGN/'microscopic_electric_robustness_independent/sources'
for name,expected in [('repository_AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),('planning_AGENTS.md','b72ba953ee650b464b7987c71de3415de590be5aa42451240525a2b2585312e7'),('SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4')]:
 snapshot(prior/name,Path('instructions')/name,expected,'reused previously verified governing instruction identity')
result={'stage':'independent PRE before autonomous-clock author access','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'premise_note_sha256':'6b9c4ae27ee49754e905f0d990b766be94f2c9ee8a624da01208a6da14b20288','premise_author_seal_sha256':'469d1f35340e2615d7c7e9d4bbad4a18a111fc04bdb49105fb9120cdb0c7ee83','scope':'The full-instrument battery/collision packet is a supplied mathematical premise, not independently certified by this new clock reconstruction. No autonomous_clock_author, CHECKPOINT or external personal calculations read.','path_policy':'Relative source aliases plus exact hashes support relocation.','sources':rows}
(HERE/'SOURCE_BINDINGS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'bound_sources':len(rows),'premise_note_sha256':result['premise_note_sha256'],'premise_author_seal_sha256':result['premise_author_seal_sha256']},indent=2))
