# T61 pre-registration (written BEFORE any of the scripts below were run)

Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check, not a referee).

Wall: a fixed regular lattice brings Planck-size shape (shear) and mass-type terms for the
gravity member that must be tuned (L16-W8 + L14-W15; source P6 = the "walker's sea feels the
shape of a constant metric" note on PR #9363).

Claim under test (my route-independent "price" argument):
  (H1) The shear stiffness is a UV / contact-term quantity, so no coarse-grained (long-wave)
       book-keeping can protect it: two couplings with IDENTICAL low-energy node metrics can
       have shear coefficients differing by O(0.1) per cell.
  (H2) For ANY matter whose Hamiltonian is affine in the inverse vielbein e (the "natural"
       coupling class, interacting or not), the ground energy E(e) is concave in e (Jensen),
       even in e, so the volume-preserving shear coefficient obeys
            c = E_vp''(0) = Hess + (g . e'')  <=  g . e''  =  K/(2d)  * tr(eps^2)/... <= 0
       with K = <H_hop> <= 0, hence the flat metric is never a minimum in this class, and the
       counterterm ("seagull") needed to cancel it, s(V) = -c(V), is state- and
       interaction-dependent (not one constant).
  (H3) Hypercubic/cubic symmetry, which protects scalars and vectors from non-Lorentz
       relevant operators in lattice QCD, leaves an EXTRA mass-type invariant for a symmetric
       rank-2 tensor field: it does not give a free lunch for the graviton.
  (H4) Arithmetic squeeze: untuned shear stiffness is compatible with the graviton-mass bound
       only for a >~ 1e-9 m, while matter-sector Lorentz tests need a <~ 1e-27 m.

## Part D1 - reproduction of the wall's numbers (free sea, Z^3, natural coupling)
Script: d1_free_sea.py.  E_0, c_E, c_T by midpoint BZ grid (N=96,128) and central differences.
  PASS (wall stated correctly): |E_0+1.19380|<2e-3, |c_E+0.17793|<2e-3, |c_T+0.14667|<2e-3.
  FAIL (wall misstated): any deviation > 2e-2.

## Part D2 - same infrared, different shear stiffness
Script: d2_same_ir.py.  Compare natural axis-shear coupling with the designed T6 volume-keeping
  momentum-space flow (v = (lam/2) (sin2k1 cos2k2, -cos2k1 sin2k2, 0), time-1 flow, RK4).
  PASS for H1: node metrics J^T J agree to <1e-6 across the 8 nodes AND across the two
       couplings, |E_designed - E_0| < 1e-5 while |E_natural - E_0| > 5e-3 at lam=0.1.
  FAIL for H1: the natural and designed couplings have different node metrics (then the
       comparison is not "same IR") or the designed sea is not shear-blind.

## Part D3 - interacting matter, natural class (exact diagonalisation)
Script: d3_ed.py.  2D walker (2 orbitals/site), 4x2 torus, antiperiodic in both directions
  (gapped free spectrum), N=8 fermions (half filling), nearest-neighbour density interaction V
  in {0, 0.5, 1, 2}, hop along axis j carries sigma_a e_a^j.
  Pre-registered readings:
   (i)  concavity: for 40 random pairs (e1,e2) E((e1+e2)/2) - (E(e1)+E(e2))/2 >= -1e-9.
   (ii) evenness: |E(e)-E(-e)| < 1e-9.
   (iii) c_vp(V) (volume-preserving path e=expm(t eps/2), tr eps^2=1, axis and face) < 0 for
        every V, and the identity c_vp = c_lin + (g . eps^2/4) holds to 1e-6 (c_lin: affine
        path 1+t eps/2), with c_lin < 0 strictly.
   (iv) seagull needed s(V) = -c_vp(V) changes by more than 10% between V=0 and V=2.
  PASS for H2: (i)-(iii) hold; (iv) holds.  FAIL for H2: any concavity violation, or any
  c_vp >= 0, or c_lin >= 0 for some V.

## Part D4 - symmetry counting
Script: d4_counting.py. Number of independent invariant quadratic forms (mass-type terms) for
  symmetric tensor h_ij under O_h (Z^3), h_mu nu under hyperoctahedral B4 (Z^4) vs O(4);
  vectors and scalars for comparison.
  PASS for H3: rank-2 counts (O_h: 3, B4: 3, O(4): 2) with vector/scalar counts equal for
  hypercubic and continuum rotation groups (1, 1).  FAIL: otherwise.

## Part D5 - arithmetic squeeze
Script: d5_squeeze.py. m_g = sqrt(32 pi c) l_P / a^2 (P6 T8 GR normalisation), c=0.109;
  compare with 1.27e-23 eV; a_min for untuned pass; required suppression of c at a=1e-19 m,
  1e-27 m, l_P.  Matter-side bound a <~ 1e-27 m is quoted as reference only (reading).
  PASS for H4: a_min > 1e-10 m.

## What each outcome would move
* D1 fail -> wall misstated (stop).  D2 fail -> H1 not shown; the "coarse-grained books" escape
  stays open.  D3 fail -> natural-class closure is not a theorem here; PRICED verdict weakened
  to STANDS.  D4/D5 are supporting.
