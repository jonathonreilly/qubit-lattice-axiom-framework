exec(open('b18lib.py').read())
FC=[np.add(*[np.array(d) for d in c]) for c in C.CORNERS]
D=lambda K: np.diag([np.exp(1j*np.dot(K,f)) for f in FC])
k=np.array([0.3,-0.2,0.9]); S2=SK(k)@SK(k)
print("S^2(k)=D(2k):",np.allclose(S2,D(2*k)),"or D(-2k):",np.allclose(S2,D(-2*k)))
for e in EX: print("S^2 period pi:",np.allclose(SK(k+np.pi*e)@SK(k+np.pi*e),S2))
