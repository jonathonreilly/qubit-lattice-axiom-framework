exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/continuous_taste_opt.py').read().split("rng=np.random.default_rng(2026)")[0].replace("check(","(lambda *a,**k:0)(") if False else open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/continuous_taste_opt.py').read().split("rng=np.random.default_rng(2026)")[0])
import time; t0=time.time()
x=np.array([3.7344,2.6932,5.6394,2.0108,4.3859,1.9652]); w=word(x,0); E=Eof(w); print("E",E,[(round(e,4),m) for e,m in node_levels(w,kst,1e-8)])
for nm,k in [("X_r",np.pi/2*EX[0]),("M_r",np.pi/2*np.array([1,1,0])),("Gamma_r",np.zeros(3)),("R_r",kst)]:
    lv=node_levels(w,k,1e-7); print(nm,"min dist to E %.4f"%min(abs(wrap(e-E)) for e,m in lv),[(round(e,4),m) for e,m in lv])
for k0 in (np.zeros(3),kst):
    v=vel_matrix(w,k0,E); print("node",np.round(k0/np.pi,3),np.round(v['sv'],6),v['chi'],v['tilt'])
ok,bad,ev,mm=certify_clean(w,E,[np.zeros(3),kst,kst-np.pi*np.ones(3)/1],0.03,lo=-np.pi/2,hi=np.pi/2,n0=24,maxdepth=8,budget=8_000_000)
print("certificate:",ok,bad,ev,time.time()-t0)
