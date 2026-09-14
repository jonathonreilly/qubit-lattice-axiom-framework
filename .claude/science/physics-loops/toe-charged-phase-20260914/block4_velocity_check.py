#!/usr/bin/env python3
"""Personal exploration: actual tensor/Peierls checks and a local shell limit."""
import json, math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

I=np.eye(2,dtype=complex)
sigma=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)
def mat(a):return np.einsum('...j,jab->...ab',a,sigma)
def symbol(k,v=1.,zeta=.4):
 k=np.asarray(k);s=np.sqrt(1-zeta*zeta)
 a=np.stack([np.sin(k[...,0]),np.sin(k[...,1]),(2+zeta-np.cos(k).sum(axis=-1))/s],axis=-1)*v
 return mat(a)
def vertex(k,j,v=1.,zeta=.4):
 k=np.asarray(k);a=np.zeros(k.shape,dtype=float);s=np.sqrt(1-zeta*zeta)
 if j<2:a[...,j]=np.cos(k[...,j])
 a[...,2]=np.sin(k[...,j])/s
 return v*mat(a)
def vertex_derivative(k,j,v=1.,zeta=.4):
 k=np.asarray(k);a=np.zeros(k.shape,dtype=float);s=np.sqrt(1-zeta*zeta)
 if j<2:a[...,j]=-np.sin(k[...,j])
 a[...,2]=np.cos(k[...,j])/s
 return v*mat(a)
def check_tensor_and_Ward():
 rng=np.random.default_rng(9140441);gm=wm=0.
 for _ in range(40):
  c=float(rng.uniform(.3,2.5));xi=float(rng.uniform(.1,3));omega=float(rng.normal());q=rng.uniform(-np.pi,np.pi,3)
  h=2*np.sin(q/2);Q=omega*omega+c*c*(h@h);k=np.r_[omega,h]
  B=np.zeros((4,4));B[0,0]=h@h;B[0,1:]=B[1:,0]=-omega*h
  B[1:,1:]=omega*omega*np.eye(3)+c*c*((h@h)*np.eye(3)-np.outer(h,h))
  gf=np.r_[omega,c*c*h];M=B+np.outer(gf,gf)/(c*c*xi)
  D=np.diag([c*c,1,1,1])/Q+(xi-1)*c*c*np.outer(k,k)/Q**2
  err=float(np.max(abs(M@D-np.eye(4))));gm=max(gm,err);assert err<2e-13
  assert np.linalg.eigvalsh(M).min()>0
  p=rng.uniform(-np.pi,np.pi,3);v=float(rng.uniform(.3,2));z=float(rng.uniform(.1,.8))
  diff=symbol(p+q/2,v,z)-symbol(p-q/2,v,z)
  w=sum(h[j]*vertex(p,j,v,z) for j in range(3));err=float(np.max(abs(diff-w)));wm=max(wm,err);assert err<1e-13
  # Temporal part of the same identity, D=i omega+h, W_0=i I.
  assert np.max(abs((1j*omega*I+diff)-(1j*omega*I+w)))<1e-13
 return {'cases':40,'true_inverse_max_error':gm,'Peierls_Ward_max_error':wm}
def check_residues():
 out=[]
 for c,v in [(1,.3),(1,.7),(1,1),(1,1.7),(1,3),(1.7,.8)]:
  i3=quad(lambda x:(1-x)/(x*v*v+(1-x)*c*c)**1.5,0,1,epsabs=1e-12)[0]
  i5=quad(lambda x:(1-x)/(x*v*v+(1-x)*c*c)**2.5,0,1,epsabs=1e-12)[0]
  assert abs(i3-2/(c*(c+v)**2))<1e-11
  assert abs(i5-2*(2*c+v)/(3*c**3*v*(c+v)**2))<1e-10
  ft=quad(lambda t:(v*v-t*t)/((t*t+v*v)**2*(t*t+c*c)),-np.inf,np.inf,epsabs=1e-12)[0]
  fs=quad(lambda t:(t*t+v*v/3)/((t*t+v*v)**2*(t*t+c*c)),-np.inf,np.inf,epsabs=1e-12)[0]
  at=(3*v*v-c*c)*i3/(8*np.pi**2);ass=(c*c+v*v)*c*c*i5/(8*np.pi**2)
  assert abs(at-(3*v*v-c*c)*ft/(4*np.pi**3))<1e-12
  assert abs(ass-(c*c+v*v)*fs/(4*np.pi**3))<1e-12
  target=(c-v)*(4*v*v+3*v*c+c*c)/(6*np.pi**2*c*(v+c)**2)
  assert abs(v*(ass-at)-target)<1e-12
  out.append({'c':c,'v':v,'A_t_over_e2':at,'A_s_over_e2':ass,'dv_dell_over_e2':target})
 return out

def shell_samples(nt=64,nu=12,nphi=24):
 x,wx=leggauss(nt);u,wu=leggauss(nu);phi=2*np.pi*np.arange(nphi)/nphi
 theta_t=np.pi*x/2;t=np.tan(theta_t);wt=wx*np.pi/2/np.cos(theta_t)**2
 vectors=np.stack([np.sqrt(1-u[:,None]**2)*np.cos(phi),np.sqrt(1-u[:,None]**2)*np.sin(phi),np.broadcast_to(u[:,None],(nu,nphi))],axis=-1).reshape(-1,3)
 wangle=np.repeat(wu,nphi)*2*np.pi/nphi
 directions=np.broadcast_to(vectors,(nt,len(vectors),3)).reshape(-1,3)
 times=np.repeat(t,len(vectors));weight=np.repeat(wt,len(vectors))*np.tile(wangle,nt)/(2*np.pi)**4
 return directions,times,weight

def local_lattice_shell(rho,v=1.,c=1.,zeta=.4,sign=1,quad_data=None):
 direction,t,weight=shell_samples() if quad_data is None else quad_data
 q=rho*direction;omega=rho*t;node=np.array([0.,0.,sign*np.arccos(zeta)])
 internal=node-q;mid=node-q/2
 H=symbol(internal,v,zeta);E2=np.real(np.einsum('nab,nba->n',H,H))/2
 S=(-1j*omega[:,None,None]*I+H)/(omega*omega+E2)[:,None,None]
 qhat=2*np.sin(q/2);Q=omega*omega+c*c*np.sum(qhat*qhat,axis=1)
 V=[vertex(mid,j,v,zeta) for j in range(3)]
 St=-1j*(S@S)
 corr=c*c*St-sum(a@St@a for a in V)
 coef_t=np.einsum('n,nab->ab',weight*rho**4/Q,corr)
 at=(np.trace(coef_t)/(2j)).real
 asp=[];off=[]
 for j in range(3):
  Sj=-S@vertex(internal,j,v,zeta)@S
  Vj=vertex_derivative(mid,j,v,zeta)
  corr=c*c*Sj-sum(a@Sj@a for a in V)-Vj@S@V[j]-V[j]@S@Vj
  coef=np.einsum('n,nab->ab',weight*rho**4/Q,corr)
  components=np.array([np.trace(s@coef).real/(2*v) for s in sigma]);components[2]*=sign
  asp.append(float(components[j]));components[j]=0;off.append(float(np.linalg.norm(components)))
 i3=2/(c*(c+v)**2);i5=2*(2*c+v)/(3*c**3*v*(c+v)**2)
 target_t=(3*v*v-c*c)*i3/(8*np.pi**2);target_s=(c*c+v*v)*c*c*i5/(8*np.pi**2)
 return {'rho':rho,'v':v,'c':c,'node_sign':sign,'time':float(at),'space':asp,'target_time':target_t,'target_space':target_s,'max_error':float(max(abs(at-target_t),max(abs(a-target_s) for a in asp))),'off_axis':off}

def main():
 result={'tensor_and_Ward':check_tensor_and_Ward(),'independent_residues':check_residues()}
 qd=shell_samples();rows=[]
 for v,c,sign in [(.7,1.,1),(1.,1.,1),(1.7,1.,-1)]:
  for rho in [.16,.08,.04,.02,.01]:
   r=local_lattice_shell(rho,v,c,sign=sign,quad_data=qd);rows.append(r);print(json.dumps(r),flush=True)
 result['local_lattice_shells']=rows
 # Local quadrature trends are falsifiers only; analytic remainder proof is separate.
 for v in [.7,1.,1.7]:
  group=[r for r in rows if r['v']==v]
  assert group[-1]['max_error']<group[0]['max_error']/20
  assert group[-1]['max_error']<2e-5
 result['scope']='leading one-loop local shell checks; not a full quantum phase or exact charged pole'
 Path(__file__).with_name('BLOCK4_VELOCITY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
 print('PASS: true gauge inverse, exact Peierls WTI, two residue integrals, and local lattice shell checks')
if __name__=='__main__':main()
