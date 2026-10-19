> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Distinct check: installed free-energy moment accounting

**Disposition: SUPPORT for the accounting identities and norm-compatible mean balance, with one narrow wording correction required for literal universal reading.** The sentence “The actual energetic reference is not exactly beta(t)” must be qualified. Exact equality is not guaranteed; it is not universally excluded. At t=0 the actual reference is exactly beta. For p unequal to q and sufficiently small comparison error, the proved mean balance does exclude equality, as quantified below. No other mathematical defect was found.

## Exact source, reused premises and exposure

Fully read `active_energy_moment_accounting/PROPOSAL.md`, SHA256 `4bd84f3b86e74792724649bf355152d9eeb58f45d595a5f25b513c9b7fb86627`, under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The installed apparatus and complete input/target are the unchanged previously fully checked sources:

- `active_energy_loader_interface/PROPOSAL.md`, `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570`, with my review `ebf747aa6327d0c240054d21eacf14c6b28aeae2fa9967d55101b9c25ce599a6`.
- `cubic_reference_resolvent/PROPOSAL.md`, `7708b10262cd4061592751c9ec1a69cd473ee053ed06645319db6661a1d6b895`, with my review `25f290e96014dd8622575c207fd66f125ae2160727ca7d0b7a7bf35b7c3de3b5`.

Their exact source identities were refreshed in the immediately preceding task, and their needed commutation and full-output premises are reused here. ROOT authored the new note and exposed its intended accounting interpretation. I share the campaign's earlier gauge/clock ancestry and checked the two prerequisites. This is a distinct algebraic reconstruction of the new moment statements, not a fresh independent check of the apparatus or a retained audit. No scientific program was needed.

## 1. Exact installed conservation

Let K=sum_B n_B and Z=n_P, so H_E=omega(K+Z). The actual terms obey the claimed conservation separately:

- P-corner exchange interchanges |10> and |01> and preserves n_P+n_corner.
- Reference swaps preserve the sum of the two equal-gap occupations.
- X_Q acts on the freely degenerate Q; Z_Q,Z_P and Z_Q Z_P commute with n_P.
- Physical P-dependent suffix diamond contacts are diagonal on P. The path mixers and head-only onsite/cable blocks do not act on energetic qubits, and final R contacts act on freely degenerate R.
- Positive identity shifts and free occupation terms commute as well.

Consequently [H_tot,H_E]=0 on the complete physical space, not just on the one-head reduction or the symmetric reference sector. Every spectral projector of finite-dimensional H_E commutes with its evolution. Hence the entire actual H_E distribution and all its moments are conserved. This does not identify H_E with H_tot or with an arbitrary active-environment Hamiltonian.

## 2. Initial moments, including correlated data inputs

The energetic reference is initially the product beta=|+>^N, independent of the whole data/passive-reference input. Therefore measurement of K has binomial(N,1/2) distribution, with

 E K=N/2,    E K^2=N^2/4+N/4.

The data occupation Z is a projector. With p=E Z, E Z^2=p and Var Z=p(1-p), regardless of coherences or correlations with Q, path or passive reference. Initial independence gives E KZ=(N/2)p. Expansion yields

 E H_E=omega(N/2+p),
 E H_E^2=omega^2[N^2/4+N/4+(N+1)p],
 Var H_E=omega^2[N/4+p(1-p)].

These are actual values at every time by conservation. No subsequent independence of the actual reference and data is assumed. This point is important: actual evolution may generate correlations, but the conserved total moments can still be calculated from the initial factorization.

## 3. Target moments and their differences

Write the target data unitary U_f=X_R C_P^(b) SWAP_QP. Since both suffix factors commute with n_P,

 U_f^* n_P U_f=SWAP_QP^* n_P SWAP_QP=n_Q.

Thus target P occupation is q=E_input n_Q, including arbitrarily entangled data inputs. The target reference beta(t) differs from beta only by occupation-diagonal free phases and has the same binomial distribution. It remains independent of the target data/passive-reference state because this is the specified complete comparison isometry. Common phases and head embedding do not affect H_E.

Replacing p by q in the three formulas is therefore exact for the normalized target. Subtraction gives

 actual minus target mean =omega(p-q),
 actual minus target second moment =omega^2(N+1)(p-q),
 actual minus target variance =omega^2[p(1-p)-q(1-q)].

Variance is computed from each state's own mean; it is not the variance of a difference observable. For the explicit input Q=1,P=0, p=0,q=1: the target total mean exceeds the conserved actual mean by omega and its second moment by omega^2(N+1). The variance difference happens to vanish for that example. These signs and factors agree with the source.

## 4. Actual reference balance and norm limits

For normalized complete pure states psi,V with ||psi-V||<=delta, the difference of any bounded expectation satisfies

 |<psi,A psi>-<V,A V>|<=2||A||delta.

Taking A=n_P, which has norm1 independent of N, gives |p_actual(t)-q|<=2delta. Conservation of the total mean then implies

 omega E_actual K=omega[N/2+p-p_actual(t)]
                 =omega[N/2+p-q]+e,
 |e|<=2omega delta.

This argument keeps every output and uses no closeness of an unbounded-size energy operator. It controls the order-one reference energy exchange even when the apparatus grows. The formula also follows for mixed inputs from the complete channel/purified comparison: occupation expectations are linear, and the variance formulas follow after evaluating the two moments. Linearity of variance itself is not needed or claimed.

The energy-operator continuity bound obtained directly from vector norm would instead involve ||H_E||=omega(N+1), and for the second moment ||H_E^2||=omega^2(N+1)^2. Thus a vanishing complete-vector error along a growing-N family does not imply vanishing energy-moment error. The source's explicit nonzero moment differences are compatible with its complete-output approximation. The target reference is a comparator, not an exact energy-return certificate.

### Necessary wording qualification

As written, “The actual energetic reference is not exactly beta(t)” reads as an unconditional statement. That is too strong. The actual supplied reference equals beta at time zero, and the argument does not exclude equality for every input with p=q or every possible time.

A valid replacement is: “The actual energetic reference is not guaranteed to equal beta(t). In particular, if p differs from q and delta<|p-q|/2, the mean balance rules out exact equality.” Indeed equality of the actual reference state with beta(t) would require its mean to equal omega N/2, whereas the displayed balance gives a mean difference of magnitude at least omega(|p-q|-2delta)>0. This correction preserves the intended energy-accounting point and all quantitative formulas. It is not a no-go theorem about reference return under other inputs, apparatus or times.

## Scope and work record

The conclusions concern the installed equal-gap free energy H_E and the specified independent energetic reference supply. They do not provide preparation, a thermal/ground-state certificate, a uniformly controlled growing-apparatus energy-moment target, capture, reset, repeated reuse or arbitrary H_PE transfer. The example demonstrates a concrete mean-accounting difference, not a universal impossibility claim.

Only this REVIEW.md was created. No source, W/canonical file, Git state, checkpoint, physical axiom, editable prompt, model/effort or publication/audit status was changed. No numerical/symbolic scientific executable, sweep, external search or delegation was used. The proposed one-sentence qualification is reported without modifying the frozen source.
