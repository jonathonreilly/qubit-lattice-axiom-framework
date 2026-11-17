"""Pre-registered long-sheet diagnostics. Run only after batch exit. GUIDE only."""
import importlib.util
import json
import os
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('prior_analysis',HERE.parent/'gap-descent-mc-astra/analyze.py')
prior=importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
from batch import gate,sha,utc,SCRATCH

WINDOWS=[(2,6),(4,8),(6,12),(8,16),(12,20),(16,24),(20,32),(24,40),(32,48)]
NAMES=['E1','E4','E8','E16','plaquette']

def diagnostics(xs,L):
    if max(x.var() for x in xs)<1e-18:
        return dict(status='constant',accepted=False)
    s=prior.statistics(xs,64);doub=prior.statistics(xs,128)
    taus=[];drift=[]
    for x in xs:
        mu=x.mean();axes=tuple(range(1,x.ndim));mean=x.mean(axis=axes)
        tau=[prior.tau_int(mean)]
        for t in (2,8,16):
            z=x-mu
            tau.append(prior.tau_int((z*np.roll(z,-t,axis=-1)).mean(axis=axes)))
        taus.append(max(tau))
        n=len(mean)//64
        bins=mean[:n*64].reshape(n,64).mean(axis=1)
        lo,hi=np.array_split(bins,2)
        error=np.hypot(lo.std(ddof=1)/np.sqrt(len(lo)),hi.std(ddof=1)/np.sqrt(len(hi)))
        drift.append(abs(lo.mean()-hi.mean())/error if error>0 else 0.)
    result={k:s[k] for k in ('C','error','mean','mean_z','corr2_z','blocks','bin')}
    result.update(tau=taus,drift_z=drift,effective=prior.effective(s,L),fits=[],accepted=False,status='OPEN')
    common=[]
    if max(taus)*8>64:common.append('bin_too_short')
    if sum(len(x) for x in xs)/(2*max(taus))<100:common.append('ESS_below_100')
    if s['blocks']<16 or doub['blocks']<16:common.append('too_few_bins')
    if max(s['mean_z'],s['corr2_z'])>4:common.append('hot_cold')
    if max(drift)>4:common.append('within_chain_drift')
    for lo,hi in WINDOWS:
        if hi>L//2:continue
        err=s['error'][lo:hi+1]
        snr=np.divide(s['C'][lo:hi+1],err,out=np.zeros_like(err),where=err>0)
        reasons=common.copy()
        if min(snr)<3:reasons.append('signal_below_3sigma')
        v=s['cov'][lo:hi+1,lo:hi+1]
        rank=np.linalg.matrix_rank(v,tol=max(np.linalg.eigvalsh(v)[-1],0)*1e-9)
        if rank<len(err):reasons.append('covariance_rank')
        vd=doub['cov'][lo:hi+1,lo:hi+1]
        rankd=np.linalg.matrix_rank(vd,tol=max(np.linalg.eigvalsh(vd)[-1],0)*1e-9)
        if rankd<len(err):reasons.append('double_bin_covariance_rank')
        f=prior.fit_one(s['C'],s['cov'],L,lo,hi)
        record=dict(range=[lo,hi],min_snr=float(min(snr)),rank=int(rank),accepted=False,reasons=reasons)
        if f is None:
            record['reasons'].append('fit_failed');result['fits'].append(record);continue
        record.update(f)
        if f['p']<.05:record['reasons'].append('chi2')
        if record['reasons']:
            result['fits'].append(record);continue
        full=prior.fit_jack(s,L,lo,hi)
        shift=prior.fit_jack(s,L,lo+1,hi)
        dbl=prior.fit_jack(doub,L,lo,hi)
        if any(x is None for x in (full,shift,dbl)):
            record['reasons'].append('jackknife_failed');result['fits'].append(record);continue
        record.update(full,shift=shift,double_bin=dbl)
        record['mL']=full['m']*L
        record['finite_volume_warning']=record['mL']<4
        for key,fit in [('mass',full),('shift',shift),('double_bin',dbl)]:
            if fit['error']>=.5*fit['m'] or fit['boundary_fraction']>.02 or fit['m']<=.002:
                record['reasons'].append(key+'_unresolved')
        if abs(full['m']-shift['m'])>2*np.hypot(full['error'],shift['error']):record['reasons'].append('window_shift')
        if abs(full['m']-dbl['m'])>2*np.hypot(full['error'],dbl['error']):record['reasons'].append('bin_shift')
        if full['error']<=0 or not 2/3<=dbl['error']/full['error']<=1.5:record['reasons'].append('bin_error_instability')
        record['accepted']=not record['reasons']
        result['fits'].append(record)
    good=[x for x in result['fits'] if x['accepted']]
    if good:
        result.update(accepted=True,status='GUIDE_candidate',chosen=good[-1])
    return result

def independent_sheet_control(stats,L,beta):
    f=lambda x:np.sqrt(x[1]/x[2]-1)/(2*np.sin(np.pi/L)) if x[1]>x[2]>0 else np.nan
    r=dict(xi=prior.scalar_jack(stats,f,64),double_bin=prior.scalar_jack(stats,f,128),
           energy=prior.scalar_jack(stats,lambda x:x[0],64),
           tau=[max(prior.tau_int(x[:,j]) for j in range(3)) for x in stats])
    split=[prior.scalar_jack([x],f,64) for x in stats]
    r['hot_cold_z']=abs(split[0]['value']-split[1]['value'])/np.hypot(split[0]['error'],split[1]['error'])
    r['separate']=split
    r['drift_z']=[]
    for x in stats:
        bins=x[:len(x)//64*64].reshape(-1,64,3).mean(axis=1)
        low,high=np.array_split(bins,2)
        err=np.hypot(low.std(axis=0,ddof=1)/np.sqrt(len(low)),high.std(axis=0,ddof=1)/np.sqrt(len(high)))
        r['drift_z'].append((abs(low.mean(axis=0)-high.mean(axis=0))/err).tolist())
    if L==128:
        ref={2.3:(18.95,.13),2.4:(25.39,.13),2.5:(33.14,.12)}[beta]
        r['reference']=ref
        r['z']=(r['xi']['value']-ref[0])/np.hypot(r['xi']['error'],ref[1])
        r['status']='FAILS' if abs(r['z'])>3 else 'GUIDE_compatible'
    else:r['status']='GUIDE_no_exact_size_benchmark'
    ratio=r['double_bin']['error']/r['xi']['error']
    if (max(r['tau'])*8>64 or r['hot_cold_z']>4 or
        max(max(z) for z in r['drift_z'])>4 or not 2/3<=ratio<=1.5 or
        sum(len(x) for x in stats)/(2*max(r['tau']))<100):r['status']='OPEN_sampling_gate'
    return r

def main():
    phase=sys.argv[1]
    done=json.loads((HERE/(phase+'_batch.json')).read_text())
    if not done['all_reaped']:raise RuntimeError('batch not reaped')
    gate()
    prior.selftest()
    plan=json.loads((HERE/(phase+'_plan.json')).read_text())['chains']
    groups={}
    for p in plan:
        key=(p['model'],p['L'],p['T'],p['beta'],p['coupling'])
        groups.setdefault(key,[]).append(p)
    summaries=[]
    for key,chains in groups.items():
        if len(chains)!=2:raise RuntimeError('need two starts')
        model,L,T,beta,k=key
        arrays=[];stats=[]
        for chain in chains:
            receipt=json.loads((HERE/(chain['tag']+'.json')).read_text())
            if receipt['exit_code']!=0 or not receipt['reaped']:raise RuntimeError('unreaped/failed chain')
            path=SCRATCH/(chain['tag']+'.f32')
            if sha(path)!=next(r['sha256'] for r in receipt['records'] if r['path']==str(path)):raise RuntimeError('hash mismatch')
            a=np.fromfile(path,dtype=np.float32).reshape(chain['samples'],2,5,L).astype(float)
            if not np.isfinite(a).all() or abs(a).max()>1.00001:raise RuntimeError('invalid observable')
            arrays.append(a)
            stats.append(np.loadtxt(SCRATCH/(chain['tag']+'.csv'),delimiter=',',skiprows=1))
        r=dict(model=model,L=L,T=T,beta=beta,coupling=k,channels={},chains=[c['tag'] for c in chains])
        for c,name in enumerate(chains[0].get('channels',NAMES)):
            for axis in ('pool',0,1):
                xs=[x[:,:,c,:] if axis=='pool' else x[:,axis,c,:] for x in arrays]
                r['channels'][f'{name}_{axis}']=diagnostics(xs,L)
        if (model=='gh' and k==-1) or (model!='gh' and k==0):r['spin_control']=independent_sheet_control(stats,L,beta)
        tag=chains[0]['tag'].rsplit('_c',1)[0]
        detail=SCRATCH/('analysis_'+tag+'.json')
        detail.write_text(json.dumps(prior.finite(r),indent=2)+'\n')
        summary={q:r[q] for q in ('model','L','T','beta','coupling','chains')}
        summary['channels']={name:{q:v[q] for q in ('status','accepted','chosen','tau','mean_z','corr2_z','drift_z') if q in v} for name,v in r['channels'].items()}
        if 'spin_control'in r:summary['spin_control']=r['spin_control']
        summary['detail']=dict(path=str(detail),bytes=detail.stat().st_size,sha256=sha(detail))
        summaries.append(prior.finite(summary))
        (HERE/(phase+'_summary.json')).write_text(json.dumps(summaries,indent=2)+'\n')
        primary='E8' if model=='gh' else 'E64' if model=='face' else 'plaquette'
        print(tag, 'primary',r['channels'][primary+'_pool']['status'],flush=True)
        prior.memory_gate()
    (HERE/(phase+'_analysis_receipt.json')).write_text(json.dumps(dict(ended=utc(),
        source_sha256=sha(Path(__file__)),shared_analysis_sha256=sha(HERE.parent/'gap-descent-mc-astra/analyze.py'),
        batch_sha256=sha(HERE/(phase+'_batch.json')),ensembles=len(summaries),
        nice=os.getpriority(os.PRIO_PROCESS,0)),indent=2)+'\n')

if __name__=='__main__':main()
