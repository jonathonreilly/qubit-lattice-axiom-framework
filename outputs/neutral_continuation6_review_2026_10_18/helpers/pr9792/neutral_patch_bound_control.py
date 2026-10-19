import numpy as np,json
rng=np.random.default_rng(182024)
checks=[]
R=6;n=R*R
for case in range(8):
 s=rng.choice([-1.,1.],(R,R));tx=np.zeros((n,n));ty=tx.copy()
 for x in range(R):
  for y in range(R):
   i=x*R+y;j=((x+1)%R)*R+y;tx[i,j]=tx[j,i]=-1
   j=x*R+(y+1)%R;ty[i,j]=ty[j,i]=-s[x,y]*s[x,(y+1)%R]
 T=tx+ty;D=-(tx-ty)@(tx-ty)/8
 inequality=8*(T+4*np.eye(n))-(tx-ty)@(tx-ty)
 assert np.linalg.eigvalsh(inequality)[0]>-1e-10
 psi=rng.normal(size=n)+1j*rng.normal(size=n);psi/=np.linalg.norm(psi)
 energy=np.vdot(psi,(T+4*np.eye(n))@psi).real
 F=0.
 for x in range(R):
  for y in range(R):
   p=s[x,y]*s[(x+1)%R,y]*s[x,(y+1)%R]*s[(x+1)%R,(y+1)%R]
   F+=(1-p)/2*sum(abs(psi[a*R+b])**2 for a,b in [(x,y),((x+1)%R,y),(x,(y+1)%R),((x+1)%R,(y+1)%R)])
 assert F<=8*energy+1e-10
 checks.append(dict(inequality_min=float(np.linalg.eigvalsh(inequality)[0]),F=float(F),eight_excess=float(8*energy)))
rows=[]
for lam in [.1,.03,.01,.003,.001]:
 ell=int(np.ceil(lam**(-.75)));R=2*int(np.ceil(2/lam))
 confinement=4*lam*(1-np.cos(np.pi/(ell+1)))
 reset=lam**4*(ell+8)**2
 rows.append(dict(lam=lam,ell=ell,R=R,ratio=float((confinement+reset)/lam**2.5)))
print(json.dumps(dict(status='pass',matrix_checks=checks,scaling_control=rows,scope='dimensionless illustrative bound constants; no fitted radius or finite-lambda error certificate')))
