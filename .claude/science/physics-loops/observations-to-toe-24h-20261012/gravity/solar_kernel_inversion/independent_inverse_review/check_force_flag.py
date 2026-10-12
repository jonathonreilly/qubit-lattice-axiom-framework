#!/usr/bin/env python3
"""Confirm that the relaxed rectangle LP does not impose inward force."""
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path

import check_inverse_synthetic as review

review.guard()
op = review.subject('direct_galaxy_response_operator')
review.subject('direct_response_basis')
fit = review.subject('direct_shared_response_fit')
rows = review.fixture([4.,1.],[1.,1.],[1.,-1.])
# Both boxes arise from allowed synthetic velocity errors: v=(2,1), R=(1,1),
# e=(0,.5), giving lower=(4,0), upper=(4,4).
rows[0]['low'][1], rows[0]['high'][1] = 0., 4.
actual = fit.solve(rows,False)
assert abs(actual['primary_minimum_t']-.4) < 1e-12
assert not actual['force_positive']
forces = rows[0]['g_N']+rows[0]['K']@review.np.array(actual['weights'])
assert forces[1] < 0
review.guard()
result = {'script_sha256':review.sha(__file__), 'fit_source_sha256':review.sha(fit.__file__),
          'synthetic_only':True, 'actual':actual, 'forces':forces.tolist(),
          'scope':'Expected consequence of the frozen relaxed LP, not evidence of an actual galaxy failure. A false force_positive flag cannot support a physical circular-speed candidate.'}
with (review.OUT/'force_flag_scope_probe.json').open('x') as stream:
    json.dump(result,stream,indent=2);stream.write('\n')
print(json.dumps(result,indent=2))
