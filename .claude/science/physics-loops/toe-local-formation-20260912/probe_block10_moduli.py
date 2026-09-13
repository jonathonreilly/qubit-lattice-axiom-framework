"""Exact constant-metric projections of the scalar cubic Regge term."""
import itertools,json,time,hashlib
from pathlib import Path
import sympy as s
start=time.monotonic();A,B,h=s.symbols('A B h',real=True)
components=[(a,a) for a in range(4)]+list(itertools.combinations(range(4),2))
pairs=list(itertools.combinations(range(5),2));normals=[s.Matrix([-1,0,0,0]),s.Matrix([1,-1,0,0]),s.Matrix([0,1,-1,0]),s.Matrix([0,0,1,-1]),s.Matrix([0,0,0,1])]
result=[0]*10
for perm in itertools.permutations(range(4)):
    vertices=[(0,0,0,0)]
    for ax in perm:
        v=list(vertices[-1]);v[ax]=1;vertices.append(tuple(v))
    def edge(i,j):
        if i==j:return 0
        v,w=vertices[min(i,j)],vertices[max(i,j)];st=[w[a]-v[a] for a in range(4)]
        return (st[3]-sum(st[:3]))*((B if v[0] else A)+(B if w[0] else A))
    H=s.zeros(4)
    for a in range(1,5):
        H[a-1,a-1]=edge(a-1,a)
        for b in range(a+1,5):H[a-1,b-1]=H[b-1,a-1]=(edge(a,b-1)+edge(a-1,b)-edge(a,b)-edge(a-1,b-1))/2
    for i,j in pairs:
        ni,nj=normals[i],normals[j];a,b,c=ni.dot(ni),ni.dot(nj),nj.dot(nj);det=a*c-b*b
        N=ni.row_join(nj);P=s.eye(4)-N*(N.T*N).inv()*N.T
        u=(ni.T*H*ni)[0]/a;v=(nj.T*H*nj)[0]/c;B1=(ni.T*H*nj)[0]
        HH=H*H;U=(ni.T*HH*ni)[0]/a;V=(nj.T*HH*nj)[0]/c;B2=(ni.T*HH*nj)[0]
        s1=(u+v)/2;s2=3*(u*u+v*v)/8+u*v/4-(U+V)/2
        W=B1-b*s1;Z=-b*s2+B1*s1-B2;t=s.trace(P*H);cA=t*t/8-s.trace(P*H*P*H)/4
        for ix,(aa,bb) in enumerate(components):
            K=s.zeros(4);K[aa,bb]=K[bb,aa]=1
            D=K.extract(perm,perm);dHH=H*D+D*H
            du=(ni.T*D*ni)[0]/a;dv=(nj.T*D*nj)[0]/c;dB1=(ni.T*D*nj)[0]
            dU=(ni.T*dHH*ni)[0]/a;dV=(nj.T*dHH*nj)[0]/c;dB2=(ni.T*dHH*nj)[0]
            ds1=(du+dv)/2;ds2=3*(u*du+v*dv)/4+(du*v+u*dv)/4-(dU+dV)/2
            dW=dB1-b*ds1;dZ=-b*ds2+dB1*s1+B1*ds1-dB2;dt=s.trace(P*D)
            dcA=t*dt/4-s.trace(P*D*P*H)/2
            derivative=dt*Z/12+t*dZ/12-b*(dt*W*W+2*t*W*dW)/(24*det)+dcA*W/3+cA*dW/3
            result[ix]+=s.expand(derivative)
result=[s.factor(x) for x in result]
print(dict(zip(map(str,components),map(str,result))))
out=dict(components=components,projections=list(map(str,result)),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_sec=time.monotonic()-start,scope='first exact constant-metric coefficient extraction')
Path(__file__).with_name('BLOCK10_MODULI_FIRST.json').write_text(json.dumps(out,indent=2)+'\n')
