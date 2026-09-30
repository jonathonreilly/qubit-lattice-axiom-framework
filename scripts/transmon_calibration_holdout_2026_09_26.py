#!/usr/bin/env python3
"""Calibrated square-rotor comparator: numerical KIT holdout residuals.

No parameter is fit to f03/f04/f05. This is a retrospective empirical
benchmark of an imported device model, not a native TOE prediction.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
from pathlib import Path
from itertools import product
import csv
import hashlib
import json
import numpy as np
from scipy.optimize import least_squares
from transmon_resonator_model_2026_09_26 import predict, endpoint, CAL_INDEX
from transmon_direct_charge_check_2026_09_26 import independent_predict

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/TRANSMON_CALIBRATION_HOLDOUT_BOUNDED_THEOREM_NOTE_2026-09-26.md',
    'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'scripts/transmon_resonator_model_2026_09_26.py',
    'scripts/transmon_direct_charge_check_2026_09_26.py',
    'scripts/data/transmon_holdout_2026_09_26/Experiment.csv',
    'scripts/data/transmon_holdout_2026_09_26/provenance.json',
)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'scripts/data/transmon_holdout_2026_09_26/Experiment.csv'
SOURCE_SHA256 = '0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b'
CAL_KEYS = ('f01', 'f02', 'fres1', 'fres2')
ORDER = ('f01','f02','f03','f04','f05','f06','fres1','fres2')


def fit_calibration(target, start, bounded=True):
    def residual(z):
        return (predict(np.exp(z))[0][CAL_INDEX] - target) * 1000
    options = dict(xtol=1e-12, ftol=1e-12, gtol=1e-9, max_nfev=150)
    if bounded:
        options['bounds'] = (np.log([.05,2,5,.0001]), np.log([1,100,10,1]))
    fit = least_squares(residual, np.log(start), **options)
    p = np.exp(fit.x)
    error = float(max(abs(residual(fit.x))))
    assert fit.success and error < .001, ('calibration error MHz',error)
    return p, error


def construct_predictions(calibration):
    """Only the four calibration values enter this function."""
    target = np.array([calibration[k] for k in CAL_KEYS])
    fits = []
    for ec in (.15,.25,.35):
        start = [ec,(target[0]+ec)**2/(8*ec),target[2]+.02,.08]
        p,error = fit_calibration(target,start)
        fits.append(dict(parameters=p.tolist(),maximum_error_MHz=error))
    p = np.array(fits[0]['parameters'])
    assert max(np.max(abs(np.array(r['parameters'])-p)) for r in fits) < 1e-6
    nominal, detail = predict(p)
    # Individually and jointly broaden the three truncations at fixed parameters.
    cutoff_results = []
    for dims in ((30,12,9),(30,20,9),(30,20,16),(40,24,20)):
        f,d = predict(p,*dims)
        difference = float(max(abs(f-nominal))*1000)
        assert difference < .001, ('cutoff shift MHz',dims,difference)
        cutoff_results.append(dict(dimensions=dims,max_shift_MHz=difference))
    direct,direct_detail = independent_predict(p)
    disagreement = float(max(abs(direct-nominal))*1000)
    assert disagreement < .001, ('independent comparison MHz',disagreement)
    assert max(x['eigen_residual_max_GHz'] for x in direct_detail['endpoints']) < 1e-7
    # These are sampled dominant-bare-label checks, not eigenvector continuation.
    sampled_min_weight = 1.0
    for ng in (0.,.5):
        for scale in np.linspace(0,1,21):
            _,labels = endpoint(p,ng,scale_G=float(scale))
            sampled_min_weight = min(sampled_min_weight,labels['min_weight'])
    assert sampled_min_weight > .5
    # Charge-grid control, including the supplied endpoint-mean convention.
    charge_grid = np.array([endpoint(p,float(ng))[0] for ng in np.linspace(0,.5,21)])
    charge_width = 1000*np.ptp(charge_grid,axis=0)
    # Predetermined calibration perturbations: f02 is twice its drive frequency.
    halfwidth = np.array([1,2,1,1])/1000
    corners = []
    for signs in product((-1,1),repeat=4):
        shifted = target + halfwidth*np.array(signs)
        pp,error = fit_calibration(shifted,p)
        ff,dd = predict(pp)
        assert min(dd['assignment_ng0']['min_weight'],dd['assignment_ng_half']['min_weight']) > .5
        corners.append(dict(signs=list(signs),parameters=pp.tolist(),prediction_GHz=ff.tolist(),calibration_error_MHz=error))
    a = np.array([c['prediction_GHz'] for c in corners])
    # Independent local Jacobian response, a diagnostic rather than a box proof.
    step=1e-5
    jac=np.column_stack([(predict(p+np.eye(4)[i]*step)[0]-predict(p-np.eye(4)[i]*step)[0])/(2*step) for i in range(4)])
    response=jac@np.linalg.inv(jac[CAL_INDEX,:])
    return dict(parameter_names=['EC_over_h','EJ_over_h','Omega_over_2pi','G_over_2pi'],
                units='GHz',parameters=p.tolist(),fit_starts=fits,
                prediction_order=list(ORDER),predictions_GHz=nominal.tolist(),
                independent_predictions_GHz=direct.tolist(),independent_max_difference_MHz=disagreement,
                cutoff_checks=cutoff_results,sampled_min_assignment_weight=sampled_min_weight,
                direct_min_assignment_weight=min(min(x['bare_weights']) for x in direct_detail['endpoints']),
                charge_grid_width_MHz=charge_width.tolist(),
                calibration_jacobian_condition=float(np.linalg.cond(jac[CAL_INDEX,:])),
                linearized_box_halfwidth_MHz=(abs(response)@np.array([1,2,1,1])).tolist(),
                corner_halfwidth_MHz=[1,2,1,1],corner_minimum_GHz=a.min(axis=0).tolist(),
                corner_maximum_GHz=a.max(axis=0).tolist(),corners=corners)


def main():
    raw=DATA.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA256, 'External data bytes differ from pinned upstream source'
    row=next(r for r in csv.DictReader(raw.decode().splitlines()) if r['Experiment']=='KIT')
    calibration={k:float(row[k]) for k in CAL_KEYS}
    result=construct_predictions(calibration)
    # Evaluation values are converted only after all fits and controls finish.
    evaluation=[]
    for j in range(3,7):
        key=f'f0{j}'
        if not row.get(key) or row[key].lower()=='nan':
            continue
        observed=float(row[key]);predicted=result['predictions_GHz'][j-1]
        lo=result['corner_minimum_GHz'][j-1];hi=result['corner_maximum_GHz'][j-1]
        evaluation.append(dict(transition=key,measured_GHz=observed,predicted_GHz=predicted,
            residual_total_MHz=1000*(predicted-observed),residual_drive_MHz=1000*(predicted-observed)/j,
            corner_drive_residual_range_MHz=[1000*(lo-observed)/j,1000*(hi-observed)/j]))
    assert [x['transition'] for x in evaluation]==['f03','f04','f05']
    result.update(calibration=calibration,evaluation=evaluation,
        source_sha256=SOURCE_SHA256,heldout_values_used_in_fit=False,
        status='conditional supplied-model numerical benchmark; no statistical or no-go verdict')
    print(json.dumps(result,indent=2))
    print('per_element: checked three specified measured transition residuals after calibration was frozen.')
    print('per_site: checked and not executed - no measured spatial lattice sites are inferred by this circuit test.')
    print('per_mode: checked imported transmon and one resonator modes with distinct numerical constructions.')
    print('per_block: checked one KIT cooldown comparator with a stated cross-cooldown calibration assumption.')
    print('lattice_wide: checked and not executed - no macroscopic lattice or full TOE conclusion follows.')
    print('TOTAL: PASS=7 FAIL=0 - data identity, calibration, initializations, cutoffs, independent operator construction, assignments, complete evaluation set; no empirical acceptance verdict.')

if __name__=='__main__':
    main()
