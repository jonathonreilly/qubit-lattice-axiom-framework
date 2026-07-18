# Worker B08 analysis: verification of the gauged-kernel-feed activity assembly

Scope: verify, line by line and with exact arithmetic, the supervisor-supplied
assembly that feeds a one-particle exponential-decay kernel on Z^3 into a
weighted many-body activity `kappa`. Every numbered step below is checked;
supervisor errors are flagged LOUDLY. Nothing outside the spec was read.

Convention: ASCII. `r = ||x-y||_inf`, `x` (in steps 3-8) is the series variable
`x = e^{-(eta - 3 mu)}`, NOT a lattice site. Lattice sites are named x, y, z but
only inside metric/CAR statements.

## Given (taken as supplied, not re-derived)

One-particle kernel on Z^3:  `|| <x|h|y> || <= K e^{-eta ||x-y||_inf}`, with
`K > 0`, `eta > 0`, both independent of a background parameter U and of volume.

Second quantization (unordered {x,y}, x != y):
    h_{xy} = <x|h|y> c_x^dag c_y + <y|h|x> c_y^dag c_x ,   <y|h|x> = conj(<x|h|y>)
    h_x    = <x|h|x> c_x^dag c_x .

Activity definition (from sibling class, taken as given):
    kappa = sup_x  sum_{S ni x}  ||h_S|| * |S| * e^{mu * diam_1(S)},
with diam_1 = l1 (Manhattan) diameter. Pair {x,y}: |S| = 2, diam_1 = ||x-y||_1.
Singleton {x}: |S| = 1, diam_1 = 0.

## CAR facts (verified)

- ||c_x^dag c_y|| = 1, x != y.
  (c_x^dag c_y)(c_x^dag c_y)^dag = c_x^dag c_y c_y^dag c_x
    = c_x^dag (1 - c_y^dag c_y) c_x               [c_y c_y^dag = 1 - n_y]
    = c_x^dag c_x - c_x^dag c_y^dag c_y c_x
    = n_x (1 - n_y)                                [x != y, anticommute cleanly]
  which is an orthogonal projection (product of commuting projections n_x and
  1-n_y) onto {n_x = 1, n_y = 0}, a nonzero subspace, so norm 1. Hence
  ||c_x^dag c_y||^2 = 1, ||c_x^dag c_y|| = 1.  VERIFIED.

- ||c_x^dag c_x|| = ||n_x|| = 1 (number operator, spectrum {0,1}).  VERIFIED.

- Each pair term is EVEN: c_x^dag c_y and c_y^dag c_x each carry 2 fermionic
  generators -> even fermion parity.  VERIFIED.

- Hermitian: h_{xy}^dag = conj(<x|h|y>) c_y^dag c_x + conj(<y|h|x>) c_x^dag c_x?
  carefully: (<x|h|y> c_x^dag c_y)^dag = conj(<x|h|y>) c_y^dag c_x = <y|h|x> c_y^dag c_x,
  (<y|h|x> c_y^dag c_x)^dag = conj(<y|h|x>) c_x^dag c_y = <x|h|y> c_x^dag c_y.
  Sum = <x|h|y> c_x^dag c_y + <y|h|x> c_y^dag c_x = h_{xy}.  VERIFIED Hermitian.

- ||h_{xy}|| <= |<x|h|y>|*||c_x^dag c_y|| + |<y|h|x>|*||c_y^dag c_x||
             = |<x|h|y>| + |<y|h|x>| = 2|<x|h|y>|  (|<y|h|x>| = |conj(<x|h|y>)|)
             <= 2 K e^{-eta r}.  VERIFIED (triangle inequality; factor-2 is an
  UPPER bound, see LIMITS: exact single-pair norm is |<x|h|y>|, half of this).

- ||h_x|| = |<x|h|x>| * ||c_x^dag c_x|| = |<x|h|x>| <= K e^{-eta*0} = K.  VERIFIED.

## Step 1 -- metric conversion  ||z||_1 <= 3 ||z||_inf on Z^3

Let z = (z1,z2,z3) in Z^3. Write M = ||z||_inf = max_i |z_i|. Each |z_i| <= M,
so ||z||_1 = |z1|+|z2|+|z3| <= M + M + M = 3M = 3 ||z||_inf.  VERIFIED.
(General d: ||z||_1 <= d ||z||_inf; here d = 3.)

Equality cases: ||z||_1 = 3||z||_inf  iff  |z1| = |z2| = |z3| (all equal to M).
Examples: z = 0 (0 = 0); z = (1,1,1) and all sign/coordinate variants; (2,-2,2);
generally the 8 "corner" directions t*(+/-1,+/-1,+/-1). If even one |z_i| < M the
inequality is strict.

Monotonicity of exp (increasing) with mu > 0 (see LIMITS -- positivity of mu is
USED here) gives  mu ||z||_1 <= 3 mu ||z||_inf, hence
    e^{mu ||z||_1} <= e^{3 mu ||z||_inf}.  VERIFIED.

## Step 2 -- l_inf shell count on Z^3

The closed l_inf ball {z : ||z||_inf <= r} is the cube [-r,r]^3 cap Z^3, with
(2r+1)^3 points (each coordinate takes 2r+1 integer values). The shell
{||z||_inf = r} = ball(r) \ ball(r-1), so for r >= 1
    #{||z||_inf = r} = (2r+1)^3 - (2(r-1)+1)^3 = (2r+1)^3 - (2r-1)^3.

Exact expansion:
    (2r+1)^3 = 8r^3 + 12r^2 + 6r + 1
    (2r-1)^3 = 8r^3 - 12r^2 + 6r - 1
    difference = (12r^2 + 12r^2) + (1 + 1) = 24 r^2 + 2.
So  #{||z||_inf = r} = 24 r^2 + 2,  r >= 1.  VERIFIED (supervisor form matches).

Spot-enumeration:
    r=1: 24*1+2 = 26 ; direct 3^3 - 1^3 = 27 - 1 = 26.   MATCH.
    r=2: 24*4+2 = 98 ; direct 5^3 - 3^3 = 125 - 27 = 98.  MATCH.
    r=3: 24*9+2 = 218; direct 7^3 - 5^3 = 343 - 125 = 218. MATCH.

## Step 3 -- per-site pair sum, and the factor 4

Fix a site x. The pair sets containing x are {x,y}, y != x. Each contributes
    ||h_{xy}|| * |S| * e^{mu diam_1({x,y})} = ||h_{xy}|| * 2 * e^{mu ||x-y||_1}.

Bound each factor:
    ||h_{xy}||        <= 2 K e^{-eta r}       (CAR facts, r = ||x-y||_inf)
    e^{mu ||x-y||_1}  <= e^{3 mu r}           (Step 1, needs mu > 0)
so the {x,y} term is
    <= (2 K e^{-eta r}) * 2 * e^{3 mu r} = 4 K e^{-(eta - 3 mu) r}.

FACTOR-4 CHECK: 4 = 2 * 2, the first 2 from the norm bound ||h_{xy}|| <= 2|<x|h|y>|
and the second 2 from |S| = 2. VERIFIED.

Group the sum over y != x by l_inf shells r = ||x-y||_inf >= 1 (Step 2 counts):
    sum_{y != x} 4 K e^{-(eta-3 mu) r}
        = 4 K sum_{r>=1} (24 r^2 + 2) e^{-(eta - 3 mu) r}
        = 4 K sum_{r>=1} (24 r^2 + 2) x^r ,      x := e^{-(eta - 3 mu)}.
Convergence needs |x| < 1, i.e. eta - 3 mu > 0, i.e. mu < eta/3.  VERIFIED.
(The per-shell bound depends on y only through r, so replacing the y-sum by the
shell-count times the common bound is exact, not an over-count.)

## Step 4 -- closed form of  sum_{r>=1} (24 r^2 + 2) x^r

Standard generating sums, valid for |x| < 1:
    sum_{r>=1} x^r     = x/(1-x)
    sum_{r>=1} r x^r   = x/(1-x)^2
    sum_{r>=1} r^2 x^r = x(1+x)/(1-x)^3.

Therefore
    sum_{r>=1}(24 r^2 + 2) x^r = 24 * x(1+x)/(1-x)^3 + 2 * x/(1-x).
Put over common denominator (1-x)^3, using x/(1-x) = x(1-x)^2/(1-x)^3:
    = [ 24 x(1+x) + 2 x(1-x)^2 ] / (1-x)^3.
This matches the supervisor's claimed intermediate form.  VERIFIED.

EXACT numerator expansion:
    24 x (1 + x)      = 24x + 24x^2
    2 x (1 - x)^2     = 2x(1 - 2x + x^2) = 2x - 4x^2 + 2x^3
    ---------------------------------------------------------
    sum               = (24x + 2x) + (24x^2 - 4x^2) + 2x^3
                      = 26x + 20x^2 + 2x^3.

Supervisor factoring claim:  26x + 20x^2 + 2x^3 = 2x(13 + 10x + x^2).
Check by re-expanding: 2x(13 + 10x + x^2) = 26x + 20x^2 + 2x^3.  IDENTICAL.
VERIFIED. So
    sum_{r>=1}(24 r^2 + 2) x^r = 2x(13 + 10x + x^2) / (1-x)^3.

Numeric cross-check at x = 1/2 (independent of the algebra):
    partial sums of (24r^2+2)(1/2)^r: r=1:13, r=2:24.5, r=3:27.25, r=4:24.125,
    r=5:18.8125, r=6:13.53125, r=7:9.203125, r=8:6.0078125, tail r>=9 ~ +9.57,
    -> total ~ 146.  Closed form: 2*(1/2)*(73/4)/(1/8) = (73/4)*8 = 146.  MATCH.

## Step 5 -- total kappa bound, and the factor 8

kappa = sup_x [ singleton term + pair sum ]. The only nonzero h_S are singletons
(|S|=1) and pairs (|S|=2); h_S = 0 for |S| >= 3, so no higher sets contribute.
Singleton {x}: ||h_x|| * 1 * e^{mu*0} = ||h_x|| <= K.
Pair sum (Step 3-4):
    4 K sum_{r>=1}(24r^2+2) x^r = 4 K * 2x(13+10x+x^2)/(1-x)^3
                                = 8 K x(13 + 10x + x^2)/(1-x)^3.
Hence, uniformly in x (translation-uniform per-site bound), so sup_x is attained:
    kappa <= K + 8 K x(13 + 10x + x^2)/(1-x)^3.

FACTOR-8 CHECK: 8 = 4 * 2, the 4 from Step 3 (norm-2 * size-2) and the 2 from the
numerator factor 2x(13+10x+x^2) of Step 4. VERIFIED (supervisor form matches).

## Step 6 -- instance x = 1/2 : kappa/K exactly

Set x = 1/2 in kappa/K <= 1 + 8 x (13 + 10x + x^2)/(1-x)^3.

Piecewise, exact rationals:
    13 + 10*(1/2) + (1/2)^2 = 13 + 5 + 1/4 = 73/4.
    (1 - 1/2)^3 = (1/2)^3 = 1/8.
    8 * (1/2) = 4.
    numerator  8x(13+10x+x^2) = 4 * (73/4) = 73.
    divide by (1-x)^3:  73 / (1/8) = 73 * 8 = 584.
    add singleton 1:  1 + 584 = 585.

Therefore  kappa/K <= 585  at x = 1/2  (i.e. at e^{-(eta-3mu)} = 1/2, eta-3mu = ln 2).
Supervisor claim 585.  VERIFIED (exact, not approximate).

Consistency with the numeric cross-check of Step 4: pair sum bound = 4K*146 = 584K,
plus singleton K = 585K. Same 585.  CONSISTENT.

## Step 7 -- threshold statement and the "0 < d mu < eta" pattern

The bound K + 8 K x(13+10x+x^2)/(1-x)^3 is finite exactly when the geometric-type
series converges, i.e. iff x < 1. Now
    x = e^{-(eta - 3 mu)} < 1  iff  eta - 3 mu > 0  iff  3 mu < eta  iff  mu < eta/3.
So: bound finite  <=>  x < 1  <=>  mu < eta/3.  VERIFIED.

Comparison with the known pattern "0 < d mu < eta" at d = 3: substituting d = 3
gives 0 < 3 mu < eta, i.e. (positivity) mu > 0 AND (finiteness) mu < eta/3. This
is exactly the joint condition used here: mu > 0 is consumed in Step 1 (metric
conversion / exp-monotonicity) and mu < eta/3 in Steps 3-4 (convergence). The
factor d = 3 is precisely the l1-vs-l_inf conversion constant of Step 1. MATCH:
the assembly reproduces the d=3 case of the general pattern, with 3 = the Z^3
Manhattan/Chebyshev ratio, not an independent constant.

## Step 8 -- background (U) uniformity

Every inequality feeding the bound used ONLY:  |<x|h|y>| <= K e^{-eta r}, with K
and eta independent of U (hypothesis). No step referenced U, the specific matrix
elements' phases, or the volume:
  - Step 1 metric conversion: pure lattice geometry (U-free).
  - Step 2 shell count: pure lattice combinatorics (U-free).
  - Steps 3-6: use only K, eta and the CAR norms (U-free).
Hence the numerical bound (e.g. 585 K at x=1/2) holds with the SAME K and the SAME
eta for every background U simultaneously: the activity bound is
background-independent (uniform in U).  VERIFIED.

What WOULD break it: any U-dependence entering K or eta -- e.g.
  - K = K(U) unbounded as U varies (prefactor blows up), or
  - eta = eta(U) with inf_U eta(U) = 0 (decay rate degrades), pushing 3 mu >= eta(U)
    for some U so x(U) >= 1 and the series diverges,
  - or a U-dependent range/hopping that violates the single exponential envelope.
As long as the supplied one-particle estimate has U-independent (K, eta), none of
these occur and uniformity stands. (This is exactly the hypothesis the sibling
note supplies; it is an INPUT, not proved here.)

## Step 9 -- runner toy: 3-site chain, Z_2 sign background, exact uniformity

Sites {0,1,2} on a line. Kernel  h[s]_{xy} = s_{xy} * (1/2)^{|x-y|},  signs
s_{xy} = s_{yx} in {+1,-1}, s_{xx} = +1. Independent signs: the three off-diagonal
pairs (s_{01}, s_{12}, s_{02}) -> 2^3 = 8 backgrounds.

1D metric note: for z in Z, ||z||_1 = |z| = ||z||_inf. So l1 = l_inf exactly; the
Step-1 factor 3 (a Z^3 artifact) does NOT enter -- no conversion loss in the toy.
diam_1({x,y}) = |x-y|.

Term norms used for kappa (exact single-pair operator norm = coefficient magnitude,
since h_{xy} = t(c_x^dag c_y + c_y^dag c_x), t real, and ||c_x^dag c_y + c_y^dag c_x||
= 1 -- the hop has many-body spectrum {-1,0,+1}):
    ||h_{xy}|| = |h[s]_{xy}| = |s_{xy}| (1/2)^{|x-y|} = (1/2)^{|x-y|},
    ||h_x||    = |h[s]_{xx}| = |s_{xx}| (1/2)^0    = 1.

UNIFORMITY: |s_{xy}| = 1 for every sign choice, so |h[s]_{xy}| = (1/2)^{|x-y|} is
identical across all 8 backgrounds. Concretely the pair magnitudes are always
    |h_{01}| = (1/2)^1 = 1/2,  |h_{12}| = (1/2)^1 = 1/2,  |h_{02}| = (1/2)^2 = 1/4,
and |h_{xx}| = 1. Enumerating (s_{01},s_{12},s_{02}):
    (+,+,+) (+,+,-) (+,-,+) (+,-,-) (-,+,+) (-,+,-) (-,-,+) (-,-,-)
in EVERY row the three magnitudes are (1/2, 1/2, 1/4) and diagonals 1. So every
kappa-summand (which uses |h_S|, never the sign) is background-independent, hence
kappa(box) is identical for all 8.  VERIFIED -- exact uniformity exhibit.

kappa(box) exactly at e^mu = 9/8:
Per pair at chain-distance d, summand = ||h_{xy}|| * |S| * e^{mu diam_1}
    = (1/2)^d * 2 * (9/8)^d = 2 * ( (1/2)(9/8) )^d = 2 * (9/16)^d.
Singleton summand = ||h_x|| * 1 * e^0 = 1.

Site 0 (neighbours: 1 at d=1, 2 at d=2):
    1 + 2*(9/16)^1 + 2*(9/16)^2
    = 1 + 2*(9/16) + 2*(81/256)
    = 1 + 9/8 + 81/128
    = 128/128 + 144/128 + 81/128 = 353/128.
Site 2 (neighbours: 1 at d=1, 0 at d=2): by reflection symmetry = 353/128.
Site 1 (neighbours: 0 at d=1, 2 at d=1):
    1 + 2*(9/16) + 2*(9/16)
    = 1 + 9/8 + 9/8 = 1 + 9/4 = 13/4 = 416/128.

kappa(box) = sup over sites = max(353/128, 416/128, 353/128) = 416/128 = 13/4.
The middle site 1 dominates (two nearest neighbours beat one-near + one-far).
    kappa(box) = 13/4 = 3.25 exactly, identical for all 8 sign backgrounds.

(Check 353/128 = 2.7578125 < 3.25, consistent with sup at site 1.)

## Step 10 -- LIMITS

Supervisor arithmetic: ALL five checkable claims verified with no error --
Step 2 shell count 24r^2+2; Step 3 factor 4 = 2*2; Step 4 numerator
26x+20x^2+2x^3 = 2x(13+10x+x^2); Step 5 factor 8 = 4*2; Step 6 kappa/K = 585 at
x=1/2. No supervisor error found to flag.

Assumptions / taken-as-given (NOT proved here; supervisor/sibling note must own):
1. The one-particle envelope |<x|h|y>| <= K e^{-eta r} with K, eta > 0 and
   U-independent, volume-independent. Everything downstream inherits this; if it
   is only a claim, uniformity (Step 8) is only as strong as it.
2. The activity DEFINITION kappa = sup_x sum_{S} ||h_S|| |S| e^{mu diam_1}, taken
   verbatim from the sibling class -- including that singletons are counted with
   |S|=1, diam=0 (this supplies the "+K" / "+1"). If the sibling class excludes
   singletons or weights |S| differently, Step 5's "K +" and Step 6's "1 +" shift.
3. Only 1- and 2-site terms exist (h_S = 0, |S|>=3). True for a quadratic
   (one-particle-derived) Hamiltonian; would fail if interactions were added.

NORM-CONVENTION FLAG (supervisor must reconcile -- the two halves of the spec use
DIFFERENT pair norms, both internally correct):
  - Main line (Steps 3-6) uses the triangle-inequality UPPER bound
    ||h_{xy}|| <= 2|<x|h|y>|. This is loose by exactly 2x for a Hermitian pair,
    whose true norm is |<x|h|y>|. So 585 is a valid UPPER BOUND on kappa/K, not
    the exact kappa; the exact-norm bound would be K + 4Kx(13+10x+x^2)/(1-x)^3,
    giving (585+1)/2 = 293 at x=1/2. The spec asked to verify 585, which is the
    factor-2-bound value -- correct as stated, but it is a bound, read it as such.
  - Toy (Step 9) uses the EXACT single-pair norm ||h_{xy}|| = |h[s]_{xy}|, giving
    kappa(box) = 13/4. This is the natural reading of "the pair norms |h[s]_{xy}|"
    and "compute kappa(box) exactly". If instead the toy must mirror the main
    line's factor-2 convention, each pair summand doubles: site-1 sum becomes
    1 + 2*[2*(9/16)] + 2*[2*(9/16)] = 1 + 9/2 = 11/2, site-0/2 become
    1 + 9/4 + 81/64 = 289/64 = 4.515625, so kappa(box) = 11/2 = 5.5. Supervisor
    should state which convention the sibling class intends so the toy and the
    main line agree; the value is 13/4 (exact norm) or 11/2 (factor-2 bound).

4. mu > 0 is REQUIRED and used (Step 1 exp-monotonicity); the finiteness window is
   the open interval 0 < mu < eta/3. At mu = 0 the bound is finite but the
   diam-weight is trivial; at mu -> eta/3^- the bound diverges like (1-x)^{-3}.
5. sup_x in the infinite lattice = the single translation-uniform per-site value
   (Step 5); legitimate because the per-site bound has no x-dependence. In the
   finite toy the sup is a genuine max over 3 sites (attained at the middle site).
6. The l1<=3 l_inf conversion (Step 1) is 3D-specific; the toy is 1D where
   l1 = l_inf, so the toy does NOT test the factor-3 step -- it isolates the
   sign/uniformity mechanism only. A faithful 3D uniformity exhibit would be a
   separate, larger enumeration.

Recheck requests for supervisor: (a) confirm the intended pair-norm convention
(factor-2 bound vs exact) so 585 and the toy value are on the same footing;
(b) confirm singletons belong in the sibling-class kappa sum; (c) confirm the
U-independence of (K, eta) is an established input from the cited note.
