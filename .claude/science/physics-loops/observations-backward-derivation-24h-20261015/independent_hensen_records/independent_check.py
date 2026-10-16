import zipfile,hashlib,io,json,math
import numpy as np
from fractions import Fraction as F
from pathlib import Path
archive=Path('/Users/jonBridger/.codex/campaigns/observations-backward-derivation-24h-20261015/private_sources/hensen_data_v1.zip')
assert hashlib.sha256(archive.read_bytes()).hexdigest()=='c28eb0f075759aef620a0b2e00a70fd675ce712bc8214d11c103f5a3d29492c0'
z=zipfile.ZipFile(archive)
# Independently written from the deposited header and original example;
# the example itself is never imported or executed.
a=np.loadtxt(io.BytesIO(z.read('bell_open_data.txt')),delimiter=',',usecols=range(1,17),dtype=np.int64)
assert a.shape[1]==16
start=np.array([5426350,5425700]); t1,c1,t2,c2=a[:,2],a[:,3],a[:,4],a[:,5]
assert set(c1)<=set([0,1]) and set(c2)<=set([0,1])
h=(t1>=start[c1])&(t1<start[c1]+52450)&(t2>=start[c2]+250000)&(t2<start[c2]+302450)&(c1!=c2)
valid=((a[:,14]==0)|(a[:,14]>250))&((a[:,15]==0)|(a[:,15]>250))
early=(a[:,12]==0)&(a[:,13]==0)
mask=h&valid&early
A,B=a[mask,6],a[mask,7]
x=2*((a[mask,10]>10620)&(a[mask,10]<=14320)).astype(int)-1
y=2*((a[mask,11]>10620)&(a[mask,11]<=14320)).astype(int)-1
N=int(mask.sum());wins=int(np.sum(x*y==1-2*A*B))
counts=np.zeros((4,4),dtype=int)
for aa,bb,xx,yy in zip(A,B,x,y):counts[2*aa+bb,(0 if xx==1 else 2)+(0 if yy==1 else 1)]+=1
E=[F(int(row[0]-row[1]-row[2]+row[3]),int(row.sum())) for row in counts]
S=E[0]+E[1]+E[2]-E[3];variance=sum((1-e*e)/int(row.sum()) for e,row in zip(E,counts))
tau=F(108,10000000);qvalues={'original':F(3,4)+3*(tau+tau*tau),'conditional_independent':F(3,4)+tau-tau*tau,'ideal':F(3,4)}
tails={}
for name,q in qvalues.items():
 mass=(1-q)**N;tail=F(0)
 for j in range(N+1):
  if j>=wins:tail+=mass
  if j<N:mass*=F(N-j,j+1)*q/(1-q)
 tails[name]={'q':str(q),'tail':float(tail)}
result={'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'archive_md5':hashlib.md5(archive.read_bytes()).hexdigest(),'bytes':archive.stat().st_size,'member_sha256':{n:hashlib.sha256(z.read(n)).hexdigest() for n in z.namelist()},'selection_counts':[len(a),int(h.sum()),int((h&valid).sum()),N],'selected_line_numbers_sha256':hashlib.sha256(json.dumps((np.flatnonzero(mask)+1).tolist(),separators=(',',':')).encode()).hexdigest(),'wins':wins,'matrix':counts.tolist(),'S':float(S),'descriptive_S_error':math.sqrt(float(variance)),'tails':tails}
Path(__file__).with_name('independent_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
