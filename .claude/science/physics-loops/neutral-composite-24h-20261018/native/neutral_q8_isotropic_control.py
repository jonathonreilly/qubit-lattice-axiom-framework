import mpmath as m,json
m.mp.dps=220
g=m.mpf(12155)/33554432;D=m.mpf(15)/512;b=D/8;t=g*g/D;pref=g**4/(2*b)**3
S=m.mpf(607201)/144000;zeta=pref*S
rows=[]
for ls in ['.01','.0001','1e-8']:
 l=m.mpf(ls);qbase=2*m.pi*l**5
 for nx,ny in [(1,0),(1,1),(2,1)]:
  x=nx*qbase;y=ny*qbase
  a=-2*t*l**14*(m.cos(x)+4*m.cos(y));bb=-2*t*l**14*(4*m.cos(x)+m.cos(y))
  mix=-pref*l**22*(m.mpf(9673)/12000+m.mpf(191)/192*(m.cos(x)+m.cos(y))+m.mpf(1637)/1152*m.cos(x)*m.cos(y))
  en=(a+bb)/2-m.sqrt(((a-bb)/2)**2+mix**2)
  e0=-10*t*l**14-zeta*l**22
  predicted=m.mpf(5)/2*t*l**14*(x*x+y*y)
  rows.append(dict(lambda_value=ls,n=[nx,ny],ratio=str((en-e0)/predicted),relative_error=float((en-e0)/predicted-1)))
print(json.dumps(dict(zeta=str(zeta),curvature=str(m.mpf(5)/2*t),rows=rows),indent=2))
