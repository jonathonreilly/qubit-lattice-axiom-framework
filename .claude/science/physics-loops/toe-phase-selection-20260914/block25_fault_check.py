#!/usr/bin/env python3
"""Actual source faults for the private block25 evidence, not independent review."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, tempfile
PACK=Path(__file__).resolve().parent
SOURCE=PACK/'block25_relational_check.py'
FAULTS=[
 ('adjoint_metric_order','return h.inv()*a.conjugate().T*h','return h*a.conjugate().T*h.inv()','check_balancing'),
 ('determinant_normalization','ht = abs(T.det())*T.inv().T*h*T.inv()','ht = T.inv().T*h*T.inv()','check_balancing'),
 ('empty_word_removed','out = {(): I}','out = {(): ZERO}','check_word_support'),
 ('quadratic_words_removed','for n in range(1, max_length+1):','for n in range(1, min(max_length,1)+1):','check_word_support'),
 ('word_covariance_conjugation','vec(w)*vec(w).conjugate().T','vec(w)*vec(w).T','check_word_covariance'),
 ('neighbor_mean_normalization','mean=sum(aa,ZERO)/6','mean=sum(aa,ZERO)/5','check_actual_gaussian_law'),
 ('word_mark_sum_removed','return mean+sum((marks[w]*a for w,a in ww.items()),ZERO)','return mean+sum((marks[w]*a for w,a in ww.items() if len(w)<2),ZERO)','check_actual_gaussian_law'),
 ('future_clock_dependency','if rank[u]<rank[v]','if rank[u]>rank[v]','check_clock_orders'),
 ('path_infimum_reversed','brute[x]=min(brute.get(x,sp.oo),cost)','brute[x]=max(brute.get(x,0),cost)','check_transmission_growth'),
]

def main():
 body=SOURCE.read_text();rows=[]
 with tempfile.TemporaryDirectory(prefix='toe-block25-fault-') as tmp:
  for name,old,new,fn in FAULTS:
   assert body.count(old)==1,(name,body.count(old))
   candidate=body.replace(old,new,1);p=Path(tmp)/(name+'.py');p.write_text(candidate)
   command='import runpy; r=runpy.run_path('+repr(str(p))+'); r['+repr(fn)+']()'
   r=subprocess.run([sys.executable,'-c',command],text=True,capture_output=True,timeout=60)
   row={'name':name,'family':fn,'original':old,'replacement':new,'source_sha256':hashlib.sha256(candidate.encode()).hexdigest(),
        'exit_code':r.returncode,'stderr':r.stderr,'stdout':r.stdout,'caught':r.returncode!=0 and 'AssertionError' in r.stderr}
   rows.append(row);print(json.dumps({'fault':name,'caught':row['caught'],'stderr_end':r.stderr.splitlines()[-1:] }),flush=True)
 receipt={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':SOURCE.name,
          'source_sha256':hashlib.sha256(body.encode()).hexdigest(),'faults':rows,'all_caught':all(r['caught'] for r in rows)}
 (PACK/'BLOCK25_FAULT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
 assert receipt['all_caught']
if __name__=='__main__':main()
