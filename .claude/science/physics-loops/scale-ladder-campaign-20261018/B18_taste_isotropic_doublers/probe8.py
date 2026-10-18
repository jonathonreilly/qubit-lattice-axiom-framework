exec(open('b18lib.py').read())
def parse(un):
    U=np.eye(12,dtype=complex)
    for part in un.split("*"):
        U=U@(UHf(int(part[1]),int(part[2])) if part[0]=="H" else ULf(int(part[1]),int(part[2]),int(part[3])))
    return U
U=parse('L202'); W=lambda k: SK(k)@U
print("U diag?",np.allclose(U,np.diag(np.diag(U))), "U^2=1?",np.allclose(U@U,np.eye(12)))
print(np.round(U,3).real)
k=np.array([0.3,0.5,-0.7])
a=np.sort(np.angle(np.linalg.eigvals(W(k)))); b=np.sort(np.angle(np.linalg.eigvals(W(k+np.pi*EX[0]))))
print(np.round(a,4)); print(np.round(b,4))
blW=blocks_of(W,list(blS))
for phi in (1,-1,1j,-1j):
    B,_=intertwiners(blW,shifted(blW,EX[0],phi),r=0); print("phase",phi,"dim",len(B),"inv",generic_invertible(B))
print("levels at k*",[(round(E,4),m) for E,m in levels(W,kst)])
print("levels at k*+pi ex",[(round(E,4),m) for E,m in levels(W,kst+np.pi*EX[0])])
