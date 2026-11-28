"""Render factual tables and diagnostic figures from the saved analyses."""
import csv
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from analyze import memory_gate
HERE=Path(__file__).resolve().parent
summary=json.loads((HERE/'summary.json').read_text())
lookup={(x['L'],x['beta'],str(x['mult'])):x for x in summary}
def fmt(x,e=None):
    if x is None:return 'OPEN'
    return f'{x:.5g}' if e is None else f'{x:.5g} ± {e:.2g}'
lines=['# Numerical tables — GUIDE only','',
    'These are minima over accepted candidate fits in the measured basis.',
    'Errors condition on the selected observable and window. They exclude systematics.','',
    '| beta | beta_L/beta | L | measured minimum | observable / direction | fit t | difference from face | z |',
    '|---|---|---|---|---|---|---|---|']
comparisons=[]
for beta in (2.3,2.4,2.5):
    for mult in ('1','2','4','8','face'):
        for L in (8,12):
            row=lookup.get((L,beta,mult));facerow=lookup.get((L,beta,'face'))
            if row is None:continue
            f=row['minimum'];face=facerow['minimum'] if facerow else None
            delta=error=z=None
            if f and face and mult!='face':
                delta=f['m']-face['m'];error=float(np.hypot(f['error'],face['error']));z=delta/error
                comparisons.append(dict(beta=beta,mult=mult,L=L,delta=delta,error=error,z=z,finite=f,face=face))
            lines.append(f"| {beta} | {mult} | {L} | {fmt(f['m'],f['error']) if f else 'OPEN'} | {f['channel'] if f else 'none accepted'} | {str(f['range']) if f else '—'} | {fmt(delta,error) if delta is not None else '—'} | {fmt(z) if z is not None else '—'} |")
lines+=['','## Directional minima','','| beta | beta_L/beta | L | axis | measured rate | observable | fit t | mL < 4 |','|---|---|---|---|---|---|---|---|']
for r in summary:
    for axis,f in r.get('direction_minima',{}).items():
        lines.append(f"| {r['beta']} | {r['mult']} | {r['L']} | {axis} | {fmt(f['m'],f['error']) if f else 'OPEN'} | {f['channel'] if f else 'none accepted'} | {f['range'] if f else '—'} | {f['thermal_warning'] if f else '—'} |")
lines+=['','## Autocorrelations and chain agreement','','Tau is in saved-measurement units (four HB+OR cycles per unit).',
    'Maxima range over the measured local means and t=2 correlation estimators.','',
    '| beta | beta_L/beta | L | max tau_int | largest cold/hot z | accepted channels |',
    '|---|---|---|---|---|---|']
for r in summary:
    lines.append(f"| {r['beta']} | {r['mult']} | {r['L']} | {fmt(r['tau_max'])} | {fmt(r['hot_cold_z_max'])} | {r['accepted_channel_count']} |")
lines+=['','## Isotropic controls','','Fixed scalar channel: eight APE steps, spatial rectangles.',
    'Each direction retains its own fit. No minimum over directions is taken for this control.','',
    '| beta | L | axis | scalar rate | range | comparator | difference / combined error |',
    '|---|---|---|---|---|---|---|']
for beta in (2.4,2.5):
    for L in (8,12,16):
        p=HERE/f'analysis_L{L}_b{beta:.1f}_1.json'
        if not p.exists():continue
        d=json.loads(p.read_text())
        for axis in (0,2):
            c=d['channels'][f'a{axis}_s8_scalar_R'];f=c.get('chosen')
            ref,err=(.953,.019) if beta==2.4 else (.660,.022)
            z=(f['m']-ref)/np.hypot(f['error'],err) if f else None
            lines.append(f"| {beta} | {L} | {axis} | {fmt(f['m'],f['error']) if f else 'OPEN'} | {f['range'] if f else '—'} | {ref} ± {err} ({12 if beta==2.4 else 16}^4) | {fmt(z)} |")
lines+=['','## Winding-loop controls','','All accepted winding channels are shown; OPEN means no accepted window.',
    'The conversion uses only the leading string formula; it is not a controlled long-string limit.','',
    '| beta | L | axis / winding index | E | fit t | sqrt(sigma) proxy |',
    '|---|---|---|---|---|---|']
for beta in (2.4,2.5):
    for L in (8,12,16):
        p=HERE/f'analysis_L{L}_b{beta:.1f}_1.json'
        if not p.exists():continue
        d=json.loads(p.read_text())
        for key,c in d.get('torelon',{}).items():
            f=c.get('chosen')
            sig=np.sqrt((f['m']+np.pi/(3*L))/L) if f else None
            err=f['error']/(2*L*sig) if f else None
            lines.append(f"| {beta} | {L} | {key} | {fmt(f['m'],f['error']) if f else 'OPEN'} | {f['range'] if f else '—'} | {fmt(sig,err) if sig else 'OPEN'} |")
o4=json.loads((HERE/'o4_summary.json').read_text()) if (HERE/'o4_summary.json').exists() else []
lines+=['','## O(4) control, 128^2','','| beta | xi_2nd | published xi_2nd | z | energy per bond | max tau | cold/hot xi z |','|---|---|---|---|---|---|---|']
for r in o4:
    lines.append(f"| {r['beta']} | {fmt(r['xi2']['value'],r['xi2']['error'])} | {fmt(*r['reference_xi'])} | {fmt(r['xi_z'])} | {fmt(r['energy']['value'],r['energy']['error'])} | {fmt(max(r['tau_measurements']))} | {fmt(r['hot_cold_z'])} |")
anchors=json.loads((HERE/'anchor_comparison.json').read_text()) if (HERE/'anchor_comparison.json').exists() else []
lines+=['','## Matched-size decoupled-sheet control','','| beta | L | max point-correlator difference / combined error | max standalone tau | max embedded tau |','|---|---|---|---|---|']
for r in anchors:
    lines.append(f"| {r['beta']} | {r['L']} | {fmt(max(abs(z) for z in r['z']))} | {fmt(max(r['standalone_tau']))} | {fmt(max(r['face_tau']))} |")
(HERE/'tables.md').write_text('\n'.join(lines)+'\n')
(HERE/'comparisons.json').write_text(json.dumps(comparisons,indent=2)+'\n')

# Full channel tables, including failed fits and non-finite effective masses.
with (HERE/'fit_inventory.csv').open('w',newline='') as f,(HERE/'effective_masses.csv').open('w',newline='') as g:
    w=csv.writer(f);v=csv.writer(g)
    w.writerow(['L','beta','mult','channel','lo','hi','mass','se','chi2','dof','p','accepted','reasons'])
    v.writerow(['L','beta','mult','channel','t','mass','se','valid_jack_fraction'])
    for r in summary:
        d=json.loads((HERE/f"analysis_L{r['L']}_b{r['beta']:.1f}_{r['mult']}.json").read_text())
        for key,c in d['channels'].items():
            for fit in c.get('fits',[]):
                w.writerow([r['L'],r['beta'],r['mult'],key,*fit['range'],fit['m'],fit.get('error'),fit['chi2'],fit['dof'],fit['p'],fit.get('accepted',False),';'.join(fit.get('reasons',[fit.get('reason','')]))])
            for e in c.get('effective',[]):v.writerow([r['L'],r['beta'],r['mult'],key,e['t'],e['m'],e['error'],e['valid_jack_fraction']])

for beta in (2.3,2.4,2.5):
    fig,axs=plt.subplots(2,5,figsize=(17,6),constrained_layout=True)
    for i,L in enumerate((8,12)):
        for j,mult in enumerate(('1','2','4','8','face')):
            ax=axs[i,j];p=HERE/f'analysis_L{L}_b{beta:.1f}_{mult}.json'
            if not p.exists():ax.text(.1,.5,'not run',transform=ax.transAxes);continue
            d=json.loads(p.read_text());m=d['minimum'];key=m['channel'] if m else 'a0_s8_scalar_R';c=d['channels'][key]
            e=[x for x in c.get('effective',[]) if x['m'] is not None and x['error'] is not None]
            if e:ax.errorbar([x['t'] for x in e],[x['m'] for x in e],yerr=[x['error'] for x in e],fmt='o',capsize=2,ms=3,color='#176b87')
            if m:
                lo,hi=m['range'];ax.hlines(m['m'],lo,hi,color='#b54921');ax.fill_between([lo,hi],m['m']-m['error'],m['m']+m['error'],alpha=.18,color='#b54921')
            ax.set_title(f'L={L}, beta_L/beta={mult}\n{key}'+('' if m else '\nOPEN'),fontsize=9)
            ax.set_xlim(.5,L/2+.5);ax.set_ylim(-.1,3);ax.grid(alpha=.2);ax.set_xlabel('separation t')
            if j==0:ax.set_ylabel('effective mass')
    fig.suptitle(f'GUIDE: beta={beta}; selected candidate or fixed scalar fallback. Band shows fit range; no mass gap claim.',fontsize=12)
    fig.savefig(HERE/f'plateaus_beta{beta:.1f}.png',dpi=140);plt.close(fig)
    memory_gate()
print('Wrote tables, all-channel inventories, comparisons, and three plateau figures.')
