"""Physical-offset Ramsey comparison using separately calibrated parameters.
The offset envelope is numerical, not a certified continuum bound.
"""
import numpy as np
from scipy.optimize import minimize_scalar
from ens_andreev_resonator_model_2026_09_27 import endpoint,predict
from ens_direct_charge_check_2026_09_27 import solve

def physical(p,q,**kwargs):
    delta=p[3]**2/(4*p[0]*p[2]);assert 0<=delta<1
    return endpoint(p,q*(1-delta),**kwargs)

def construct_parity(calibrated):
    output={}
    for name in ('cosine','andreev'):
        p=calibrated[name]['parameters'];rows=[]
        for q in np.linspace(0,1,65):
            f,labels=physical(p,float(q),N=20,M=18,K=12,grid=8192)
            rows.append(dict(physical_q=float(q),frequency_GHz=f.tolist(),labels=labels))
        pairs=[dict(physical_q=rows[k]['physical_q'],splitting_MHz=abs(rows[k]['frequency_GHz'][5]-rows[k+32]['frequency_GHz'][5])*1000,center_GHz=(rows[k]['frequency_GHz'][5]+rows[k+32]['frequency_GHz'][5])/2) for k in range(33)]
        def splitting(q):
            return abs(physical(p,q,N=20,M=18,K=12,grid=8192)[0][5]-physical(p,q+.5,N=20,M=18,K=12,grid=8192)[0][5])*1000
        extrema=[]
        for lo,hi in ((0,.0625),(.0625,.125),(.125,.1875),(.1875,.25)):
            fit=minimize_scalar(lambda q:-splitting(q),bounds=(lo,hi),method='bounded',options={'xatol':1e-8})
            assert fit.success
            extrema.append(dict(bounds=[lo,hi],q=float(fit.x),splitting_MHz=-float(fit.fun),endpoints_MHz=[float(splitting(lo)),float(splitting(hi))],success=bool(fit.success)))
        controls=[]
        for q in (0.,.25,.5,1.):
            f,d=physical(p,q,N=24,M=22,K=16,grid=16384);change=(f[5]-rows[round(q*64)]['frequency_GHz'][5])*1e9
            assert abs(change)<1., 'Selected parity cutoff control exceeds1Hz'
            controls.append(dict(physical_q=q,f06_GHz=float(f[5]),primary_to_fine_Hz=float(change),labels=d))
        independent=[]
        for q in (0.,.25,.5):
            direct,_=solve(22,16,q,parameters=p,physical_offset=True)
            fine=next(x['f06_GHz'] for x in controls if x['physical_q']==q)
            error=(direct['frequencies_GHz'][5]-fine)*1e9
            assert abs(error)<1. and direct['eigen_residual_max_GHz']<1e-7
            independent.append(dict(physical_q=q,direct=direct,independent_minus_fine_Hz=float(error)))
        old,_=predict(p,N=20,M=18,K=12,grid=8192);new=(np.array(rows[0]['frequency_GHz'])+np.array(rows[32]['frequency_GHz']))/2
        period=(rows[-1]['frequency_GHz'][5]-rows[0]['frequency_GHz'][5])*1e9
        assert abs(period)<1., 'Physical offset period control'
        assert pairs[16]['splitting_MHz']<1e-6, 'Quarter-offset parity symmetry'
        corners=[]
        for row in calibrated['rounding_corners' if name=='andreev' else 'baseline_corners']:
            pp=row['parameters'];f0,_=physical(pp,0,N=20,M=18,K=12,grid=8192);fh,_=physical(pp,.5,N=20,M=18,K=12,grid=8192)
            corners.append(dict(signs=row['signs'],parameters=pp,endpoint_splitting_MHz=float(abs(f0[5]-fh[5])*1000)))
        maximum=max([r['splitting_MHz'] for r in pairs]+[v for r in extrema for v in r['endpoints_MHz']]+[r['splitting_MHz'] for r in extrema])
        output[name]=dict(parameters=p,physical_offset_rows=rows,parity_pairs=pairs,numerical_maximum_MHz=maximum,center_range_MHz=1000*(max(r['center_GHz'] for r in pairs)-min(r['center_GHz'] for r in pairs)),local_extrema=extrema,cutoff_controls=controls,independent_direct=independent,period_error_Hz=float(period),physical_minus_old_calibration_mean_Hz=((new-old)[[0,1,6,7,8]]*1e9).tolist(),rounding_endpoint_controls=corners)
    return output

def compare_figure(predictions,figure):
    """Only called after calibration and physical predictions are constructed."""
    rows=[]
    for row in figure['rows']:
        # These are visibly identified branch windows in digitized source data.
        low=max((r for r in row['bins'] if 8<=r['center_MHz']<=9.8),key=lambda r:r['mean_blue_minus_red'])
        high=max((r for r in row['bins'] if 10<=r['center_MHz']<=12),key=lambda r:r['mean_blue_minus_red'])
        separation=high['center_MHz']-low['center_MHz'];bin_range=[high['edges_MHz'][0]-low['edges_MHz'][1],high['edges_MHz'][1]-low['edges_MHz'][0]]
        assert 0<bin_range[0]<=separation<=bin_range[1]
        rows.append(dict(time_min=row['time_min'],positive_peaks_MHz=[low['center_MHz'],high['center_MHz']],positive_peak_separation_MHz=separation,geometric_bin_range_MHz=bin_range,cosine_numerical_max_below_bin_range=predictions['cosine']['numerical_maximum_MHz']<bin_range[0],andreev_numerical_max_above_bin_range=predictions['andreev']['numerical_maximum_MHz']>bin_range[1]))
    assert {r['time_min'] for r in rows}=={40,120}
    assert all(r['cosine_numerical_max_below_bin_range'] and r['andreev_numerical_max_above_bin_range'] for r in rows), 'Declared nominal scale comparison changed'
    return dict(rows=rows,scope='Necessary envelope-capacity comparison under same-sign detunings and cross-acquisition device mapping; geometric bins are not confidence intervals; unknown charge offset is not fitted or predicted.')
