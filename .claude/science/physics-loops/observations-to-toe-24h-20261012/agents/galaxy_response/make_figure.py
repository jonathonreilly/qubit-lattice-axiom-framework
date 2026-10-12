#!/usr/bin/env python3
"""Plot every primary test galaxy in frozen name order, no selection by fit."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from galaxy_forward import OUT,guard

guard();results=json.loads((OUT/'comparison_results.json').read_text())['results']
chosen={r['model']:r for r in results if r['dataset']=='forward64' and not r['fixed_U']}
curves={m:{g['name']:g for g in r['test']['per_galaxy']} for m,r in chosen.items()}
names=list(curves['N']);fig,axes=plt.subplots(5,4,figsize=(13,13),constrained_layout=True)
for ax,name in zip(axes.flat,names):
    n=curves['N'][name];nl=curves['NL'][name]
    ax.plot(n['R_kpc'],n['observed_km_s'],'o',ms=3,color='black',label='SPARC processed curve')
    ax.plot(n['R_kpc'],n['predicted_km_s'],color='#236aa4',lw=1.5,label='Newton = positive linear fit')
    ax.plot(nl['R_kpc'],nl['predicted_km_s'],color='#c34b27',lw=1.5,label='Nonlinear circular response')
    ax.set_title(name,fontsize=10);ax.set_xlabel('Radius [kpc]',fontsize=8);ax.set_ylabel('Speed [km/s]',fontsize=8)
    ax.tick_params(labelsize=8);ax.grid(alpha=.2)
last=axes.flat[-1];last.axis('off');handles,labels=axes.flat[0].get_legend_handles_labels();last.legend(handles,labels,loc='upper left',frameon=False,fontsize=9)
last.text(.02,.5,'19 whole-galaxy test objects\nGlobal parameters trained on 84 others\n\nN/L: U=1; all range weights=0\nNL: U=0.5605; a0=7.658e-11 m/s²\n\nCentral D and i; no per-galaxy fit\nModel-development holdout\nProcessed curves, not a raw likelihood',transform=last.transAxes,fontsize=9,va='top')
fig.suptitle('Frozen SPARC disk-response comparison: all primary test galaxies',fontsize=15)
fig.savefig(OUT/'galaxy_test_predictions.png',dpi=160)
fig.savefig(OUT/'galaxy_test_predictions.pdf')
print(OUT/'galaxy_test_predictions.png')
