#!/usr/bin/env python3
"""All exposed day169 archive counts in quotient space. No phase-history lift.

The archive contains rows extending into day170. All declared rows are kept.
No physical calibration, gravity residual, clipping, or new data exposure.
"""
AUDIT_TIMEOUT_SEC = 180

from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
import gzip,hashlib,io,json,sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import cassini_atdf_decode as tdf
import cassini_odf_decode as odf
from scalar_phase_quotient_controls import centered

M=2**32
META=(3,12,19,24,29,79,84,85,86,87,88)


def rat(x):
    x=F(x);return {'numerator':x.numerator,'denominator':x.denominator,'approximate':float(x)}


def run(input_cache, output_dir):
    OUT=Path(output_dir)
    OUT.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((ROOT/'scripts/cassini_doppler_development_inputs.json').read_text())
    blobs={}
    for key,entry in manifest['inputs'].items():
        b=(Path(input_cache)/entry['filename']).read_bytes()
        assert len(b)==entry['bytes'] and hashlib.sha256(b).hexdigest()==entry['sha256']
        blobs[key]=b
    wanted={1,3,4,5,6,7,8,10,11,12,13,14,19,20,22,23,24,26,29,30,31,32,43,44,79,84,85,86,87,88}
    fields=[f for f in tdf.schema(blobs['tdf_label'].decode()) if f.item in wanted]
    by_endpoint=defaultdict(list);rawflags=Counter();rawcalendar=Counter();rawtypes=Counter()
    for number in range(3,3+160870):
        d=tdf.decode(blobs['tdf'][(number-1)*288:number*288],fields)
        assert d[1]==8;rawcalendar[(d[4],d[5])]+=1;rawtypes[d[12]]+=1
        if d[12] not in (1,2,7,11,12):continue
        rawflags[(d[5],d[19],d[24],d[87])]+=1
        key=(tdf.nominal_seconds(d),d[10],d[11],d[14],d[13])
        phase=F(d[30]*10**14+d[31]*10**7+d[32],10**6)
        ref=F(d[43]*10**9+d[44],10**6)
        state=(phase,ref,d[20],d[22],d[23],d[26])
        by_endpoint[key].append((number,state,tuple(d[j] for j in META)))
    stats=Counter();quality=Counter();uniques={};groups=defaultdict(list);outcomes=Counter();worstM=F(0);worst1=F(0)
    streams=defaultdict(list);rowhash=hashlib.sha256();triphash=hashlib.sha256();allcounts=[]
    # The gzip ledger is deterministic and preserves every accounted interval.
    ledger=OUT/'QUOTIENT_ROWS_v1.jsonl.gz'
    with ledger.open('wb') as raw, gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as gz:
      for number in range(6,6+91863):
        d=odf.decode(blobs['odf'][(number-1)*36:number*36])
        if d['type'] not in (11,12,13):continue
        mid=F(d['time_seconds'])+F(d['time_milliseconds'],1000);dt=F(d['compression_centiseconds'],100)
        a,b=mid-dt/2,mid+dt/2
        rec={'odf_record':number,'type':d['type'],'rx':d['rx'],'tx':d['tx'],'odf_bad':d['bad']}
        if dt<=0 or a.denominator!=1 or b.denominator!=1:
            rec['outcome']='unsupported_grid'
        else:
            tail=(d['rx'],d['down_band'],d['type']-10,d['item15'])
            ends=[by_endpoint.get((int(t),)+tail,[]) for t in (a,b)]
            sets=[{v[1] for v in end} for end in ends]
            if not all(ends):rec['outcome']='missing_endpoint'
            elif any(len(z)!=1 for z in sets):rec['outcome']='ambiguous_counter_state'
            else:
                cs,ce=[next(iter(z)) for z in sets]
                if cs[1:]!=ce[1:] or cs[2:]!=(1000,1,1,5) or d['down_band']!=2:
                    rec['outcome']='outside_registered_receiver_mode'
                else:
                    # The signed difference is used directly. No forward-lift, reset,
                    # monotonicity, or upper-increment assumption enters this algebra.
                    delta=ce[0]-cs[0]
                    y=F(d['observable_integer'])+F(d['observable_fraction_billionths'],10**9)
                    oref=F((d['reference_frequency_high_mHz']<<24)|d['reference_frequency_low_mHz'],1000)
                    known=F(10**6)
                    if d['type']==11:known+=F(880,221)*cs[1]-F(11,3)*oref
                    native=delta-known*dt;stored=y*dt
                    errM=centered(stored-native,M);err1=centered(stored-native)
                    diagnostic_scale=F(2,10**6)+dt*F(1,10**9)
                    if d['type']==11:diagnostic_scale+=dt*(F(11,3000)+F(880,221*10**6))
                    # This scale is only a format-comparison diagnostic inherited from
                    # the registered protocol. It is never a physical error certificate.
                    assert abs(errM)<=diagnostic_scale and abs(err1)<=diagnostic_scale
                    worstM=max(worstM,abs(errM));worst1=max(worst1,abs(err1))
                    flat=[x for end in ends for x in end]
                    nz=any(z[2][META.index(87)]!=0 for z in flat)
                    goodlocked=all(z[2][META.index(19)]==0 and z[2][META.index(24)]==0 for z in flat)
                    stats['matched_endpoint_occurrences']+=len(flat)
                    stats['endpoint_occurrences_nonzero_item87']+=sum(z[2][META.index(87)]!=0 for z in flat)
                    stats['intervals_any_nonzero_item87']+=nz;stats['intervals_good_locked_but_nonzero_item87']+=nz and goodlocked
                    stats['signed_negative_native_counter_differences']+=delta<0
                    stats['duplicate_candidate_intervals']+=any(len(x)>1 for x in ends)
                    for nr,_,meta in flat:quality[meta]+=1;uniques[nr]=meta
                    rec.update(outcome='quotient_reconstructed',left_seconds=int(a),right_seconds=int(b),duration_seconds=str(dt),
                        native_representative_cycles=str(native),stored_representative_cycles=str(stored),
                        error_mod_M_cycles=str(errM),error_mod_one_cycles=str(err1),
                        native_mod_one_cycles=str(centered(native)),any_item87_nonzero=nz,all_item19_item24_zero=goodlocked,
                        endpoint_candidates=[[{'record':nr,'metadata':list(meta)} for nr,_,meta in end] for end in ends])
                    groups[(d['type'],d['rx'],d['tx'])].append((errM,err1,nz,goodlocked))
                    excluded={'time_seconds','time_milliseconds','observable_integer','observable_fraction_billionths','compression_centiseconds','uplink_delay_ns','downlink_delay_ns'}
                    key=tuple((k,d[k]) for k in sorted(d) if k not in excluded)
                    streams[key].append({'record':number,'a':a,'b':b,'dt':dt,'native':native,'stored':stored,'nonzero':nz})
                    allcounts.append(number)
        outcomes[rec['outcome']]+=1
        line=(json.dumps(rec,sort_keys=True,separators=(',',':'))+'\n').encode();rowhash.update(line);gz.write(line)
    triples=0;chaincount=0;neighbors=Counter();strata=defaultdict(Counter);maxtripleerror=F(0);unequal=0
    bins=[F(0),F(1,1000),F(1,100),F(1,10),F(1,4),F(49,100),F(1,2)]
    with (OUT/'QUOTIENT_TRIPLES_v1.jsonl.gz').open('wb') as raw,gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as gz:
      for streamid,(key,rows) in enumerate(sorted(streams.items())):
        rows.sort(key=lambda r:(r['a'],r['b'],r['record']));chains=[];part=[]
        for row in rows:
            if part:
                gap=row['a']-part[-1]['b'];neighbors['adjacent' if gap==0 else ('gap' if gap>0 else 'overlap_or_duplicate')]+=1
                if gap!=0:chains.append(part);part=[]
            part.append(row)
        if part:chains.append(part)
        chaincount+=len(chains)
        for chainid,ch in enumerate(chains):
          for i in range(max(0,len(ch)-2)):
            rr=ch[i:i+3]
            if len({z['dt'] for z in rr})!=1:unequal+=1;continue
            v=[1,-2,1];z=centered(sum(c*x['native'] for c,x in zip(v,rr)));zodf=centered(sum(c*x['stored'] for c,x in zip(v,rr)))
            err=centered(zodf-z);maxtripleerror=max(maxtripleerror,abs(err));flag=any(x['nonzero'] for x in rr)
            bidx=next(j for j,t in enumerate(bins) if abs(z)<=t)
            strata[(streamid,flag)][str(bins[bidx])]+=1;triples+=1
            rec={'stream':streamid,'chain':chainid,'odf_records':[x['record'] for x in rr],'native_third_endpoint_mod_one':str(z),'odf_comparison_mod_one':str(zodf),'comparison_error_cycles':str(err),'any_recorded_slip_diagnostic':flag}
            line=(json.dumps(rec,sort_keys=True,separators=(',',':'))+'\n').encode();triphash.update(line);gz.write(line)
    assert sum(outcomes.values())==91664 and outcomes=={'quotient_reconstructed':91664}
    out={'role':'All-row exposed development quotient consistency; not physical calibration or independent evidence','sources':manifest['inputs'],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'decoder_identities':{str(Path(m.__file__).relative_to(ROOT)):hashlib.sha256(Path(m.__file__).read_bytes()).hexdigest() for m in [tdf,odf]},'raw_calendar_counts':[{'year_mod1900':k[0],'day':k[1],'rows':v} for k,v in sorted(rawcalendar.items())],'raw_sample_types':dict(rawtypes),'raw_doppler_flag_counts':[{'day':k[0],'item19':k[1],'item24':k[2],'item87':k[3],'records':v} for k,v in sorted(rawflags.items())],'outcomes':dict(outcomes),'counts':dict(stats),'unique_matched_endpoint_records':len(uniques),'unique_matched_nonzero_item87':sum(x[META.index(87)]!=0 for x in uniques.values()),'max_abs_error_mod_M_cycles':rat(worstM),'max_abs_error_mod_one_cycles':rat(worst1),'quality_fields':list(META),'endpoint_metadata_occurrences':[{'values':list(k),'occurrences':v} for k,v in sorted(quality.items())],'group_summary':[{'key':list(k),'records':len(v),'any_nonzero_item87':sum(x[2] for x in v),'good_locked_and_nonzero':sum(x[2] and x[3] for x in v),'max_error_cycles':rat(max(abs(x[0]) for x in v))} for k,v in sorted(groups.items())],'chains':chaincount,'streams':len(streams),'neighbor_counts':dict(neighbors),'equal_duration_triples':triples,'unequal_duration_triples_retained_as_unsupported':unequal,'max_abs_triple_format_difference_cycles':rat(maxtripleerror),'third_difference_bins_upper_abs_cycles':[str(z) for z in bins],'third_difference_strata':[{'stream':k[0],'any_nonzero_item87':k[1],'bin_counts':dict(v)} for k,v in sorted(strata.items())],'ledgers':{'rows':{'path':'QUOTIENT_ROWS_v1.jsonl.gz','uncompressed_sha256':rowhash.hexdigest()},'triples':{'path':'QUOTIENT_TRIPLES_v1.jsonl.gz','uncompressed_sha256':triphash.hexdigest()}},'scope':['No forward phase-history lift is computed or selected.','No quality or slip flag is used to discard a row.','Modulo agreement checks dependent archive products only.','Third endpoint differences still include physical orbit, clock, medium and electronics. They are not scalar residuals.','No actual scalar energy or physical error budget is inferred.','No new raw empirical file was opened.']}
    for x in out['ledgers'].values():x['compressed_sha256']=hashlib.sha256((OUT/x['path']).read_bytes()).hexdigest();x['compressed_bytes']=(OUT/x['path']).stat().st_size
    (OUT/'QUOTIENT_DEVELOPMENT_RESULTS_v1.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['outcomes','counts','unique_matched_endpoint_records','unique_matched_nonzero_item87','max_abs_error_mod_M_cycles','max_abs_error_mod_one_cycles','chains','streams','equal_duration_triples','max_abs_triple_format_difference_cycles','ledgers']},indent=2))
    return out


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--input-cache',type=Path,default=ROOT/'outputs/cassini_doppler_inputs')
    parser.add_argument('--output-dir',type=Path,default=ROOT/'outputs/scalar_phase_quotient')
    args=parser.parse_args()
    run(args.input_cache,args.output_dir)
