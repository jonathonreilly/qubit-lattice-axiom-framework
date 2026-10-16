#!/usr/local/bin/python3
"""Plot frozen synthetic diagnostic output; no new experiment."""
import hashlib
import json
import pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

p=pathlib.Path(__file__).resolve().parent
src=p/'METRIC_READOUT_NUMERICS_v3.json';d=json.loads(src.read_text())
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(12,5.3))
fig.subplots_adjust(left=.08,right=.98,top=.83,bottom=.23,wspace=.30)
for name,label,color in [('trace','Four-column trace','#245e9c'),('scalar','Five-column scalar','#b84b22')]:
    axs[0].loglog([float(c['k0']) for c in d['rank_cases']],
                 [10**c[name]['mpmath_log10_condition'] for c in d['rank_cases']],
                 marker='o',color=color,label=label)
axs[0].set(xlabel='Base wave number k0 (constructed units)',ylabel='Normalized design condition number',
           title='Exact growing modes can be nearly dependent')
axs[0].legend(frameon=False);axs[0].grid(alpha=.2)
for du,color in [(.005,'#245e9c'),(.025,'#b84b22'),(.1,'#39836a')]:
    rows=[c for c in d['noise_cases'] if c['du']==du and c['sigma']==1e-8]
    axs[1].loglog([c['n'] for c in rows],[c['Puu_rms_error'] for c in rows],marker='o',color=color,label=f'time half-step {du}')
    axs[1].loglog([c['n'] for c in rows],[c['expected_Puu_noise_rms'] for c in rows],ls=':',color=color)
axs[1].set(xlabel='Number of radial samples (fixed range)',ylabel='RMS error in recovered second time derivative',
           title='Unregularized differences amplify record noise')
axs[1].set_xticks([65,129,257],['65','129','257']);axs[1].xaxis.set_minor_formatter(NullFormatter());axs[1].legend(frameon=False);axs[1].grid(alpha=.2)
fig.suptitle('Synthetic stress tests - no observational fit or survey forecast',fontsize=13)
fig.text(.56,.035,'Solid: one seeded noise realization. Dotted: stencil variance prediction.\nAdditive lensing-potential noise sigma=1e-8; no smoothing.',fontsize=9)
fig.savefig(p/'METRIC_READOUT_DIAGNOSTICS_v2.png',dpi=180,bbox_inches='tight')
out={'source':src.name,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'runner_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
     'plot_sha256':hashlib.sha256((p/'METRIC_READOUT_DIAGNOSTICS_v2.png').read_bytes()).hexdigest(),
     'matplotlib':matplotlib.__version__,'scope':'visualization of frozen synthetic results only'}
(p/'METRIC_READOUT_DIAGNOSTICS_MANIFEST_v2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
