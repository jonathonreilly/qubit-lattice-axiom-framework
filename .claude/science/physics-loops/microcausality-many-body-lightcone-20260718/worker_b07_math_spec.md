# Worker B (math build): weighted-norm quasilocal-class walk expansion — full inequality chain

Substitution disclosure: this worker seat is Opus 4.8 at max reasoning
effort (owner-directed; supervisor responsible).

Do NOT read any repository files. Self-contained task. Write
INCREMENTALLY to:
.claude/science/physics-loops/microcausality-many-body-lightcone-20260718/worker_b07_math_analysis.md

## Setup (supervisor-supplied; verify each step, fill gaps, flag errors)

Finite region Lambda in Z^3, sites carry finite-dim spaces. Supplied
interaction family: for finite sets S (assume connected, diam = graph
diameter), Hermitian h_S with the SUPPLIED weighted bound
  kappa := sup_x sum_{S: x in S} ||h_S|| * |S| * e^{mu * diam(S)} < infinity
for a supplied mu > 0. H = sum_S h_S. Observables A on X, B on Y,
d = d(X,Y) >= 1. tau_t = Heisenberg. The Duhamel/norm-transport
machinery (Jacobi, boundary reduction [H,A] = sum_{S cap X nonempty}
[h_S, A], self-drop, ||f(t)|| <= ||f(0)|| + int ||R||, iterated
integrals t^k/k!) may be TAKEN AS GIVEN (it is proven in a sibling
note); your job is ONLY the counting/summation layer on top of it.

## Required derivation (show every inequality, no gaps)

1. CHAIN LEMMA: for a chain (S_1,...,S_k) with S_1 cap X nonempty,
   S_{j+1} cap S_j nonempty, S_k cap Y nonempty: every site of S_j is
   within distance sum_{i<=j} diam(S_i) of X; conclude
   sum_j diam(S_j) >= d. Prove cleanly by induction.
2. WEIGHT SPLIT: Pi_j ||h_{S_j}|| <= e^{-mu d} * Pi_j (||h_{S_j}||
   e^{mu diam S_j}) using the chain lemma. State exactly.
3. STEPWISE FACTORIZATION: bound
   sum over chains of Pi_j (||h_{S_j}|| e^{mu diam S_j})
   <= (start factor) * kappa^{k-1}
   where the step S_j -> S_{j+1} uses: sum over S' meeting S_j of
   ||h_{S'}|| e^{mu diam S'} <= |S_j| * kappa / ... CAREFUL: the |S|
   weight inside kappa exists precisely to absorb the |S_j| choices of
   contact site — but the chain's next factor carries ITS OWN |S_{j+1}|
   weight needed for the step after. Track this precisely: show the
   correct bookkeeping is
   sum_{S' cap S_j nonempty} ||h_{S'}|| |S'| e^{mu diam S'}
   <= |S_j| * kappa,
   and that the |S_j| got consumed from the PREVIOUS factor's |S_j|
   weight. Conclude the exact start factor (something like
   n_X^w := sum_{S cap X nonempty} ||h_S|| |S| e^{mu diam S} <= |X| kappa).
4. ASSEMBLY: with the sibling's unrolled form
   ||[tau_t(A),B]|| <= ||[A,B]|| + 2||A|| sum_{k>=1} 2^{k-1}
   (chain sums with base ||[h_{S_k},B]|| <= 2||h_{S_k}|| ||B||)
   |t|^k / k!
   — CHECK the 2-powers bookkeeping against this shape: each Duhamel
   iterate contributes 2||h||, the base contributes 2||h|| ||B||; make
   the final constants exact. Derive:
   ||[tau_t(A),B]|| <= ||[A,B]|| + C * e^{-mu d} * (e^{c kappa |t|} - 1)
   with C and c fully explicit in ||A||, ||B||, |X|, kappa (state the
   exact final display).
5. CONSISTENCY REDUCTION: specialize to the strict bond class
   (h_S = 0 unless S a bond, ||h_b|| <= J): compute kappa exactly
   (bonds through a site: 6, |S| = 2, diam = 1 => kappa = 12 J e^{mu}),
   and compare the resulting bound/velocity against the sibling's
   direct bond result (activity 20J, mu-form e^{-mu d + 20J|t|e^mu}).
   Report which is stronger and why (the general bound should be
   weaker but same shape — quantify).
6. INSTANCE FAMILY for runner gates: an exactly summable supplied
   family on Z^3 or a chain: pair interactions h_{x,y} = lambda^{|x-y|}
   * (2-site Hermitian) for rational lambda < 1. Compute kappa as an
   exact rational function of lambda and e^mu (geometric sums; be
   careful: diam = |x-y|, |S| = 2, and count pairs through a fixed x
   at each distance r on Z^3: exact count = number of sites at graph
   distance r from x — give the exact formula for Z^3 (it is
   4r^2 + 2 for r >= 1) and the resulting series; state the
   convergence condition lambda e^mu (something) < 1 and closed form).
   Also a 1D-chain variant (count = 2 per distance) for cheap exact
   gates.
7. LIMITS: everything unproven/assumed, every place the supervisor
   must double-check.

Exact arithmetic only for load-bearing constants; no floats except
advisory. Show EVERY step of 3 and 4 — those are where errors hide.
