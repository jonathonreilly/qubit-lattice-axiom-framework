from dev_engine import *
Mz=np.eye(4,dtype=complex); Mall=build_M_all(Mz)
g=6.0
H=box_H(5,(0,0,0),{r:g*Mall[r] for r in POS})
print(H.shape, abs(H-H.getH()).max())
w=spl.eigsh(H,k=40,sigma=g+1.0,which='LM',return_eigenvectors=False)
print(np.round(np.sort(w.real),6))
