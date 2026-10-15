"""Frozen exposed-development challenge of a conditional uniform error-direction law.

No physical error bound is estimated. No observation is held out from campaign
development; 'training/validation' below only names a mathematical sample split.
"""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import argparse,collections,hashlib,json,math,re,struct,time
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
PROTOCOL=ROOT/'.claude/science/physics-loops/observations-backward-24h-20261014/calibration_supplier'
from scipy.optimize import minimize_scalar
import cassini_error_direction as geo


def schema(label):
    blocks=re.findall(r'(?m)^  OBJECT\s*= COLUMN\n(.*?)^  END_OBJECT\s*= COLUMN',label.read_text(),re.S)
    return [(re.search(r'NAME\s*= "([^\"]*)"',b)[1],
             int(re.search(r'START_BYTE\s*= (\d+)',b)[1])-1,
             int(re.search(r'BYTES\s*= (\d+)',b)[1]),
             re.search(r'DATA_TYPE\s*= (\w+)',b)[1]) for b in blocks]


def header(record,fields):
    h={}
    for name,start,size,typ in fields:
        if name=='SAMPLE WORDS':continue
        raw=record[start:start+size]
        h[name]=struct.unpack('>d',raw)[0] if typ=='IEEE_REAL' else (raw.decode('ascii') if typ=='CHARACTER' else int.from_bytes(raw,'big',signed=typ=='MSB_INTEGER'))
    return h


def decode(record):
    # The registered products use 16-bit Q in the high word and I in the low.
    words=np.frombuffer(record,dtype='>u4',offset=260).astype(np.uint32)
    i=(words&65535).astype(np.int32);q=(words>>16).astype(np.int32)
    i[i>=32768]-=65536;q[q>=32768]-=65536
    return i,q


def training_reference(z,fs=1000.):
    n=len(z);t=geo.times(n,fs);energy=float(np.vdot(z,z).real)
    if energy==0:raise ValueError('zero training energy; estimator not specified')
    size=16000;transform=np.fft.fft(z,n=size);k=int(np.argmax(np.abs(transform)))
    f0=float(np.fft.fftfreq(size,1/fs)[k]);step=fs/size
    def loss(f):return -abs(np.dot(z,np.exp(-2j*np.pi*f*t)))**2/energy/n
    fit=minimize_scalar(loss,bounds=(f0-step,f0+step),method='bounded',options={'xatol':1e-9,'maxiter':100})
    return dict(frequency_Hz=(float(fit.x)+fs/2)%fs-fs/2,fit_success=bool(fit.success))


def receiver_controls():
    words=np.array([0x7fff8000,0x80007fff,0xffff0000,0x0000ffff],dtype='>u4')
    i,q=decode(bytes(260)+words.tobytes())
    assert i.tolist()==[-32768,32767,0,-1] and q.tolist()==[32767,-32768,-1,0]
    rows=[dict(control='signed_iq_word_order')]
    for f in [-499.98,-1.234,0.,12.34,499.98]:
        z=(123+321j)*np.exp(2j*np.pi*f*geo.times(500,1000.))
        result=training_reference(z);err=(result['frequency_Hz']-f+500)%1000-500
        assert result['fit_success'] and abs(err)<4e-5
        rows.append(dict(control='training_known_tone',frequency_Hz=f,error=err))
    return rows


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def desc(x):return dict(zip(['min','p01','median','p99','max'],np.quantile(x,[0,.01,.5,.99,1]).tolist()))
def pair(z):return [float(z.real),float(z.imag)]


def diagnose(z):
    train=z[:500];valid=z[500:];n=len(valid);q=math.sqrt(2*n)
    fit=training_reference(train);g=fit['frequency_Hz'];u=np.exp(2j*np.pi*g*geo.times(n,1000.))
    c=np.vdot(u,valid)/n;res=valid-c*u;E=float(np.vdot(res,res).real)
    lag={str(k):pair(np.vdot(res[:-k],res[k:])/E) for k in (1,2,3,4,5,10,20)}
    low,high,r,s=geo.spectral_parts(valid,g)
    # These diagnostics at a fitted training frequency have no exact nuisance-free
    # p-value. The separate continuous-arc construction accounts for unknown f.
    row=dict(training_frequency_Hz=g,training_fit_success=fit['fit_success'],
             validation_amplitude_at_training_frequency=pair(c),
             validation_residual_energy=E,lag_correlations=lag,
             residual_pseudocovariance=pair(np.dot(res,res)/E),
             color_at_training_frequency=dict(low_energy=low*low,high_energy=high*high,
                  low_rank=r,high_rank=s,low_per_rank_over_high_per_rank=(low*low/r)/(high*high/s)))
    row['direction_challenge']={}
    for name,alpha in [('pointwise',.01),('family_1200',.01/1200)]:
        row['direction_challenge'][name]=geo.color_arc_exclusion(valid,g,alpha,q)
    return row


def run(out,cache=None):
    out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();manifest=ROOT/'scripts/cassini_error_direction_inputs.json'
    inp=json.loads(manifest.read_text());cache=cache or ROOT/'outputs/cassini_rsr_inputs'
    for v in inp['products']:
        assert sha(cache/v['filename'])==v['sha256'],v['filename']
    sources=[Path(__file__),HERE/'cassini_error_direction.py',manifest,PROTOCOL/'DEVELOPMENT_PROTOCOL_v1.json',PROTOCOL/'DIRECTION_TEST_PROTOCOL_v1.json']
    freeze={'source_inputs':{str(x.relative_to(ROOT)):sha(x) for x in sources},'raw_inputs':inp['products']}
    (out/'SOURCE_FREEZE_v1.json').write_text(json.dumps(freeze,indent=2)+'\n')
    rows=[];hists={}
    with (out/'DIRECTION_ROWS_v1.jsonl').open('w') as ledger:
        for band,stem,suffix in [('X','c32easc2002_169_1335x54x25d','.1a1'),('Ka','c32easc2002_169_1335x54k25d','.1b1')]:
            fields=schema(cache/('rsr_'+stem+'.lbl'));blob=(cache/(stem+suffix)).read_bytes()
            hist=collections.defaultdict(collections.Counter)
            for j in range(600):
                rec=blob[4260*j:4260*(j+1)];h=header(rec,fields)
                assert h['SFDU SECOND']==48900+j and h['SAMPLE RATE']==1 and h['SAMPLE RESOLUTION']==16
                i,q=decode(rec);z=2*i.astype(float)+1+1j*(2*q.astype(float)+1)
                row=dict(band=band,record_index=j,second=48900+j,iq_sha256=hashlib.sha256(np.column_stack([2*i+1,2*q+1]).astype('>i4').tobytes()).hexdigest(),
                     extremes=int(np.count_nonzero((i==-32768)|(i==32767)|(q==-32768)|(q==32767))),
                     error_count=h['DATA ERROR COUNT'],result=diagnose(z))
                for key in ['FGAIN','FGAIN IF BANDWIDTH','DIG ATTENUATION','TRACKING MODE','DATA ERROR COUNT']:
                    hist[key][str(h[key])]+=1
                rows.append(row);ledger.write(json.dumps(row,sort_keys=True,separators=(',',':'))+'\n');ledger.flush()
            hists[band]={k:dict(v) for k,v in hist.items()}
            print(json.dumps({'band_complete':band,'records':600,'elapsed_seconds':time.monotonic()-start}),flush=True)
    stats={}
    for band in ['X','Ka']:
        rr=[v for v in rows if v['band']==band];res=[v['result'] for v in rr]
        stats[band]=dict(records=len(rr),extreme_records=sum(v['extremes']>0 for v in rr),
            training_failures=sum(not v['training_fit_success'] for v in res),
            training_frequency_Hz=desc([v['training_frequency_Hz'] for v in res]),
            low_over_high_per_rank=desc([v['color_at_training_frequency']['low_per_rank_over_high_per_rank'] for v in res]),
            real_lag1=desc([v['lag_correlations']['1'][0] for v in res]),
            imaginary_lag1=desc([v['lag_correlations']['1'][1] for v in res]),
            real_pseudocovariance=desc([v['residual_pseudocovariance'][0] for v in res]),
            imaginary_pseudocovariance=desc([v['residual_pseudocovariance'][1] for v in res]),
            direction_challenge={k:dict(numerically_excluded=sum(v['direction_challenge'][k]['numerically_excluded'] for v in res),
               no_arc=sum(v['direction_challenge'][k]['arc']['half_width_Hz']>=500 for v in res),
               normalized_minimum_score=desc([v['direction_challenge'][k]['normalized_lower_score'] for v in res if 'normalized_lower_score' in v['direction_challenge'][k]])) for k in ['pointwise','family_1200']})
    final=dict(role='exposed-development conditional error-law diagnostic; no independent empirical test or scalar inference',
               source_freeze_sha256=sha(out/'SOURCE_FREEZE_v1.json'),ledger_sha256=sha(out/'DIRECTION_ROWS_v1.jsonl'),
               headers=hists,statistics=stats,elapsed_seconds=time.monotonic()-start,
               physical_noise_scale_calibrated=False,physical_noise_direction_law_derived=False,
               numerical_status='Real-arithmetic formulas have conservative mesh/ADC margins; floating computations are not outward-rounded interval certificates.',
               independent_empirical_tests=0)
    (out/'DIRECTION_SUMMARY_v1.json').write_text(json.dumps(final,indent=2)+'\n')
    return final


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args()
    print(json.dumps(run(a.output_dir),indent=2))
