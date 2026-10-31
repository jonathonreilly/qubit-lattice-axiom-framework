# bb8n_defect criteria (lane B session 8; written after bb8n ran (11:21:10-11:21:12 UTC) and before checks/bb8n_defect.py)

Informational probe, written because bb8n's L-c printed defect ratios 0.0000 (its [0.5, 2] scaling clause then compared
round-off). bb8n.out stays the record of that run (L-c FAIL as written). This probe prints the raw max own |d_j| (m = 1, 2, 3;
f_k = 0.10 and 0.05; the ungauged and a Haar-gauged top field), with bb8n's code unchanged (imported by exec of bb8n_lip.py's
definitions). Prediction written here before the run: if the straight root row lies on the first-axis branch of the axial tree
and the DD8 transverse weights at offset 0 are δ (interpolatory), the row links carry exp(0) and the face link exp(0)·Z(X, X'),
so d_j = 0 exactly (round-off, ≤ 1e-13). D-a: max own |d_j| ≤ 1e-13 for every m, amplitude and gauge (PASS = prediction holds).
