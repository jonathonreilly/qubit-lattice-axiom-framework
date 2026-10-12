#!/usr/bin/env python3
"""Show fitted curves and response functions after actual field validation."""
import datetime as dt
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import direct_shared_response_fit as fit

OUT=fit.operator.OUT

def main():
    fit.operator.guard()
    output=OUT/'DIRECT_INVERSE_FIGURE.json'
    assert not output.exists()
    source=fit.operator.field.sha(__file__)
    files={name:OUT/name for name in ['shared_response_fits_v1.json','field_validation_v1.json','margin_candidate_v1.json','margin_field_validation_v1.json']}
    values={name:json.loads(path.read_text()) for name,path in files.items()}
    original=values['shared_response_fits_v1.json']
    validation=values['field_validation_v1.json']
    margin=values['margin_field_validation_v1.json']
    assert margin['passed']
    label='D_galaxies_external_solar'
    assert validation['candidate_passes'][label]
    assert validation['fits_sha256']==fit.operator.field.sha(files['shared_response_fits_v1.json'])
    assert margin['candidate_sha256']==fit.operator.field.sha(files['margin_candidate_v1.json'])
    response=next(row['best_sampled'] for row in original['cases'] if row['family']+'_'+row['constraints']==label)
    interior=values['margin_candidate_v1.json']
    fig,axes=plt.subplots(2,2,figsize=(11,8),layout='constrained')
    colors={'original':'#315cb4','interior':'#c65424'}
    for ax,training,base,follow in zip(axes.flat,fit.training_rows(),validation['rows'],margin['rows']):
        assert training['name']==base['name']==follow['name']
        radius=training['R']; observed=np.sqrt(training['A']*radius)
        lower=np.sqrt(training['low']*radius); upper=np.sqrt(training['high']*radius)
        original_velocity=np.sqrt(radius*np.array(base['candidate_results'][label]['refined_direct_force']))
        interior_velocity=np.sqrt(radius*np.array(follow['forces']['refined']))
        ax.fill_between(radius,lower,upper,color='#c8cdd2',alpha=.5,label='Declared velocity rectangle')
        ax.plot(radius,observed,'o',color='#292f35',ms=4,label='Processed observation')
        ax.plot(radius,np.sqrt(radius*training['g_N']),':',color='#6d757d',lw=1.5,label='Newtonian source')
        ax.plot(radius,original_velocity,color=colors['original'],lw=2,label='Original combined D fit')
        ax.plot(radius,interior_velocity,color=colors['interior'],lw=2,label='Interior D follow-up')
        ax.set_title(training['name']+' — fitted input',loc='left',fontweight='bold')
        ax.set(xlabel='Radius [kpc]',ylabel='Circular-speed readout [km/s]')
        ax.grid(alpha=.18)
    ax=axes.flat[3]
    acceleration=np.geomspace(1e-13,1e-8,1000)
    for item,name,color in [(response,'Original combined D fit',colors['original']),
                            (interior,'Interior D follow-up',colors['interior'])]:
        response_value=1+sum(weight*fit.operator.ramp(acceleration,lo,hi)
                   for weight,lo,hi in zip(item['weights'],fit.operator.KNOTS[:-1],fit.operator.KNOTS[1:]))
        ax.semilogx(acceleration,response_value,lw=2,color=color,label=name)
    ax.axvline(interior['external_newtonian_SI'],color='#505961',ls='--',lw=1,label='Fixed Newtonian external field')
    ax.set_title('One response used for disk and solar fields',loc='left',fontweight='bold')
    ax.set(xlabel='Newtonian field magnitude [m/s²]',ylabel='Response N(A)',ylim=(.94,2.7))
    ax.grid(alpha=.18)
    handles,labels=axes.flat[0].get_legend_handles_labels()
    fig.legend(handles,labels,loc='outside lower center',ncol=3,frameon=False,fontsize=9)
    fig.suptitle('Conditional inverse reconstruction: three fitted galaxies',fontsize=16,fontweight='bold')
    axes.flat[1].text(.03,.96,'Uncorrected pressure support remains a premise',transform=axes.flat[1].transAxes,va='top',fontsize=8)
    png=OUT/'DIRECT_INVERSE_FIGURE.png'; pdf=OUT/'DIRECT_INVERSE_FIGURE.pdf'
    assert not png.exists() and not pdf.exists()
    fig.savefig(png,dpi=170); fig.savefig(pdf); plt.close(fig)
    assert source==fit.operator.field.sha(__file__)
    output.write_text(json.dumps({'at':dt.datetime.now(dt.timezone.utc).isoformat(),
        'source_sha256':source,'inputs':{name:fit.operator.field.sha(path) for name,path in files.items()},
        'png_sha256':fit.operator.field.sha(png),'pdf_sha256':fit.operator.field.sha(pdf),
        'limits':'Fitted inputs and descriptive rectangles, not independent tests or confidence bands. Refined fields shown. Original candidate tiny rectangle violation retained in inverse_direct_results_v1.json.'},indent=2)+'\n')
    print(png)

if __name__=='__main__':
    main()
