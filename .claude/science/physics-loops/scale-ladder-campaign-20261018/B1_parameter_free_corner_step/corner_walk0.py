import sys, numpy as np
sys.path.insert(0,'.')
exec(open('diraclib.py').read().split("Xb=np.load")[0])
Hon=H0(1.0,0.0); Hli=H0(0.0,1.0)
print("Hon^2 prop to I:", np.allclose(Hon@Hon, (Hon@Hon)[0,0]*np.eye(nV)), "diag", (Hon@Hon)[0,0], "spec", np.round(np.unique(np.round(np.linalg.eigvalsh(Hon),6)),4))
print("Hli^2 prop to I:", np.allclose(Hli@Hli, (Hli@Hli)[0,0]*np.eye(nV)), "diag", (Hli@Hli)[0,0], "spec", np.round(np.unique(np.round(np.linalg.eigvalsh(Hli),6)),4))
