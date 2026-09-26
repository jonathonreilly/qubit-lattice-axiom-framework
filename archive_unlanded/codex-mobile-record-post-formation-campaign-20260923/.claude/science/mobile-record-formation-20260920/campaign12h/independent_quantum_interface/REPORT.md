# Six-axis qubit measurement and formation interface

Independent pre-source derivation from `INPUT.md` and ordinary completely positive quantum operations. The conclusions apply to the specified physical-qubit interface; they do not classify the underlying classical record dynamics or any physics/TOE construction.

Let `v_a` be the six signed Cartesian unit vectors, `rho_a=(I+v_a.sigma)/2`, `D=p+q+4r`, and `P=p+q`, with `p,q,r>0`. The required classical kernel is `K(b|a)=p/D`, `q/D`, or `r/D` for equal, opposite, or orthogonal vectors, respectively. All statements concern a single unknown input qubit per parent, with no accessible preparation label, extra input copy, or input-correlated ancilla. Input-independent ancillas, arbitrary instruments, and outcome-dependent recovery are allowed.

The exact answers are:

\[
\begin{array}{ll}
\text{Classical six-outcome POVM:}& p+q=2r\quad\text{if and only if};\\[2mm]
\text{Optimal worst-row TV error:}&
\displaystyle \Delta_* =\left|\frac{p+q}{D}-\frac13\right|
=\frac{2|p+q-2r|}{3D};\\[2mm]
\text{Optimal average parent fidelity, when feasible:}&
\displaystyle \overline F_* =\frac{2+\sqrt{1-\eta^2}}3,
\quad\eta=\frac{p-q}{p+q};\\[2mm]
\text{Newborn marginal only:}&
\displaystyle -\frac13\le\frac{p-q}{D}\le1\quad\text{if and only if}.
\end{array}
\tag{1}
\]

The last condition is weaker than classical-outcome realizability and, under the stipulated positive parameters, is equivalent to `q<=2(p+r)`. Fidelity here means pure-state overlap, averaged uniformly over the six inputs and over all six formation outcomes, without discarding recovery failures. It does not average over an additional no-occurrence branch of a rare-event protocol. Its optimum is attained by the square-root instrument.

Postselection does **not** enlarge the one-parent classical-kernel family. For a nontrivial realizable kernel, its occurrence rate must be input independent. For any fixed number `n` of independently prepared parents with product odds, the same feasibility condition is necessary, and the nontrivial kernel forces the occurrence rate to be a constant multiple of the product-odds normalizer. Positive quantum rate instruments attain that requirement.

## 1. Exact measurement and optimal approximation

Every axis gives a different decomposition of the same state:

\[
\frac{\rho_{+i}+\rho_{-i}}2=I/2.
\tag{2}
\]

For a fixed outcome `b`, averaging the target probabilities on its own antipodal input pair gives `P/(2D)`, while averaging them on an orthogonal antipodal pair gives `r/D`. The effect `E_b` must give the same probability on both preparations of `I/2`. Hence `P=2r` is necessary. When it holds, the unique effects are

\[
E_b=\frac16(I+\eta v_b\cdot\sigma),
\qquad \eta=\frac{p-q}{P},\qquad |\eta|<1.
\tag{3}
\]

They are positive, sum to `I`, and give the specified probabilities. Uniqueness follows because the six input density matrices span the Hermitian qubit operators. Randomizing the promised pure preparations to test (2) does not introduce an additional resource: absent a preparation label, both mixtures are the same physical input state.

For the minimax approximation, consider any six-effect POVM, and combine the two outputs on axis `i` into `A_i=E_(+i)+E_(-i)`. The target probability of that combined output on either input `+i` or `-i` is `P/D`. If every row's TV error is at most `Delta`, averaging these two input inequalities gives

\[
\left|\tfrac12\operatorname{tr}A_i-P/D\right|\le\Delta.
\]

Since `sum_i A_i=I`, the mean of the three quantities `tr A_i/2` is `1/3`. Therefore `Delta>=|P/D-1/3|`. This lower bound uses only operational linearity and normalization; allowing an asymmetric POVM cannot evade it.

For every positive `p,q,r`, use the valid POVM (3) with `eta=(p-q)/P`, whether or not `P=2r`. Its probabilities on the same-axis pair are `p/(3P)` and `q/(3P)`, and all four orthogonal probabilities are `1/6`. Within each of the two groups, the errors have one sign. Their total TV error is exactly `|P/D-1/3|` on every row. This proves the optimum in (1), not just a symmetric-ansatz optimum.

## 2. Sharp parent-preservation bound, including recovery

Write all effective Kraus operators, after recovery and after tracing unused output systems, as `L_bj`, so that

\[
\sum_j L_{bj}^\dagger L_{bj}=E_b,
\qquad
\overline F=\frac16\sum_a\operatorname{tr}\!left[
\rho_a\sum_{b,j}L_{bj}\rho_aL_{bj}^\dagger\right].
\]

Any deterministic recovery conditioned on `b` or on retained auxiliary information is included in this description. The six inputs obey the exact second-moment identity

\[
\frac16\sum_a\rho_a^T\otimes\rho_a
=\frac{I_4+|\Omega\rangle\langle\Omega|}{6},
\qquad |\Omega\rangle=|00\rangle+|11\rangle.
\]

It follows that

\[
\overline F=\frac{2+\sum_{b,j}|\operatorname{tr}L_{bj}|^2}{6}.
\tag{4}
\]

For each fixed effect with eigenvalues `lambda_1,lambda_2`, diagonalize that effect and collect the Kraus diagonal entries into two vectors. Their squared norms are at most `lambda_1` and `lambda_2`; the triangle and Cauchy inequalities give

\[
\sum_j|\operatorname{tr}L_{bj}|^2
\le(\sqrt{\lambda_1}+\sqrt{\lambda_2})^2
=(\operatorname{tr}\sqrt{E_b})^2.
\tag{5}
\]

The single Kraus operator `L_b=sqrt(E_b)` attains equality. For (3), the eigenvalues are `(1+eta)/6` and `(1-eta)/6`. Substitution into (4) gives precisely `F_*` in (1). Thus unrestricted recovery cannot improve the result.

The attaining nonselective parent channel is depolarizing with Bloch contraction `(1+2 sqrt(1-eta^2))/3`, so it gives this same preservation fidelity on every pure input. It can simultaneously emit a classical outcome `b` and prepare a newborn qubit in `rho_b`: append that state to the square-root instrument's output. Nontrivial `eta` nevertheless disturbs the parent. Perfect preservation occurs only for `eta=0`, which within the exactly realizable family means `p=q=r`. The limiting value at `|eta|=1` is `2/3`; strict positive `p,q` keep that boundary excluded.

For the positive witness `(p,q,r)=(3,1,2)`, `eta=1/2` and the optimal average fidelity is `(4+sqrt(3))/6`, approximately `0.9553418012614795`. An input-independent random outcome, `(1,1,1)`, permits parent fidelity one. These statements concern the average over all declared outcomes. A different metric that discards unsuccessful recovery runs is not this optimization.

## 3. A newborn marginal is a different operational requirement

If no classical `b` is available and only the newborn density matrix is specified, the requested output on input `a` is

\[
\tau_a=\sum_b K(b|a)\rho_b
=\frac12(I+s\,v_a\cdot\sigma),\qquad s=\frac{p-q}{D}.
\tag{6}
\]

A channel producing one output on every use is then uniquely the depolarizing map `Phi_s(rho)=s rho+(1-s)I/2`. Its unnormalized Choi matrix is `s|Omega><Omega|+(1-s)I_4/2`; the eigenvalues are `(1+3s)/2` once and `(1-s)/2` three times. Hence complete positivity is equivalent to `-1/3<=s<=1`. A constructive realization is the Pauli channel with probabilities `(1+3s)/4` for identity and `(1-s)/4` for each of the three Pauli conjugations.

For `(2,2,1)`, the classical kernel is impossible and its optimal TV error is `1/6`, yet the newborn marginal is the constant `I/2`. For `(10,1,1)`, the marginal has `s=3/5` and is a valid quantum channel despite classical-kernel TV error `2/5`. Reversing `p,q` gives `s=-3/5`, which is not a channel. The boundary example `(1,4,1)` has `s=-1/3` and is completely positive.

Matching the marginal does not establish that the stipulated classical label or its preparation-dependent ensemble decomposition exists, even if someone calls that label hidden. A genuine record of `b` would itself require the POVM already tested. Conversely, the preservation bound (4)-(5) applies when that classical outcome is required; it must not be imposed as the optimum for a different, label-free parent/newborn broadcasting problem. Perfectly preserving all six pure parent states while giving a nonconstant newborn marginal is still impossible: purity makes each joint output a product with the parent, and a Stinespring inner-product comparison on the connected graph of nonorthogonal inputs forces the other output to be input independent. No optimization of imperfect label-free broadcasting is claimed here.

## 4. The supplied two-parent occurrence rate

Let `W_ba=6 K(b|a)` and define

\[
x=\frac{3(p-q)}D,\qquad y=\frac{3(p+q-2r)}D.
\]

On the six axes,

\[
W_{ba}=1+x\,v_b\cdot v_a
          +y[(v_b\cdot v_a)^2-1/3].
\]

Using the antipodal pairs and their orthogonal-axis sums gives the exact total rate

\[
\lambda_{ac}=\epsilon\sum_b W_{ba}W_{bc}
=\epsilon\{6+2x^2v_a\cdot v_c
                  +2y^2[(v_a\cdot v_c)^2-1/3]\}.
\tag{7}
\]

An observable quantum occurrence rate must have the form `tr(R rho_a tensor rho_c)` with a positive rate operator `R`. Fix the second parent at `+i`. Averaging the first parent over `+i,-i` gives rate `epsilon(6+4y^2/3)`, while averaging it over an orthogonal pair gives `epsilon(6-2y^2/3)`. Both preparations have density matrix `(I/2) tensor rho_(+i)`. Their rate difference is `2 epsilon y^2`. Thus for `epsilon>0`, operational linearity requires `y=0`, exactly `p+q=2r`.

This necessary condition is sufficient. Now `x=eta`, and the unique two-parent total rate operator is

\[
R=\epsilon\left[6I_4+2\eta^2\sum_{i=1}^3\sigma_i\otimes\sigma_i\right].
\tag{8}
\]

Its eigenvalues are `epsilon(6+2eta^2)` on the triplet subspace and `6epsilon(1-eta^2)` on the singlet, so it is positive. More strongly, each classical outcome rate has the positive effect

\[
R_b=\epsilon(I+\eta v_b\cdot\sigma)\otimes(I+\eta v_b\cdot\sigma),
\qquad\sum_bR_b=R.
\tag{9}
\]

For sufficiently small `dt`, Kraus operators `sqrt(dt R_b)` and the no-occurrence operator `sqrt(I-dt R)` form an ordinary instrument. A record of `b` and a newborn `rho_b` can be appended. The normalization of the conditional birth odds is supplied by conditioning on the observed occurrence, not by a nonlinear trace-preserving channel. This is a positive rate-interface construction; it does not preserve unknown parents unchanged or establish the full classical waiting-time process after quantum backaction. At `epsilon=0` the rate test is trivially zero for every menu and supplies no formation interface.

## 5. What allowing postselection changes

First consider one parent and allow an unknown-input-dependent nonzero occurrence rate. Let the positive outcome-rate effects be `R_b`, their sum `R`, and

\[
\lambda_a=\operatorname{tr}(R\rho_a)=A+u\cdot v_a,
\qquad A=\operatorname{tr}R/2>0.
\]

The required unnormalized probabilities are `tr(R_b rho_a)=lambda_a K(b|a)`. For `b=+i` and `b=-i`, compare the antipodal input-pair sum on axis `i` with that on an orthogonal axis. Linearity of each `R_b` yields

\[
(P-2r)A+(p-q)u_i=0,\qquad
(P-2r)A-(p-q)u_i=0.
\tag{10}
\]

Adding these equations forces `P=2r`. Thus postselection cannot restore any otherwise unrealizable one-parent kernel. If `p!=q`, subtraction forces all `u_i=0`: the occurrence rate is constant and `R_b=lambda E_b`. If `p=q`, feasibility also requires `p=q=r`; this uniform-outcome exception allows any positive `R`, with `R_b=R/6`. A zero instrument is excluded as a realization of formation. Allowing zero probability on some promised inputs does not evade the equations for a nonzero instrument; those rows would also lack defined conditional odds.

There is a useful exact extension to any fixed finite `n` of independently prepared parents. Put

\[
U_b(a_1,\ldots,a_n)=\prod_{j=1}^n W_{b a_j},\qquad
Z=\sum_bU_b,\qquad P(b\mid\text{occurrence},a_1,\ldots,a_n)=U_b/Z.
\]

Write `h=lambda/Z`. Fix all but one parent to particular input states. Partial expectation of the outcome-rate effects gives positive effects on the remaining qubit. Divide outcome `b`'s effect by the fixed positive scalar `prod_(j!=i)W_(b a_j)`. Their probabilities become `h(a_i,rest) W_(b a_i)`, and their total rate is `6h`, since the columns of `W` sum to six. They are therefore an instance of the one-parent postselection problem.

It follows that a nonzero instrument requires `p+q=2r`. For the nontrivial case `p!=q`, the same argument makes `h` constant in each input coordinate (a zero slice has `h=0` throughout), hence constant on the entire product input set. Consequently

\[
\boxed{\lambda(a_1,\ldots,a_n)=c\,Z(a_1,\ldots,a_n)},\qquad
R_b=c\bigotimes_{j=1}^n(I+\eta v_b\cdot\sigma),\quad c>0.
\tag{11}
\]

The effects are positive and give a construction. They are also unique for the chosen scale because the product six-state preparations span all Hermitian `n`-qubit operators. The constant scale may be supplied separately for each specified `n`; it is not derived as a universal rate across different input sizes. In the uniform-menu exception, the odds are `1/6` and any positive `n`-qubit rate operator is allowed, with `R_b=R/6`.

Thus postselection can implement normalized multiparent product odds for the Born-realizable nontrivial menu, but its observable rate is fixed up to scale. In particular the stipulated `epsilon Z` rate has exactly the required form. A constant occurrence probability would fail for nontrivial `n>=2` product odds because `Z` is not constant. This is distinct from rescuing a forbidden one-parent kernel, which postselection cannot do. Positivity matters: signed formal rates are not operational alternatives.

## Checks, limitations and pre-source identity

`check.py` reads no primary campaign source. It checks:

- Thirteen menus using exact rational probabilities and the attaining POVM. A floating global LP with positivity deliberately relaxed supplies a matching lower bound in each case; it is not mislabeled as a full POVM SDP.
- The exact six-state second-moment identity; five square-root instruments; positive semidefinite dual certificates for the Kraus-trace optimization; and sixty independently generated conditional channels. The largest numerical effect residual is below `3.4e-16`, and the smallest dual-certificate eigenvalue is above `-2.2e-16` at tolerance `1e-12`.
- Seven newborn/rate cases, including the completely positive boundary `s=-1/3`; exact two-parent intensity identities; and the two-qubit rate spectra.
- Exact one- and two-parent linearity-constraint ranks and floating nonnegative feasibility checks for postselection. The nontrivial feasible menu has a one-dimensional space of `h`; the uniform menu has the expected `4^n` linear space. The invalid symmetric menu `(2,2,1)` admits signed null vectors but no nonnegative nonzero rate, providing a useful positivity discriminator.
- A three-parent positive construction on all 216 preparation tuples and all six individual outcome rates, 1,296 comparisons in total.

All checks pass. The universal results are the proofs above, not extrapolations from these finite parameter samples. The numerical checks have declared tolerances; exact arithmetic is identified separately. No approximate multiparent optimization, full growing-process quantum realization, or joint label-free broadcasting optimum is claimed.

These restrictions rely on the physical input being exactly the supplied unknown qubit(s). Access to a classical preparation label, input-correlated auxiliary system, or extra copies changes the interface. In particular, the multiparent theorem requires all independently selectable preparation tuples; a promise of identical multiple copies is a different input family. Strict positivity is used when dividing by fixed-neighbor weights; zero-weight boundary kernels are outside that classification. No such resource or boundary extension is silently supplied here.

The only mathematical input source for this continuation is the task specification recorded in `INPUT.md`; the proofs import no primary author result. No primary file with `QUANTUM` or `quantum` in its name, no unpublished primary calculation, and no quantum-interface publication source was read. No primary source, Git state, PR, audit, editable prompt, model or reasoning effort was changed, and no work was delegated. Outputs remain inside the assigned independent directory. `python3 check.py > RUN.log` reproduces the checks; `SEAL.json` records complete source/output hashes and the pre-source boundary.
