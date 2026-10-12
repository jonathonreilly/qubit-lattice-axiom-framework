"""C5 R12-3, script 3: convergence / mass dependence of the transverse-photino partner loop (r123_partner_loop.py).
Same formulas; N up to 96 and m down to 0.025.  An m-dependence ~ ln(1/m) signals an IR (in-box) non-covariance of the
TRANSVERSE PART ONLY; the omitted horizontal-dressing terms are instantaneous (Coulomb-like) and may cancel it."""
import sys, time, io, contextlib
sys.path.insert(0, '.')
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import r123_partner_loop as P   # re-runs the module's own checks silently
t0 = time.time()
U16 = P.U16
for lab, ce, kind in [('Wilson-circle e / cochain photino', P.wilson_curve(), 'cochain'),
                      ('box b1=0.8 e / box photino (1,2)', P.make_box_curve(0.8, 1.6), 'box')]:
    for m, N in [(0.1, 96), (0.05, 96), (0.025, 96)]:
        r = P.dc(ce, kind, m, N)
        print('   %-36s m=%.3f N=%3d : %+9.4f   [%.0fs]' % (lab, m, N, r * U16, time.time() - t0), flush=True)
