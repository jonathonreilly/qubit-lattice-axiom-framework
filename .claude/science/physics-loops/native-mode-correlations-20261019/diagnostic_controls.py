"""Independent covariance algebra and residual/visibility predicate controls."""
import json
import numpy as np
AUDIT_TIMEOUT_SEC = 60

def checked(E,V,H,weights):
 residual=np.linalg.norm(H@V-V*E,axis=0)
 assert np.max(residual)<1e-9
 return [j for j in range(1,len(E)) if weights[j]>1e-8]

def main():
 rng=np.random.default_rng(191919);z=np.diag([1.,-1.]);I=np.eye(2)
 B=[np.kron(z,I),np.kron(I,z),np.kron(z,z)]
 M=rng.normal(size=(4,4));H=(M+M.T)/2;E,V=np.linalg.eigh(H)
 rho=(np.outer(V[:,1],V[:,1])+np.outer(V[:,2],V[:,2]))/2
 means=np.array([np.trace(rho@b) for b in B]);direct=np.array([[np.trace(rho@b@c) for c in B] for b in B])-np.outer(means,means)
 act=np.array([np.array([b@V[:,k] for b in B]) for k in [1,2]])
 via=sum(s@s.T for s in act)/2-np.outer(means,means)
 assert np.max(abs(via-direct))<1e-12
 angle=.731;R=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
 W=V[:,1:3]@R
 assert np.max(abs(W@W.T/2-rho))<1e-12
 # The missing centering mutation must fail on this nonzero-mean fixture.
 uncentered=sum(s@s.T for s in act)/2
 assert np.max(abs(uncentered-direct))>1e-3
 assert checked(E,V,H,[0,0,.2,0])==[2]
 try:checked(E+.1,V,H,[0,0,.2,0])
 except AssertionError:detected=True
 else:detected=False
 assert detected
 assert checked(E,V,H,[0,0,0,0])==[]
 print(json.dumps(dict(covariance_error=float(np.max(abs(via-direct))),centering_mutation_error=float(np.max(abs(uncentered-direct))),energy_shift_mutation_detected=detected,zero_visibility_selected=[])))
if __name__=='__main__':main()
