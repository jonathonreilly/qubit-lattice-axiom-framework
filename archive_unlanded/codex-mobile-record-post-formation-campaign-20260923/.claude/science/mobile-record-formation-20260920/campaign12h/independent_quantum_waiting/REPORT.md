# Independent two-parent quantum waiting-law check

**Result.** No quantum experiment on the stipulated initial two qubits can reproduce the classical exponential waiting law on all 36 promised inputs. At any strictly positive deadline, the target already violates linearity in the initial density operator. The supplied jump instrument is valid and matches every initial marked rate, but gives a singlet/triplet mixture of exponentials. Its survival exceeds the classical target for perpendicular or antiparallel parents.

This report was derived and sealed before reading any primary waiting-law files or calculations. It concerns the supplied two-parent interface, with no preparation label or correlated ancillary resource. It is not an audit or a claim about other dynamics.

## 1. Ensemble consistency rules out the complete target law

Let u=v_a dot v_c in {−1,0,1}. The six menu vectors sum to zero and obey sum_b v_b v_b^T=2I_3, so the supplied hazard is

\[
H(a,c)=\epsilon(6+2j^2u),\qquad
S_{\rm cl}(t\mid a,c)=q e^{-xu},\qquad
q=e^{-6\epsilon t},\quad x=2\epsilon j^2t.
\tag{1}
\]

Any quantum experiment, however adaptive or disturbing, represents the event “no first event by t” by an effect E_t on the initial two qubits:

\[
S_{\rm phys}(t\mid a,c)
=\operatorname{tr}[E_t(\rho_a\otimes\rho_c)],\qquad 0\leq E_t\leq I_4.
\tag{2}
\]

Input-independent ancillas and intermediate outcomes are absorbed into this effect. Thus the survival probability is affine in the initial density operator. No assumption about a Markov generator or parent preservation is required for (2).

Fix c=+e3. An equal mixture of a=±e3 and an equal mixture of a=±e1 both give the identical physical input (I_2/2) tensor rho_c. Their target survival probabilities instead average to

\[
\tfrac12\{S_{\rm cl}(t\mid +e_3,c)+S_{\rm cl}(t\mid -e_3,c)\}
=q\cosh x,
\qquad
\tfrac12\{S_{\rm cl}(t\mid +e_1,c)+S_{\rm cl}(t\mid -e_1,c)\}=q.
\tag{3}
\]

For epsilon>0, j≠0 and t>0 the difference q(cosh x−1) is positive. Hence even the binary survival observation at this single deadline cannot have all the target rows; the complete waiting-time law is therefore impossible as well.

Define the worst-input deadline error

\[
\Delta_t(E)=\max_{a,c}|\operatorname{tr}[E(\rho_a\otimes\rho_c)]-S_{\rm cl}(t\mid a,c)|.
\]

This is the worst-row TV error for the two-valued observation {event by t, no event by t}. The triangle inequality applied to (3) gives the universal bound

\[
\boxed{\Delta_t(E)\geq\frac{q}{2}(\cosh x-1)>0.}
\tag{4}
\]

Its small-time expansion is epsilon² j⁴ t²+O(t³) at fixed parameters. For any full timestamp distribution, TV dominates the discrepancy on the event {T>t}. Choosing t=1/(6epsilon) gives the explicit lower bound

\[
\max_{a,c}\operatorname{TV}(\mathcal L_{a,c}(T),\operatorname{Exp}(H(a,c)))
\ \geq\ \frac{e^{-1}}2\left[\cosh\!\left(\frac{j^2}{3}\right)-1\right].
\tag{5}
\]

Equation (5) is a lower bound on the complete timestamp problem, not a claimed optimum for it.

## 2. Sharp error at a single chosen deadline

For completeness, the binary problem in (4) can be solved exactly without requiring a single protocol to optimize all deadlines. Let

\[
T=\sum_{i=1}^3\sigma_i\otimes\sigma_i.
\]

Average any candidate E under simultaneous proper octahedral rotations of both qubits. The 36 promised inputs and their target probabilities are permuted, so convexity cannot increase Delta_t. Averaging its Pauli expansion removes the one-qubit vector terms and makes the two-qubit coefficient matrix scalar. The averaged effect therefore has form

\[
E=\alpha I_4+\beta T,
\quad S_E(u)=\alpha+\beta u,
\quad 0\leq\alpha+\beta\leq1,
\quad 0\leq\alpha-3\beta\leq1.
\tag{6}
\]

The last two constraints are its triplet and singlet eigenvalue bounds. In addition to (4), positivity implies S_E(−1)=2S_E(0)−S_E(1)≤2S_E(0), giving Delta_t≥q(e^x−2)/3 whenever that expression is positive. These bounds are attained, yielding

\[
\boxed{
\inf_{0\leq E\leq I}\Delta_t(E)=q
\begin{cases}
(\cosh x-1)/2,&0\leq x\leq\log3,\\
(e^x-2)/3,&x\geq\log3.
\end{cases}}
\tag{7}
\]

For the first interval choose alpha=q(1+cosh x)/2 and beta=−q sinh x. Its three output errors are equal in magnitude, with the u=0 error opposite in sign to the endpoint errors. Writing z=e^x and r=3/j²>3, q=z^{−r}. The triplet eigenvalue is q(2−z+3/z)/4≥0 for z≤3. The singlet eigenvalue is q(2+7z−5/z)/4≤1: it suffices to replace q by z^{−3}, and the remaining inequality follows from

\[
4z^4-7z^2-2z+5=(z-1)^2(4z^2+8z+5)\geq0.
\]

The triplet eigenvalue is no larger than the singlet one. For the second interval take alpha=q(z+1)/3 and beta=−alpha. The triplet eigenvalue is zero, while the singlet eigenvalue 4q(z+1)/3≤16/81 for z≥3. The u=−1 and u=0 errors have magnitude q(z−2)/3, and the remaining error q/z is no larger. This proves attainability and all effect constraints. At x=log 3 the two constructions agree.

Equation (7) optimizes a binary observation at a chosen deadline. It does not assert the optimal TV error of a full timestamp distribution. The lower bounds obtained from it still apply to every such experiment.

## 3. Exact law of the supplied quantum jump instrument

Each marked rate effect

\[
F_b=\epsilon(I+jv_b\cdot\sigma)\otimes(I+jv_b\cdot\sigma)
\]

is strictly positive for |j|<1. Choosing jump operators sqrt(F_b) gives a valid time-homogeneous jump instrument with no Hamiltonian and total rate operator

\[
R=\sum_bF_b=\epsilon(6I_4+2j^2T).
\tag{8}
\]

The identity T=2 Swap−I_4 gives triplet eigenvalue 1 and singlet eigenvalue −3. Denote the associated projectors by P_tr and P_si. Their rates and the initial product-state weights are

\[
r_{\rm tr}=\epsilon(6+2j^2),\quad
r_{\rm si}=\epsilon(6-6j^2),\quad
w_{\rm tr}=\frac{3+u}{4},\quad
w_{\rm si}=\frac{1-u}{4}.
\tag{9}
\]

Both rates are strictly positive under the stated hypotheses. From K_0(t)=exp(−tR/2), the exact survival is

\[
\boxed{S_{\rm jump}(t\mid a,c)
=\operatorname{tr}[e^{-tR}(\rho_a\otimes\rho_c)]
=\frac{3+u}{4}e^{-r_{\rm tr}t}
 +\frac{1-u}{4}e^{-r_{\rm si}t}.}
\tag{10}
\]

The initial marked rates agree individually with the classical model:

\[
\operatorname{tr}[F_b(\rho_a\otimes\rho_c)]
=\epsilon(1+jv_b\cdot v_a)(1+jv_b\cdot v_c).
\tag{11}
\]

Consequently −S'_jump(0)=w_tr r_tr+w_si r_si=H(a,c), including the correct initial total rate and the marked odds conditional on an event in an infinitesimal initial interval. This does not identify the mark distribution integrated over the whole waiting time. The equality of initial rates does not replace (10) by exp(−tH). In general tr(exp(−tR)rho) differs from exp(−t tr(Rrho)).

Convexity of the exponential gives S_jump≥S_cl. It is strict at t>0 for u=0 or u=−1 because both weights are nonzero and the two rates differ. It is equality for u=1, where the product input lies in the triplet sector. The first nonzero difference is

\[
S_{\rm jump}-S_{\rm cl}
=2\epsilon^2j^4(1-u)(3+u)t^2+O(t^3).
\tag{12}
\]

Conditioning on no event reweights the two sectors. Its hazard is

\[
h_{\rm jump}(t)
=\frac{w_{\rm tr}r_{\rm tr}e^{-r_{\rm tr}t}
       +w_{\rm si}r_{\rm si}e^{-r_{\rm si}t}}
      {w_{\rm tr}e^{-r_{\rm tr}t}+w_{\rm si}e^{-r_{\rm si}t}},
\]

whose derivative is minus the conditional variance of the two rates. Thus it decreases when both sectors have weight, approaching r_si. There is no fixed classical preparation-dependent hazard throughout the waiting interval. Nevertheless the first event occurs almost surely because both rates are positive.

At epsilon=1, j=1/2 and t=1/6, a direct 4 by 4 matrix exponential gives:

| Parent relation u | Classical survival | Jump survival | Absolute gap |
|---|---:|---:|---:|
| −1, antiparallel | 0.399849654345 | 0.405415988924 | 0.005566334579 |
| 0, perpendicular | 0.367879441171 | 0.371940707015 | 0.004061265844 |
| 1, identical | 0.338465425107 | 0.338465425107 | 0 |

For example, the perpendicular quantum value is (3/4)e^{−13/12}+(1/4)e^{−3/4}, while the classical value is e^{−1}. The incompatible ensemble target averages differ by 0.00127809855435, so every physical experiment has worst-input deadline error at least 0.000639049277176. Here that lower bound is the sharp value (7). The supplied jump instrument is not asserted to minimize that approximation error.

## 4. Scope, controls and source seal

The obstruction uses all independently selectable promised inputs; it allows disturbance and arbitrary adaptive experiments. Classical preparation labels or input-correlated resources would change the premise. The binary no-event observation is unconditional, so discarding runs cannot redefine the complete target waiting law. At t=0 there is no discrepancy; at j=0 the input-independent exponential of rate 6epsilon is implementable and the jump instrument has exactly that law. The stated model excludes |j|=1; at that boundary the jump singlet rate vanishes, changing its long-time behavior.

`check.py` is independent and imports no author module. Exact symbolic checks cover all 36 initial total rates, all 216 marked rates, all 36 singlet/triplet weights and all 36 second-order differences. A direct symbolic matrix exponential checks all 36 survival rows at j=1/2, epsilon=1, t=1/6, rather than only evaluating the claimed mixture formula. Exact mixed input equality and three finite-time parameter controls, including a negative j, are also checked. Independent vertex enumeration of the symmetric binary-effect linear program checks (7) at seven points, on both sides of and at x=log 3. These numerical controls supplement the proofs above; they do not replace them.

Run `python3 check.py > RUN.log` from this directory. All checks passed using Python 3.13.5, NumPy 2.4.4 and SymPy 1.14.0. Full results are in `RESULTS.json`, identical to `RUN.log`. `SEAL.json` records the complete SHA-256 identities of the supplied-input receipt, this report, code, results and execution log. No primary waiting-law source or result was accessed before sealing, and no file outside the assigned output directory was changed.
