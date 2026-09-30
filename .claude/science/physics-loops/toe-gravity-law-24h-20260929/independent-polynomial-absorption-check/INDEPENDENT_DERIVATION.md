# Reconstruction before reading the source extension

This derivation was frozen before opening FAST_ONE_HOLE_ABSORPTION.md or any root polynomial-extension proof. Formula exposure is exactly recorded in PRE.md; this is an independent derivation with disclosed targets, not a blind prediction. The scope is the supplied bounded-generator hypotheses, to be checked against the actual frozen sector afterward.

## 1. Spectral bands supply bounded commutators

Let Q>=1 have integer spectrum, E_n its spectral projections, and A=-i delta H-kappa G/2. Suppose H is bounded, ||H||<=M, H has Q bandwidth2, and G is bounded diagonal in Q. On a finite torus these statements are on the complete physical rotor Hilbert space of the selected sector, not a box-truncated electric carrier.

Define H_d=sum_n E_(n+d) H E_n for d=-2,-1,0,1,2, omitting nonexistent output eigenvalues. For fixed d the output spaces are orthogonal, so

    ||H_d psi||² = sum_n ||E_(n+d) H E_n psi||²
                 <= ||H||² sum_n ||E_n psi||².

Thus ||H_d||<=M without a matrix row-sum premise. The finite band sum is H. On the finite-field core, then by its bounded extension,

    ad_Q^r(A) = -i delta sum_(d=-2)^2 d^r H_d,       r>=1,
    ||ad_Q^r(A)|| <= 2 delta M (1+2^r)
                  <= 5 delta M 2^r = h_r.                 (A)

The diagonal G contributes zero at every positive commutator order. The proposed constant is safe and not sharp. This argument requires actual bandwidth in total absolute electric field, not just spatial support. Two elementary link shifts imply that bandwidth even when both hit the same link or cross E=0; the absolute-field value changes by at most two.

## 2. Domain preservation with the original generator

The finite-field core is invariant under A by finite Q bandwidth. Its closure in ||Q^p psi|| is D(Q^p); spectral cutoffs of the input prove this, and Q>=1 makes this a complete norm equivalent to the usual graph norm. On the core, repeated Q A=A Q+[Q,A] gives

    Q^p A psi = A Q^p psi
       + sum_(r=1)^p binom(p,r) ad_Q^r(A) Q^(p-r) psi.     (B)

By (A) and ||Q^(p-r)psi||<=||Q^p psi||, the right side is bounded by a constant times ||Q^p psi||. Approximate any psi in D(Q^p) by finite-field inputs. A psi_n converges in Hilbert norm, while (B) makes Q^p A psi_n Cauchy. Closedness of Q^p proves A psi lies in D(Q^p), and (B) extends there. Thus A is bounded on this graph-norm Banach space.

Exponentiating that same operator in the graph norm preserves D(Q^p). The graph-norm exponential agrees with exp(tA) in the Hilbert space because the embedding is continuous and both are the same power series. No transition is removed, and no finite electric-box generator is substituted. The apparently nondecaying preliminary graph bound is used only for domain justification; the sharper decay estimate comes next.

For psi in D(Q^p), differentiation and variation of constants are now justified and give the exact identity

    Q^p S(t)psi = S(t)Q^p psi
       + sum_(r=1)^p binom(p,r) integral_0^t
           S(t-s) ad_Q^r(A) Q^(p-r) S(s)psi ds.            (C)

This is a closed-domain proof at each finite volume, with the subsequent estimates uniform in volume when the stated M,C0,gamma are uniform. It does not itself construct an infinite-volume sector representation.

## 3. Direct weighted recurrence and its solution

Assume ||S(t)||<=C0 exp(-gamma t), gamma>0. Necessarily C0>=1. Define R_0(t)=1 and, recursively,

    R_p(t)=1+C0 sum_(r=1)^p binom(p,r) h_r
                          integral_0^t R_(p-r)(s) ds.      (D)

Induction in (C), using the lower-order bound on psi and monotonicity of powers of Q, proves

    ||Q^p S(t)psi|| <= C0 exp(-gamma t) R_p(t)||Q^p psi||. (E)

The exponential generating function R(z,t)=sum_p R_p(t) z^p/p! is a formal power series; no assumption of exponential-field integrability of psi enters. Since every R_p(0)=1, equations (A),(D) give

    partial_t R = 5 C0 delta M (exp(2z)-1) R,
    R(z,0)=exp(z),
    R(z,t)=exp[z+x(exp(2z)-1)],    x=5 C0 delta M t.        (F)

Let T_p(x)=sum_(k=0)^p S(p,k)x^k be the Touchard polynomial, with T_0=1 and S(p,k) the Stirling numbers of the second kind. The standard finite coefficient identity follows directly by expanding exp[x(exp(w)-1)]; it need not be imported as a probabilistic law. From (F),

    P_p(t)=2^p T_p(x),
    R_p(t)=sum_(r=0)^p binom(p,r)P_r(t).                   (G)

Here P_0=1, P_p(0)=0 for p>0, and its differentiated generating function yields exactly the proposed P recurrence. Explicit checks, with the same x, are

    R_0=1,
    R_1=1+2x,
    R_2=1+8x+4x²,
    R_3=1+26x+36x²+8x³.

The only use of an exponential here is formal coefficient algebra in z, not a norm on exp(aQ)psi. For every fixed integer p the proof uses only the single finite moment ||Q^p psi||.

## 4. The original marked output

Let J psi=(j_m psi)_m be the direct-sum map for actual marks, so J†J=G and ||J||<=sqrt(12). For a coherent edge, j_m is its unnormalized coherent sign sum; signs are not split into extra observed marks. The output Q_out acts on physical electric fields in each mark summand. A birth changes one link by one, hence J has rectangular Q_out/Q_in bandwidth1. Decompose J=sum_(d=-1)^1 J_d by the two spectral resolutions. The same orthogonality proof gives ||J_d||<=sqrt(12).

On a band and an input Q eigenvalue n>=1 with n+d>=1,

    Q_out^p J_d Q_in^-p = J_d g_d(Q_in),
    g_d(n)=((n+d)/n)^p <=2^p.

Zero bands at nonexistent output eigenvalues are omitted. This also proves, by closing on finite-field inputs, that J maps D(Q_in^p) into D(Q_out^p). Therefore

    ||Q_out^p J Q_in^-p|| <= 3 sqrt(12) 2^p.              (H)

Again the proposed constant is conservative. Squaring (H), applying (E), and using the actual loss-rate convention in A gives

    kappa sum_m integral_0^infinity ||Q_out^p j_m S(t)psi||² dt
      <= 108 kappa 4^p C0² ||Q^p psi||²
           * integral_0^infinity exp(-2gamma t)R_p(t)² dt. (I)

This is the total 2p-th electric-field weight of the first original marked output in this no-event problem. All within-mark field/charge coherence is retained. It is not a bound on arbitrary later microscopic record words or on an independently changed secular instrument.

The integral is finite. Writing R_p(t)=sum_(k=0)^p c_k t^k gives the exact finite expression

    sum_(k,l=0)^p c_k c_l (k+l)!/(2gamma)^(k+l+1).

The time variable is the one for S(t)=exp[t(-i delta H-kappa G/2)]; if it is called microscopic fast time elsewhere, the same change of variables must be made in the jump intensity. No extra epsilon factor may be inserted in (I).

## 5. Preliminary finding and remaining source checks

The disclosed polynomial formulas and constants are mathematically consistent under the stated bounded-band generator and uniform-decay hypotheses. There is a complete domain argument using only D(Q^p), so an exponential-field input premise is unnecessary for this particular weighted absorption conclusion. The independent proof above does not establish those sector/decay hypotheses; the frozen actual source must still be read. It also does not address arbitrary global B occupation, multiple holes, repeated microscopic injections, or the volume-uniform original local-output limit from bare Omega.
