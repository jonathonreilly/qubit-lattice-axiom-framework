#!/usr/bin/env python3
"""Read-only independent scoring of frozen parameters; no author helper imports."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import argparse,json,hashlib
from pathlib import Path
import numpy as np
from scipy.constants import parsec

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--runtime',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();r=args.runtime
 train=json.loads((r/'training_parameters_frozen.json').read_text())
 split=json.loads((r/'fit_code_and_split_freeze.json').read_text())['split']['forward64']
 target=np.load(r/'sealed_targets.npz');fields=np.load(r/'baryonic_forward_64.npz')
 reports=json.loads((r/'comparison_results.json').read_text())['results'];rows=[]
 for entry in train['entries']:
  if entry['dataset']!='forward64':continue
  model=entry['model'];par=entry['parameters'];output={'model':model,'fixed_U':entry['fixed_U']}
  expected=next(x for x in reports if x['dataset']=='forward64' and x['model']==model and x['fixed_U']==entry['fixed_U'])
  for name_set in ['train','test']:
   means=[];derivatives=[];nrows=0
   for name in split[name_set]:
    mask=fields[name+'_score_mask'];rad=fields[name+'_R'][mask]
    gas=fields[name+'_gas'][:,mask];star=fields[name+'_disk'][:,mask]
    total=gas[0]+par['U']*star[0]
    if model=='L':
     w=np.array(par['weights'])
     total=(1-w.sum())*(gas[0]+par['U']*star[0])+np.einsum('i,ij->j',w,gas[1:]+par['U']*star[1:])
    if model=='NL':
     z=np.sqrt(total/rad*1e6/(1000*parsec)/par['a0'])
     pred=np.sqrt(total/(-np.expm1(-z)))
    else:pred=np.sqrt(total)
    delta=np.log10(pred/target[name+'_v'][mask]);means.append(np.mean(delta**2));nrows+=len(delta)
    if model=='NL' and name_set=='train':
     aa=z/np.expm1(z)
     dloga=aa/4
     dlogU=par['U']*star[0]/total*(1-aa/2)/2
     derivatives.append([np.mean(2*delta*dloga/np.log(10)),np.mean(2*delta*dlogU/np.log(10))])
   rms=float(np.sqrt(np.mean(means)));old=expected[name_set]['galaxy_equal_rms_log10_velocity'];assert abs(rms-old)<1e-14
   output[name_set]={'rms':rms,'reference_difference':rms-old,'galaxies':len(means),'rows':nrows}
   if derivatives:output['analytic_training_gradient_log_a0_log_U']=np.mean(derivatives,axis=0).tolist()
  rows.append(output)
 result={'scope':'Independent scores at frozen training parameters; no refit and no likelihood','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'files':{n:hashlib.sha256((r/n).read_bytes()).hexdigest() for n in ['training_parameters_frozen.json','fit_code_and_split_freeze.json','sealed_targets.npz','baryonic_forward_64.npz','comparison_results.json']},'rows':rows}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
