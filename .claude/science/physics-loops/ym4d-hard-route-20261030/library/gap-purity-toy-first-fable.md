lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-29T06:06Z

# gap-purity-toy-first-fable (FINISH row 1697)

Worker: Claude Fable 5.2, high effort, Mac mini worker 1. Pinned commit 34d7b8d23.
Started 2026-11-28T18:06:49Z (date -u).
Status: DONE at 2026-11-28T18:35Z (date -u). Sections 1 to 5; the RESULT line is the last line.

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
| Degree of the auxiliary function | Size, in a Gaussian (Bargmann-Fock) norm where the squared norm of z^j is j!. In this norm size and twice the divisibility agree in the term j log j, and the period (Chowla-Selberg) matches the constant L'/L(1,chi_d) - gamma ([R] Section 7, lines 567-640). |

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

**Reference check (between 2026-11-28T18:22Z and 18:28Z, INSPIRE API, titles and journals only; I read none of these papers in this session).** Confirmed to exist with the stated data: Lüscher, Nucl. Phys. B 219 (1983) 233; Lüscher and Münster, Nucl. Phys. B 232 (1984) 445; Simon, Ann. Phys. 146 (1983) 209. What I say about their content is from memory.

**Guide computation (not a proof step).** Script `/tmp/toyfirst-fable-1697/x2y2.py`, run under the numeric lock at 67% memory free. It is the two-variable relative of the toy, H = -(1/2) Laplacian + (1/2) x^2 y^2 on [-R,R]^2, by finite differences, against the free twin on the same square.

| R | E_0 | E_1 - E_0 | purity at s = 4 | purity at s = 8 | free twin at s = 4 | free twin at s = 8 |
|---|---|---|---|---|---|---|
| 3 | 0.5671 | 0.7093 | 0.795 | 0.986 | 0.509 | 0.866 |
| 6 | 0.5540 | 0.6351 | 0.712 | 0.975 | 0.111 | 0.240 |
| 12 | 0.5540 | 0.6349 | 0.711 | 0.975 | 0.025 | 0.052 |

The run agrees with the theorem: the purity of the commutator model settles as R grows, and the twin's purity falls like R^(-2). The run proves nothing. The grid error is not bounded, and 260 eigenvalues were kept.

### 2.5 A second toy that reads the dimension (cited, not rebuilt)

The toy of 2.1 has no scale. The toy that has one is the Migdal-Kadanoff (MK) recursion. I name it because Part 3 needs it. I do not prove its theorem here.

- **The model.** A positive class function f on the group stands for the effective plaquette weight. One step of scale b in dimension d is: convolve b^2 copies (decimation; the character coefficients c_j go to c_j^(b^2)), then take the pointwise power b^(d-2) (bond moving).
- **The theorem (CITED from the abstracts only; corrected 2026-11-28T18:34Z after I fetched the publisher pages; the PDFs are behind a paywall and I stopped there).** K. R. Ito, "Analytic study of the Migdal-Kadanoff recursion formula", Commun. Math. Phys. 95 (1984) 247: abstract, for D less than 4 the effective actions of U(1) models "are uniformly driven to the high temperature region no matter how low the initial temperature is". K. R. Ito, "Permanent quark confinement in four-dimensional hierarchical lattice gauge theories of Migdal-Kadanoff type", Phys. Rev. Lett. 55 (1985) 558 (title only). V. F. Müller and J. Schiemann, "Convergence of Migdal-Kadanoff iterations in non-abelian lattice gauge models", Commun. Math. Phys. 97 (1985) 605: abstract, for SU(N) or U(N) "the Gibbs factor of a plaquette with Wilson action is driven to 1 for all values of the temperature"; the page prints the dimension range as "d<4", which may be a lost "at most" sign (UNVERIFIED). V. F. Müller and J. Schiemann, "Convergence of Migdal-Kadanoff iterations: a simple and general proof", Lett. Math. Phys. 15 (1988) 289: abstract, convergence "for a large class of functions on compact connected Lie groups", with "lower bounds for string tension and mass gap in hierarchical four-dimensional lattice gauge and two-dimensional spin models".
- **Twin test on the cited theorem (this corrects what I first wrote from memory).** "Compact connected Lie groups" includes U(1). So the convergence theorem is blind to the group: in the MK model the abelian twin also flows to strong coupling in four dimensions. (Title-level support: K. R. Ito, "Absence of the Kosterlitz-Thouless fixed points in the Migdal-Kadanoff recursion formulas", Phys. Rev. Lett. 54 (1985) 2383.) The MK model has no Coulomb phase. The group is read only by the rate: a fixed drop of beta per step for SU(2) (below), against a drop of order exp(-c beta) for U(1) (ARGUED from the image terms). On a trajectory beta_K = c K the SU(2) model reaches strong coupling in K steps and the U(1) model does not (ARGUED). The rate proved in the 1988 paper is not known to me.
- **What carries it (my computation, exact for the leading term of the SU(2) heat kernel).** Let theta in (0, pi) be the class angle and g_t(theta) = (theta/sin theta) exp(-theta^2/(4t)), the leading term of the heat kernel on SU(2) = S^3. Then g_t^p = (theta/sin theta)^(p-1) g_{t/p}. PROVED: theta/sin theta >= exp(theta^2/6) on (0, pi), because log(theta/sin theta) = sum_{k>=1} zeta(2k) theta^(2k) / (k pi^(2k)) has only nonnegative terms and the first is theta^2/6. So g_t^p / g_{t'} is nondecreasing in theta when 1/t' = p/t - 2(p-1)/3. The power is flatter than the Gaussian rule t/p predicts. With beta = 1/(2t), p = b^(d-2), and decimation t -> b^2 t, one step gives (ARGUED: the true heat kernel has image terms, and I did not prove that decimation keeps this order)

      beta'  =  b^(d-4) beta  -  (b^(d-2) - 1) / (3 b^2).

  - d = 4: beta' = beta - (b^2-1)/(3b^2). The coupling drops by a fixed amount at every step. The drop is the Van Vleck factor theta/sin theta, that is, the curvature of S^3.
  - U(1), d = 4: the heat kernel on the circle has no such factor. The power of a Gaussian is a Gaussian, and beta' = beta up to image terms of order exp(-pi^2 beta). The step is void.
  - SU(2), d = 5: beta' = b beta - ... grows. No flow to strong coupling from weak coupling.
  - U(1), d = 3: beta' = beta/b. The coupling drops for the trivial reason.
- **The object and the inequality of this toy:** the effective plaquette as a class function; the inequality theta/sin theta >= exp(theta^2/6), raised to the power b^(d-2) - 1. It reads the group (curvature) and the dimension (the exponent b^(d-4)).

## 3. Part 3 (closed folder). The analogue for the Wilson SU(2) transfer

Written from 2026-11-28T18:29Z (date -u). Notation: on a cube Γ of side n at coupling beta, let lambda_0 >= lambda_1 >= ... >= 0 be the eigenvalues of T on the neutral sector (range of P0), with multiplicity, and x_i = lambda_i / lambda_0 in [0,1]. Put D(v) = sum_i x_i^v = tr(P0 T^v)/lambda_0^v and tau(v) = D(v) - 1 when lambda_0 is simple. Then purity(u) = D(2u)/D(u)^2. `Purity.lean` lines 60-70 and 77-87 give this form (slots in [0,1], slot zero equal to 1, summable for v >= 2).

Verdict first. **The carrying inequality of the toy of 2.1 has no analogue at the couplings of the crux card.** Sections 3.1-3.3 prove this in three forms. The second toy (2.5) has an analogue, written in 3.5; it is a known programme, and it dies at a named step. Section 3.4 holds one bookkeeping identity that respects lesson (S3).

### 3.1 One family, two corners (Lemma NEC, PROVED)

The Wilson transfer is one family in three parameters: side n, coupling beta, time u.

- **Crux corner:** n = l L^k >= 2^70, beta = betaAt(k), u = n/512.
- **Toy corner:** n fixed, beta to infinity, u of order beta^(1/3) (the scaling of 2.1: R of order g^(-2/3), energy unit g^(2/3)).

**Lemma NEC (necessary and sufficient sizes).** Assume lambda_0 is simple.
(i) If tau(u) <= 25/sqrt(457) - 1 = 0.16945..., then purity(u) >= 457/625.
(ii) If purity(u) >= 457/625, then tau(u) <= 168/457, and u log(lambda_0/lambda_1) >= log(457/168) > 1. With u <= n/512: n (E_1 - E_0) > 512, where E_i = -log lambda_i.

Proof. purity = (1 + tau(2u))/(1 + tau(u))^2 and 0 <= tau(2u) <= tau(u). So (1+tau)^(-2) <= purity <= (1+tau)^(-1). (i) follows from the left bound. For (ii), the right bound gives 1 + tau <= 625/457. One term of tau is x_1^u, so x_1^u <= 168/457. ∎

**Consequence (ARGUED).** In the toy corner the target is false for SU(2) itself. At small coupling on the scale of the box, the neutral sector holds states with n (E_i - E_0) of order 4 pi (two gluons with opposite lowest momenta) and of order g^(2/3) (the constant modes of 2.1). Both are far below 512. So the toy mechanism lives exactly where purity at time n/512 fails. The number 512 is the line that shuts out every small-box mechanism. Free photons fail (ii) for the same reason, with n (E_1 - E_0) = 4 pi at every size.

### 3.2 The toy proof, moved line by line (Proposition EMPTY, PROVED from the spectrum facts above)

| Toy step | The same step for the Wilson transfer at one cutoff | What it gives |
|---|---|---|
| (a) fibre inequality | none needed: the configuration space SU(2)^links is compact | nothing |
| (b) trace bound uniform in R | tr(P0 T^v) is finite for v >= 2, for every Γ and beta | true, no content |
| (d) simple ground state, so tau(s) -> 0 | x_i in [0,1], sum x_i^2 finite, so D(v) -> m_0 and purity(u) -> 1/m_0 as u -> infinity, m_0 the multiplicity of x = 1 | true, no rate |

**Proposition EMPTY.** For every cube Γ and every beta > 0, purity(Γ, beta, u) converges to 1/m_0 as u goes to infinity. Proof: dominated convergence in D(v) = sum x_i^v, with x_i^v <= x_i^2 for v >= 2. ∎

The same holds for compact U(1) (ARGUED: its configuration space is compact too). So the toy proof moves to the lattice verbatim, and it proves a statement that is true, blind to the group, and silent on the rate. In the toy the rate constant delta came from Perron-Frobenius. That argument gives no number, and the crux is only the number: n (E_1 - E_0) > 512 at u = n/512.

**Where the toy's uniformity went.** "Uniform in R" in the toy is "uniform in the coupling on the scale of the box, as that coupling goes to zero". For the lattice that is the limit of a small physical box. (PUR-io) asks for a large physical box. The two statements sit at opposite ends of one function. Define g_k(l) = n (E_1 - E_0) for n = l L^k at beta = betaAt(k). The toy describes g at its small end: g of order (coupling at the box scale)^(2/3) for SU(2), against (coupling)^2 for the twin (ARGUED, from Lüscher 1983 as I recall it). The crux needs g above 512 (and about 12,000 by the card's estimate). Between the two ends is the range where the coupling at the box scale is of order one. The toy gives nothing there.

### 3.3 Proposition NO-A: a comparison proof needs an extensive quantity to absolute precision 80/n (PROVED)

The toy bounds numerator and denominator separately: Z from above by a comparison operator, E_0 from above by a trial function. This is the route that lesson (S3) warns against. The cost can be stated exactly.

**Proposition NO-A.** Let Z^+ >= tr(P0 T^u) and 0 < lambda^- <= lambda_0 be the two numbers that a proof controls. Suppose the proof concludes purity(u) >= 457/625 from one of the two toy routes: purity >= ((lambda^-)^u / Z^+)^2 (route (c)), or tau(u) <= Z^+/(lambda^-)^u - 1 and Lemma NEC (i) (route (d)). Then Z^+/(lambda^-)^u <= 25/sqrt(457). Hence, with E^+ = -(1/u) log Z^+ <= E_0 and E^- = -log lambda^- >= E_0:

    E^- - E^+  <=  (1/u) log(25/sqrt(457))  =  0.15653.../u  =  80.14.../n   at u = n/512.

Proof. Both routes need (Z^+/(lambda^-)^u)^(-2) >= 457/625. Take logarithms. E^+ <= E_0 because Z^+ >= lambda_0^u. ∎

**What it means.** E_0 is the total vacuum energy of the cube. It is extensive, of order n^3. The proof must enclose it between two bounds that differ by at most 80.1/n, at n >= 2^70. An inequality that loses a fixed fraction of one mode's zero-point energy, as Step 1 of the toy does (the factor theta and the dropped longitudinal term), loses an amount of order n^3 (ARGUED: one such loss per mode). So no fibre inequality of the toy's kind, and no Golden-Thompson step, can enter a proof of (PUR-io) through routes (c) or (d). This is the purity form of [R]'s "why a single number fails": the cofactor there, the vacuum energy here, cannot be made small; it must cancel.

### 3.4 Lemma RATIO: the form in which the main term cancels term by term (PROVED; bookkeeping, not a candidate)

**Lemma RATIO.** Assume lambda_0 is simple. For integers v >= 2 put r(v) = tr(P0 T^(v+1)) / (lambda_0 tr(P0 T^v)) = D(v+1)/D(v). Then
1. 0 < r(v) <= 1, r is nondecreasing in v, and r(v) -> 1.
2. purity(u) = prod_{v=u}^{2u-1} r(v)^2 * prod_{v>=2u} r(v), for u >= 2.
3. With q(v) = -log r(v) >= 0 (nonincreasing): log(1/purity(u)) = 2 sum_{v=u}^{2u-1} q(v) + sum_{v>=2u} q(v).
4. Necessary for purity(u) >= 457/625: q(2u-1) <= log(625/457)/(2u) = 0.15653/u. Sufficient: 2 sum_{v>=u} q(v) <= log(625/457) = 0.31307...

Proof. D is nonincreasing and tends to 1, so r <= 1 and prod_{v=u}^{V} r(v) = D(V+1)/D(u) -> 1/D(u). Then purity = D(2u)/D(u)^2 = (prod_{v>=u} r)^2 / prod_{v>=2u} r, which is item 2. r is nondecreasing because D(v) D(v+2) >= D(v+1)^2 (Cauchy-Schwarz on sum x_i^v). Item 4: all terms of item 3 are nonnegative, the 2u terms of the first sum are each at least q(2u-1), and the whole is at most 2 sum_{v>=u} q(v). ∎

**Reading.** r(v) lambda_0 = Z(v+1)/Z(v) is the factor by which the neutral partition function grows when one time layer is added to a torus of time length v. Its limit is lambda_0. So purity is a statement about one sequence, Z(v+1)/Z(v) for v >= u, and about how fast it reaches its own limit. No vacuum energy has to be known. Item 4 says: at v = n/256 the growth factor must already equal its limit up to the factor exp(-80.1/n).

**Twin test.** The lemma is an identity for any positive trace-class operator. It holds for U(1) verbatim. It reads nothing. I record it only because it is the form that (S3) asks for.

### 3.5 The analogue of the second toy, its first lemma, and where it dies

**Object.** The effective plaquette at scale r: the law rho_r of the class angle theta of the holonomy around a planar r × r loop, under the Wilson law at beta. It is a positive class function on SU(2). Its character coefficients are the Wilson loops in all representations, <chi_j(W_r)>/(2j+1). In the MK toy this object is the iterate f_K, and "strong coupling at the box scale" means that rho at the box scale is close to Haar measure on the integer-spin and half-integer-spin coefficients alike.

**First lemma, toy level (PROVED in 2.5 for the model family g_t).** For all t > 0 and all integers p >= 2: g_t^p / g_{t'} is nondecreasing on (0, pi), where 1/t' = p/t - 2(p-1)/3. The constant 2/3 is 4 times the 1/6 of theta/sin theta >= exp(theta^2/6).

**First lemma, native form (GUESSED; a target, not a result).** Let M_p f = f^p / ∫ f^p (bond moving) and let D_b be b^2-fold convolution. For every beta >= beta_*, every scale b^j with b^(j+1) <= n/2:

    rho_{b^(j+1)} / ( M_{b^2} D_b rho_{b^j} )  is nondecreasing in theta on (0, pi).

In words: the true holonomy law at scale b r is at least as disordered as the MK image of the true law at scale r. With the cited MK convergence theorem this would drive rho at the box scale to Haar. (By 2.5 that theorem is blind to the group; the rate is what must be carried.)

- **The step that reads the group and the dimension:** the Van Vleck factor inside M_p, with p = b^(d-2) = b^2 exactly cancelling the decimation b^2 in d = 4. Curvature of S^3 is the gain; the cancellation is the dimension.
- **How it fails for weak four-dimensional compact U(1):** the native statement is false there, not void. The MK image of a U(1) law still flows to disorder (CITED from the abstracts in 2.5). The true law does not: weak compact U(1) in four dimensions has a Coulomb phase (CITED from memory, UNVERIFIED in this session: A. Guth, Phys. Rev. D 21 (1980) 2291; J. Fröhlich and T. Spencer, Commun. Math. Phys. 83 (1982) 411). So no proof of the native lemma can be blind to the group. The toy-level lemma is void for U(1) (no factor theta/sin theta).
- **Where it is likely to die:** at the comparison between the true law and its MK image. Bond moving is known to bound partition functions in one direction only. An order on holonomy laws needs a correlation inequality of Ginibre type for a non-abelian group, and none is known. This is the open step of Tomboulis's programme (E. T. Tomboulis, arXiv:0707.2179; criticism by K. R. Ito and E. Seiler, arXiv:0711.4930 and arXiv:0803.3019; all three exist on INSPIRE, content from memory).
- **Pre-filter of the crux card.** (Q1) Two laws: the true law at scale b r, and the MK image of the true law at scale r. (Q2) The key step is needed at the scale where the effective coupling is of order one; nothing replaces the small parameter there except the unknown correlation inequality. By the card's rule this is a stop. (Q3) The sign is fixed by theta/sin theta > 1 (curvature of the group); for the U(1) twin the factor is 1; for five-dimensional SU(2) the exponent b^(d-4) > 1 reverses the flow; for three-dimensional compact U(1) the exponent b^(-1) gives the same sign as SU(2). (Q4) Not computed: no loss per scale exists until the comparison holds.

**Status of 3.5:** not a new method (Tomboulis's programme, MK), no proved native lemma. I list it because the task asks for the analogous object. Phase 2 checks whether the folder holds it.

### 3.6 The toy-first verdict for Part 3

1. **Toy of 2.1 (commutator wall).** Proved in the toy. Its analogue at the crux corner does not exist: the target is false where the mechanism lives (3.1), the proof moves to a statement with no rate (3.2), and its kind of inequality cannot meet the precision 80/n that any separate bound needs (3.3).
2. **Toy of 2.5 (MK).** The analogue exists as an object. Its first native lemma is the known open comparison. It stops at pre-filter question (Q2).
3. **What the RH lessons add.** (S3) is now exact: Proposition NO-A and Lemma RATIO. (S1) is not met: neither toy is carried by a discrete fact. I looked for one (integer multiplicity of the top eigenvalue; forced multiplicities from a non-abelian symmetry, in the manner of a trace bound against a multiplicity) and found none that acts on the neutral sector: its symmetry group (translations, the cubic group, the centre) has irreducible representations of dimension at most 48 on the lattice (ARGUED), for SU(2) and U(1) alike.

## 4. Part 4 (Phase 2). Comparison with the registry and the record

Phase 2 opened after Part 3 was saved (2026-11-28T18:29:53Z); this section was written at 18:35Z (both date -u). Method: keyword counts over `library/open-registry.md`, `library/open-core.md`, `FINISH.md` and `library/*.md`, then the RESULT parts of the rows named in the brief, then the nearest files by line.

**Search record.** `library/open-registry.md` (synced at row 391, the existence chain) and `library/open-core.md` have no hit for toron, Lüscher, Migdal, Tomboulis, Golden-Thompson or step scaling. The gap lane's record is in `FINISH.md` and `library/`. Hits there: toron 19 rows and 98 files; Tomboulis 47 rows and 126 files; Migdal 17 rows and 83 files; x^2 y^2 in 15 files; "Van Vleck" in none.

**Disclosure.** One grep over `library/gap-purity-*.md` printed line 57 of `library/gap-purity-y4-solve-fable.md`, the output of row 1696, which the brief bars. The line is about the one-link Wilson kernel. I did not open the file, I used nothing from the line, and I excluded the file from later searches.

### 4.1 Piece by piece

| Piece of this file | Nearest row or file, with a phrase quoted | What differs | Mark |
|---|---|---|---|
| Part 1, the architecture (one-sided, rigidity against size, main term cancels, amplifier, order of choices) | Row 1688, `gap-purity-rh-strategy-fable.md` Part 1 (moves M1-M13): "toy, defect list, exact cost, named missing device, in that order". Rows 1481, 1482, 1487: "The direction 'tools of the RH proof for the crux' is CLOSED on the record". | I read the new source (Rubinstein's outline v1.5 of the shortened proof; the earlier rows read the first explainer). The Gram-determinant form (Theorems A, B, C; h cancels) is new in the source, not in the lesson: row 1688 has (Y2) "the extensive terms cancel identically". | ON FILE. No new tool. |
| Lessons (S1)-(S5) | Row 1688 Section 2.3, wish list (Y1)-(Y4) | (S1) is (Y4) in other words. (S5) is move M7 there. | ON FILE |
| Toy of 2.1 as an idea | Row 1686, `gap-purity-mp-strategy-fable.md` L378-L391 (P25): "the non-abelian term Σ&#124;[c_i,c_j]&#124;² confines the flat valleys quantum-mechanically, so the spectrum is discrete with gap of order g^{2/3}/L. Simon proved the discreteness". Also `gap-skeleton-max-b.md` L107; rows 930-942 (torons). | Same toy, same two references. | ON FILE |
| Theorem TOY (a)-(e) with proof and constants | `gap-mini-solve-d-fable.md` L82: "Zero-point closing of flat valleys (Simon's x^2 y^2, Luscher's toron Hamiltonian) as a volume-uniform operator inequality" is listed there as an idea and set aside. I found no written proof with constants (keyword search only; a search that finds nothing does not prove absence). | Here: the fibre inequality with kappa = sqrt(theta(D-1)/2), the trace bound, the uniform purity floor, the threshold, the twin. | NEW AS A WRITTEN TOY PROOF. Not a candidate for (PUR-io). |
| 3.1, the target is false in the toy corner | Row 1688 Section 2.3: "Small physical volume: perturbative. Defect: the purity fails there for SU(2) as for U(1), because modes of energy 2π/ℓ are not suppressed at time ℓ/512". The standing fact test SMALL-BOX (rows 931 on). | Same statement. Lemma NEC (ii) adds the exact line n(E_1 - E_0) > 512. | ON FILE |
| Lemma NEC | Row 1688 Lemma P3 (ii): "M(2s) ≤ M(s) gives c ≤ 1/M(s)". `Purity.lean` L74-L95. Row 1487: "P_K = 1/(1 + delta_u)". | Same two-sided bound, other constants. | ON FILE |
| Proposition EMPTY | Row 1688 Lemma P3 (i) gives the rate form; the limit statement is elementary. | None of substance. | ON FILE (elementary) |
| 3.2, the toy proof gives no rate | `gap-mini-solve-d-fable.md` L82, same table row: "it bounds H below, not E_1 - E_0; in a background field the spin term reverses the sign (the paramagnetic term that gives asymptotic freedom)". Row 1647 Theorem 2 (4D and 5D torons behave alike; a single-scale comparison cannot carry the gain "without multi-scale ultraviolet-to-infrared running"). | Same verdict, reached again from the toy side. The five-dimensional test is already run there: my toy holds for every D >= 2, so it does not read the dimension. | ON FILE |
| Proposition NO-A (precision 80.14/n on the total vacuum energy) | Row 1688 Section 2.3: the classical (Jensen) bound is exp(-c n³), "off at the LEADING order". Row 1686 Section 4.2: Golden-Thompson-type bounds "per mode ... lose the factor exp(ω/2T), which is the whole effect". | Same obstruction. NO-A states it for every comparison route at once and gives the number. | VARIANT (sharper form of a fact on file) |
| Lemma RATIO | Row 1520, `gap-twoperiod-solve-fable.md` L319-L333: "The vacuum cancels (v + 2v = (v+1) + (2v-1))", with the unit-step drops log[Z_+(v)^2 Z_+(2v+2) / (Z_+(v+1)^2 Z_+(2v))]. | Same bookkeeping with unit steps. RATIO writes the whole purity as one product. | ON FILE in substance |
| 2.5 and 3.5, the MK toy and the curvature gain | `gap-mech-direction2-fable.md` L260: "Migdal-Kadanoff or hierarchical step as a template (the curvature gain of a convolution on S^3 times the classical factor 2^(d-4))", pointing to Proposition G1 (row 1128) and row 1025. `gap-cr-tomboulis-max.md` L354 has the heat kernel with (psi/sin psi). Row 1390 table D1: "the factor is 2^(d-4) by construction". | Same object and same reading. My formula beta' = b^(d-4) beta - (b^(d-2) - 1)/(3 b^2) is a worked instance. | ON FILE |
| 3.5, where the native lemma dies | Row 1025: Proposition BR ("one inequality (TB)_n between the Wilson model and its Migdal-Kadanoff image"), Proposition SIGN ("bond moving has no sign on the twist quotient"), Identity MOV. | Row 1025 proves the death that I only named. | ON FILE, and closed there |
| 2.5, the cited MK theorems are blind to the group | Row 736, `prior/gap-precedent-lit.md` Section 8: Ito's papers "NOT READ"; the local file `~/ym4d-papers/gap-precedent-lit-ito84/ito84.pdf` is an HTML page of an unrelated article. Row 735 used the MK model as "recalled". | Read here from the publisher abstracts: Müller and Schiemann (1988) prove convergence for compact connected Lie groups, so U(1) is included, and they give lower bounds for the mass gap of the hierarchical model. | NEW AS A READ FACT (abstract level). It is a twin-test result on a cited precedent. |
| 3.6 item 3, no forced multiplicity on the neutral sector | Row 1482: "the RH frame second-moment estimate Tr(Q^2)/(Tr Q)^2 at most (1 + eta)/D" points the wrong way. Row 1201 (box symmetry group), by its row title only. | I did not find the multiplicity-against-trace idea stated; it is void in two lines, so I did not search further. | VOID either way |

### 4.2 The rows named in the brief

- **Row 1380, Theorem C1** ("for lab-frame link-end moves every bound of form (2.2) is at least ((72/7) K + (3/2) B) times a site-local class norm: no gain in scale"; "a gain can only come from dressed moves, a renormalization step"). The toy inequality of 2.2 (a) is not an engine inequality of form (2.2): it is a lower bound on H by a wall, not a bound on a move. It does not meet Theorem C1, and it does not escape its conclusion: the toy has one scale, and Section 3.2 finds that its transport carries no gain in scale. Agreement, by a different path.
- **Rows 1481-1487.** Their verdict (B), no transfer, stands for the shortened proof too. The shortened proof changes how the lower bound is obtained (product formula for a Gram determinant in place of lattice slopes; [R] L121). It adds no object that a gauge theory has. Row 1487's sharpened trigger (R7), "a size bound proved independently of the integral structure", is untouched.
- **Row 1688, Proposition OBS and wish (Y4).** OBS ("every one-way inequality found holds for models of purity near zero") holds for everything in this file: NEC, EMPTY, NO-A and RATIO are true for any positive trace-class operator. Row 1688 wrote "No toy has the wished property (Y4)". Theorem TOY (a) is a one-way inequality in a toy whose proof uses the commutator and has a size (kappa). So it is a toy with the first form of (Y4). Against the replacement (Y4) of check 1692 it fails at once: clause 1 (it is not a statement about the Wilson law at beta_K on the box of side l L^K; it sits at the small end of the box size), and clause 4 (it holds for five-dimensional SU(2) verbatim, and for U(1) with a charged spectator). It is not an input to the purity bound.

### 4.3 What Phase 2 changes in Parts 2 and 3

Nothing is withdrawn. Two statements are weaker than I wrote them in the closed-folder phase, and one is stronger:
- "I chose the toy" has no claim to novelty: the record chose it before and set it aside for the reason of 3.2.
- 3.5 is a re-derivation of rows 1025, 1128 and 1390, not a find.
- The twin test on the MK precedent (2.5) is stronger than the record: the precedent that the record "recalled" as a non-abelian flow theorem is, by its authors' abstract, a theorem for U(1) too. The step at order-one coupling in the MK model is therefore carried by a fact that the twin shares (ARGUED: compactness of the group). Weak compact U(1) in four dimensions is a counterexample to any transport of that step to the true lattice law that does not read the group.

## 5. Result

**Verdicts.**
1. Part 1: done from both sources. The architecture is on file (row 1688); no tool of the shortened proof transfers (as rows 1481-1487 found for the first proof).
2. Part 2: Theorem TOY is PROVED by hand for the constant-mode model, with the abelian twin failing. Constants are explicit except delta (existence argument). Object: the transverse oscillators over the abelian valley. Inequality: the one-mode uncertainty bound. The toy itself is on file as an idea; the written proof is new.
3. Part 3: the analogue of the toy's carrying inequality does not exist at the crux couplings. Proved forms: Lemma NEC (the target forces n(E_1 - E_0) > 512, which the toy regime cannot meet; the regime statement is ARGUED), Proposition EMPTY (the transported proof has no rate and is blind to the group), Proposition NO-A (any comparison route must hold the total vacuum energy to 80.14/n). The second toy (MK) has an analogue, which is Tomboulis's comparison, closed on the record by row 1025.
4. Part 4: no piece is a new candidate. New as written text: Theorem TOY with constants; Proposition NO-A as one number; the abstract-level reading that the MK convergence theorems include U(1).

**What stays open.** (PUR-io), unchanged. The toy-first strategy needs a toy in which the purity bound holds at a large box on a weak-coupling trajectory and fails for the abelian twin. No such toy with a proof is known to me: the constant-mode toy sits at the small end; two dimensions and strong coupling do not separate the groups (row 1688); the MK model does not separate them either, except by a rate that I could not read.

**One step that the record lacks (proposal, not done here).** Obtain Müller and Schiemann, Lett. Math. Phys. 15 (1988) 289, by a route the rules allow, and read its rate of convergence. Decisive outcome: (a) the rate at weak coupling is a fixed drop per step only for non-abelian groups: then the paper holds a written, group-reading inequality for an exact renormalisation step at every coupling, in a model, and it is the toy this lane looked for; (b) the rate is the same for U(1): then the MK model is closed as a toy for this campaign, with the reason. Row 736 records these papers as not read.

**Not done, and limits.** No Lean. One guide computation (Section 2.3), which proves nothing. The papers of Lüscher, Simon, Ito, Müller and Schiemann, Tomboulis, Guth, Fröhlich and Spencer were not read in this session; what I say about them is from memory or from abstracts, as labelled. Author only; checked by no one. Phase 2 was a keyword search and a reading of RESULT parts, not a full reading of the files named.

## Credits

Levent Alpoge (the note, the original proof, with Claude). Luke Sernau, colleagues at Anthropic, and Claude (the shortened proof). Michael Rubinstein (the outline v1.5). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, on Balaban's method (the release, the Wilson transfer, the purity consumer in `Purity.lean`). M. Lüscher and B. Simon (the constant-mode model and the discrete-spectrum mechanism). K. R. Ito, V. F. Müller and J. Schiemann (Migdal-Kadanoff convergence), after A. A. Migdal and L. P. Kadanoff. E. T. Tomboulis; K. R. Ito and E. Seiler. The authors of rows 1025, 1128, 1380, 1390, 1481, 1482, 1487, 1520, 1647, 1686 and 1688 of this lane, whose results Part 4 quotes.

RESULT: Row 1697 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; one guide run under the numeric lock, no subagents). Part 1 done from Alpoge's note and Rubinstein's outline v1.5; architecture on file (row 1688), no tool transfers. Part 2: Theorem TOY PROVED by hand (constant-mode SU(2) model with valley cutoff R: fibre inequality H >= (1-theta)(-Laplacian/2) + sqrt(theta(D-1)/2) sum|x_i|, trace bound and purity floor uniform in R, threshold 457/625 for s >= s_0 with one existence constant; the abelian twin's purity is at most (e pi sqrt(s/2)/R)^D and fails). Part 3: the toy's inequality has no analogue at the crux couplings (Lemma NEC, Proposition EMPTY, Proposition NO-A: a comparison proof must hold the total vacuum energy to 80.14/n); the MK toy's analogue is Tomboulis's comparison, closed by row 1025. Part 4: nothing here is a new candidate for (PUR-io); new as text are the written toy proof, NO-A as a number, and the abstract-level fact that the Migdal-Kadanoff convergence theorems cover U(1). Open: (PUR-io) unchanged; no toy with a large-box, group-reading purity proof is known; proposed next step is to read the rate in Müller-Schiemann 1988.
