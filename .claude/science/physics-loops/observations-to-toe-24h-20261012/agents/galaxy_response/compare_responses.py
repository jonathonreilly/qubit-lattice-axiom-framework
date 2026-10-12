#!/usr/bin/env python3
"""Train-only global fits; fixed held-out galaxy evaluation, no raw likelihood."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
import datetime, hashlib, json, time
import numpy as np
from scipy.constants import parsec
from scipy.optimize import minimize, minimize_scalar
from galaxy_forward import OUT, LAMBDAS, guard, digest

ACC=1e6/(1000*parsec)  # (km/s)^2/kpc to m/s^2

def pack(names,rows,forward,target,kind):
    objects=[]
    for name in names:
        row=rows[name];mask=forward[name+'_score_mask'];R=forward[name+'_R'][mask]
        if kind=='published':
            gas=forward[name+'_published_gas'][mask][None,:]
            disk=forward[name+'_published_disk'][mask][None,:]
        else:
            gas=forward[name+'_gas'][:,mask];disk=forward[name+'_disk'][:,mask]
        v=target[name+'_v'][mask];error=target[name+'_error'][mask]
        if not np.all(np.isfinite(v)&(v>0)):
            raise ValueError('Nonpositive/invalid Vobs invalidates log score: '+name)
        objects.append({'name':name,'meta':row['meta'],'R':R,'gas':gas,'disk':disk,'v':v,'error':error})
    assert objects
    total=len(objects)
    return {'objects':objects,'R':np.concatenate([o['R'] for o in objects]),
         'gas':np.concatenate([o['gas'] for o in objects],axis=1),
         'disk':np.concatenate([o['disk'] for o in objects],axis=1),
         'v':np.concatenate([o['v'] for o in objects]),
         'weight':np.concatenate([np.full(len(o['R']),1/(total*len(o['R']))) for o in objects])}

def prediction(data,model,p):
    U=p['U']; g=data['gas'];d=data['disk'];v2=g[0]+U*d[0]
    if model=='L':
        w=np.array(p['weights']);v2=v2+w@(g[1:]-g[0]+U*(d[1:]-d[0]))
    if np.any(v2<=0):return None
    if model=='NL':
        z=np.sqrt((v2/data['R']*ACC)/p['a0'])
        v2=v2/(-np.expm1(-z))
    return np.sqrt(v2)

def loss(data,model,p):
    pred=prediction(data,model,p)
    if pred is None:return 1e6
    r=np.log10(pred/data['v'])
    return float(np.dot(data['weight'],r*r))

def fit(data,model,fixed_U):
    starts=[]
    if model=='N':
        if fixed_U:
            p={'U':.5};return p,{'loss':loss(data,model,p),'starts':[],'global_count':0}
        f=lambda u:loss(data,model,{'U':float(u)})
        r=minimize_scalar(f,bounds=(.1,1.),method='bounded',options={'xatol':1e-12})
        choices=[(float(r.fun),float(r.x)),(f(.1),.1),(f(1.),1.)]
        val,u=min(choices)
        return {'U':u},{'loss':val,'success':bool(r.success),'message':str(r.message),'global_count':1}
    if model=='NL':
        if fixed_U:
            f=lambda loga:loss(data,model,{'U':.5,'a0':10**float(loga)})
            r=minimize_scalar(f,bounds=(-12,-8),method='bounded',options={'xatol':1e-11})
            val,loga=min([(float(r.fun),float(r.x)),(f(-12),-12),(f(-8),-8)])
            return {'U':.5,'a0':10**loga},{'loss':val,'success':bool(r.success),'global_count':1}
        def f(x):return loss(data,model,{'U':10**float(x[1]),'a0':10**float(x[0])})
        for loga in (-12.,-10.,-8.):
            for U in (.2,.5,1.):
                r=minimize(f,[loga,np.log10(U)],method='L-BFGS-B',bounds=[(-12,-8),(-1,0)],
                           options={'ftol':1e-14,'gtol':1e-10,'maxiter':2000})
                starts.append({'x':r.x.tolist(),'loss':float(r.fun),'success':bool(r.success),'message':str(r.message)})
        best=min(starts,key=lambda r:r['loss'])
        return {'U':10**best['x'][1],'a0':10**best['x'][0]},{'loss':best['loss'],'starts':starts,'global_count':2}
    assert model=='L'
    base,_=fit(data,'N',fixed_U)
    def pars(x): return {'U':.5 if fixed_U else float(x[0]),'weights':list(map(float,x if fixed_U else x[1:]))}
    def f(x):return loss(data,model,pars(x))
    wstarts=[np.zeros(6),np.full(6,.1)]+[np.eye(6)[i] for i in range(6)]
    bounds=[(0,1)]*6 if fixed_U else [(.1,1)]+[(0,1)]*6
    def sumw(x):return float(np.sum(x if fixed_U else x[1:]))
    for w in wstarts:
        x0=w if fixed_U else np.r_[base['U'],w]
        if f(x0)>=1e6:
            starts.append({'x':x0.tolist(),'loss':1e6,'success':False,'message':'invalid radial-force start'});continue
        r=minimize(f,x0,method='SLSQP',bounds=bounds,constraints=[{'type':'ineq','fun':lambda x:1-sumw(x)}],
                   options={'ftol':1e-13,'maxiter':2000})
        starts.append({'x':r.x.tolist(),'loss':float(r.fun),'success':bool(r.success),'message':str(r.message),'sum_weights':sumw(r.x)})
    # Keep nested Newtonian control even if a constrained optimizer fails.
    bx=np.zeros(6) if fixed_U else np.r_[base['U'],np.zeros(6)]
    starts.append({'x':bx.tolist(),'loss':f(bx),'success':True,'message':'nested Newtonian control','sum_weights':0.})
    valid=[r for r in starts if r['success'] and r.get('sum_weights',0)<=1+1e-8]
    best=min(valid,key=lambda r:r['loss']);p=pars(np.array(best['x']))
    assert min(p['weights'])>=-1e-10
    return p,{'loss':best['loss'],'starts':starts,'global_count':6 if fixed_U else 7}

def weighted_median(v,w):
    order=np.argsort(v);return float(v[order][np.searchsorted(np.cumsum(w[order]),.5*np.sum(w))])

def score(data,model,p):
    pred=prediction(data,model,p)
    if pred is None:return {'status':'nonpositive predicted acceleration'}
    residual=np.log10(pred/data['v']);per=[];offset=0
    for o in data['objects']:
        n=len(o['R']);r=residual[offset:offset+n];vp=pred[offset:offset+n];err=o['error'];valid=err>0
        per.append({'name':o['name'],'n':n,'rms_log10_velocity':float(np.sqrt(np.mean(r*r))),
          'mean_log10_velocity':float(np.mean(r)),'median_log10_velocity':float(np.median(r)),
          'descriptive_rms_error_normalized':float(np.sqrt(np.mean(((vp[valid]-o['v'][valid])/err[valid])**2))) if np.any(valid) else None,
          'R_kpc':o['R'].tolist(),'observed_km_s':o['v'].tolist(),'predicted_km_s':vp.tolist(),'log10_residual':r.tolist()})
        offset+=n
    return {'status':'evaluated','galaxies':len(per),'rows':len(pred),'galaxy_equal_rms_log10_velocity':float(np.sqrt(np.dot(data['weight'],residual**2))),
       'galaxy_equal_mean_log10_velocity':float(np.dot(data['weight'],residual)),
       'galaxy_equal_median_log10_velocity':weighted_median(residual,data['weight']),'per_galaxy':per}

def main():
    guard();start=time.time()
    reports={n:json.loads((OUT/f'baryonic_reconstruction_{n}.json').read_text()) for n in (64,96)}
    forward={n:np.load(OUT/f'baryonic_forward_{n}.npz') for n in (64,96)}
    rows={n:{r['name']:r for r in report['rows']} for n,report in reports.items()}
    common=sorted(set(reports[64]['accepted'])&set(reports[96]['accepted']))
    specs=[('forward64',64,'forward',reports[64]['accepted']),('forward96_common',96,'forward',common),
           ('forward64_common',64,'forward',common),('published_all',64,'published',list(rows[64])),
           ('published64_sample',64,'published',reports[64]['accepted'])]
    protocol=Path(__file__).with_name('FROZEN_COMPARISON.md')
    freeze={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'code_sha256':digest(__file__),
      'forward_code_sha256':digest(Path(__file__).with_name('galaxy_forward.py')),'protocol_sha256':digest(protocol),
      'sources':{str(OUT/f'baryonic_forward_{n}.npz'):digest(OUT/f'baryonic_forward_{n}.npz') for n in (64,96)},
      'split':{label:{split:[name for name in names if rows[n][name]['split']==split] for split in ('train','test')} for label,n,kind,names in specs},
      'status':'before Vobs load or any target-response fit in this runner; extra common sample sensitivity declared before unsealing'}
    freeze_path=OUT/'fit_code_and_split_freeze.json'
    assert not freeze_path.exists(),'Do not overwrite frozen target evaluation; investigate under a new documented block'
    freeze_path.write_text(json.dumps(freeze,indent=2)+'\n')
    targets=np.load(OUT/'sealed_targets.npz');trained=[];data={}
    for label,n,kind,names in specs:
        guard();train_names=freeze['split'][label]['train']
        train=pack(train_names,rows[n],forward[n],targets,kind);data[label]=(n,kind,names,train)
        for fixed in (False,True):
            for model in (['N','L','NL'] if kind=='forward' else ['N','NL']):
                p,receipt=fit(train,model,fixed)
                entry={'dataset':label,'model':model,'fixed_U':fixed,'parameters':p,'fit':receipt}
                trained.append(entry)
                print(json.dumps({'stage':'train','dataset':label,'model':model,'fixed_U':fixed,'parameters':p,'rms':receipt['loss']**.5}),flush=True)
    trainfile=OUT/'training_parameters_frozen.json'
    trainfile.write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entries':trained,'status':'frozen before test scoring'},indent=2)+'\n')
    # All global parameters have now been frozen. Test data never enter fit().
    results=[]
    for entry in trained:
        guard();label=entry['dataset'];n,kind,names,train=data[label]
        test=pack(freeze['split'][label]['test'],rows[n],forward[n],targets,kind)
        result=dict(entry)
        result['train']=score(train,entry['model'],entry['parameters'])
        result['test']=score(test,entry['model'],entry['parameters']);results.append(result)
        print(json.dumps({'stage':'test','dataset':label,'model':entry['model'],'fixed_U':entry['fixed_U'],
          'rms':result['test'].get('galaxy_equal_rms_log10_velocity'),'galaxies':result['test'].get('galaxies')}),flush=True)
    output={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.time()-start,'code_sha256':digest(__file__),
       'freeze_sha256':digest(freeze_path),'training_parameters_sha256':digest(trainfile),'status':'processed-curve model-development comparison; no likelihood or exclusion significance',
       'results':results}
    (OUT/'comparison_results.json').write_text(json.dumps(output,indent=2)+'\n')

if __name__=='__main__':main()
