# A variance-calibrated clock transfer and its joint rotor limit

Author derivation in progress, 2026-09-16. The exact Fourier matching is for a supplied coupling and external time step. It selects no native dynamics and proves no phase. The basic fixed-N logarithmic matching and spatial inverse-logarithmic matching already appear in current main's COMPACT_DETERMINANT_CURRENTS_SIGNED_SECTORS_AND_FINITE_CYCLIC_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-14.md PartIII. The new target here is uniform matching along arbitrary joint clock/time paths.

## 1. Exact clock kernel and a crossover that must be priced

For c>0 define p_c(k)=exp(-c k²)/Z(c), k in Z, and v(c)=E_c k². On an N-state clock, N>=3, let X translate the angle by2pi/N and put

    Q_(c,N)=sum_k p_c(k) X^k.

The character r has eigenvalue

    lambda_r(c,N)=E_c cos(2pi r k/N)
      = [sum_m exp(-pi²(m+r/N)²/c)]
        /[sum_m exp(-pi²m²/c)].                       (1)

Poisson summation proves the second formula. It is strictly positive; the first proves it is at most1. Q is consequently a positive self-adjoint contraction. It is precisely the normalized sampled Villain temporal kernel with beta_tau=N²c/(2pi²).

For the naive rotor time scaling beta_tau=1/(g²delta), write J=delta g²N²/2, so c=pi²/J. For fixed r and fixed J in(0,infinity), delta=2J/(g²N²) and N->infinity give

    -delta^-1 log lambda_r -> (g²/2)r² D(J),
    D(J)=(2pi²/J)v(pi²/J)=1-2J v(J).                 (2)

The second identity follows by logarithmically differentiating
Z(J)=sqrt(pi/J)Z(pi²/J). For every finite J, 0<D(J)<1: positivity follows from the first expression and the strict upper bound from the second. Moreover D(J)->0 as J->0 and D(J)->1 as J->infinity. At small J the first expression is asymptotic to(4pi²/J)exp(-pi²/J); at large J the second is1-4J exp(-J)+smaller terms. A joint limit at finite J therefore changes the low-mode kinetic coefficient. These conclusions concern this actual sampled kernel, not every clock discretization.

The expansion used for(2) has an O(N^-2) energy remainder at fixed J, since all integer-Gaussian moments are finite. Uniformity over J approaching an endpoint needs an additional argument; the result below supplies a different calibration that avoids that requirement.

## 2. Existence of an exact variance calibration

v'(c)=-Var_c(k²)<0. Termwise differentiation is justified on every compact c interval. Also v(c)->0 as c->infinity, and v(c)->infinity as c->0, the latter by the Poisson identity and exponentially small dual moments. Thus for every delta,g>0 and integer N>=3 there is exactly one c=c(delta,N,g)>0 such that

    v(c)=delta g² N²/(4pi²).                         (3)

This is a mathematical matching of a supplied target kinetic coefficient. It is not a fit to observations and does not derive g from the framework. At small target variance, exp(-c) is asymptotic to v/2 and recovers the known logarithmic clock scaling. At large target variance, c is asymptotic to1/(2v) and beta_tau is asymptotic to1/(g²delta).

## 3. Uniform fourth-moment bound

We need a bound valid even in the crossover. Let mu4(c)=E_c k4. The following deliberately loose constant suffices:

    mu4(c)<=224[v(c)+v(c)²], all c>0.                (4)

For c>=1, divide the positive sums for mu4 and v and retain k=1 in the denominator. Since k²-1>=3(k-1),

    mu4/v <=sum_(k>=1) k4 exp[-(k²-1)]
      <=sum_(k>=1)k4 r^(k-1)<3, r=exp(-3)<1/16.

The last series equals(1+11r+11r²+r³)/(1-r)^5, and its value at1/16 is less than3.

For0<c<=1, put d=pi²/c>9. The dual variance obeys
v(d)<=2 sum_(k>=1) k² exp(-d k²)<=3 exp(-d).
Here use k²-1>=3(k-1) and the geometric second-moment sum; exp(-3d)<1/16. The differentiated Poisson identity gives

    v(c)=[1-2d v(d)]/(2c)>=1/(4c),

because6d exp(-d)<=54 exp(-9)<1/2. Also Z(c)>=sqrt(pi/c) by Poisson summation. On each interval[k-1,k],
k4 exp(-c k²)<=(x+1)^4 exp(-c x²). Using(x+1)^4<=8(x4+1) and the two Gaussian integrals gives

    2 sum_(k>=1)k4 exp(-c k²)
      <=6sqrt(pi)c^(-5/2)+8sqrt(pi)c^(-1/2).

After division by Z(c), mu4<=6c^-2+8<=14c^-2<=224v(c)². Combining the two ranges proves(4). No finite sampling supplies this bound.

## 4. Quantitative one-link energy matching

Let h=2pi r/N, and use calibration(3). For the centered representative |r|<=N/2 put z=h²v/2=delta g²r²/2. The elementary cosine remainder implies

    0<=lambda_r-1+z<=h4 mu4/24.

If z<=1/2, set u=1-lambda_r in[0,z]. Since
0<=-log(1-u)-u<=u²/[2(1-u)]<=u²,

    |-delta^-1 log lambda_r-(g²/2)r²|
      <= h4 mu4/(24delta)+z²/delta
      <=400 r4 [g²/N²+delta g4].                    (5)

The last constant follows from(4), pi²<10, and direct substitution of(3): the two coefficients before enlargement are224pi²/6 and224/24+1/4. The r=0 eigenvalue is exactly1 and both sides vanish. At fixed finite r, (5) tends to zero along EVERY sequence delta->0,N->infinity, with g fixed. No condition on delta N² is imposed. This does not approximate all high clock modes uniformly.

A direct one-step bound avoids the logarithm and is useful for products:

    |lambda_r-1+delta g²r²/2|
      <=(224pi²/6)delta g²r4/N²
         +(224/24)delta²g4r4.                       (6)

It needs no small-z restriction; the right side may simply become uninformative for high modes.

## 5. Full finite-volume transfer: proof plan to complete

For a fixed finite spatial graph use one calibrated Q per link. Let y=delta/(2g²), and use the existing normalized spatial Villain B_y(curl theta). Its uniform expansion is1-delta g^-2(1-cos)+O(delta²). The actual positive symmetric transfer is B_delta^(1/2) Q_delta^(tensor E) B_delta^(1/2), not its quadratic approximation. It commutes with the finite-clock gauge projection.

Embed the centered clock Fourier basis into l2(Z^E). Finite trigonometric polynomials are eventually contained in this image. Their one-step consistency should be

    ||(T_delta,N-I+delta H)f||
       <=C_f[delta²+delta/N²],
    H=(g²/2)sum E²+g^-2 sum[1-cos curl theta].

The spatial expansion has an operator-norm remainder on each finite graph. Multiplication of a finite Fourier polynomial by the leading cosine potential is another such polynomial; this prevents an unpriced high-mode commutator in the consistency proof. A bounded gauge-compatible matter multiplier can be included by an additional symmetric sandwich after a finite-volume scalar shift.

Extend the finite transfer by zero on the orthogonal complement of the embedded clock space. Then A_delta,N=(I-T_delta,N)/delta is positive and bounded. If A_delta,N f->Hf on the finite-Fourier core, the identity

    ||(A_delta,N+1)^-1(H+1)f-f||<=||(H-A_delta,N)f||

and density of(H+1)core give strong resolvent convergence. Uniform polynomial approximation in(1+x)^-1 yields strong heat-semigroup convergence. The scalar difference between lambda^n and exp[-n(1-lambda)] on[0,1] tends uniformly to zero, so the actual transfer products converge as well. Verify the bound, time rounding and the mod-N physical projector passage before promoting this plan to a theorem.

No thermodynamic phase, actual ground-state convergence uniform in volume, fixed finite-N rotor law, real-time physical clock selection, or native axiom result follows from this finite-volume bridge.
