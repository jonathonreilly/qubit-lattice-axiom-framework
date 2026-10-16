"""Descriptive, post-exposure figure for one deposited lock-in trace."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
r=json.loads((P/'FUCHS_RAW_ACQUISITION_v1.json').read_text())
raw=Path(r['local_path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256']
a=np.genfromtxt(raw.decode().splitlines(),delimiter=';',comments='%')
edges=[0,*map(int,np.flatnonzero(np.diff(a[:,0])<0)+1),len(a)]
streams=[a[lo:hi] for lo,hi in zip(edges[:-1],edges[1:])]
assert len(streams)==9 and all(np.array_equal(s[:,0],streams[0][:,0]) for s in streams)
t=(streams[0][:,0]-streams[0][0,0])/3600
fig,axs=plt.subplots(3,2,figsize=(11,9),layout='constrained')
for i,ch in enumerate((2,3)):
    amp=streams[ch-1][:,1]*1000;phase=np.unwrap(streams[ch+2][:,1]*np.pi/180)
    axs[i,0].plot(t,amp,lw=.6,color=['#255f91','#a34043'][i])
    axs[i,0].set(ylabel=f'Demod{ch} amplitude (mV)',xlabel='Elapsed time (h)')
    axs[i,1].plot(t,(phase-phase[0])/(2*np.pi),lw=.7,color=['#255f91','#a34043'][i])
    axs[i,1].set(ylabel=f'Demod{ch} phase change (turns)',xlabel='Elapsed time (h)')
old=json.loads((P/'FUCHS_DEVELOPMENT_RESULTS_v1.json').read_text())['cases']
new=json.loads((P/'FUCHS_COMPLEX_DEVELOPMENT_v1.json').read_text())['cases']
for cases,label,color in ((old,'Real compact probe','#a34043'),(new,'Real + modulated probes','#255f91')):
    selected=[c for c in cases if c['receiver_demod_hypothesis']==2 and c['input_model']=='unit_phasor' and c.get('model','exact_second_order_weak')=='exact_second_order_weak']
    xs=[c['duration_s']/60 for c in selected]
    axs[2,0].plot(xs,[c['fit_all']['forcing_coefficient_abs']/1e-7 for c in selected],'o-',label=label,color=color)
    axs[2,1].plot(xs,[c['fit_all']['train_residual_rms']/c['fit_all']['train_R_rms'] for c in selected],'o-',label=label,color=color)
axs[2,0].set(xlabel='Window duration (min)',ylabel='Conditional |b| (1e-7 V/s)',yscale='log',xticks=[10,20,40])
axs[2,1].set(xlabel='Window duration (min)',ylabel='RMS residual / RMS weak target',xticks=[10,20,40])
axs[2,1].legend(fontsize=8,loc='upper right')
for ax in axs.flat:ax.grid(alpha=.2)
fig.suptitle('Fuchs2024: one exposed development record\nInstrument channels and descriptive weak fits; no force calibration or physical identification',fontsize=12)
fig.savefig(P/'FUCHS_DEVELOPMENT_DIAGNOSTIC_v1.png',dpi=160)
fig.savefig(P/'FUCHS_DEVELOPMENT_DIAGNOSTIC_v1.pdf')
manifest={'source_sha256':r['sha256'],'all_samples_plotted':True,'selected_physical_wiring':False,'force_estimate':False,'empirical_validation':False,
    'note':'Within-record descriptive comparison after both analyses; no confidence intervals or unseen tests',
    'files':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('plot_fuchs_development_v1.py','FUCHS_DEVELOPMENT_RESULTS_v1.json','FUCHS_COMPLEX_DEVELOPMENT_v1.json','FUCHS_DEVELOPMENT_DIAGNOSTIC_v1.png','FUCHS_DEVELOPMENT_DIAGNOSTIC_v1.pdf')}}
(P/'FUCHS_FIGURE_IDENTITY_v1.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest))
