"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib

    import json

    import pathlib

    import mpmath as mp

    import numpy as np

    mp.mp.dps=80

    checks=[]

    rank_cases=[]

    def spectrum(rows):
        a=np.asarray([[float(x) for x in row] for row in rows])
        a=a/np.linalg.norm(a,axis=0,keepdims=True)
        a=a/np.linalg.norm(a,axis=1,keepdims=True)
        sv=np.linalg.svd(a,compute_uv=False)
        b=mp.matrix(rows)
        for j in range(b.cols):
            norm=mp.sqrt(mp.fsum(b[i,j]**2 for i in range(b.rows)))
            for i in range(b.rows): b[i,j]/=norm
        for i in range(b.rows):
            norm=mp.sqrt(mp.fsum(b[i,j]**2 for j in range(b.cols)))
            for j in range(b.cols): b[i,j]/=norm
        svmp=mp.svd(b,compute_uv=False)
        return {'numpy_singular_values':sv.tolist(),
                'mpmath_80digit_singular_values':[mp.nstr(v,25) for v in svmp],
                'numpy_relative_threshold_rank':int(np.count_nonzero(sv/sv[0]>1e-10)),
                'mpmath_relative_threshold_rank':sum(v/svmp[0]>mp.mpf('1e-10') for v in svmp),
                'mpmath_min_max_ratio':mp.nstr(svmp[svmp.rows-1,0]/svmp[0],25),
                'mpmath_log10_condition':float(mp.log10(svmp[0]/svmp[svmp.rows-1,0]))}

    for k0 in ['0.1','1','10','100','1000']:
        trace=[];scalar=[];modes=[]
        for ratio in ['1','1.2','1.5','2','3']:
            k=mp.mpf(k0)*mp.mpf(ratio);L=k*k/4
            d=9+8*L;z=6*L/(d+mp.sqrt(d*d+96*L))
            m=(-1+mp.sqrt(1+4*z))/2
            Y=(8*m*m+12*m+3)/(2*m+3)
            trace.append([m,1,m*Y,Y]);scalar.append([-m*Y,-Y,m,L,1])
            modes.append({'k':mp.nstr(k,12),'m':mp.nstr(m,25),'Y':mp.nstr(Y,25)})
        tr=spectrum(trace);sc=spectrum(scalar)
        rank_cases.append({'k0':k0,'modes':modes,'trace':tr,'scalar':sc})
        checks.append({'name':'high_precision_trace_positive_'+k0,
                       'pass':mp.mpf(tr['mpmath_min_max_ratio'])>0})
        checks.append({'name':'high_precision_scalar_positive_'+k0,
                       'pass':mp.mpf(sc['mpmath_min_max_ratio'])>0})

    rng=np.random.default_rng(20261016)

    noise_cases=[]

    for n in [65,129,257]:
        radius=np.linspace(.2,1.2,n);dr=radius[1]-radius[0];ri=radius[1:-1]
        wp=ri*ri/(2*dr*dr)+ri/(2*dr)
        w0=-ri*ri/(dr*dr)
        wm=ri*ri/(2*dr*dr)-ri/(2*dr)
        sumw2=wp*wp+w0*w0+wm*wm
        for du in [.005,.025,.1]:
            us=1.6+np.array([-du,0.,du])
            truthpsi=(1+us[:,None]+us[:,None]**2)*radius[None,:]**2/3
            for sigma in [0.,1e-8,1e-6]:
                noise=rng.normal(0.,sigma,size=truthpsi.shape)
                record=truthpsi+noise
                reconstructed=(wm*record[:,:-2]+w0*record[:,1:-1]+wp*record[:,2:])
                second=(reconstructed[0]-2*reconstructed[1]+reconstructed[2])/du**2
                ep=reconstructed[1]-(1+1.6+1.6**2)*ri*ri
                eu=second-2*ri*ri
                rms=lambda f:float(np.sqrt(np.mean(f*f)))
                # Conservative floating-operation scale; this is not a data-error bound.
                roundoff=100*np.finfo(float).eps*np.max(np.abs(truthpsi))*np.max(np.abs(wm)+np.abs(w0)+np.abs(wp))
                expected_p=float(sigma*np.sqrt(np.mean(sumw2)))
                expected_u=float(np.sqrt(6)*expected_p/du**2)
                noise_cases.append({'n':n,'dr':float(dr),'du':du,'sigma':sigma,
                                    'P_rms_error':rms(ep),'Puu_rms_error':rms(eu),
                                    'expected_P_noise_rms':expected_p,'expected_Puu_noise_rms':expected_u,
                                    'roundoff_P_bound':float(roundoff),
                                    'roundoff_Puu_bound':float(4*roundoff/du**2),
                                    'raw_noise_sha256':hashlib.sha256(noise.tobytes()).hexdigest()})
                if sigma==0:
                    checks.append({'name':f'polynomial_zero_noise_{n}_{du}',
                                   'pass':rms(ep)<roundoff and rms(eu)<4*roundoff/du**2})

    for check in checks: check['pass']=bool(check['pass'])

    return checks, {"rank_cases": rank_cases, "noise_cases": noise_cases}
