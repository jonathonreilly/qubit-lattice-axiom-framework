#!/usr/bin/env python3
"""Plots preserved simulation analyses and exact response data without refits."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,
                     'axes.spines.right':False,'axes.grid':True,'grid.alpha':.2,'figure.dpi':140})
colors={16:'#bb7040',24:'#bb7040',32:'#4383ae',48:'#237f68',64:'#4d436d'}
deps=[]
def read(rel):
 p=HERE/rel;deps.append(dict(path=rel,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 return np.load(p)
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight')
 plt.close(fig)
fig,axs=plt.subplots(2,3,figsize=(12.2,6.6),sharex=True,sharey='row')
for col,(tag,j) in enumerate([('00',0),('05',.5),('09',.9)]):
 for side in (16,32,48):
  d=read(f'admissibility_wave_screen/native_j{tag}_L{side}_continuum_analysis.npz')
  time=d['times']
  for row,(field,part,key) in enumerate([(0,'real','real_interval'),(1,'imag','imag_interval')]):
   ax=axs[row,col];mean=getattr(d['mean'][:,1,field],part);ci=d[key][:,:,1,field]
   ax.plot(time,mean,color=colors[side],lw=1.6,label=f'L={side}')
   ax.fill_between(time,*ci,color=colors[side],alpha=.17,lw=0)
   if side==48:ax.plot(time,getattr(d['target'][:,1,field],part),color='#282b31',ls='--',lw=1.6,label='Euler target (unfitted)')
   ax.axhline(0,color='#777777',lw=.55);ax.set_xlim(time[0],time[-1])
 axs[0,col].set_title(f'Neighbor coupling j={j:g}',fontweight='bold')
 axs[1,col].set_xlabel('Macroscopic time')
axs[0,0].set_ylabel(r'Re density mode $\hat\rho_1$')
axs[1,0].set_ylabel(r'Im vector mode $\hat g_{x,1}$')
handles,labels=axs[0,0].get_legend_handles_labels()
fig.legend(handles,labels,ncol=4,loc='lower center',bbox_to_anchor=(.5,.015),frameon=False)
fig.suptitle('Record formation with immutable exchange: finite lattices remain strongly damped',fontsize=14,x=.52,y=.98)
fig.text(.5,-.018,'Fixed nonlinear six-field PDE targets. Shading: pointwise 95% whole-path bootstrap intervals; no finite-size correction fitted.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.07,1,.94));save(fig,'native_formation_wave_comparison')

fig,axs=plt.subplots(1,3,figsize=(12.2,3.9),sharey=True)
for col,group in enumerate(('axis','face','body')):
 for side in (24,48):
  d=read(f'axis_balanced_screen/balanced_growth_L{side}_growing_analysis.npz')
  time=d['macro_times'];mean=d[f'{group}_density_mean'].real;ci=d[f'{group}_density_ci_real']
  axs[col].plot(time,mean,color=colors[side],label=f'L={side}',lw=1.6)
  axs[col].fill_between(time,*ci,color=colors[side],alpha=.17,lw=0)
  if side==48:axs[col].plot(time,d[f'{group}_density_theory'].real,'--',color='#282b31',label='Gaussian continuum target',lw=1.6)
 axs[col].axhline(0,color='#777777',lw=.55);axs[col].set_xlabel('Macroscopic time');axs[col].set_title(group.capitalize()+' Fourier directions')
axs[0].set_ylabel('Normalized two-time density covariance')
fig.suptitle('Uniform formation: covariance oscillations strengthen with lattice size',fontsize=14,y=1.01)
handles,labels=axs[0].get_legend_handles_labels();fig.legend(handles,labels,ncol=3,loc='lower center',bbox_to_anchor=(.5,-.03),frameon=False)
fig.text(.5,-.065,'Unfitted full six-field response, including birth noise. Pointwise 95% bootstrap intervals; no numerical convergence claim.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.055,1,.98));save(fig,'uniform_formation_covariance_comparison')

fig,axs=plt.subplots(1,2,figsize=(10.5,4.2))
sides=(4,8,16,24,32,48,64);final=[]
for idx,side in enumerate(sides):
 d=read(f'native_formation_centering/three_dimensional_L{side}.npz')
 color=plt.cm.viridis(.1+.8*idx/(len(sides)-1))
 axs[0].plot(d['times'],d['scaled_density_coefficient'],color=color,label=f'N={side}',lw=1.4)
 final.append(float(d['scaled_density_coefficient'][-1]))
 if side==64:
  target=d['target_scaled_density_coefficient'][-1]
  axs[0].plot(d['times'],d['target_scaled_density_coefficient'],'--',color='#222222',lw=2,label='Green-function limit')
axs[0].set_xlabel('Macroscopic time');axs[0].set_ylabel('N × third density Taylor coefficient')
axs[0].legend(ncol=2,fontsize=8,frameon=False)
axs[1].plot(sides,final,'o-',color='#4383ae',lw=1.6)
axs[1].axhline(target,ls='--',color='#222222',label='Unfitted limit at t=1')
axs[1].set_xlabel('Torus side N');axs[1].set_ylabel('N × third coefficient at t=1');axs[1].legend(frameon=False,fontsize=9)
fig.suptitle('Correlation-induced centering: a controlled perturbative test case',fontsize=14,y=1.01)
fig.text(.5,-.04,'Symmetric stirring, β=0.2, κ=0.75, initial vacancy=0.6. Exact response equations solved numerically; no fixed-coupling CLT claim.',ha='center',fontsize=9)
fig.tight_layout();save(fig,'native_formation_third_order_centering')
manifest=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies=deps,
 figures=[dict(path=str(p.relative_to(HERE)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(OUT.glob('*')) if p.stem in {'native_formation_wave_comparison','uniform_formation_covariance_comparison','native_formation_third_order_centering'}])
(OUT/'NATIVE_FORMATION_FIGURE_PROVENANCE.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Wrote three PNG/PDF figures from',len(deps),'source reads')
