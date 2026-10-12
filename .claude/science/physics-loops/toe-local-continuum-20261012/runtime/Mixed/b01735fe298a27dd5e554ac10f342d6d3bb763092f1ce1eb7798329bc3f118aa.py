"""Deterministic diagnostic records, not acceptance manufactured by metadata."""
import argparse,hashlib,importlib.util,json,platform,sys
from pathlib import Path
import numpy as np
import scipy

def arguments(extra=None):
    p=argparse.ArgumentParser()
    p.add_argument('--candidate',default=str(Path(__file__).with_name('candidate.py')))
    p.add_argument('--output',required=True)
    if extra:extra(p)
    args=p.parse_args()
    spec=importlib.util.spec_from_file_location('tested_candidate',args.candidate)
    candidate=importlib.util.module_from_spec(spec);spec.loader.exec_module(candidate)
    return args,candidate

class Book:
    def __init__(self,label,args):self.label=label;self.args=args;self.rows=[]
    def check(self,name,value,bound,**context):
        value=float(value);bound=float(bound)
        self.rows.append({'name':name,'value':value,'bound':bound,
                          'pass':bool(np.isfinite(value) and value<=bound),'context':context})
    def finish(self,notes):
        failures=[r for r in self.rows if not r['pass']]
        result={'label':self.label,'candidate':str(Path(self.args.candidate).resolve()),
          'candidate_sha256':hashlib.sha256(Path(self.args.candidate).read_bytes()).hexdigest(),
          'versions':{'python':sys.version,'executable':sys.executable,'numpy':np.__version__,
                      'scipy':scipy.__version__,'platform':platform.platform()},
          'rows':self.rows,'failure_count':len(failures),'notes':notes}
        output=Path(self.args.output);output.parent.mkdir(parents=True,exist_ok=True)
        data=json.dumps(result,indent=2,allow_nan=False)+'\n';output.write_text(data);print(data,end='')
        raise SystemExit(1 if failures else 0)
