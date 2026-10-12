#!/usr/bin/env python3
"""Frozen follow-up optimization for an interior shared-response candidate."""
import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

import direct_shared_response_fit as fit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    fit.operator.guard()
    assert not args.output.exists()
    source = fit.operator.field.sha(__file__)
    freeze_path = fit.operator.OUT/'FOLLOWUP_MARGIN_FREEZE.json'
    freeze = json.loads(freeze_path.read_text())
    assert fit.operator.field.sha(Path(__file__).with_name('FOLLOWUP_MARGIN_PROTOCOL.md')) == freeze['protocol_sha256']
    parent_path = fit.operator.OUT/'shared_response_fits_v1.json'
    assert fit.operator.field.sha(parent_path) == freeze['parent_fits_sha256']
    external = freeze['fixed_external_newtonian_SI']
    rows = fit.training_rows()
    matrix, bound, q = fit.constraints(rows, differential=True, external=external, solar_limit=True)
    # Replace relaxed-t coefficients with the declared tightened-z coefficients.
    count = sum(2*len(row['A']) for row in rows)
    assert np.all(matrix[:count,-1] == -1) and np.all(matrix[count:,-1] == 0)
    matrix[:count,-1] = 1
    matrix[-3:-1,-1] = (fit.EXTERNAL[1]-fit.EXTERNAL[0])/(2*external)
    matrix[-1,-1] = 1
    bounds = [(0,None)]*20+[(0,1)]
    options = {'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,
               'ipm_optimality_tolerance':1e-10}
    first = linprog(np.r_[np.zeros(20),-1.],A_ub=matrix,b_ub=bound,bounds=bounds,method='highs',options=options)
    result = {'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':source,
              'protocol_sha256':freeze['protocol_sha256'],'parent_fits_sha256':freeze['parent_fits_sha256'],
              'freeze_sha256':fit.operator.field.sha(freeze_path),'external_newtonian_SI':external,
              'status':int(first.status),'message':first.message,
              'operator_receipts':{r['name']:r['operator_receipt_sha256'] for r in rows},
              'numerical_candidate_validation_required':True}
    if first.success:
        zmax = float(first.x[-1])
        matrix2 = np.vstack([matrix,np.r_[np.zeros(20),-1.]])
        bound2 = np.r_[bound,-zmax+1e-8]
        second = linprog(np.r_[np.ones(20),0.],A_ub=matrix2,b_ub=bound2,bounds=bounds,method='highs',options=options)
        assert second.success,second.message
        value = second.x
        violation = max(0.,float(np.max(matrix2@value-bound2)),float(-np.min(value)),float(value[-1]-1))
        assert violation<=1e-7
        weights=value[:-1]
        external_physical=external*(1+sum(w*float(fit.operator.ramp(external,lo,hi))
             for w,lo,hi in zip(weights,fit.operator.KNOTS[:-1],fit.operator.KNOTS[1:])))
        galaxy_margins={r['name']:float(np.min(np.r_[
            (r['g_N']+r['K']@weights-r['low'])/r['A'],
            (r['high']-r['g_N']-r['K']@weights)/r['A']])) for r in rows}
        external_margin=2*min(external_physical-fit.EXTERNAL[0],fit.EXTERNAL[1]-external_physical)/(fit.EXTERNAL[1]-fit.EXTERNAL[0])
        solar_margin=1-float(q@weights)/fit.QMAX
        assert min(*galaxy_margins.values(),external_margin,solar_margin)>=value[-1]-1e-7
        result.update(primary_max_z=zmax,secondary_z=float(value[-1]),weights=weights.tolist(),
                      total_weight=float(weights.sum()),max_scaled_primal_violation=violation,
                      galaxy_matrix_margins=galaxy_margins,external_margin=external_margin,
                      solar_margin=solar_margin,predicted_external_physical_SI=external_physical,
                      Q2_s_minus2=float(q@weights),
                      force_positive=all(np.all(r['g_N']+r['K']@weights>0) for r in rows))
    result['limits']='Exposed follow-up under its own frozen protocol. Original six fits preserved. Margin has mixed explicitly declared normalizations; it is not a confidence level. Actual candidate fields and original rectangles must be checked before empirical interpretation.'
    assert fit.operator.field.sha(__file__) == source
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
