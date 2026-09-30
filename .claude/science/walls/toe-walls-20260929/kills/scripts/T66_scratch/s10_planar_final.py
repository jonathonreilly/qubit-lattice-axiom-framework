"""Final record run for the planar (1D) sector S1: identity-only and ADM-frame-matched, R=1,2,3, exact mod-p + float."""
import json, time
from solve import analyse, PRIMES
import solve2
out = []
for R in (1, 2, 3):
    r1, _ = analyse(R, 'full', exact=True, verbose=False)
    r2, _ = analyse(R, 'uniformM', exact=True, verbose=False)
    r3, _ = solve2.run(R, verbose=False)
    row = dict(R=R,
               identity_full=dict(rows=r1['rows'], cols=r1['cols'], float_resid=r1['float_resid'], mod_consistent=r1['mod'][0][2]),
               identity_uniformM=dict(rows=r2['rows'], cols=r2['cols'], float_resid=r2['float_resid'], mod_consistent=r2['mod'][0][2]),
               matched_ADM=dict(rows_id=r3['rows_identity'], rows_match=r3['rows_match'], cols=r3['cols'], float_resid=r3['float_resid'], mod_consistent=r3['mod'][2]))
    out.append(row)
    print(json.dumps(row), flush=True)
json.dump(out, open('planar_final.json', 'w'), indent=1)
