---
claim_id: corrected_dispersion_bounded_theorem_note_2026-10-13
claim_type: bounded_theorem
claim_scope: "Supplied massive one-dimensional chain: fixed finite positive kinetic corrections, uniform smooth-cell commutators and domains, and full placed-density comparison with the exact compressed potential on stated growing time windows."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
artifact_role: theorem
assembly_status: publication_prepared_exact_root_review_pending
runner: scripts/corrected_dispersion_identity_2026_10_13.py
scientific_execution: none_in_publication_preparation
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
conditional_surface_status: "Supplied model, polarization, ordinary cells and fixed finite smooth interaction; named provisional parents remain conditional and Current remains open_gate."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Accepted ordinary conditional proof assembled without a mathematical-body edit; source assembly accepted; new publication wrappers await root review."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Root review of the exact publication wrappers, identity tools and driver before any runtime or publication action."
upstream_dependencies:
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
---

# Corrected dispersion: publication wrapper

Claim type: bounded_theorem

This projection preserves the accepted 1049-line proof apart from two explicit LaTeX whitespace repairs; the original archived proof has
SHA-256 `402cbc03585ac1cf0fc32facfc18b889de09a2fc9b3bb1449dfda47beb813c0d`.
Only this wrapper and the closing source/status appendix are new. The exact
source assembly was accepted by ordinary root review. These publication
wrappers and the identity-only tool remain subject to separate exact review;
no scientific execution or retained-status decision occurs in preparation.

The theorem fixes positive mass and velocity, the supplied one-dimensional
carrier, ordinary one-sided cells, and a fixed finite selfadjoint even CAR
polynomial in fixed smooth compact real inputs. Each kinetic order is chosen
before the spacing limit. The comparison is between the entire placed actual
density and low evolution of its unconditional high partial trace with high
vacuum appended. The effective potential is the exact finite-spacing
compression, including its high contractions. The physical-band operator
domains and the different full-low effective domain keep their stated roles.

The first kinetic correction is the displayed quadratic-in-spacing term in
the original proof. For every fixed order J, its sufficient growing window
has T_c c^(2J+2) tending to zero. The proof's first interacting-mean argument
retains its older valid power 1/(4J+7). The companion
moment-sensitive note
later obtains 1/(4J+6) under its explicit moment and commutator resources.
The older proof is not rewritten to contain that later argument.

This proof was recovered after a transport failure; the recovery worker saw
the predecessor's draft. Its exclusion of the new root candidates and its
disclosed earlier smooth-high exposure remain separate facts. Later complete
comparison and ordinary root acceptances are bound in the appendix. None
establishes model diversity, a fresh proof by this assembly worker, formal
analytic verification or a transitive audit.

Original titles, exposure disclosures, failed routes, and statements that
review or potential identification was pending remain historical statements
at their original freeze. The full accepted body begins immediately below.

# Finite kinetic corrections for ordinary-cell interactions: checked recovery

Status: conditional-support; ordinary bounded theorem proposal.
Claim type: bounded_theorem. Trace class: upstream_support.
Current remains open_gate. No retained or audit status is conferred.

For the supplied representation and a fixed finite smooth ordinary-cell
interaction, the first explicit kinetic correction is
\(c^2v^2p^4/(8E(p))\). With the exact finite-spacing high-vacuum compressed
potential it gives a sufficient low evolution window \(T_c=o(c^{-4})\),
compared with \(o(c^{-2})\) without that correction. A whole-band remainder,
uniform free commutators, and an interacting spectral-window domain bootstrap
prove the full placed-density comparison. An interacting first-mean-energy cap
suffices after an explicit spectral truncation. The note also verifies each
fixed finite correction order. None of these statements identifies the
effective potential with a fixed continuum polynomial.

This is a recovery of a prior same-family derivation whose transport failed.
The complete recovered draft was read before this worker's proof checks and
was treated as unverified. Its mathematics is now checked below, with the
load-bearing checks recorded separately. Thus this worker is source exposed
to that draft; it is not an independent second derivation of the draft itself.
Both the recovery and its predecessor exclude the new corrected-dispersion
and effective-potential root candidates. The predecessor's disclosed prior
exposure to the old smooth-high root remains part of the provenance.
No model diversity or transitive parent audit is claimed.

## 1. Source contract and precise comparison

The neutral source plan was sealed at 2026-10-13T00:27:58.167630+00:00,
before scientific copying or rereading for this task. The five exact inputs are:

| Label | File | SHA-256 |
|---|---|---|
| Current | CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md | 763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff |
| Local | LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md | b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa |
| Ground | BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md | 8454f1c88d5d6c05910b5d7fd1ec34d454118c4b41ad3d930a339c77c97c45b2 |
| S | SMOOTH_HIGH_BAND_DECOUPLING_INDEPENDENT.md | c69d638eb4519d81e51dd39fd920b7323d320d5aea9c427ff109736bdcda75dd |
| D | LOW_BLOCK_EFFECTIVE_DYNAMICS_CROSSCHECK.md | 10aa75b19058e8cc635a7c2a35a31552fbdb7976851c6bb0ec3c432ad9a061e3 |

This recovery worker read all five permitted copied bodies completely:
Current 601 lines, Local 731, Ground 1199, S 768, and D 480. Truncated combined
outputs were repaired by explicit overlapping reads; none is counted as
completed coverage without that recovery. Ground's later formal records were
read as part of its body, but no formal analytic evidence is imported.
Underlying parent bodies and the source paths mentioned inside these notes
were not followed. The prior READ_COVERAGE.json is preserved unchanged;
RECOVERY_READ_AND_PROOF_CHECK.md records this worker's actual coverage.

The predecessor disclosed exposure to old smooth-high root 54cac073 and its
old crosscheck 1a10d9c6. This worker has not opened either underlying file.
No new dispersion/effective-potential root, forbidden failed-worker folder,
scalar or positive-series Lean source, symbolic check, checkpoint/queue, or
publication source was read. The explicitly assigned recovery draft is the
only additional candidate body read. The inherited model and reasoning effort
are unchanged. The five copied source hashes were rechecked against the sealed
input manifest before completing this proof.

Fix the supplied \(m,v>0\), the ordinary cell origin, and the exact Current
placement:
\[
 (C_cf)_j=c^{-1/2}\int_{cj}^{c(j+1)}f(x)\,dx,\qquad
 J_cC_cf=(\ell_cf,h_cf).
 \tag{1}
\]
Real smearings have two components. Use a fixed finite formally selfadjoint
even polynomial
\[
 V_c=(U_c+U_c^*)/2,\qquad
 U_c=\sum_\alpha a_\alpha
        \prod_{j=1}^{n_\alpha}\gamma(J_cC_cf_{\alpha j}),
 \quad n_\alpha\ {\rm even}.
 \tag{2}
\]
The inputs, coefficients, degrees and term count are independent of c.
There is no cell-by-cell normalization by spacing-dependent norms.
Complex smearings may first be expanded into real and imaginary parts.
A uniform bound is
\(K_{\rm pol}=\sum_\alpha|a_\alpha|\prod_j\|f_{\alpha j}\|\);
let K be any valid uniform total norm bound for \(V_c\).
No assumption \(K<m/2\) is needed in this note.

Fixed compact physical support makes each \(V_c\) an actual finite even-spin
observable on its cell hull. A growing number of cells in that fixed interval
does not make (2) an extensive sum. The theorem below also works without
compact support under its stated Sobolev conditions; in that case this finite
physical-support assertion is not available.

Work on Ground's actual carrier \(\Pi_c\mathcal F_*\), with
\[
 \mathcal F_*=\mathcal F_L\otimes\mathcal F_H,\quad
 P=I_L\otimes|\Omega_H\rangle\langle\Omega_H|,\quad Q=I-P,
 \quad P\Pi_c=q_c\otimes|\Omega_H\rangle\langle\Omega_H|,
 \quad q_c=\Gamma(\mathbf1_{I_c}),\quad I_c=(-1/c,1/c).
 \tag{3}
\]
The low one-particle carrier is the positive eigenline of
\(D(p)=-vp\sigma_x-m\sigma_y\), with
\(P_+(p)=(I+D(p)/E(p))/2\). The high carrier has
\(C_0=-\sigma_y\) and \(P_0=(I+C_0)/2\). These are the supplied
polarizations, not additional state choices. Low-first ordering fixes the
graded tensor identification in (3).
The actual positive free Hamiltonian is \(H_c\), and \(G_c=H_c+V_c\).
On the two one-particle branches,
\[
 E(p)=\sqrt{m^2+v^2p^2},\quad w_c(p)=\sqrt{1-c^2p^2},
\]
\[
 e_{c,L}^2=m^2+\frac{2v^2p^2}{1+w_c},\qquad
 e_{c,H}^2=m^2+\frac{2v^2}{c^2}(1+w_c),\qquad
 \Lambda_c=\sqrt{m^2+2v^2/c^2}.
 \tag{4}
\]
In particular \(E\le e_{c,L}\le\sqrt2E\) and \(H_c\ge\Lambda_cQ\).
P and \(\Pi_c\) strongly reduce the free operator and its powers.
Write \(H_{L,c}=d\Gamma(e_{c,L})\) on \(q_c\mathcal F_L\) and
\(H_0=d\Gamma(E)\) on full \(\mathcal F_L\). Every free Fock operator here
has its maximal multiplication domain: for one-particle multiplier e,
\[
 D(d\Gamma(e))=
 \left\{\Psi=(\Psi_n)_{n\ge0}:\quad
 \sum_{n\ge0}\left\|\Bigl(\sum_{i=1}^n e(p_i)\Bigr)\Psi_n\right\|^2
 <\infty\right\}.
\]
For two branches the sum uses each particle's actual branch energy; on the
vacuum the sum is zero. Powers use the corresponding power of that sum.
At each fixed c, both actual branch energies lie between m and a finite
upper bound, so \(D(H_c^j)=D(N^j)\) on its actual carrier for positive
integers j; the analogous low statement holds on q_c. Bounded perturbation
gives \(D(G_c)=D(H_c)\) and selfadjointness. Higher interacting domains are
proved in section 4. No outside-band zero-energy extension is used in a
spectral or energy bound.

A density \(\rho_c\) below is already the placed actual density:
\(\rho_c=\iota_c\rho_c^{\rm phys}\iota_c^*\).
The effective initial density is its full high partial trace
\[
 \tau_c=\operatorname{Tr}_H\rho_c ,
 \tag{5}
\]
which has support in \(q_c\mathcal F_L\). No high-vacuum conditioning or
state-dependent normalization is implicit in (5). The conclusion compares
the entire placed density with an evolved low density tensored with high
vacuum, not just selected observables.

## 2. Uniform cell energy-Sobolev estimate, including all aliases

Let \(D_c\) be Local L3's bounded signed lattice generator. Its periodic
continuum Fourier multiplier will be denoted \(\mathscr D_c\), using the same
matrix symbol at every real k. Direct multiplication, with Current's
\(g_c\mathsf J_c=v^2/(4c^2)\), gives
\[
 \mathscr D_c(k)^2
   =s_c(k)^2I,\qquad
 s_c(k)=\sqrt{m^2+\frac{4v^2}{c^2}\sin^2(ck/2)}
        \le E(k).
 \tag{6}
\]
The equality contains the mass term and the exact lattice coupling; it is not
the continuum approximation to the lattice clock.

Cell integration commutes exactly with translations by c. Since \(D_c\)
and \(\mathscr D_c\) are the same finite translation/matrix expression on the
two spaces,
\[
 D_c C_c=C_c\mathscr D_c.
\]
All three operators here are bounded at a fixed c. Polynomial approximation
of continuous functions on their bounded spectral intervals therefore gives,
for every real \(r\ge0\),
\[
 |D_c|^r C_c=C_c|\mathscr D_c|^r=C_c s_c(D_x)^r .
\]
Using the contraction \(C_c\), (6) proves the uniform estimate
\[
 \boxed{\ \||D_c|^r C_cf\|\le\|E(D_x)^r f\|,\qquad f\in H^r.\ }
 \tag{7}
\]
The constant is one and does not deteriorate at the fold or with c.

Current's isometry and exact diagonalization of absolute energy now give
\[
 \boxed{\ \|e_{c,L}^r\ell_cf\|^2+\|e_{c,H}^r h_cf\|^2
       =\||D_c|^rC_cf\|^2\le\|E^r f\|^2.\ }
 \tag{8}
\]
These are norms in the supplied real coefficient spaces. In particular
\(\|E^r\ell_cf\|\le\|E^rf\|\) on the low output.

No alias term has been discarded in (7). The exact translation intertwining
already includes them. For comparison with S's high-tail argument, put
\(S_a=\mathbf1_{|k|<a}\). The exact high coefficient vanishes on
\(S_{\pi/(2c)}\), so (8) applied to the complementary input also gives
\[
 \|e_{c,H}^r h_cf\|
 \le\|E^r(1-S_{\pi/(2c)})f\|
 \le(2c/\pi)^s
       \|E^r|D_x|^s(1-S_{\pi/(2c)})f\|=o(c^s)
 \tag{9}
\]
for each fixed \(f\in H^{r+s}\), \(r,s\ge0\).
Removing the tail indicator in the last norm gives a uniform big-O bound
on a bounded Sobolev family. Fixed-input little-o and uniform-family big-O
are different statements.

## 3. Bounded iterated free commutators and exact high blocks

Write \(\mathfrak D_c\) for Local's signed coefficient generator after the
Current placement. For real h in its domain, the supplied field flow is
\[
 e^{itH_c}\gamma(h)e^{-itH_c}=\gamma(e^{it\mathfrak D_c}h)
\]
on the placed range. Its branches are
\(e_{c,L}D/E\) and \(e_{c,H}C_0\).
For an integer \(r\ge0\), the rth norm derivative of a field is
\(\gamma((i\mathfrak D_c)^r h)\). Reality is preserved because
\(i\mathfrak D_c\) maps real coefficients to real coefficients.

Equivalently, on the usual finite-particle core the creation/annihilation
identities give the same commutator, and norm differentiation extends it.
The multinomial Leibniz rule and (7) give the explicit constants
\[
 M_r=\sum_\alpha|a_\alpha|
 \sum_{j_1+\cdots+j_{n_\alpha}=r}
 {r!\over j_1!\cdots j_{n_\alpha}!}
 \prod_{k=1}^{n_\alpha}\|E^{j_k}f_{\alpha k}\|,
 \tag{10}
\]
\[
 \|\operatorname{ad}_{H_c}^{\,r}(V_c)\|\le M_r.
 \tag{11}
\]
Multiplication by \(i^r\) does not change the norm. The adjoint half of (2)
has the same bound, so no extra factor two is present. Degree-zero terms
contribute only when r=0. No inverse input norm occurs.
For r fixed, \(f_{\alpha k}\in H^r\) suffices for (10).
A fixed smooth compact polynomial supplies every finite r uniformly in c.

Here is the domain content of (11), rather than just a formal commutator.
If \(t\mapsto e^{itH}Ve^{-itH}\) is norm differentiable, then for
\(\psi\in D(H)\) the identity
\[
 e^{itH}V\psi=(e^{itH}Ve^{-itH})e^{itH}\psi
\]
has a strong derivative at zero. The generator criterion gives
\(V\psi\in D(H)\) and \(HV\psi=VH\psi+[H,V]\psi\).
Applying the same argument to the successive bounded norm derivatives and
inducting yields, when derivatives through order r exist,
\[
 V D(H^r)\subset D(H^r),\qquad
 H^rV\psi=\sum_{j=0}^r{r\choose j}
          \operatorname{ad}_H^j(V)H^{r-j}\psi .
 \tag{12}
\]
This supplies the typed domains used below.

Define the exact compressed potential and actual coupling by
\[
 PV_cP=W_c\otimes|\Omega_H\rangle\langle\Omega_H|,\qquad
 B_c=QV_cP,\qquad \beta_c=\|B_c\|\le K.
 \tag{13}
\]
The unital CAR extension of Vc or Wc has the same norm as its physical
restriction: the polynomial is supported in the in-band coefficient space
and, being even, acts as that operator tensor the identity on outside modes.
The high-vacuum off-block norm is computed on the actual carrier; its tail
bound below remains valid there.

The already independently proved S bounds give
\[
 \beta_c\le B_1(c):=\sum_\alpha|a_\alpha|
       \sum_j t_{\alpha j}\prod_{k\ne j}F_{\alpha k},
 \quad t_{\alpha j}=\|h_cf_{\alpha j}\|,\quad F_{\alpha j}=\|f_{\alpha j}\|,
\]
\[
 \epsilon_c:=\|W_c-V_c^L\|\le B_2(c):=
 \sum_\alpha|a_\alpha|\sum_{i<j}t_{\alpha i}t_{\alpha j}
                                  \prod_{k\ne i,j}F_{\alpha k}.
 \tag{14}
\]
Here \(V_c^L\) is (2) evaluated on \(\ell_cf\), with its same formal
symmetrization. The off-block bound is linear in high tails. The compression
bound is quadratic by the Taylor interpolation of the fields
\(\gamma(\ell,u h)\): its compressed first derivative vanishes and the second
derivative is twice the pair sum. Evenness permits a single high field
accompanied by an odd low field and does not improve \(\beta_c\) to B2.

For fixed inputs in Hs, \(\beta_c=o(c^s)\) and \(\epsilon_c=o(c^{2s})\).
Fixed smooth compact data give every finite algebraic order.
These are actual high-component statements, not estimates of the whole
coefficient error.

The exact potential in (13) can be calculated without defining a new
normal-ordering prescription. In the low-first tensor order,
\(\gamma(\ell,h)=L+Z_L\otimes H\).
For an ordered word and an even subset S of high slots, its contribution is
\[
 (-1)^{N(S)}
 \omega_H\!\left(\prod_{j\in S}^{\longrightarrow}\gamma_H(h_j)\right)
 \prod_{j\notin S}^{\longrightarrow}\gamma_L(\ell_j),
 \quad
 N(S)=\#\{(i,j):i\in S,\ j\notin S,\ i<j\}.
 \tag{15}
\]
Sum all even S, then perform (2)'s linear combination and symmetrization.
Odd S vanish. The high expectation is the finite Pfaffian with covariance
\(2\langle h_i,P_0h_j\rangle\). Formula (15) fixes the graded signs.
Its empty subset is \(V_c^L\); all other subsets are actual high-vacuum
contractions. This is the exact effective potential used below.

Since P commutes with the free flow and the high vacuum has energy zero,
\[
 \operatorname{ad}_{H_{L,c}}^r(W_c)
       =P\,\operatorname{ad}_{H_c}^r(V_c)\,P
 \tag{16}
\]
under the low identification. Thus it has the same M_r bound and domain
properties. Compact physical support of (2) does not make Wc physically local.

## 4. Operator-domain bootstrap on bounded interacting windows

The following elementary lemma explains the regularity resource.

Let \(r\ge1\) be an integer, \(H\ge0\) selfadjoint, \(V=V^*\) bounded
with \(\|V\|\le K\), and \(G=H+V\) on D(H). Assume bounded free
commutators of orders 1 through \(r-1\) in the norm-flow/domain sense proved
in section 3. For \(r=1\) this is an empty additional assumption.
Then
\[
 D(G^r)=D(H^r).
 \tag{17}
\]
Indeed it holds for r=1 by bounded perturbation. At the next step, (12) makes
V preserve \(D(H^{r-1})\). If \(\psi\in D(G^r)\), induction gives
\(\psi,G\psi\in D(H^{r-1})\), so
\(H\psi=G\psi-V\psi\in D(H^{r-1})\).
Conversely, if \(\psi\in D(H^r)\), then
\(G\psi=H\psi+V\psi\in D(H^{r-1})=D(G^{r-1})\).
This proves (17) and every intermediate domain assertion.

For \(R\ge-K\), put \(E_R=\mathbf1_{[-K,R]}(G)\) and
\(m_R=\max(K,|R|)\). Set \(\kappa_0=K\), and let \(\kappa_j\) bound
\(\|\operatorname{ad}_H^j(V)\|\) for \(j\ge1\). Define
\[
 C_0(R)=1,\qquad
 C_n(R)=m_R C_{n-1}(R)+
   \sum_{j=0}^{n-1}{n-1\choose j}\kappa_j C_{n-1-j}(R).
 \tag{18}
\]
Then, for every integer \(0\le n\le r\),
\[
 \boxed{\ \|H^nE_R\|\le C_n(R),\qquad
 \|H^n e^{-itG}E_R\|\le C_n(R).\ }
 \tag{19}
\]
To prove it use, on the domains just established,
\[
 H^n\psi=H^{n-1}G\psi-
 \sum_{j=0}^{n-1}{n-1\choose j}
      \operatorname{ad}_H^j(V)H^{n-1-j}\psi,
\]
and note that \(GE_R\) stays in E_R and has norm at most \(m_R\).
The second bound in (19) uses exact G-window invariance. There is no
exponential-in-time Gronwall factor.

The constants are explicit polynomials of degree n in \(m_R+K\).
For example \(C_1=m_R+K\),
\(C_2=(m_R+K)^2+\kappa_1\), and
\(C_3=(m_R+K)^3+3\kappa_1(m_R+K)+\kappa_2\).
For fixed resources, \(C_n(R)\le C(1+R)^n\) when \(R\ge0\).

Apply this lemma to the actual \(H_c,V_c,G_c\), with (10)–(11).
It is uniform in c. Also apply it to
\[
 A_c=H_{L,c}+W_c
 \tag{20}
\]
on \(q_c\mathcal F_L\), using (16).
The mere equality \(D(H+V)=D(H)\) would not justify these higher powers.
Ground (28)–(30)'s rough compact input explicitly fails even free form-domain
preservation; compact physical support and boundedness alone do not imply
the uniform commutator hypotheses.

## 5. Explicit finite kinetic corrections and a global remainder

Let \(J\ge0\) be a fixed integer. J counts the retained correction terms;
J=0 is the uncorrected continuum kinetic energy.

For \(p\in I_c\), put
\[
 z=c^2p^2\in[0,1),\qquad
 u={v^2p^2\over E(p)^2}\in[0,1),\qquad
 g(z)={1-\sqrt{1-z}\over1+\sqrt{1-z}}.
\]
The exact dispersion is
\[
 {e_{c,L}(p)\over E(p)}
  =\Phi(z,u):=\sqrt{1+u g(z)}.
 \tag{21}
\]
Write \(\Phi(z,u)=1+\sum_{n\ge1}d_n(u)z^n\). Its coefficients are explicit:
\[
 d_n(u)={u\over 2n\,4^n}
 \sum_{k=0}^{n-1}{-1/2\choose k}
                u^k {2n\choose n-1-k},\qquad n\ge1.
 \tag{22}
\]
In particular
\[
 d_1(u)=u/8,\qquad d_2(u)=u/16-u^2/128.
 \tag{23}
\]

Here is a derivation and a sign check for all finite orders. The relation
\(z=4g/(1+g)^2\) determines g analytically near zero. Coefficient extraction
after the substitution \(z=4t/(1+t)^2\), followed by formal integration by
parts of the coefficient residue, gives
\[
 [z^n]F(g(z))={1\over n4^n}
       [t^{n-1}]F'(t)(1+t)^{2n}.
\]
For clarity, put \(\varphi(t)=(1+t)^2/4\), so \(z=t/\varphi(t)\).
The substituted coefficient residue is
\[
 \operatorname{Res}_{t=0}
 F(t)\left(\frac{\varphi(t)^n}{t^{n+1}}
            -\frac{\varphi(t)^{n-1}\varphi'(t)}{t^n}\right).
\]
The residue of \((F(t)\varphi(t)^n/t^n)'\) is zero. Solving that
identity for the second summand gives
\(n^{-1}\operatorname{Res}_{t=0}F'(t)\varphi(t)^n/t^n\), exactly the
displayed coefficient. The substitution is locally invertible since
\(dz/dt=4\) at zero. Thus no all-order sign premise is assumed in (22).
Apply it to \(F(t)=\sqrt{1+ut}\) to obtain (22).
The absolute successive terms inside its alternating finite sum have ratio
\[
 {2k+1\over2k+2}\,u\,{n-1-k\over n+2+k}<1
 \quad(0\le k<n-1,\ 0\le u\le1).
\]
Consequently \(d_n(u)>0\) for \(u>0\), and \(d_n(0)=0\).

For \(|z|<1\), the principal square root has
\({\rm Re}\sqrt{1-z}>0\), so \(|g(z)|<1\).
Thus \(\Phi\) is analytic there for every \(0\le u\le1\).
For real z increasing to one, nonnegative coefficients and monotone
convergence give
\[
 \sum_{n\ge1}d_n(u)=\sqrt{1+u}-1\le u/2 .
\]
This proves the uniform global remainder, including the region arbitrarily
close to the fold:
\[
 0\le\Phi(z,u)-\sum_{n=0}^Jd_n(u)z^n
   \le {u\over2}z^{J+1},\qquad 0\le z\le1,\quad d_0=1.
 \tag{24}
\]
No derivative at \(z=1\), which would diverge, was used.

Define the finite explicit kinetic energy
\[
 e_c^{[J]}(p)
   =E(p)\sum_{n=0}^Jd_n\!\left({v^2p^2\over E(p)^2}\right)c^{2n}p^{2n}.
 \tag{25}
\]
It is positive for all real p, since every retained coefficient is
nonnegative. On \(I_c\),
\[
 E\le e_c^{[J]}\le e_{c,L}\le\sqrt2E.
\]
Put \(\alpha=2J+2\) and \(r=\alpha+1=2J+3\). From (24),
\[
 \boxed{\ 0\le r_c^{[J]}(p):=e_{c,L}(p)-e_c^{[J]}(p)
 \le {v^2\over2}c^\alpha {|p|^{\alpha+2}\over E(p)}
 \le {c^\alpha\over2v^\alpha}E(p)^r,\quad p\in I_c.\ }
 \tag{26}
\]

The first correction is particularly simple:
\[
 e_c^{[1]}=E+c^2\,{v^2p^4\over8E},\qquad
 H_c^{[1]}=H_0+c^2d\Gamma\!\left({v^2p^4\over8E}\right).
 \tag{27}
\]
For J=1 the tail in (24) is at most \(3uz^2/8\), because its first
coefficient is u/8. Hence the constant \(1/(2v^4)\) in (26) improves to
\(3/(8v^4)\). These are global in-band bounds, not fixed-momentum expansions.

There is a separate direct algebraic check of the first correction and its
whole-band remainder, independent of the positive-series argument. With
\(w=\sqrt{1-z}\), one has
\[
 g(z)-z/4=\frac{z^2(3+w)}{4(1+w)^3},
\]
and rationalizing the difference of the two positive square roots gives
\[
 \Phi(z,u)-1-uz/8
 =\frac{uz^2}{\Phi(z,u)+1+uz/8}
       \left[\frac{3+w}{4(1+w)^3}-\frac{u}{64}\right].       \tag{27a}
\]
For \(0\le w\le1\), the first fraction in brackets decreases from
\(3/4\) to \(1/8\): its derivative is
\(-(4+w)/(2(1+w)^4)<0\). Thus the bracket is between \(7/64\) and
\(3/4\) for \(0\le u\le1\), and the denominator is at least two.
It follows directly that
\[
 0\le e_{c,L}-E-\frac{c^2v^2p^4}{8E}
       \le\frac{3v^2c^4p^6}{8E}
       \le\frac{3c^4}{8v^4}E^5,\qquad |p|\le1/c.          \tag{27b}
\]
This check includes the fold by continuity and uses no bounded derivative
of \(\sqrt{1-z}\) there. At fixed bounded p, (27a) also gives the next
coefficient \(v^2p^6/(16E)-v^4p^8/(128E^3)\), used in the even-state
critical-time control below. These are two arithmetic routes within this
same recovery context, not two independent reviewers.

Let \(H_c^{[J]}=d\Gamma(e_c^{[J]})\) on the full low Fock space, with its
maximal multiplication domain, and restrict to q_c when comparing actual
states. The outside-band positive multiplier in (25) is an explicit
mathematical extension; it is not an outside-band zero-energy Hamiltonian.
q_c strongly reduces it. On q_c the corrected and actual low free operators
have the same domain \(D(N)\) at every fixed c, and their powers have
domain \(D(N^r)\). Their one-particle energies are comparable as above.

The many-body remainder is
\(\mathcal R_c^{[J]}=d\Gamma(r_c^{[J]})\) on q_c. Pointwise in each
particle sector,
\(\sum_iE(p_i)^r\le(\sum_iE(p_i))^r\). Thus
\[
 \boxed{\ \|\mathcal R_c^{[J]}\psi\|
       \le L_J c^\alpha\|H_0^r\psi\|,\qquad
       L_J={1\over2v^\alpha},\quad
       \psi\in D(H_0^r)\cap q_c\mathcal F_L.\ }
 \tag{28}
\]
For J=1 take \(L_1=3/(8v^4)\).
This is a norm bound for commuting Fock multiplication operators, independent
of particle number; it is not obtained by squaring a noncommuting form order.

Finally set the effective generator
\[
 \boxed{\ \widetilde A_c^{[J]}=H_c^{[J]}+W_c.\ }
 \tag{29}
\]
Wc is exactly (13)/(15). It is bounded selfadjoint with norm at most K,
so (29) is selfadjoint on \(D(H_c^{[J]})\). It leaves q_c invariant.
Neither the cell/frame error in Wc nor its high-vacuum contractions have
been silently removed.

For completeness Wc has uniform iterated commutators also with the corrected
free operator. On the actual two-branch carrier use the hybrid free generator
with low energy \(e_c^{[J]}\) and the original high energy. Its coefficient
powers are bounded by the original powers in (8). Repeating (10) and
compressing its high vacuum proves the same M_r estimate for
\(\operatorname{ad}_{H_c^{[J]}}^r(W_c)\). Thus the domain bootstrap is also
available for bounded spectral windows of (29), although the main comparison
below uses the actual Gc window.

## 6. Full interacting-window comparison, with domains and high discard

Fix \(R\ge-K\) with
\[
 \Delta_R=\Lambda_c-K-R>0,\qquad
 F_R=\mathbf1_{[-K,R]}(G_c),\qquad
 \mathcal E_R=\operatorname{ran}F_R,\quad G_R=G_c|_{\mathcal E_R}.
\]
Use the block notation
\[
 G_c=\begin{pmatrix}A_c&B_c^*\\B_c&C_c^{\rm high}\end{pmatrix},
 \qquad C_c^{\rm high}\ge\Lambda_c-K.
 \tag{30}
\]
The high block is not the cell map \(C_c\).
Let \(I_R\) include the Gc spectral space, and put
\(Y=QI_R\), \(X=PI_R\). Spectral vectors belong to D(Gc)=D(Hc);
P and Q preserve that free domain. Therefore
\[
 C_c^{\rm high}Y-YG_R=-B_cX
\]
is a well-defined bounded graph identity. Integrating the derivative of
\(e^{-sC_c^{\rm high}}Ye^{sG_R}\) gives
\[
 Y=-\int_0^\infty e^{-sC_c^{\rm high}}B_cX e^{sG_R}\,ds,\qquad
 \boxed{\ \|QF_R\|\le\delta_R:={\beta_c\over\Delta_R}.\ }
 \tag{31}
\]
The integral converges in norm because its integrand is at most
\(\beta_ce^{-s\Delta_R}\). The initial Y already maps into the high domain,
with bounded high graph norm by the block equation, so the differentiation
has no unproved \(C_c^{\rm high}B_c\) product at zero.
Equivalently one can truncate at positive s and use the closedness argument
reconstructed in permitted D section 2. This is the old separation mechanism
at a Gc window, not a new independent low-block theorem.

The actual smooth-domain bootstrap is what makes the kinetic step possible:
\[
 \|H_0^r P F_R\|\le\|H_c^rF_R\|\le C_r(R).
 \tag{32}
\]
The first inequality is again between commuting free multipliers before
application to \(F_R\), not an assumed commutation with Gc.

The exact projected defect is
\[
 XG_R-\widetilde A_c^{[J]}X
       =B_c^*Y+\mathcal R_c^{[J]}X .
 \tag{33}
\]
Its norm is at most
\[
 D_R(c):={\beta_c^2\over\Delta_R}
                  +L_Jc^\alpha C_r(R).
 \tag{34}
\]
All compositions in (33) are defined: (32) controls the remainder and X maps
into the common low operator domain. Equation (33) also gives a bounded
graph norm for X into \(D(\widetilde A_c^{[J]})\).

Strong differentiation of
\(e^{-i(t-s)\widetilde A_c^{[J]}}X e^{-isG_R}\) is therefore legitimate,
and for either sign of time yields
\[
 \|P e^{-itG_c}F_R-e^{-it\widetilde A_c^{[J]}}P F_R\|
       \le |t|D_R(c).
 \tag{35}
\]
This comparison does not presume that \(PF_R\) lies in a spectral window of
Ac or of the effective generator. Its right-hand source space is the actual
interacting Gc window throughout.

Let \(\rho_c=F_R\rho_cF_R\) be any normal density. Write
\(\rho_c(t)=e^{-itG_c}\rho_ce^{itG_c}\) and
\(U_J(t)=e^{-it\widetilde A_c^{[J]}}\).
Then the full placed trace-distance bound is
\[
 \boxed{
 \sup_{|t|\le T}
 \|\rho_c(t)-[U_J(t)\tau_cU_J(t)^*]\otimes
                  |\Omega_H\rangle\langle\Omega_H|\|_1
 \le\min\{2,\ 2\delta_R+\delta_R^2+2T D_R(c)\}.
 \ }
 \tag{36}
\]

Here are the high-discard and trace constants explicitly. Window invariance
gives \(q_t=\operatorname{Tr}Q\rho_c(t)\le\delta_R^2\).
The Hilbert-Schmidt factorization of
\(\rho-P\rho P=Q\rho+P\rho Q\) gives
\(\|\rho-P\rho P\|_1\le2\sqrt{\operatorname{Tr}Q\rho}\).
The two low Hilbert-Schmidt columns
\(P e^{-itG_c}\rho_c^{1/2}\) and \(U_J(t)P\rho_c^{1/2}\)
differ by at most \(TD_R(c)\) and each has norm at most one.
Their density difference is therefore at most \(2TD_R(c)\).
Finally,
\(\tau_c-\operatorname{Tr}_H(P\rho_cP)
 =\operatorname{Tr}_H(Q\rho_cQ)\ge0\), with trace \(q_0\).
The cross terms have zero high partial trace. This last replacement costs
at most \(\delta_R^2\). Adding these three terms proves (36).
No trace of an unbounded Hamiltonian product is taken.

In particular, for the requested first correction the resource in (36) is
\[
 2\delta_R+\delta_R^2+
 2T\left[\frac{\beta_c^2}{\Lambda_c-K-R}
                    +\frac{3c^4}{8v^4}C_5(R)\right],
 \qquad \delta_R=\frac{\beta_c}{\Lambda_c-K-R}.            \tag{36a}
\]
Fixed \(H^4\) input data supply all four commutators needed for \(C_5\).
For a growing interacting window the factor \(C_5(R)\), rather than just
\(c^4\), remains part of the time resource.

For a chosen finite J, inputs in \(H^\alpha=H^{2J+2}\) suffice for all
commutators needed in (19) with \(r=\alpha+1\), and give
\(\beta_c=o(c^\alpha)\). Fixed R has \(\Delta_R^{-1}=O(c)\).
Consequently (36) tends to zero uniformly for
\[
 \boxed{\ T_c=o(c^{-(2J+2)}).\ }
 \tag{37}
\]
The leading proved kinetic contribution is \(O(T_cc^{2J+2})\).
Fixed smooth compact inputs permit every fixed finite J, with constants
depending on J and their corresponding Sobolev norms. This is not a single
bound uniform in J or an assertion for exponentially growing times.

If the initial class is instead an included spectral window of the actual
compressed Ac, the permitted D section 2 estimate gives
\[
 \|e^{-itG_c}I_E-I_Ee^{-it(A_c|_E)}\|
       \le(2\beta_c+|t|\beta_c^2)/\Delta_R .
\]
Combining the Ac version of (19) with (28) and Duhamel adds
\(|t|L_Jc^\alpha C_r(R)\). The density bound is at most twice this vector
bound, capped by two. This is a separate low-supported initial class; the
two spectral windows must not be identified.

## 7. Extension to first interacting-energy caps

Assume only that the initial normal densities obey
\[
 \operatorname{Tr}\rho_c(G_c+K)\le\mathcal E,\qquad 0\le\mathcal E<\infty .
 \tag{38}
\]
The operator is nonnegative. This is a first interacting-energy cap, not
a bound on higher powers or a preparation near the ground.
The expectation in (38) means its nonnegative quadratic-form expectation,
equivalently the monotone spectral-truncation trace. It does not assume
that the density's range lies in \(D(G_c)\).

For \(R>-K\), the spectral tail outside \(F_R\) satisfies
\[
 q_R\le{\mathcal E\over R+K}.
\]
When \(q_R<1\), normalize the spectral corner to a density \(\rho_{c,R}\).
A purification projected onto \(F_R\) has overlap \(\sqrt{1-q_R}\) with
the original purification, giving
\(\|\rho_c-\rho_{c,R}\|_1\le2\sqrt{q_R}\).
Both comparison channels in (36)—actual unitary evolution, and high partial
trace followed by the low unitary and vacuum inclusion—contract trace distance.
Their two initial replacements therefore cost at most \(4\sqrt{q_R}\).
When \(q_R=1\), the cap by two is already sufficient. Thus
\[
 \boxed{
 \sup_{|t|\le T}\|\rho_c(t)-[U_J(t)\tau_cU_J(t)^*]\otimes
                 |\Omega_H\rangle\langle\Omega_H|\|_1
 \le \min\!\left\{2,\
 4\sqrt{\frac{\mathcal E}{R+K}}
 +2\delta_R+\delta_R^2
 +2T\left(\frac{\beta_c^2}{\Delta_R}
                         +L_Jc^\alpha C_r(R)\right)\right\}.
 \ }
 \tag{39}
\]
One still requires \(R<\Lambda_c-K\). The moment condition belongs to Gc,
and the cut is in Gc; no low-energy moment of the partial trace is invented.

This suffices for exactly the same qualitative time window (37).
For an explicit, non-optimal rate put
\[
 \varepsilon_c=(1+T_c)c^\alpha\longrightarrow0,\qquad
 R_c=\varepsilon_c^{-2/(2\alpha+3)} .
 \tag{40}
\]
Eventually \(R_c\ge0\), \(R_c+K>\mathcal E\), and
\[
 cR_c\le c^{3/(2\alpha+3)}\to0,
\]
because \(\varepsilon_c\ge c^\alpha\).
Hence \(\Delta_{R_c}\) is comparable to \(c^{-1}\).
Using \(C_r(R)\le C(1+R)^r\), \(r=\alpha+1\), the first and kinetic terms
of (39) are both \(O(\varepsilon_c^{1/(2\alpha+3)})\).
The remaining terms tend to zero faster under the sufficient H-alpha
regularity: \(\beta_c=o(c^\alpha)\) and \(T_c\le c^{-\alpha}\) eventually.
In particular,
\[
 \sup_{\rho_c\ {\rm satisfying}\ (38)}
 \sup_{|t|\le T_c}
 \|\rho_c(t)-[U_J(t)\tau_cU_J(t)^*]\otimes
                         |\Omega_H\rangle\langle\Omega_H|\|_1
 =O\!\left(((1+T_c)c^{2J+2})^{1/(4J+7)}\right)
 \tag{41}
\]
for fixed data and fixed cap, as long as \((1+T_c)c^{2J+2}\to0\).
This exponent comes from this elementary truncation/graph-norm argument;
it is not claimed optimal. For J=1 it is a one-eleventh power of
\((1+T_c)c^4\).

The low initial density \(\tau_c\) can vary with c and need not converge in
trace norm under (38). The conclusion is a comparison of the matching
placed/effective evolutions. It is neither trace-norm compactness nor a
physical state-selection theorem. No gap-smallness or ground uniqueness is
used.

## 8. Exact potential, all-low replacement, and the fixed V0 limit

The exact potential in (29) is Wc from (15). In particular it is neither a
chosen continuum polynomial nor the energy-dependent Schur self-energy.
The virtual high-block contribution is controlled separately by
\(\beta_c^2/\Delta_R\). For these fixed smooth ordinary-cell interactions
it is negligible on every fixed polynomial time interval after choosing
sufficient fixed regularity; a generic abstract coupling of size K would not
have that property.

Replacing Wc by \(V_c^L\) changes the effective unitary by at most
\(|t|\epsilon_c\) in operator norm and its density channel by at most
\(2|t|\epsilon_c\). The free part is unchanged, and the difference is bounded,
so no domain mapping by that difference is needed. With fixed smooth data
\(\epsilon_c\) is superalgebraically small, and with the sufficient
H-alpha data it is \(o(c^{2\alpha})\), already adequate for (37).
Thus an all-low polynomial is another justified finite-c effective potential,
with its explicit additional error. It still depends on c.

Let \(V_0\) be the same formally selfadjoint polynomial evaluated on the
unmodified target real inputs. The old independent S argument gives
\[
 \|W_c-V_0\|\le L_{\rm cell}(c)+B_2(c),\quad
 L_{\rm cell}(c)=\sum_\alpha|a_\alpha|\sum_j
 \|\ell_cf_{\alpha j}-f_{\alpha j}\|\prod_{k\ne j}\|f_{\alpha k}\|.
 \tag{42}
\]
The bounded norm is on the full unital low carrier. Therefore replacing Wc
by V0 in the full-low corrected generator adds at most
\[
 2T_c\,[L_{\rm cell}(c)+B_2(c)]
 \tag{43}
\]
to the density comparison. The V0 evolution may leave q_c; it is defined on
the full low space with the positive multiplier (25), so this is still a
legitimate bounded-perturbation Duhamel comparison.

The separate sufficient regularity \(f,xf\in H^3\) gives S's actual expansion
\[
 \ell_cf=f+cB_{\rm cell}\partial_xf+O_{L^2}(c^2),\qquad
 B_{\rm cell}=\operatorname{diag}(3/4,1/4).
\]
Fixed smooth compact functions satisfy this hypothesis. Polynomial
multilinearity, the formal symmetrization and the high-tail estimate give
\[
 W_c=V_0+cV_1+O_{\rm op}(c^2),
\]
\[
 V_1=\operatorname{Sym}
 \sum_\alpha a_\alpha\sum_j
 \left(\prod_{k<j}\gamma_L(f_{\alpha k})\right)
 \gamma_L(B_{\rm cell}\partial_xf_{\alpha j})
 \left(\prod_{k>j}\gamma_L(f_{\alpha k})\right).
 \tag{44}
\]
This formula specifies the first missing potential term; it is not a change
to the prescribed physical interaction. In general (43) is \(O(T_c\,c)\),
whereas the fixed-window kinetic contribution is \(O(T_c\,c^{2J+2})\).
It supplies a sufficient fixed-V0 window \(T_c=o(c^{-1})\)
under this norm argument, even when the kinetic part has been corrected.

The O(c) potential difference can be real, not just a loose upper bound.
For nonzero real \(\phi\in C_c^\infty\), use the actual quadratic
\[
 V_c={i\over2}[\gamma(J_cC_c(\phi e_1)),\gamma(J_cC_c(\phi e_2))].
\]
It is fixed, even, selfadjoint and physically local. S's checked covariance
calculation gives
\[
 \omega_L(W_c-V_0)
 =-{cv\over2}\int_{\mathbb R}{p^2\over E(p)}
                       |\widehat\phi(p)|^2\,dp+O(c^2).
 \tag{45}
\]
The integral is strictly positive, proving an operator-norm lower bound of
order c. Its sign is fixed by
\(2i(-3ip/4+ip/4)=p\) and
\(P_+(p)_{12}=(-vp+im)/(2E(p))\).
The actual high compression correction is superalgebraically small here.

An operator difference and its vacuum expectation do **not** by themselves
prove a density-evolution obstruction at time \(c^{-1}\).
A scalar phase is unobservable in a density; a perturbation generated by a
conjugacy can also behave better than the norm-Duhamel bound.
No universal critical-time theorem for replacing Wc by V0 is established
from (45). A particular cancellation or an additional explicit potential
correction requires its own analysis. The genuine kinetic critical-time
controls below are different and use relative phases.

## 9. Critical kinetic times: actual even-state controls

The sufficient little-o time windows cannot uniformly be enlarged to their
critical scale while retaining only the same J kinetic terms. The free case
\(V_c=0\) is already in the fixed even polynomial class. Here Wc, the virtual
self-energy and all high couplings vanish exactly.

For fixed bounded momentum sets, analyticity in (21) gives
\[
 c^{-\alpha}r_c^{[J]}(p)\longrightarrow
 b_J(p):=E(p)d_{J+1}\!\left({v^2p^2\over E(p)^2}\right)p^{2J+2}
 \tag{46}
\]
uniformly. One can see uniformity directly from (24) with J replaced by J+1:
on a fixed bounded momentum set the next remainder, divided by \(c^\alpha\),
is \(O(c^2)\). The limit is strictly positive for \(p\ne0\). In particular
\[
 b_0(p)={v^2p^4\over8E(p)},\qquad
 b_1(p)={v^2p^6\over16E(p)}
              -{v^4p^8\over128E(p)^3}>0\quad(p\ne0).
 \tag{47}
\]

Choose normalized positive-polarization low packets u,v with disjoint compact
momentum supports away from zero, in small intervals around p1,p2.
Their normalized two-particle wedge \(\chi=u\wedge v\) is in q_c for every
sufficiently small c. Its actual energy has a uniform bounded spectral support,
since \(e_{c,L}\le\sqrt2 E\). Take the even state
\[
 \psi=\sqrt{1-\theta}\,\Omega_L+\sqrt{\theta}\,\chi,
 \qquad 0<\theta\le1/2,
 \tag{48}
\]
with high vacuum. The two free evolutions commute as Fock multipliers.
At \(t_c=\tau c^{-\alpha}\), their overlap tends to
\[
 1-\theta+\theta
 \int |u(p)|^2|v(q)|^2e^{-i\tau[b_J(p)+b_J(q)]}\,dp\,dq.
 \tag{49}
\]
There is no fermionic factor missing: disjoint supports give this integral
for a normalized wedge and a symmetric multiplication operator.

Choose \(\tau=\pi/[b_J(p_1)+b_J(p_2)]\). By taking the two fixed packet
supports sufficiently narrow, the integral in (49) is within any prescribed
small positive tolerance of -1. The limiting modulus is then strictly less
than one, so the pure-density trace distance
\(2\sqrt{1-|\text{overlap}|^2}\) has a positive lower bound.
For \(\theta=1/2\) it can be made close to two.
This is an observable relative phase between the vacuum and an even
two-particle component, not a one-dimensional global phase.

The same control fits any strictly positive first energy cap by choosing a
fixed sufficiently small \(\theta>0\), since its mean energy is theta times
the bounded pair energy. Thus the critical-scale nonconvergence is present
both for a bounded actual interacting window (free in this example) and for
a first-energy cap.

For J=0 this is the \(c^{-2}\) kinetic scale. For J=1 it is \(c^{-4}\).
It does not prove failure for every interaction, every state, or every
effective generator. Adding the next finite term moves the remainder and
its test to a later scale; keeping the exact dispersion removes this kinetic
error altogether. No universal impossibility or physical-axiom necessity
is asserted.

## 10. Failed routes, scope controls and verification limits

The following distinctions are essential to the proof:

- A local Taylor expansion on a fixed momentum interval would not control
  all modes in an interacting spectral vector. Equation (24) is global on
  the complete physical band, and (19) supplies the needed high free moment.
- The fold derivatives are singular. The remainder proof uses positive
  coefficients and the finite boundary value, not a false uniform derivative
  bound at \(c|p|=1\).
- A small norm of V and equality of first operator domains do not supply
  bounded iterated commutators or higher-power domains. The cell estimate
  and norm-differentiable field flow prove those hypotheses explicitly.
- A generic free-energy growth estimate can introduce avoidable time factors.
  Actual interacting spectral-window invariance gives (19) uniformly in time.
- A mean first-energy cap is not a bound on \(H_c^r\). The normalized
  interacting spectral cut and both channel costs are retained in (39).
- The high-vacuum projection is not an interacting spectral projection.
  Equation (31) compares them; no window is silently transferred to Ac.
- Fixed smooth ordinary cells suppress the actual high block. Replacing it
  by a generic norm K would lose the required long-time control.
- Exact Wc, all-low \(V_c^L\), fixed V0 and a Schur correction are distinct
  operators. Their separate errors and domains are stated.
- The actual O(c) potential witness does not establish a density critical
  time. The free kinetic controls do establish their specified relative-phase
  failure and leave higher corrections available.

These are concrete bounded controls, not a complete No-Go Discipline packet.
There are no five independent attack families for a universal no-go, no N5
scientific runner certificate and no broad prior-cycle/queue search.
Positive counter-routes—higher finite order, exact dispersion, cancelling
potentials and suitable further potential corrections—remain available.
No global negative-packet PASS, novelty or route-exhaustion claim is made.

### No-Go Discipline Gate: partial narrowing only

- **N1.** The actual negative checks are the free relative-phase construction
  for a fixed finite kinetic truncation, and the inherited smooth quadratic
  compression norm witness for replacing Wc by V0. They attack different
  strengthened statements and are not five routes against one universal
  claim. Higher finite order and the exact kinetic multiplier are successful
  alternatives already preserved here. The five-family packet requirement
  remains unmet; no packet PASS is claimed.
- **N2.** No list of independent physical walls is claimed. Sobolev input
  hypotheses prove the commutators; those commutators prove the window graph
  bounds; the graph bounds control the remainder. These are a dependent
  proof chain, not three independent obstructions. The separate potential
  and kinetic error terms are algebraically identified, not evidence of
  independence of physical conditions.
- **N3.** The complete final argument was reread with fixed positive m,v,
  ordinary cells and target frame, actual full-Fock placement, formal
  selfadjointness/evenness, fixed polynomial complexity, total norm bound,
  input regularity, and actual interacting spectral or first-energy
  hypotheses explicit. The final phrase scan is bookkeeping only; it does
  not replace that domain/premise examination.
- **N4.** Ground (28)–(30) concerns a rough local potential failing free
  form-domain preservation; it only refutes omitting regularity from the
  higher-domain argument. S (42), reproduced in (45), concerns a potential
  operator-norm difference; it does not refute a density convergence time.
  Equations (46)–(49) concern a fixed kinetic truncation and actually compare
  its density phases. These are the exact residuals used here; no generic
  earlier campaign obstruction is imported.
- **N5.** Scalar identities are proved on the entire one-particle band.
  Their remainders are lifted by commuting multiplication to every finite
  particle sector and the maximal Fock domains. The critical-time witness
  is an even vacuum/two-particle superposition in that supplied carrier.
  No extensive per-site interaction, lattice-wide physical selection,
  arbitrary observable family, or higher-dimensional statement is tested.
  There is no N5 scientific execution certificate.
- **N6.** Keeping the exact dispersion, adding another finite kinetic term,
  retaining Wc, or explicitly correcting the potential changes the
  mathematical approximation without requiring a new physical axiom.
  None is ruled out. Specially cancelling polynomials can improve the
  displayed sufficient bounds.
- **N7.** A hostile reviewer should first ask whether the purported
  order-c potential defect is a scalar or an infinitesimal unitary
  conjugacy: either can invalidate an inference from norm size to a
  c-inverse density obstruction. That route is open, and no such obstruction
  is claimed. For the fixed kinetic truncation, exact or higher-order
  generators can remove the constructed phase defect; the counterexample
  says only that retaining exactly the stated terms does not ensure
  convergence at its critical scale for all permitted initial states.
- **N8.** The assignment excludes campaign checkpoints, queues and broad
  prior-cycle searches. None was opened. The permitted S and D notes already
  preserve higher corrections and exact spectral alternatives. Global
  search/novelty and negative-packet obligations remain uncompleted.

Every correction here approximates the supplied Hamiltonian in the supplied
current coordinates. It does not change a physical axiom, select m, v, the
interaction, the state or its preparation, establish current conservation of V,
construct an extensive interaction limit, or supply a higher-dimensional theory.
The main bounds apply to every normal density in the stated window or cap;
they do not require parity invariance or even-sector support. The interaction
is even, and the critical-time counterexample uses an even pure state.

The mathematical proof is ordinary analytic work. No numerical, symbolic or
formal scientific execution was run, and no model-diverse review or transitive
audit was performed. The recovered coefficient formula was checked by explicit
coefficient extraction and its finite alternating sum. The first corrected
remainder was also checked by the new rational identity (27a). The cell,
commutator, higher-domain, spectral separation, Duhamel and density steps were
checked with their actual domains, factor order and normalization. Hash and
text checks establish provenance only. Final-source independent review and
comparison with new candidates remain the supervisor's work; this recovery
does not prewrite their conclusions.

This worker fully read the assigned checkout AGENTS pointer and
SCIENCE_WORKFLOW, the freshness procedure, and the workhorse and no-go skills.
Their hashes agree with the prior procedure manifest. No Git fetch or standing
ai/execution AGENTS body read was performed under the task's Git prohibition.
The prior physics-loop/procedure manifest is retained as inherited provenance,
not relabeled a new complete read by this worker. The owner-selected
continuous-discovery, selective-check and milestone cadence remains unchanged.
No Git, runtime, checkout, publication, PR, audit, other-chat message,
delegation, campaign checkpoint, editable prompt, canonical repository source
or platform instruction was changed.

Only the assigned proof and recovery evidence directory were written. The
original recovered draft, prior receipts and input copies are preserved.
The checked final proof has a separate source seal before any new-candidate
comparison or scientific reporting to the supervisor. No prohibited new
root/Lean/campaign body was read. This is same-family, draft-exposed recovery;
source exclusion from new candidates does not establish model diversity.
The fixed campaign deadline remains 2026-10-13T16:42:30Z.

## Later source binding and current publication scope

The accepted 449-line source-exposed comparison has SHA-256
`a89c8915a2f1207aaee8fbef7273494126445d4e26fbda625d418f0557a83cb6`.
Its addendum preserves the root's sharper orthogonal-column constant, the
extra trace-norm premise for replacing the moving initial state, and the
limited formal scope. Exact ordinary root acceptances are
`CORRECTED_DISPERSION_ROOT_READ_ACCEPTANCE.json`
(`5169f32898d6f1c1a32f7ebf297215b73e75ef5c68e20a9bc09b32b0d1e34965`)
and `CORRECTED_DISPERSION_COMPARISON_ROOT_ACCEPTANCE.json`
(`b045c5a86bf619ae54cffc10288a1c7db6bd3c9bcc72a50c8d1b07fb5a1d4fba`).
Those later records do not alter any field in the older records or proof.

| Direct source | Role and boundary |
|---|---|
| [Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md), `763082a6…` | Actual symbols, current-coordinate placement and physical bands; its canonical claim remains `open_gate`. |
| [Local](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md), `b5a8394a…` | Real CAR normalization, free coefficient flow and even-spin interpretation. |
| [Ground](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md), `8454f1c8…` | Actual two-branch Fock carrier and rough-domain counterexample; no small-interaction ground-selection premise is imposed here. |
| Smooth-high independent, `c69d638e…` | Archived provisional smooth high-tail/off-block estimate; no invented canonical claim ID. |
| Low-block comparison, `10aa75b1…` | Archived provisional separated-block/domain mechanism; its distinct window classes and wording repairs remain explicit. |

The source packet records full hashes and exact archived bytes for every
listed input. The first three rows produce canonical dependency edges; the
last two are explicit archived provisional premises. The planned publication
parent PR9510 is branch lineage, not a mathematical premise of this theorem.

The companion explicit-potential note addresses the separate bounded
potential-identification obligation. Its use requires its own fixed-order
norm estimate and the same-kinetic Duhamel cost. It is not substituted into
the unchanged exact-compression theorem above. There is no order-uniform,
exponential-time, fixed uncorrected generator, fixed-preparation sharpness,
time-dependent interaction or physical model-selection conclusion.

Historical scalar and positive-series Lean executions certify only their
displayed ordered-field inequalities and nonnegative summable-series leaf.
The failed first import, successful later attempts, sources and axiom-output
logs remain archived. Neither those leaves nor the eight-order symbolic
diagnostic proves the analytic coefficient identification, domains, CAR
construction or dynamics. No scientific program was executed in this assembly.

The publication packet is
`.claude/science/physics-loops/toe-corrected-dynamics-20261013`.
Its [source recovery and scope](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/bd831ffb14c7d7f12bf1b8165596a0db85f838ef/.claude/science/physics-loops/toe-corrected-dynamics-20261013/SOURCE_RECOVERY.md)
binds the accepted source freeze, exact comparisons and root records.
The [identity-only runner](../scripts/corrected_dispersion_identity_2026_10_13.py) checks source bytes and
reconstruction only; it proves no coefficient, domain, commutator or
dynamical estimate. It has not been executed during publication preparation.
Root accepted the exact source assembly; the new publication wrappers,
tools and driver require separate review and actual execution receipts.
Original pending/false fields remain historical and unchanged. Current
stays `open_gate`; N1/N5 and broader no-go obligations remain pending.
No formal analytic, model-diverse, audit or retained status is conferred.


Review-loop integration note: dependencies are integrated through main 160abf2a01435d2afcc3561d25a592da0c0eb4a2 and this reviewed energy/dynamics batch. Original analytic arguments and historical evidence remain preserved. Live canonical parent hashes are refreshed with original bindings retained; earlier pending/main labels describe publication-time provenance and confer no audit authority. Any formatting-only transformations are explicitly recorded in the publication map.
