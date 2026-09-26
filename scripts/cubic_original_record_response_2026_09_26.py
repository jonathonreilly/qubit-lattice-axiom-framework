"""Two prospectively fixed4096 Haar targets; full original first-minus vector.

Statistical coverage is conditional on iid uniform exact integration samples.
The implementation uses seeded pseudorandom binary64 points and noninterval
floating propagation; a separate stepped-Taylor reconstruction tests selected
samples. Endpoint and time-average are distinct targets, with joint95% bounds.
"""
from pathlib import Path
import base64,hashlib,json,math,time
import scipy
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

SAMPLES=4096

def sample_payload(values,ks,times,norm_errors):
    """Lossless terminal payload kept below the canonical cache stdout cap.

    Decode base64 into little-endian binary64 and reshape to (4096,2).
    Columns are endpoint and time_average. Regenerate the integration design
    using the recorded PCG64 seeds, then verify the little-endian array hashes.
    """
    def raw(x):return np.ascontiguousarray(x,dtype='<f8').tobytes()
    assert np.shape(values)==(SAMPLES,2)
    data=raw(values)
    result={'sample_payload_schema':1,'shape':[SAMPLES,2],'dtype':'<f8',
      'columns':['endpoint','time_average'],'encoding':'base64',
      'values_sha256':hashlib.sha256(data).hexdigest(),
      'values':base64.b64encode(data).decode('ascii'),
      'design':{'generator':'PCG64','numpy_version':np.__version__,
        'momentum_seed':261926322,'momentum_uniform':[-float(np.pi),float(np.pi)],
        'momentum_shape':[SAMPLES,3],'momenta_sha256':hashlib.sha256(raw(ks)).hexdigest(),
        'time_seed':261926323,'time_uniform':[0.,.02],
        'time_shape':[SAMPLES],'times_sha256':hashlib.sha256(raw(times)).hexdigest()},
      'norm_errors_sha256':hashlib.sha256(raw(norm_errors)).hexdigest(),
      'maximum_norm_errors':np.max(norm_errors,axis=0).tolist(),
      'scipy_version':scipy.__version__}
    assert base64.b64decode(result['values'])==data
    assert len(json.dumps(result))<90000
    return result

def calculate(work):
    work=Path(work);start=time.monotonic()
    h=np.load(work/'closed_quotient_operator.npz');g=np.load(work/'projected_hazard.npz')
    n=len(h['diagonal']);phi=h['first_minus'].astype(complex)
    off=np.zeros(n,dtype=np.int64);np.add.at(off,g['dst'],abs(g['coefficient']))
    lo=int(np.min(g['diagonal']-off));hi=int(np.max(g['diagonal']+off));assert (lo,hi)==(-684,212)
    ks=np.random.Generator(np.random.PCG64(261926322)).uniform(-np.pi,np.pi,(SAMPLES,3))
    times=np.random.Generator(np.random.PCG64(261926323)).uniform(0.,.02,SAMPLES)
    shift=float(np.mean(h['diagonal']));identity=sparse.eye(n);values=[];norm_errors=[]
    for i,k in enumerate(ks):
        def fiber(x):
            return sparse.coo_matrix((x['coefficient']*np.exp(-1j*(x['tau']@k)),
                      (x['dst'],x['src'])),shape=(n,n)).tocsr()+sparse.diags(x['diagonal'])
        H=fiber(h);G=fiber(g);row=[];errs=[]
        for t in (.02,float(times[i])):
            y=expm_multiply((-1j*t)*(H-shift*identity),phi,traceA=0.)
            error=float(abs(np.vdot(y,y).real-1));assert error<1e-9
            value=np.vdot(y,G@y);assert abs(value.imag)<1e-8 and lo-1e-6<=value.real<=hi+1e-6
            row.append(float(value.real));errs.append(error)
        values.append(row);norm_errors.append(errs)
        if (i+1)%128==0:print(json.dumps({'completed_samples':i+1,'fixed_stop':SAMPLES}),flush=True)
    values=np.asarray(values);norm_errors=np.asarray(norm_errors)
    np.savez_compressed(work/'original_record_response_samples.npz',momenta=ks,times=times,values=values,norm_errors=norm_errors)
    targets={};factor=math.log(160);changes=values+1164/5
    for j,name in enumerate(('endpoint','time_average')):
        x=changes[:,j];variance=float(np.var(x,ddof=1));mean=float(np.mean(x))
        radius=math.sqrt(2*variance*factor/SAMPLES)+7*(hi-lo)*factor/(3*(SAMPLES-1))
        targets[name]={'mean_change':mean,'sample_variance':variance,'standard_error_diagnostic':math.sqrt(variance/SAMPLES),
            'empirical_Bernstein_radius':radius,'conditional_joint95_interval':[mean-radius,mean+radius],
            'maximum_norm_error':float(np.max(norm_errors[:,j]))}
    result={'samples_each':SAMPLES,'momentum_seed':261926322,'time_seed':261926323,'prior_samples_included':False,
       'exact_hazard_range':[lo,hi],'initial_exact':'-1164/5','targets':targets,
       'paired_sample_covariance':np.cov(changes.T,ddof=1).tolist(),
       'elapsed_seconds':time.monotonic()-start,
       'qualification':'Joint bound conditional on iid uniform exact integrands. Seeded PRNG, floating evaluation, physical identification/calibration separate. No fitted observational value.'}
    (work/'ORIGINAL_RECORD_RESPONSE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(sample_payload(values,ks,times,norm_errors)),flush=True)
    print(json.dumps(result,indent=2),flush=True)
    return result
