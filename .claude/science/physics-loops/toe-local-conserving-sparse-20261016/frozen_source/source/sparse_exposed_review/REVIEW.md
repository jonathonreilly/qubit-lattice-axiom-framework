# Exposed mathematical review of the sparse conserving compiler

**Disposition: qualified support for the stated fixed-q nominal laboratory resource bound.** I found no load-bearing defect in the selected charge blocks, the full-space spectator controls, the clean-ancilla determinant correction, the elementary counts, or the conversion to a physical-path bound `G <= K_q L^4`. The count has an explicit construction; it is not inferred from a small selected subspace alone. The effective interface establishes a terminating finite-error certificate search under the specified computable-input oracles. It does not establish polynomial classical runtime, preparation time, autonomous timing, or a compiler for general interacting old Hamiltonians. The inherited energy/readiness and timing qualifications below remain necessary.

This is a source-exposed, same-model analytical check, not blind replication, retained audit, or complete revalidation of every imported result. Root owns acceptance. No scientific executable was run or replayed by this reviewer. The only new execution captured here verifies source identities, historical receipts, and text extraction.

## 1. Identity, exposure and coverage

The reviewed candidate is `local_conserving_sparse_compiler_candidate/DERIVATION.md`, 30201 bytes, SHA256 `6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b`. Its actual final seal filename is `FREEZE.json`, 3916 bytes, SHA256 `1fd6b69f78b2b9e270e1dc4655ef9c6da9c6d4290a3e2867ebfac42fc23ac0c9`. All ten sections were read completely. Every one of the 21 frozen members, plus that seal, was verified and copied under `author_source/`; the exact path map is `SOURCE_MANIFEST.json`.

The local-control parent copied by the author is SHA256 `c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60`. I reviewed that complete source immediately before this task. The prior review and seal remain unchanged, respectively SHA256 `0f87bf70c55412bf1fca93e2c3c5c3be569b7257b4b986dc0fb084ff562273f1` and `5f1dc73712ed9e82ffb30becb9d310b5d146ee2686c530b44bb83b9915dc7dfa`. That exposure includes the author's endpoint phase-layer method, earlier finite-lift sources, and the distinct earlier root period-wait proposal. This review does not import that period-wait construction into the present proof.

The declared primary is the saved Bai–Marvian arXiv:2309.11051v3 PDF, SHA256 `add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8`. Its PDF pages 8–16 were read completely for the present construction: the variable exchange identity, controlled exchange, special-unitary decomposition, control recursion, same-weight routing and clean-ancilla phase mechanism. Prior same-byte coverage of pages 3–4, including the theorem hypotheses and strict-path exception, is reused. The entire 38-page paper and unrelated appendices were not independently verified. `PRIMARY_SCOPE.txt` preserves the present extraction. The explicit identities and counts below are independently reconstructed rather than accepted from the paper's theorem label.

Complete actual scientific source, both original and captured launchers, both receipts and all streams were inspected. Exact identity verification establishes that the source read equals the executed source. The failed launch is retained. Detailed coverage and evidence limits are in `SOURCE_COVERAGE.md`.

## 2. Selected support and complete charge-sector extension

Let `M=L+2q`, `n=q+M=L+3q`, `m=n+1`, `d=2^q`, with `q,L>=1`. For each total charge `a=q,...,M`, define

`b_(a,x) = |x>_S |prefix_(a-w(x))>_B`, for every q-bit string x.

The prefix length lies between zero and M because `0<=w(x)<=q`. Every such vector has charge a. Distinct old strings give distinct vectors within the block, and different a give orthogonal charge sectors. There are exactly `(L+q+1)2^q` selected vectors. Acting as V on each full d-dimensional block and as identity on its orthogonal complement is therefore a full unitary commuting with total number. The complement includes nonprefix battery strings and incomplete sectors; it is not discarded. The top block a=M belongs to the full definition even though the supplied input packet does not populate it.

The number of selected vectors is not in general the number of changed columns. The latter is `(L+q+1) r(V)`, where `r(V)=#{x:V e_x != e_x}`; it can be zero for identity V. This is descriptive support accounting, not a zero-decision oracle used by the compiler.

For two states in one selected block,

`h(b_(a,x),b_(a,y)) = h(x,y)+|w(x)-w(y)| <= 2q`.

It is even because the full strings have equal weight. Thus the number of moved excitation pairs is at most q, independent of L. This bounded internal distance, together with O(L) blocks of fixed size, is the useful sparsity property.

## 3. Block elimination and determinant phase

For a two-entry column `(a,b)^T` with `r^2=|a|^2+|b|^2>0`,

`g = (1/r) [[conj(a),conj(b)],[-b,a]]`

is unitary, has determinant one, and maps that column to `(r,0)^T`. At a zero pivot pair choose identity in the exact finite-real existence argument. A fixed lower-triangular elimination uses at most `p=d(d-1)/2` such operations. Earlier cleared columns vanish in both rows of subsequent rotations. Unitarity then makes the first d-1 diagonal entries positive one; the last is `det V`. Hence

`V = G_1^* ... G_p^* D`, with `D=diag(1,...,1,det V)`.

This is an ordinary matrix product: a chronological emitter must apply D first, then `G_p^*,...,G_1^*`. The candidate claims no actual emitted target list, and its equation gives the correct order. Exact branch selection is not being passed off as an effective algorithm.

The determinant phase cannot be thrown away as a global scalar: this block sits beside identity on other physical states. Even `V=e^(i alpha)I` has relative phases against that complement. The candidate's separate diagonal correction preserves them.

## 4. Elementary identities, spectators and base constants

Use `A=exp(i pi R/4)`, `R=(XX+YY)/2`, and onsite `Z(phi)=exp(i phi Z)`. On the one-excitation pair space `(|01>,|10>)`, R is X and `(Z_1-Z_2)/2` is Z. Conjugation by A takes that Z to Y, and conjugation by `S_1^*`, `S=diag(1,i)`, takes Y to X. On the zero- and two-excitation subspaces both R and the difference vanish. Therefore the all-space identity is

`exp(i theta R) = S_1^* A Z_1(theta/2) Z_2(-theta/2) A^* S_1`.

Since `A^8=I`, `A^*=A^7` exactly, including vacuum and double occupation. Expressing each S or S* as an onsite Z introduces opposite scalar factors in these paired conjugations; they cancel exactly at the logical level. The cost is `1+1+2+7+1=12` forward-A/onsite gates. It would be wrong to count an inverse A as one available forward gate.

For an independent sign check, define `F=iSWAP_13 iSWAP_23^* iSWAP_12`, with the rightmost factor acting first. Its full computational-basis action is:

| input | output |
|---|---|
| 000 | 000 |
| 001 | -i 010 |
| 010 | -001 |
| 011 | i 011 |
| 100 | i 100 |
| 101 | -110 |
| 110 | -i 101 |
| 111 | 111 |

It follows directly that `F^* S_3^* R_23 S_3 F = Z_1 R_23`: the transitions 001↔010 have coefficient +1, 101↔110 coefficient -1, and all others vanish. Thus

`E_23(theta/2) F^* S_3^* E_23((-1)^b theta/2) S_3 F`

equals `exp[i theta(1+(-1)^b Z_1)R_23/2]`. It applies the exchange rotation exactly when the control is b and is identity on the other control value and all nonparticipating target states. This checks a full three-qubit unitary, not only the desired transition.

The two variable-exchange calls cost 24. Across F and F* there are three forward iSWAPs (`A^2`) and three inverse iSWAPs (`A^6`), costing 24, and the outer S pair costs two. Hence a singly controlled exchange costs 50. Three such X/Y/X rotations, with a further paired onsite conjugation for the Y rotation, implement a singly controlled arbitrary embedded SU(2) at cost at most `3*50+2=152`. For a controlled iSWAP, the half-angle rotations are A and its inverse, costing eight rather than 24, so the bound is `8+24+2=34`.

A single controlled exchange is not an arbitrary controlled SU(2). The candidate correctly pays for the three-axis construction. The saved paper's abbreviated leaf description is not used to replace 152 by 50 or 34.

## 5. Multiple controls, pair transport and the phase ancilla

Every SU(2) matrix can be written `U=cos(theta)I+i sin(theta) v.sigma`. Choose a unit vector w perpendicular to v, let `A_0=cos(theta/2)I+i sin(theta/2)v.sigma` and `B_0=i w.sigma`. Conjugation by B_0 reverses v, giving

`A_0 B_0 A_0^* B_0^* = A_0^2 = U`.

The endpoints U=±I also have explicit choices, for example `(I,iX)` and `(iZ,iX)`. Embed these matrices as identity outside the one-excitation target pair. Divide the k spectator-control bits into two disjoint groups. The four corresponding conditionally applied factors give U when both groups match; when one group fails, the remaining factor and its inverse cancel; when both fail, all four are identity. This holds on every computational control string and therefore on arbitrary superpositions and reference-correlated inputs. No hidden flag ancilla is needed.

With `T(1)=1` and `T(k)=2T(floor(k/2))+2T(ceil(k/2))`, elementary induction gives

`T(k) <= (9k^2-1)/8` for odd k, and `T(k) <= (9k^2-4)/8` for even k.

The k=2 value is four; the parity bounds supply the induction. Thus a pair gate conditioned on every other bit of n data qubits costs `B(n)=152T(n-2)<=171(n-2)^2`. Here n≥4, so no omitted zero-control base case enters the count.

For a general equal-weight pair at distance 2t, label its t occupied/unoccupied mismatch pairs. The t-1 controlled iSWAPs in the candidate map one string to a string differing from the other in exactly one excitation pair, with phase `i^(t-1)`, while fixing the other string. Their product K is a monomial unitary on the entire basis, not merely a partial map. Conjugating the two-level matrix by `diag(i^(t-1),1)` accounts for that phase. The central gate W is identity off its selected pair, so `K^* W K` is identity on every other basis state even though K itself moved spectators. The cost is

`B(n)+2*34(t-1) <= B(n)+68(q-1)`.

For each block's final determinant phase take the selected string with all q old bits equal to one, `b_a=|1...1> prefix_(a-q)`. It has at least one occupied bit. Clear its first old bit to obtain b'_a. Then `(b_a,ancilla=0)` and `(b'_a,ancilla=1)` have equal charge and differ in two positions. The full special-unitary diagonal

`exp[i theta (|b_a,0><b_a,0|-|b'_a,1><b'_a,1|)]`

phases exactly b_a on the entire ancilla-zero input space and returns the ancilla there. Its ancilla-one action is retained as part of a full unitary; no projection or postselection is used. It costs `B(n+1)=152T(n-1)`. All block phases can reuse the same clean ancilla. They commute; even sharing a partner would not invalidate their ancilla-zero action. Together with the data-only gates, this gives the exact full isometry identity

`C J_A = J_A U_L(V)`

with phase one. The vacuum is fixed. This is stronger than an unspecified scalar equivalence and is the convention actually tested by the effective compiler. Logical S scalars have cancelled, while physical positive-pulse reserves still contribute to the laboratory scalar.

## 6. Count on the physical path

There are `A_count=L+q+1` complete blocks. A V-independent integer upper bound before spatial routing is

`G0=A_count { p[152T(n-2)+68(q-1)]+152T(n-1) }`.

The arbitrary pair gates in this alphabet are forward A; onsite Z needs no transport. A pair at path separation j-i is implemented by at most j-i-1 adjacent **full physical SWAPs**, one desired adjacent gate, and the reverse SWAP sequence. With m=n+1 sites this costs at most `2(m-2)+1=2n-1` per elementary gate. A full SWAP is a separate supplied positive control in the parent. Substituting an iSWAP or a fermionic swap would invalidate this unqualified conjugation argument. All moved qubits are restored by the inverse permutation. Therefore

`G <= Gbar=(2n-1)G0`

and

`Gbar <= (2n-1)(L+q+1){p[171(n-2)^2+68(q-1)]+171(n-1)^2}`.

For L≥1, use `n<=(3q+1)L`, `L+q+1<=(q+2)L`, and enlarge the constant term by L². This gives exactly

`K_q = 2(3q+1)(q+2){171(p+1)(3q+1)^2+68p(q-1)}`,

`Gbar <= K_q L^4`.

The factors are O(L) blocks, O(L²) spectator synthesis per block, and O(L) spatial routing. Generic synthesis on a `(L+q+1)2^q`-dimensional active subspace would not by itself justify this power. Fixed q is essential: p grows exponentially in q. The claim is not polynomial jointly in q and accuracy. There is no numerical evidence here of a complete emitted elementary list achieving the bound; the bound follows from the analytical construction and its imported gate permissions.

## 7. Effective certification, with its actual limits

Exact pivot, axis and phase choices can be discontinuous functions of a computable V. The candidate avoids an unjustified zero oracle by separating finite-real existence from a finite-error search. For rational positive eta_C, enumerate all words of length at most G0 over the finite operand alphabet and an onsite angle grid with spacing at most `eta_C/[8 max(1,G0)]`. Telescoping products of unitaries bounds the distance from a rounded exact word by the sum of its angle errors, at most eta_C/8. The -pi endpoint can be replaced by +pi since both onsite unitaries are exactly -I; this does not introduce an output scalar ambiguity, and the positive-reserve absolute angle agrees.

The tested residual is the entire isometry `E=CJ_A-J_AU_L(V)`, without optimizing a free phase and without dropping ancilla output rows. For a rational approximation Ehat with certified `||E-Ehat||<=delta`, one can certify

`Tr[(Ehat^*Ehat)^k] < (eta_C-delta)^(2k)`.

The Schatten 2k norm decreases to the operator norm. More explicitly, it lies between `||Ehat||` and `D^(1/(2k))||Ehat||`, where D is the finite input dimension. Thus the word with strict margin is eventually certified under sufficiently fine matrix enclosures and increasing k. Dovetailing candidates/refinements prevents a threshold candidate from blocking the search. A full-matrix Frobenius test alone at the stated coarse grid would not have this property; the candidate explicitly avoids that substitution.

Block repetition does not multiply the target operator error: `||U_L(Vhat)-U_L(V)||=||Vhat-V||<=d delta_v` for entrywise enclosure radius delta_v. Consequently `delta_v<=eta_C/(32d)` is a valid input allowance. Vhat need not itself be unitary when used only to enclose the target residual. Matrix-product evaluation on the physical 2^m space may still require O(m) additional precision bits, exponential storage and enormous search effort. No efficient classical algorithm follows. Oracle response time is not bounded. The note proves a supplier exists for computable data and positive tolerance; it does not supply a target-specific certificate or implemented compiler for an unspecified V.

## 8. Nominal duration, phases, precision and physical scope

The same parent generators and cosine pulses apply, with `Q_*=6pi` and fixed

`h >= max(4 hbar Q_*/g, sqrt(4pi hbar Q_*/sigma))`.

Pad to Gbar serial slots with zero pulses and use the parent's final **parallel onsite** phase slot. The duration `tau=(Gbar+1)h` is fixed from q,L before choosing target-dependent angles. With `x=Delta tau/hbar`, a rational r satisfying `|r-x/(2pi)|<=1/4` and `k=floor(r)+2` yields `lambda=2pi k-x` in `(3pi/2,9pi/2]`. Integer number eigenvalues give `exp[-i(x+lambda)N_tot]=I` on all physical states. The old `K=E0 I+Delta N_S` stays present with coefficient one throughout. No inverse old evolution is substituted.

The nominal endpoint is

`U_lab(tau)=exp[-i(E0 tau/hbar+Phi)] C`,

`Phi=(pi/4) N_forward_A + sum_actual_word |phi|`.

The exact logical convention is phase one, so there is no unspecified zeta. Full SWAP reserve and exchange phases cancel at their endpoints, but their positive energy and work remain charged. Phi must be computed from the actual rounded word. Neither the target's own phase nor E0 is removed.

The parent joint bound is `4pi q/(L+1)+epsilon_p+2eta_C+2eta_H+2eta_t`, retaining S/B/A/R. Selecting rational rho within 1/4 of `20pi q/epsilon` and `L=floor(rho)+2` avoids exact ceiling decisions and gives `L<=(20pi q+3)/epsilon` for epsilon≤1. With `A_q=20pi q+3`, `C_q=K_q A_q^4`, `D_q=A_q+3q+1`, one obtains `Gbar<=C_q epsilon^-4`, `tau<=h(C_q+1)epsilon^-4` and `m<=D_q/epsilon`. The allocation `epsilon_p<=epsilon/5`, `eta_C,eta_H,eta_t<=epsilon/10` gives five contributions at most epsilon/5 each.

These are nominal laboratory bounds **starting with a ready state and compiled schedule**. They do not count obtaining the coherent sine packet, preparing its phase, performing the classical search, oracle latency, or storing an unknown input while that search runs. Such storage would have its own actual-time evolution. Fixed per-site caps do not imply an accuracy-independent global installed norm; here it grows as O(epsilon^-1).

The sufficient precision requests can be checked directly. For

`b_*=hbar epsilon^5/[30h(C_q+1)]`,
`delta_*=epsilon^5/[30(C_q+D_q)]`,
`area_*=delta_*/Q_*`,
`time_*=hbar epsilon^2/[10(E0+D_q Delta)]`,

the static integral `tau b/hbar`, aggregate generator error `(Gbar+m)delta`, and aggregate area error `Q_*(Gbar+m)area` each contribute at most epsilon/30. Also `(E0+mDelta)time_*/hbar<=epsilon/10`. An onsite angle error delta_*/2 suffices because `||Q_phi-Q_phi'||<=2|phi-phi'|`. The global static allowance must be divided among M+1 new free fields if bounded individually, producing a sufficient O(epsilon^6) per-field request. No error in literal old K is silently included as a redefinition.

Computing lambda to O(epsilon^5) after subtracting two O(epsilon^-4) numbers needs, for example, O(epsilon^9) errors in the relevant Delta and pi evaluations, with the tau/unit errors and cross terms separately budgeted. The displayed inequalities `tau delta_Delta/hbar<=delta_lambda/4` and `2|k|delta_pi<=delta_lambda/4` express that conditioning. Choosing a fixed certified rational h removes an avoidable timing arithmetic ambiguity. Phase reporting still needs precision for E0 tau/hbar and Phi. O(log(1/epsilon)) requested bits for these fixed physical numbers does not bound oracle time or the much larger internal matrix arithmetic.

All these error bounds are distinct from physical admissibility. A small Hermitian perturbation need not preserve positivity of a positive semidefinite generator with zero eigenvalues. Support, positive parameterization, actual pulse norm and per-site derivative bounds must be supplied or independently certified. Equal matched gaps, the full-SWAP path and simultaneous final onsite access on all m qubits are physical premises. A permission for only one active control globally or only one old port does not imply this schedule.

## 9. Guarded start shifts and inherited output qualifications

For the optional start-shift model, adding one h guard at each end changes the declared time to `tau_g=(Gbar+3)h`; lambda must be recomputed from this complete time. The zero-extended cosine envelope is C1 and has `integral |f_h'|=4/h`. The translation estimate gives

`integral |f_h(t-s)-f_h(t)| dt <=4|s|/h`,

and hence `eta_shift <= (4Q_*/h)(Gbar+m)delta_s`. The stated `delta_s<=h eta_H_budget/[8Q_*(Gbar+m)]` spends at most half the generator budget. Use the remaining half for the coefficient categories, with tau_g and the changed constants.

If delta_s<h/2, three serial supports cannot overlap: the first's latest end is before the third's earliest start. During the final layer at most one serial pulse and one onsite pulse touch a particular site. Requiring each **actual** integrated positive generator, including its area multiplier, to have norm at most Q_* therefore yields at most g and sigma per site. Adding the allowed new static-field error fits Delta+2g. This is not a consequence of a Duhamel error bound alone. Width or waveform distortions require separate integrals. An accumulating per-period start error needs a further division by Gbar+1, giving the stated sufficient O(epsilon^9) request. It does not specify a microscopic clock.

The endpoint time-error formula must retain the parent's condition that sampling occurs **after all pulses have turned off**. Sampling inside a pulse instead requires its control contribution in the timing/error integral. The guard model can ensure this by an additional sampling-margin condition, or by post-off sampling; the algebraic `time_*` bound alone is not a universal pulse-support certificate for arbitrary fixed constants.

The remaining inherited limits are consequential:

* The nominal conserving schedule preserves the entire distribution of the fixed free observable F, including joint moments and covariance. It does not make the time-varying controlled Hamiltonian constant. All battery and ancilla outputs remain present.
* Net prescribed-drive work is zero in the ideal matched model because F is conserved and the controls vanish at both endpoints. The absolute-work bound follows by integrating each pulse's derivative norm: at most `g(Gbar+m)`, or the stated coarser calibrated `sigma h(Gbar+m)` under its support/derivative assumptions. Overlap can be handled by the triangle bound per pulse. Identity reserves contribute to energy, work and phase.
* The parent's nominal old-energy transfer estimate using final trace error alone presumes the actual initial old marginal equals the declared one. Under full readiness distance epsilon_p alone, retain the initial-marginal error as well: the safe discrepancy bound is `(q Delta/2)(e_out+epsilon_S0)`, with `epsilon_S0<=epsilon_p`. This was demonstrated and qualified in the unchanged prior review. This compiler-count result does not repair or supersede that boundary.
* Moment errors require the relevant observable norms, initial allowances and covariances; trace readiness by itself does not yield accuracy-independent battery moment accuracy as M grows. Scalar E0 cancels from equal-trace energy differences but remains in absolute energies and amplitude phase.
* Uniform storage comparison requires the same subsequent free evolution. A persistent calibrated static mismatch or noise incurs an additional storage-time integral. Endpoint agreement does not imply permanent halt, fresh reusable reference, or indefinitely repeatable reservoir operation.
* External phase preparation, controls, clock and their microscopic energy outputs are supplied, not closed by this finite driven schedule. This is an equal-gap noninteracting old plant result, not measured-energy identification, a general-H theorem, or a native autonomous construction.

## 10. Actual finite evidence and unresolved implementation work

The author's exact SymPy source is SHA256 `2ede311427e4e765dfa0f75ac3ad7feeb4af31f5873f42a5bb1c787216c7d565`. It checks full finite generator/control identities, both control values, inverse-A powers, a nonreal split-control SU(2) example, six complex d=4 Givens eliminations with determinant remainder -i, clean-ancilla diagonal phases including a shared partner, and the q=2,L=1 selected-prefix enumeration. Its wrong-S-adjoint and omitted-inverse mutants have exact squared Frobenius residuals 16 and 32/5. Those are actual discriminators of the named finite risks.

The first launch failed before executing the scientific source. Its receipt has exit code null and stderr `SubprocessError('Exception occurred in preexec_fn.')`. The exact cause is not exposed; removing the attempted address-space restriction in the retry is not proof of the cause. The retry ran the same source once, with a 90-second wall timeout and 60-second CPU limit, completed in approximately 1.48 seconds and exited zero. Both original argv records contain the source path without `-B`; they are preserved unchanged. The metadata verifier does not retrofit them.

The successful source does not produce a 152-gate or 34-gate primitive list, implement the arbitrary-k recursion, emit and route an entire target compiler, certify a finite angle-grid search, or simulate the positive pulse schedule. Its unused helper supplies no tested coverage. The general identities and count therefore rest on the analytical arguments above and the stated primary-source dependencies, not 18 PASS booleans. The author's suggested future end-to-end list check is sensible implementation work; it has not occurred here and is not claimed.

The present packet's captured execution is explicitly metadata-only. It verifies all 21 author freeze members, the seal, sources/launchers/stream hashes and unchanged prior review identities. The complete stdout and empty stderr were inspected. No new numerical science result, target-specific circuit, retained audit verdict, canonical edit, Git operation, publication, prompt/axiom edit or lock change is claimed. Within the stated scope the nominal fixed-q polynomial count survives this review, subject to the qualifications above.
