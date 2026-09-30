"""Kill check on T36 P3: is the '1.3e5 stiffness spread' an isotropy problem at any momentum, or only for p << m_min?
Same corner model / build_D as attacker's t36_p3_locking.py; scan |E0(p)| along each axis and report the local speed dE/dp."""
import numpy as np
I2=np.eye(2,dtype=complex); SX=np.array([[0,1],[1,0]],dtype=complex); SY=np.array([[0,-1j],[1j,0]],dtype=complex); SZ=np.diag([1,-1]).astype(complex)
def kr(*ms):
    o=np.array([[1.0+0j]])
    for m in ms: o=np.kron(o,m)
    return o
XI=[kr(SX,I2,I2),kr(SZ,SX,I2),kr(SZ,SZ,SX)]; GAM=[kr(SY,I2,I2),kr(SZ,SY,I2),kr(SZ,SZ,SY)]
HW=np.array([bin(s).count("1") for s in range(8)]); axis_state=[4,2,1]
def Hb(q): return sum((1+np.cos(q[a]))*XI[a]+np.sin(q[a])*GAM[a] for a in range(3))
def build_D(m,heavy=5.0):
    D=np.zeros((8,8),dtype=complex)
    for s in range(8):
        if HW[s]>=2: D[s,s]=heavy
    for i,a in enumerate(axis_state): D[a,a]=m[i]
    return D
def E0(p,D):
    w,U=np.linalg.eigh(Hb(np.pi+np.asarray(p))+D); return w[int(np.argmax(np.abs(U[0,:])**2))]
m=(1.0,7.4e-3,7.5e-6); D=build_D(m)
print("hw=0 branch energy E0(p) along each axis; local speed v=|dE0/dp| at p ; masses",m)
for p in (1e-9,1e-7,1e-5,1e-3,1e-2,1e-1):
    row=[]
    for a in range(3):
        d=np.zeros(3); d[a]=p; h=p*1e-3
        d2=np.zeros(3); d2[a]=p+h; d1=np.zeros(3); d1[a]=p-h
        v=abs(E0(d2,D)-E0(d1,D))/(2*h); row.append(v)
    print(f"  p={p:8.0e}  speed along axes (m=1, 7.4e-3, 7.5e-6): {row[0]:.3e} {row[1]:.3e} {row[2]:.3e}")
