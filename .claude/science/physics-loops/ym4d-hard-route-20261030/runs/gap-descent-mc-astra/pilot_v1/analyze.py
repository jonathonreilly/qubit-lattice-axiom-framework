"""Binned jackknife, autocorrelation and periodic-cosh diagnostics. GUIDE only.

Run only after the sampler has stopped, under the same numeric lock/resource gate.
Raw records retain enough information to change any analysis decision explicitly.
"""
import csv
import json
import math
import os
from pathlib import Path
import resource
import sys
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import chi2

HERE=Path(__file__).resolve().parent
PLANES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def memory_gate():
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if (rss if sys.platform=='darwin' else 1024*rss)>2e9:raise RuntimeError('2 GB RSS stop')

def finite(x):
    if isinstance(x,dict):return {k:finite(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [finite(v) for v in x]
    if isinstance(x,np.ndarray):return finite(x.tolist())
    if isinstance(x,(np.floating,float)):return float(x) if np.isfinite(x) else None
    if isinstance(x,np.integer):return int(x)
    if isinstance(x,np.bool_):return bool(x)
    return x

def tau_int(x):
    x=np.asarray(x,dtype=float);x=x-x.mean();n=len(x)
    if np.dot(x,x)<1e-22:return 0.5
    z=np.fft.rfft(x,n=2*n);ac=np.fft.irfft(z*z.conj())[:n]/np.arange(n,0,-1)
    rho=ac/ac[0];s=.5
    # Initial positive pair sequence, with self-consistent window 6*tau.
    for t in range(1,min(n//5,1024)-1,2):
        pair=rho[t]+rho[t+1]
        if pair<=0:break
        s+=pair
        if t+1>=6*s:break
    return max(.5,float(s))

def channels(a,L):
    x=a[:,:48*L].astype(float).reshape(-1,2,2,6,2,L)
    out={}
    for ax,axis in enumerate((0,2)):
        for sm,steps in enumerate((0,2)):
            for shape in range(2):
                for p,(mu,nu) in enumerate(PLANES):
                    label=f'a{axis}_s{steps}_{mu}{nu}_{"P" if shape==0 else "R"}'
                    out[label]=(x[:,ax,sm,p,shape,:],axis in (mu,nu))
                groups={'L':[0],'T':[5],
                    'Mspace':[p for p in range(1,5) if axis not in PLANES[p]],
                    'Mtime':[p for p in range(1,5) if axis in PLANES[p]],
                    'scalar':[p for p in range(6) if axis not in PLANES[p]]}
                for name,idx in groups.items():
                    out[f'a{axis}_s{steps}_{name}_{"P" if shape==0 else "R"}']=(x[:,ax,sm,idx,shape,:].mean(axis=1),any(axis in PLANES[p] for p in idx))
    return out

def statistics(chains,binwidth,connected=True):
    L=chains[0].shape[1];half=L//2;bs=[];taus=[];chainstats=[]
    for x in chains:
        n=len(x);mean=x.mean(axis=1)
        prods=np.stack([(x*np.roll(x,-t,axis=1)).mean(axis=1) for t in range(half+1)],axis=1)
        centered=x-x.mean();probe=(centered*np.roll(centered,-2,axis=1)).mean(axis=1)
        taus.append(max(tau_int(mean),tau_int(probe)))
        k=n//binwidth
        b=np.column_stack([mean,prods])[:k*binwidth].reshape(k,binwidth,-1).mean(axis=1)
        bs.append(b)
        chainstats.append((b.mean(axis=0),b))
    b=np.concatenate(bs);B=len(b);full=b.mean(axis=0);jack=(B*full-b)/(B-1)
    C=full[1:]-(full[0]**2 if connected else 0)
    CJ=jack[:,1:]-(jack[:,0,None]**2 if connected else 0)
    D=CJ-CJ.mean(axis=0);cov=(B-1)/B*(D.T@D);err=np.sqrt(np.maximum(0,np.diag(cov)))
    # Cold/hot consistency of the mean and of the t=2 connected correlation.
    tests=[]
    for stat,b1 in chainstats:
        n=len(b1);j1=(n*stat-b1)/(n-1);v=stat[3]-(stat[0]**2 if connected else 0)
        jv=j1[:,3]-(j1[:,0]**2 if connected else 0)
        tests.append((stat[0],np.std(b1[:,0],ddof=1)/np.sqrt(n),v,np.std(jv,ddof=0)*np.sqrt(n-1)))
    def z(i,e):
        den=np.hypot(tests[0][e],tests[1][e]);return abs(tests[0][i]-tests[1][i])/den if den>1e-20 else 0.
    return dict(C=C,CJ=CJ,cov=cov,error=err,tau=taus,mean=full[0],mean_z=z(0,1),corr2_z=z(2,3),blocks=B,bin=binwidth)

def fit_one(C,cov,L,lo,hi):
    t=np.arange(lo,hi+1);y=C[lo:hi+1];v=cov[lo:hi+1,lo:hi+1]
    if len(y)<2 or not np.all(np.isfinite(y)) or np.max(np.diag(v))<=0:return None
    W=np.linalg.pinv(v,rcond=1e-9)
    def at(m):
        f=np.exp(-m*t)+np.exp(-m*(L-t));den=f@W@f
        A=(f@W@y)/den if den>0 else 0
        r=y-A*f
        return (float(r@W@r) if A>0 else 1e100),float(A)
    sol=minimize_scalar(lambda m:at(m)[0],bounds=(.001,5.),method='bounded',options={'xatol':1e-6})
    q,A=at(sol.x);dof=len(y)-2
    return dict(m=sol.x,A=A,chi2=q,dof=dof,p=chi2.sf(q,dof) if dof>0 else None)

def fit_jack(s,L,lo,hi):
    f=fit_one(s['C'],s['cov'],L,lo,hi)
    if f is None:return None
    jj=[fit_one(c,s['cov'],L,lo,hi) for c in s['CJ']]
    if any(v is None for v in jj):return None
    masses=np.array([v['m'] for v in jj]);f['error']=np.std(masses,ddof=0)*np.sqrt(len(masses)-1)
    f['boundary_fraction']=np.mean((masses<.002)|(masses>4.99));f['range']=[lo,hi]
    return f

def effective(s,L):
    vals=[]
    for t in range(1,L//2+1):
        after=t+1 if t<L//2 else t-1
        def calc(c):
            ratio=(c[...,t-1]+c[...,after])/(2*c[...,t])
            return np.where((c[...,t]>0)&(ratio>=1),np.arccosh(np.maximum(ratio,1)),np.nan)
        with np.errstate(divide='ignore',invalid='ignore'):m=calc(s['C']);j=calc(s['CJ'])
        valid=np.isfinite(j);error=np.std(j)*np.sqrt(len(j)-1) if valid.all() else np.nan
        vals.append(dict(t=t,m=m,error=error,valid_jack_fraction=valid.mean()))
    return vals

def analyze_channel(xs,L,connected=True):
    if max(float(x.var()) for x in xs)<1e-20:return dict(status='constant',accepted=False)
    s=statistics(xs,64,connected);s2=statistics(xs,128,connected)
    result={k:s[k] for k in ('C','error','tau','mean','mean_z','corr2_z','blocks','bin')}
    result['effective']=effective(s,L);result['fits']=[];result['accepted']=False
    for lo in range(2,L//2-1):
        hi=L//2;snr=np.divide(s['C'][lo:hi+1],s['error'][lo:hi+1],out=np.zeros(hi-lo+1),where=s['error'][lo:hi+1]>0)
        central=fit_one(s['C'],s['cov'],L,lo,hi)
        if central is None:continue
        central.update(range=[lo,hi],min_snr=float(snr.min()),accepted=False)
        if snr.min()<2 or central['p']<.01:
            central['reason']='signal_or_chi2';result['fits'].append(central);continue
        f=fit_jack(s,L,lo,hi);shift=fit_jack(s,L,lo+1,hi);dbl=fit_jack(s2,L,lo,hi)
        if f is None or shift is None or dbl is None:
            central['reason']='jackknife_failed';result['fits'].append(central);continue
        f['min_snr']=float(snr.min());f['shift']=shift;f['double_bin']=dbl
        reasons=[]
        if snr.min()<3:reasons.append('signal_below_3sigma')
        if f['p']<.05:reasons.append('chi2')
        if f['error']>=.5*f['m'] or f['boundary_fraction']>.02:reasons.append('mass_error_or_boundary')
        if abs(f['m']-shift['m'])>2*np.hypot(f['error'],shift['error']):reasons.append('window_shift')
        if abs(f['m']-dbl['m'])>2*np.hypot(f['error'],dbl['error']):reasons.append('bin_shift')
        if f['error']<=0 or not .67<=dbl['error']/f['error']<=1.5:reasons.append('bin_error_instability')
        if 64<8*max(s['tau']):reasons.append('bin_too_short')
        if sum(len(x) for x in xs)/(2*max(s['tau']))<100:reasons.append('low_ESS')
        if s['mean_z']>4 or s['corr2_z']>4:reasons.append('hot_cold')
        f['accepted']=not reasons;f['reasons']=reasons
        f['mL']=f['m']*L;f['thermal_warning']=f['mL']<4
        result['fits'].append(f)
    good=[f for f in result['fits'] if f.get('accepted')]
    if good:
        # Latest admissible start, fixed before looking at minima across channels.
        result['chosen']=good[-1];result['accepted']=True;result['status']='candidate_plateau'
    else:result['status']='OPEN'
    return result

def scalar_jack(chains,fun,bw=64):
    b=np.concatenate([x[:len(x)//bw*bw].reshape(-1,bw,*x.shape[1:]).mean(axis=1) for x in chains]);n=len(b);m=b.mean(axis=0);js=(n*m-b)/(n-1)
    value=fun(m);rep=np.array([fun(j) for j in js]);return dict(value=value,error=np.std(rep,axis=0,ddof=0)*np.sqrt(n-1))

def run(L,beta,mult):
    tags=[f'L{L}_b{beta:.1f}_{mult}_c{i}' for i in (0,1)]
    paths=[HERE/(tag+'.npz') for tag in tags]
    if not all(p.exists() for p in paths):return None
    raw=[np.load(p)['records'] for p in paths];cs=[channels(a,L) for a in raw]
    result=dict(L=L,beta=beta,mult=mult,n=sum(len(a) for a in raw),channels={})
    for key in cs[0]:
        xs=[c[key][0] for c in cs];result['channels'][key]=analyze_channel(xs,L)
    means=[a[:,48*L:48*L+24].astype(float).reshape(-1,6,4) for a in raw]
    result['plaquette']=scalar_jack(means,lambda m:m[:,0])
    result['creutz22']=scalar_jack(means,lambda m:-np.log(m[:,3]*m[:,0]/(m[:,1]*m[:,2])))
    good=[(k,c['chosen']) for k,c in result['channels'].items() if c.get('accepted')]
    if good:
        k,f=min(good,key=lambda kf:kf[1]['m']);result['minimum']=dict(channel=k,**f)
    else:result['minimum']=None
    result['accepted_channel_count']=len(good)
    if mult==1:
        pp=[a[:,48*L+24:].astype(float).reshape(-1,2,3,L) for a in raw];result['torelon']={}
        for ax,axis in enumerate((0,2)):
            for d in range(3):
                result['torelon'][f'a{axis}_w{d}']=analyze_channel([p[:,ax,d,:] for p in pp],L,False)
        # Average correlators (not loops) over orthogonal winding directions.
        # Individual energies stay in the output; no extra fit is selected post hoc.
    if mult=='anchor':
        spin=[np.load(p)['spin'].astype(float) for p in paths]
        result['anchor_point_spin']=scalar_jack(spin,lambda m:m)
    path=HERE/f'analysis_L{L}_b{beta:.1f}_{mult}.json';path.write_text(json.dumps(finite(result),indent=2)+'\n')
    memory_gate();return result

def selftest():
    L=12;t=np.arange(7);m=.71;C=.3*(np.exp(-m*t)+np.exp(-m*(L-t)))
    f=fit_one(C,np.eye(7)*1e-8,L,2,6)
    if abs(f['m']-m)>2e-6:raise RuntimeError('cosh fit control')
    s=dict(C=C,CJ=np.tile(C,(32,1)))
    if max(abs(v['m']-m) for v in effective(s,L))>1e-10:raise RuntimeError('effective mass control')
    if analyze_channel([np.ones((256,8))]*2,8)['status']!='constant':raise RuntimeError('constant control')
    return dict(cosh_mass=f['m'],expected=m,constant_rejected=True)

def o4_results():
    refs={2.3:(18.95,.13,1.28420/2,.00018/2),2.4:(25.39,.13,1.31898/2,.00016/2),2.5:(33.14,.12,1.35023/2,.00011/2)}
    results=[]
    for beta in (2.3,2.4,2.5):
        paths=[HERE/f'o4_L128_b{beta:.1f}_c{i}.csv.gz' for i in (0,1)]
        if not all(p.exists() for p in paths):continue
        a=[np.loadtxt(p,delimiter=',',skiprows=1) for p in paths]
        f=lambda x:np.sqrt(x[1]/x[2]-1)/(2*np.sin(np.pi/128))
        xi=scalar_jack(a,f,512);xi2=scalar_jack(a,f,1024)
        en=scalar_jack(a,lambda x:x[0],512)
        ref,err,e,ee=refs[beta]
        tau=[max(tau_int(x[:,1]),tau_int(x[:,2]),tau_int(x[:,0])) for x in a]
        separate=[scalar_jack([x],f,512) for x in a]
        zhot=abs(separate[0]['value']-separate[1]['value'])/np.hypot(separate[0]['error'],separate[1]['error'])
        result=dict(beta=beta,L=128,xi2=xi,double_bin=xi2,tau_measurements=tau,
            hot_cold=separate,hot_cold_z=zhot,energy=en,reference_xi=[ref,err],reference_energy=[e,ee],
            reference='Borisenko-Skala hep-lat/9812020 Table 1, 2beta column',
            xi_z=(xi['value']-ref)/np.hypot(xi['error'],err),energy_z=(en['value']-e)/np.hypot(en['error'],ee))
        results.append(result)
    (HERE/'o4_summary.json').write_text(json.dumps(finite(results),indent=2)+'\n')

if __name__=='__main__':
    for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
        if os.environ.get(v)!='1':raise RuntimeError(v+' must be 1')
    print(json.dumps(selftest()),flush=True)
    rows=[]
    for beta in (2.3,2.4,2.5):
        for mult in (1,2,4,8,'face','anchor'):
            for L in (8,12):
                r=run(L,beta,mult)
                if r is None:continue
                row={k:r[k] for k in ('L','beta','mult','n','minimum','accepted_channel_count')}
                row['tau_max']=max((max(c['tau']) for c in r['channels'].values() if 'tau'in c),default=0)
                row['hot_cold_z_max']=max((max(c['mean_z'],c['corr2_z']) for c in r['channels'].values() if 'mean_z'in c),default=0)
                rows.append(finite(row));print(json.dumps(finite(row)),flush=True)
    (HERE/'summary.json').write_text(json.dumps(rows,indent=2)+'\n')
    o4_results()
