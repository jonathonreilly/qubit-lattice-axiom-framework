#!/usr/bin/env python3
"""Nominal count-window geometry of already-exposed day169 development ODF.
No physical residual, energy estimate, holdout, clipping, or parameter fit.
"""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict,Counter
import hashlib,json,re,struct,sys
import cassini_odf_decode as odf

AUDIT_TIMEOUT_SEC = 240

def interval(row):
    center=1000*row['time_seconds']+row['time_milliseconds'];duration=10*row['compression_centiseconds']
    return 2*center-duration,2*center+duration

def runs(rows):
    ordered=sorted(rows,key=lambda r:(r['left_2ms'],r['right_2ms'],r['record']))
    chains=[];edges=Counter();part=[]
    for r in ordered:
        if part:
            delta=r['left_2ms']-part[-1]['right_2ms']
            tag='adjacent' if delta==0 else ('gap' if delta>0 else 'overlap_or_duplicate')
            edges[tag]+=1
            if delta!=0:chains.append(part);part=[]
        part.append(r)
    if part:chains.append(part)
    return chains,edges

def rational(q):return {'numerator':q.numerator,'denominator':q.denominator,'approximate':float(q)}

def weighted_moments(ds,ys):
    s0=sum(ds);s1=sum(d*y for d,y in zip(ds,ys));s2=sum(d*y*y for d,y in zip(ds,ys))
    return Fraction(s1,s0*10**9),Fraction(s0*s2-s1*s1,s0*100*10**18)

def selfcheck():
    mock=[{'left_2ms':a,'right_2ms':b,'record':i} for i,(a,b) in enumerate([(0,2),(2,4),(6,8),(6,8),(8,10)])]
    ch,ed=runs(mock[::-1]);assert [len(x) for x in ch]==[2,1,2] and dict(ed)=={'adjacent':2,'gap':1,'overlap_or_duplicate':1}
    assert interval({'time_seconds':100,'time_milliseconds':250,'compression_centiseconds':50})==(200000,201000)
    for ds,ys in [([50,150],[10**20+3,10**20-7]),([20,90,300],[-7,11,19]),([100],[1234567890123456789])]:
        mean,var=weighted_moments(ds,ys)
        centered=sum(Fraction(d,100)*(Fraction(y,10**9)-mean)**2 for d,y in zip(ds,ys))
        assert var==centered
        shifted_mean,shifted_var=weighted_moments(ds,[y+10**24 for y in ys])
        assert shifted_var==var and shifted_mean-mean==10**15
    return {'partition_with_gap_duplicate_and_reversed_input':True,'exact_interval_midpoint':True,'large_offset_centered_moment':True,'unequal_duration_centered_moment':True,'singleton_centered_moment':True}

def run_checks(input_paths,output_dir,manifest):
    protocol=manifest;blobs={}
    for key,entry in protocol['inputs'].items():
        blob=Path(input_paths[key]).read_bytes();assert len(blob)==entry['bytes'] and hashlib.sha256(blob).hexdigest()==entry['sha256'];blobs[key]=blob
    label=blobs['odf_label'].decode('ascii');data=blobs['odf'];first=int(re.search(r'^\^ODF3C_TABLE\s*=\s*\("[^\"]+",(\d+)\)',label,re.M).group(1))
    obj=re.search(r'^OBJECT\s*=\s*ODF3C_TABLE\s*$(.*?)^END_OBJECT\s*=\s*ODF3C_TABLE',label,re.M|re.S).group(1);count=int(re.search(r'^\s*ROWS\s*=\s*(\d+)',obj,re.M).group(1));assert count==91863 and first==6
    assert struct.unpack('>i',data[(first-2)*36:(first-2)*36+4])[0]==109
    excluded={'time_seconds','time_milliseconds','observable_integer','observable_fraction_billionths','compression_centiseconds','uplink_delay_ns','downlink_delay_ns'}
    streams=defaultdict(list);types=Counter();unsupported=[]
    for number in range(first,first+count):
        row=odf.decode(data[(number-1)*36:number*36]);types[row['type']]+=1
        if row['type'] not in [11,12,13]:continue
        if row['compression_centiseconds']<=0:unsupported.append({'record':number,'reason':'nonpositive_duration'});continue
        keys=tuple(sorted(k for k in row if k not in excluded));key=tuple(row[k] for k in keys)
        a,b=interval(row);streams[key].append({'record':number,'left_2ms':a,'right_2ms':b,'duration_cs':row['compression_centiseconds'],'observable_nhz':row['observable_integer']*10**9+row['observable_fraction_billionths'],'up_delay_ns':row['uplink_delay_ns'],'down_delay_ns':row['downlink_delay_ns']})
    output=Path(output_dir)/'count_window_chains.jsonl';groups=[];total=0;chain_count=0;durations=Counter()
    with output.open('w') as f:
     for index,(key,rows) in enumerate(sorted(streams.items())):
        chains,edges=runs(rows);lengths=Counter();dat={k:v for k,v in zip(keys,key)}
        for j,ch in enumerate(chains):
            lengths[len(ch)]+=1;chain_count+=1;total+=len(ch)
            ds=[r['duration_cs'] for r in ch];ys=[r['observable_nhz'] for r in ch];durations.update(ds)
            s0=sum(ds);mean,var=weighted_moments(ds,ys);assert var>=0
            T=[d/100 for d in ds];H=[(a+b)/2 for a,b in zip(T[:-1],T[1:])]
            diag=[(1/a+1/b)/(h*h) for a,b,h in zip(T[:-1],T[1:],H)]
            off=[-1/(H[i]*H[i+1]*T[i+1]) for i in range(max(0,len(H)-1))]
            rec={'stream':index,'chain':j,'configuration':dat,'records':len(ch),'first_odf_record':ch[0]['record'],'last_odf_record':ch[-1]['record'],'left_2ms':ch[0]['left_2ms'],'right_2ms':ch[-1]['right_2ms'],'duration_seconds':rational(Fraction(s0,100)),'duration_cs_counts':dict(Counter(ds)),'raw_frequency_weighted_variance_hz2_s':rational(var),'raw_mean_frequency_hz':rational(mean),'gram_6pi_diagonal_range':([min(diag),max(diag)] if diag else []),'gram_6pi_offdiagonal_range':([min(off),max(off)] if off else []),'delay_changes':sum((a['up_delay_ns'],a['down_delay_ns'])!=(b['up_delay_ns'],b['down_delay_ns']) for a,b in zip(ch[:-1],ch[1:])),'interpretation':'descriptive raw frequency moment and nominal timing geometry only; no physical field energy or calibrated residual'}
            f.write(json.dumps(rec)+'\n')
        groups.append({'stream':index,'configuration':dat,'records':len(rows),'chains':len(chains),'chain_lengths':dict(sorted(lengths.items())),'sorted_neighbor_relations':dict(edges),'source_order_time_decreases':sum(b['left_2ms']<a['left_2ms'] for a,b in zip(rows[:-1],rows[1:]))})
    assert total+len(unsupported)==91664
    result={'role':protocol['role'],'self_checks':selfcheck(),'inputs':protocol['inputs'],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'decoder_sha256':hashlib.sha256(Path(odf.__file__).read_bytes()).hexdigest(),'orbit_records':count,'type_counts':dict(types),'doppler_records_accounted':total+len(unsupported),'unsupported':unsupported,'streams':len(streams),'chains':chain_count,'duration_cs_counts':dict(sorted(durations.items())),'groups':groups,'full_chain_ledger':output.name,'full_chain_ledger_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'physical_energy_inferences':0,'physical_residual_fits':0,'new_raw_products_opened':0,'limits':['Nominal archive time is not a derived physical clock map.','Reference, configuration and validity strata are retained; no values are clipped.','Overlaps and gaps break this strictly adjacent-chain construction and remain counted.','Raw frequency weighted variance is neither scalar energy nor a gravity residual.','Different chains or stations are not assumed independent or pooled into an energy.']}
    return result
