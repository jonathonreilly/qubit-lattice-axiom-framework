import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
import t2_opt_extension as t
L=4
n,a,om,E,par=t.build(L,"flat")
N=n**3;d=3;w0,w1=a**d,a**(d-2)
A=(w0*sp.identity(N)+w1*t.lap(N,E)).tocsr()
both=om[E[:,0]]&om[E[:,1]]
Gf=(w0*sp.diags(om.astype(float))+w1*t.lap(N,E,both)).tocsr()
iO,iY=np.where(om)[0],np.where(~om)[0]
GOO=Gf[iO][:,iO].tocsc();AOO=A[iO][:,iO].tocsc();AOY=A[iO][:,iY].tocsc();AYY=A[iY][:,iY].tocsc()
def means(ix):
    u,inv=np.unique(par[ix],return_inverse=True)
    return sp.csc_matrix((np.ones(len(ix)),(inv,np.arange(len(ix)))),shape=(len(u),len(ix)))
CY=means(iY);CO=means(iO)
print("shapes",CY.shape,CO.shape,"row sums",np.asarray(CY.sum(1)).ravel()[:4])
KY=sp.bmat([[AYY,CY.T],[CY,None]],format="csc")
for reg in (1e-14,0):
    M=KY+reg*sp.identity(KY.shape[0],format="csc") if reg else KY
    lu=sla.splu(M)
    rng=np.random.default_rng(0)
    b=np.concatenate([rng.standard_normal(len(iY)),np.zeros(CY.shape[0])])
    x=lu.solve(b)
    print("reg",reg,"resid",np.linalg.norm(KY@x-b),"C x",np.linalg.norm(CY@x[:len(iY)]))
KO=sp.bmat([[GOO,CO.T],[CO,None]],format="csc")
print("nnz checks", KO.shape, (KO-KO.T).nnz)
