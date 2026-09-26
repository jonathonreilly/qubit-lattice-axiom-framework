"""Root controls for exact parity and deterministic Fourier bounds."""
from pathlib import Path
from itertools import product
from collections import Counter
import csv,hashlib,json
import numpy as np
HERE=Path(__file__).resolve().parent
D=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
def validate(s):
 N=s.shape[0];sites=np.array(list(product(range(N),repeat=3)));counts=np.array([np.sum(s==2*j) for j in range(3)])
 for x in sites:
  a=int(s[tuple(x)])
  if a>=0:assert s[tuple((x+D[a])%N)]==(a^1)
 vac=sites[s.reshape(-1)<0];parity=np.sum(vac%2,axis=0)%2
 assert np.array_equal(counts%2,parity)
 return sites,counts,vac

def constructed(N):
 s=np.full((N,N,N),-1,dtype=int)
 for x in range(0,N,2):s[x,:,:]=0;s[x+1,:,:]=1
 s[:2,:2,:2]=-1
 for x,j in [((1,0,0),1),((0,1,0),2),((0,0,1),0)]:
  x=np.array(x);s[tuple(x)]=2*j;s[tuple(x+D[2*j])]=2*j+1
 return s

def fourier_checks(s):
 N=s.shape[0];sites,counts,vac=validate(s);sigma=(-1.)**np.sum(sites,axis=1)
 B=np.array([sigma*((s.reshape(-1)==2*j)-1/6) for j in range(3)]).T
 rows=[]
 for mode in [(1,0,0),(1,2,0),(1,1,1)]:
  k=2*np.pi*np.array(mode)/N;phase=np.exp(-1j*(sites@k));f=phase@B/N**1.5
  q=-np.sum(((-1.)**np.sum(vac,axis=1))*np.exp(-1j*(vac@k)))/N**1.5
  d=1-np.exp(-1j*k);norm2=float(np.sum(abs(d)**2));actual=float(abs(q)**2/norm2);bound=len(vac)**2/(N**3*norm2)
  residual=abs(d@f-q);assert residual<2e-12
  longitudinal=np.conjugate(d)*q/norm2
  assert abs(np.vdot(longitudinal,longitudinal).real-actual)<2e-13 and actual<=bound+1e-13
  assert abs(np.vdot(longitudinal,f-longitudinal))<2e-12
  rows.append({'N':N,'mode':mode,'vacancies':len(vac),'longitudinal_power':actual,'bound':bound,'divergence_residual':float(residual)})
 return rows

def main():
 rows=[];construct=[]
 for N in (4,6,8,16,32):
  s=constructed(N);_,counts,vac=validate(s)
  assert list(counts)==[N**3//2-3,1,1] and len(vac)==2 and np.all(counts%2==1)
  construct.append({'N':N,'counts':list(map(int,counts)),'vacancies':vac.tolist()});rows+=fourier_checks(s)
 screens=[]
 for phase in ['pilot','screen']:
  directory=HERE/('paired_growth_'+phase)
  for result in json.loads((directory/'BATCH_RESULTS.json').read_text()):
   N=result['side'];s=np.loadtxt(directory/(result['stem']+'.final.txt'),dtype=int).reshape(N,N,N)
   _,counts,vac=validate(s);last=list(csv.DictReader((directory/(result['stem']+'.csv')).open()))[-1]
   assert counts.tolist()==[int(last[k]) for k in ('nx','ny','nz')]
   assert len(vac)==N**3-result['occupied']
   rows+=fourier_checks(s)
   active=sum(a*b for a,b in zip(result['enabled_channel_counts'],[result['beta'],result['kappa']/2,result['nu'],result['mu']]))
   screens.append({'case':result['stem'],'phase':phase,'N':N,'vacancies':len(vac),'counts':list(map(int,counts)),'all_odd_two_vacancy_obstruction':bool(len(vac)==2 and np.all(counts%2)),'zero_active_rate':bool(active==0)})
 sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'PAIRED_RECORD_PARITY_AND_RESIDUAL_VACANCIES.md']}
 output={'status':'author checks; no independent review or formation scaling theorem','sources_sha256':sources,'constructed':construct,'all_final_states':screens,'fourier_rows':rows}
 (HERE/'PAIRED_RECORD_PARITY_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
 print(json.dumps({'constructed_sizes':len(construct),'final_states_checked':len(screens),'fourier_cases':len(rows),'max_divergence_residual':max(r['divergence_residual'] for r in rows),'all_odd_two_vacancy_endpoints':sum(r['all_odd_two_vacancy_obstruction'] for r in screens),'sources_sha256':sources},indent=2))
if __name__=='__main__':main()
