# J:derive:review-20260929-tensor-effective-stiffness:a1 -- attempt

Same-family (Claude Sonnet 5.5), unrefereed. Labels: PROVED = a full argument is written here (not a landed or referee-confirmed status); CHECKED = executed in `check.py` (exact rational/sympy arithmetic); ASSUMED = premise; READING = interpretation; CITED = classical result named, not re-proved here. Nothing here is a no-go claim.

## Plain-language summary

The landed note on current main proves "helicity-one weight is at least a quarter of the TT weight" only for stiffnesses written as a finite sum of squares of move amplitudes (a "finite positive Gram"). It says an arbitrary positive analytic symbol is not known to have such a form. This attempt settles both halves.

1. The quarter bound does not need the Gram form. Averaged over directions, helicity-one weight minus a quarter of the TT weight equals 9/4 times the stiffness measured on one specific tensor, the helicity-zero tensor n n^T - I/3. That is non-negative whenever the symbol is positive semidefinite, Gram or not.
2. The Gram form really is an extra restriction. An explicit positive, finite-range symbol with one gapped trace channel has no finite Gram of moves at all (it is built from Choi's classic positive-but-not-sum-of-squares form).

What is still open is the inertia: stiffness weights are not mode content unless the kinetic form is known (step 13).

## 1. Provenance (CHECKED, retrieval only -- not new)

- Read in full before any premise judgment: `docs/MINIMAL_AXIOMS_2026-06-29.md` (four axioms: Lattice, Qubit, Admissibility, Record; "Axioms and approved primitives are the complete supplied foundation"; dynamics, kinetic branch, tensor carrier, harmonic comparators are explicitly downstream) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (approved primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`; none supplies a tensor stiffness). Consequence: every object below (tensor slots, finite-range symbols, positivity of a harmonic form, isotropic inertia) is a supplied mathematical comparator, not an axiom consequence.
- Source branch `claude/toe-viability-probes-20260927`, frozen head `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36` fetched; all 31 task-named objects (and all 97 files of the PR 9363 map) hash-verified against SOURCE_MAP.json (`RECOVERY_STATUS.json`). Current main read at `3e1a2dd2531590dabf85bee8db56175ba9b96e90`.
- Corrected current-main source used as the baseline: `docs/TENSOR_HELICITY_RATIONAL_CERTIFICATES_AND_TRACE_ELIMINATION_BOUNDED_THEOREM_NOTE_2026-09-29.md` (quarter inequality for linear moments, LDL certificate, rank 10; trace elimination "for a finite positive Gram", with the explicit remark that an arbitrary analytic positive symbol "is not asserted to admit" that representation). Related runners: `scripts/tensor_symbol_rational_review_controls_2026_09_29.py`, `scripts/tensor_trace_schur_review_controls_2026_09_29.py`.
- Source quarter note (frozen branch) `docs/EVERY_GAUSS_LAW_COMPATIBLE_MOVE_...QUARTER...2026-09-29.md` grepped for gram / positive-semidefinite / perfect-square / helicity-zero: it states the average identity only on the scalar-compatible subspace (|xi|^2/3), not the square form below.
- Prior-art search: current-main docs/scripts for helicity content (only the 2026-09-29 note above is on tensor helicity); 229 open PRs by title/branch (none on this topic; title-level only). Related task `gravity-node-with-the-formation-kernels` and earlier `probes/work` attempts: nothing on tensor stiffness.

## 2. Setting and premises (ASSUMED)

- A: real momentum q in R^3 near 0 (lattice symbols are trigonometric polynomials in q; only the Taylor jet at 0 is used). Family space F = symmetric 3x3 tensors (6 components), Frobenius inner product. A "symbol" V(q) is a Hermitian (real part symmetric) matrix on F, analytic at 0, with V(q) positive semidefinite for real q.
- B: "local, finite positive Gram" means V(q) = R(q)^* R(q), R(q) an M x dim F matrix of analytic (for lattice moves: trigonometric polynomial) amplitudes, M finite.
- C: n = q/|q|. Weights of a quadratic symbol V(n) (homogeneous degree 2): H1(V)=<tr(Pi_H1(n)V(n))>, TT(V)=<tr(Pi_TT(n)V(n))>, <.> = normalised sphere integral, Pi_H1, Pi_TT the matrices of the quadratic forms H1(M,n)=2(|Mn|^2-f^2), TT(M,n)=tr M^2-2|Mn|^2+f^2-(trM-f)^2/2, f=n^T M n. For a Gram sum V=sum M_m M_m^T these are the sums of the weights of the moves. (Definitions of the weights are the main note's; step 5 validates them.)
- D (only for step 12): inertia is K = kappa * identity on traceless tensors (supplied comparator; not derived).
- Not assumed: Gram form, cubic or rotation symmetry (except where stated), any residual symmetry.

## 3. Where the Gram premise enters (PROVED + CHECKED)

Claim 3. If V=R^*R with R analytic, V(0)=diag(a^*a on one gapped direction, 0 elsewhere) (single gapped trace channel, as in the main note), then the leading Schur complement of the gapped channel is S2(q)=(PB)^*(PB), P=I-aa^*/(a^*a), B=the linear (first-moment) part of the other columns. Proof: R e_1=a+O(q); R e_j=B_j(q)+O(q^2) (since V_jj(0)=0 forces R(0)e_j=0); V_11=a^*a+O(q), V_1j=a^*B_j+O(q^2); S=V_22-V_21V_11^{-1}V_12 = B^*B-B^*aa^*B/(a^*a)+O(q^3). So S2 is a sum of squares of linear forms in q (real and imaginary parts of the complex linear forms give real squares). CHECKED 4.6 (three exact random trials including random O(q) trace corrections and O(q^2) terms).

Consequence: a symbol with a gapped trace channel and a leading effective stiffness S2 that is positive but NOT a sum of squares of linear forms has no finite Gram. This is the exact content of the extra premise: the old route needs "S2 is SOS in the biquadratic (q, tensor) sense".

## 4. Positivity alone gives a PSD quadratic effective stiffness (PROVED)

Let V be a symbol as in step 2A, N=ker V(0), G=range V(0)>0 (any dimension, constant). Block form relative to N+G.
(i) V_NN(0)=0 and V_NN(eps e)=eps V1(e)+O(eps^2) is PSD for both signs of eps, so V1=0: V_NN=O(q^2).
(ii) V_NG(0)=0, so V_NG=O(q).
(iii) Schur complement S=V_NN-V_NG V_GG^{-1}V_GN is PSD for every small real q; S(eps e)=eps^2 S2(e)+O(eps^3) with S2(e)=V_NN^{(2)}(e)-V_NG^{(1)}(e)V_GG(0)^{-1}V_GN^{(1)}(e) a homogeneous quadratic polynomial in e, PSD as a limit of PSD matrices.
No Gram, no finiteness of range, no locality was used. The slaved gapped components are O(q) relative to h_N and do not change the leading weights (READING). Order of operations matters: helicity must be measured on S2, not on V_NN^{(2)} (CHECKED 4.5: the two give different weights, 52/35 and 64/35 versus 12/5 and 12/5 in the example; both obey the quarter bound because both are PSD).

## 5. The weight formulas are the helicity projections (CHECKED 1.1)

H1(M,n) and TT(M,n) equal the squared Frobenius norms of the explicit helicity-one part (n w^T+w n^T, w the transverse part of Mn) and TT part (transverse-traceless part of P M P) for five rational unit directions times three rational tensors.

## 6. The perfect-square identity (CHECKED, exact and complete for the stated finite statement)

Coordinates u_a on F (a = xx,yy,zz,xy,xz,yz; off-diagonals shared by ij and ji). Pi_ab=(1/2) d^2/du_a du_b of (H1-TT/4). Y_a(n)=d/du_a of (n^T M n - tr M/3) (the covector of the helicity-zero tensor n n^T - I/3: diagonal entries n_i^2-1/3, off-diagonal 2 n_i n_j).

**Identity.** For all a,b,k,l: <Pi_ab n_k n_l> = (9/4) <Y_a Y_b n_k n_l>. Sphere averages by symbolic integration in spherical coordinates, all 324 index entries exact rational (CHECKED 2.1). Equivalent forms:
- for every linear first-moment M(n)=sum_k n_k M_k (18 coefficients): <H1>-<TT>/4 = (9/4) <(n^T M n - tr M/3)^2>;
- on the scalar-compatible family sym(n xi)+sym([n]xA) this is |xi|^2/3 (the main note's value, CHECKED 2.6);
- Q is the Gram matrix of cubic functions: positive semidefinite, rank 10 = dim of odd cubic functions on S^2 (spin 1 + spin 3), kernel 8 (CHECKED 2.2-2.4). PSD by characteristic-polynomial sign pattern, not LDL.
- Equality (the 1/4 is attained) for M=sym([n]x diag(1,-1,0)): <H1>=1/5, <TT>=4/5 (CHECKED 2.7).
Independent reproduction of the main certificate: rank 10, PSD over all 18 first-moment dimensions, plus cross-validation of my integration against the closed double-factorial moment formula on a random integer vector (CHECKED 2.5).

## 7. Extension to every positive quadratic symbol (PROVED from step 6; CHECKED 3.1, 4.3)

Let V(n)=sum_{k<=l} n_k n_l V_kl with V_kl real symmetric 6x6 (contravariant on the u-coordinates), V(n) PSD for every n. By step 6 and linearity in V (the pairing is sum Q_{ak,bl} V_{ab,kl}, and Q=(9/4) integral of (Y_a n_k)(Y_b n_l)):

  H1(V) - TT(V)/4 = (9/4) < Y(n)^T V(n) Y(n) > >= 0,

with equality iff V(n)Y(n)=0 for all n. Gram sums are the special case; no factorisation is used. CHECKED on a random indefinite symbol with 126 integer coefficients (3.1) and on the non-Gram Choi symbol (4.3: <H1>=52/35, <TT>=64/35, difference 36/35 = (9/4)<Y^T W Y>). Complex Hermitian V: the helicity matrices and Y are real, so only the real symmetric part, which is PSD, enters.

Combined with step 4: for any analytic positive symbol with any constant gapped sector, the effective quadratic stiffness on the gapless sector obeys the quarter bound. The 'additional factorization needed by the partner argument' is therefore not needed for the angular inequality.

## 8. Positive, finite range, gapped trace, no finite Gram (CHECKED + PROVED)

- Choi's biquadratic form f(x,y)=sum x_i^2 y_i^2 - 2 sum x_i x_{i+1} y_i y_{i+1} + sum x_i^2 y_{i+1}^2 (indices mod 3; CITED Choi 1975, form recorded here from memory and re-verified).
- PSD (CHECKED 4.1): the 3x3 matrix N(x)=Hess_y f/2 has all principal minors non-negative; the determinant x1^4x2^2+x1^2x3^4+x2^4x3^2-3x1^2x2^2x3^2 is the three-term AM-GM expression, certified by u^3+v^3+w^3-3uvw=(u+v+w)*sum(u-v)^2/2 with u^3,v^3,w^3 the three positive monomials.
- Not a sum of squares of bilinear forms, any number of squares (CHECKED 4.2): any bilinear ell=x^T A y in a sum of squares equal to f vanishes at 7 zeros of f (three (e_i,e_{i-1}) pairs and four sign pairs (s,s)); these force A=diag(a1,a2,a3), a1+a2+a3=0; squares of such forms contain no x1^2 y2^2 term while f has coefficient 1.
- Tensor embedding and lattice symbol (CHECKED 4.4): amplitudes y=(u_xy,u_xz,u_yz), x=q; F=(trace amplitude s, u). V(q)=[[1,b^T],[b,bb^T+N(sin q)]], b=(sin q1,sin q2,sin q3): trigonometric-polynomial entries (finite range), V=L diag(1,N(sin q))L^T so PSD, V(0)=diag(1,0,0,0), exact Schur complement N(sin q), leading O(q^2) part N(q).
- Non-Gram (PROVED from steps 3 and 8): a finite Gram V=R^*R, even with analytic (non-polynomial) R and complex amplitudes, would give S2=(PB)^*(PB) (step 3), a sum of squares of real bilinear forms in (q,u); but S2=N(q) is not (4.2). So no finite positive Gram of move amplitudes exists. READING: positivity (even with finite range and a single gapped channel) does not imply the Gram representation the old trace-elimination step assumes.
- Classical context (CITED, not re-proved): d=1 positive trigonometric matrix polynomials do factor (matrix Fejer-Riesz); biquadratic PSD = SOS when min(d,k)<=2 (Calderon, Choi). The gap opens at (d,k)=(3,3), the tensor case has k>=3.

## 9. Gram = PSD for isotropic leading symbols on traceless tensors (CHECKED)

SO(3)-covariant quadratic symbols on traceless tensors are a1 tr(Y^2)|q|^2+a2 q^T Y^2 q; at q=z they are diagonal in the helicity basis with eigenvalues (lam0,lam1,lam2)=(a1+2a2/3, a1+a2/2, a1), hence 4*lam1=lam2+3*lam0 (locality fixes lam1; CHECKED 5.2-5.4). Spin channels of 5 x 3 = 1+2+3 (Casimir projectors on 27-dim tensor space, exact) have rays (a1,a2)=(0,3/5),(2/3,-1),(1/3,2/5). An invariant Gram can be averaged to an invariant Gram (Haar), multiplicity-free, so Gram cone = cone of these rays = {a1>=0, a1+2a2/3>=0} = PSD cone (CHECKED 5.5). Weights: H1=2*lam1, TT=2*lam2, H1-TT/4=(3/2)*lam0=(9/4)<Y^T V Y> (CHECKED 5.6, consistent with step 7). So the counterexample of step 8 must break full rotation covariance (it does).

## 10. Not new (stated to bound the claim)

The quarter inequality for linear moments, the rank-10 certificate, the trace-elimination projector and the explicit remark that Gram is a premise (main note above); Choi's example, Fejer-Riesz, Calderon (classical); the saturating 8-dimensional family and the min ratio 1/4 (main note and source quarter note C, F).

## 11. Exact-gauge dichotomy without Gram (PROVED from step 7)

If a positive quadratic symbol annihilates all helicity-one tensors sym(n x e), e perp n (exact transverse linearised-diffeomorphism invariance at leading order), then the H1 weight vanishes, so by step 7 TT(V)<=0, and since the TT weight tr(Pi_TT V(n)) is non-negative and polynomial on S^2, it vanishes identically; also V(n)Y(n)=0. So: positivity plus exact transverse gauge invariance leaves no O(q^2) TT stiffness. This reproduces the source's case (i) (omega_TT=O(q^2)) for the leading quadratic symbol with neither a Gram form nor a split into storage assignments. Isotropic instance: lam1=0 forces lam2=-3*lam0, hence lam0=lam2=0 (CHECKED 6.1). READING: helicity-one weight that is nonzero is by definition non-gauge, so the 'partner' content in step 12 lives in the physical quotient only when those tensors are not exact gauge; deciding that is model input (step 13).

## 12. Dispersion consequence under supplied isotropic inertia (PROVED, conditional on D)

Take K=kappa*identity on traceless tensors and S2 as in step 4. At direction n the normal modes are eigenvectors e_i of S2(n) with omega_i^2=lam_i/kappa. Then H1 weight = sum lam_i ||P_H1 e_i||^2 >= 0 and likewise TT. If TT(V)>0 then H1(V)>=TT(V)/4>0 (step 7), the real-analytic weight tr(Pi_H1 S2(n)) is not identically zero, so it is positive on an open dense set of directions; at each such n some mode with omega^2>0 (linear in |q|) has non-zero helicity-one overlap. This holds for every positive S2, with no Gram form. Isotropic instance: omega_1^2=(3*omega_0^2+omega_TT^2)/4 exactly (CHECKED 6.2), so omega_1>=omega_TT/2.

## 13. First unresolved step

Step 12 uses K proportional to the identity. For a general positive kinetic form (non-isotropic, q-dependent, or the O(q^2) Gauss-law-compatible kinetic range of the swapped assignment) the modes are generalised eigenvectors of (K,S2) and stiffness weight no longer implies mode content; the sources' P / H / H2 lemmas address one such K and are not re-derived here. Also unresolved:
- which helicity-one directions are exact gauge in a concrete lattice model (physical quotient; step 11 gives only the dichotomy at the quadratic level);
- higher order than the leading quadratic jet, and gapped sectors with q-dependent range;
- Gram classification for cubic-only symmetric symbols (only the isotropic case is classified; d or k <=2 cited);
- referee confirmation; this worker did not commit, run `run_probe.py` or `claim.py`.

## 14. Falsifiers and attack routes tried

- Not claimed: a pointwise (fixed-direction) version of the identity; only the direction average was checked. The identity needs V homogeneous of degree 2 in q (the weights are averaged against n_k n_l).
- A positive symbol with TT stiffness but zero H1 weight: excluded by step 7 for the quadratic jet; no route tried here removes the quadratic-jet or gapped-sector hypotheses.
- A failed identity entry, a non-PSD Q, a Choi minor with a negative coefficient, or a Gram trial with S2 != (PB)^T(PB) would falsify the corresponding check.
