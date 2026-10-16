# Independent quotient/history precheck v1

Reviewer: `/root/force_energy_bridge_check`. Lead author remains `/root`.
This derivation was written before reading the author's new calibration_error notes or code. The only new scientific input is the task's abstract model: native accumulated cycles are reported modulo M=2^32; each supplied continuous segment has an arbitrary real offset; each observation has an arbitrary integer cycle ambiguity; real errors are separately bounded. No raw observations, network sources, calibration data, author implementation, or other checker's new derivation were read. Existing campaign science is not being audited or modified.

## 1. Exact quotient imposed by the proposed model

Let there be J observations in S known, nonempty, disjoint continuous segments. Let B be their J-by-S incidence matrix: B_js=1 if observation j is in segment s, otherwise 0. Each row has exactly one 1. Let Phi_j(h) be the supplied candidate physical phase response, expressed in cycles. The abstract observation law is

```
q_j = [Phi_j(h) + (B b)_j + n_j + epsilon_j]_M,
M=2^32, b in R^S arbitrary, n in Z^J arbitrary.
```

For any representatives q in R^J, the law is equivalent to

```
q - Phi(h) - epsilon in B R^S + Z^J.                 (Q1)
```

Indeed a representative has an additional M k with k integer, and n-Mk ranges over all Z^J because M is an integer and n was already arbitrary. Conversely any integer in (Q1) is a permissible n. Thus the large native modulus does not retain integer-cycle history in this model. It reduces to a unit-cycle torus before the segment offsets are eliminated. This deduction depends on the stated independent arbitrary integer n_j; restrictions on slips, their size, sign, continuity, count, or correlations would change the model and must be supplied explicitly.

Pick one anchor a_s in each segment and let K have one row e_j^T-e_a_s^T for every nonanchor observation j. Then

```
K B = 0, rank K = J-S = d, K Z^J = Z^d, ker_R K = im_R B.
```

The exact observable quotient is

```
R^J/(Z^J+B R^S)  isomorphic to  R^d/Z^d = T^d,
[q] maps to [K q]_1.                                (Q2)
```

Surjectivity of K on integer lattices matters. If K(q-q') is integral, choose n with zero anchor components and the indicated integer nonanchor differences. Then q-q'-n is constant on each segment and equals B b. This proves that (Q2) loses exactly the declared ambiguities, rather than adding a new one. A singleton segment contributes no observable coordinate.

Consequently every continuous invariant factors through the within-segment differences modulo one cycle. There is no canonical continuous real lift of those circular differences. Real-valued periodic functions such as cosine are legitimate continuous invariants; the statement is not that every real-valued continuous observable is constant. The statement about **linear** observables is stricter: an ordinary real linear form w^T q is invariant under every integer history only if w=0. Applying n=e_j proves this immediately.

If the actual stored q values contain only integer cycles, Kq is integral and the quotient datum is zero. With zero error allowed, h=0, b=0, n=q gives a compatible zero-field explanation. This is a conditional consequence of this model and data type, not a claim about any actual instrument record, which has not been opened. Fractional cycles can retain nontrivial torus data; arbitrary integer n does not erase fractional differences within a segment.

## 2. Circular linear contrasts, projected counts, and noninteger weights

For a specified output period P>0, the circular linear form

```
w^T q mod P
```

descends to (Q2) exactly when

```
B^T w = 0 and w/P in Z^J.                          (Q3)
```

The continuous real offsets require exact annihilation, not a modulo condition: b is arbitrary. The individual integer histories require each w_j/P integral. Modulo-M representatives impose no additional restriction once (Q3) holds. Checking only M w_j/P integral is insufficient, because arbitrary unit-cycle n_j is a stronger ambiguity than the native wrap.

For the unit circle, invariant characters are exp(2 pi i w^T q) with w integer and B^T w=0. Equivalently w=K^T ell for ell in Z^d. Trigonometric polynomials in these characters approximate every continuous invariant on the compact quotient. Noninteger-looking weights are not categorically forbidden: they are valid if the output period/lattice is transformed consistently. For a nonzero integer ell, the exact scalar image lattice is

```
ell^T Z^d = g_ell Z,
g_ell = gcd(|ell_1|,...,|ell_d|).
```

Thus ell^T Kq has natural period g_ell. Using period one remains invariant but can fold away information when ell is not primitive. A common real scale a times a primitive integer vector has period |a|. It need not have period one.

More generally for a real contrast v in R^d, the ambiguity group is Lambda_v=v^T Z^d. If its nonzero coefficients are rationally commensurate, Lambda_v is a discrete cyclic subgroup a Z and a circular observable survives. If at least two coefficients have irrational ratio, Lambda_v is dense in R. A continuous scalar function invariant under this group is constant; the algebraic quotient R/Lambda_v is not a useful Hausdorff observation circle. A Euclidean projection that discards this lattice arithmetic can manufacture a nonexistent real residual.

If normalized adjacent counts are y_i=(q_(i+1)-q_i)/T_i within supplied segments, let D_T be that incidence/duration matrix. A linear combination l^T y has phase weights w=D_T^T l. Unit-cycle invariance requires w integer as well as segment-offset annihilation. The latter is automatic for within-segment differences; the former is not automatic for arbitrary durations or regression/projection weights. Appropriate period rescaling or an explicitly transformed lattice can restore a valid observation. A full-rank real change of coordinates z=T Kq is also valid if its lattice is T Z^d, even when T is noninteger. An integer unimodular T is the special case preserving the unit lattice. A rank-reducing real projection may have dense image lattice.

Two exact failure witnesses are useful:

* With q=(0,1/4), w=(-1/2,1/2), the period-one value is 1/8. The allowed integer history q'=(0,5/4) gives 5/8. Native modulus M is even, so merely checking the native wrap would miss this failure. The correct scalar period is 1/2, under which these agree.
* Let y=3/4, the true response be A h=h, and N(h)=h^2. Its quotient minimum is dist(3/4,Z)^2=1/16, attained mathematically at h=-1/4. If one changes coordinates by T=1/2, then z=3/8 and G'=1/4, but falsely keeps the unit lattice, one obtains (3/8)^2/(1/4)=9/16. That claimed lower bound is nine times the energy of an explicitly compatible field. With the correct lattice (1/2)Z, the value is again 1/16.

## 3. Real resets and general real nuisance directions

A known arbitrary real reset simply creates another segment boundary. Formula (Q2) then applies to the refined segmentation and loses one dimension for every additional independent segment offset. No real contrast crossing such a boundary can be assumed invariant merely because an integer-slip correction was applied.

If independent arbitrary real resets at every observation boundary are allowed, the nuisance span is all R^J. All continuous invariants are constant and h=0 can explain any data through the resets (assuming zero error is admissible). A positive field-energy requirement is then unavailable. This conclusion assumes a history family closed under those arbitrary resets. A model allowing exactly one reset at one unknown location is a union of alternatives, not automatically the group generated by all reset steps; it must be treated as that union rather than silently enlarged or reduced.

For an arbitrary supplied real nuisance matrix C, the continuous characters are integer w satisfying C^T w=0. Taking an ordinary Euclidean nullspace is not sufficient. For example C=(1,sqrt(2))^T has a one-dimensional real left nullspace but no nonzero integer character. Its flow on T^2 is dense, so every continuous invariant is constant. The real-null vector (sqrt(2),-1) has dense integer ambiguity image. This is a topology/arithmetic obstruction, not a failure that can be repaired by selecting a scalar state.

## 4. Scalar energy lower bound that survives the quotient

Let H be a real Hilbert energy space with N(h)=||h||_H^2. If a physical energy is to be quoted, its conversion E_phys=kappa N must be supplied with kappa>0; otherwise this derivation bounds N only. One may instead use a supplied inequality E_phys>=kappa N. No value of kappa, physical upper energy budget, initial state, or real noise magnitude is selected here.

It is sufficient that the relevant contrast A h=K Phi(h) extend to bounded linear functionals on H. The individual raw phase rows need not be assumed bounded when only finite contrasts are defined. Write the finite contrast Gram G=A A*, which is positive semidefinite; require positive definiteness only where its inverse is used.

For nonzero ell in Z^d, put L_ell(h)=ell^T A h, g=||L_ell||^2=ell^T G ell, P=g_ell, and

```
y=Kq, delta=dist(ell^T y, P Z),
e_ell >= sup_(epsilon in E) |ell^T K epsilon|.       (Q4)
```

The actual error set E is supplied separately. For independent bounds |epsilon_j|<=sigma_j, a valid projected bound is sum_j |(K^T ell)_j| sigma_j. Correlations may tighten that number but cannot be ignored or invented. Any compatible h satisfies

```
max(0,delta-e_ell) <= |L_ell(h)| <= sqrt(g) ||h||,
N(h) >= max(0,delta-e_ell)^2/g,                      (Q5)
E_phys >= kappa max(0,delta-e_ell)^2/g.
```

Proof: for some integer k in the image lattice, ell^T y-Pk=L_ell(h)+ell^T Kepsilon. Taking the minimum distance to PZ and the triangle inequality gives the first bound, and Riesz/Cauchy-Schwarz gives the second. This is valid for any justified upper bound e_ell, even if conservative. If the only scalar information retained is this circular datum and the error projection can fill [-e_ell,e_ell], the scalar bound is sharp: take the nearest lift and the opposing error, then the Riesz minimizer. That is a mathematical attainability statement, not a physical choice of the actual field or error.

If g=0, a datum with delta>e_ell is incompatible with the supplied model; otherwise the inequality gives no positive energy bound. One must not divide by zero. If no quantitative physical error budget is supplied, (Q5) is a conditional formula, not a numerical physical constraint. It is not legitimate to set the actual error to zero merely to obtain a stronger bound.

For a general real v, the same inequality can use delta=dist(v^T y, closure(Lambda_v)), its actual image lattice/closure, and g=v^T Gv. When Lambda_v is dense, delta=0, so this scalar reduction gives only the trivial lower bound. Using dist(v^T y,Z) in that case has no justification.

## 5. Vector Gram/lattice minimum

Let C_err=K E be the supplied projected error set. The exact compatible residuals are

```
r=y-z-e, z in Z^d, e in C_err, r in range(A).        (Q6)
```

For a positive-definite Gram, A is onto R^d and the least mathematical Hilbert norm at fixed r is r^T G^(-1) r, attained by A*G^(-1)r. Therefore every compatible field obeys

```
N(h) >= inf_(z in Z^d,e in C_err)
          (y-z-e)^T G^(-1)(y-z-e).                  (Q7)
```

For semidefinite G, replace the inverse by G^+ **and retain** r in range(G). Without the range condition, a pseudoinverse can assign a finite value to impossible data. Example: G=diag(1,0), y=(1/4,1/10), zero error. No integer lift has second coordinate zero, so the datum is incompatible; the unconstrained pseudoinverse expression 1/16 would conceal that fact. With y=(1/4,0), the compatible minimum is 1/16.

If the error set is nonempty compact and G is SPD, the minimum is attained: finite objective bounds bound r, compact errors then bound z, and only finitely many integer z remain. This establishes an exact mathematical minimum, not computational tractability in arbitrary dimension. The zero-noise version is a closest-lattice-vector problem in the G^(-1) metric. It is periodic under y->y+m and invariant under a unimodular basis change. An arbitrary invertible change T is also equivalent only if y, G, the error set and the lattice are all transformed together.

For a finite raw-phase Gram F that is SPD, eliminating arbitrary real segment offsets before or after the lattice search is equivalent. The continuous minimization identity is

```
F^(-1)-F^(-1)B(B^T F^(-1)B)^(-1)B^T F^(-1)
  = K^T(K F K^T)^(-1)K.                             (Q8)
```

The nullspace and rank are as in section 1. Surjectivity K Z^J=Z^d then proves that minimizing over the original integer lifts and real offsets is exactly (Q7), not merely an approximation. The scalar lower bounds (Q5) can be weaker than this joint bound but cannot exceed the true compatible minimum when their error and lattice constraints are correct.

## 6. Planned independent controls and scope boundaries

I will implement exact rational modulo/offset/history invariance and normal-form reconstruction; the two noninteger-projection failure witnesses; a Pell-sequence demonstration of arbitrarily small nonzero irrational ambiguity increments; an SPD two-dimensional closest-lattice/box-error fixture with a justified finite enumeration region; integer-lift and unimodular-coordinate invariance; the continuous-offset Schur identity; compatible-field checks of scalar bounds; zero-response and PSD range-compatibility examples; and the real-reset and integer-only-data degeneracies. Synthetic error radii in those controls are mathematical test inputs, not estimates or choices for physical noise.

The algebraic observation quotient does not identify a receiver count with a sky phase, supply an oscillator or clock model, determine a propagation/trajectory map, calibrate an absolute scale, or validate a scalar interpretation. Those are separate physical imports. No assertion about actual receiver resets, phase fractions, noise, empirical residuals, scalar detection, or a TOE follows from this precheck. Any author-source comparison will be written only after this derivation and its independent controls are frozen, and will be labeled post-exposure.
