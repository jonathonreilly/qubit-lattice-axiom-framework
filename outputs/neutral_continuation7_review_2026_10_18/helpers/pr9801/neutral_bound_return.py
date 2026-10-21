AUDIT_TIMEOUT_SEC=300
import numpy as np,json,math
R=14;n=R*R
s=np.ones((R,R),dtype=np.int64);s[0,0]=s[1,0]=-1
T=np.zeros((n,n),dtype=np.int64);T0=T.copy()
for x in range(R):
 for y in range(R):
  i=x*R+y
  for dx,dy in [(1,0),(0,1)]:
   xx=(x+dx)%R;yy=(y+dy)%R;j=xx*R+yy
   T[i,j]=T[j,i]=-1 if dx else -s[x,y]*s[xx,yy]
   T0[i,j]=T0[j,i]=-1
P=np.eye(n,dtype=np.int64);P0=P.copy();mom=[]
for k in range(1,11):
 P=P@T;P0=P0@T0;mom.append(dict(n=k,trace_difference=int(np.trace(P)-np.trace(P0))))
e=np.linalg.eigvalsh(T);e0=np.linalg.eigvalsh(T0)
rows=[]
for tau in [.1,.2,.4]:
 tr=float(np.sum(np.cos(tau*e))-np.sum(np.cos(tau*e0)))
 rows.append(dict(tau=tau,trace_difference=tr,scaled=tr/tau**4))
print(json.dumps(dict(R=R,moments=mom,returns=rows,expected_limit=-8/3),indent=2))
