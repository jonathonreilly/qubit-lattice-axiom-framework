from ckmodel import *
print("EV_H", EV_H, "EV_L", EV_L, "S blocks", len(blS), "L blocks", len(blL))
Wk=W(np.array([0.3,0.7,-1.1])); print("unitary", np.allclose(Wk@Wk.conj().T, np.eye(12)))
# symmetry
rng=np.random.default_rng(1); ok=True
for g in range(48):
    for k in rng.uniform(-np.pi,np.pi,(3,3)):
        ok &= np.allclose(UF[g]@W(k)@UF[g].T, W(gk(g,k)))
print("all 48 lifts symmetric (U W U^T = W(gk)):", ok)
okp=all(np.allclose(UF[g]@W(k)@UF[g].T, W(gk(g,k))) for g in PROPER for k in rng.uniform(-np.pi,np.pi,(3,3)))
print("proper:", okp)
for k in CUBE:
    for E in (np.pi/2,-np.pi/2):
        Qm=level_at(k,E)
        if Qm is None: print(k/np.pi*2, E, None); continue
        a,B=weyl_B(k,Qm); sv=np.linalg.svd(B,compute_uv=False)
        print(np.round(k/np.pi*2).astype(int), round(E,3), Qm.shape[1], np.round(np.sort(sv),7), int(np.sign(np.linalg.det(B))), len(stab(k)))
