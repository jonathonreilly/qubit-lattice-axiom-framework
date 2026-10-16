"""Exact archived-double NCO continuity comparison; development metadata only."""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
from fractions import Fraction as F
import gzip,json,hashlib
import numpy as np

def evaluate(h,t):
    p=[F.from_float(h['SUB-CHANNEL PHASE COEF P'+str(j)]) for j in range(1,5)]
    return F.from_float(h['SUB-CHANNEL ACCUMULATED PHASE'])+sum(v*t**j for j,v in enumerate(p))

def run(root):
    rows={}
    for band in ('X','KA'):
        file=root/(band+'_HEADERS_v1.jsonl.gz')
        with gzip.open(file,'rt') as f:hh=[json.loads(x) for x in f]
        tests=[]
        for shift in (F(0),F(1,2000)):
            residual=[];identities=[]
            for old,new in zip(hh[:-1],hh[1:]):
                assert new['SFDU SECOND']-old['SFDU SECOND']==1
                d=evaluate(new,shift)-evaluate(old,1+shift)
                residual.append(d);identities.append(str(d))
            a=np.array([float(x) for x in residual]);q=np.array([float(x-round(x)) for x in residual])
            tests.append({'shift_seconds':str(shift),'count':len(residual),'exact_residual_identity_sha256':hashlib.sha256(('\n'.join(identities)+'\n').encode()).hexdigest(),'raw_min_max':[float(a.min()),float(a.max())],'absolute_quantiles_0_50_99_100':np.quantile(np.abs(a),[0,.5,.99,1]).tolist(),'fractional_abs_max':float(np.abs(q).max()),'first_three_exact':identities[:3]})
        rows[band]={'header_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'tests':tests}
    result={'role':'internal metadata continuity of already exposed development records','products':rows,'physical_phase_identification':False,'no_fitted_parameters':True,'independent_empirical_tests':0}
    (root/'NCO_CONTINUITY_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n');return result

if __name__=='__main__':
    import sys
    run(Path(sys.argv[1]))
