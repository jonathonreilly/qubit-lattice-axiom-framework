"""R19-16 (root): the archived photon row evaluators (R18-9 lib9.phot_quad; R18-13 vwface.xi_geo), UNMODIFIED, run with the
ANALYTIC law (lib1916.AnalyticPhotonLaw) in place of the archived tabulated photonGw, at N = 224 (shifts (1, 2)).
argv: axial | face.  Output .npy feeds r1916_resolve.py.  The archived-table values are in orig/photquad_N224.npy and
orig/arch18_13/photface_N224.out."""
import os, sys, time, numpy as np
import lib1916 as R
HERE = R.HERE
sys.path.insert(0, os.path.join(HERE, 'orig', 'arch18_9')); sys.path.insert(0, os.path.join(HERE, 'orig', 'arch18_13'))
mode = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 224
t0 = time.time()
LAWA = R.AnalyticPhotonLaw()
if mode == 'axial':
    import lib9 as L9
    L9.photonGw = lambda b, w: LAWA                    # phot_quad builds photonGw(2.9435, 1.0*(pi - 2.9435)) == the root edge
    P = L9.phot_quad(2.9435, 1.0, N)
    v = np.r_[P['T2g'], P['Eg'], P['muE']]
    np.save(os.path.join(HERE, f'photquad_analytic_N{N}.npy'), v)
    ref = np.load(os.path.join(HERE, 'orig', 'photquad_N224.npy')) if N == 224 else None
    print(f'N={N} analytic law: T {P["T2g"].tolist()} E {P["Eg"].tolist()} muE {P["muE"]!r} [{time.time()-t0:.0f}s]')
    if ref is not None: print('  analytic - archived table:', np.array2string(v - ref, precision=3))
else:
    import vwface as V
    if mode == 'facetab':                               # control: archived tabulated law, full precision
        from photon import photonGw
        LAWA = photonGw(2.9435, np.pi - 2.9435)
    a = -0.1760950036
    sets = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
    F1 = V.xi_geo(LAWA, N, 'face1', a, sets, (1, 2)); F2 = V.xi_geo(LAWA, N, 'face2', a, sets, (1, 2))
    v = np.r_[F1[0], F2[0], F1[1] - F1[0], F1[2] - F1[0], F2[1] - F2[0], F2[2] - F2[0]]
    np.save(os.path.join(HERE, f'photface_{"tab" if mode == "facetab" else "analytic"}_N{N}.npy'), v)
    print(f'N={N} {LAWA.name}, per vector at (wd,wo)=(0,0): face1 {F1[0]:+.12e} face2 {F2[0]:+.12e} | d/dwd {v[2]:+.9e} {v[4]:+.9e}'
          f' | d/dwo {v[3]:+.9e} {v[5]:+.9e} [{time.time()-t0:.0f}s]')
    if N == 224:
        ref = np.array([2.182473207e-01, 1.092917123e-01, 1.397040e-01, 2.892797e-01, 0.0, 5.785714e-01])
        print('  analytic - archived table (archived printed to 10/7 digits):', np.array2string(v - ref, precision=3))
