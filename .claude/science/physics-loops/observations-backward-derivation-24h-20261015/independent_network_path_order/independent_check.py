from pathlib import Path
import sympy as s,json
I=s.eye(3);K=s.Matrix([[4,-1,0],[-1,5,-1],[0,-1,6]]);O=s.Matrix([[1,0,0],[0,s.Rational(3,5),-s.Rational(4,5)],[0,s.Rational(4,5),s.Rational(3,5)]]);P=O*K*O.T;e=s.Matrix([1,0,0]);w=s.Matrix([0,1,-1]);theta=s.Rational(2,3)
matrices=[('chain',K,w),('rotated',P,w),('equal_distance_late',s.Matrix([[4,-1,-1],[-1,5,-1],[-1,-1,6]]),w),('equal_distance_invisible',s.Matrix([[3,-1,-1],[-1,3,-1],[-1,-1,3]]),w)]
rows=[]
for name,A,v in matrices:
 mu=[(v.T*A**j*e)[0] for j in range(3)];d=next((j for j,x in enumerate(mu) if x!=0),None);B=A+theta*v*v.T
 if d is None:
  assert all((e.T*(A**j-B**j)*e)[0]==0 for j in range(12));rows.append({'name':name,'invisible':True});continue
 for n in range(2*d+1):assert (e.T*(A**n-B**n)*e)[0]==0
 leading=(-1)**(2*d+1)*(e.T*(A**(2*d+1)-B**(2*d+1))*e)[0]
 assert leading==theta*mu[d]**2
 rows.append({'name':name,'d':d,'mu':str(mu[d]),'degree':4*d+3,'coefficient':str(leading/s.factorial(4*d+3))})
assert s.simplify((O*(K+theta*w*w.T)*O.T)-(P+theta*(O*w)*(O*w).T))==s.zeros(3)
# Direct chain paths show increasing d for successively deeper edges.
for size in range(2,7):
 A=4*s.eye(size)
 for j in range(size-1):A[j,j+1]=A[j+1,j]=-1
 ee=s.eye(size)[:,0]
 for j in range(size-1):
  vv=s.eye(size)[:,j]-s.eye(size)[:,j+1]
  assert all((vv.T*A**n*ee)[0]==0 for n in range(j))
  assert (vv.T*A**j*ee)[0]==(-1)**j
rows.append({'chain_distance_checks':'all edges for sizes2..6'})
Path(__file__).with_name('independent_results.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows))
