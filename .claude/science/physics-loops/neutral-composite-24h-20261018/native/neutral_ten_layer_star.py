import mpmath as m,json
m.mp.dps=70
G=m.mpf(12155)/33554432;v=m.mpf(45)/16384;D=m.mpf(15)/512;kappa=4*G**2/v;eta=4*G**2/D
# Exact half-line resolvents of displayed coefficient graph, divided by lambda^8.
# Common thin diagonal energy subtracted. Not full microscopic numerical data.
def green(E,d,h):
 z=E-d
 return 2/(z-m.sqrt(z*z-4*h*h)) # E below every arm band

def values(lam,q=0):
 h=2*G*lam**2;d=D/lam**2
 hx=h*m.cos(q/2);hy=h;lx=h*m.cos(q);ly=h;ca=hy;cb=hx
 def parts(E):
  hub=E-d-hx*hx*green(E,d,hx)-hy*hy*green(E,d,hy)
  fa=E+v-lx*lx*green(E,0,lx);fb=E+v-ly*ly*green(E,0,ly)
  return hub,fa,fb
 def f(E):
  hub,fa,fb=parts(E)
  return fa*fb-(fa*cb*cb+fb*ca*ca)/hub
 guess=-v-h*h/v-2*eta*lam**6
 E=m.findroot(f,(guess,guess-eta*lam**6/10),solver='secant')
 return E,parts(E)[0],h,d
rows=[]
for st in ['.2','.1','.05','.02']:
 lam=m.mpf(st);E,hub,h,d=values(lam);anti=-v-h*h/v;q=lam/1000;Eq=values(lam,q)[0]
 low=h*green(E,0,h);hi=h*green(E,d,h);center=2*h/hub
 norm=2/(1-low**2)+center**2*(1+2*hi**2/(1-hi**2))
 rows.append(dict(lam=float(lam),energy=float(E),source_weight=float(4/norm),splitting_scaled=float((anti-E)/lam**6),curvature_scaled=float((Eq-E)/q**2/lam**4)))
print(json.dumps(dict(rows=rows,expected_splitting=float(2*eta),expected_curvature=float(kappa/2),scope='Truncated native coefficient graph only; not full microscopic spectrum')))
