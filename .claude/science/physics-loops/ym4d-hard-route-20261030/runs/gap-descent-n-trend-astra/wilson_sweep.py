#!/usr/bin/env python3
"""Run feasible full n=3 Wilson truncations, serially, then compare.
No convergence claim unless both gap and endpoint difference change <=1e-4.
"""
import json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent

def main():
    scratch=Path(sys.argv[1]);saved=[]
    for J,E in ((4,44),(4,48)):
        stem=f'wilson_J{J}E{E}';dest=scratch/stem;output=HERE/(stem+'.json')
        if not (dest/'meta.json').exists():
            with (HERE/(stem+'_build.log')).open('w') as log:
                subprocess.run([sys.executable,str(HERE/'wilson.py'),'build','--J',str(J),'--E',str(E),'--basis',str(dest)],stdout=log,stderr=subprocess.STDOUT,check=True)
        with (HERE/(stem+'_run.log')).open('a') as log:
            subprocess.run([sys.executable,str(HERE/'wilson.py'),'run','--basis',str(dest),'--output',str(output)],stdout=log,stderr=subprocess.STDOUT,check=True)
        saved.append(json.loads(output.read_text()));print('WILSON_COMPLETE',J,E,flush=True)
    changes=[]
    for b in (2.3,2.4,2.5,2.6):
        for mul in (0,4,2,1):
            pair=[next(x for x in d['results'] if x['beta']==b and x['multiplier']==mul) for d in saved]
            changes.append({'beta':b,'multiplier':mul,'gap_change':pair[1]['gap']-pair[0]['gap'],'difference_change':pair[1]['difference']-pair[0]['difference']})
    record={'grade':'GUIDE','criterion':'absolute changes <=1e-4 in gap and endpoint difference','changes':changes,'passes':all(abs(x[y])<=1e-4 for x in changes for y in ('gap_change','difference_change'))}
    (HERE/'wilson_comparison.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
if __name__=='__main__':main()
