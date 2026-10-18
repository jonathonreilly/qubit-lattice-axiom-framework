exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
Tb1=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/Tb1.npy')
blb=blocks_from(Tb1)
print("shifts H_li:",sorted(blli.keys())," Tb:",sorted(blb.keys()))
for nm,bl in (("H_li",blli),("Tb1",blb)):
    for k in (kst, kst+np.array([0.1,0.2,0.3]), np.array([0.37,1.1,-0.4])):
        M=Hk(bl,k); print(nm, np.round(k,2), "||M^2-2I|| =", round(np.linalg.norm(M@M-2*np.eye(12)),6))
