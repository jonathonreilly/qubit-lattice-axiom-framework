from pathlib import Path
import importlib.util,json,time,numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('core',HERE/'check_block10.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
def dvector(k,zeta):return np.stack([np.sin(k[...,0]),np.sin(k[...,1]),2+zeta-np.cos(k[...,0])-np.cos(k[...,1])-np.cos(k[...,2])],axis=-1)
def pauli(v):return np.einsum('...i,ijk->...jk',v,np.array(c.SIG))
def first(k,axis):
 out=np.zeros(k.shape);out[...,2]=np.sin(k[...,axis])
 if axis<2:out[...,axis]=np.cos(k[...,axis])
 return pauli(out)
def second(k,axis):
 out=np.zeros(k.shape);out[...,2]=np.cos(k[...,axis])
 if axis<2:out[...,axis]=-np.sin(k[...,axis])
 return pauli(out)
def native_shell(radius,ratio,n,w,zeta=.7):
 vel=np.sqrt(1-zeta*zeta);D=np.array([1,1,vel]);momentum=radius*n[:,1:]/D;omega=radius*n[:,0];I=np.eye(2,dtype=complex)
 denominator=omega**2+np.sum((2*D*np.sin(momentum/2))**2,axis=1)
 self_rows=[];electric=np.zeros(3,complex);magnetic=np.zeros((3,3),complex)
 for chir in [-1,1]:
  node=np.array([0,0,chir*np.arccos(zeta)]);internal=node-momentum;mid=node-momentum/2
  h=pauli(ratio*dvector(internal,zeta));G=(1j*omega[:,None,None]*I+h)/(omega**2+np.sum((ratio*dvector(internal,zeta))**2,axis=1))[:,None,None]
  vertices=[1j*I]+[ratio/D[i]*first(mid,i) for i in range(3)]
  correction_time=sum((V@G@(1j*G)@V for V in vertices),np.zeros_like(G))
  z0=np.sum(w*radius**4/denominator*np.trace(correction_time,axis1=-2,axis2=-1)/(2j))
  zs=[]
  for axis in range(3):
   derivative=ratio/D[axis]*first(internal,axis);corr=sum((V@G@derivative@G@V for V in vertices),np.zeros_like(G))
   dV=ratio/D[axis]**2*second(mid,axis);V=vertices[axis+1];corr-=dV@G@V+V@G@dV
   alpha=c.SIG[axis]*(chir if axis==2 else 1)
   # The two-photon Peierls contact also contributes to the inverse
   # fermion propagator. Its velocity shell is O(radius^2).
   tadpole=-np.sum(w*radius**4/denominator)/(2*D[axis]**2)
   zs.append(np.sum(w*radius**4/denominator*np.trace(alpha@corr,axis1=-2,axis2=-1)/(2*ratio))+tadpole)
  self_rows.append([z0,*zs])
  # Fermion-only photon loop, with no extra photon propagator.
  current=[ratio/D[i]*first(internal,i) for i in range(3)]
  for i in range(3):
   Vi=current[i];electric[i]+=np.sum(w*radius**4*(-np.trace(Vi@G@Vi@G@G@G,axis1=-2,axis2=-1)))
   for j in range(3):
    if i==j:continue
    Wj=current[j];Tj=ratio/D[j]**2*second(internal,j)
    second_G=G@Wj@G@Wj@G-.5*G@Tj@G
    magnetic[i,j]+=np.sum(w*radius**4*np.trace(Vi@G@Vi@second_G,axis1=-2,axis2=-1))
 return np.array(self_rows),electric,magnetic
if __name__=='__main__':
 n,w=c.sphere_grid(32,20,40);start=time.monotonic();rows=[]
 for ratio in [.8,1.2]:
  target=np.array([-(1-3*ratio**2)*2/(1+ratio)**2]+[(1+ratio**2)*2*(2+ratio)/(3*ratio*(1+ratio)**2)]*3)
  for rad in [.2,.1,.05,.025]:
   sf,el,mag=native_shell(rad,ratio,n,w);res=dict(ratio=ratio,radius=rad,self_real=sf.real.tolist(),self_error=float(np.max(np.abs(sf-target))),electric_real=el.real.tolist(),electric_error=float(np.max(abs(el-4/(3*ratio)))),magnetic_real=mag.real.tolist(),magnetic_error=float(max(abs(mag[i,j]-4*ratio/3) for i in range(3) for j in range(3) if i!=j)),max_imag=float(max(np.max(abs(sf.imag)),np.max(abs(el.imag)),np.max(abs(mag.imag)))))
   rows.append(res)
 result=dict(elapsed_seconds=time.monotonic()-start,rows=rows)
 (HERE/'BLOCK10_NATIVE_SHELL_EXPLORATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
