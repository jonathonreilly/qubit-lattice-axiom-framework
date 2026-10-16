#!/usr/bin/env python3
"""Decode the archived format-2 ODF orbit records for a development inventory.

Uses PDS3 label pointers/counts and the label's big-endian bit definitions.
Does not produce corrected Doppler, a trajectory, a gravity fit or a likelihood.
"""
import argparse
import collections
import datetime
import hashlib
import json
import re
import struct
from pathlib import Path

AUDIT_TIMEOUT_SEC = 120


def bitfield(block, first, width):
    """PDS one-based MSB bit numbering; no byte-alignment assumption."""
    shift = 8*len(block) - first - width + 1
    if first < 1 or width < 1 or shift < 0:
        raise ValueError('bit field outside record')
    return (int.from_bytes(block, 'big') >> shift) & ((1 << width)-1)


def decode(row):
    if len(row) != 36:
        raise ValueError('record must have 36 bytes')
    time_int, time_pack, obs_int, obs_frac = struct.unpack('>IIii', row[:16])
    b,c = row[16:28],row[28:36]
    return dict(time_seconds=time_int, time_milliseconds=time_pack >> 22,
                downlink_delay_ns=time_pack & ((1<<22)-1),
                observable_integer=obs_int, observable_fraction_billionths=obs_frac,
                format=bitfield(b,1,3), rx=bitfield(b,4,7), tx=bitfield(b,11,7),
                network=bitfield(b,18,2), type=bitfield(b,20,6),
                down_band=bitfield(b,26,2), up_band=bitfield(b,28,2),
                exciter_band=bitfield(b,30,2), bad=bitfield(b,32,1),
                item15=bitfield(b,33,7), spacecraft=bitfield(b,40,10),
                independent_receiver=bitfield(b,50,1),
                reference_frequency_high_mHz=bitfield(b,51,22),
                reference_frequency_low_mHz=bitfield(b,73,24),
                item20=bitfield(c,1,20), compression_centiseconds=bitfield(c,21,22),
                uplink_delay_ns=bitfield(c,43,22))


def self_check():
    # An independent bit-string layout checks cross-byte fields and signed words.
    fields=[(2,3),(25,7),(54,7),(0,2),(13,6),(3,2),(2,2),(2,2),(1,1),
            (0,7),(82,10),(1,1),(1048579,22),(8388613,24)]
    s=''.join(format(v,f'0{n}b') for v,n in fields)
    suffix=''.join(format(v,f'0{n}b') for v,n in [(0,20),(6000,22),(1234,22)])
    row=struct.pack('>IIii',1234567890,(789<<22)|123456,-234,-567890123)
    row+=int(s,2).to_bytes(12,'big')+int(suffix,2).to_bytes(8,'big')
    d=decode(row)
    wanted=dict(format=2,rx=25,tx=54,type=13,down_band=3,up_band=2,exciter_band=2,
                bad=1,spacecraft=82,independent_receiver=1,compression_centiseconds=6000,
                uplink_delay_ns=1234,time_milliseconds=789,observable_integer=-234,
                observable_fraction_billionths=-567890123,
                reference_frequency_high_mHz=1048579,reference_frequency_low_mHz=8388613)
    assert all(d[k]==v for k,v in wanted.items()),(d,wanted)
    assert decode(row[:8]+struct.pack('>ii',234,567890123)+row[16:])['observable_integer']==234
    try:
        decode(row[:-1])
    except ValueError:
        pass
    else:
        raise AssertionError('truncated-record control failed')
    # A known cross-boundary field mutation must be observed rather than masked.
    mutated=bytearray(row);mutated[19]^=1  # last bit in items6-14 is validity.
    assert decode(mutated)['bad']==0 and d['bad']==1
    return {'known_cross_byte_fields':len(wanted),'signed_control':True,
            'truncation_rejected':True,'validity_mutation_detected':True}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--label',type=Path,required=True)
    ap.add_argument('--odf',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();checks=self_check();labelbytes=a.label.read_bytes()
    label=labelbytes.decode('ascii');data=a.odf.read_bytes()
    number=lambda name: int(re.search(r'^'+re.escape(name)+r'\s*=\s*(\d+)',label,re.M).group(1))
    assert number('RECORD_BYTES')==36
    assert len(data)==36*number('FILE_RECORDS'),'length does not match label'
    table=re.search(r'^OBJECT\s*=\s*ODF3C_TABLE\s*$(.*?)^END_OBJECT\s*=\s*ODF3C_TABLE',label,re.M|re.S).group(1)
    count=int(re.search(r'^\s*ROWS\s*=\s*(\d+)',table,re.M).group(1))
    first=int(re.search(r'^\^ODF3C_TABLE\s*=\s*\("[^\"]+",(\d+)\)',label,re.M).group(1))
    assert first>1 and first+count-1<=number('FILE_RECORDS')
    header=data[(first-2)*36:(first-1)*36]
    assert struct.unpack('>i',header[:4])[0]==109,'unexpected orbit header'
    assert struct.unpack('>I',header[12:16])[0]==first-2,'header pointer mismatch'
    records=[decode(data[i*36:(i+1)*36]) for i in range(first-1,first-1+count)]
    assert all(d['format']==2 for d in records),'unsupported format present'
    assert all(d['time_milliseconds']<1000 for d in records),'invalid fractional time'
    assert all(abs(d['observable_fraction_billionths'])<10**9 for d in records),'fraction out of range'
    times=[d['time_seconds']+d['time_milliseconds']/1000 for d in records]
    types=collections.Counter(d['type'] for d in records)
    links=collections.Counter((d['type'],d['rx'],d['tx'],d['up_band'],d['down_band'],d['bad']) for d in records)
    channels=collections.defaultdict(list)
    for d in records:
        if d['type'] in (11,12,13):
            channels[(d['type'],d['rx'],d['tx'],d['up_band'],d['down_band'],d['bad'])].append(d)
    groups=[]
    for key,rows in sorted(channels.items()):
        vals=[d['observable_integer']+d['observable_fraction_billionths']*1e-9 for d in rows]
        ts=[d['time_seconds']+d['time_milliseconds']/1000 for d in rows]
        counts=collections.Counter(d['compression_centiseconds'] for d in rows)
        groups.append(dict(key=list(key),records=len(rows),time_seconds=[min(ts),max(ts)],
                           compression_centiseconds=dict(counts),raw_observable_hz=[min(vals),max(vals)],
                           time_decreases=sum(b<a for a,b in zip(ts[:-1],ts[1:]))))
    iso=lambda sec:(datetime.datetime(1950,1,1)+datetime.timedelta(seconds=sec)).isoformat()
    result=dict(role='exposed development inventory; no empirical gravity test',
                source=dict(label_sha256=hashlib.sha256(labelbytes).hexdigest(),
                            odf_sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),
                            orbit_first_record_one_based=first,orbit_records=count),
                self_checks=checks,type_counts=dict(types),
                link_field_order=['type','receiving_station','transmitting_station','uplink_band','downlink_band','bad'],
                link_counts=[dict(key=list(k),count=v) for k,v in sorted(links.items())],
                nominal_utc_bounds=[iso(min(times)),iso(max(times))],
                time_conversion_scope='naive label-epoch calendar arithmetic only; no relativistic or station time correction',
                all_record_time_decreases=sum(b<a for a,b in zip(times[:-1],times[1:])),
                spacecraft_ids=sorted({d['spacecraft'] for d in records}),doppler_groups=groups,
                measurement_scope='Archived observable is a receiver/ramp/transponder compression product, not fractional gravitational Doppler or a plasma-corrected residual. All channels and validity flags retained; none selected by values.')
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['role','source','self_checks','type_counts','nominal_utc_bounds','all_record_time_decreases','spacecraft_ids']},indent=2))
    print('Doppler channel groups:',len(groups))
    for g in groups: print(json.dumps(g))


if __name__=='__main__': main()
