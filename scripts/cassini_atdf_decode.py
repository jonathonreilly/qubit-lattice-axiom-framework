#!/usr/bin/env python3
"""Label-driven extraction, with PDS Appendix B corrected count scale; no science fit."""
import argparse
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
import datetime
import hashlib
import json
from pathlib import Path
import re

AUDIT_TIMEOUT_SEC = 120
LABEL_SHA='5c62b58cd56585b8ab2b518ca915e3ec7b8ccdc887de36b07ebabd09d496b5d6'


@dataclass(frozen=True)
class Field:
    item: int
    name: str
    first_bit_zero_based: int
    width: int
    signed: bool

    def read(self, word, bits=2304):
        v=(word >> (bits-self.first_bit_zero_based-self.width)) & ((1 << self.width)-1)
        return v-(1 << self.width) if self.signed and v & (1 << (self.width-1)) else v


def schema(label):
    body=re.search(r'^OBJECT\s*=\s*TDF5_TABLE\s*$(.*?)^END_OBJECT\s*=\s*TDF5_TABLE',label,re.M|re.S).group(1)
    columns=re.findall(r'^\s*OBJECT\s*=\s*COLUMN\s*$(.*?)^\s*END_OBJECT\s*=\s*COLUMN\s*$',body,re.M|re.S)
    fields=[]
    def prop(block,key):
        return re.search(r'^\s*'+key+r'\s*=\s*("[^"]*"|[^\r\n]+)',block,re.M).group(1).strip().strip('"')
    for col in columns:
        prefix=col.split('OBJECT')[0]
        start,width=int(prop(prefix,'START_BYTE'))-1,int(prop(prefix,'BYTES'))
        children=re.findall(r'^\s*OBJECT\s*=\s*BIT_COLUMN\s*$(.*?)^\s*END_OBJECT\s*=\s*BIT_COLUMN\s*$',col,re.M|re.S)
        for block in children or [col]:
            item=int(re.search(r'Item\s+(\d+):',block).group(1))
            offset=(int(prop(block,'START_BIT'))-1) if children else 0
            bits=int(prop(block,'BITS')) if children else width*8
            dtype=prop(block,'BIT_DATA_TYPE' if children else 'DATA_TYPE')
            if dtype not in ('MSB_INTEGER','MSB_UNSIGNED_INTEGER') or offset+bits>width*8:
                raise ValueError('unsupported type or field outside column')
            fields.append(Field(item,prop(block,'NAME'),8*start+offset,bits,dtype=='MSB_INTEGER'))
    fields.sort(key=lambda f:f.item)
    if len(columns)!=41 or len({f.item for f in fields})!=len(fields):
        raise ValueError('column count or item identity mismatch')
    used=[]
    for f in fields: used.extend(range(f.first_bit_zero_based,f.first_bit_zero_based+f.width))
    if len(used)!=len(set(used)) or min(used)!=0 or max(used)>=2304:
        raise ValueError('overlapping or out-of-range fields')
    return fields


def decode(row,fields):
    if len(row)!=288: raise ValueError('tracking record must have 288 bytes')
    word=int.from_bytes(row,'big')
    return {f.item:f.read(word) for f in fields}


def nominal_seconds(d):
    dt=datetime.datetime(1900+d[4],1,1)+datetime.timedelta(days=d[5]-1,hours=d[6],minutes=d[7],seconds=d[8])
    return int((dt-datetime.datetime(1950,1,1)).total_seconds())


def check_schema(fields):
    expected={1:(0,32,False),3:(40,32,False),4:(72,12,False),10:(144,10,False),
              20:(217,18,True),22:(236,1,False),23:(237,1,False),
              26:(240,6,False),29:(256,32,False),30:(288,24,False),
              31:(312,24,False),32:(336,24,False),79:(1440,8,False),120:(1808,32,True)}
    got={f.item:(f.first_bit_zero_based,f.width,f.signed) for f in fields}
    if any(got[k]!=v for k,v in expected.items()): raise AssertionError((got,expected))
    # Independent string construction exercises positive and negative boundary values.
    count=0
    for f in fields:
        values=[0,1,(1 << (f.width-1))-1]
        if f.signed:values += [-1,-(1 << (f.width-1))]
        else:values += [(1 << f.width)-1]
        for v in values:
            bits='0'*f.first_bit_zero_based+format(v % (1<<f.width),f'0{f.width}b')
            bits=bits.ljust(2304,'0')
            if decode(int(bits,2).to_bytes(288,'big'),[f])[f.item]!=v:raise AssertionError((f,v))
            count+=1
    return dict(manually_checked_field_positions=len(expected),synthetic_boundary_values=count,
                scope='extraction and label schema; not independent verification or semantic conversion')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--label',type=Path,required=True)
    ap.add_argument('--tdf',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); lb=a.label.read_bytes();lh=hashlib.sha256(lb).hexdigest()
    if lh!=LABEL_SHA or a.tdf.name!='c32easc2002_169_0000xmmmv0.tdf':
        raise ValueError('unregistered product')
    label=lb.decode('ascii');fields=schema(label);checks=check_schema(fields)
    data=a.tdf.read_bytes();dh=hashlib.sha256(data).hexdigest()
    if len(data)!=160888*288:raise ValueError('registered byte count mismatch')
    first=int(re.search(r'^\^TDF5_TABLE\s*=\s*\("[^"]+",(\d+)\)',label,re.M).group(1))
    body=re.search(r'^OBJECT\s*=\s*TDF5_TABLE\s*$(.*?)^END_OBJECT\s*=\s*TDF5_TABLE',label,re.M|re.S).group(1)
    count=int(re.search(r'^\s*ROWS\s*=\s*(\d+)',body,re.M).group(1))
    keyitems=[12,10,11,14,20,22,23,26,27,28,29,79]
    stats=defaultdict(lambda:dict(records=0,times=[],ref_counts=Counter(),quality=Counter(),slips=Counter(),example=None))
    types=Counter();formats=Counter();receivers=Counter();calendars=Counter();alltimes=[]
    for n in range(first,first+count):
        d=decode(data[(n-1)*288:n*288],fields)
        formats[d[1]]+=1;types[d[12]]+=1;receivers[d[26]]+=1
        calendars[(d[4],d[5])]+=1
        if d[1]!=8:raise ValueError('unsupported tracking record format')
        t=nominal_seconds(d);alltimes.append(t)
        if d[12] not in (1,2,7,11,12):continue
        s=stats[tuple(d[k] for k in keyitems)]
        s['records']+=1;s['times'].append(t)
        s['ref_counts'][d[43]*10**9+d[44]]+=1 # exact micro-Hertz, label items43/44
        s['quality'][d[19]]+=1;s['slips'][d[87]]+=1
        if s['example'] is None:
            s['example']=dict(record=n,items=d,phase_microcycles=d[30]*10**14+d[31]*10**7+d[32])
    groups=[]
    for key,s in sorted(stats.items()):
        groups.append(dict(key=list(key),records=s['records'],nominal_time_seconds=[min(s['times']),max(s['times'])],
            reference_microhertz_counts=[dict(value=k,count=v) for k,v in sorted(s['ref_counts'].items())],
            doppler_quality_counts=dict(s['quality']),slipped_cycle_counts=dict(s['slips']),example=s['example']))
    out=dict(role='registered exposed development ATDF inventory; no physical calibration',
        sources=dict(label_sha256=lh,tdf_sha256=dh,bytes=len(data),tracking_first_record=first,tracking_records=count),
        schema=[asdict(f) for f in fields],self_checks=checks,format_counts=dict(formats),sample_type_counts=dict(types),
        receiver_type_counts=dict(receivers),nominal_date_counts=[dict(year_mod1900=k[0],day=k[1],records=v) for k,v in sorted(calendars.items())],
        key_fields=[dict(item=k,name=next(f.name for f in fields if f.item==k)) for k in keyitems],
        doppler_groups=groups,scope=['All declared tracking rows retained in inventory counts. No value-based clipping.',
            'Dates are nominal label calendar arithmetic, without station or relativistic time conversion.',
            'Label-driven extraction only; receiver/bias units and phase conventions require separate source checks.',
            'No ODF reconstruction or independent empirical validation is claimed by this inventory.'])
    a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['sources','self_checks','format_counts','sample_type_counts','receiver_type_counts','nominal_date_counts','key_fields']},indent=2))
    print('Doppler groups',len(groups))
    for g in groups:print(json.dumps({k:v for k,v in g.items() if k!='example'}))


if __name__=='__main__':main()
