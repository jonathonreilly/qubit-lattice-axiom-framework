#!/usr/bin/env python3
"""Serial two-truncation grid and bisection. No proof is inferred."""
from leakage import point,base
import argparse,json,time
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 start=time.monotonic();record={'grade':'GUIDE','grid':[],'bisection':[],'controls':[]}
 def save():
  record['seconds']=time.monotonic()-start;record['peak_RSS_bytes']=base.memory_check();a.output.write_text(json.dumps(record,indent=2)+'\n')
 for n,expected in [(2,1.281922541024204),(3,1.420804)]:
  b=2.4 if n==2 else 2.0
  x=point(n,b,0,10,12,32);x['reference_difference']=expected;record['controls'].append(x);save();print('CONTROL',json.dumps(x),flush=True)
 for n in (2,3):
  last=None;firstbracket=None
  for b in (.5,1.,1.5,2.,2.3,2.4,2.5,2.6,3.,3.5,4.,5.,6.,8.,10.):
   values=[point(n,b,b,A,D,Q) for A,D,Q in ((10,12,32),(14,18,44))]
   item={'n':n,'beta':b,'values':values,'cutoff_disagreement':abs(values[0]['difference']-values[1]['difference'])};record['grid'].append(item);save();print('GRID',json.dumps(item),flush=True)
   if values[1]['difference']<0 and firstbracket is None:firstbracket=(last,b)
   last=b
  if firstbracket:
   lo,hi=firstbracket
   while hi-lo>1e-5:
    mid=(lo+hi)/2;values=[point(n,mid,mid,A,D,Q) for A,D,Q in ((10,12,32),(14,18,44))]
    if values[0]['difference']*values[1]['difference']<=0:raise RuntimeError('cutoffs disagree on sign')
    if values[1]['difference']<0:hi=mid
    else:lo=mid
    record['bisection'].append({'n':n,'beta':mid,'values':values,'bracket':[lo,hi]});save();print('BISECT',n,mid,values[1]['difference'],lo,hi,flush=True)
  record.setdefault('first_negative_brackets',[]).append({'n':n,'bracket':None if firstbracket is None else [lo,hi]});save()
if __name__=='__main__':main()
