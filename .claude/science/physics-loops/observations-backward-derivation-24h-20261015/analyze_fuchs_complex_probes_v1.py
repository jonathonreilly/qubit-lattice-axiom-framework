"""Post-exposure development extension; one previously opened trace only."""
import hashlib,json
from pathlib import Path
import numpy as np
from fuchs_weak_math_v1 import fit,serial_rows
from fuchs_weak_modulated_v1 import modulated_integrals,phase_slope
HERE=Path(__file__).resolve().parent
receipt=json.loads((HERE/'FUCHS_RAW_ACQUISITION_v1.json').read_text());source=Path(receipt['local_path'])
assert hashlib.sha256(source.read_bytes()).hexdigest()==receipt['sha256']
a=np.genfromtxt(source,delimiter=';',comments='%');assert a.shape==(678861,2) and np.isfinite(a).all()
edges=[0,*map(int,np.flatnonzero(np.diff(a[:,0])<0)+1),len(a)]
assert len(edges)==10
streams=[a[lo:hi] for lo,hi in zip(edges[:-1],edges[1:])]
assert all(np.array_equal(b[:,0],streams[0][:,0]) for b in streams)
t=streams[0][:,0]-streams[0][0,0];assert np.all(np.diff(t)>0)
assert all(np.all(streams[i][:,1]==streams[i][0,1]) for i in (6,7,8))
assert streams[7][0,1]==streams[8][0,1]
Omega=2*np.pi*streams[7][0,1]
phasors=[streams[j][:,1]*np.exp(1j*np.pi/180*streams[j+3][:,1]) for j in range(3)]
cases=[]
for receiver,sourceidx in ((2,3),(3,2)):
    z=phasors[receiver-1];us=phasors[sourceidx-1];assert np.all(abs(us)>0)
    slope,phase_meta=phase_slope(t,us)
    for inputmodel in ('unit_phasor','measured_voltage_phasor'):
        u=us/abs(us) if inputmodel=='unit_phasor' else us
        for duration in (600.,1200.,2400.):
            rows=modulated_integrals(t,z,u,duration,[0.,slope]);nwindows=len(rows)//2
            ntrain=2*(2*nwindows//3)
            all_fit=fit(rows,Omega);temporal=fit(rows,Omega,train_count=ntrain)
            thin=[]
            for stride in (2,4):
                ft=fit(modulated_integrals(t,z,u,duration,[0.,slope],stride),Omega)
                thin.append(dict(stride=stride,parameters=ft['parameters'],max_abs_parameter_change=float(max(abs(np.array(ft['parameters'])-all_fit['parameters'])))))
            cases.append(dict(receiver_demod_hypothesis=receiver,source_demod_hypothesis=sourceidx,input_model=inputmodel,
                duration_s=duration,source_phase_slope=phase_meta,time_windows=nwindows,probes_per_time_window=2,
                train_time_windows=ntrain//2,later_time_windows=nwindows-ntrain//2,fit_all=all_fit,
                chronological_development_check=temporal,quadrature_thinning=thin,rows=serial_rows(rows),
                input_moment_norm_zero=float(np.linalg.norm([r['moments'][3] for r in rows[::2]])),
                input_moment_norm_modulated=float(np.linalg.norm([r['moments'][3] for r in rows[1::2]])),
                unwindowed_tail_s=float(t[-1]-rows[-1]['t1'])))
out=dict(source_sha256=receipt['sha256'],cases=cases,development_only=True,post_v1_exposure=True,
    probes_are_correlated=True,reported_train_windows_means_probe_rows=True,
    physical_channel_assignment='Unestablished',force_or_scalar_parameter_estimate=False,
    source_phase_rule='Full-record affine unwrap slope; this includes later development data, not a held-out or prospective estimate',
    empirical_validation=False,reserved_raw_files_opened=False,
    sources={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('FUCHS_COMPLEX_PROBE_PLAN_v1.json','FUCHS_COMPLEX_PROBE_EXTENSION_v1.md','FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v2.md','FUCHS_RAW_ACQUISITION_v1.json','fuchs_weak_math_v1.py','fuchs_weak_modulated_v1.py',Path(__file__).name)})
print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))
