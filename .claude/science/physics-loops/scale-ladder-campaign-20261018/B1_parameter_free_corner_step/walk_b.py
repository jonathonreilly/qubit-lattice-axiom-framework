exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
GROUP=[]
for Pr,sr in rots:
    for Pt,st in trans: GROUP.append((Pt[Pr], sr ^ st[Pr]))
def sym_pair(i,j,amp):
    T=np.zeros((nV,nV),complex)
    for P,s in GROUP:
        a=amp*(-1.0)**(int(s[i])+int(s[j])); T[P[i],P[j]]+=a; T[P[j],P[i]]+=np.conj(a)
    return T
X,Y,Z=(1,0,0),(0,1,0),(0,0,1); mX,mY=(-1,0,0),(0,-1,0)
i0=C.VID[((0,0,0),frozenset((X,Y)))]
jb1=C.VID[((0,0,1),frozenset((X,mY)))]; jb2=C.VID[((0,0,1),frozenset((mX,Y)))]
Tb1=sym_pair(jb1,i0,1.0); Tb1/=np.abs(Tb1).max()
Tb2=sym_pair(jb2,i0,1.0); Tb2/=np.abs(Tb2).max()
np.save('Tb1.npy',Tb1.real); np.save('Tb2.npy',Tb2.real)
for nm,T in (("Tb1",Tb1),("Tb2",Tb2)):
    print(nm,"real",np.allclose(T.imag,0),"T^2=2I",np.allclose(T@T,2*np.eye(nV)),"nnz/row",np.count_nonzero(np.abs(T[0])>1e-9),
          "inversion-even",np.allclose(conj(T,*invs[0]),T),"inversion maps to other", np.allclose(conj(T,*invs[0]),Tb2 if nm=="Tb1" else Tb1) or np.allclose(conj(T,*invs[0]),-(Tb2 if nm=="Tb1" else Tb1)))
