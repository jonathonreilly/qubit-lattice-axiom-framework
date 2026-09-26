# Independent check: repeated six-axis formation marks

This is a pre-source mathematical check of the specification in `INPUT.md`, not a review of primary author calculations. No new primary files were read. The result is a resource classification for the stipulated interface.

Write v_a in {±e1,±e2,±e3}, rho_a=(I+v_a·sigma)/2 and

\[
K_j(b\mid a)=\frac{1+jv_a\cdot v_b}{6},\qquad 0<|j|<1.
\]

All six inputs are independently selectable promises. Total variation is TV(p,q)=one half of the sum of absolute differences. Trace distance has the same one-half convention. The j=0 case is a control.

**Results.** A bare unknown qubit cannot produce two conditionally iid marks with this kernel for any nonzero j. Every two-mark protocol has worst-input-row TV error at least j²/18. This value is the exact optimum for |j|≤1/2, attained by a joint POVM that also matches both single-mark marginals exactly. A supplied, input-correlated qutrit ancilla is necessary and sufficient for unlimited iid marks with exact parent preservation. The qutrit stores the axis; the original parent supplies the sign in that axis. This makes the six joint code states orthogonal. One event with parent preservation needs only a supplied extra qubit copy, whereas the bare qubit cannot do it.

## 1. Two iid classical marks: obstruction and sharp approximation

Any adaptive protocol, including arbitrary disturbance, input-independent ancillary systems and recovery, has a 36-effect POVM {E_bc} on the initial qubit once its two classical outputs are retained. Its probabilities are affine in rho_a. The target is

\[
T_a(b,c)=K_j(b\mid a)K_j(c\mid a)
=\frac{1+jv_a\cdot(v_b+v_c)+j^2(v_a\cdot v_b)(v_a\cdot v_c)}{36}.
\tag{1}
\]

Mix the two inputs ±ei equally. Each such input mixture is I/2, but the target output mixtures are

\[
M_i(b,c)=\frac{1+j^2(e_i\cdot v_b)(e_i\cdot v_c)}{36}.
\tag{2}
\]

For i≠k the difference M_i−M_k has eight nonzero entries of magnitude j²/36: the four pairs with both outputs on axis i and the four with both on axis k. Thus TV(M_i,M_k)=j²/9. Any actual POVM has one common output distribution Qbar on I/2. If every input-row error is at most Delta, convexity gives TV(M_i,Qbar)≤Delta for each i. The triangle inequality proves

\[
\boxed{\inf_{\{E_{bc}\}}\max_a\operatorname{TV}(T_a,Q_a)
\ \geq\ \frac{j^2}{18}.}
\tag{3}
\]

This is an ensemble-consistency obstruction, so allowing a destructive measurement or an adaptive second event does not remove it.

For any |ell|≤1/2 define

\[
E_{bc}^{(\ell)}=\frac{I+\ell(v_b+v_c)\cdot\sigma}{36}.
\tag{4}
\]

These effects are positive because |v_b+v_c|≤2, and their sum is I because the six vectors sum to zero. Their Born probabilities are

\[
Q_a^{(\ell)}(b,c)=\frac{1+\ell v_a\cdot(v_b+v_c)}{36}.
\tag{5}
\]

For |j|≤1/2, take ell=j. Equation (1) differs from (5) in only four entries of each input row, all with absolute difference j²/36. Therefore

\[
\boxed{\inf_{\{E_{bc}\}}\max_a\operatorname{TV}(T_a,Q_a)
=\frac{j^2}{18}\quad (|j|\leq1/2).}
\tag{6}
\]

Summing (4) over c gives (I+j v_b·sigma)/6; summing over b gives the corresponding c effect. Hence this optimal approximation has both desired marginals exactly. The errors are in the conditional joint law. At j=1/2 its error is 1/72.

There is also an explicit approximation throughout |j|<1: set ell to j clipped to [−1/2,1/2]. Direct summation gives

\[
\max_a\operatorname{TV}(T_a,Q_a^{(\ell)})
=\frac{j^2+4(|j|-1/2)_+}{18}.
\tag{7}
\]

For completeness, putting d=j−ell, the absolute-difference sum before division by 72 is

\[
|j^2+2d|+|j^2-2d|+2j^2+16|d|.
\]

For the clipped ell and |j|≤1, j²≥2|d|, giving (7). For |j|>1/2 this is only an upper bound; the optimum between (3) and (7) is not classified here. These clipped marginals have parameter ell rather than j.

Matching both marginals is possible for every |j|<1 even without clipping: measure the single-mark POVM (I+j v_b·sigma)/6 and duplicate its classical output, c=b. The two marginals equal K_j, but the joint law is perfectly correlated. Its TV from the iid target is 1−sum_b K_j(b|a)²=(15−j²)/18. This witness is deliberately distinct from the useful small-j approximation.

The pair obstruction also survives heralding with an input-dependent positive success probability when error is measured conditionally on producing the pair. To see this, twirl the unnormalized successful effects over the proper octahedral rotation group, rotating both outcome labels with the input. The total successful effect becomes lambda_bar I. After division by lambda_bar>0 the successful effects form a POVM. Each conditional row is a success-weighted convex combination of relabeled original conditional rows, with the same covariant target (1), so its worst row TV cannot increase. Equation (3) therefore still applies. This observation does not turn survival-conditioned histories into the normalized unlimited histories considered below.

## 2. Two quantum-only newborns

If a mark b is converted into rho_b and its label discarded, one newborn has the marginal

\[
\omega_a=\sum_bK_j(b\mid a)\rho_b
=\frac{I+(j/3)v_a\cdot\sigma}{2}.
\tag{8}
\]

Two conditionally independent newborns would have state omega_a tensor omega_a. Put s=j/3. Equal mixing of inputs ±ei would produce

\[
R_i=\frac{I_4+s^2\sigma_i\otimes\sigma_i}{4},
\tag{9}
\]

which depends on i. Thus no quantum channel on the bare parent can produce these exact product states for nonzero j either. This is a difference in observable joint density operators, not a statement about an inaccessible classical decomposition. In fact, for i≠k, the eigenvalues of R_i−R_k are ±s²/2,0,0, so the same mixture argument gives a worst-input trace-distance error lower bound s²/4=j²/36 for this product-state target. No optimality claim for that quantum approximation is made.

If only the two individual newborn marginals are requested, a channel exists for every |j|<1: measure b with the single-mark POVM and prepare rho_b tensor rho_b. Both marginals are (8), but the siblings are correlated. The parent may be disturbed in this construction. Merely saying “two newborn qubits” does not specify a product joint state or nondisturbance.

## 3. Unlimited iid marks: exact ancillary dimension

Now supply an input-correlated ancillary state tau_a on a fixed d_A-dimensional system. The initial state is

\[
\Sigma_a=\rho_a\otimes\tau_a.
\tag{10}
\]

A pure specified parent marginal forces this product form even if one initially allows general joint states. All other ancillary resources are input-independent. “Unlimited iid” means that for every positive integer n the complete, normalized classical history has law K_j(·|a)^{tensor n}, from this same initial resource. There is no conditioning on non-abort or an asymptotically rare acceptance event.

For j≠0 all six rows of K_j are distinct: their mean vector is (j/3)v_a. For any pair a≠c, the iid histories become perfectly distinguishable as n tends to infinity, for example by the law of large numbers applied to their different mean vectors. But an n-event protocol is a measurement on the original Sigma_a. Therefore

\[
\operatorname{TV}\bigl(K_j(\cdot\mid a)^{\otimes n},
K_j(\cdot\mid c)^{\otimes n}\bigr)
\leq D_{\rm tr}(\Sigma_a,\Sigma_c)\leq1.
\tag{11}
\]

The first inequality follows directly by testing any classical history event: its pullback is an effect F with 0≤F≤I, and |tr[F(Sigma_a−Sigma_c)]| is at most the trace distance. Taking n to infinity forces trace distance one, hence mutually orthogonal supports for all six initial joint states. This necessity does not even require preservation of the parent. Six nonzero orthogonal states need joint dimension at least six, so 2d_A≥6 and

\[
d_A\geq3.
\tag{12}
\]

The support condition is informative. For states on different Pauli axes, tr(rho_a rho_c)=1/2, so

\[
0=\operatorname{tr}(\Sigma_a\Sigma_c)
=\tfrac12\operatorname{tr}(\tau_a\tau_c)
\]

forces the corresponding ancillary supports to be orthogonal. Opposite states on the same axis already have orthogonal parent supports and can share an ancillary state. At d_A=3 the three axis groups therefore occupy three mutually orthogonal one-dimensional subspaces.

This yields an attaining construction. Use a qutrit basis |1>,|2>,|3>, set tau_{±ei}=|i><i|, and define six orthogonal rank-one projectors

\[
\Pi_a=\rho_a\otimes|\operatorname{axis}(a)\rangle
\langle\operatorname{axis}(a)|,\qquad \sum_a\Pi_a=I_6.
\tag{13}
\]

The instrument with one Kraus operator per mark,

\[
M_b=\sum_a\sqrt{K_j(b\mid a)}\,\Pi_a,
\tag{14}
\]

obeys

\[
\sum_bM_b^\dagger M_b=I_6,\qquad
M_b\Pi_aM_b^\dagger=K_j(b\mid a)\Pi_a.
\tag{15}
\]

Repeated use gives exactly the iid product history probabilities and preserves both the parent and its qutrit register after every history. Thus **d_A=3 is necessary and sufficient** for nonzero j. The resource is a six-state orthogonal encoded record; the axis register is supplied correlated with preparation and cannot be generated freely from the unknown bare qubit.

For a quantitative information control, the single-mark Bhattacharyya affinity between two perpendicular-axis input rows is

\[
\beta_\perp(j)=\frac{\sqrt{1+j}+\sqrt{1-j}+1}{3}<1\quad(j\ne0).
\tag{16}
\]

For n iid marks, TV is at least 1−beta_perp(j)^n, since sum min(p,q)≤sum sqrt(pq). At j=1/2 this loose lower bound exceeds the initial cross-axis trace distance of a bare qubit, 1/sqrt(2), at n=54; it exceeds that of a parent plus a supplied identical copy, sqrt(3)/2, at n=88. These are illustrative non-sharp history bounds. The sharper ensemble-consistency argument already rules out the bare-qubit product law at n=2.

## 4. Distinct resource and scope cases

- **One event, exact parent preservation.** No correlated ancilla (d_A=1) is insufficient for nonzero j. In every instrument branch each Kraus operator must map every promised pure state to a scalar multiple of itself. The ±e3 eigenbasis makes it diagonal and the +e1 state forces the two diagonal entries to agree. Hence every Kraus operator is scalar and outcome probabilities are input-independent. Conversely, d_A=2 suffices: supply tau_a=rho_a as an extra copy, measure only that copy with the single-mark POVM and leave the parent alone. Thus the minimum here is two, not the unlimited-history value three. The supplied copy is an explicit resource, not cloning of the unknown parent. No minimum dimension for each fixed history length n≥2 is claimed.
- **Trivial kernel.** At j=0 one may generate independent uniform marks using input-independent randomness and leave the parent alone, with d_A=1. The dimension-three necessity requires nonzero j and all six independently selectable inputs. If the possible inputs are restricted to a known antipodal pair, those inputs are orthogonal and the requirement changes.
- **Optional orthogonal vacancy flag.** Equations (12)–(15) concern an occupied record only. If one additionally demands a vacancy state orthogonal to all occupied encoded states, total site dimension is at least seven; C|vac> direct sum (C² tensor C³) attains seven. If a fixed tensor factorization C² tensor C^{d_A} must include this vacancy, 2d_A≥7 requires d_A≥4. This is a separate architecture assumption, not a consequence of the word “vacancy.”
- **Excluded resources and interpretations.** A freely supplied preparation label, correlated apparatus outside tau_a, fresh supplied copies, or postselection on increasingly rare histories changes the resource question. Matching individual marginals does not establish iid histories, nor does a classical mark by itself identify a new physical qubit. These statements do not alter the supplied classical record dynamics.

## 5. Independent executable evidence and seal

Run from this directory with `python3 check.py`; the only generated output is `RESULTS.json`, with stdout also captured as `RUN.log`. The code imports no primary author module. Exact rational arithmetic checks eight positive/negative/zero j values for the two-mark mixture obstruction, the attained TV formula and both marginals. Small effect matrices also check positivity, completeness and Born probabilities. A separate exact symbolic four-dimensional check verifies the incompatible product-newborn mixtures. The qutrit construction is checked on all six inputs at three nonzero j values, including all 216 length-three histories per input: 3,888 history checks in total. Thirty-six one-event supplied-copy branches and an optional seven-dimensional vacancy direct sum are also checked.

All executable controls passed on Python 3.13.5, NumPy 2.4.4 and SymPy 1.14.0. The largest single-branch residual was 5.56e−17 and largest relative history residual 4.03e−15. Finite numerical histories are controls for (15); the equation itself proves the unlimited claim. No numerical search is used as an optimality or dimension proof.

`SEAL.json` records complete SHA-256 identities for this input receipt, report, independent code, results and execution log, together with the preceding independent report identity. The input source is the supplied specification. No new primary calculation was accessed before sealing. The open optimization outside |j|≤1/2, and the separate architecture/resource assumptions above, remain explicit limits.
