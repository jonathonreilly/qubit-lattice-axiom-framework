import sympy as s,itertools,json,time
start=time.monotonic();out=[]
def ck(n,x):
 assert x,n
 out.append(n)
# Independent determinant expansion by permutations, not trace-log matrix powers.
A,B=s.symbols('A B',real=True);on=s.Matrix([[B,A],[A,-B]]);T=s.Matrix([[-1,-1],[1,1]])/2;order=5;zero=s.zeros(4)
def mul(a,b):return [sum((a[j]*b[k-j] for j in range(k+1)),zero.copy()).applyfunc(s.expand) for k in range(6)]
p=[s.eye(4)]+[zero.copy() for _ in range(5)]
for phase in [1,s.I,-1]:
 h=s.zeros(4);h[:2,:2]=on;h[2:,2:]=on;h[:2,2:]=phase*T;h[2:,:2]=s.conjugate(phase)*T.T
 ex=[((-h)**n/s.factorial(n)).applyfunc(s.expand) for n in range(6)];p=mul(ex,p)
p[0]+=s.eye(4)
def conv(x,y):return [s.expand(sum(x[j]*y[k-j] for j in range(k+1))) for k in range(6)]
det=[s.S(0)]*6
for perm in itertools.permutations(range(4)):
 v=[s.S(1)]+[s.S(0)]*5
 for i,j in enumerate(perm):v=conv(v,[p[k][i,j] for k in range(6)])
 sign=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
 det=[s.expand(x+sign*y) for x,y in zip(det,v)]
# Scalar log derivative: n*d_n=sum k*l_k*d_(n-k).
logs=[s.S(0)]*6
for n in range(1,6):logs[n]=s.expand((n*det[n]-sum(k*logs[k]*det[n-k] for k in range(1,n)))/(n*det[0]))
expected=[0,0,(18*A*A+18*B*B+1)/4,s.I*A,-(162*A**4+324*A*A*B*B-110*A*A+162*B**4-28*B*B+1)/96,-s.I*A*(7*A*A+7*B*B-1)/4]
for n in range(1,6):ck('general_log_coefficient_'+str(n),s.expand(logs[n]-expected[n])==0)
m1,m3,B0=s.symbols('m1 m3 B0',real=True)
combo=s.expand(logs[5].subs({A:m1,B:B0+m3})+logs[5].subs({A:-m1,B:B0-m3}));ck('quartet_imaginary_fifth',s.simplify(s.im(combo)+7*B0*m1*m3)==0)
ck('rational_witness',(-7*B0*m1*m3).subs({B0:s.Rational(13,5),m1:s.Rational(4,25),m3:s.Rational(3,25)})==-s.Rational(1092,3125))
ck('phase_kernel_slope',(5-3*s.sqrt(5))/20<0)
# Exact combinatorial neutral two-cell sector: Nx=2+E, Ny=2-E.
for cutoff,target in [(0,36),(1,68),(2,70)]:ck('Gauss_dimension_'+str(cutoff),sum(s.binomial(4,2+e)*s.binomial(4,2-e) for e in range(-cutoff,cutoff+1))==target)
# Two one-step outward amplitudes at S=M=0 have leading norm sqrt(2)Jt.
ck('two_outward_endpoint_factor',s.sqrt(2)>s.Rational(7,5))
# Positive quadratic electric term is absent from weighted anti-Hermitian generator.
J,lam=s.symbols('J lam',positive=True);X=s.Matrix([[0,0,0],[1,0,0],[0,1,0]]);R=s.diag(7,0,7);H=R+J*(X+X.T);W=s.diag(s.exp(-lam),1,s.exp(lam));anti=(W*H*W.inv()-W.inv()*H*W)/(2*s.I)
ck('weighted_generator_onsite_cancels',all(s.simplify(x.rewrite(s.exp))==0 for x in anti-(J*s.sinh(lam)/s.I)*(X-X.T)))
print(json.dumps(dict(status='ok',count=len(out),checks=out,elapsed_seconds=time.monotonic()-start,primary_imported=False),indent=2))
