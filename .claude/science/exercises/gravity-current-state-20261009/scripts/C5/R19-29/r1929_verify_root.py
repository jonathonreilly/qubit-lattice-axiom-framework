"""R19-29: direct photon re-evaluation (Ng = 128) of kappa, c4 at the lam_nn = 0 branch roots found by r1929_resolve_scan.py."""
import sys, numpy as np
sys.argv = ['x', '128', '-2.547003e-02', '-4.280511e-01', '1.011290e-01']
exec(open('r1929_resolve.py').read().split('wds = [')[0])
for wd in (0.75313, -0.47329):
    kg_, cg_, Xg = phot_kc(wd, wo0)
    kt, ct, Xt = kap_sd + 12*kg_, c4_sd + 12*cg_, X_sd + 12*Xg
    print('w_d=%+.5f direct: kappa_tot %+.6e c4_tot %+.6e X_tot %+.6e  raw face1 (Lemma O, linear) %+.6e  Schur term %+.6e  phys face1 %+.6e'
          % (wd, kt, ct, Xt, J11*(wd - wd0), -kt**2/(ct + 8*Xt), J11*(wd - wd0) - kt**2/(ct + 8*Xt)), flush=True)
