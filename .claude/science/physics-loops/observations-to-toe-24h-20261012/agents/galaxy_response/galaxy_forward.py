#!/usr/bin/env python3
"""Positive axisymmetric source reconstruction, never using Vobs to fit mass."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
import argparse, datetime, hashlib, io, json, time, zipfile
import numpy as np
import scipy
from scipy.constants import G as G_SI, parsec
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.special import roots_legendre, j0, j1, i0e, i1e

BASE=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=BASE/'galaxy_response'
INPUT=OUT/'inputs'
G=4.30091e-6  # declared kpc (km/s)^2 / solar mass; same in every response
LAMBDAS=np.array([.3,1.,3.,10.,30.,100.])
EXPOSED={'CamB','D512-2','D564-8','D631-7','DDO064','UGCA442'}
QUAD_CACHE={}

def guard():
    assert not list(BASE.glob('*STOP_REQUESTED*')), 'Stop requested'
    assert time.time()<json.loads((BASE/'DEADLINE.json').read_text())['deadline_epoch'], 'Deadline'

def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def metadata():
    result={}
    for line in (INPUT/'SPARC_Lelli2016c.mrt').read_text().splitlines():
        try:
            f=line.split()
            if len(f)<19: continue
            # Official website copy has separator spaces beyond the historical
            # byte schema. Token columns retain the specified order.
            name=f[0];t=int(f[1]);distance=float(f[2])
            result[name]={'name':name,'T':t,'D':distance,'e_D':float(f[3]),'f_D':int(f[4]),
              'i':float(f[5]),'e_i':float(f[6]),'L':float(f[7])*1e9,
              'e_L':float(f[8])*1e9,'Rd':float(f[11]),'MHI':float(f[13])*1e9,
              'RHI':float(f[14]),'Q':int(f[17]),'original_references':' '.join(f[18:])}
        except (ValueError,IndexError): pass
    assert len(result)==175, len(result)
    return result

def inputs():
    meta=metadata(); output={}; targets={}; excluded=[]
    with zipfile.ZipFile(INPUT/'Rotmod_LTG.zip') as z:
        for filename in sorted(z.namelist()):
            name=filename.removesuffix('_rotmod.dat')
            x=np.loadtxt(io.StringIO(z.read(filename).decode()))
            assert x.ndim==2 and x.shape[1]==8
            m=meta[name]
            # Vobs and error are stored separately, not passed to reconstruction.
            targets[name]={'v':x[:,1],'error':x[:,2]}
            reasons=[]
            if m['Q'] not in (1,2): reasons.append('quality')
            if m['i']<30: reasons.append('inclination')
            if np.any(x[:,5]!=0): reasons.append('bulge')
            if np.count_nonzero(x[:,0]>0)<6: reasons.append('fewer_than_six_radii')
            mask=(x[:,0]>=.5*m['Rd']) & (x[:,0]>0)
            if mask.sum()<5: reasons.append('fewer_than_five_scored_radii')
            if m['Rd']<=0 or m['L']<=0: reasons.append('invalid_size_or_luminosity')
            if reasons:
                excluded.append({'name':name,'reasons':reasons});continue
            test=(int(hashlib.sha256(('galaxy-response-20261012:'+name).encode()).hexdigest()[:8],16)%5==0) and name not in EXPOSED
            output[name]={'meta':m,'R':x[:,0],'gas':x[:,3]*abs(x[:,3]),'disk':x[:,4]*abs(x[:,4]),'SB':x[:,6],
                          'score_mask':mask,'split':'test' if test else 'train'}
    return output,targets,excluded

def quadrature(n):
    if n not in QUAD_CACHE:
        x,w=roots_legendre(n);QUAD_CACHE[n]=((x+1)/2,w/2)
    return QUAD_CACHE[n]

def basis(R, A, sigma, h, lambdas=LAMBDAS, nodes=1024):
    x,w=quadrature(nodes);k=x*8/sigma;w=w*8/sigma
    left=j1(np.outer(R,k));right=j0(np.outer(k,A))
    common=w*np.exp(-.5*(sigma*k)**2)
    mats=[]
    for lam in np.r_[np.inf,lambdas]:
        mu=0 if np.isinf(lam) else 1/lam
        q=np.sqrt(k*k+mu*mu)
        kernel=common*k*k/q/(1+h*q)
        mats.append(G*R[:,None]*((left*kernel[None,:])@right))
    return np.asarray(mats)

def surface_basis(R,A,sigma):
    arg=R[:,None]*A[None,:]/sigma**2
    return np.exp(-.5*((R[:,None]-A[None,:])/sigma)**2)*i0e(arg)/(2*np.pi*sigma**2)

def fit_component(matrix,target,mass):
    if mass==0 and np.all(target==0):
        return np.zeros(matrix.shape[1]),{'status':'zero','accepted':True,'rms':0.,'max':0.,'mass_ratio':1.}
    if mass<=0:
        return None,{'status':'inconsistent_nonpositive_mass','accepted':False}
    scale=max(float(np.max(abs(target))),1.)
    A=matrix*mass/scale;y=target/scale;n=len(y)
    reg=1e-10  # deterministic minimal-norm preference, no Vobs dependence
    def objective(x):
        residual=A@x-y
        return .5*np.mean(residual**2)+.5*reg*np.dot(x,x)
    def jac(x): return A.T@(A@x-y)/n+reg*x
    cons=[{'type':'ineq','fun':lambda x:np.sum(x)-.95,'jac':lambda x:np.ones_like(x)},
          {'type':'ineq','fun':lambda x:1.05-np.sum(x),'jac':lambda x:-np.ones_like(x)}]
    result=minimize(objective,np.ones(A.shape[1])/A.shape[1],jac=jac,method='SLSQP',bounds=[(0,None)]*A.shape[1],constraints=cons,
                    options={'ftol':1e-12,'maxiter':1500,'disp':False})
    residual=A@result.x-y;rms=float(np.sqrt(np.mean(residual**2)));maxerr=float(np.max(abs(residual)))
    massratio=float(np.sum(result.x))
    accepted=bool(result.success and rms<=.02 and maxerr<=.05 and .95-1e-8<=massratio<=1.05+1e-8)
    return result.x*mass,{'status':str(result.message),'success':bool(result.success),'iterations':int(result.nit),
        'accepted':accepted,'rms':rms,'max':maxerr,'mass_ratio':massratio,'objective':float(result.fun),'scale_v2':scale,
        'positive_terms':int(np.count_nonzero(result.x>1e-9))}

def controls():
    # Independent real-space force for a central Gaussian disk: integrate radial
    # density derivative by parts to remove the local singular force kernel.
    # a_R=G/sigma² integral da a² Sigma(a) integral dphi cos(phi)/distance.
    R=np.array([.3,1.,3.,10.]);sigma=1.;A=np.array([0.]);M=1/G
    calculated=basis(R,A,sigma,0,lambdas=np.array([]),nodes=2048)[0,:,0]*M/R
    analytic=[]
    # Closed thin Gaussian potential is -GM sqrt(pi/2)/sigma exp(-z) I0(z),
    # z=R²/(4sigma²); derivative gives the following acceleration.
    for r in R:
        z=r*r/(4*sigma*sigma)
        analytic.append(np.sqrt(np.pi/2)*r/(2*sigma**3)*(i0e(z)-i1e(z)))
    err=float(np.max(abs(calculated/analytic-1)))
    assert err<2e-11,err
    r=np.array([80.]);lam=np.array([40.])
    # Compact Gaussian far field compared to point pole, finite-size O(sigma²/R²).
    far=basis(r,A,.1,0,lambdas=lam,nodes=4096)[:,:,0]*M
    point=np.array([1/80,(1+80/40)*np.exp(-80/40)/80])
    farerr=float(np.max(abs(far[:,0]/point-1)))
    assert farerr<1e-4,farerr
    # Gauss node convergence using a noncentral ring and exponential height.
    rr=np.array([.1,.8,1.2,2.,4.]);aa=np.array([0.,.4,1.,2.,3.])
    b1=basis(rr,aa,.125,.2,nodes=1024);b2=basis(rr,aa,.125,.2,nodes=2048)
    qe=float(np.max(abs(b1-b2))/np.max(abs(b2)))
    assert qe<1e-10,qe
    return {'gaussian_disk_relative_error':err,'gaussian_far_point_relative_error':farerr,
            'noncentral_finite_height_quadrature_difference':qe,'gaussian_control_values':calculated.tolist()}

def reconstruct(rings):
    guard();started=time.time();items,targets,excluded=inputs();checks=controls(); rows=[];arrays={}
    accepted=[]
    for name,d in items.items():
        guard();R=d['R'];rmax=float(max(R));sigma=rmax/(rings/2);A=np.linspace(0,1.5*rmax,rings)
        h=.196*d['meta']['Rd']**.633
        row={'name':name,'split':d['split'],'n_radii':len(R),'n_score':int(d['score_mask'].sum()),'meta':d['meta'],'sigma':sigma,'h':h}
        for component,mass,height in [('gas',1.33*d['meta']['MHI'],0.),('disk',d['meta']['L'],h)]:
            matrices=basis(R,A,sigma,height,nodes=1024)
            masses,result=fit_component(matrices[0],d[component],mass)
            row[component]=result
            if masses is None: continue
            fine=basis(R,A,sigma,height,nodes=2048)
            pred=np.einsum('mij,j->mi',fine,masses)
            coarse=np.einsum('mij,j->mi',matrices,masses)
            err=float(np.max(abs(pred-coarse))/max(1,float(np.max(abs(pred)))))
            row[component]['quadrature_difference']=err
            assert err<1e-8,(name,component,err)
            arrays[name+'_'+component]=pred;arrays[name+'_'+component+'_masses']=masses
            if component=='disk':
                sb=surface_basis(R,A,sigma)@masses/1e6
                arrays[name+'_reconstructed_SB']=sb
                row['SB_fractional_L1_diagnostic']=float(np.sum(abs(sb-d['SB']))/max(np.sum(d['SB']),1.))
        good=row['gas']['accepted'] and row['disk']['accepted']
        row['accepted']=good
        if good:accepted.append(name)
        rows.append(row)
        arrays[name+'_R']=R;arrays[name+'_score_mask']=d['score_mask'];arrays[name+'_A']=A
        arrays[name+'_published_gas']=d['gas'];arrays[name+'_published_disk']=d['disk']
        # Target arrays are copied without reading them into any optimization.
        print(json.dumps({'name':name,'split':d['split'],'accepted':good,'gas_rms':row['gas'].get('rms'),'disk_rms':row['disk'].get('rms')}),flush=True)
    np.savez_compressed(OUT/f'baryonic_forward_{rings}.npz',**arrays)
    np.savez_compressed(OUT/'sealed_targets.npz',**{n+'_'+k:v for n,t in targets.items() for k,v in t.items()})
    report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'code_sha256':digest(__file__),'source_files':{str(p):digest(p) for p in [INPUT/'SPARC_Lelli2016c.mrt',INPUT/'Rotmod_LTG.zip']},
        'rings':rings,'lambda_kpc':LAMBDAS.tolist(),'G_kpc_km2_s2_per_Msun':G,'selection_excluded':excluded,'controls':checks,'rows':rows,'accepted':accepted,
        'n_initial':len(items),'n_accepted':len(accepted),'runtime_seconds':time.time()-started,'software':{'numpy':np.__version__,'scipy':scipy.__version__},
        'status':'baryonic calibration only; Vobs not supplied to source fit'}
    (OUT/f'baryonic_reconstruction_{rings}.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['rings','controls','n_initial','n_accepted','runtime_seconds']}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--rings',type=int,choices=[64,96],default=64);args=parser.parse_args();reconstruct(args.rings)
