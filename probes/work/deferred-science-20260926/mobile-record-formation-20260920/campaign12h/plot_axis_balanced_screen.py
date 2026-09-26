#!/usr/bin/env python3
"""Export the completed fixed-plan axis-balanced screen, with source receipts."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent;D=HERE/'axis_balanced_screen';F=HERE/'figures';F.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=json.loads((D/'STATIONARY_ANALYSIS.json').read_text());assert len(rows)==6
completed=json.loads((D/'COMPLETED_CASES.json').read_text());assert len(completed)==8
for case in completed:
    assert sha(D/(case['case']+'.npz'))==case['raw_npz_sha256']
    assert sha(D/(case['case']+'.json'))==case['metadata_sha256']
for row in rows:assert sha(D/(row['case']+'_stationary_analysis.npz'))==row['analysis_npz_sha256']
by={(r['rho'],int(r['case'].rsplit('L',1)[1])):r for r in rows}
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,axs=plt.subplots(2,2,figsize=(11,7.5),layout='constrained')
for ax,rho in zip(axs.flat,(.25,.5,.75)):
    theta=np.linspace(0,2*np.pi,301);ax.plot(theta,np.cos(theta),color='#777777',ls=':',lw=1.5,label='Euler cosine')
    for size,color,style in ((32,'#9c6b30','--'),(64,'#176087','-')):
        row=by[rho,size];data=np.load(D/(row['case']+'_stationary_analysis.npz'))
        t=data['axis_theta'];m=data['axis_density_mean'];lo,hi=data['axis_density_ci']
        ax.plot(t,m,color=color,ls=style,lw=1.8,label=f'L={size}')
        ax.fill_between(t,lo,hi,color=color,alpha=.12)
    ax.axhline(0,color='#cccccc',lw=.7);ax.set_xlim(0,2*np.pi);ax.set_ylim(-1.08,1.2)
    ax.set_xticks([0,np.pi,2*np.pi],['0',r'$\pi$',r'$2\pi$'])
    ax.set_title(rf'Density correlation, $\rho={rho:g}$')
    ax.set_xlabel(r'Predicted phase $c_s |k|t$');ax.set_ylabel('Normalized axial correlation')
axs.flat[0].legend(loc='upper right',frameon=False,fontsize=9)
ax=axs.flat[3];r=np.linspace(.2,.8,201)
ax.plot(r,2*r*np.sqrt((1-r)/3),color='#444444',lw=1.5,label='Predicted speed')
for group,color,offset,marker in [('axis','#176087',-.008,'o'),('face','#ab6634',0,'s'),('body','#42846b',.008,'^')]:
    x=[];y=[];lower=[];upper=[]
    for rho in (.25,.5,.75):
        fit=by[rho,64]['groups'][group]['complex_fit'];lo,hi=fit['pointwise_bootstrap_parameter_intervals'][1]
        x.append(rho+offset);y.append(fit['speed']);lower.append(fit['speed']-lo);upper.append(hi-fit['speed'])
    ax.errorbar(x,y,yerr=[lower,upper],fmt=marker,color=color,ms=5,capsize=3,label=f'L=64 {group}')
ax.set_xlabel(r'Density $\rho$ (directions offset for legibility)');ax.set_ylabel('Fitted speed, lattice sites / tick')
ax.set_title('All nine L=64 directional fits');ax.legend(frameon=False,fontsize=9,loc='lower right')
fig.suptitle('Immutable axis-balanced exchanges: larger-volume screen',fontsize=15)
fig.supxlabel('256 complete paths per case. Shading: pointwise 95% path-bootstrap intervals. Speed intervals omit fit-model error.',fontsize=9)
stem=F/'axis_balanced_completed_screen';fig.savefig(stem.with_suffix('.png'),dpi=180);fig.savefig(stem.with_suffix('.pdf'));plt.close(fig)

lines=['# Completed axis-balanced wave screen','',
       '2026-09-21. Fixed supplied rate parameters and predeclared simulation/analysis plan. This is finite-volume evidence, not a scaling theorem.','',
       'All eight planned cases completed, including the three L=64 stationary cases. Each stationary case used 256 independent paths. The source/seed-preserving continuation changed batch execution only; its bitwise control and scheduling receipts are retained.','',
       'The L=64 fitted speeds agree with the predeclared density-dependent speed within each of the nine conditional bootstrap intervals. Damping remains substantial: the first axial density minimum is about -0.49 to -0.61 instead of the Euler cosine value -1. Increasing volume improves the oscillation amplitude in every density case, but two sizes do not establish a limiting rate.','',
       '| Density | L | Predicted speed | Axial fitted speed [95% bootstrap] | Axial first-minimum correlation [95% bootstrap] |',
       '|---|---:|---:|---|---|']
maximum=0;covered=0
for rho in (.25,.5,.75):
    for size in (32,64):
        row=by[rho,size];v=row['groups']['axis'];fit=v['complex_fit'];lo,hi=fit['pointwise_bootstrap_parameter_intervals'][1];dl,dh=v['density_pointwise_95_interval']
        lines.append(f"| {rho:.2f} | {size} | {row['reference_speed']:.6f} | {fit['speed']:.6f} [{lo:.6f}, {hi:.6f}] | {v['density_at_that_time']:.4f} [{dl:.4f}, {dh:.4f}] |")
        if size==64:
            for group,data in row['groups'].items():
                f=data['complex_fit'];a,b=f['pointwise_bootstrap_parameter_intervals'][1]
                covered+=int(a<=row['reference_speed']<=b)
                maximum=max(maximum,abs(f['speed']/row['reference_speed']-1))
                assert f['optimizer_success'] and f['bootstrap_optimizer_failures']==0
lines += ['',f'The maximum relative speed discrepancy among the nine L=64 fits is {maximum*100:.3f}%; {covered}/9 displayed intervals contain the predicted value. This is a descriptive comparison across correlated fitted observables, not a simultaneous confidence statement.','',
          'The fit uses a complex damped exponential over the first predicted half-period. Four thousand whole-trajectory bootstrap samples preserve dependence among times, fields and symmetry modes; one thousand are refitted. Directional shells are averaged within each path. Pointwise intervals describe sampling variation conditional on the fit and omit finite-size and model error. Raw correlation arrays and every bootstrap fit are available for alternate diagnostics.','',
          'All completed raw NPZ and metadata identities were authenticated. The maximum final Fourier reconstruction discrepancy is '+f"{max(c['max_fourier_reconstruction_error'] for c in completed):.3g}. The exact conserved counts and birth bookkeeping remain in the raw audits.", '',
          'The two nonstationary uniform-birth cases have a separate evolving-covariance analysis in GROWING_ANALYSIS.json; they are not folded into stationary speed fits. The native formation experiments use another generator and remain separate.','',
          'The plot is figures/axis_balanced_completed_screen.png (and PDF). Figure, analysis, fit, plan and raw input identities are recorded in figures/AXIS_BALANCED_FIGURE_PROVENANCE.json. No inferred parameter or target was changed after seeing these data.']
(HERE/'AXIS_BALANCED_COMPLETED_SCREEN_REPORT.md').write_text('\n'.join(lines)+'\n')
inputs=[D/'STATIONARY_ANALYSIS.json',D/'COMPLETED_CASES.json',HERE/'AXIS_BALANCED_SIMULATION_PLAN.md',HERE/'analyze_stationary_context_cases.py',HERE/'analyze_context_exchange.py']
inputs += [D/(r['case']+'_stationary_analysis.npz') for r in rows]
receipt=dict(plot_source_sha256=sha(Path(__file__)),inputs={str(p.relative_to(HERE)):sha(p) for p in inputs},raw_cases=completed,
             outputs={str(p.relative_to(HERE)):sha(p) for p in (stem.with_suffix('.png'),stem.with_suffix('.pdf'),HERE/'AXIS_BALANCED_COMPLETED_SCREEN_REPORT.md')},maximum_L64_relative_speed_discrepancy=maximum,interval_coverage_count=covered,versions=dict(numpy=np.__version__,matplotlib=matplotlib.__version__),scope='Descriptive fixed-plan finite-volume screen; no claim of universal or asymptotic physics.')
(F/'AXIS_BALANCED_FIGURE_PROVENANCE.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(cases=len(completed),stationary_cases=len(rows),L64_directional_intervals_containing_reference=covered,maximum_relative_speed_discrepancy=maximum,figure=str(stem.with_suffix('.png')))))
