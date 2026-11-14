import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, scipy.linalg as sl
import t2_opt_extension as t
for L in (4,8):
    n,a,om,E,par=t.build(L,"flat")
    N=n**3;d=3;w0,w1=a**d,a**(d-2)
    A=(w0*sp.identity(N)+w1*t.lap(N,E)).tocsr()
    both=om[E[:,0]]&om[E[:,1]]
    Gf=(w0*sp.diags(om.astype(float))+w1*t.lap(N,E,both)).tocsr()
    iO,iY=np.where(om)[0],np.where(~om)[0]
    AOO=A[iO][:,iO].toarray();AOY=A[iO][:,iY].toarray();AYY=A[iY][:,iY].toarray();G=Gf[iO][:,iO].toarray()
    def C(ix):
        u=np.unique(par[ix]);return np.array([(par[ix]==p).astype(float) for p in u])
    CO,CY=C(iO),C(iY)
    # exact dense
    ZO=sl.null_space(CO);ZY=sl.null_space(CY)
    Yp=ZY.T@AYY@ZY
    S=AOO-AOY@ZY@np.linalg.solve(Yp,ZY.T@AOY.T)
    ev=sl.eigh(ZO.T@S@ZO,ZO.T@G@ZO,eigvals_only=True)
    print("L",L,"exact dense A",ev[-1],ev[-2],"t2 run",t.run(L,"flat"))
