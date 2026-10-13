#!/usr/bin/env python3
"""Plot a declared conditional diagnostic, not an observation likelihood."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


root = Path(__file__).resolve().parent
data = json.loads((root/'evidence_v1/RESULTS.json').read_text())
curve = data['figure_trace']
r = np.array([v['R_kpc_at_2p6Mpc'] for v in curve])
sigma = np.array([v['Sigma_HI_Msun_pc2'] for v in curve])
row = next(v for v in data['diagnostics'] if v['width_kpc'] == .18)
lo, hi = row['figure_interval_kpc']
grid = np.linspace(lo, hi, 200)
required = row['Sigma_endpoints_Msun_pc2'][0]*(grid/lo)**(-data['required_log_slope'])
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
fig, ax = plt.subplots(figsize=(9, 5.8))
fig.subplots_adjust(left=.12, right=.98, bottom=.29, top=.86)
ax.axvspan(lo, hi, color='#64748b', alpha=.1)
ax.plot(r, sigma, color='#b91c1c', linewidth=2.2, label='Published HI profile (figure trace)')
ax.plot(grid, required, '--', color='#0f172a', linewidth=2,
        label='If required pressure persists across the interval')
ax.axvline(data['selected_radius']['figure_kpc'], color='#64748b', linewidth=1, linestyle=':')
ax.set(xlim=(.58, 1.32), ylim=(.075, 4), yscale='log',
       xlabel='Radius at the figure distance of 2.6 Mpc (kpc)',
       ylabel=r'HI surface density ($M_\odot\,\mathrm{pc}^{-2}$)')
ax.set_title('HI profile and the required sustained pressure gradient', loc='left', pad=18, weight='bold', fontsize=12)
ax.text(.02, .80, 'UGC 7577 / DDO 125', transform=ax.transAxes, va='top', color='#334155')
ax.text(.02, .11, 'Illustrative dispersion: 8 km/s; constant gas height\n'
        'Nominal 180 pc interval shaded; no error model or raw cube',
        transform=ax.transAxes, color='#334155', fontsize=9)
ax.grid(which='major', color='#e2e8f0', linewidth=.7)
ax.legend(loc='lower left', bbox_to_anchor=(0, -.43), frameon=False, fontsize=10)
fig.text(.02, .035, 'Source: Lelli et al. 2012, Fig. 9. The pointwise certificate does not impose interval persistence.',
         fontsize=8.5, color='#475569')
out = root/'figures';out.mkdir(exist_ok=True)
for ext in ['png', 'svg']:
    fig.savefig(out/f'pressure_profile_diagnostic.{ext}', dpi=180)
print(out/'pressure_profile_diagnostic.png')
