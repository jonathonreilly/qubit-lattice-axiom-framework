"""Compare frozen native finite spectra against derived fourth-order theory."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
native=json.loads((P/'neutral_tube_anisotropy.json').read_text())['rows']
effective=json.loads((P/'neutral_open_xy_comparison.json').read_text())['rows']
assert len(native)==len(effective)==18
rows=[]
for x,y in zip(native,effective):
 assert (x['L'],x['lambda_z'])==(y['L'],y['lambda_z'])
 lam=x['lambda_z']; err=max(abs(u-v) for u,v in zip(x['gaps_over_t'],y['fourth_gaps_over_t']))
 rows.append(dict(L=x['L'],lambda_z=lam,max_gap_error_over_t=err,error_over_lambda4=err/lam**4,native_index2_weight_over_lambda4=x['mode_source_weights'][2]/lam**4,derived_index2_O2_weight=y['O2_mode_weights'][2]))
(P/'neutral_anisotropy_comparison.json').write_text(json.dumps(dict(rows=rows,scope='Finite selected-sector development comparison. Sorted eigenvalues, no complete-spectrum certificate. Index2 source comparison is valid near weak coupling; level reordering makes it invalid as an equal-mode comparison at strong coupling.'),indent=2)+'\n')
print(json.dumps(rows[-3:],indent=2))
