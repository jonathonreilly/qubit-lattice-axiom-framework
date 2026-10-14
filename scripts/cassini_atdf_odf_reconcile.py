#!/usr/bin/env python3
"""Reconstruct stored ODF Doppler from registered development ATDF counters.

Version1 remains the failed literal-label route. PDS tdf_unpack Appendix B
corrects the count scaling. The forward modulo lift is CONDITIONAL on a
nonnegative increment smaller than 2**32 cycles, without a counter reset.
Endpoint observations alone do not derive this bounded-history condition.
No orbit, gravitational parameter, clipping rule, or fitted constant appears.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from cassini_atdf_decode import schema, decode as tdecode, nominal_seconds
from cassini_odf_decode import decode as odecode

AUDIT_TIMEOUT_SEC = 120
MODULUS_MICROCYCLES = 2**32 * 10**6
IDENTITIES = {
    'tdf': '215c2de473fd00b278267ab3ff0431ab4d00e9c3baaa17e949105b964644f4f3',
    'odf': '39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f',
    'tdf_label': '5c62b58cd56585b8ab2b518ca915e3ec7b8ccdc887de36b07ebabd09d496b5d6'}
MODE_FIELDS = (12, 19, 20, 22, 23, 26, 27, 28, 29, 79, 87)


def count_microcycles(d):
    # Corrected PDS guide, Table5 and Appendix B(3), not the erroneous label.
    return d[30]*10**14 + d[31]*10**7 + d[32]


def forward_lift(a, b):
    """Unique lift only within 0 <= increment < modulus, with no reset."""
    if not (0 <= a < MODULUS_MICROCYCLES and 0 <= b < MODULUS_MICROCYCLES):
        raise ValueError('counter outside unsigned 32-cycle-bit domain')
    wraps = int(b < a)
    return b-a+wraps*MODULUS_MICROCYCLES, wraps


def reference(d):
    return Q(d[43]*10**9+d[44], 10**6)


def conversion_state(d):
    # Quality and low/high-rate variants are retained separately, not clipped.
    # Equality here only means the stored observable is value-identifiable.
    return (count_microcycles(d), reference(d), d[20], d[22], d[23], d[26])


def reconstruct(cycles, duration, kind, receiver_reference, spacecraft_reference):
    if duration <= 0 or kind not in (11, 12, 13):
        raise ValueError('unsupported interval or type')
    value = cycles/duration - 10**6
    if kind == 11:
        value -= Q(880, 221)*receiver_reference - Q(11, 3)*spacecraft_reference
    return value


def rational(value):
    value = Q(value)
    return dict(numerator=value.numerator, denominator=value.denominator,
                approximate=float(value))


def controls():
    cs = {}
    def check(name, value):
        cs[name] = bool(value)
        if not value:
            raise AssertionError(name)
    check('published_pds_count_example',
          count_microcycles({30:16, 31:4398198, 32:1475000}) == 1643981981475000)
    check('high_part_carry', count_microcycles({30:1,31:0,32:0}) -
          count_microcycles({30:0,31:9999999,32:9999999}) == 1)
    check('ordinary_lift', forward_lift(11, 37) == (26, 0))
    check('rollover_lift', forward_lift(MODULUS_MICROCYCLES-11, 37) == (48, 1))
    check('extra_full_turn_unidentifiable',
          (37 + MODULUS_MICROCYCLES) % MODULUS_MICROCYCLES == 37)
    for name, pair in [('negative_counter', (-1, 0)),
                       ('out_of_range_counter', (0, MODULUS_MICROCYCLES))]:
        try:
            forward_lift(*pair)
        except ValueError:
            check(name, True)
        else:
            check(name, False)
    check('coherent_known_count', reconstruct(Q(3000007,2),Q(3,2),12,0,0)==Q(7,3))
    check('oneway_reference_sign', reconstruct(Q(10**6),Q(1),11,Q(221),Q(3))==-869)
    try:
        reconstruct(1, Q(0), 12, 0, 0)
    except ValueError:
        check('nonpositive_interval_rejected', True)
    else:
        check('nonpositive_interval_rejected', False)
    return cs


def main():
    ap = argparse.ArgumentParser()
    for name in ('tdf','odf','tdf-label','output','rows-output'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    checks, blobs = controls(), {}
    for name, digest in IDENTITIES.items():
        blob = getattr(args, name).read_bytes()
        if hashlib.sha256(blob).hexdigest() != digest:
            raise ValueError('unregistered input '+name)
        blobs[name] = blob
    wanted = {1,4,5,6,7,8,10,11,12,13,14,19,20,22,23,26,27,28,29,30,31,32,43,44,79,87}
    fields = [f for f in schema(blobs['tdf_label'].decode('ascii')) if f.item in wanted]
    index = defaultdict(list)
    tracking_samples = 0
    for number in range(3,3+160870):
        d = tdecode(blobs['tdf'][(number-1)*288:number*288], fields)
        if d[1] != 8:
            raise ValueError('unsupported ATDF format')
        if d[12] not in (1,2,7,11,12):
            continue
        key = (nominal_seconds(d), d[10], d[11], d[14], d[13])
        index[key].append((number,d))
        tracking_samples += 1
    outcomes, counters, quality = Counter(), Counter(), Counter()
    groups = defaultdict(list)
    examples = []
    row_hash = hashlib.sha256()
    args.rows_output.parent.mkdir(parents=True,exist_ok=True)
    with args.rows_output.open('w') as rows:
        for number in range(6,6+91863):
            d = odecode(blobs['odf'][(number-1)*36:number*36])
            if d['type'] not in (11,12,13):
                continue
            mid = Q(d['time_seconds']) + Q(d['time_milliseconds'],1000)
            duration = Q(d['compression_centiseconds'],100)
            start,end = mid-duration/2,mid+duration/2
            rec = dict(odf_record=number,type=d['type'],rx=d['rx'],tx=d['tx'],odf_bad=d['bad'])
            if duration <= 0 or start.denominator != 1 or end.denominator != 1:
                rec['outcome'] = 'unsupported_endpoint_grid'
            else:
                tail = (d['rx'],d['down_band'],d['type']-10,d['item15'])
                low = index.get((int(start),)+tail,[])
                high = index.get((int(end),)+tail,[])
                rec['tdf_candidates'] = [[n for n,_ in side] for side in (low,high)]
                states = [set(conversion_state(z) for _,z in side) for side in (low,high)]
                if not low or not high:
                    rec['outcome'] = 'missing_endpoint'
                elif any(len(s) != 1 for s in states):
                    rec['outcome'] = 'ambiguous_conversion_state'
                else:
                    cs,ce = next(iter(states[0])),next(iter(states[1]))
                    rec['value_equivalent_duplicate_endpoint'] = len(low)>1 or len(high)>1
                    rec['tdf_mode_quality_fields'] = [
                        [dict(record=n,values=[z[k] for k in MODE_FIELDS]) for n,z in side]
                        for side in (low,high)]
                    for side in (low,high):
                        for _,z in side:
                            quality[tuple(z[k] for k in MODE_FIELDS)] += 1
                    domain = all(z[26]==5 and z[20]==1000 and z[22]==1 and z[23]==1
                                 for side in (low,high) for _,z in side)
                    if not domain or cs[1]!=ce[1] or d['down_band']!=2:
                        rec['outcome'] = 'mode_or_reference_outside_fixed_candidate'
                    elif not all(0 <= s[0] < MODULUS_MICROCYCLES for s in (cs,ce)):
                        rec['outcome'] = 'counter_outside_unsigned_domain'
                    else:
                        delta_microcycles,wraps = forward_lift(cs[0],ce[0])
                        dc = Q(delta_microcycles,10**6)
                        observed = Q(d['observable_integer'])+Q(d['observable_fraction_billionths'],10**9)
                        oref = Q((d['reference_frequency_high_mHz']<<24)|d['reference_frequency_low_mHz'],1000)
                        predicted = reconstruct(dc,duration,d['type'],cs[1],oref)
                        error = observed-predicted
                        scale = Q(2,10**6)/duration+Q(1,10**9)
                        if d['type']==11:
                            scale += Q(11,3*1000)+Q(880,221*10**6)
                        # Wrong-label countermodel, still without rollover as in v1.
                        ds,de = low[0][1],high[0][1]
                        wrong_delta = Q((de[30]-ds[30])*10**12+
                                        (de[31]-ds[31])*10**7+de[32]-ds[32],10**6)
                        wrong_error = observed-reconstruct(wrong_delta,duration,d['type'],cs[1],oref)
                        no_wrap_error = error+Q(wraps*2**32)/duration
                        omit_oneway_error = observed-(dc/duration-10**6)
                        rec.update(outcome='reconstructed_conditional_lift',
                            count_delta_cycles=rational(dc),lift_wraps=wraps,
                            count_endpoint_microcycles=[cs[0],ce[0]],
                            error_hz=rational(error),storage_quantum_scale_hz=rational(scale),
                            within_storage_quantum_scale=abs(error)<=scale,
                            coherent_reference_matches_odf=(cs[1]==oref if d['type']!=11 else None),
                            countermodel_wrong_label_scale_error_hz=rational(wrong_error),
                            countermodel_omit_wrap_error_hz=rational(no_wrap_error),
                            countermodel_subtract1000_error_hz=rational(error-999000),
                            countermodel_reverse_count_error_hz=rational(error+2*dc/duration),
                            countermodel_omit_oneway_reference_error_hz=rational(omit_oneway_error))
                        groups[(d['type'],d['rx'],d['tx'])].append((number,error,scale,dc,cs[1]==oref))
                        counters['rollovers'] += wraps
                        counters['value_equivalent_duplicate_endpoint_intervals'] += rec['value_equivalent_duplicate_endpoint']
                        counters['mismatches'] += abs(error)>scale
                        counters['wrong_label_scale_mismatches'] += abs(wrong_error)>scale
                        counters['omitted_rollover_mismatches'] += abs(no_wrap_error)>scale
                        counters['wrong_bias_mismatches'] += abs(error-999000)>scale
                        counters['reverse_count_mismatches'] += abs(error+2*dc/duration)>scale
                        if d['type']==11:
                            counters['omitted_oneway_reference_mismatches'] += abs(omit_oneway_error)>scale
                        if abs(error)>scale or wraps or rec['value_equivalent_duplicate_endpoint']:
                            examples.append(rec)
            outcomes[rec['outcome']] += 1
            line = json.dumps(rec,sort_keys=True,separators=(',',':'))+'\n'
            rows.write(line)
            row_hash.update(line.encode())
    summary=[]
    for key,vals in sorted(groups.items()):
        worst = max(vals,key=lambda x:abs(x[1]))
        summary.append(dict(key=list(key),records=len(vals),
            error_min_hz=rational(min(v[1] for v in vals)),
            error_max_hz=rational(max(v[1] for v in vals)),
            max_abs_error_hz=rational(abs(worst[1])),worst_odf_record=worst[0],
            within_storage_quantum_scale=sum(abs(v[1])<=v[2] for v in vals),
            count_delta_min_cycles=rational(min(v[3] for v in vals)),
            count_delta_max_cycles=rational(max(v[3] for v in vals)),
            nonpositive_count_increments=sum(v[3]<=0 for v in vals),
            coherent_reference_equality_count=sum(v[4] for v in vals) if key[0]!=11 else None))
    out=dict(role='exposed development stored-count reconstruction; conditional counter lift; no physical fit',
        sources=IDENTITIES,self_checks=checks,tracking_samples_indexed=tracking_samples,
        outcome_counts=dict(outcomes),counters=dict(counters),groups=summary,
        mode_quality_field_order=list(MODE_FIELDS),
        endpoint_quality_occurrences=[dict(values=list(k),occurrences=v) for k,v in sorted(quality.items())],
        rollover_duplicate_or_mismatch_examples=examples,
        all_rows_sha256=row_hash.hexdigest(),all_rows_filename=args.rows_output.name,
        scope=['All91664ODF Doppler rows receive an outcome. No residual clipping or quality-group deletion.',
               'Modulo lift assumes 0<=true interval increment<2^32 cycles with no reset; this bounded-history premise is not derived from two endpoints.',
               'Equivalent endpoint variants identify the count/reference value only; their quality flags and item87 slip diagnostic remain distinct.',
               'Storage-quantum comparison scales are not certified legacy software errors or instrumental accuracy.',
               'Reconstruction of processed data from its precursor is not independent empirical validation.',
               'No physical sky-frequency, trajectory, plasma calibration or scalar constraint is asserted.'])
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('self_checks','outcome_counts','counters','groups','all_rows_sha256')},indent=2))


if __name__=='__main__':
    main()
