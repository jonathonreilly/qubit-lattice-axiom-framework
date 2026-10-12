"""Post-freeze comparison and predeclared physical-input evaluation."""
from pathlib import Path
import hashlib
import itertools
import json
import sys
sys.dont_write_bytecode=True
import solar_quadrupole as q
import numpy as np

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def physical(a0,g,sigma=0.0,n=128):
    row=q.prediction(float(a0),float(g),float(sigma),n=n)
    # Unit-explicit output names; the original module's internal key is ambiguous.
    row['Q2_s_minus2']=row.pop('Q2_s_m2')
    row['Hzz_s_minus2']=row.pop('Hzz_s_m2')
    return row

def main():
    start=q.checkpoint()
    own=q.OUT/'initial_numerical_results.json'
    freeze=json.loads((q.OUT/'initial_numerical_freeze.json').read_text())
    assert digest(own)==freeze['sha256'] and not freeze['parent_results_read']
    parent=q.RUNTIME/'gravity/solar_external_independent_results.json'
    mine={r['eta']:r['values'][-1] for r in json.loads(own.read_text())['rows']}
    theirs=[r for r in json.loads(parent.read_text())['results'] if r['order']==512]
    comparison=[]
    for row in theirs:
        eta=row['eta']
        if eta not in mine:
            continue
        h=-2*mine[eta]['ibp']/3
        comparison.append(dict(eta=eta,own_h=h,parent_h_parts=row['h_parts'],parent_h_direct=row['h_direct'],parts_relative_difference=(h-row['h_parts'])/abs(h),direct_relative_difference=(h-row['h_direct'])/abs(h)))

    central=[]
    for label,a0 in [('primary_free_ML',q.A0_PRIMARY),('fixed_ML_control',q.A0_FIXED_ML)]:
        for sigma in [0.0,47.0]:
            row=physical(a0,2.32e-10,sigma,n=256)
            row.update(calibration=label,conversion='spherical' if sigma==0 else 'disk_approx')
            row['density_F']=q.response(row['eta_N'],256,60.0,'density')
            central.append(row)

    box=[]
    for conversion,sigmas in [('spherical',[0.0]),('disk_approx',np.linspace(41,53,5))]:
        for a0,g,sigma in itertools.product(np.linspace(7.65e-11,8.70e-11,9),np.linspace(2.00e-10,2.64e-10,17),sigmas):
            if len(box)%100==0:
                q.checkpoint()
            row=physical(a0,g,sigma)
            row['conversion']=conversion
            box.append(row)
    envelopes={}
    for conversion in ['spherical','disk_approx']:
        selected=[r for r in box if r['conversion']==conversion]
        lo=min(selected,key=lambda r:r['Q2_s_minus2'])
        hi=max(selected,key=lambda r:r['Q2_s_minus2'])
        for row in [lo,hi]:
            row['higher_order_Q2_s_minus2']=physical(row['a0'],row['g_physical'],row['sigma_Msun_pc2'],256)['Q2_s_minus2']
        envelopes[conversion]=dict(min=lo,max=hi,count=len(selected),status='sampled numerical envelope; not certified global extrema or statistical interval')

    # Check finite differences across every row of the declared rectangular grid.
    slopes={}
    for conversion,sigmas in [('spherical',[0.0]),('disk_approx',np.linspace(41,53,5))]:
        selected=[r for r in box if r['conversion']==conversion]
        arr=np.array([r['Q2_s_minus2'] for r in selected]).reshape(9,17,len(sigmas))
        axes={}
        for axis,name in [(0,'a0'),(1,'g_e'),(2,'Sigma')]:
            if arr.shape[axis]>1:
                diff=np.diff(arr,axis=axis)
                axes[name]=dict(min_step=float(diff.min()),max_step=float(diff.max()),all_increasing=bool(np.all(diff>0)),all_decreasing=bool(np.all(diff<0)))
        slopes[conversion]=axes

    # Exposed publication numbers are a post-freeze scale/convention control only.
    publication_control=[]
    for sigma,quoted in [(0.0,3.387e-26),(47.0,3.411e-26)]:
        row=physical(1.02e-10,2.32e-10,sigma,256)
        row['Park2026_quoted_Q2_s_minus2']=quoted
        row['relative_difference_from_rounded_publication']=(row['Q2_s_minus2']-quoted)/quoted
        publication_control.append(row)

    payload=dict(started_at=start,finished_at=q.checkpoint(),own_initial_sha256=digest(own),parent_results_sha256=digest(parent),code_sha256=digest(Path(__file__)),
        parent_comparison=comparison,convention='Our Q2=-3Hzz/2, opposite parent QPhi=+3Hzz/2; compare raw Hzz first',central=central,
        sampled_envelopes=envelopes,sampled_monotonicity=slopes,parameter_box_rows=box,publication_controls=publication_control,
        targets=dict(Park2026=dict(Q2=1.6e-27,sigma=1.8e-27,summary_rectangle=[-2.0e-27,5.2e-27]),Hees2014=dict(Q2=3e-27,sigma=3e-27,summary_rectangle=[-3e-27,9e-27])),
        interpretation='No solar parameters fit. Fixed candidate plus provisional galaxy-to-PDE transfer and external-field prescriptions. No likelihood, confidence level, blind test, or arbitrary-QUMOND exclusion.')
    dest=q.OUT/'physical_comparison_results.json'
    assert not dest.exists()
    dest.write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k!='parameter_box_rows'},indent=2))
    print('RESULT_SHA256',digest(dest))

if __name__=='__main__':
    main()
