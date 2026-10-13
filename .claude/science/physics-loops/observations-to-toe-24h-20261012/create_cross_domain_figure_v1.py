#!/usr/bin/env python3
"""Display existing checked comparisons, with no new fit or acceptance rule."""
from pathlib import Path
import datetime, hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
OUT=HERE/'synthesis'
OUT.mkdir(exist_ok=True)
sources={
    'SN':HERE/'cosmology/direct_history_distance_comparison/evidence_v2/RESULTS.json',
    'BAO':HERE/'cosmology/direct_bao_distance_comparison/evidence_v2/RESULTS.json',
    'PPN':HERE/'cosmology/direct_actual_background_weak_field/evidence_v1/RESULTS.json',
    'PPN_qualification':HERE/'cosmology/direct_actual_background_weak_field/READOUT_PRECISION_QUALIFICATION_v1.md',
}
pins={k:dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for k,p in sources.items()}
sn=json.loads(sources['SN'].read_text());ba=json.loads(sources['BAO'].read_text());pp=json.loads(sources['PPN'].read_text())
reference=next(r for r in ba['models'] if r['case']=='supplied_LCDM_0.3')
rows=[]
for row in sn['models']:
    name=row['case'];b=next(r for r in ba['models'] if r['case']==name);p=next(r for r in pp['rows'] if r['case']==name)
    rows.append(dict(case=name,SN_transfer_Q=row['conditional_transfer_chi2'],
                     SN_delta_Q=row['conditional_transfer_chi2']-sn['reference']['conditional_transfer_chi2'],
                     BAO_transfer_Q=b['transfer_chi2'],BAO_delta_Q=b['transfer_chi2']-reference['transfer_chi2'],
                     conditional_delta_gamma=float(p['actual']['delta_gamma']),
                     Cassini_separate_intervals=[dict(error_multiple=x['reported_error_multiple'],inside=x['separate_intervals']['Cassini']['inside']) for x in p['separate_working_rectangles']],
                     independently_completed_full_path=name=='equal_k0.01'))
result=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_inputs=pins,
            scope='Existing exposed comparisons only. Delta Q relative to supplied flat Omega_m=.3 shape; separate low-redshift calibrations. No joint score, significance, model ranking claim or acceptance decision.',
            SN_reference_Q=sn['reference']['conditional_transfer_chi2'],BAO_reference_Q=reference['transfer_chi2'],rows=rows)
(OUT/'CROSS_DOMAIN_v1.json').write_text(json.dumps(result,indent=2)+'\n')
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'font.family':'DejaVu Sans'})
fig,axes=plt.subplots(1,3,figsize=(13.6,5.4),sharey=True,gridspec_kw={'width_ratios':[1,1,1.45]})
y=np.arange(len(rows));colors=['#275d9a','#db8734','#275d9a','#db8734','#275d9a','#db8734']
labels=['split  k = 0.01','equal  k = 0.01','split  k = 10⁻⁵','equal  k = 10⁻⁵','split  k = 10⁻⁶','equal  k = 10⁻⁶']
for ax,key,title in zip(axes[:2],['SN_delta_Q','BAO_delta_Q'],['Supernova transfer','BAO transfer']):
    vals=[r[key] for r in rows];ax.barh(y,vals,color=colors,height=.58,alpha=.88);ax.axvline(0,color='#555555',lw=.8)
    ax.set_title(title,pad=14);ax.set_xlabel('ΔQ versus supplied reference');ax.grid(axis='x',alpha=.17);ax.set_axisbelow(True)
    for yy,v in zip(y,vals):ax.text(v+(.03 if v>=0 else -.03),yy,f'{v:+.3f}',va='center',ha='left' if v>=0 else 'right',fontsize=9)
axes[0].set_xlim(-1.55,.12);axes[1].set_xlim(-.92,.38)
ax=axes[2];ax.axvspan(-2.5e-5,6.7e-5,color='#dce8f3',label='reported ±2 error interval');ax.axvspan(-2e-6,4.4e-5,color='#aac8e2',label='reported ±1 error interval')
ax.scatter([r['conditional_delta_gamma'] for r in rows],y,c=colors,s=48,zorder=3)
ax.set_xscale('symlog',linthresh=1e-6,linscale=1);ax.set_xlim(-.08,.00012);ax.set_title('Conditional Cassini readout',pad=14);ax.set_xlabel('γ − 1  (symmetric log scale)');ax.grid(axis='x',alpha=.17);ax.legend(loc='upper left',bbox_to_anchor=(0,-.17),frameon=False,fontsize=8)
axes[0].set_yticks(y,labels);axes[0].invert_yaxis()
fig.suptitle('One fixed candidate family across distance and local-gravity comparisons',fontsize=15,x=.06,ha='left',y=.98)
fig.text(.06,.035,'Distance shapes are exposed; calibrations are separate. Cassini uses a light weak-body/environment-matching assumption.\nOnly equal k = 0.01 has an independent complete trajectory; weak-case refinements remain unfinished. No joint acceptance is claimed.',fontsize=9,color='#444444')
fig.subplots_adjust(left=.15,right=.985,top=.82,bottom=.27,wspace=.24)
fig.savefig(OUT/'CROSS_DOMAIN_v1.png',dpi=180);fig.savefig(OUT/'CROSS_DOMAIN_v1.svg');plt.close(fig)
assert all(hashlib.sha256(Path(v['path']).read_bytes()).hexdigest()==v['sha256'] for v in pins.values())
(OUT/'CROSS_DOMAIN_CAPTION_v1.md').write_text('''# Fixed-history cross-domain comparison

Bars show differences in the already checked conditional transfer quadratics,
relative to the supplied flat Omega_m=.3 reference. They are descriptive;
neither panel supplies a joint likelihood, significance or model-selection
decision. Supernovae use405 low-redshift calibration rows and953 exposed
transfer rows; BAO uses one BGS calibration row and12 transfer entries, with
the full released covariance and calibration uncertainty. The BAO ruler
amplitude is calibrated rather than predicted. Published table/release
discrepancies are retained in the BAO source record.

The final panel uses each actual stored late scalar background, not the
initial u=0 point. It displays the conditional long-range weak-body PPN
readout and the separate historical Cassini error intervals, not an apparatus
likelihood. The weak split k=1e-6 point lies only about2e-12 above the lower
one-error boundary; no history uncertainty bound certifies that classification.
No inference is made here from the representation-sensitive tiny G-drift or
eta values. Only equal k=.01 has an independent complete trajectory; its
Cassini point misses even the two-error interval under the supplied bridge.

All plotted numbers come directly from source-bound stored results. The figure
adds no fit, numerical trajectory or theory assumption. CROSS_DOMAIN_v1.json
contains the exact figure rows and their source hashes.
''')
print(json.dumps(dict(rows=rows,outputs=[str(OUT/'CROSS_DOMAIN_v1.png'),str(OUT/'CROSS_DOMAIN_v1.svg')]),indent=2))
