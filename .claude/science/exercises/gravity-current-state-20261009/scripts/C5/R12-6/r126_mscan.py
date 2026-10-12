"""C5 R12-6, script 5: m-scan / N-convergence of the partner pieces (Wilson electron, cochain photino; matched curves).
Purpose: separate an IR (in-box) log from grid effects.  Columns: T (= unrepaired total for matched curves), repaired
photino (eta,a,b), B loop, repaired total.  Units 16 pi^2/e^2."""
import numpy as np, sys, time
sys.path.insert(0, '.')
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import r126_electron_loops as L
    import r126_repaired_loops as R
from r101_pairing import wilson_curve
t0 = time.time(); ce = wilson_curve(); U = L.U16
for m, Ns in [(0.4, (32, 48, 64)), (0.2, (48, 64, 96)), (0.1, (64, 96))]:
    for N in Ns:
        rT = L.dcl(L.dE_photino, ce, 'cochain', m, N, 'T') * U
        rKB = L.dcl(R.dE_photino_full, ce, 'cochain', m, N) * U
        rB = L.dcl(R.dE_Bloop, ce, 'cochain', m, N) * U
        rS = L.dcl(L.dE_sigma, ce, 'cochain', m, N) * U
        print('m=%.2f N=%3d : T(unrepaired total) %+8.3f | repaired photino %+8.3f  B %+8.3f  sigma %+7.3f  total %+8.3f  [%.0fs]'
              % (m, N, rT, rKB, rB, rS, rKB + rB + rS, time.time() - t0), flush=True)
