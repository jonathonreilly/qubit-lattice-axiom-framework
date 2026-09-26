#!/usr/bin/env python3
"""Post-outcome comparison of frozen, unfitted winding-generator benchmarks."""
from pathlib import Path
import argparse, datetime, hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent

def ident(p):
    p=Path(p);return dict(path=str(p.resolve()),bytes=p.stat().st_size,
                         sha256=hashlib.sha256(p.read_bytes()).hexdigest())

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--analysis',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();assert not args.output.exists();args.output.mkdir(parents=True)
    frozen=HERE/'dimer_routed_finite_wavelength_checks/RESULTS.json'
    assert ident(frozen)['sha256']=='89bd6b739074ffd695e0883394339bb975248e1e9793510bee3b84bafb9aa556'
    theory=json.loads(frozen.read_text())
    for row in theory['sources']:assert ident(row['path'])==row
    primary=args.analysis/'RESULTS.json'
    assert ident(primary)['sha256']=='08aab30040e7b0c50c60486bf769f7c87247d8771f3f2315d577725fd4d60345'
    observed=json.loads(primary.read_text())
    predictions={(x['N'],x['axis']):x for x in theory['predictions']}
    rows=[];averages=[]
    for cell in observed['cells']:
        if cell['kind']!='winding':continue
        value=np.array(cell['by_mode']['mean']);se=np.array(cell['by_mode']['standard_error'])
        assert value.shape==se.shape==(5,3,4)
        pp=[]
        for axis in range(3):
            t=predictions[cell['N'],axis];assert t['times']==cell['times']
            prediction=np.array(t['projected_benchmark']);pp.append(prediction)
            rows.append(dict(N=cell['N'],axis=axis,histories=cell['histories'],times=cell['times'],
                             projected_benchmark=prediction.tolist(),observed_mean=value[:,axis].tolist(),
                             observed_standard_error=se[:,axis].tolist(),
                             difference=(value[:,axis]-prediction).tolist()))
        average=np.mean(pp,axis=0)
        averages.append(dict(N=cell['N'],histories=cell['histories'],projected_benchmark=average.tolist(),
                             observed=cell['mode_average'],
                             difference=(np.array(cell['mode_average']['mean'])-average).tolist()))
    result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                comparison_source=ident(__file__),frozen_projection=ident(frozen),original_analysis=ident(primary),
                by_axis=rows,mode_average=averages,
                scope='Post-outcome comparison with no parameter fitting. Per-axis errors are original whole-history standard errors. The projected exponential is a closure benchmark, not an exact finite-time law.')
    (args.output/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    colors={16:'#aeb3bb',32:'#8395ad',64:'#477eaf',128:'#074775'}
    fig,axes=plt.subplots(2,3,figsize=(14.6,8.2),sharex=True,sharey='row')
    for axis in range(3):
        for panel,metric in enumerate((0,2)):
            ax=axes[panel,axis]
            for row in rows:
                if row['axis']!=axis:continue
                mu=np.array(row['observed_mean'])[:,metric]
                se=np.array(row['observed_standard_error'])[:,metric]
                target=np.array(row['projected_benchmark'])[:,metric]
                ax.plot(row['times'],target,'--',lw=1.6,color=colors[row['N']])
                ax.errorbar(row['times'],mu,yerr=se,fmt='o',ms=4,capsize=2,color=colors[row['N']],
                            label=f"N={row['N']}")
            dense=np.linspace(0,1.75,201)
            ax.plot(dense,np.zeros_like(dense) if metric==0 else np.sin(4*np.pi*dense/7),
                    ':',color='#bd492c',lw=1.8)
            ax.grid(alpha=.17);ax.spines[['top','right']].set_visible(False)
            if panel==0:ax.set_title(['x mode, parallel to winding','y mode','z mode'][axis],fontsize=11)
            if axis==0:ax.set_ylabel(['Mean-square propagation error','Signed E–B cross covariance'][panel])
            if panel==1:
                ax.set_xlabel('Macroscopic time t')
                ax.set_xticks([0,7/16,7/8,21/16,7/4],['0','7/16','7/8','21/16','7/4'])
            ax.set_ylim((-.08,2.3) if panel==0 else (-.15,1.18))
    handles,labels=axes[0,0].get_legend_handles_labels()
    fig.legend(handles,labels,loc='upper center',bbox_to_anchor=(.5,.91),ncol=4,frameon=False)
    fig.suptitle('The winding geometry predicts strong finite-size directional damping',fontsize=16,y=.99)
    fig.text(.5,.943,'Points ± 1 standard error: simulation   •   Dashed: projected-generator benchmark   •   Dotted red: Euler target',
             ha='center',fontsize=10)
    fig.text(.5,.018,'No fitted parameters. The exact initial generator projection does not close at finite time for γ=1.\n'
             'This comparison was specified after the original mode-averaged results; it covers only the fixed winding matching.',
             ha='center',fontsize=9,color='#444444')
    fig.subplots_adjust(top=.81,bottom=.1,left=.065,right=.985,hspace=.19,wspace=.14)
    for suffix in ('png','pdf'):fig.savefig(args.output/('WINDING_FINITE_WAVELENGTH_COMPARISON.'+suffix),dpi=180)
    plt.close(fig)
    receipt=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source=ident(__file__),
                 inputs=[ident(frozen),ident(primary)],
                 outputs=[ident(args.output/x) for x in ['RESULTS.json','WINDING_FINITE_WAVELENGTH_COMPARISON.png','WINDING_FINITE_WAVELENGTH_COMPARISON.pdf']],
                 visual_inspection='Pending root image inspection.')
    (args.output/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'mode_average_quarter':[{'N':x['N'],'benchmark':x['projected_benchmark'][2],
          'observed':x['observed']['mean'][2]} for x in averages],'receipt':ident(args.output/'RECEIPT.json')},indent=2))

if __name__=='__main__':main()
