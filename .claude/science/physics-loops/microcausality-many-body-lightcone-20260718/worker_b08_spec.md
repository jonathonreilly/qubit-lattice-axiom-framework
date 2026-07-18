# Worker task (Opus 4.8 max; owner-directed workhorse substitution, supervisor responsible): verify the block08 gauged-kernel-feed assembly

Do NOT read any repository files. Self-contained. Write INCREMENTALLY to:
.claude/science/physics-loops/microcausality-many-body-lightcone-20260718/worker_b08_analysis.md

## Supervisor-supplied assembly to verify line by line (flag ANY error)

Supplied input (from a cited note, take as given): a one-particle kernel
on Z^3 with || <x| h |y> || <= K e^{-eta ||x-y||_inf}, K and eta > 0
independent of a background parameter U and of volume. Second-quantize:
pair terms for unordered {x,y}, x != y:
  h_{xy} = <x|h|y> c_x^dag c_y + <y|h|x> c_y^dag c_x
(kernel Hermitian: <y|h|x> = conj(<x|h|y>)), on-site terms
  h_x = <x|h|x> c_x^dag c_x.
CAR facts to verify: ||c_x^dag c_y|| = 1 (x != y), ||c_x^dag c_x|| = 1,
each pair term is EVEN (2 generators), Hermitian, and
||h_{xy}|| <= 2 |<x|h|y>| <= 2 K e^{-eta r}, r = ||x-y||_inf;
||h_x|| <= K.

Target activity (weighted norm from a sibling class, take the
DEFINITION as given): kappa = sup_x sum_{S ni x} ||h_S|| |S| e^{mu diam_1(S)}
where diam_1 = l1 (Manhattan) diameter. For the pair {x,y}: |S| = 2,
diam_1 = ||x-y||_1.

Steps to verify:
1. Metric conversion: ||z||_1 <= 3 ||z||_inf on Z^3 (prove; equality
   cases). Hence e^{mu ||z||_1} <= e^{3 mu ||z||_inf}.
2. l_inf shell count on Z^3: #{z : ||z||_inf = r} = (2r+1)^3 - (2r-1)^3
   = 24 r^2 + 2 for r >= 1 (prove + spot-enumerate r = 1, 2, 3).
3. Per-site pair sum: sum_{y != x} ||h_{xy}|| * 2 * e^{mu ||x-y||_1}
   <= 4K sum_{r>=1} (24 r^2 + 2) x^r with x = e^{-(eta - 3 mu)},
   requiring mu < eta/3. VERIFY the factor 4 = (2 from ||h_{xy}||
   bound) * (2 from |S|).
4. Closed form: sum_{r>=1} (24 r^2 + 2) x^r = [24 x(1+x) + 2x(1-x)^2]
   / (1-x)^3; expand the numerator EXACTLY and simplify (supervisor
   claims 26x + 20x^2 + 2x^3 = 2x(13 + 10x + x^2); verify or refute).
5. Total: kappa <= K + 8 K x (13 + 10x + x^2)/(1-x)^3. VERIFY the 8.
6. Instance x = 1/2: compute kappa/K exactly (supervisor claims 585;
   verify or refute, show arithmetic).
7. Threshold statement: the bound is finite iff x < 1 iff mu < eta/3;
   compare with the known pattern "0 < d mu < eta" at d = 3.
8. Background-uniformity logic: the bound uses only |<x|h|y>| <= K
   e^{-eta r}, which is U-independent by hypothesis; hence kappa's
   bound is background-independent. State what WOULD break it
   (U-dependent K or eta).
9. Design a runner toy instance: a 3-site chain (sites 0,1,2), kernel
   h[s]_{xy} = s_{xy} * (1/2)^{|x-y|} with signs s_{xy} = s_{yx} in
   {+1,-1} (a Z_2 background), s_{xx} = 1. Enumerate ALL 2^3 = 8 sign
   backgrounds: verify the pair norms |h[s]_{xy}| are identical across
   backgrounds, hence kappa(box) identical — an exact uniformity
   exhibit. Compute kappa(box) exactly at e^mu = 9/8 (rational; l1 =
   l_inf in 1D so no conversion loss in the exhibit — note this).
10. LIMITS: anything assumed, anything the supervisor must recheck.

Exact arithmetic only; show every step of 4, 5, 6, 9.
