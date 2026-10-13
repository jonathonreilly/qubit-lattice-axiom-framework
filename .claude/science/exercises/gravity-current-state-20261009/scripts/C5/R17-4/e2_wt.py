"""R17-4: E2 off-axis rows vs turn width (Z1 skeleton, m = 0.1, U vertex); resolution check n1 = 2^14 vs 2^15."""
import numpy as np, sys; sys.path.insert(0, '.')
from laws import Z1
from e2rows import rows_E2
for wt in [0.03, 0.06, 0.12, 0.24]:
    L = Z1(wt)
    for n1 in [1 << 14, 1 << 15]:
        X2, X1 = rows_E2(L, 0.1, n1=n1)
        print('Z1(wt=%.2f) n1=%d  E1 face1 %+.4e face2 %+.4e | E2 face1 %+.4e face2 %+.4e body %+.4e' % (wt, n1, X1['face1'], X1['face2'], X2['face1'], X2['face2'], X2['body']), flush=True)
