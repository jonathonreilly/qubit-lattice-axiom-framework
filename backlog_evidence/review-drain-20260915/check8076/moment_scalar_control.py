from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
R=Path(__file__).parent;idx=json.loads((R/'8076-recovered-object-inventory.json').read_text());bind={};S=2**192
def read(tail):
 x=next(x for x in idx if x['original'].endswith('/'+tail));bind[tail]=x['sha256'];return json.loads((R/'forensic'/x['sha256']).read_text())
def rnd(l,u):return F(l.numerator*S//l.denominator,S),F(-((-u.numerator*S)//u.denominator),S)
def at(x,n):
 v=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)),F());return v,v+x**(2*n+1)/F(2*n+1)
a,b=at(F(1,5),32),at(F(1,239),10);pl,pu=16*a[0]-4*b[1],16*a[1]-4*b[0]
# Independent convolution of three central-binomial moment sequences.
m=[1]+[0]*27
for _ in range(3):m=[sum(comb(n,k)*m[k]*comb(2*(n-k),n-k) for k in range(n+1)) for n in range(28)]
ans=[]
for name,shift in [('native-cminus-catalog-run-1f93',0),('native-highprecision-mu-repair-run-9d21',1)]:
 d=read(name+'/RESULT.json');total=list(map(F,d['middle']))
 tail=sum((F((-1)**n*m[n+shift],(2*n+1)*8**(2*n+1)) for n in range(26)),F());rem=F(12**(26+shift),53*8**53);low=F(1,(3 if shift==0 else 1)*2**64);rad=F(400,27)*F(4,25)**26 if not shift else F(20,3)*(4+F(4800,961))*F(4,25)**26
 for k,v in [('high_partial',tail),('high_remainder',rem),('low_bound',low),('quadrature_radius',rad)]:assert F(d[k])==v
 l,u=rnd(total[0]+tail,total[1]+tail+rem);l,u=rnd(l-rad,u+rad+low);got=rnd(l*2/pu,u*2/pl);assert list(got)==list(map(F,d['interval']));assert got[1]-got[0]<=F(2,10**19);ans.append({'name':name,'interval':list(map(str,got))})
(R/'moment-scalar-control.json').write_text(json.dumps({'status':'PASS','results':ans,'bindings':bind,'scope':'Independent moment convolution and analytic-tail/Pi final enclosure from saved middle intervals; original panel integrations not repeated. No oracle or full worker replay.'},indent=2)+'\n');print('PASS cminus/mu exact moment-tail final enclosures')
