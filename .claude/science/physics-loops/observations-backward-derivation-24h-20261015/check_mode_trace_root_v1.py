"""Root post-exposure trace derivation, with an existing author forward model.

The checker independently originated the four-column route. This code does
not import its implementation; it deliberately reuses the frozen author's
original-equation forward generator. It is not an independent-CAS check.
"""
import ast
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp

p=Path(__file__).resolve().parent
checks=[]
def exact(name,expr):
 z=s.factor(s.cancel(s.expand(expr)));checks.append({'name':name,'pass':z==0,'residual':str(z)})
def ck(name,ok,**ev):checks.append({'name':name,'pass':bool(ok),**ev})
h,hp,q,qp,G,Gp,P0,P1,P2,J0,J1=s.symbols('h hp q qp G Gp P P1 P2 J J1',real=True)
ell=h-q
R=-2*hp+2*qp-2*h*q+2*q*q-q*G
# Direct conversion of the pressure trace; cancellation of b'/b is explicit.
L=s.symbols('L',real=True)
trace=(2*P2+2*(q+4*ell)*P1+(4*(hp-qp)+4*q*ell+6*ell**2+q*G)*P0
       -G*J1+G*L*J0-(Gp+G*L+(3*h-2*q)*G+R)*J0)
lhs=2*P2+8*h*P1+(4*hp+6*h*h)*P0
coeff=[6*q,4*qp+8*h*q-2*q*q-q*G,G,Gp+3*(h-q)*G-2*hp+2*qp-2*h*q+2*q*q]
exact('personally rederived pressure trace coefficients',trace-(lhs-sum(c*z for c,z in zip(coeff,[P1,P0,J1,J0]))))
exact('coupling derivative cancels from pressure trace',s.diff(trace,L))

# Execute only the frozen forward definitions, stopping before integration.
src=p/'check_mode_inverse_jets_v1.py'
expected='95dbccb44fc966428151cf45c2867a600ca77001f7b544c4946e7799a57bf2b3'
actual=hashlib.sha256(src.read_bytes()).hexdigest()
if actual!=expected:raise RuntimeError('frozen forward source changed')
tree=ast.parse(src.read_text(),filename=str(src))
prefix=[]
for node in tree.body:
 if isinstance(node,ast.Assign) and any(isinstance(v,ast.Name) and v.id=='times' for v in node.targets):break
 prefix.append(node)
else:raise RuntimeError('forward definition boundary missing')
ns={'__file__':str(src),'__name__':'root_forward_definitions'}
exec(compile(ast.Module(body=prefix,type_ignores=[]),str(src),'exec'),ns)
phi,v,r,H,a,u,pi,P,U,delta,k2=[ns[z] for z in ['phi','v','r','H','a','u','pi','P','U','delta','k2']]
A,b=ns['A'],ns['b']
jets=ns['jets'];variables=ns['variables']
expr=jets(P,4)+jets(b*u,3)+jets((H+b*v)/A,3)
observable=s.lambdify(variables+[k2],expr,'numpy',cse=True)
truth=s.lambdify(variables+[k2],[b*v/A,(v/A)/b,b,ns['mu']/A**2,r/A**2], 'numpy',cse=True)
times=np.linspace(0,.4,21)
sol=solve_ivp(ns['original_rhs'],(0,.4),ns['state0'],t_eval=times,method='DOP853',rtol=2e-12,atol=2e-15,max_step=.005)
ck('reused original forward generator succeeds',sol.success,message=sol.message)
maximum={n:0. for n in ['q','G','b_magnitude','R','kappa','Ctrace_compatibility','Ftrace_compatibility','overdetermined_residual']}
minimum_sigma=1.
rows=[]
for tt,yy in zip(sol.t,sol.y.T):
 bg=yy[:5];D=[[],[],[]];Y=[[],[],[]]
 for kv,row in zip(ns['kvalues'],yy[5:].reshape(5,5)):
  p0,p1,p2,p3,p4,j0,j1,j2,j3,h0,h1,h2,h3=np.asarray(observable(*bg,*row,kv),float)
  D[0].append([p1,p0,j1,j0]);D[1].append([p2,p1,j2,j1]);D[2].append([p3,p2,j3,j2])
  K=4*h1+6*h0*h0;Kp=4*h2+12*h0*h1;Kpp=4*h3+12*h1*h1+12*h0*h2
  Y[0].append(2*p2+8*h0*p1+K*p0)
  Y[1].append(2*p3+8*h0*p2+(8*h1+K)*p1+Kp*p0)
  Y[2].append(2*p4+8*h0*p3+(16*h1+K)*p2+(8*h2+2*Kp)*p1+Kpp*p0)
 ds=[np.asarray(v)/ns['epsilon'] for v in D];ys=[np.asarray(v)/ns['epsilon'] for v in Y]
 d0,d1,d2=ds;y0,y1,y2=ys
 theta=np.linalg.lstsq(d0,y0,rcond=None)[0]
 first=np.linalg.lstsq(d0,y1-d1@theta,rcond=None)[0]
 second=np.linalg.lstsq(d0,y2-d2@theta-2*d1@first,rcond=None)[0]
 qv,gv=theta[0]/6,theta[2];qpv,gpv=first[0]/6,first[2];qpp,gpp=second[0]/6,second[2]
 x2=qv*gv
 if x2<=0:raise RuntimeError('nonphysical reconstructed kinetic product')
 x=np.sqrt(x2);bv=qv/x
 Rv=-2*h1+2*qpv-2*h0*qv+2*qv*qv-qv*gv
 xp_over_x=.5*(qpv/qv+gpv/gv)
 xpp_over_x=.5*(qpp/qv-(qpv/qv)**2+gpp/gv-(gpv/gv)**2)+xp_over_x**2
 kap=-xpp_over_x-3*h0*xp_over_x-3*h1+2*qpv-6*h0*qv+4*qv*qv+3*(h0-qv)*Rv/gv
 tq,tg,tb,tk,tR=np.asarray(truth(*bg,*yy[5:].reshape(5,5)[0],ns['kvalues'][0]),float)
 errors={'q':abs(qv-tq)/(1+abs(tq)),'G':abs(gv-tg)/(1+abs(tg)),
         'b_magnitude':abs(abs(bv)-abs(tb))/(1+abs(tb)),'R':abs(Rv-tR)/(1+abs(tR)),
         'kappa':abs(kap-tk)/(1+abs(tk)),
         'Ctrace_compatibility':abs(theta[1]-(4*qpv+8*h0*qv-2*qv*qv-qv*gv)),
         'Ftrace_compatibility':abs(theta[3]-(gpv+3*(h0-qv)*gv-2*h1+2*qpv-2*h0*qv+2*qv*qv)),
         'overdetermined_residual':float(np.max(abs(d0@theta-y0)))}
 for key,value in errors.items():maximum[key]=max(maximum[key],float(value))
 sig=np.linalg.svd(d0,compute_uv=False);minimum_sigma=min(minimum_sigma,float(sig[-1]/sig[0]))
 rows.append({'t_E':float(tt),'recovered_trace_coefficients':theta.tolist(),'first':first.tolist(),'second':second.tolist(),
              'recovered_q':float(qv),'recovered_G':float(gv),'recovered_b_magnitude':float(abs(bv)),
              'recovered_R':float(Rv),'recovered_kappa':float(kap),'forward_truth':[float(tq),float(tg),float(tb),float(tk),float(tR)]})
for key,value in maximum.items():ck(key+' from pressure trace',value<2e-8,max_error=value)
ck('trace rank four at every sampled epoch',minimum_sigma>1e-5,min_relative_sigma=minimum_sigma)
files=['check_mode_trace_root_v1.py','MODE_TRACE_ROOT_DERIVATION_v1.md','check_mode_inverse_jets_v1.py',
       'independent_mode_inverse/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md']
out={'author':'/root','stage':'post-exposure personal derivation and integration of independently originated pressure-trace route',
     'independent_forward_code_claim':False,'empirical_validation':False,
     'scientific_input_reads':['check_mode_inverse_jets_v1.py: frozen author original-equation forward generator'],
     'integrity_read_paths':files,'checks':checks,'passed':sum(z['pass'] for z in checks),'failed':sum(not z['pass'] for z in checks),
     'rows':rows,'source_sha256':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in files}}
print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(int(out['failed']>0))
