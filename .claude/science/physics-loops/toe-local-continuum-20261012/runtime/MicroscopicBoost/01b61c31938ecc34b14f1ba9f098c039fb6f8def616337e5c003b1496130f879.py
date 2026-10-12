"""Compare all full stored flow vectors across the preplanned refinement."""
import argparse,json
from pathlib import Path
import numpy as np

def main():
    p=argparse.ArgumentParser();p.add_argument('coarse');p.add_argument('fine');p.add_argument('--output',required=True)
    args=p.parse_args();coarse=np.load(args.coarse);fine=np.load(args.fine);rows=[]
    for key in coarse.files:
        if not key.endswith('_indices'):continue
        base=key[:-8];ci=coarse[key];fi=fine[key]
        mask=np.isin(fi,ci);indices=np.flatnonzero(mask)
        assert np.array_equal(fi[mask],ci)
        for suffix in ['_evolved','_continuum_cells']:
            cv=coarse[base+suffix].reshape(-1,2);fv=fine[base+suffix].reshape(-1,2)
            padded=np.zeros_like(fv);padded[indices]=cv
            error=float(np.linalg.norm(padded-fv))
            rows.append({'name':base+suffix,'value':error,'bound':3e-7,'pass':error<=3e-7})
    result={'rows':rows,'failure_count':sum(not r['pass'] for r in rows),
            'limits':'Changes box and quadrature together; small differences do not prove absence of common truncation error.'}
    data=json.dumps(result,indent=2)+'\n';Path(args.output).write_text(data);print(data,end='')
    raise SystemExit(1 if result['failure_count'] else 0)

if __name__=='__main__':main()
