#!/usr/bin/env python3
"""Plot the frozen declared statistics; performs no new fit or resampling."""
from pathlib import Path
import hashlib,json,shutil
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

HERE=Path(__file__).resolve().parent
SOURCE=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/geometric_fixed_rate_analysis')
OUT=HERE/'geometric_fixed_rate_results'
OUT.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
EXPECTED='51b2f9b5174877030b7ebb8baa345dd030dbeb23b3ca3072f6525fb73ed79c86'
assert sha(SOURCE/'RESULTS.json')==EXPECTED
data=json.loads((SOURCE/'RESULTS.json').read_text())
assert data['runs_used']==2496 and data['excluded']==[] and len(data['cells'])==12
for name in ['RESULTS.json','TABLE.md','PER_HISTORY.json','RECEIPT_VERIFICATION.json']:
    target=OUT/name
    if target.exists():assert target.read_bytes()==(SOURCE/name).read_bytes()
    else:shutil.copy2(SOURCE/name,target)
settings=[('S1','Longest-mode transverse power',r'$S_1$',None),
          ('S4_over_S1','Spectral shape',r'$S_4/S_1$',1),
          ('W_over_S1','Winding and longest-mode power',r'$W/S_1$',1),
          ('axis_mode_fourth_ratio','Individual-mode fourth moment',r'$\langle S_{\rm mode}^2\rangle/\langle S_1\rangle^2$',1.5),
          ('time_per_volume','Scaled formation time',r'$\beta\,\langle T\rangle/V$',None),
          ('site_reuse_fraction','Sites with a later birth',r'Fraction with birth count $>1$',None)]
colors=['#2166ac','#bd6a17','#228b69'];markers=['o','s','^']
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'semibold','pdf.fonttype':42})
fig,axes=plt.subplots(2,3,figsize=(13.2,8.5))
for ax,(key,title,ylabel,ref) in zip(axes.flat,settings):
    if ref is not None:
        ax.axhline(ref,color='#777777',lw=1,ls='--',zorder=0)
    for rate,color,marker in zip([.1,1.,10.],colors,markers):
        rows=sorted((r for r in data['cells'] if r['beta']==rate),key=lambda r:r['N'])
        x=np.array([r['N'] for r in rows]);v=[r['observables'][key] for r in rows]
        assert all(d['estimate_status']==d['CI_status']=='defined' for d in v)
        y=np.array([d['estimate'] for d in v]);ci=np.array([d['CI95_pointwise'] for d in v])
        if key=='time_per_volume':y*=rate;ci*=rate
        ax.errorbar(x,y,yerr=np.stack([y-ci[:,0],ci[:,1]-y]),color=color,marker=marker,
                    markersize=5,capsize=3,lw=1.2,label=rf'$\beta/\kappa={rate:g}$')
    ax.set_xscale('log',base=2);ax.set_xticks([16,32,64,128])
    ax.xaxis.set_major_formatter(ScalarFormatter());ax.set_xlabel('Side length N')
    ax.set_title(title,pad=9);ax.set_ylabel(ylabel);ax.grid(axis='y',alpha=.17)
    if key=='S1':ax.set_ylim(0,.26)
    if key=='site_reuse_fraction':ax.set_ylim(0,.30)
    if key=='time_per_volume':ax.set_ylim(0,.46)
axes.flat[0].legend(frameon=False,fontsize=10,loc='lower left')
fig.suptitle('Record formation on cubic tori: declared fixed-rate follow-up',fontsize=17,y=.975)
fig.text(.5,.93,'First completed geometry • 2,496 independent histories • κ = 1',ha='center',fontsize=11,color='#444444')
fig.text(.5,.025,'Bars: pointwise 95% whole-history bootstrap intervals. 256 histories/cell for N ≤ 64; 64 for N = 128.\nDashed lines are conditional flat-spectrum / Gaussian references. No asymptotic fit or equilibrium identification.',ha='center',fontsize=10,color='#444444')
fig.subplots_adjust(top=.86,bottom=.13,hspace=.45,wspace=.34)
for ext in ['png','pdf']:fig.savefig(OUT/f'fixed_rate_formation.{ext}',dpi=190,facecolor='white')
plt.close(fig)
receipt=dict(source_result_sha256=EXPECTED,plotter_sha256=sha(Path(__file__)),
input_copies={p.name:sha(p) for p in OUT.iterdir() if p.suffix in ['.json','.md'] and p.name!='PLOT_RECEIPT.json'},
figures={f'fixed_rate_formation.{ext}':sha(OUT/f'fixed_rate_formation.{ext}') for ext in ['png','pdf']},
scope='Display of already declared estimates and intervals; no new estimator, fit, history selection or resampling.')
(OUT/'PLOT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(source_sha256=EXPECTED,figures=receipt['figures'])))

