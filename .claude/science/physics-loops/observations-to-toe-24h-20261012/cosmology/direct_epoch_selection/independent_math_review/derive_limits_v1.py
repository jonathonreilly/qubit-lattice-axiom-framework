#!/usr/bin/env python3
"""Independent exact limiting-system derivation from the field metric/action.
No parent implementation, parent symbolic expression import or numerical run.
H_v=1 fixes units; N and all displayed autonomous quantities are dimensionless.
"""
from pathlib import Path
import json,hashlib,sys
import sympy as s
import mpmath as mp

HERE=Path(__file__).resolve().parent
a,nu=s.symbols('a nu',positive=True)
u,x,y=s.symbols('u x y',real=True)
pu,px,py=s.symbols('p_u p_x p_y',real=True)
sm,sr=s.symbols('sigma r',nonnegative=True)
U,V,P,W=s.symbols('U V P W',real=True)
t=s.symbols('t',positive=True)
lam=s.symbols('lambda')
checks=[];results={}
def exact(name,expr):
    reduced=s.factor(s.cancel(expr))
    checks.append({'name':name,'passed':reduced==0,'remainder':str(reduced)})
def zero_matrix(name,m):
    for i in range(m.rows):
        for j in range(m.cols):exact(name+' '+str(i)+','+str(j),m[i,j])
def lim(expr):
    num,den=s.cancel(expr).as_numer_denom();num=s.Poly(num,t);den=s.Poly(den,t)
    if num.degree()<den.degree():return s.S(0)
    if num.degree()>den.degree():raise ValueError('Unexpected divergent rational limit: '+str(expr))
    return s.factor(num.LC()/den.LC())

coords=[u,x,y];vel=[pu,px,py]
c=2*(1+a)/3;D=1+c*(x*x+y*y)
metric=s.diag(1,4*a/(9*D),a/(3*D));inverse=metric.inv()
potential=s.Rational(3,2)+(a/2-s.sqrt(a)*u+2*u*u)*x*x+a*y*y/3+nu*u*u/2
Gamma={}
for i in range(3):
    for j in range(3):
        for k in range(3):
            value=s.factor(sum(inverse[i,l]*(s.diff(metric[l,k],coords[j])+s.diff(metric[l,j],coords[k])-s.diff(metric[j,k],coords[l]))/2 for l in range(3)))
            if value!=0:Gamma[i,j,k]=value
T=sum(metric[i,j]*vel[i]*vel[j]for i in range(3)for j in range(3))
H2=2*(sm+sr+potential)/(3-T)
h=-(sm+s.Rational(4,3)*sr)/H2-T
acc=[]
for i in range(3):
    connection=sum(Gamma.get((i,j,k),0)*vel[j]*vel[k]for j in range(3)for k in range(3))
    force=sum(inverse[i,j]*(s.diff(potential,coords[j])+(s.sqrt(a)*sm if j==0 else 0))for j in range(3))
    acc.append(-(3+h)*vel[i]-connection-force/H2)
results['metric']=str(metric);results['Christoffels']={','.join(map(str,k)):str(v)for k,v in Gamma.items()}

print('dust full-action limit',flush=True)
dust={u:s.sqrt(a)*U,x:t,y:0,pu:s.sqrt(a)*V,px:P*t,py:0,sm:W*t*t,sr:0}
bm=2*a/(3*(1+a));br=a/(2*(1+a));f=a*(s.Rational(1,2)-U+2*U*U)
F=2*(W+f)/(3-a*V*V-bm*P*P)
hh=-W/F-a*V*V-bm*P*P
expected=s.Matrix([V,-(3+hh)*V-(-1+4*U+W)/F,-(3+hh)*P-2*f/(bm*F),W*(-3+a*V-2*P)])
derived=s.Matrix([V,lim((acc[0]/s.sqrt(a)).subs(dust)),lim((acc[1]/x-(px/x)**2).subs(dust)),W*(-3+a*V-2*P)])
exact('dust H2 normalization',lim((H2/x**2).subs(dust))-F)
exact('dust h',lim(h.subs(dust))-hh)
zero_matrix('dust vector field',derived-expected)
results['dust_rhs']=list(map(str,derived));results['dust_F']=str(s.factor(F))

d=1/(1+a);z=lam*(lam+s.Rational(3,2))
J0=s.Matrix([[0,1,0,0],[-6*d,-s.Rational(3,2),0,-3*d/2],[9*d/2,0,-s.Rational(3,2),9*d/4],[0,a,-2,0]])
J1=s.Matrix([[0,1,0,0],[-2*d,-s.Rational(3,2),0,-d/2],[9*d/2,0,-s.Rational(3,2),3*d/4],[0,3*a,-6,0]])
fixed=[(0,1,c,J0,z*z+(21+3*a)*d*z/2+s.Rational(27,2)*d*d),(-s.Rational(1,2),3,3*c,J1,z*z+(13+3*a)*d*z/2-s.Rational(9,2)*d*d)]
for i,(uu,ww,ff,jj,poly)in enumerate(fixed):
    E={U:uu,V:0,P:-s.Rational(3,2),W:ww}
    zero_matrix('dust equilibrium '+str(i),derived.subs(E))
    exact('dust fixed H2 '+str(i),F.subs(E)-ff)
    exact('dust fixed h '+str(i),hh.subs(E)+s.Rational(3,2))
    J=derived.jacobian([U,V,P,W]).subs(E).applyfunc(s.factor)
    zero_matrix('dust Jacobian '+str(i),J-jj)
    exact('dust characteristic polynomial '+str(i),J.charpoly(lam).as_expr()-poly)
    results['dust_E'+str(i)]={'Jacobian':str(J),'characteristic':str(s.factor(poly)),'F':str(ff),'denominator':str(s.factor((3-a*V*V-bm*P*P).subs(E)))}

print('radiation full-action limit',flush=True)
rad={x:0,y:t,pu:0,px:0,py:P*t,sm:0,sr:W*t*t}
Fr=2*(W+a/3)/(3-br*P*P);hr=-s.Rational(4,3)*W/Fr-br*P*P
radexpected=s.Matrix([-(3+hr)*P-2*a/(3*br*Fr),W*(-4-2*P)])
radderived=s.Matrix([lim((acc[2]/y-(py/y)**2).subs(rad)),W*(-4-2*P)])
exact('radiation H2 normalization',lim((H2/y**2).subs(rad))-Fr)
exact('radiation h',lim(h.subs(rad))-hr)
zero_matrix('radiation vector field',radderived-radexpected)
Er={P:-2,W:1};zero_matrix('radiation equilibrium',radderived.subs(Er));exact('radiation fixed H2',Fr.subs(Er)-c)
Jr=radderived.jacobian([P,W]).subs(Er).applyfunc(s.factor)
zero_matrix('radiation Jacobian',Jr-s.Matrix([[-1,2*d],[-2,0]]))
exact('radiation characteristic',Jr.charpoly(lam).as_expr()-(lam**2+lam+4*d))
results['radiation']={'rhs':list(map(str,radderived)),'Jacobian':str(Jr),'characteristic':str(s.factor(Jr.charpoly(lam).as_expr())),'denominator':str(s.factor((3-br*P*P).subs(Er)))}

print('transverse full-action limits',flush=True)
radbase={u:0,x:0,y:t,pu:0,px:0,py:-2*t,sm:0,sr:t*t}
dustbase={u:0,x:t,y:0,pu:0,px:-s.Rational(3,2)*t,py:0,sm:t*t,sr:0}
transverse={}
for name,index,field,momentum,base,stiff,damp in [('rad_x',1,x,px,radbase,s.Rational(21,4),5),('dust_y',2,y,py,dustbase,5,s.Rational(9,2)),('rad_u',0,u,pu,radbase,0,1)]:
    k=lim(s.diff(acc[index],field).subs(base));bcoef=lim(s.diff(acc[index],momentum).subs(base))
    exact(name+' stiffness',k+stiff);exact(name+' damping',bcoef+damp)
    transverse[name]={'field_acceleration_coefficient':str(k),'velocity_acceleration_coefficient':str(bcoef),'characteristic':str(lam**2+damp*lam+stiff),'roots':[str(v)for v in s.solve(lam**2+damp*lam+stiff,lam)]}
results['transverse']=transverse

print('missing velocity-domain counterexample',flush=True)
q=s.symbols('q',real=True)
velocitydust=dict(dust);velocitydust[py]=q*t
Fcounter=lim((H2/x**2).subs(velocitydust));Pcounter=lim((acc[1]/x-(px/x)**2).subs(velocitydust))
exact('counterexample retained transverse kinetic',Fcounter-2*(W+f)/(3-a*V*V-bm*P*P-br*q*q))
specific={a:1,U:0,V:0,P:-s.Rational(3,2),W:1,q:s.Rational(1,5)}
exact('counterexample F value',Fcounter.subs(specific)-s.Rational(75,56))
exact('counterexample p acceleration',Pcounter.subs(specific)+s.Rational(3,100))
results['domain_counterexample']={'conditions':'x=t -> infinity, y=0, y_N=t/5, r=0, a=1, U=V=0, P=-3/2, W=1','limiting_F':str(s.factor(Fcounter.subs(specific))),'limiting_P_N':str(s.factor(Pcounter.subs(specific))),'claimed_without_velocity_condition_F':'4/3','claimed_without_velocity_condition_P_N':'0'}

# Sign classification uses exact quadratics, supplemented with high-precision
# direct matrix eigenvalues at finite a values; no author eigenvalue routine.
mp.mp.dps=70;samples=[]
for aa in ['0.000001','0.00040016006402561027','0.01','1','15','16','1000']:
    matrices=[]
    for name,jmat in [('E0',J0),('E1',J1),('radiation',Jr)]:
        mat=mp.matrix([[mp.mpf(str(v.evalf(72,subs={a:s.Rational(aa)})))for v in row]for row in jmat.tolist()]);ev=mp.eig(mat,left=False,right=False)
        if name=='E1':ok=sum(mp.re(v)>0 for v in ev)==1 and sum(mp.re(v)<0 for v in ev)==3
        else:ok=all(mp.re(v)<0 for v in ev)
        checks.append({'name':'independent eigenvalues '+name+' a='+aa,'passed':bool(ok),'eigenvalues':[str(v)for v in ev]})
        matrices.append({'name':name,'eigenvalues':[str(v)for v in ev]})
    samples.append({'a':aa,'modes':matrices})
results['eigenvalue_samples']=samples
results['checks']=checks;results['passed']=sum(c['passed']for c in checks);results['failed']=sum(not c['passed']for c in checks);results['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();results['versions']={'sympy':s.__version__,'mpmath':mp.__version__}
with (HERE/'DERIVATION_RESULTS_v1.json').open('x')as f:json.dump(results,f,indent=2);f.write('\n')
print(json.dumps({'passed':results['passed'],'failed':results['failed'],'failures':[c for c in checks if not c['passed']],'counterexample':results['domain_counterexample']},indent=2))
sys.exit(bool(results['failed']))
