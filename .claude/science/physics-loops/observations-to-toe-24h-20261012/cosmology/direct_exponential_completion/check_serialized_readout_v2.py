#!/usr/bin/env python3
"""Bind each actual serialized physical readout to the primitive clock."""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
def main(freeze,source,out):
    checks=[]
    def ck(n,good,**detail):checks.append(dict(name=n,passed=bool(good),**detail))
    def near(n,got,want):
        e=abs(got/want-1);ck(n,np.isfinite(e) and e<=3e-12,relative_error=float(e),tolerance=3e-12)
    pin=json.loads(freeze.read_text())
    for x in pin['inputs']:ck('source.'+x['path'],hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'])
    d=json.loads(source.read_text());ck('original_checks_pass',all(x['passed'] for x in d['checks']))
    ck('six_case_census',len(d['histories'])==6)
    for h in d['histories']:
        cfg=h['configuration'];ident=h['case']['id'];ck(ident+'.complete',h['success'] and len(h['rows'])==241)
        for j,r in enumerate(h['rows']):
            u,pu=r['state'][0],r['state'][3];al=np.sqrt(cfg['a']);A=np.exp(al*u);F=1+cfg['s']*A*A
            B2=(1+cfg['s'])*A*A/F;rate=1+al*pu/F;hj=r['H2']*rate*rate/B2
            near(f'{ident}.{j}.HJ2',r['HJ2'],hj)
            near(f'{ident}.{j}.Hratio',r['Hratio'],np.sqrt(hj/r['HGR2']))
            near(f'{ident}.{j}.NJprime',r['NJprime'],rate)
    for x in pin['inputs']:ck('unchanged.'+x['path'],hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'])
    result=dict(scope='Separate semantic readout check; no dynamics rerun, no changes to v1 source or histories.',source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),original_counts=d['counts'],checks=checks,counts=dict(passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks)))
    assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(result['counts']);return bool(result['counts']['failed'])
if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--freeze',required=True,type=Path);pa.add_argument('--results',required=True,type=Path);pa.add_argument('--out',required=True,type=Path);a=pa.parse_args();raise SystemExit(main(a.freeze,a.results,a.out))
