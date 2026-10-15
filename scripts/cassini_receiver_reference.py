"""Compare predeclared RSR candidates with exposed pre-NSP count products."""
from pathlib import Path
from fractions import Fraction as Q
import collections,datetime,hashlib,json,sys
import numpy as np
AUDIT_TIMEOUT_SEC = 180
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
import cassini_odf_decode as odf
import cassini_atdf_decode as atdf
import cassini_atdf_odf_reconcile as count

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rat(q):return dict(numerator=q.numerator,denominator=q.denominator,approximate=float(q))
def nco_increment(row,delta):
    # Use the declared archived phase coefficients, not a rational identity
    # inferred from separately rounded frequency coefficients.
    p1,p2,p3,p4=map(Q,row['nco_P'])
    return p2+p3*(1+2*delta)+p4*(1+3*delta+3*delta*delta)
def run(cache,out,protocol_dir):
    here=protocol_dir
    estimates=[json.loads(s) for s in (out/'CARRIER_ESTIMATES_v1.jsonl').read_text().splitlines()]
    bysec={r['second']:r for r in estimates if r['band']=='X'}
    manifest=json.loads((ROOT/'scripts/cassini_doppler_development_inputs.json').read_text())
    blobs={}
    for k,v in manifest['inputs'].items():
        p=cache/v['filename'];assert sha(p)==v['sha256'];blobs[k]=p.read_bytes()
    epoch=int((datetime.datetime(2002,6,18)-datetime.datetime(1950,1,1)).total_seconds())
    # All source variants at each endpoint remain in the row ledger.
    wanted={1,4,5,6,7,8,10,11,12,13,14,19,20,22,23,26,27,28,29,30,31,32,43,44,79,87}
    fields=[f for f in atdf.schema(blobs['tdf_label'].decode('ascii')) if f.item in wanted]
    idx=collections.defaultdict(list)
    for n in range(3,3+160870):
        d=atdf.decode(blobs['tdf'][(n-1)*288:n*288],fields)
        if d[1]!=8:raise ValueError('wrong tracking format')
        sec=atdf.nominal_seconds(d)-epoch
        if 48900<=sec<=49500 and d[10]==25 and d[11]==2 and d[14]==3:
            idx[(sec,d[13])].append((n,d))
    rows=[]
    for n in range(6,6+91863):
        d=odf.decode(blobs['odf'][(n-1)*36:n*36]);mid=Q(d['time_seconds']-epoch)+Q(d['time_milliseconds'],1000)
        duration=Q(d['compression_centiseconds'],100);start=mid-duration/2;end=mid+duration/2
        if not(d['type'] in (12,13) and d['rx']==25 and d['tx']==54 and d['down_band']==2 and 48900<=start<end<=49500):continue
        assert duration==1 and start.denominator==end.denominator==1
        low=idx[(int(start),d['item15'])];high=idx[(int(end),d['item15'])]
        states=[set(count.conversion_state(v) for _,v in side) for side in (low,high)]
        assert len(states[0])==len(states[1])==1
        l,h=next(iter(states[0])),next(iter(states[1]));assert l[1]==h[1]
        assert all(v[26]==5 and v[20]==1000 and v[22]==1 and v[23]==1 for side in (low,high) for _,v in side)
        stored_ref=Q((d['reference_frequency_high_mHz']<<24)|d['reference_frequency_low_mHz'],1000)
        assert stored_ref==l[1] and d['exciter_band']==1
        reference=Q(880,221)*stored_ref
        doppler=Q(d['observable_integer'])+Q(d['observable_fraction_billionths'],10**9)
        increment,wraps=count.forward_lift(l[0],h[0]);doppler_count=Q(increment,10**6)/duration-10**6
        sky=reference-doppler;raw_sky=reference-doppler_count;r=bysec[int(start)]
        modes=[]
        for delta in [Q(0),Q(1,2000)]:
            # GHz subtraction is exact. Only the fitted residual frequency is floating.
            nominal=Q(r['nominal_LO_Hz'])-nco_increment(r,delta)
            nominal_difference=nominal-sky
            for sign in [-1,1]:
                err=float(nominal_difference)+sign*r['estimate']['frequency_Hz']
                modes.append(dict(phase_delta_seconds=rat(delta),spectral_sign=sign,
                                  nominal_RSR_minus_count_sky_Hz=rat(nominal_difference),
                                  RSR_minus_count_sky_Hz=err))
        rows.append(dict(odf_record=n,odf=d,start_second=int(start),end_second=int(end),
                         atdf_endpoint_variants=[[dict(record=j,fields=v) for j,v in s] for s in (low,high)],
                         stored_reference_Hz=rat(stored_ref),X_reference_Hz=rat(reference),
                         ODF_mean_received_sky_Hz=rat(sky),ATDF_mean_received_sky_Hz=rat(raw_sky),
                         ODF_minus_ATDF_sky_Hz=rat(sky-raw_sky),conditional_count_wraps=wraps,
                         RSR_baseband_estimate_Hz=r['estimate']['frequency_Hz'],candidates=modes))
    assert len(rows)==600 and len({r['start_second'] for r in rows})==600
    path=out/'REFERENCE_COMPARISON_ROWS_v1.jsonl';path.write_text(''.join(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n' for r in rows))
    summary={}
    for k in range(4):
        vals=np.array([r['candidates'][k]['RSR_minus_count_sky_Hz'] for r in rows]);v=rows[0]['candidates'][k]
        summary[str(k)]={'spectral_sign':v['spectral_sign'],'phase_delta_seconds':v['phase_delta_seconds'],
                        'min_median_max_Hz':np.quantile(vals,[0,.5,1]).tolist(),'mean_Hz':float(vals.mean()),
                        'RMS_Hz':float(np.sqrt(np.mean(vals*vals)))}
    result=dict(role='exposed cross-receiver development comparison under historical conversion and local carrier assumptions',
                source_sha256=sha(Path(__file__)),frozen_candidate_sha256=sha(here/'REFERENCE_COMPARISON_FREEZE_v1.json'),
                estimator_ledger_sha256=sha(out/'CARRIER_ESTIMATES_v1.jsonl'),comparison_ledger_sha256=sha(path),
                matched_intervals=len(rows),ODF_bad_count=sum(r['odf']['bad'] for r in rows),
                ATDF_endpoint_nonzero_slip_diagnostics=sum(v['fields'][87]!=0 for r in rows for side in r['atdf_endpoint_variants'] for v in side),
                stored_reference_Hz=rows[0]['stored_reference_Hz'],X_reference_Hz=rows[0]['X_reference_Hz'],
                maximum_ODF_ATDF_sky_difference_Hz=max(abs(r['ODF_minus_ATDF_sky_Hz']['approximate']) for r in rows),
                candidates=summary,fitted_biases=0,fitted_timeshifts=0,independent_empirical_gravity_tests=0,
                limit='No comparison RMS is a certified physical carrier error. Later-RSR complex sign is supported by an external convention, and this is a development consistency check. Timing ambiguity and calibration remain open.')
    (out/'REFERENCE_COMPARISON_SUMMARY_v1.json').write_text(json.dumps(result,indent=2)+'\n');return result
if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--input-cache',type=Path,required=True);ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--protocol-dir',type=Path,required=True)
    a=ap.parse_args();print(json.dumps(run(a.input_cache,a.output_dir,a.protocol_dir),indent=2))
