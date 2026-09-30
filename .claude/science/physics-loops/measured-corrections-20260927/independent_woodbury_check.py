"""Test exact diagonal W2 block and reduced equation from independent states."""
import contextlib,io,json
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    from independent_joint_check import build
rows=[]
for S in (3,5,8):
    states,w,P,T,comp=build(S)
    Q=np.flatnonzero(w==1);R=np.flatnonzero(w==2)
    A=T[np.ix_(Q,P)];B=T[np.ix_(R,Q)];Z=B@A
    m=np.array([states[i][1][0] for i in R]);n=np.array([states[i][1][0] for i in P]);C=S*(S+1)
    d=1-m*(m+1)/C; bb_error=np.max(abs(B@B.T-np.diag(4*d)))
    x=.04;delta=1.7;K=delta/(x*C)
    for lam in (-.04,.02):
        physical_E=delta*lam/x**2
        original=(4*x*np.eye(len(P))-x*A.T@np.linalg.inv((1-lam)*np.eye(len(Q))-x*(B.T@B)/(2-lam))@A-lam*np.eye(len(P)))
        rr=(1-lam)*(2-lam)-4*x*d
        reduced=np.diag(4*K*n*n)-delta*Z.T@np.diag(1/rr)@Z-physical_E*(1+4*x-lam)*np.eye(len(P))
        error=np.max(abs(reduced-original*(1-lam)*delta/x**2))
        rows.append(dict(S=S,lambda_value=lam,BBstar_diagonal_error=float(bb_error),reduced_equation_error=float(error)))
print(json.dumps(rows,indent=2))

AUDIT_TIMEOUT_SEC = 180
