#!/usr/bin/env python3
"""Exact ramp inventory for the registered exposed Cassini development product.

This is a format/phase-integration check, not a corrected Doppler or gravity fit.
It intentionally does not select a historical receiver processing convention.
"""
import argparse
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import struct

from cassini_odf_decode import decode

AUDIT_TIMEOUT_SEC = 120
NS = 10**9
REGISTERED_ODF_SHA = '39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f'
REGISTERED_LABEL_SHA = '37beef944cfbab3711ba49b415535e2ca29113c3cd892ffe3f25160b1badf04e'


@dataclass(frozen=True)
class Ramp:
    station: int
    start_ns: int
    end_ns: int
    frequency_nhz: int
    rate_nhz_per_second: int
    sky_level: bool
    record_one_based: int = 0

    def frequency(self, at_ns):
        return Fraction(self.frequency_nhz, NS) + Fraction(
            self.rate_nhz_per_second * (at_ns - self.start_ns), NS**2)

    def integral(self, lo_ns, hi_ns):
        if not self.start_ns <= lo_ns <= hi_ns <= self.end_ns:
            raise ValueError('ramp extrapolation forbidden')
        return Fraction(self.frequency_nhz * (hi_ns-lo_ns), NS**2) + Fraction(
            self.rate_nhz_per_second * ((hi_ns-self.start_ns)**2 -
                                        (lo_ns-self.start_ns)**2), 2*NS**3)


def decode_ramp(row, record=0):
    if len(row) != 36:
        raise ValueError('ramp record must have 36 bytes')
    sec, frac, rate_i, rate_f, packed, hz, nhz, end, end_frac = struct.unpack('>IIiiIIIII', row)
    ghz, station = packed >> 10, packed & 1023
    if max(frac, end_frac, hz, nhz) >= NS or abs(rate_f) >= NS:
        raise ValueError('ramp fraction or frequency component out of range')
    r = Ramp(station, sec*NS+frac, end*NS+end_frac,
             (ghz*NS+hz)*NS+nhz, rate_i*NS+rate_f, ghz != 0, record)
    if r.end_ns <= r.start_ns:
        raise ValueError('nonpositive ramp interval')
    return r


def phase_integral(ramps, lo_ns, hi_ns):
    """Integrate disjoint, sorted ramps; reject gaps and any overlapping table."""
    if hi_ns <= lo_ns:
        raise ValueError('nonpositive integration interval')
    if any(a.end_ns > b.start_ns for a, b in zip(ramps, ramps[1:])):
        raise ValueError('overlapping or unsorted ramps')
    if len({r.station for r in ramps}) > 1 or len({r.sky_level for r in ramps}) > 1:
        raise ValueError('mixed station or frequency level')
    cursor, total, used = lo_ns, Fraction(0), []
    for r in ramps:
        if r.end_ns <= cursor or r.start_ns >= hi_ns:
            continue
        if r.start_ns > cursor:
            raise ValueError('uncovered integration interval')
        stop = min(r.end_ns, hi_ns)
        total += r.integral(cursor, stop)
        used.append(r.record_one_based)
        cursor = stop
        if cursor == hi_ns:
            return total, used
    raise ValueError('uncovered integration interval')


def table(label, name):
    pointer = re.search(r'^\^'+name+r'\s*=\s*\("[^"]+",(\d+)\)', label, re.M)
    body = re.search(r'^OBJECT\s*=\s*'+name+r'\s*$(.*?)^END_OBJECT\s*=\s*'+name,
                     label, re.M | re.S)
    if not pointer or not body:
        raise ValueError('missing table '+name)
    return int(pointer.group(1)), int(re.search(r'^\s*ROWS\s*=\s*(\d+)', body.group(1), re.M).group(1))


def rational(q):
    q = Fraction(q)
    return dict(numerator=q.numerator, denominator=q.denominator, approximate=float(q))


def self_checks():
    checks = {}
    def check(name, passed):
        checks[name] = bool(passed)
        if not passed:
            raise AssertionError(name)
    row = struct.pack('>IIiiIIIII', 1655517848, 123, -2, -500000000,
                      (7 << 10) | 54, 175200560, 321, 1655517850, 456)
    r = decode_ramp(row)
    check('signed_rate', r.rate_nhz_per_second == -2500000000)
    check('cross_word_station_and_ghz', r.station == 54 and r.frequency_nhz == 7175200560000000321)
    check('nanosecond_epochs', (r.start_ns, r.end_ns) == (1655517848000000123, 1655517850000000456))
    a = Ramp(25, 0, 2*NS, 10*NS, 3*NS, True, 1)
    b = Ramp(25, 2*NS, 4*NS, 16*NS, -NS, True, 2)
    check('single_affine_integral', a.integral(0, 2*NS) == 26)
    check('piecewise_integral', phase_integral([a,b], 0, 4*NS)[0] == 56)
    check('clipped_piecewise_integral', phase_integral([a,b], NS, 3*NS)[0] == 30)
    check('half_nanosecond_exact', a.integral(Fraction(1,2), Fraction(3,2)) ==
          Fraction(10, NS) + Fraction(3, NS**2))
    split = NS + 13
    check('partition_additivity', a.integral(0,split)+a.integral(split,2*NS) == a.integral(0,2*NS))
    epoch = 1655517848*NS
    shifted = Ramp(25, epoch, epoch+2*NS, 10*NS, 3*NS, True)
    check('epoch_shift_invariance', shifted.integral(epoch+1,epoch+2*NS-1) == a.integral(1,2*NS-1))
    jump = Ramp(25, 2*NS, 4*NS, 20*NS, 0, True, 3)
    check('frequency_jump_preserved', phase_integral([a,jump],0,4*NS)[0] == 66)
    for name, fn in [
        ('gap_rejected', lambda: phase_integral([a,Ramp(25,3*NS,4*NS,0,0,True)],0,4*NS)),
        ('overlap_rejected', lambda: phase_integral([a,Ramp(25,NS,4*NS,0,0,True)],0,4*NS)),
        ('extrapolation_rejected', lambda: a.integral(-1,NS)),
        ('mixed_level_rejected', lambda: phase_integral([a,Ramp(25,2*NS,4*NS,0,0,False)],0,4*NS)),
        ('truncated_record_rejected', lambda: decode_ramp(row[:-1]))]:
        try:
            fn()
        except ValueError:
            check(name, True)
        else:
            check(name, False)
    # A midpoint approximation is only exact inside one affine ramp.
    check('midpoint_across_jump_counterexample', phase_integral([a,jump],NS,3*NS)[0] != 2*jump.frequency(2*NS))
    return checks


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--label', type=Path, required=True)
    ap.add_argument('--odf', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args=ap.parse_args()
    checks=self_checks()
    lb, data=args.label.read_bytes(), args.odf.read_bytes()
    lh, dh=hashlib.sha256(lb).hexdigest(),hashlib.sha256(data).hexdigest()
    if (lh,dh) != (REGISTERED_LABEL_SHA,REGISTERED_ODF_SHA):
        raise ValueError('unregistered input: do not expose reserved measurement files')
    label=lb.decode('ascii')
    nbytes=int(re.search(r'^RECORD_BYTES\s*=\s*(\d+)',label,re.M).group(1))
    nrows=int(re.search(r'^FILE_RECORDS\s*=\s*(\d+)',label,re.M).group(1))
    if nbytes != 36 or len(data) != nrows*36:
        raise ValueError('label byte count mismatch')
    record=lambda n: data[(n-1)*36:n*36]
    ramps={}; station_summaries=[]
    for st in sorted(set(re.findall(r'^\^ODF4B(\d+)_TABLE',label,re.M)),key=int):
        start, count=table(label, f'ODF4B{st}_TABLE')
        header=struct.unpack('>iIIIIIIII',record(start-1))
        if header[:4] != (2030,int(st),1,start-2):
            raise ValueError('ramp header does not match pointer/station')
        rs=[decode_ramp(record(i),i) for i in range(start,start+count)]
        if any(r.station != int(st) for r in rs):
            raise ValueError('station mismatch')
        ramps[int(st)]=rs
        boundaries=[]
        for a,b in zip(rs,rs[1:]):
            boundaries.append(dict(left_record=a.record_one_based,right_record=b.record_one_based,
                gap_ns=b.start_ns-a.end_ns,
                endpoint_frequency_difference_hz=rational(b.frequency(b.start_ns)-a.frequency(a.end_ns))))
        # One exact integral per original ramp: no interpolation outside its domain.
        integrals=[dict(record=r.record_one_based,cycles=rational(r.integral(r.start_ns,r.end_ns))) for r in rs]
        station_summaries.append(dict(station=int(st),records=count,
            start_ns=rs[0].start_ns,end_ns=rs[-1].end_ns,all_sky_level=all(r.sky_level for r in rs),
            boundaries=boundaries,whole_segment_integrals=integrals,ramps=[asdict(r) for r in rs]))
    first,count=table(label,'ODF3C_TABLE')
    groups=defaultdict(list)
    for n in range(first,first+count):
        d=decode(record(n))
        if d['type'] not in (11,12,13):
            continue
        key=tuple(d[k] for k in ['type','rx','tx','network','up_band','down_band','exciter_band','bad','item15','independent_receiver'])
        groups[key].append((n,d))
    fields=['type','rx','tx','network','up_band','down_band','exciter_band','bad','channel_raw','independent_receiver']
    outgroups=[]
    for key,records in sorted(groups.items()):
        refs=Counter(); coverage=Counter(); examples=[]
        for n,d in records:
            ref=(d['reference_frequency_high_mHz']<<24)|d['reference_frequency_low_mHz']
            refs[ref]+=1
            mid=d['time_seconds']*NS+d['time_milliseconds']*10**6
            half=d['compression_centiseconds']*5*10**6
            try:
                cycles, used=phase_integral(ramps.get(d['rx'],[]),mid-half,mid+half)
                coverage['nominal_receive_interval_covered']+=1
                if len(used)>1:
                    coverage['crosses_ramp_boundary']+=1
                if len(examples)<2 or (len(used)>1 and len(examples)<6):
                    examples.append(dict(record=n,midpoint_ns=mid,segments=used,cycles=rational(cycles)))
            except ValueError as exc:
                coverage[str(exc)]+=1
        outgroups.append(dict(fields=dict(zip(fields,key)),records=len(records),
            reference_frequency_mHz=[dict(value=k,records=v) for k,v in sorted(refs.items())],
            nominal_receiver_ramp_coverage=dict(coverage),integration_examples=examples))
    result=dict(role='exposed development data; instrument reconstruction only; no gravity fit',
        sources=dict(odf_sha256=dh,label_sha256=lh,bytes=len(data),
                     specification='TRK-2-18 2000-06-15 tables 3-3b and 3-4b; Moyer 2000 13.3.2.2.2'),
        self_checks=checks,ramp_stations=station_summaries,doppler_groups=outgroups,
        clock_offset_table_present=bool(re.search(r'^\^ODF5',label,re.M)),
        scope=['Times are exact label-coordinate nanoseconds, not a validated station/UTC/proper-time bridge.',
               'Coverage at nominal reception time is diagnostic only: does not establish emission-time coverage.',
               'Receiver/exciter flag is preserved; a receiver ramp is not assumed to define the archived reference.',
               'Sky-level status follows the nonzero-GHz indicator in each ramp record.',
               'No absence of a clock table is interpreted as zero clock error.',
               'All Doppler groups and validity flags retained; no values select a theory or fit.'])
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(self_checks=checks,stations=[dict(station=x['station'],records=x['records'],
        sky=x['all_sky_level'],gaps=sum(b['gap_ns']>0 for b in x['boundaries']),
        overlaps=sum(b['gap_ns']<0 for b in x['boundaries']),
        jumps_at_contiguous_boundary=sum(b['gap_ns']==0 and b['endpoint_frequency_difference_hz']['numerator']!=0 for b in x['boundaries'])) for x in station_summaries],
        doppler_groups=[{k:v for k,v in g.items() if k!='integration_examples'} for g in outgroups]),indent=2))


if __name__=='__main__':
    main()
