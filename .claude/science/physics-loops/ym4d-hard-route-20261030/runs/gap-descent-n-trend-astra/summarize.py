#!/usr/bin/env python3
"""Collect saved records only. Refuse incomplete required grids or brackets."""
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
WINDOW=(2.3,2.4,2.5,2.6)

def main():
    data=json.loads((HERE/'sweep.json').read_text())
    old=json.loads((HERE.parent/'gap-descent-window-astra/leak_sweep.json').read_text())
    assert {x['n'] for x in data['brackets']} >= {4,5,6}
    summary={'grade':'GUIDE','heat_window':[],'brackets':[],'inventory':data['inventory']}
    for n in (4,5,6):
        for b in WINDOW:
            x=next(x for x in data['grid'] if x['n']==n and x['beta']==b)
            assert len(x['values'])==2
            summary['heat_window'].append(x)
    for source,ns in ((old,(2,3)),(data,(4,5,6))):
        points=source['grid']+source['bisection']
        for n in ns:
            key='first_negative_brackets' if n<4 else 'brackets'
            bracket=next(x['bracket'] for x in source[key] if x['n']==n)
            lo,hi=bracket;assert 0<hi-lo<=1e-5
            ends=[next(x for x in points if x['n']==n and x['beta']==b) for b in bracket]
            assert all(v['difference']>0 for v in ends[0]['values'])
            assert all(v['difference']<0 for v in ends[1]['values'])
            summary['brackets'].append({'n':n,'reused':n<4,'bracket':bracket,'endpoint_differences':[[v['difference'] for v in x['values']] for x in ends]})
    for x in data['grid']+data['bisection']:
        for v in x['values']:
            g=v['per_gap'];assert max(abs(g[j][i]-g[-1-j][i]) for j in range(len(g)) for i in (0,1))<=1e-9
    summary['heat_window_minimum']=min(v['difference'] for x in summary['heat_window'] for v in x['values'])
    summary['heat_window_max_cutoff_difference']=max(x['cutoff_disagreement'] for x in summary['heat_window'])
    summary['heat_window_max_lambda2_over_lambda1']=max(v['lambda2_over_lambda1'] for x in summary['heat_window'] for v in x['values'])
    summary['heat_peak_RSS_bytes']=max(v['peak_RSS_bytes'] for x in data['grid']+data['bisection'] for v in x['values'])
    summary['heat_max_residual']=max(r for x in data['grid']+data['bisection'] for v in x['values'] for r in v['residuals'])
    summary['heat_bisection_max_cutoff_difference']=max(x['cutoff_disagreement'] for x in data['bisection'])
    summary['wilson']=[]
    for E in (44,48):
        d=json.loads((HERE/f'wilson_J4E{E}.json').read_text())
        assert {(x['beta'],x['multiplier']) for x in d['results']}=={(b,m) for b in WINDOW for m in (0,4,2,1)}
        summary['wilson'].append(d)
    comparison=json.loads((HERE/'wilson_comparison.json').read_text())
    summary['wilson_comparison']=comparison
    summary['wilson_max_gap_change']=max(abs(x['gap_change']) for x in comparison['changes'])
    summary['wilson_max_difference_change']=max(abs(x['difference_change']) for x in comparison['changes'])
    summary['wilson_minimum_finite_difference']=min(x['difference'] for d in summary['wilson'] for x in d['results'] if x['multiplier'])
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('heat_window','wilson','wilson_comparison')},indent=2))
if __name__=='__main__':main()
