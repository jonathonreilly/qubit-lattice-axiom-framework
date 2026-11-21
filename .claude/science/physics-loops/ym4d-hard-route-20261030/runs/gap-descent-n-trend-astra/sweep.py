#!/usr/bin/env python3
"""Serial, restartable two-cutoff sweep. Stops grid after first bracket.
Each subprocess inherits caller niceness and installs memory/thread guards.
"""
import argparse,json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
GRID=(.5,1.,1.5,2.,2.3,2.4,2.5,2.6,3.,3.5,4.,5.,6.,8.,10.)
CUTS=((10,12,32),(14,18,44))

def estimate(n,A,Q):return int(8*A**n*(21+3*Q/A)+80_000_000)

def main():
    p=argparse.ArgumentParser();p.add_argument('--ns',nargs='+',type=int,default=[4,5,6,7]);a=p.parse_args()
    dest=HERE/'sweep.json';record=json.loads(dest.read_text()) if dest.exists() else {'grade':'GUIDE','cutoffs':CUTS,'grid':[],'bisection':[],'brackets':[],'inventory':[]}
    def save():
        tmp=dest.with_suffix('.tmp');tmp.write_text(json.dumps(record,indent=2)+'\n');tmp.replace(dest)
    def pair(n,b):
        vals=[]
        for A,D,Q in CUTS:
            stem=f'n{n}_b{b:.17g}_A{A}_D{D}_Q{Q}'
            file=HERE/(stem+'.json')
            if not file.exists():
                cmd=[sys.executable,str(HERE/'leakage.py'),'--n',str(n),'--beta',str(b),'--cutoff',str(A),str(D),str(Q),'--output',str(file)]
                with (HERE/(stem+'.log')).open('w') as log:subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,check=True)
            x=json.loads(file.read_text());vals.append(x)
        if vals[0]['difference']*vals[1]['difference']<=0:raise RuntimeError(f'cutoff sign disagreement n={n}, beta={b}')
        item={'n':n,'beta':b,'values':vals,'cutoff_disagreement':abs(vals[0]['difference']-vals[1]['difference'])}
        print('POINT',n,b,[v['difference'] for v in vals],[v['seconds'] for v in vals],flush=True)
        return item
    for n in a.ns:
        predicted=[estimate(n,A,Q) for A,D,Q in CUTS]
        item={'n':n,'estimated_bytes':predicted,'admitted':max(predicted)<=1_950_000_000}
        if not any(x['n']==n for x in record['inventory']):record['inventory'].append(item);save()
        if not item['admitted']:print('MEMORY_GATE',item,flush=True);break
        if any(x['n']==n for x in record['brackets']):continue
        last=None;first=None
        for b in GRID:
            x=next((x for x in record['grid'] if x['n']==n and x['beta']==b),None)
            if x is None:x=pair(n,b);record['grid'].append(x);save()
            if x['values'][1]['difference']<0:
                if last is None:raise RuntimeError('first grid point negative; no positive bracket')
                first=(last,b);break
            last=b
        if first is not None:
            lo,hi=first
            while hi-lo>1e-5:
                mid=(lo+hi)/2
                x=next((x for x in record['bisection'] if x['n']==n and x['beta']==mid),None)
                if x is None:
                    x=pair(n,mid);record['bisection'].append(x)
                if x['values'][1]['difference']<0:hi=mid
                else:lo=mid
                x['bracket']=[lo,hi];save()
            record['brackets'].append({'n':n,'initial':first,'bracket':[lo,hi]})
        else:record['brackets'].append({'n':n,'initial':None,'bracket':None})
        save();print('COMPLETE_N',n,record['brackets'][-1],flush=True)
if __name__=='__main__':main()
