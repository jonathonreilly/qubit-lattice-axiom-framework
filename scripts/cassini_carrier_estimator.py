"""Frozen-window carrier estimator; no physical-noise or gravity calibration."""
from pathlib import Path
import collections, hashlib, json, math, sys
import numpy as np
from scipy.optimize import minimize_scalar

AUDIT_TIMEOUT_SEC = 180
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import cassini_rsr_development as rsr

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def amplitude_certificate(x,y):
    squared=[int(a)**2+int(b)**2 for a,b in zip(x,y)]
    ceiling=[math.isqrt(r)+(math.isqrt(r)**2<r) for r in squared]
    n=len(squared);s=sum(squared);c=sum(ceiling)
    numerator=n*s-c*c
    low=max((max(abs(int(a))-1,0))**2+(max(abs(int(b))-1,0))**2 for a,b in zip(x,y))
    high=min((abs(int(a))+1)**2+(abs(int(b))+1)**2 for a,b in zip(x,y))
    return dict(N=n,center_energy_integer=s,ceil_radius_sum_integer=c,
                constant_amplitude_residual_lower_numerator=numerator,
                lower_denominator=n,ideal_cell_energy_limit=2*n,
                quantization_only_rejected=numerator>2*n*n,
                max_cell_radius_lower_squared=low,min_cell_radius_upper_squared=high,
                common_amplitude_intersection_empty=low>high)

def estimate(z,fs=1000.,grid_size=16000):
    n=len(z);t=(np.arange(n)-(n-1)/2)/fs
    energy=float(np.vdot(z,z).real)
    fft=np.fft.fft(z,n=grid_size);freq=np.fft.fftfreq(grid_size,1/fs)
    k=int(np.argmax(np.abs(fft)));f0=float(freq[k]);step=fs/grid_size
    def correlation(f):return np.dot(z,np.exp(-2j*np.pi*f*t))
    def objective(f):return -abs(correlation(f))**2/energy/n
    fit=minimize_scalar(objective,bounds=(f0-step,f0+step),method='bounded',
                        options={'xatol':1e-9,'maxiter':100})
    # With centered times, an alias-period shift can change template phase.
    # Recompute amplitude at the returned frequency so the pair stays coherent.
    f=(float(fit.x)+fs/2)%fs-fs/2;c=correlation(f);a=c/n
    residual=float(np.vdot(z-a*np.exp(2j*np.pi*f*t),z-a*np.exp(2j*np.pi*f*t)).real)
    grid_amp=float(abs(fft[k]));derivative=2*np.pi*np.sum(np.abs(t)*np.abs(z))
    upper=min(float(np.sqrt(n*energy)),grid_amp+float(derivative)*step/2)
    return dict(frequency_Hz=f,grid_frequency_Hz=f0,
                grid_peak_correlation=grid_amp,fitted_complex_amplitude=[float(a.real),float(a.imag)],
                fit_success=bool(fit.success),fit_function_calls=int(fit.nfev),
                center_energy=energy,residual_energy=residual,
                fitted_tone_power_fraction=float(abs(c)**2/n/energy),
                numerical_global_residual_lower_bound=max(0.,energy-upper*upper/n),
                derivative_correlation_bound=float(derivative),grid_cover_radius_Hz=step/2,
                note='frequency and amplitude fit an explicitly conditional one-tone approximation; residual is not an upper bound on physical noise')

def controls():
    rows=[];fs=1000;n=1000;t=(np.arange(n)-(n-1)/2)/fs
    for f in [-499.98,-123.4567,-.124,0.,12.34567,499.98]:
        z=(123+321j)*np.exp(2j*np.pi*f*t);r=estimate(z)
        error=(r['frequency_Hz']-f+fs/2)%fs-fs/2
        assert abs(error)<3e-5,(f,error)
        assert r['fitted_tone_power_fraction']>1-1e-8
        assert r['numerical_global_residual_lower_bound']<1e-6*np.vdot(z,z).real
        a=complex(*r['fitted_complex_amplitude'])
        assert np.max(np.abs(a*np.exp(2j*np.pi*r['frequency_Hz']*t)-z))<.01
        rows.append({'control':'known_tone','frequency':f,'error':error})
    z=(123+321j)*np.exp(2j*np.pi*31.234*t)
    assert abs(estimate(z)['frequency_Hz']+estimate(z.conj())['frequency_Hz'])<1e-6
    rows.append({'control':'conjugation_reverses_sign'})
    # Exact integer certificate accepts a feasible cell waveform and rejects a clear one.
    assert not amplitude_certificate([101]*n,[11]*n)['quantization_only_rejected']
    assert amplitude_certificate([1,1001],[1,1])['quantization_only_rejected']
    assert amplitude_certificate([1,1001],[1,1])['common_amplitude_intersection_empty']
    rows.append({'control':'exact_amplitude_cell_witnesses'})
    # Eliminating the complex amplitude is a geometric identity, not a noise assumption.
    z=np.array([1+2j,4-3j,-2+1j]);u=np.exp(2j*np.pi*.137*np.arange(3));a=np.vdot(u,z)/3
    assert abs(np.vdot(z-a*u,z-a*u).real-(np.vdot(z,z).real-abs(np.vdot(u,z))**2/3))<1e-12
    rows.append({'control':'projection_identity'})
    return rows

def run(cache,out,protocol_dir):
    here=protocol_dir;out.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((ROOT/'scripts/cassini_rsr_development_inputs.json').read_text())
    inputs=manifest['products']
    for item in inputs:
        p=cache/item['filename'];assert sha(p)==item['sha256']
    rows=[];heads={}
    for band,stem,suffix in [('X','c32easc2002_169_1335x54x25d','.1a1'),('Ka','c32easc2002_169_1335x54k25d','.1b1')]:
        fields=rsr.schema(cache/('rsr_'+stem+'.lbl'));blob=(cache/(stem+suffix)).read_bytes()
        for j in range(600):
            rec=blob[4260*j:4260*(j+1)];h=rsr.header(rec,fields)
            assert h['SFDU SECOND']==48900+j and h['SAMPLE RATE']==1 and h['SAMPLE RESOLUTION']==16
            i,q=rsr.decode(rec,16);x=2*i.astype(np.int64)+1;y=2*q.astype(np.int64)+1;z=x+1j*y
            row=dict(band=band,record_index=j,second=48900+j,
                     error_count=h['DATA ERROR COUNT'],tracking_mode=h['TRACKING MODE'],
                     extreme_codes=int(np.count_nonzero((i==-32768)|(i==32767)|(q==-32768)|(q==32767))),
                     origin_reaching_cells=int(np.count_nonzero(x*x+y*y<=2)),
                     estimate=estimate(z),amplitude_certificate=amplitude_certificate(x,y),
                     nco_F=[h['SUB-CHANNEL FREQUENCY COEF F'+str(k)] for k in range(1,4)],
                     nco_P=[h['SUB-CHANNEL PHASE COEF P'+str(k)] for k in range(1,5)],
                     nco_accumulated=h['SUB-CHANNEL ACCUMULATED PHASE'],
                     nominal_LO_Hz=(h['DDC LO FREQUENCY']+h['RF-IF LO FREQUENCY'])*10**6)
            rows.append(row)
    ledger=out/'CARRIER_ESTIMATES_v1.jsonl'
    ledger.write_text(''.join(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n' for r in rows))
    stats={}
    for b in ('X','Ka'):
        rr=[r for r in rows if r['band']==b]
        describe=lambda v:dict(zip(['min','p01','median','p99','max'],np.quantile(v,[0,.01,.5,.99,1]).tolist()))
        stats[b]=dict(blocks=len(rr),frequency_Hz=describe([r['estimate']['frequency_Hz'] for r in rr]),
                     tone_power_fraction=describe([r['estimate']['fitted_tone_power_fraction'] for r in rr]),
                     residual_energy=describe([r['estimate']['residual_energy'] for r in rr]),
                     exact_quantization_only_rejections=sum(r['amplitude_certificate']['quantization_only_rejected'] for r in rr),
                     exact_empty_amplitude_intersections=sum(r['amplitude_certificate']['common_amplitude_intersection_empty'] for r in rr),
                     fit_failures=sum(not r['estimate']['fit_success'] for r in rr))
    result=dict(role='exposed development; no gravity inference or physical noise bound',
                source_sha256=sha(Path(__file__)),protocol_sha256=sha(here/'DEVELOPMENT_PROTOCOL_v1.json'),
                supplement_sha256=sha(here/'DEVELOPMENT_PROTOCOL_SUPPLEMENT_v1.json'),
                controls=controls(),ledger_sha256=sha(ledger),statistics=stats,
                independent_empirical_tests=0,fitted_parameters_per_block=3)
    (out/'CARRIER_SUMMARY_v1.json').write_text(json.dumps(result,indent=2)+'\n');return result

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--input-cache',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--protocol-dir',type=Path,required=True)
    a=ap.parse_args();print(json.dumps(run(a.input_cache,a.output_dir,a.protocol_dir),indent=2))
