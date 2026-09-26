"""Root reconstruction of all saved geometry and FFT observables, plus descriptive summaries."""
from pathlib import Path
import hashlib,json,math
import numpy as np
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 rows=[];max_difference=0.;max_gauss=0.;input_hashes={}
 for mode in ['pilot','screen']:
  folder=HERE/f'geometric_growth_{mode}';summary=json.loads((folder/'SUMMARY.json').read_text())
  assert summary['all_processes_succeeded'] and len(summary['results'])==(6 if mode=='pilot' else 144)
  for brief in summary['results']:
   prefix=folder/brief['name'];path=Path(str(prefix)+'.json');statepath=Path(str(prefix)+'.state.txt');receipt=json.loads(Path(str(prefix)+'.receipt.json').read_text());d=json.loads(path.read_text())
   for file,digest in receipt['files'].items():assert sha(folder/file)==digest
   input_hashes[str(path.relative_to(HERE))]=sha(path);input_hashes[str(statepath.relative_to(HERE))]=sha(statepath)
   N=d['N'];V=N**3;a=np.loadtxt(statepath,skiprows=2,dtype=np.int64);assert a.shape==(V,4) and np.array_equal(a[:,0],np.arange(V))
   partner=a[:,1];identity=a[:,2];births=a[:,3];assert d['full'] and np.all(partner>=0)
   assert np.array_equal(partner[partner],np.arange(V)) and np.array_equal(np.sort(identity),np.arange(V)) and np.all((identity^identity[partner])==1)
   assert int(births.sum())==V==2*d['birth_events'] and int(np.maximum(births-1,0).sum())==d['site_reuses'] and int(births.max())==d['max_site_births']
   x=np.indices((N,N,N)).reshape(3,-1).T;difference=(x[partner]-x)%N;distance=np.minimum(difference,N-difference);assert np.all(distance.sum(axis=1)==1)
   sigma=(-1)**x.sum(axis=1);ni=np.zeros((V,3),dtype=int)
   for i in range(3):
    y=x.copy();y[:,i]=(y[:,i]+1)%N;v=(y[:,0]*N+y[:,1])*N+y[:,2];ni[:,i]=(partner==v)
   counts=ni.sum(axis=0);assert counts.tolist()==d['orientation_counts'] and np.all(counts%2==0)
   B=(sigma[:,None]*(ni-1/6)).reshape(N,N,N,3);sixB=(sigma[:,None]*(6*ni-1)).reshape(N,N,N,3)
   divergence=sum(sixB[...,i]-np.roll(sixB[...,i],1,axis=i) for i in range(3));assert np.max(abs(divergence))==0
   winding=[]
   for i in range(3):
    planes=[int((sigma[x[:,i]==plane]*ni[x[:,i]==plane,i]).sum()) for plane in range(N)]
    assert len(set(planes))==1;winding.append(planes[0])
   assert winding==d['winding']
   transform=np.fft.fftn(B,axes=(0,1,2),norm='ortho');shells={}
   for item in d['modes']:
    ell=np.array(item['ell']);field=transform[tuple(ell%N)];normal=1-np.exp(-2j*np.pi*ell/N)
    div=normal@field;longitudinal=abs(div)**2/np.vdot(normal,normal).real;power=np.vdot(field,field).real;ST=(power-longitudinal)/2
    max_gauss=max(max_gauss,float(abs(div)));max_difference=max(max_difference,float(abs(ST-item['transverse_per_polarization'])),float(abs(power-item['power'])))
    assert abs(ST-item['transverse_per_polarization'])<1e-9 and abs(div)<1e-9
    shells.setdefault(int(ell@ell),[]).append(float(ST))
   assert {k:len(v) for k,v in shells.items()}=={1:3,2:6,3:4,4:3}
   row={**brief,'mode':mode,'volume':V,'time_per_volume':d['time']/V,'slides_per_site':d['slide_events']/V,'reuse_per_site':d['site_reuses']/V,'winding_power_per_component':sum(w*w for w in winding)/(3*N),'shells':{str(k):float(np.mean(v)) for k,v in shells.items()}}
   rows.append(row)
 groups=[];markdown=['| N | beta | runs | median filling time | mean slides/site | winding power/component | first-shell transverse power/polarization |','|---:|---:|---:|---:|---:|---:|---:|']
 for N in [4,8,12,16,24,32]:
  for beta in [.1,1,10]:
   selected=[r for r in rows if r['mode']=='screen' and r['N']==N and r['beta']==beta];assert len(selected)==8
   def moments(values):return {'mean':float(np.mean(values)),'sem_over_runs':float(np.std(values,ddof=1)/math.sqrt(len(values))),'min':min(values),'max':max(values)}
   g={'N':N,'beta':beta,'runs':8,'filling_time':moments([r['time'] for r in selected]),'median_filling_time':float(np.median([r['time'] for r in selected])),'slides_per_site':moments([r['slides_per_site'] for r in selected]),'reuse_per_site':moments([r['reuse_per_site'] for r in selected]),'winding_power_per_component':moments([r['winding_power_per_component'] for r in selected]),'shells':{str(k):moments([r['shells'][str(k)] for r in selected]) for k in [1,2,3,4]}}
   groups.append(g);markdown.append(f"| {N} | {beta} | 8 | {g['median_filling_time']:.5g} | {g['slides_per_site']['mean']:.5g} | {g['winding_power_per_component']['mean']:.5g} | {g['shells']['1']['mean']:.5g} |")
 result={'scope':'all 150 saved geometry states and all 2400 low-mode rows reconstructed; root verification, not independent review; summaries descriptive only','runs':len(rows),'max_FFT_power_difference':max_difference,'max_FFT_gauss_residual':max_gauss,'groups':groups,'rows':rows,'inputs_sha256':input_hashes,'source_sha256':sha(Path(__file__))}
 (HERE/'GEOMETRIC_GROWTH_ANALYSIS.json').write_text(json.dumps(result,indent=2)+'\n');(HERE/'GEOMETRIC_GROWTH_TABLE.md').write_text('\n'.join(markdown)+'\n')
 print(json.dumps({k:result[k] for k in ['runs','max_FFT_power_difference','max_FFT_gauss_residual']},indent=2));print('\n'.join(markdown))
if __name__=='__main__':main()
