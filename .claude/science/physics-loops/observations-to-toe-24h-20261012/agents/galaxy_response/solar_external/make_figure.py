"""A source-bound prediction plot, with statistical and model boxes distinguished."""
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import solar_quadrupole as q
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

q.checkpoint()
d=json.loads((q.OUT/'physical_comparison_results.json').read_text())
raw=d['parameter_box_rows']
gvals=sorted({r['g_physical'] for r in raw})
g=np.array(gvals)*1e10
lo=[];hi=[]
for gv in gvals:
    values=[r['Q2_s_minus2']*1e27 for r in raw if r['g_physical']==gv]
    lo.append(min(values));hi.append(max(values))
primary_s=[q.prediction(q.A0_PRIMARY,gv)['Q2_s_m2']*1e27 for gv in gvals]
primary_d=[q.prediction(q.A0_PRIMARY,gv,47)['Q2_s_m2']*1e27 for gv in gvals]
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':160})
fig,ax=plt.subplots(figsize=(7.4,5.0))
ax.axhspan(-2.0,5.2,color='#707070',alpha=.16,label='Park 2026: central ± 2 quoted standard errors')
ax.axhline(1.6,color='#505050',lw=1.2)
ax.fill_between(g,lo,hi,color='#3683ad',alpha=.2,label='Sampled model box: both field conversions')
ax.plot(g,primary_s,color='#183f5d',lw=2,label='Primary galaxy scale; spherical conversion')
ax.plot(g,primary_d,color='#a05616',ls='--',lw=1.8,label='Primary scale; disk approximation, Σ=47')
ax.axvline(2.32,color='#555555',ls=':',lw=1)
ax.set(xlim=(2.00,2.64),ylim=(-3,38),xlabel=r'Physical external acceleration $g_e$ ($10^{-10}$ m s$^{-2}$)',ylabel=r'Predicted $Q_2$ ($10^{-27}$ s$^{-2}$)')
ax.set_title('Fixed exponential response with a supplied QUMOND completion',loc='left',fontsize=12,pad=12)
ax.legend(loc='center left',bbox_to_anchor=(.015,.35),fontsize=8.8,frameon=False)
ax.text(.015,.94,'No Solar fit; provisional transfer of algebraic galaxy calibration',transform=ax.transAxes,fontsize=9,color='#333333',va='top')
fig.subplots_adjust(left=.11,right=.98,bottom=.15,top=.89)
for ext in ['png','pdf']:
    fig.savefig(q.OUT/f'solar_quadrupole_comparison.{ext}')
print(q.checkpoint())
