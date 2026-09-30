"""T02 script D: two ADJACENT unrecorded sites under the compressed Heisenberg generator.
Does the ground-state one-site odds at x depend on the fields at y (records two steps from x)?
(Re-check of the landed isolation theorem; sets the size of the second supplied clause.)"""
import numpy as np, scipy.linalg as sl
rng = np.random.default_rng(11)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2); S=[sx,sy,sz]
def H(J,hx,hy):
    return J*sum(np.kron(s,s) for s in S)+np.kron(sum(h*s for h,s in zip(hx,S)),I2)+np.kron(I2,sum(h*s for h,s in zip(hy,S)))
def bloch_x(J,hx,hy):
    w,v = np.linalg.eigh(H(J,hx,hy)); g=v[:,0]; rho=np.outer(g,g.conj()).reshape(2,2,2,2)
    rx=np.einsum('abcb->ac',rho); return np.array([np.trace(rx@s).real for s in S])
for J in (-1.0,1.0):
    d=[]
    for _ in range(400):
        hx=rng.normal(size=3); hy=rng.normal(size=3); hy2=rng.normal(size=3)
        d.append(np.linalg.norm(bloch_x(J,hx,hy)-bloch_x(J,hx,hy2)))
    print(f"J={J:+.0f}: median change of the odds Bloch vector at x when only y's neighbour records change: {np.median(d):.3f} (max {np.max(d):.3f})")
# isolated reference: x alone in field hx (all neighbours recorded) does not see y at all
print("isolated site: Bloch vector = -h^ exactly, independent of everything beyond its six neighbours (landed Thm 2/3).")
