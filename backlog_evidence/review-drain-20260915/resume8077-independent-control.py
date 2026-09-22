import json,sys,signal,time,hashlib
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(20000)
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('60s control cap')));signal.alarm(60)
t=time.monotonic();root=Path(__file__).parent
inv=json.loads((root/'resume8077-required-payload-inventory.json').read_text())['rows']
def file(suffix):
 rows=[r for r in inv if r['path'].endswith(suffix)];assert len({r['sha256'] for r in rows})==1;return Path(rows[0]['local'])
nodes=json.loads(file('/NODES.json').read_text())['rows'];assert len(nodes)==378
# Independent scalar Legendre recurrence at the 21 saved root endpoints.
def leg(x):
 p,q=F(1),x
 for n in range(2,22):p,q=q,((2*n-1)*x*q-(n-1)*p)/n
 return q
roots=[]
for i,n in enumerate(nodes):
 j,k=divmod(i,21);a=F(4)**(j-16);lo,hi=map(F,n['s_interval']);wl,wh=map(F,n['weight_interval'])
 assert a<lo<=hi<4*a and 0<wl<=wh
 pair=((2*lo/a-5)/3,(2*hi/a-5)/3)
 if j==0:roots.append(pair)
 else:assert pair==roots[k]
 assert F(n['s'])==(lo+hi)/2
for k,(lo,hi) in enumerate(roots):
 assert leg(lo)*leg(hi)<=0
 if k:assert roots[k-1][1]<lo
assert roots[10]==(0,0)
# Check every retained inverse/rounding and physical-column coefficient block,
# reading saved event data without importing producer or checker code.
count=0;last=None;weight=None;pm=None;et=F(0)
for line in file('/EVENTS.ndjson').open():
 e=json.loads(line);p=e['payload'];s=e['stage']
 if s=='reciprocal_pi':pm=sum(map(F,p['interval']))/2
 if s=='weight_recentered':weight=sum(map(F,p['rounded']))/2
 if s=='coefficient_inputs':
  v={k:F(p[k]) for k in ('s','A','D','Bgeo','a','determinant')};x,A,D,B,a,d=(v[k] for k in ('s','A','D','Bgeo','a','determinant'))
  assert D==(1-x*x*A)/6 and a==1-4*D and d==a*a+8*x*x*A*B and d>=F(1,9)
  last=[[-8*x*B/d,2*a/d],[-2*a/d,-4*x*A/d]]
 if s=='coefficient_exact_and_rounded':
  assert [[F(x) for x in row] for row in p['Q']]==last
  rounded=[]
  for row in last:
   out=[]
   for x in row:
    z=x*2**84;out.append(F((z+F(1,2)).__floor__(),2**84))
   rounded.append(out)
  assert [[F(x) for x in row] for row in p['Qhat']]==rounded
  err=2*max(abs(last[j][k]-rounded[j][k]) for j in range(2) for k in range(2));assert err==F(p['operator_rounding']) and err<=F(1,2**84);et=max(et,err)
 if s=='node_operator':
  block=[[F(x) for x in row] for row in p['positive_imaginary']]
  for j in range(2):
   for k in range(2):assert block[j][k+2]==-weight*pm*rounded[j][k]/2 and block[k+2][j]==-block[j][k+2]
  count+=1
 if s=='ledger_before_gate':
  analytic=F(2,9)*F(5439,160)/2**48+F(867,192)/2**64+F(1,8)*F(9,64)**15*(1+F(18,64*33))+6139*F(4,25)**21
  factors={'A':2**27,'pole':2**42,'weight':2**13,'coefficient':5,'reciprocal_pi':2**12}
  total=analytic+sum(F(p['input_radii'][k])*v for k,v in factors.items());assert total==F(p['total_error']) and total<F(2,10**13)
assert count==756
out={'scope':'Independent saved-data algebra; no oracle or primary replay','root_brackets':21,'mapped_nodes':378,'coefficient_blocks':count,'total_error':str(total),'seconds':time.monotonic()-t,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'resume8077-independent-control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
