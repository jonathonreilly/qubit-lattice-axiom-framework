import numpy as np, sys; sys.path.insert(0,'.')
from offaxis import POLS, _expr
N=64; m=1.0
k1 = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
K = np.meshgrid(k1,k1,k1,indexing='ij')
for vtx in ['M','U']:
  for name in ['face1']:
    n,e = POLS[name]; n=np.array(n,float)
    s=[2*np.sin(k/2) for k in K]; spp=[np.cos(k/2) for k in K]; f=[a*b for a,b in zip(s,spp)]
    fp=[np.cos(k) for k in K]  # d/dk (sin k) = cos k  (f = 2 sin(k/2) cos(k/2) = sin k)
    tau = (lambda i,j: s[i]*s[j]) if vtx=='M' else (lambda i,j: f[i]*f[j])
    V = sum(e[i,j]*tau(i,j) for i in range(3) for j in range(3))
    if vtx=='M': dV = sum(n[k]*sum(e[i,j]*((spp[k]*s[j] if i==k else 0)+(spp[k]*s[i] if j==k else 0)) for i in range(3) for j in range(3)) for k in range(3))
    else: dV = sum(n[k]*sum(e[i,j]*((fp[k]*f[j] if i==k else 0)+(fp[k]*f[i] if j==k else 0)) for i in range(3) for j in range(3)) for k in range(3))
    W=V*V; DW=2*V*dV; S=sum(n[i]*f[i] for i in range(3)); ep=np.sqrt(m*m+sum(x*x for x in s))
    cf = (5/32)*np.mean(W*S*S/ep**7) - (1/32)*np.mean(W/ep**5) - (3/64)*np.mean(DW*S/ep**5)
    # numerical directional derivative check of DW
    h=1e-5; Kp=[k+h*n[i] for i,k in enumerate(K)]; Km=[k-h*n[i] for i,k in enumerate(K)]
    def Wf(KK):
        s_=[2*np.sin(k/2) for k in KK]; f_=[np.sin(k) for k in KK]
        t_=(lambda i,j: s_[i]*s_[j]) if vtx=='M' else (lambda i,j: f_[i]*f_[j])
        return sum(e[i,j]*t_(i,j) for i in range(3) for j in range(3))**2
    DWn=(Wf(Kp)-Wf(Km))/(2*h)
    print(vtx, name, 'grid closed form', cf, ' max|DW - DWnum|', np.abs(DW-DWnum).max() if False else np.abs(DW-DWn).max())
    ex = _expr(list(n), [[float(e[i,j]) for j in range(3)] for i in range(3)], vtx)
    print(ex[2][0])
