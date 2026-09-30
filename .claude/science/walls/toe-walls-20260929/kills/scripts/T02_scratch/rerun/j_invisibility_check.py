"""T02 script C: what the record-level odds see of the generator's numbers.
Compressed field on an isolated site h = sum_f M_f q_f (landed Theorem 2), odds (1 + lam p.h^)/2 (landed Thm 3).
Heisenberg: M_f = J I.  Full soldering: M_f = J I + K f f^T + D [f], [f] v = f x v."""
import numpy as np
rng = np.random.default_rng(3)
F = [np.array(v,float) for v in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))]
def cross_mat(f): return np.array([[0,-f[2],f[1]],[f[2],0,-f[0]],[-f[1],f[0],0]])
def field(q, J, K=0.0, D=0.0):
    h = np.zeros(3)
    for f,qf in zip(F,q):
        M = J*np.eye(3) + K*np.outer(f,f) + D*cross_mat(f)
        h += M@qf
    return h
def unit(v): return v/np.linalg.norm(v)
worst_scale, worst_sign, worst_ratio = 0, 0, []
for _ in range(2000):
    q = rng.normal(size=(6,3)); q/= np.linalg.norm(q,axis=1,keepdims=True)
    h1 = unit(field(q,1.0)); h2 = unit(field(q,7.3)); h3 = unit(field(q,-1.0))
    worst_scale = max(worst_scale, np.linalg.norm(h1-h2))
    worst_sign  = max(worst_sign, np.linalg.norm(h1+h3))      # sign flip => direction flips exactly (c = lam sgn J)
print(f"Heisenberg: max |h^(J) - h^(7.3 J)| = {worst_scale:.2e}; max |h^(J) + h^(-J)| = {worst_sign:.2e}")
# soldered: scaling all three invariant; ratios matter
mx = 0; ang=[]
for _ in range(500):
    q = rng.normal(size=(6,3)); q/= np.linalg.norm(q,axis=1,keepdims=True)
    a = unit(field(q,1.0,0.6,0.3)); b = unit(field(q,5.0,3.0,1.5)); c = unit(field(q,1.0,1.6,0.3))
    mx = max(mx, np.linalg.norm(a-b)); ang.append(np.degrees(np.arccos(np.clip(a@c,-1,1))))
print(f"soldered: scaling (J,K,D) by 5 changes direction by <= {mx:.2e}; changing K/J 0.6->1.6 rotates it by median {np.median(ang):.1f} deg")
