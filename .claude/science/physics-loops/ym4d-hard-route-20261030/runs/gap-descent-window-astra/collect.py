#!/usr/bin/env python3
"""Collect saved spectra; require complete symmetry coverage for a gap."""
import argparse,json,math
from pathlib import Path

def collect(paths):
    data={}
    for path in paths:
        d=json.loads(Path(path).read_text())
        for x in d['results']:data[(x['beta'],x['multiplier'],x['sector'])]=x
    points=[]
    for b,m in sorted({(b,m) for b,m,s in data}):
        missing=[s for s in (0,1,2,4,5,6) if (b,m,s) not in data]
        if missing:continue
        vals=[]
        for s in range(8):
            source=1 if s==3 else 5 if s==7 else s
            vals += [(v,s) for v in data[b,m,source]['eigenvalues']]
        vals.sort(reverse=True)
        assert vals[0][1]==0
        points.append(dict(beta=b,multiplier=m,beta_L='infinity' if m==0 else b*m,gap=math.log(vals[0][0]/vals[1][0]),winning_sector=vals[1][1],first_competitor_sector=vals[2][1],lambda2_over_lambda1=vals[2][0]/vals[1][0]))
    faces={x['beta']:x['gap'] for x in points if x['multiplier']==0}
    for x in points:
        if x['beta'] in faces:x['difference']=x['gap']-faces[x['beta']]
    return points

def main():
 p=argparse.ArgumentParser();p.add_argument('files',nargs='+');p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 x=collect(a.files);a.output.write_text(json.dumps(dict(grade='GUIDE',inputs=a.files,results=x),indent=2)+'\n');print(json.dumps(x,indent=2))
if __name__=='__main__':main()
