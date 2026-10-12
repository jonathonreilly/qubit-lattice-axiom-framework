#!/usr/bin/env python3
"""Extract a previously unfitted far-field consequence of frozen responses."""
import datetime as dt
import json
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
import direct_shared_response_fit as fit


def main():
    fit.operator.guard()
    out=fit.operator.OUT/'FAR_FIELD_PREDICTION_v1.json'
    assert not out.exists()
    fits_path=fit.operator.OUT/'shared_response_fits_v1.json'
    margin_path=fit.operator.OUT/'margin_candidate_v1.json'
    fits=json.loads(fits_path.read_text())
    margin=json.loads(margin_path.read_text())
    original=next(row['best_sampled'] for row in fits['cases'] if row['family']=='D' and row['constraints']=='galaxies_external_solar')
    rows=[]
    au=149597870700
    for label,candidate in [('original_D_joint',original),('interior_D_joint',margin)]:
        weights=np.array(candidate['weights'])
        knots=fit.operator.KNOTS
        E=candidate['external_newtonian_SI']
        cell=np.searchsorted(knots,E)-1
        assert knots[cell]<E<knots[cell+1] and weights[cell]==0
        first,last=cell,cell
        while first>0 and weights[first-1]==0:
            first-=1
        while last<len(weights)-1 and weights[last+1]==0:
            last+=1
        low=knots[first] if first>0 else 0.
        high=knots[last+1] if last<len(weights)-1 else np.inf
        N=lambda acceleration: 1+sum(w*fit.operator.ramp(acceleration,lo,hi) for w,lo,hi in zip(weights,knots[:-1],knots[1:]))
        ne=float(N(E))
        delta=min(E-low,high-E)
        assert delta>0
        radius=np.sqrt(fit.GM/delta)
        x,q=roots_legendre(128)
        checks=[]
        for factor in [1.001,2.,10.]:
            r=radius*factor
            strength=fit.GM/(r*r)
            magnitude=np.sqrt(E*E+strength*strength+2*E*strength*x)
            response=N(magnitude)
            flux_coefficient=.5*np.dot(q,response*(1+E/strength*x))
            assert np.max(np.abs(response-ne))<1e-14
            assert abs(flux_coefficient-ne)<1e-11
            checks.append({'radius_over_support_bound':factor,'flux_over_4piGM':float(flux_coefficient)})
        rows.append({'candidate':label,'E_SI':E,'constant_interval_SI':[float(low),float(high)],
                     'N_E':ne,'K_E':0.,'asymptotic_acceleration_ratio':ne,
                     'asymptotic_circular_speed_scale_ratio':float(np.sqrt(ne)),
                     'solar_mass_support_bound_AU':float(radius/au),'delta_SI':float(delta),'flux_checks':checks})
    result={'at':dt.datetime.now(dt.timezone.utc).isoformat(),
            'source_sha256':fit.operator.field.sha(__file__),
            'note_sha256':fit.operator.field.sha(Path(__file__).with_name('DIRECT_FAR_FIELD_PREDICTION.md')),
            'fits_sha256':fit.operator.field.sha(fits_path),'margin_sha256':fit.operator.field.sha(margin_path),
            'rows':rows,'scope':'Asymptotic point-source/test-particle prediction under constant external boundary. No finite-radius force accuracy, two-body orbit likelihood or observational success claimed.'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
