import numpy as np,json,math
b=.23475690092702978;E=-4*(1+b);sig=(E+np.sqrt(E*E-16))/2
Dx=np.arctan(1/np.sqrt(b))/(2*np.pi);Dy=np.arctan(np.sqrt(b))/(2*np.pi*b);Dxy=1/(2*np.pi*np.sqrt(b));Dxx=2*(1+b)*Dx-2*b*Dxy;Dyy=2*(1+b)*Dy/b-2*Dxy/b
G=np.array([[Dxx-4*Dx,2*Dxy-2*Dx-2*Dy],[2*Dxy-2*Dx-2*Dy,Dyy-4*Dy]])
w,vs=np.linalg.eigh(sig*G);v=vs[:,-1];v*=np.sign(v[1]);A=-np.sqrt(2)*sig*np.dot(v,[Dx,Dy]);Q=2*np.arccos(b);q=Q/2-np.pi/2;theta=np.arccos(1+b-np.cos(q));ps=np.array([[theta,q],[-theta,q],[theta,q],[-theta,q]])
def h(x,y):
 aa=2*np.sin(np.asarray(x)/2)**2;bb=2*np.sin(np.asarray(y)/2)**2;den=aa+b*bb
 return sig/(2*np.sqrt(2))*np.divide(v[0]*aa+v[1]*bb,den,out=np.zeros(np.broadcast_shapes(np.shape(aa),np.shape(bb))),where=den>1e-28)
for L in [64,128,256,512,1024]:
 k=2*np.pi*(np.arange(L)+.5)/L;kx=k[:,None];ky=k[None,:];base=h(kx,ky)
 gs={}
 for typ,px in [(0,0),(1,2*theta),(-1,-2*theta)]:
  gs[typ]=float(np.mean(base*h(px-kx,-np.pi-ky))+2*A*h(px,-np.pi))
 total=0j
 for d in np.array([[1,0],[-1,0],[0,1],[0,-1]]):
  fd=np.exp(1j*Q*d[1]/2)*(v[0] if d[0] else v[1])/np.sqrt(2)
  for ia in range(4):
   for ib in range(4):
    if ia==ib:continue
    ic,id=[j for j in range(4) if j not in [ia,ib]];pc,pd=ps[ic],ps[id];s1=h(pc[0],pc[1]-Q/2)-fd*np.exp(-1j*np.dot(pc,d));s2=h(pd[0],pd[1]-Q/2)-fd*np.exp(-1j*np.dot(pd,d));typ=int(round((pc[0]+pd[0])/(2*theta)));gg=gs[typ]-fd**2*np.exp(-1j*np.dot(pc+pd,d));total+=4*np.exp(-1j*np.dot(ps[ib],d))*(s1*s2-gg)
 print(json.dumps(dict(L=L,v=v.tolist(),A=A,theta=theta,convolutions=gs,kernel_over_u2=[total.real,total.imag])),flush=True)
