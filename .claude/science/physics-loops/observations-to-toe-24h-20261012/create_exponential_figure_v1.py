from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
E=P/'cosmology/direct_exponential_completion';O=P/'synthesis'
paths=[E/'evidence_v1/RESULTS.json',E/'REGULAR_LIMIT_RESULTS_v1.json',E/'OBSERVATION_RESULTS_v2.json']
pins=[dict(path=str(f),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in paths]
hist=json.loads(paths[0].read_text())['histories'];limit=json.loads(paths[1].read_text())['runs'][0]['rows']
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,1,figsize=(9.6,6.6),sharex=True,layout='constrained')
colors=['#c85a32','#387bb5','#2f8a73']
for h,color in zip([h for h in hist if h['case']['refined']],colors):
    k=h['case']['k'];L=np.array([r['L'] for r in h['rows']]);u=np.array([r['state'][0] for r in h['rows']]);H=np.array([r['Hratio'] for r in h['rows']])
    label=f'k = {k:g}'
    axs[0].plot(L,u,color=color,label=label,lw=1.7)
    axs[1].plot(L,(H*H-1)/k,color=color,label=label,lw=1.7)
L=np.array([r['L'] for r in limit]);axs[0].plot(L,[r['state'][0] for r in limit],color='#242933',ls='--',lw=1.5,label='regular limit')
axs[1].plot(L,[r['C_exp'] for r in limit],color='#242933',ls='--',lw=1.5,label='limit coefficient')
axs[0].set_ylabel('Extra scalar u');axs[1].set_ylabel(r'$(H_J^2/H_{\rm GR}^2-1)/k$')
axs[1].set_xlabel(r'Cooling parameter $L=\ln(T_{\mathrm{initial}}/T_\gamma)$')
for a in axs:a.axhline(0,color='#b5bdc6',lw=.7);a.grid(alpha=.17);a.set_xlim(0,24)
axs[0].legend(ncol=4,frameon=False,loc='upper center');axs[1].legend(ncol=4,frameon=False,loc='upper center')
fig.suptitle('New exponential candidate: full thermal evolution',fontsize=16)
axs[0].set_title('Fixed action and initial conditions; no fit to these curves',fontsize=10,color='#505964')
fig.savefig(O/'EXPONENTIAL_EVOLUTION_v1.png',dpi=180);fig.savefig(O/'EXPONENTIAL_EVOLUTION_v1.svg')
f=O/'EXPONENTIAL_EVOLUTION_v1.svg';f.write_text('\n'.join(line.rstrip() for line in f.read_text().splitlines())+'\n')
(O/'EXPONENTIAL_EVOLUTION_v1.json').write_text(json.dumps(dict(scope='Plot of stored personally computed histories and regular limit; no refit or new calculation of dynamics.',inputs=pins),indent=2)+'\n')
(O/'EXPONENTIAL_EVOLUTION_CAPTION_v1.md').write_text('''# New exponential candidate: thermal evolution

All curves use the new potential, fixed calibration and fixed initial state.
The upper panel shows the extra scalar evolving during the supplied plasma,
massive-neutrino and dust history. The lower panel divides the physical Hubble
correction by k so the regular weak limit is visible; the small-k curves
nearly coincide. Dotted curves are a separately integrated three-field
limiting system, not an old-action history. Hubble rates use the same H_v
normalization in numerator and denominator.

These are theoretical histories with internal numerical comparisons. The
gas approximation, masses, vacuum scale and initial conditions are supplied.
They do not establish an observed fit, global stability or a TOE. Numerical
agreement does not supply a rigorous physical-history error bound. Source
hashes are saved beside the figure; the detailed conditional theorem and
focused independent checks are in direct_exponential_completion.
''')
print('Saved exponential evolution figure and source pins.')
