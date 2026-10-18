exec(open('b18lib.py').read())
# explicit diagonal taste candidate for H_link
for i in range(3):
    ei=tuple(int(x) for x in EX[i])
    Vd=np.diag([(-1.0)**(ei in c) for c in C.CORNERS])
    ok=[np.allclose(Vd@HL(k)@Vd, w*HL(k+np.pi*EX[i])) for w in (1,-1) for k in [np.array([0.3,0.5,-0.9])]]
    print("axis",i,"V diag (-1)^[+e_i in c]: commutes/anticommutes with H_link shift",ok,
          " [V,H_on]=0:",np.allclose(Vd@Hon0,Hon0@Vd)," [V,Lam]=0:",np.allclose(Vd@Lam,Lam@Vd),"{V,Lam}=0:",np.allclose(Vd@Lam,-Lam@Vd))
W2=lambda k: RL(k)@(np.eye(12)-2*Ps[2])
for lab,k0 in (("k*",kst),("k*+pi ex",kst+np.pi*EX[0]),("-k*",-kst)):
    print(lab,[(round(E,4),m) for E,m in levels(W2,k0)])
    for d in (EX[0],EX[1],(EX[0]+EX[1])/np.sqrt(2)):
        ee=wrap(np.angle(np.linalg.eigvals(W2(k0+1e-4*d)))); ee=np.sort(ee[np.abs(ee)<0.01]); print("   ",np.round(ee/1e-4,5))
