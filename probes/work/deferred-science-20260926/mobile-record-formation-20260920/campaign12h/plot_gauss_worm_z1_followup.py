from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent;source=HERE/'gauss_worm_z1_followup/analysis/FOLLOWUP_ANALYSIS.json'
data=json.loads(source.read_text());out=HERE/'figures';out.mkdir(exist_ok=True)
fig,axes=plt.subplots(2,2,figsize=(11,7),layout='constrained')
colors=['#1763a6','#d07821'];labels=['Empty start','Fully aligned start']
for init in (0,1):
    selected=sorted([c for c in data['cases'] if c['metadata']['initialization']==init],key=lambda c:c['metadata']['L'])
    sizes=np.array([c['metadata']['L'] for c in selected]);profiles=[c['profiles'][1] for c in selected]
    for ax,key in [(axes[0,0],'ratio_axis'),(axes[0,1],'ratio_diagonal'),(axes[1,0],'rho'),(axes[1,1],'S_x1')]:
        vals=np.array([p['values'][key]['estimate'] for p in profiles]);ci=np.array([p['values'][key]['interval'] for p in profiles])
        ax.errorbar(sizes+(init-.5)*.65,vals,yerr=np.array([vals-ci[:,0],ci[:,1]-vals]),fmt='o-',color=colors[init],capsize=3,lw=1.3,ms=5,label=labels[init])
for ax in axes.flat:
    ax.set_xlabel('Lattice side L');ax.set_xticks([17,25,33,49]);ax.grid(alpha=.17)
for ax in axes[0]:
    ax.axhline(1,color='#444444',ls='--',lw=1,label='Flat-spectrum ratio')
    x=np.linspace(17,49,100);ax.plot(x,1/(4*np.cos(2*np.pi/x)**2),color='#969696',ls=':',lw=1.5,label='Quadratic sin² comparator')
    ax.set_ylim(.18,1.24);ax.set_ylabel('S(first mode) / S(second mode)')
axes[0,0].set_title('Axis modes (1,0,0) and (2,0,0)')
axes[0,1].set_title('Diagonal modes (1,1,0) and (2,2,0)')
axes[0,0].legend(frameon=False,fontsize=8,loc='center right')
axes[1,0].set_title('Occupation agrees across initializations');axes[1,0].set_ylabel('Occupied fraction');axes[1,0].ticklabel_format(axis='y',useOffset=False)
axes[1,1].set_title('Lowest axis-mode transverse spectral trace');axes[1,1].set_ylabel('S_T = |Ê(k)|² / (2L³)')
fig.suptitle('Gauss-constrained equilibrium screen at fugacity 1',fontsize=15)
fig.supxlabel('Author follow-up: 10⁹ production attempts per chain. Bars: paired 1024-sample block bootstrap.\nSerial dependence and equilibration are not certified; no phase or physical formation-state claim.',fontsize=9)
png=out/'gauss_worm_z1_followup.png';pdf=out/'gauss_worm_z1_followup.pdf';fig.savefig(png,dpi=180);fig.savefig(pdf)
(out/'gauss_worm_z1_followup_provenance.json').write_text(json.dumps(dict(analysis_path=str(source),analysis_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),raw_identities_sha256=data['raw_identities_sha256'],outputs=[dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in (png,pdf)]),indent=2)+'\n')
print(png)
