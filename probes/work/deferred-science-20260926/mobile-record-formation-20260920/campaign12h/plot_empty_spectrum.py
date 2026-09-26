#!/usr/bin/env python3
"""Standalone scientific figure from preserved empty-start observations."""
from pathlib import Path
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
data = json.loads((HERE/'EMPTY_SPECTRUM_ANALYSIS.json').read_text())
cases = {row['case']:row for row in data['cases']}


def at_density(case):
    return next(row for row in case['rows'] if row.get('ensemble_density') == .9)


plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                     'pdf.fonttype':42,'svg.fonttype':'none'})
fig,axes = plt.subplots(2,2,figsize=(11,8),layout='constrained')
colors = ('#777777','#2676ba','#ce583a')
settings = ((0.,.1,'Immobile'),(1.,.1,'Motion / formation = 10'),
            (1.,.01,'Motion / formation = 100'))
for (mobility,eps,label),color in zip(settings,colors):
    name = f'L16_p12_mobility{mobility}_eps{eps}'
    raw = json.loads((HERE/'empty_spectrum'/f'{name}.json').read_text())
    means = np.array(raw['mean'],float); se = np.array(raw['standard_error'],float)
    tau = np.array(raw['taus'])
    axes[0,0].plot(tau,means[:,0],color=color,label=label)
    axes[0,0].fill_between(tau,means[:,0]-1.96*se[:,0],means[:,0]+1.96*se[:,0],color=color,alpha=.18)
    row = at_density(cases[name])
    k = np.array(row['wave_number_magnitude']); take = np.ones(len(k),dtype=bool)
    s = np.array(row['vector_structure_per_record']); interval = np.array(row['vector_structure_pointwise_95'])
    axes[0,1].plot(k[take],s[take],'.-',ms=4,lw=1.2,color=color,label=label)
    axes[0,1].fill_between(k[take],interval[0,take],interval[1,take],color=color,alpha=.16)
    r = np.array(row['spatial_separation']); take = r > 0
    c = np.array(row['vector_pair_correlation']); interval = np.array(row['vector_pair_correlation_pointwise_95'])
    axes[1,0].plot(r[take],c[take],'.-',ms=4,lw=1.2,color=color)
    axes[1,0].fill_between(r[take],interval[0,take],interval[1,take],color=color,alpha=.16)
axes[0,0].plot(tau,1-np.exp(-tau),':',color='#333333',lw=1,label='Exact uniform-weight control')
axes[0,0].set(xlabel=r'Formation time $\tau=6\epsilon t$',ylabel='Expected occupied fraction',ylim=(0,1.02),
              title='(a) Formation from an empty cube')
axes[0,0].legend(fontsize=8,loc='lower right',frameon=False)
axes[0,1].axhline(1,color='#777777',ls=':',lw=1)
axes[0,1].set(xlabel=r'Wave-number magnitude $|k|$ (lattice units)',ylabel=r'$S(k)/\langle N\rangle$',
              title='(b) Vector correlations at mean density 0.9')
axes[1,0].axhline(0,color='#777777',lw=.8)
axes[1,0].set(xlabel='Periodic separation (lattice spacings)',ylabel=r'$\langle m(x)\cdot m(x+r)\rangle$',
              title='(c) Spatial decay at the same mean density')
for p,color,offset in ((3,'#277d60',-.1),(12,'#ce583a',.1)):
    x=[];y=[];lower=[];upper=[]
    for side in (8,16):
        row=at_density(cases[f'L{side}_p{p}_mobility1.0_eps0.01'])['S0_per_record']
        x.append(side+offset);y.append(row['estimate'])
        lower.append(row['estimate']-row['bootstrap_95_percentile'][0])
        upper.append(row['bootstrap_95_percentile'][1]-row['estimate'])
    axes[1,1].errorbar(x,y,yerr=[lower,upper],fmt='o-',capsize=3,color=color,
                     label=f'Raw weights ({p}, 1, 2)')
axes[1,1].set(xticks=[8,16],xlim=(6,18),xlabel='Cube side length',ylabel=r'$S(0)/\langle N\rangle$',
              title='(d) Two volumes; no phase extrapolation')
axes[1,1].legend(frameon=False,fontsize=9)
fig.suptitle('Empty-start formation creates correlations while vacancy motion continues',fontsize=14)
fig.supxlabel('Finite supplied stochastic model. Panels a–c: side 16, raw weights (12,1,2), normalized to row sum six.\n'
              '128 trajectories/case; b–d: pointwise 95% trajectory-bootstrap intervals. Density interpolation error is separate.\n'
              'Panel d: motion / formation = 100. Correlations are not an established phase, massless field, or physical force.',fontsize=9)
out=HERE/'figures';out.mkdir(exist_ok=True)
for extension in ('png','pdf','svg'):
    fig.savefig(out/f'empty_start_correlations.{extension}',dpi=180)
svg = out/'empty_start_correlations.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
receipt={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'analysis_sha256':hashlib.sha256((HERE/'EMPTY_SPECTRUM_ANALYSIS.json').read_bytes()).hexdigest(),
         'matplotlib_version':matplotlib.__version__,
         'artifacts_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.glob('empty_start_correlations.*')}}
(out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
