"""Frozen development diagnostics. Does not label a device as a physical force."""
import hashlib,json,sys
from pathlib import Path
import numpy as np
from fuchs_weak_math_v1 import integrals,fit,serial_rows
HERE=Path(__file__).resolve().parent
receipt=json.loads((HERE/"FUCHS_RAW_ACQUISITION_v1.json").read_text())
source=Path(receipt["local_path"])
assert hashlib.sha256(source.read_bytes()).hexdigest()==receipt["sha256"]
a=np.genfromtxt(source,delimiter=";",comments="%")
assert a.ndim==2 and a.shape[1]==2 and np.isfinite(a).all()
edges=[0,*map(int,np.flatnonzero(np.diff(a[:,0])<0)+1),len(a)]
assert len(edges)==10
streams=[a[lo:hi] for lo,hi in zip(edges[:-1],edges[1:])]
assert all(np.array_equal(b[:,0],streams[0][:,0]) for b in streams)
t=streams[0][:,0]-streams[0][0,0]
assert np.all(np.diff(t)>0)
assert all(np.all(streams[i][:,1]==streams[i][0,1]) for i in (6,7,8))
assert streams[7][0,1]==streams[8][0,1]
freq=float(streams[7][0,1]);Omega=2*np.pi*freq
phasors=[streams[j][:,1]*np.exp(1j*np.pi/180*streams[j+3][:,1]) for j in range(3)]
cases=[]
for receiver,sourceidx in ((2,3),(3,2)):
    z=phasors[receiver-1];us=phasors[sourceidx-1]
    assert np.all(abs(us)>0)
    for inputmodel in ("unit_phasor","measured_voltage_phasor"):
        u=us/abs(us) if inputmodel=="unit_phasor" else us
        for duration in (600.,1200.,2400.):
            rows=integrals(t,z,u,duration)
            ntrain=2*len(rows)//3
            for exact in (True,False):
                fitall=fit(rows,Omega,exact)
                temporal=fit(rows,Omega,exact,ntrain)
                thin=[]
                for stride in (2,4):
                    fthin=fit(integrals(t,z,u,duration,stride),Omega,exact)
                    thin.append(dict(stride=stride,parameters=fthin["parameters"],
                       max_abs_parameter_change=float(np.max(abs(np.array(fthin["parameters"])-fitall["parameters"])))))
                cases.append(dict(receiver_demod_hypothesis=receiver,source_demod_hypothesis=sourceidx,
                      input_model=inputmodel,duration_s=duration,
                      model="exact_second_order_weak" if exact else "first_order_comparison",
                      fit_all=fitall,chronological_development_check=temporal,
                      quadrature_thinning=thin,rows=serial_rows(rows) if exact else None,
                      unwindowed_tail_s=float(t[-1]-rows[-1]["t1"])))
stats=[]
for j,z in enumerate(phasors):
    phase=np.unwrap(np.angle(z))
    stats.append(dict(demod=j+1,amplitude_min_V=float(min(abs(z))),amplitude_max_V=float(max(abs(z))),
                     net_phase_turns=float((phase[-1]-phase[0])/(2*np.pi)),
                     maximum_phase_increment_rad=float(max(abs(np.diff(phase))))))
out=dict(source_sha256=receipt["sha256"],source_bytes=receipt["bytes"],development_only=True,
         carrier_from_record_Hz=freq,points_per_stream=len(t),duration_s=float(t[-1]),channel_stats=stats,
         physical_channel_assignment="Unestablished; hypotheses compared without promoting fit to wiring evidence",
         phase_or_voltage_as_force_map="Unestablished; both diagnostic inputs retained",
         cases=cases,sources={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in
          ("FUCHS_WEAK_DEVELOPMENT_PLAN_v1.json","FUCHS_RELATIVE_MOTION_AND_WEAK_INVERSE_v1.md",
           "FUCHS_RAW_ACQUISITION_v1.json","fuchs_weak_math_v1.py",Path(__file__).name)},
         empirical_validation=False,force_or_scalar_parameter_estimate=False,reserved_raw_files_opened=False)
print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))
