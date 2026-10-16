"""Protocol-bound RSR development decoder; no physical carrier-noise claim."""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import argparse, collections, gzip, hashlib, io, json, math, re, struct
import numpy as np

def digest(data): return hashlib.sha256(data).hexdigest()

def schema(label):
    text=Path(label).read_text()
    blocks=re.findall(r'(?m)^  OBJECT\s*= COLUMN\n(.*?)^  END_OBJECT\s*= COLUMN',text,re.S)
    fields=[]
    for b in blocks:
        fields.append((re.search(r'NAME\s*= "([^"]*)"',b)[1],
                       int(re.search(r'START_BYTE\s*= (\d+)',b)[1])-1,
                       int(re.search(r'BYTES\s*= (\d+)',b)[1]),
                       re.search(r'DATA_TYPE\s*= (\w+)',b)[1]))
    return fields

def header(record,fields):
    d={}
    for name,offset,size,typ in fields:
        if name=='SAMPLE WORDS':continue
        raw=record[offset:offset+size]
        if typ=='IEEE_REAL': value=struct.unpack('>d',raw)[0]
        elif typ=='CHARACTER': value=raw.decode('ascii')
        else:value=int.from_bytes(raw,'big',signed=typ=='MSB_INTEGER')
        d[name]=value
    return d

def decode(record,bits):
    if bits not in (1,2,4,8,16):raise ValueError('unsupported documented sample width')
    words=np.frombuffer(record,dtype='>u4',offset=260).astype(np.uint32)
    shifts=np.arange(16//bits,dtype=np.uint32)*bits
    mask=(1<<bits)-1
    i=((words[:,None]>>shifts)&mask).reshape(-1).astype(np.int32)
    q=(((words[:,None]>>16)>>shifts)&mask).reshape(-1).astype(np.int32)
    sign=1<<(bits-1)
    i[i>=sign]-=1<<bits;q[q>=sign]-=1<<bits
    return i,q

def phase_cell(i,q,bits):
    # This describes an assumed unsaturated ideal quantizer cell, NOT carrier error.
    x=(2*i+1).astype(np.float64);y=(2*q+1).astype(np.float64)
    n2=x*x+y*y
    clipped=(i==-(1<<(bits-1)))|(i==(1<<(bits-1))-1)|(q==-(1<<(bits-1)))|(q==(1<<(bits-1))-1)
    # Origin-reaching cells cannot be assigned the simple arc; retain them as invalid.
    bad=clipped|(n2<=2)
    low=np.full(x.shape,np.inf);high=np.full(x.shape,-np.inf)
    for dx in (-1,1):
        for dy in (-1,1):
            angle=np.arctan2(x*dy-y*dx,n2+x*dx+y*dy)/(2*np.pi)
            low=np.minimum(low,angle);high=np.maximum(high,angle)
    low[bad]=np.nan;high[bad]=np.nan
    return x+1j*y,low,high,{'extreme_code':clipped,'origin_reaching':n2<=2}

def character(zx,zk):
    if np.any(np.abs(zx)==0) or np.any(np.abs(zk)==0):
        raise ValueError('complex phase requires nonzero voltages')
    return (zx/np.abs(zx))**19*np.conj(zk/np.abs(zk))**5

def character_interval(lx,hx,lk,hk):
    return 19*lx-5*hk,19*hx-5*lk

def describe(x):
    a=np.asarray(x);a=a[np.isfinite(a)]
    return {'finite':len(a),'quantiles_0_01_50_99_100':np.quantile(a,[0,.01,.5,.99,1]).tolist() if len(a) else []}

def read_product(file,label,out):
    data=Path(file).read_bytes();size=4260
    if len(data)%size:raise ValueError('partial record')
    fields=schema(label);assert len(fields)==72
    window={};all_heads=[];counter=collections.defaultdict(collections.Counter)
    with out.open('wb') as binary, gzip.GzipFile(filename='', mode='wb', fileobj=binary, mtime=0) as zipped, io.TextIOWrapper(zipped,encoding='utf-8') as dump:
        for j in range(len(data)//size):
            record=data[j*size:(j+1)*size];h=header(record,fields)
            h['record_index']=j;dump.write(json.dumps(h,sort_keys=True)+'\n');all_heads.append(h)
            for key in ('DATA ERROR COUNT','SAMPLE RESOLUTION','SAMPLE RATE','UPLINK FREQUENCY BAND','DOWNLINK FREQUENCY BAND','DEEP SPACE STATION','TRACKING MODE','PREDICTS TIME SHIFT','FROV FLAG'):
                counter[key][str(h[key])]+=1
            t=h['SFDU SECOND']
            if h['SFDU YEAR']==2002 and h['SFDU DAY OF YEAR']==169 and 48900<=t<49500:
                key=(h['SFDU YEAR'],h['SFDU DAY OF YEAR'],t,h['DEEP SPACE STATION'],h['UPLINK FREQUENCY BAND'])
                if key in window:raise ValueError('duplicate timestamp; no silent selection')
                bits=h['SAMPLE RESOLUTION'];i,q=decode(record,bits)
                if len(i)!=h['SAMPLE RATE']*1000:raise ValueError('sample payload/rate mismatch')
                z,lo,hi,flags=phase_cell(i,q,bits)
                corrected=np.column_stack((2*i+1,2*q+1)).astype('>i4')
                window[key]={'h':h,'i':i,'q':q,'z':z,'lo':lo,'hi':hi,'flags':flags,'iq_sha256':digest(corrected.tobytes())}
    times=np.array([h['SFDU SECOND'] for h in all_heads]);delta=np.diff(times)
    return window,{'file':str(file),'sha256':digest(data),'record_count':len(all_heads),'first_second':float(times[0]),'last_second':float(times[-1]),'nonunit_time_steps':[{'index':int(j),'step':float(delta[j])} for j in np.flatnonzero(delta!=1)],'histograms':{k:dict(v) for k,v in counter.items()},'headers_file':str(out),'headers_sha256':digest(out.read_bytes()),'window_records':len(window)}

def controls():
    # A hand-built two-word fixture checks signed widths, channel order and packed time order.
    counts=0
    for bits in (1,2,4,8,16):
        n=16//bits;lo=-(1<<(bits-1));hi=(1<<(bits-1))-1
        iv=[lo,hi]*n;qv=[hi,lo]*n;words=[]
        for j in range(2):
            iw=sum((iv[j*n+t]&((1<<bits)-1))<<(bits*t) for t in range(n))
            qw=sum((qv[j*n+t]&((1<<bits)-1))<<(bits*t) for t in range(n))
            words.append((qw<<16)|iw)
        rec=b'\0'*260+struct.pack('>2I',*words);i,q=decode(rec,bits)
        assert i.tolist()==iv[:2*n] and q.tolist()==qv[:2*n];counts+=1
    # Negative-axis branch and nonzero-domain fixture from independent source review.
    z,lo,hi,flags=phase_cell(np.array([-2]),np.array([-1]),16)
    assert abs(lo[0]+math.atan(1/3)/(2*math.pi))<1e-15
    assert abs(hi[0]-math.atan(1/2)/(2*math.pi))<1e-15;counts+=1
    _,lo,_,_=phase_cell(np.array([32767,0]),np.array([4,0]),16)
    assert np.isnan(lo).all();counts+=1
    theta=np.array([0,np.pi/10])
    x=np.exp(5j*theta);k=np.exp(19j*theta)
    assert np.max(np.abs(character(x,k)-1))<1e-12;counts+=1
    assert abs(character(np.array([x.mean()]),np.array([k.mean()]))[0]+1)<1e-12;counts+=1
    low,high=character_interval(np.array([-.1]),np.array([.2]),np.array([-.3]),np.array([.4]))
    assert abs(low[0]+3.9)<1e-12 and abs(high[0]-5.3)<1e-12;counts+=1
    return counts

def run(rawdir,metadir,outdir):
    outdir.mkdir(exist_ok=True)
    expected={
      rawdir/'c32easc2002_169_1335x54x25d.1a1':'28af13233a64f7629b794cc8beaad0db2500fb09cc421cda3e82544144235a92',
      rawdir/'c32easc2002_169_1335x54k25d.1b1':'9544e294be8867cb013b3d96891a413f5dddc3d5e0236e8a2b9331fe7d45a19e',
      metadir/'rsr_c32easc2002_169_1335x54x25d.lbl':'36ab671cbb83c7d04060c2a19058800a4fc50f780aa8fa6e9f77ed3089046382',
      metadir/'rsr_c32easc2002_169_1335x54k25d.lbl':'2349b0473986f5247650fc88a5bbaf7e859786e22253b38f4a8719af3dd0c697'}
    for path,sha in expected.items():
        if digest(path.read_bytes())!=sha:raise ValueError('registered source mismatch: '+str(path))
    xp='c32easc2002_169_1335x54x25d';kp='c32easc2002_169_1335x54k25d'
    wx,sx=read_product(rawdir/(xp+'.1a1'),metadir/('rsr_'+xp+'.lbl'),outdir/'X_HEADERS_v1.jsonl.gz')
    wk,sk=read_product(rawdir/(kp+'.1b1'),metadir/('rsr_'+kp+'.lbl'),outdir/'KA_HEADERS_v1.jsonl.gz')
    keys=sorted(wx.keys()&wk.keys());char=[];lower=[];upper=[];ampx=[];ampk=[];times=[];digests=[];flags=collections.Counter();nco=[]
    for key in keys:
        x,k=wx[key],wk[key];hx,hk=x['h'],k['h']
        if (hx['SAMPLE RATE'],hx['SAMPLE RESOLUTION'])!=(hk['SAMPLE RATE'],hk['SAMPLE RESOLUTION']):raise ValueError('unequal grid: no implicit resampling')
        if hx['SAMPLE RATE']!=1:raise ValueError('this registered lag diagnostic requires the documented1kSPS grid')
        zx,zk=x['z'],k['z'];assert np.all(np.abs(zx)>0) and np.all(np.abs(zk)>0)
        ch=character(zx,zk)
        low,high=character_interval(x['lo'],x['hi'],k['lo'],k['hi'])
        char.extend(ch);lower.extend(low);upper.extend(high)
        ampx.extend(np.abs(zx));ampk.extend(np.abs(zk));times.extend(key[2]+np.arange(len(zx))/(1000*hx['SAMPLE RATE']))
        for band,row in [('X',x),('Ka',k)]:
            for f,v in row['flags'].items():flags[band+'_'+f]+=int(v.sum())
        digests.append({'key':key,'X_corrected_iq_sha256':x['iq_sha256'],'Ka_corrected_iq_sha256':k['iq_sha256'],'X_error_count':hx['DATA ERROR COUNT'],'Ka_error_count':hk['DATA ERROR COUNT']})
        # These are documented nominal frequency and derivative identities only.
        r={}
        for band,h in [('X',hx),('Ka',hk)]:
            f=[h['SUB-CHANNEL FREQUENCY COEF F'+str(j)] for j in range(1,4)]
            pp=[h['SUB-CHANNEL PHASE COEF P'+str(j)] for j in range(1,5)]
            r[band]={'F':f,'P':pp,'phase_derivative_discrepancy':[pp[1]-f[0],2*pp[2]-f[1],3*pp[3]-f[2]],'nominal_LO_Hz':(h['DDC LO FREQUENCY']+h['RF-IF LO FREQUENCY'])*10**6,'RF_POINT_1':h['RF POINT 1'],'nominal_sky_at_polynomial_zero':(h['DDC LO FREQUENCY']+h['RF-IF LO FREQUENCY'])*10**6-f[0]}
        nco.append(r)
    char=np.array(char);times=np.array(times);lower=np.array(lower);upper=np.array(upper)
    full=upper-lower>=1
    lags={}
    for n in (1,1000):
        valid=np.isclose(times[n:]-times[:-n],n/1000,rtol=0,atol=1e-9)
        diff=char[n:]*np.conj(char[:-n]);values=np.angle(diff[valid])/(2*np.pi)
        lags[str(n)]={'sample_pairs':int(valid.sum()),'excluded_nonmatching_time_pairs':int((~valid).sum()),'raw_baseband_phase_difference_cycles':describe(values),'circular_mean_magnitude':float(abs(diff[valid].mean())) if valid.any() else None}
    result={'role':'exposed development; raw baseband nuisance diagnostic only','products':[sx,sk],
       'matched_window_records':len(keys),'X_unmatched_keys':sorted(wx.keys()-wk.keys()),'Ka_unmatched_keys':sorted(wk.keys()-wx.keys()),
       'sample_count':len(char),'character':[19,-5],'physical_sky_phase_restored':False,
       'ADC_cell_premise':'ideal unsaturated midrise square after2k+1; not proven by file-format correction alone; total analog voltage not carrier','flags':dict(flags),
       'X_corrected_amplitude':describe(ampx),'Ka_corrected_amplitude':describe(ampk),
       'character_ADC_lower_error_cycles':describe(lower),'character_ADC_upper_error_cycles':describe(upper),
       'character_ADC_width_cycles':describe(upper-lower),'ADC_complete_circle_count':int(full.sum()),'ADC_invalid_cell_count':int(np.count_nonzero(~np.isfinite(lower+upper))),
       'baseband_lags':lags,'decoder_controls':controls(),'independent_empirical_tests':0,
       'no_claim':'No physical noise floor, gravity residual, field state, action or scale is inferred. All raw files now exposed development; no sample clipping by flags or results.'}
    (outdir/'RSR_DEVELOPMENT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    (outdir/'RSR_WINDOW_DIGESTS_v1.json').write_text(json.dumps(digests,indent=2)+'\n')
    (outdir/'RSR_NCO_DIAGNOSTIC_v1.json').write_text(json.dumps(nco,indent=2)+'\n')
    np.savez_compressed(outdir/'RSR_CHARACTER_v1.npz',times=times,character=char,lower=lower,upper=upper)
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--rawdir',type=Path,required=True);ap.add_argument('--metadir',type=Path,required=True);ap.add_argument('--outdir',type=Path,required=True)
    a=ap.parse_args();run(a.rawdir,a.metadir,a.outdir)
