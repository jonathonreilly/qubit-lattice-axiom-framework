"""Independent FFT recomputation of the released author's finite spectral rows.

Only this checker's sealed edge polynomial and electric mask construct the
physics. Author JSON supplies rows to compare, never coefficients or builders.
The FFT implementation replaces the author's direct Laurent Fourier sums.
These remain uncut Gaussian means, not compact rotor propagation.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
import time
import numpy as np

BASE=Path(__file__).resolve().parent
def sha(path):return sha256(path.read_bytes()).hexdigest()

def edge_position(ed,data,L):
    ai,bi=data['edges'][ed]
    a=np.array(data['vertices'][ai]);b=np.array(data['vertices'][bi])
    a=(a+4)%8-4;b=(b+4)%8-4
    delta=b-a
    assert np.sum(np.abs(delta))==1
    mu=int(np.flatnonzero(delta)[0]);sign=int(delta[mu])
    tail=a if sign>0 else b
    return tuple(int(x%L) for x in tail)+(mu,),sign

def field(flow,data,L):
    out=np.zeros((L,L,L,3))
    for ed,power in flow:
        pos,sign=edge_position(ed,data,L);out[pos]+=sign*power
    return out

def spectral(L,data):
    grid=np.indices((L,L,L))
    eigenvalues=(2*np.sin(np.pi*grid/L))**2
    omega=np.sqrt(np.sum(eigenvalues,axis=0))
    inverse=np.zeros_like(omega);np.divide(1,omega,out=inverse,where=omega>0)
    cp=next(row['flow'] for row in data['defect_cosines'] if row['cos_coefficient']==170)
    cp_hat=np.fft.fftn(field(cp,data,L),axes=(0,1,2))
    cp_power=np.sum(abs(cp_hat)**2,axis=3);V=L**3
    vp=float(np.sum(cp_power*inverse)/(2*V))
    missing=np.zeros((L,L,L,3))
    for ed,pair in enumerate(data['electric_mask']):
        weight=1-pair[0]/pair[1]
        if weight:
            pos,_=edge_position(ed,data,L);missing[pos]=weight
    assert float(missing.sum())==24
    contexts=[]
    for eps in (.2,.4,.7,1.,2.,3.5):
        band=(omega>0)&(omega<=eps)
        vlow=float(np.sum(cp_power*inverse*band)/(2*V))
        row={'side':L,'epsilon':eps,'empty':vlow==0}
        if vlow:
            mu=float(np.sum(cp_power*band)/(2*V*vlow))
            projected=np.fft.ifftn(cp_hat*band[:,:,:,None],axes=(0,1,2))
            xi=projected/(2*np.sqrt(vlow))
            electric=float(np.sum(missing*abs(xi)**2))
            row.update({'band_modes_k':int(band.sum()),'vp':vp,'vlow':vlow,
                        'reference_mean_energy_times_tau':mu,
                        'electric_occupancy_energy_loss_times_tau':electric,
                        'xi_imaginary_max':float(np.max(abs(xi.imag))),
                        '_band':band,'_terms':[]})
        contexts.append(row)
    for term in data['defect_cosines']:
        w_hat=np.fft.fftn(field(term['flow'],data,L),axes=(0,1,2))
        variance=float(np.sum(np.sum(abs(w_hat)**2,axis=3)*inverse)/(2*V))
        overlap=np.sum(w_hat*np.conj(cp_hat),axis=3)*inverse/(2*V)
        for row in contexts:
            if row['empty']:continue
            chi=np.sum(overlap*row['_band'])/np.sqrt(row['vlow'])
            row['_terms'].append((term['cos_coefficient'],variance,float(abs(chi)**2)))
    for row in contexts:
        if row['empty']:continue
        terms=row.pop('_terms');row.pop('_band')
        magnetic=sum(a*chi2/4 for a,v,chi2 in terms)
        mu=row['reference_mean_energy_times_tau'];electric=row['electric_occupancy_energy_loss_times_tau']
        row.update({'magnetic_defect_energy_loss_times_tau':magnetic,
                    'limiting_added_full_mean_energy_times_tau':mu-magnetic-electric,
                    'relative_loss':(magnetic+electric)/mu,
                    'relative_loss_bound':float(Fraction(3591,128))*row['epsilon']**3 if row['epsilon']<=2 else None,
                    'finite_g_harmonic_rows':[]})
        for g in (.2,.1,.05,.025):
            empty_increment=mu*(1+np.exp(-g*g*vp/2))/2
            loss=sum(a*np.exp(-g*g*v/2)*chi2/4 for a,v,chi2 in terms)
            row['finite_g_harmonic_rows'].append({'g':g,
                  'uncut_harmonic_full_mean_increment_times_tau':float(empty_increment-electric-loss)})
    return contexts

def main():
    start=time.perf_counter()
    source=BASE/'LAURENT_DATA_L8.json';data=json.loads(source.read_text())
    independent=[*spectral(16,data),*spectral(32,data)]
    root=BASE/'post_frozen_author'
    author=json.loads((root/'ENERGY_SPECTRAL_RESULTS.json').read_text())['rows']
    historical=json.loads((root/'history/pre-electric-occupancy-correction/ENERGY_SPECTRAL_RESULTS.json').read_text())['rows']
    comparison=[];maxerror=0.;failed=[]
    for own,row,old in zip(independent,author,historical):
        assert (own['side'],own['epsilon'])==(row['side'],row['epsilon'])
        assert own['empty']==row['empty']==old['empty']
        errors={}
        if not row['empty']:
            assert own['band_modes_k']==row['band_modes_k']
            for name in ('vp','vlow','reference_mean_energy_times_tau','limiting_added_full_mean_energy_times_tau',
                         'magnetic_defect_energy_loss_times_tau','electric_occupancy_energy_loss_times_tau',
                         'relative_loss','relative_loss_bound'):
                if row[name] is None:assert own[name] is None;continue
                errors[name]=abs(own[name]-row[name])
            for i,(a,b) in enumerate(zip(own['finite_g_harmonic_rows'],row['finite_g_harmonic_rows'])):
                assert a['g']==b['g']
                errors['finite_g_'+str(a['g'])]=abs(a['uncut_harmonic_full_mean_increment_times_tau']-b['uncut_harmonic_full_mean_increment_times_tau'])
            e=own['electric_occupancy_energy_loss_times_tau']
            errors['historical_magnetic_only_limit']=abs(own['limiting_added_full_mean_energy_times_tau']+e-old['limiting_added_full_mean_energy_times_tau'])
            errors['historical_relative_loss']=abs(own['magnetic_defect_energy_loss_times_tau']/own['reference_mean_energy_times_tau']-old['relative_loss'])
            if old['relative_loss_bound'] is not None:
                errors['historical_relative_bound']=abs(float(Fraction(2943,128))*own['epsilon']**3-old['relative_loss_bound'])
            for a,b in zip(own['finite_g_harmonic_rows'],old['finite_g_harmonic_rows']):
                errors['historical_finite_g_'+str(a['g'])]=abs(a['uncut_harmonic_full_mean_increment_times_tau']+e-b['uncut_harmonic_full_mean_increment_times_tau'])
            maxerror=max(maxerror,*errors.values())
            if max(errors.values())>2e-11:failed.append([own['side'],own['epsilon'],errors])
        comparison.append({'side':own['side'],'epsilon':own['epsilon'],'empty':own['empty'],
                           'absolute_errors':errors})
    result={'method':__doc__,'independent_rows':independent,'author_comparison_rows':comparison,
            'max_absolute_difference':maxerror,'absolute_tolerance':2e-11,'discrepant_rows':failed,
            'current_rows_compared':len(author),'historical_rows_compared':len(historical),
            'current_finite_g_values_compared':sum(len(r.get('finite_g_harmonic_rows',[])) for r in author),
            'historical_finite_g_values_compared':sum(len(r.get('finite_g_harmonic_rows',[])) for r in historical),
            'PRE_data_sha256':sha(source),'author_result_sha256':sha(root/'ENERGY_SPECTRAL_RESULTS.json'),
            'code_sha256':sha(Path(__file__)),'elapsed_seconds':time.perf_counter()-start,
            'scope':'Independent FFT arithmetic for these supplied finite Gaussian examples, not an interval certificate or compact/full-time simulation.'}
    print(json.dumps(result,indent=2))
    assert not failed

if __name__=='__main__':main()
