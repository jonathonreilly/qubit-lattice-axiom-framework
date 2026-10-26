from fiber import *
N=8; m=(1,2)
K,H,H2,P=build(N,*m)
# free spectrum check
w=np.linalg.eigvalsh(H.toarray())
eps=lambda k: np.sqrt(np.sin(k[0])**2+np.sin(k[1])**2)
pred=[]
for a in range(N):
    for b in range(N):
        k1=2*np.pi*np.array([a,b])/N; k2=K-k1
        for s1 in (1,-1):
            for s2 in (1,-1): pred.append(s1*eps(k1)+s2*eps(k2))
print("spectrum match:",np.abs(np.sort(w)-np.sort(pred)).max())
for comp in (0,1):
    J=build_J(N,K,comp)
    print("J hermitian",abs(J-J.getH()).max())
    # free J0 eigen: plane waves
    # build free-only J (no exclusion) by template everywhere would be scalar; test: commutator of J with H2 zero away from window; and O norm
    O=H2@J-J@H2
    print(comp,"||[H2,J]||max entry",abs(O).max(), "||[H,J]|| (unprojected H)",abs(H@J-J@H).max())
    # J on plane wave far from origin should equal scalar: apply J to unprojected eigenvector? use H eigenvectors -> J-expect
    # scalar check: <J> in eigenstates of H should equal 1/2(sin2k1+sin2k2)_comp  for generic eigenvectors where nondegenerate: test Rayleigh
