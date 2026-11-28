lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-29T06:06Z

# gap-purity-toy-first-fable (FINISH row 1697)

Worker: Claude Fable 5.2, high effort, Mac mini worker 1. Pinned commit 34d7b8d23.
Started 2026-11-28T18:06:49Z (date -u).
Status: IN PROGRESS. This file is written step by step. The last section says where the work stopped.

## 0. Plan

1. Read `library/gap-purity-crux-card.md` in full, and the Lean files it cites.
2. Part 1. Read Alpoge's note (`~/ym4d-papers/alpoge-rh/remark.pdf`) and Rubinstein's outline v1.5 in full.
   Write how the toy-setting proof works, what carries the decisive inequality, and what was invented for the hard setting.
3. Part 2 (closed folder). Choose a toy setting for (PUR-io). Prove the purity bound there by hand. Name the object and the inequality.
4. Part 3 (closed folder). Find the analogous object for the Wilson SU(2) transfer. Write its first lemma, or prove that the analogue does not exist.
5. Part 4 (Phase 2). Compare with the registry, rows 1380, 1481-1487, 1688. Row 1696's output is not read.

Labels: PROVED, CITED, ARGUED, GUESSED, UNVERIFIED.

Credit for Part 1: Levent Alpoge (the note and the original proof), Luke Sernau with colleagues at Anthropic and Claude (the shortened proof), Michael Rubinstein (the outline v1.5).

## 1. Part 1. How the Riemann hypothesis proof was found, and what carries it

Sources, both read in full between 2026-11-28T18:07Z and 18:19Z (date -u at both ends):
- [A] Levent Alpoge, "remark" (4 pages, `~/ym4d-papers/alpoge-rh/remark.pdf`). The announcement note of 2026-11-20.
- [R] Michael O. Rubinstein, "An outline of the shortened proof of the Riemann Hypothesis", v1.5, 2026-11-27 (`rh-outline-v1.5.tex`, 1,464 lines). It follows the shortened Lean proof of Luke Sernau, colleagues at Anthropic, and Claude (2026-11-25), which keeps Alpoge's central idea.

All statements in this section are CITED from [A] or [R] unless they carry another label. I checked no step of the proof. Line numbers are those of the `.tex` file.

### 1.1 The toy setting, and the two ideas in it

The toy setting is the Riemann hypothesis for curves over finite fields (function fields). There the statement is a theorem, with short proofs.

[A] p. 1 names two ideas that he held together in the toy setting.

- **Idea 1: Stepanov's method.** One builds an auxiliary function that vanishes at every rational point, to high multiplicity, and whose degree is small. A nonzero polynomial has no more zeros (with multiplicity) than its degree. So the number of rational points is bounded from above. [A] p. 2 says that he recognised the Siegel argument in an OpenAI result as "Stepanov without multiplicity".
- **Idea 2: the sign-only identity q N = M^k + R** ([A] p. 3, footnote 3). A character sum over a "path" quadric x_1 x_2 + ... + x_{k-1} x_k is summed in two orders. Summing over h first gives q times a count N, which has a definite sign. The other order gives a zero mode M^k plus a remainder R of square-root quality, "by iterating Parseval k times". The signs are opposite, so inverse roots cannot cancel. [A] calls this the "sign-only proof of Weil and Deligne".

**What carries the decisive inequality in the toy setting (my reading, ARGUED).** Two facts, one of each kind:

1. A rigidity fact. A nonzero object of a discrete kind cannot be too small or too divisible: a nonzero polynomial of degree D has at most D zeros with multiplicity.
2. A positivity fact. A count is nonnegative, so a one-sided bound is enough. An amplification parameter (the multiplicity in Stepanov, the power k in idea 2) makes the one-sided bound sharp.

The main term is never the difficulty. The whole proof is the comparison of two bounds on one object.

### 1.2 How the same structure appears in the hard setting

[R] Steps 1-10 show the same two facts in the number-field proof.

| Toy setting | Number-field proof ([R]) |
|---|---|
| One-sided bound is enough (a count is >= 0) | Landau's lemma: only the upper bound R(y) <= y^(-1/2+eps) is needed ([R] Section 1, lines 129-161). Zeros of the twists enter with the opposite sign ([R] Section 3, lines 240-314). |
| A nonzero polynomial has at most deg zeros | Chebyshev's principle: a nonzero integer that many primes divide, and that is not too large, bounds a prime sum from above ([R] Section 5, lines 373-405). For algebraic numbers the product formula replaces "a nonzero integer is at least 1" ([R] lines 676-684). |
| Forced vanishing at rational points | Forced divisibility by the inert primes: derivatives of functions with complex multiplication are divisible by p^floor(ap/(p^2-1)) at each inert p ([R] Section 6, lines 490-545). The cause is structural: supersingular reduction, formal group of height two. Split primes do not divide ([R] lines 526-528). |
| Multiplicity | A chain of m theta lifts. Each lift adds the inert-prime divisibility once more ([R] Section 10, lines 954-960). [A] p. 1: multiplicity "is hard to find over the integers, corresponding to something like differentiating whole numbers". The chain length is m of order sqrt(X); [A] credits this suggestion to Claude. |
| Degree of the auxiliary function | Size, in a Gaussian (Bargmann-Fock) norm where |z^j|^2 = j!. In this norm size and twice the divisibility agree in the term j log j, and the period (Chowla-Selberg) matches the constant L'/L(1,chi_d) - gamma ([R] Section 7, lines 567-640). |

### 1.3 What had to be invented to find the analogue

These are the inventions that [A] and [R] name. I list them because Part 3 needs the same list for (PUR-io).

1. **A native form of the amplifier.** Multiplicity does not exist over the integers. The analogue is not a copy; it is a different object (a chain of theta lifts between unitary groups) that does the same work "in a natively automorphic manner" ([A] p. 1; timeline items 4, 8). The gain is linear in m. The cost (control of denominators) is quadratic in m. The balance at m of order sqrt(x) gives the exponent 1/2 ([R] lines 960, 998, 1199).
2. **A source of forced structure.** The inert primes divide CM derivatives for a structural reason. No estimate gives this. ([R] Section 6; [A] timeline item 2.)
3. **A norm in which the two sides agree to leading order.** Without it, a single derivative shows only one half of its size as divisibility ([R] lines 569, 901-906: "Why a single number fails": the cofactor is about half of the logarithm).
4. **One main term, never evaluated, bounded from both sides.** The proof does not make the cofactor small. Theorems A and B give an upper bound and Theorem C gives a lower bound relative to the same enormous quantity h. Then h cancels ([R] Section 9, lines 908-951; A.5, lines 1411-1418). [R] line 951: the product formula alone "does not produce the term Dh: that is the arithmetic content of Theorem C".
5. **Many vectors, not one number.** A Gram determinant of a family that fills all but a proportion 4/b^2 of a D-dimensional space. Hadamard gives the upper bound. The product formula gives the lower bound ([R] Section 8).
6. **A seesaw that makes the object computable.** Lifts out of an indefinite group have no finite formula. The seesaw identity replaces them by finite class sums on definite lattices ([R] Section 11, lines 1048-1055).
7. **A reduction that removes circularity.** The bound is proved for every auxiliary prime d, with no information on zeros. Only afterwards is d chosen, by a zero-density estimate, so that the twists have no zero in one box ([R] lines 314, 319-370). The order of the choices matters.

### 1.4 The lessons I take to (PUR-io) (ARGUED; each is a test, not a method)

- **(S1) Find the rigidity fact first.** The toy proof is short because one discrete fact does the work. A toy for (PUR-io) must show which discrete or structural fact gives purity, and it must be a fact that the abelian twin does not have.
- **(S2) One-sided, by positivity.** Purity is at most 1 always. Only the lower bound 457/625 is needed, and the transfer operator is positive.
- **(S3) The main term must cancel, not be estimated.** Purity is tr(P0 T^(2u)) / tr(P0 T^u)^2. The bulk free energy is the same above and below. A method that bounds numerator and denominator separately must be exact in an extensive quantity (Proposition NO-A in Section 3 makes this precise).
- **(S4) The analogue of the amplifier is not a copy.** If the toy mechanism has no native form at the couplings of the crux card, then the toy does not transport, however clean it is. Part 3 tests this.
- **(S5) Order of choices.** (PUR-io) leaves two free choices: the side l (any multiple of 1024) and the infinite set of cutoffs. A proof may fix them last, as [R] fixes d last.

## 2. Part 2 (closed folder). The toy setting and the toy theorem

Written 2026-11-28T18:22Z (date -u). Phase 1 rule obeyed: besides the crux card I opened only `lean/gapchain/GapChain/Purity.lean` (read in full).

One fact from `Purity.lean` that I use below. The consumer reads less than 457/625. Lines 74-95 (`neutralTailLE_of_purity`) show: purity >= 2/3 at time u gives D - 1 <= 1/2, where D = sum_i (lambda_i/lambda_0)^u is the neutral moment. So the target is a bound on the **neutral tail** tau(u) = sum_{i>=1} (lambda_i/lambda_0)^u at u = side/512.

### 2.1 Choice of the toy, and why

**The toy.** The constant-mode Hamiltonian of SU(2) Yang-Mills in a small periodic box, with a cutoff R on the flat directions.

- D >= 2 is the number of space directions (D = 3 for the real case).
- The variable is x = (x_1, ..., x_D), each x_i in R^3. R^3 stands for su(2), and the cross product stands for the commutator.
- V(x) = (1/2) sum_{i<j} |x_i × x_j|^2. V = 0 exactly when all x_i are parallel. This zero set is the **valley** (the abelian directions). It is not compact.
- Q_R = { x : |x_i| < R for all i }. H_R = -(1/2) Laplacian + V on L^2(Q_R), Dirichlet (Friedrichs extension from C_c^infinity(Q_R)). H_infinity is the same on R^(3D).
- Z_R(s) = tr exp(-s H_R). purity_R(s) = Z_R(2s) / Z_R(s)^2. E_0(R) <= E_1(R) <= ... are the eigenvalues with multiplicity.

**The abelian twin, same normalisation.** All x_i lie on one fixed line (the Cartan line). Then the commutator is zero, V = 0, and H^ab_R = -(1/2) sum_i d^2/dc_i^2 on (-R, R)^D, Dirichlet. This is a free particle in a box.

**Why this is a toy for (PUR-io)** (ARGUED).
- It is the lowest-order Hamiltonian of the zero-momentum modes of SU(2) Yang-Mills on a 3-torus of side L at small coupling g: c_i = g^(2/3) x_i, energy unit g^(2/3)/L. CITED from memory, details UNVERIFIED: M. Lüscher, "Some analytic results concerning the mass spectrum of Yang-Mills gauge theories on a torus", Nucl. Phys. B 219 (1983) 233-261. The holonomies are compact, so the range of x_i is R of order g^(-2/3). Weak coupling is R to infinity.
- So "uniform in R" is the toy form of "uniform in the cutoff": the system size is the length R of the flat directions, and it goes to infinity as the coupling goes to zero.
- The twin fails for the reason weak compact U(1) fails: at weak coupling its flat directions are free.
- It is the simplest model I know in which a commutator, and nothing else, decides between a discrete and a continuous spectrum. The discrete-spectrum fact is CITED: B. Simon, "Some quantum operators with discrete spectrum but classically continuous spectrum", Ann. Phys. 146 (1983) 209-220 (the x^2 y^2 model). The proof below is my own write-up of the same idea, with the constants.

**What the toy does not have.** It has no scale. It has no dimension 4. Its mechanism works in any D >= 2. I chose it because the proof is complete and short, and because its failure to transport (Section 3) can be proved. Section 2.5 names a second toy that does read the dimension, with its theorem cited and not rebuilt.

### 2.2 Theorem TOY

Fix D >= 2. Fix theta in (0,1] and put kappa = sqrt(theta (D-1)/2).

**(a) Fibre inequality.** For every psi in C_c^infinity(R^(3D)),

    <psi, H_infinity psi>  >=  (1 - theta) <psi, -(1/2) Laplacian psi>  +  kappa sum_i <psi, |x_i| psi>.

**(b) Trace bound, uniform in R.** For theta < 1, every s > 0 and every R in (0, infinity],

    Z_R(s)  <=  Z^+(s) := (2 pi (1-theta) s)^(-3D/2) * ( 8 pi / (s kappa)^3 )^D.

**(c) Purity floor, uniform in R.** Put E^*(R_0) = D pi^2/(2 R_0^2) + (D(D-1)/6) (1/3 - 1/(2 pi^2))^2 R_0^4. For every R_0 > 0, every R in [R_0, infinity] and every s > 0,

    purity_R(s)  >=  ( exp(-s E^*(R_0)) / Z^+(s) )^2  >  0.

**(d) Threshold, uniform in R.** There are R_0 < infinity and s_0 < infinity such that purity_R(s) >= 457/625 for all s >= s_0 and all R in [R_0, infinity]. With delta = E_1(infinity) - E_0(infinity) > 0, one may take R_0 with E_0(R_0) <= E_0(infinity) + delta/2 and

    s_0 = 1 + (2/delta) log( exp(E^*(R_0)) Z^+(1) / 0.169 ).

**(e) The abelian twin fails.** For every s > 0 and R >= pi sqrt(s/8),

    purity^ab_R(s)  <=  ( e pi sqrt(s/2) / R )^D.

So at every fixed s the twin's purity goes to zero as R goes to infinity. No s gives a bound uniform in R.

Status: (a), (b), (c), (e) PROVED below with explicit constants. (d) PROVED with one constant, delta, defined by an existence argument (simplicity of the ground state). Two standard facts are CITED, not rebuilt: the Feynman-Kac formula with strict positivity of the heat kernel, and the theorem that a positivity-improving semigroup has a simple ground state (Reed-Simon, Methods of Modern Mathematical Physics IV, Theorem XIII.44; the theorem number is from memory, UNVERIFIED).

### 2.3 Proof

**Step 1: the one-dimensional inequality.** For f in C_c^infinity(R), a, b > 0 and omega >= 0:

    (a/2) ∫ f'^2 + (b omega^2/2) ∫ y^2 f^2  >=  (1/2) sqrt(ab) omega ∫ f^2.

Proof. 0 <= ∫ (sqrt(a) f' + sqrt(b) omega y f)^2 = a ∫ f'^2 + b omega^2 ∫ y^2 f^2 + 2 sqrt(ab) omega ∫ y f f'. Integration by parts gives 2 ∫ y f f' = ∫ y (f^2)' = -∫ f^2. Divide by 2. ∎

**Step 2: one ordered pair.** Fix i ≠ j and fix all variables except x_j. Let omega = |x_i|. If x_i ≠ 0, choose orthonormal coordinates (y_1, y_2, y_3) for x_j with y_3 along x_i. Then |x_i × x_j|^2 = omega^2 (y_1^2 + y_2^2). Apply Step 1 in y_1 and in y_2 (integrate over the other coordinates of x_j), and drop the y_3 derivative, which is nonnegative. For every g in C_c^infinity(R^3):

    (a/2) ∫ |grad g|^2 dx_j + (b/2) ∫ |x_i × x_j|^2 g^2 dx_j  >=  sqrt(ab) |x_i| ∫ g^2 dx_j.

This is also true for x_i = 0.

**Step 3: sum over pairs; proof of (a).** V = (1/4) sum over ordered pairs (i,j), i ≠ j, of |x_i × x_j|^2. Each j has D-1 partners i, so

    theta * (-(1/2) Laplacian) = sum over ordered pairs (i,j) of (theta/(D-1)) * (-(1/2) Laplacian_{x_j}).

Use Step 2 with a = theta/(D-1) and b = 1/2 for each ordered pair, with g = psi as a function of x_j, and integrate over the other variables (Fubini; psi is smooth with compact support). Each ordered pair gives sqrt(theta/(2(D-1))) <psi, |x_i| psi>. Each i occurs in D-1 ordered pairs. The sum is sqrt(theta (D-1)/2) sum_i <psi, |x_i| psi>. The part (1-theta)(-(1/2) Laplacian) of the kinetic energy is left over. ∎

*Where the commutator enters.* Step 2 is the only place. The frequency omega of the transverse oscillator is |x_i|: the position along the valley sets the stiffness across it. For the twin the cross product is zero, omega = 0, and (a) says only H >= (1-theta)(-(1/2) Laplacian). For D = 1 there is no pair and kappa = 0.

**Step 4: proof of (b).** Let H^- = (1-theta)(-(1/2) Laplacian) + kappa sum_i |x_i| on R^(3D) (form sum). C_c^infinity(Q_R) is a form core of H_R, it lies in the form domain of H^-, and on it the form of H_R is at least the form of H^- by (a). By the min-max principle the k-th eigenvalue of H_R is at least the k-th eigenvalue of H^-, for every k and every R in (0, infinity]. So Z_R(s) <= tr exp(-s H^-).

Bound for tr exp(-s H^-). Put alpha = 1-theta, N = 3D, W = kappa sum |x_i|. By the Feynman-Kac formula (CITED), the diagonal kernel is

    exp(-s H^-)(x,x) = (2 pi alpha s)^(-N/2) E[ exp( -∫_0^s W(x + b_t) dt ) ],

where b is the Brownian bridge from 0 to 0 in time s with variance parameter alpha. Jensen's inequality for the uniform probability measure dt/s on [0,s] gives exp(-∫_0^s W dt) <= (1/s) ∫_0^s exp(-s W(x + b_t)) dt. Integrate over x first. For every fixed t and every value of b_t, ∫ exp(-s W(x + b_t)) dx = ∫ exp(-s W(x)) dx. So

    tr exp(-s H^-) <= (2 pi alpha s)^(-N/2) ∫ exp(-s W(x)) dx = (2 pi (1-theta) s)^(-3D/2) ( ∫_{R^3} exp(-s kappa |y|) dy )^D,

and ∫_{R^3} exp(-c|y|) dy = 8 pi / c^3. (This is the Golden-Thompson-Symanzik bound; the three lines above are its usual proof.) ∎

**Step 5: proof of (c).** Let p_i = exp(-s E_i(R)) / Z_R(s). Then purity_R(s) = sum_i p_i^2 >= p_0^2. By (b), Z_R(s) <= Z^+(s). For R >= R_0, E_0(R) <= E_0(R_0) (a trial function on Q_{R_0}, extended by zero, is a trial function on Q_R). It remains to bound E_0(R_0) from above by a trial function. Take psi = prod_i phi(x_i), phi(y) = sin(pi |y| / R_0) / |y|, the Dirichlet ground state of the ball of radius R_0 in R^3. Its kinetic energy is pi^2/(2 R_0^2) per factor. With r = |y|: <r^2> = ∫_0^{R_0} r^2 sin^2(pi r/R_0) dr / ∫_0^{R_0} sin^2(pi r/R_0) dr = R_0^2 (1/3 - 1/(2 pi^2)). The directions of x_i and x_j are independent and uniform, so <|x_i × x_j|^2> = <r^2>^2 * (2/3). Hence <V> = (1/2) * (D(D-1)/2) * (2/3) * <r^2>^2 = (D(D-1)/6) (1/3 - 1/(2 pi^2))^2 R_0^4. The sum is E^*(R_0). ∎

*Numbers for D = 3, theta = 1/2, R_0 = 2.13:* E^* = 4.91, Z^+(s) = 2081 s^(-27/2). The floor at s = 1 is about 1.2e-11. It is small, positive, and does not depend on R. For comparison (CITED from memory, UNVERIFIED): the true ground energy for D = 3 is about 4.117 (Lüscher and Münster, Nucl. Phys. B 232 (1984) 445).

**Step 6: proof of (d).**
1. H_infinity has compact resolvent, by (b). V is continuous and nonnegative, so exp(-s H_infinity) has a strictly positive kernel (Feynman-Kac, CITED). So it is positivity improving, and E_0(infinity) is simple (CITED). So delta = E_1(infinity) - E_0(infinity) > 0.
2. For each k, E_k(R) is nonincreasing in R and E_k(R) >= E_k(infinity) (min-max, extension by zero). Also E_0(R) -> E_0(infinity) as R -> infinity: C_c^infinity(R^(3D)) is a form core of H_infinity, and each function in it has support in some Q_R. Choose R_0 with E_0(R_0) <= E_0(infinity) + delta/2.
3. For R >= R_0: E_1(R) - E_0(R) >= E_1(infinity) - E_0(R_0) >= delta/2.
4. Let tau_R(s) = sum_{i>=1} exp(-s (E_i(R) - E_0(R))). For s >= 1 and R >= R_0, each term is at most exp(-(s-1) delta/2) exp(-(E_i(R) - E_0(R))), so

       tau_R(s) <= exp(-(s-1) delta/2) * exp(E_0(R)) Z_R(1) <= exp(-(s-1) delta/2) * exp(E^*(R_0)) Z^+(1).

5. purity_R(s) = (1 + sum_{i>=1} exp(-2s(E_i - E_0))) / (1 + tau_R(s))^2 >= (1 + tau_R(s))^(-2). This is at least 457/625 when tau_R(s) <= 25/sqrt(457) - 1 = 0.16945... The value s_0 of the statement makes tau_R(s) <= 0.169. ∎

**Step 7: proof of (e).** The eigenvalues of H^ab_R are (pi^2/(8 R^2)) sum_i k_i^2, k_i >= 1. Put a = s pi^2/(8 R^2) <= 1. The largest weight is p_0 = ( sum_{k>=1} exp(-a(k^2 - 1)) )^(-D). With K = floor(a^(-1/2)) >= 1: sum_{k>=1} exp(-a(k^2-1)) >= sum_{k=1}^{K} exp(-a k^2) >= K/e >= a^(-1/2)/(2e). So p_0 <= (2e sqrt(a))^D = (e pi sqrt(s/2) / R)^D. Finally purity = sum p_i^2 <= p_0 sum p_i = p_0. ∎

**Remark (gauge-invariant sector).** The physical toy space is the subspace of functions invariant under the simultaneous rotation of all x_i (Gauss law). H_R commutes with these rotations and the simple ground state is invariant. Restriction to the subspace removes excited terms only, so (b), (c), (d) hold there with the same constants.

### 2.4 The object and the inequality that carry the proof

- **Object:** the family of transverse oscillators over the valley. For each point x_i of one abelian direction, the other fields see a harmonic well of stiffness |x_i|^2 across the valley. In the field theory these transverse modes are the charged (off-diagonal) gluons in an abelian background.
- **Inequality:** Step 1, the uncertainty inequality for one transverse mode, (a/2) p^2 + (b omega^2/2) y^2 >= (1/2) sqrt(ab) omega. Summed over the fibre it turns the flat valley into a wall kappa sum |x_i|. Everything after Step 3 is general (min-max, Golden-Thompson, Perron-Frobenius).
- **What reads the group:** omega = |x_i| is the commutator. It is zero for the twin.
- **Twin test (crux card).** A U(1) theory with one charged scalar zero mode phi has V = (1/2)|x|^2 |phi|^2, and Steps 1-3 hold for it verbatim. So the inequality reads "the abelian direction has a charged partner", not "SU(2)". Pure SU(2) has the partner for free; pure U(1) has none. This is honest but it is a weaker reading of the group than the card asks: a neutral spectator does not spoil the step, and the step does not see the centre.
- **How this differs from the lesson (S1).** The fact that carries the toy is an uncertainty inequality. It is not a discrete or rigid fact. It loses a constant factor in the energy (theta, and the dropped longitudinal term). That loss is harmless in the toy, because the toy has finitely many modes. Section 3 shows that the same loss is fatal on a lattice.
