from pathlib import Path
import json
p=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_third/hardcore_live_density_independent')
a=json.loads((p/'FINITE_SECTOR_RESULTS.json').read_text());old=json.loads((p/'development/before_coherence_control/FINITE_SECTOR_RESULTS.json').read_text())
print(json.dumps(a['cases']['rectangle_3_by_2_with_frozen_external_ice_flow'],indent=2))
for k in old['cases']:
 row=dict(a['cases'][k]);print(k,'added:',row.pop('coherent_vs_resolved_controls'));assert row==old['cases'][k]
assert a['dynamics']==old['dynamics'];print('All previous mathematical result fields unchanged exactly.')
