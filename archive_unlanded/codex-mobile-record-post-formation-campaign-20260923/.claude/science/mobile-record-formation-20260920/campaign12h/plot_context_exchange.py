#!/usr/bin/env python3
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
data=HERE/'context_exchange_screen'
summary=json.loads((HERE/'CONTEXT_EXCHANGE_SCREEN_ANALYSIS.json').read_text())
records={c['case']:c for c in summary['cases']}
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                     'axes.grid':True,'grid.alpha':.18,'figure.facecolor':'white',
                     'savefig.facecolor':'white','axes.titlesize':11})
fig,axes=plt.subplots(2,2,figsize=(12,8.2),layout='constrained')
colors=['#77a7cf','#3278ad','#113f71']


def curve(ax,name,group,color,label):
    d=np.load(data/f'{name}_analysis.npz')
    x=d[f'{group}_theta'];y=d[f'{group}_density_mean'];lo,hi=d[f'{group}_density_ci']
    mask=x<=2*np.pi+1e-10
    ax.plot(x[mask],y[mask],color=color,label=label,lw=1.8)
    ax.fill_between(x[mask],lo[mask],hi[mask],color=color,alpha=.15,lw=0)


for L,color in zip([16,24,32],colors):
    curve(axes[0,0],f'context_minimal_L{L}','axis',color,f'L = {L}')
axes[0,0].set_title('Axial density oscillation strengthens with size')
for group,color,label in [('axis','#2166ac','Axis'),('face','#d47b21','Face diagonal'),
                          ('body','#549553','Body diagonal')]:
    curve(axes[0,1],'context_minimal_L32',group,color,label)
axes[0,1].set_title('Side 32: compare directions at the same wave phase')
for ax in axes[0]:
    ax.axhline(0,color='#4c5562',lw=.7)
    ax.set_xlim(0,2*np.pi);ax.set_ylim(-.75,1.2)
    ax.set_xlabel(r'Current-law phase $|k|t/\sqrt{6}$')
    ax.set_ylabel('Normalized density autocorrelation')
    ax.legend(frameon=False,fontsize=9)

for group,color,marker,label in [('axis','#2166ac','o','Axis'),
        ('face','#d47b21','s','Face diagonal'),('body','#549553','^','Body diagonal')]:
    xs=[];ys=[];lower=[];upper=[]
    for L in [16,24,32]:
        r=records[f'context_minimal_L{L}']['groups'][group];f=r['complex_fit']
        xs.append(r['wave_number']**2);ys.append(f['speed'])
        lo,hi=f['pointwise_bootstrap_parameter_intervals'][1]
        lower.append(f['speed']-lo);upper.append(hi-f['speed'])
    axes[1,0].errorbar(xs,ys,yerr=[lower,upper],fmt=marker+'-',color=color,
                     lw=1.1,capsize=3,ms=5,label=label)
axes[1,0].axhline(1/np.sqrt(6),color='#555',ls='--',lw=1,label=r'Current target $1/\sqrt{6}$')
axes[1,0].set_title('Fitted phase speeds approach the current-law target')
axes[1,0].set_xlabel(r'$|k|^2$ (lattice units)');axes[1,0].set_ylabel('Phenomenological phase speed')
axes[1,0].set_xlim(0,.49);axes[1,0].set_ylim(.28,.435)
axes[1,0].legend(frameon=False,fontsize=8,loc='lower left')

for name,color,label in [('context_minimal_L16','#2166ac','Context; small symmetric rate'),
                        ('context_constant_L16','#888888','Context; large symmetric rate'),
                        ('flat_symmetric_L16','#419d8a','Symmetric exchange control')]:
    curve(axes[1,1],name,'axis',color,label)
axes[1,1].axhline(0,color='#4c5562',lw=.7)
axes[1,1].set_xlim(0,2*np.pi);axes[1,1].set_ylim(-.4,1.2)
axes[1,1].set_title('Side 16 controls: damping matters')
axes[1,1].set_xlabel(r'Reference phase $|k|t/\sqrt{6}$')
axes[1,1].set_ylabel('Normalized density autocorrelation')
axes[1,1].legend(frameon=False,fontsize=8)
fig.suptitle('Immutable records with context-dependent exchanges\nFinite-lattice evidence for collective propagation',fontsize=15,fontweight='bold')
fig.supxlabel('256 independent trajectories per case; 95% pointwise whole-trajectory bootstrap intervals.\nSpeeds use first-half-period fits; fit-model error and the hydrodynamic limit remain open.',fontsize=9,color='#465466')
destination=HERE/'figures';destination.mkdir(exist_ok=True)
for extension in ['png','pdf']:
    fig.savefig(destination/f'context_exchange_first_screen.{extension}',dpi=180)
print(destination/'context_exchange_first_screen.png')
