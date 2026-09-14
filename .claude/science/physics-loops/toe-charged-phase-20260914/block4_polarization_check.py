#!/usr/bin/env python3
"""Private analytic-derivative photon shell test; no fitted log coefficient."""
import json
from pathlib import Path
import numpy as np
from block4_velocity_check import I,sigma,symbol,vertex,vertex_derivative,shell_samples

def polarization_shell(rho,v=1.,zeta=.4,sign=1,quad_data=None):
 direction,t,weight=shell_samples() if quad_data is None else quad_data
 k=rho*direction;omega=rho*t;node=np.array([0.,0.,sign*np.arccos(zeta)])
 H=symbol(node+k,v,zeta);E2=np.einsum('nab,nba->n',H,H).real/2
 S=(-1j*omega[:,None,None]*I+H)/(omega*omega+E2)[:,None,None]
 vertices=[np.broadcast_to(1j*I,S.shape)]+[vertex(node+k,j,v,zeta) for j in range(3)]
 def coefficient(mu,nu,axis):
  W=vertices[axis]
  Sa=-S@W@S
  curvature=0 if axis==0 else vertex_derivative(node+k,axis-1,v,zeta)
  Saa=2*S@W@S@W@S
  if axis!=0:Saa-=S@curvature@S
  U=vertices[mu];V=vertices[nu]
  a=U@Saa@V@S/8+U@S@V@Saa/8-U@Sa@V@Sa/4
  out=np.dot(weight*rho**4,np.trace(a,axis1=1,axis2=2))
  return float(out.real),float(out.imag)
 # One two-component Weyl cone, before summing the actual four cones.
 values={'E_via_Pi11_p0':coefficient(1,1,0),'E_via_Pi00_p1':coefficient(0,0,1),
         'B_via_Pi22_p1':coefficient(2,2,1),'B_via_Pi11_p3':coefficient(1,1,3),
         'longitudinal_time':coefficient(0,0,0),'longitudinal_space':coefficient(1,1,1)}
 target_e=1/(12*np.pi**2*v);target_b=v/(12*np.pi**2)
 errors=[abs(values[x][0]-y) for x,y in [('E_via_Pi11_p0',target_e),('E_via_Pi00_p1',target_e),('B_via_Pi22_p1',target_b),('B_via_Pi11_p3',target_b),('longitudinal_time',0),('longitudinal_space',0)]]
 return {'rho':rho,'v':v,'node_sign':sign,'per_Weyl_cone':values,'target_E':target_e,'target_B':target_b,'maximum_residue_error':max(errors),'maximum_imaginary':max(abs(y[1]) for y in values.values())}

def check_full_lattice_Ward():
 rows=[]
 for N in [3,5,7]:
  k=2*np.pi*(np.array(list(__import__('itertools').product(range(N),repeat=3)))+np.array([.17,.29,.41]))/N-np.pi
  v=.8;zeta=.4
  for mode in [[1,0,0],[1,-1,1]]:
   q=2*np.pi*np.asarray(mode)/N;qhat=2*np.sin(q/2)
   H=symbol(k,v,zeta);Hplus=symbol(k+q,v,zeta)
   W=[np.broadcast_to(1j*I,H.shape)]+[vertex(k+q/2,j,v,zeta) for j in range(3)]
   for omega in [0.,.317,1.4,4.]:
    S=np.linalg.inv(1j*omega*I+H);Sp=np.linalg.inv(1j*omega*I+Hplus)
    bubble=np.array([[np.trace(U@Sp@V@S,axis1=1,axis2=2).mean() for V in W] for U in W])
    contact=np.zeros((4,4),dtype=complex)
    for j in range(3):contact[j+1,j+1]=-np.trace(S@vertex_derivative(k,j,v,zeta),axis1=1,axis2=2).mean()
    total=bubble+contact
    residue=np.r_[0,qhat]@total;error=float(np.max(abs(residue)))
    scale=max(1.,float(np.linalg.norm(total)));assert error<2e-12*scale
    omitted=float(np.max(abs(np.r_[0,qhat]@bubble)))
    rows.append({'N':N,'mode':mode,'omega':omega,'full_Ward_error':error,'without_contact_error':omitted})
 assert max(r['without_contact_error'] for r in rows)>.01
 # Nonzero temporal transfer requires an actual continuous-frequency integral.
 for N in [3,5]:
  spatial=2*np.pi*(np.array(list(__import__('itertools').product(range(N),repeat=3)))+np.array([.17,.29,.41]))/N-np.pi
  xx,ww=np.polynomial.legendre.leggauss(128);angle=np.pi*xx/2
  om=np.tan(angle);weights=ww/(4*np.cos(angle)**2)
  k=np.tile(spatial,(len(om),1));omega=np.repeat(om,len(spatial))
  weight=np.repeat(weights,len(spatial))/len(spatial)
  q=2*np.pi*np.array([1,0,-1])/N;q0=.41
  H=symbol(k,.8,.4);Hp=symbol(k+q,.8,.4)
  S=np.linalg.inv(1j*omega[:,None,None]*I+H);Sp=np.linalg.inv(1j*(omega+q0)[:,None,None]*I+Hp)
  W=[np.broadcast_to(1j*I,H.shape)]+[vertex(k+q/2,j,.8,.4) for j in range(3)]
  bubble=np.array([[np.dot(weight,np.trace(U@Sp@V@S,axis1=1,axis2=2)) for V in W] for U in W])
  contact=np.zeros((4,4),dtype=complex)
  for j in range(3):contact[j+1,j+1]=-np.dot(weight,np.trace(S@vertex_derivative(k,j,.8,.4),axis1=1,axis2=2))
  total=bubble+contact;qh=np.r_[q0,2*np.sin(q/2)]
  error=float(np.max(abs(qh@total)));assert error<2e-10
  rows.append({'N':N,'mode':[1,0,-1],'external_frequency':q0,'frequency_quadrature_nodes':128,'full_Ward_error':error,'without_contact_error':float(np.max(abs(qh@bubble)))})
 return rows

def main():
 qd=shell_samples();rows=[]
 for v,sign in [(.7,1),(1.,1),(1.7,-1)]:
  for rho in [.16,.08,.04,.02,.01]:
   r=polarization_shell(rho,v,sign=sign,quad_data=qd);rows.append(r);print(json.dumps(r),flush=True)
 for v in [.7,1.,1.7]:
  rs=[r for r in rows if r['v']==v]
  assert rs[-1]['maximum_residue_error']<rs[0]['maximum_residue_error']/20
  assert rs[-1]['maximum_residue_error']<2e-5
 result={'full_static_lattice_Ward':check_full_lattice_Ward(),'local_lattice_photon_shells':rows,'scope':'analytic second external-momentum derivatives of the actual Peierls bubble; each local cone is one Weyl, not one Dirac; full lattice Ward identity also requires the momentum-independent seagull'}
 Path(__file__).with_name('BLOCK4_POLARIZATION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
 print('PASS: per-Weyl electric/magnetic residues and longitudinal residue cancellation')
if __name__=='__main__':main()
