import numpy as np, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import onshell as O, disp
def lattice_omega(ks):  # sum_i 4 sin^2(k_i/2) = 4 sinh^2(w/2)
    s = np.sum(4*np.sin(ks/2)**2); return 2*np.arcsinh(np.sqrt(s)/2)
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'gen': (3,1,2), 'gen-': (3,-1,2)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.3, 0.8, 1.5):
        ks = km*n; w = lattice_omega(ks)
        p = np.array([*ks, 1j*w])
        sr = np.sort(np.linalg.svd(O.Qedge_r(p), compute_uv=False)); sr /= sr[-1]
        sm = np.sort(np.linalg.svd(disp.maxwell_hol(p), compute_uv=False)); sm /= sm[-1]
        ss = abs(disp.scalar_hol(p))
        # off-shell control
        po = np.array([*ks, 1j*w*1.01]); so = np.sort(np.linalg.svd(O.Qedge_r(po), compute_uv=False)); so /= so[-1]
        print(f"{name:5s} k={km:.1f} w={w:.5f} scalar|S|={ss:.1e} regge sv5..8 {np.array2string(sr[4:8],precision=1)} (off-shell {np.array2string(so[4:8],precision=1)}) maxwell sv1..3 {np.array2string(sm[:3],precision=1)}")
