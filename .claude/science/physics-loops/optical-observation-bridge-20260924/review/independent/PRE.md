# Independent PRE: reference energy, optical bands and the original local probe

Status: blind independent reconstruction before release of the new root candidate. This is a conditional mathematical check, not frontier authorship, a retained verdict, a new physical postulate or an empirical exclusion. No unreleased author or other active checker packet was opened. The exact four supplied parents are reused with their hypotheses; their transitive proofs are not recertified here.

The main conclusions are:

1. On an equal even-L cubic torus, the first nonzero **reference** one-particle energy is `2(hbar c/a) sin(pi/L)`. The three harmonic zero directions removed by the parent are not additional zero-frequency photons. Under the same conditional archival timing identification, a 1 eV excitation requires L greater than about `6.18e19` (MAGIC) or `7.23e20` (LHAASO v2 ML/MINOS). These are conditional lattice-site counts per side, not a full charged-sector spectral-gap theorem.
2. For an excitation restricted to reference energies at most `E_B`, put `xi=E_B a/(hbar c)`. The exact maximal weak-field selected-mark excess relative to its vacuum rate is twice a finite spectral-weight fraction. For `0<xi<=1`, this fraction is bounded by `xi^4/(24 v_L)`, uniformly in even L>=6. The vacuum variance `v_L` includes **all** reference modes; only the one-particle excitation is restricted to the low band.
3. A mean-energy bound is different. If its dimensionless ceiling is m, the weight fraction is at most `(1-L^-3)m/(3v_L)`. High-energy tails can achieve linear rather than fourth-power behavior. An exact finite-volume optimizer is given below. Substituting the hard-band bound into a mean-energy hypothesis is false.
4. These spectral identities and volume bounds do not make the parent's count-dynamics errors uniform in volume or certify finite-g laboratory behavior. At fixed graph they can be combined with the already-proved ordered, shrinking-window count theorem, with its original full generator and limitations.

## 1. Sources, permitted reuse and physical scope

All paths below are under `/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth`. Complete byte snapshots and origin pins accompany this PRE.

| Supplied source | SHA-256 | Use |
| --- | --- | --- |
| campaign-working/docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md | `651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf` | Quotient, real oscillator normalization, prepared-packet map and harmonic dispersion; main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. |
| photon-observation-publication/docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md | `acf74cfce461cfbf607f7ba2994ff0a3d5986b9571bf7c5efacecebdf9ab5d7b` | Part I timing conversion and its stated physical/source/cosmological limitations. |
| prepared-observation-publication/docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md | `14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b` | A.2 mode normalization; B's original physical J_- preparation, exact mark effect and full-process count bounds; C.2 preparation qualifications. |
| probe-physical-limits-publication/docs/PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md | `2dd49ffa004fa09726b2388decb7c4a36dd69f2cdaf5f3bbb8ffe3e829a47c6d` | Previously checked Part C only: normalized-packet ratios and common-clock scope. No A/B science is used. |

The weak-field note is a supplied fixed-volume prepared-packet construction. The current probe retains the original resolved formation mark and full compensated charged matter/field process after preparation. Its field reference is a way to specify initial vectors, not a claim that those charged states propagate with the old vacuum harmonic Hamiltonian. The allowed published preparation supplies the physical correlated strings and Gauss constraint; I do not replace them by an uncorrelated matter superposition. Its exact compressed mark effect is used as a conditional input, not re-enumerated in this PRE.

This check uses no new primary astronomical retrieval or data fit. The archival observations are imported exactly through the permitted photon parent. Source-dependent likelihoods and systematic/cosmological assumptions remain part of that conditional identification.

## 2. Reference Hilbert space, energy and Fourier normalization

Let L>=6 be even and V=L^3. The parent removes both gauge and constant harmonic link directions:

    S = (im B^T plus H_harmonic)^perp,
    dim S = 3V-(V-1)-3 = 2(V-1).

Here the reference is the zero electric-winding field sector. The three constant link directions are free compact directions before this restriction; they are not oscillators with creation operators at frequency zero. In particular, a normalized one-particle packet cannot put norm into a fictitious zero-energy photon to evade the bounds below. The actual J_- strings can change electric winding of the charged state; this does not change which *input reference* operator is being discussed.

Restoring the harmonic directions would require a separate global-rotor/winding-sector analysis. The plaquette curl annihilates those directions, so they contribute no d_r in (2.2). No statement below is a spectral-gap assertion covering such extra sectors.

Write `D_curl=C^T C` on S. Choose real orthonormal eigenvectors f_r with eigenvalues `s_r^2>0`. Define

    tau=a/c,  E_* = hbar/tau = hbar c/a,
    H_ref^exc = E_* sum_r s_r a_r^* a_r,
    |alpha> = sum_r alpha_r a_r^*|0>,  sum_r |alpha_r|^2=1,
    E_ref(alpha) = E_* sum_r s_r |alpha_r|^2.             (2.1)

The zero of (2.1) is the harmonic vacuum energy. This energy is neither the full charged Hamiltonian nor a reservoir heat variable. Without the physical identification, `s_r/tau` is just a reference frequency and E_* is a declared conversion.

For a fixed xy plaquette p with real curl row c_p,

    d_r = (c_p.f_r)/sqrt(2 s_r),
    X_p = sum_r d_r(a_r+a_r^*),
    v_L = sum_r d_r^2,
    chi = sum_r d_r alpha_r,
    eta = |chi|^2/v_L.                                  (2.2)

No factor of two is dropped from the oscillator vacuum variance. The two transverse polarizations are both included.

To evaluate (2.2), take unitary Fourier normalization `V^-1/2 exp(i k.x)`, with `k=2 pi n/L`, `n in (Z/LZ)^3`. Put

    q_mu=e^(i k_mu)-1, h_mu=|q_mu|,
    s(k)=sqrt(h_x^2+h_y^2+h_z^2).

At every k!=0 the curl has one gauge null direction and two transverse directions of eigenvalue s(k)^2. The xy row has symbol `(-q_y,q_x,0)`, up to unitary link/plaquette phase conventions. It annihilates the gradient direction and has squared norm `h_x^2+h_y^2`. Completeness in the transverse plane therefore gives the total local weight at k

    w_p(k) = (h_x^2+h_y^2)/(2 V s(k)),   k!=0.            (2.3)

Summing all nonzero complex momenta with two polarizations is equivalent to summing `2(V-1)` real oscillators. A non-self-conjugate k,-k pair is the unitary rewrite of real sine/cosine oscillators; there is no additional doubling. The self-conjugate Nyquist momenta on even L already carry their two real transverse directions once. Arbitrary complex one-particle coefficients in a real oscillator basis are allowed; no artificial reality constraint on alpha is imposed.

Cubic permutation symmetry, valid for the full grid and any energy ceiling depending only on s, yields

    v_L = (1/(3V)) sum_(k!=0) s(k),
    A_L := sum_r d_r^2/s_r = (V-1)/(3V),
    B_L := sum_r d_r^2/s_r^2 = (1/(3V)) sum_(k!=0) 1/s(k),
    sum_r s_r d_r^2 = ||c_p||^2/2 = 2.                  (2.4)

The last equality uses the four unit entries in the plaquette row. Each identity retains both polarizations. It also shows that the unrestricted maximally matched packet `d/sqrt(v_L)` has mean reference energy `(2/v_L)E_*`, of order the lattice energy scale, not an arbitrarily small energy.

Useful exact bounds, independent of L, are

    2 cot(pi/(2L))/(sqrt(3)L) <= v_L <= sqrt(6)/3,
    v_L >= v_* := (2+sqrt(3))/(3sqrt(3)) = 0.7182335... . (2.5)

For the upper bound, average `s^2=6` over the grid and use Cauchy-Schwarz. For the lower bound, `s >= (h_x+h_y+h_z)/sqrt(3)` and `sum_(n=0)^(L-1) sin(pi n/L)=cot(pi/(2L))`. Finally `x cot x` decreases on `0<x<=pi/12`, since `sin x cos x<x`; this makes L=6 the smallest displayed lower bound. These inequalities concern the full vacuum variance, even when the excitation occupies a narrow band.

## 3. Lowest nonzero reference energy and the conditional optical size

The minimum nonzero s occurs at the six axial momenta n=+-e_mu:

    s_0=2 sin(pi/L),
    E_gap^ref = 2 E_* sin(pi/L).                         (3.1)

There are twelve real transverse oscillators in this shell. Modes whose momentum is normal to the selected xy plaquette have zero local xy curl coupling, but they still have the positive energy (3.1). This distinction is useful below. The top reference frequency on even L is `s_max=2sqrt(3)`, at the corner momentum.

A normalized one-particle packet supported in energies at most E_o exists if and only if `E_gap^ref<=E_o`. The same feasibility threshold holds for a mean-energy ceiling E_o. At fixed actual a the condition is

    2 sin(pi/L) <= E_o/E_*.

Under the **same** photon/clock/length and archival timing identification, the parent gives

    E_QG,2(n)=sqrt(12) hbar c/[a sqrt(A4(n))],
    1/3<=A4<=1,
    a < 6 hbar c/E_QG,min,  E_* > E_QG,min/6.            (3.2)

The last bound is necessary for an unknown orientation; it is not sufficient for every orientation. Combining (3.1)–(3.2), existence of a reference excitation at or below E_o requires

    sin(pi/L) < 3 E_o/E_QG,min,
    L > pi/arcsin(3 E_o/E_QG,min),                       (3.3)

when the arcsin argument is below one. L must also be even and at least six. Equation (3.3) is a necessary restriction using the largest permitted a. A smaller actual a requires a larger graph. It is not a selection of a.

For an illustrative E_o=1 eV, using the exact printed benchmark values:

| Archival conditional benchmark | Necessary a upper bound (m) | Necessary L lower threshold | Corresponding V threshold |
| --- | --- | --- | --- |
| MAGIC Table 6 with systematics, `5.9e10 GeV` | `2.0067151e-26` | `6.1784656e19` | `2.3585326e59` |
| LHAASO v2 ML/MINOS, `6.9e11 GeV` | `1.7158868e-27` | `7.2256631e20` | `3.7725337e62` |

These rounded thresholds scale essentially as E_o^-1 and E_o^-3; the exact dependence is (3.3). The controls also retain 2 eV and 3 eV examples. They do not assert a statistically sharper benchmark than the parent. In particular, the supplied `6.9e11 GeV` table entry is used rather than recomputing it from the separately rounded eta endpoint, or substituting the calibrated/CCF variants.

The corresponding physical box condition is transparent. With `ell=L a`,

    E_gap^ref = (h c/ell) [sin(pi/L)/(pi/L)],
    1-pi^2/(6L^2) <= sin(pi/L)/(pi/L) <= 1.              (3.4)

Thus the physical side needed at the first mode is approximately the photon wavelength `h c/E_o`, about `1.239842e-6 m` at 1 eV; the vast L count comes from imposing a tiny spacing on that side. Formula (3.4), rather than an uncontrolled continuum substitution, gives the finite-L correction. The 1 eV value is an illustrative energy, not a fitted detector datum.

Conversely, under the same LHAASO identification, the reference gaps on L=6 and L=16 exceed respectively `1.15e20 eV` and `4.4870774e19 eV`. These are statements about reference excitations on those finite tori. They do not exclude lower excitations of the actual charged Hamiltonian, different states, larger graphs, or other physical identifications.

The fully matched packet that approaches the unrestricted ratio three has reference mean `(2/v_L)E_* > E_QG,min/(3v_L) >= E_QG,min/sqrt(6)`. Thus its attainability in the unrestricted finite packet class does not establish attainability by an optical-energy packet under this additional identification.

## 4. Exact hard-band optimum and a finite-volume fourth-power bound

The selected resolved mark and supplied physical preparation obey the parent's exact compression

    J_-^* B_j^* B_j J_- = 1-Re W_p.

For the uncut harmonic reference, with `x=g^2 v_L/2`, the initial rates are

    r_0=kappa(1-exp(-x)),
    r_1-r_0=kappa g^2 exp(-x)|chi|^2,
    r_1/r_0=1+2 eta x/(exp(x)-1).                        (4.1)

For normalized compact initial packets, the parent supplies exponentially small absolute cutoff errors at fixed L. Since `r_0~kappa g^2 v_L/2` and v_L>0, the weak-field limit is `1+2 eta`. Throughout this PRE, “contrast” means the excess relative to the vacuum rate, `C=(r_1-r_0)/r_0`, whose limiting value is `2 eta`; the total ratio is `1+C`.

Restrict the normalized excitation to `s_r<=xi`, where `xi=E_B/E_*`. Let P_xi be this one-particle spectral projector and define

    v_L(xi) = ||P_xi d||^2
            = sum_(s(k)<=xi) w_p(k)
            = (1/(3V)) sum_(0<s(k)<=xi) s(k).            (4.2)

If `xi<s_0`, the class of normalized packets is empty: no maximal excitation ratio is defined. A zero projector weight is not a realizable normalized excitation with ratio one. If `xi>=s_0`, Cauchy-Schwarz gives the **exact** optimum

    max |chi|^2 = v_L(xi),
    eta_band,max = v_L(xi)/v_L,
    alpha_opt=P_xi d/sqrt(v_L(xi)).                      (4.3)

The supremum in (4.1) at each g is obtained by the same reference packet. The compact-state limit has the corresponding value. At the first shell `v_L(s_0)=2s_0/V`; at `xi>=2sqrt(3)` the full bright packet is permitted and eta=1. An additional direction or polarization restriction can only reduce (4.3).

Here is a uniform finite-volume bound that does not assume a continuum mode density. Represent each momentum by `n_mu in [-L/2,L/2)`. If `s(k)<=xi<2`, then

    |n_mu| <= (L/pi) arcsin(xi/2).

Therefore

    v_L(xi) <= xi/(3L^3)
        { [2 floor((L/pi) arcsin(xi/2))+1]^3 -1 }.        (4.4)

For `0<xi<=1`, convexity gives `arcsin(xi/2)<=pi xi/6`. If the band is nonempty, `xi>=2sin(pi/L)>=6/L`, by the sine chord on `[0,pi/6]`. Hence

    v_L(xi) <= (xi/3)(xi/3+1/L)^3 <= xi^4/24,
    eta_band,max <= xi^4/(24v_L) <= xi^4/(24v_*),
    C_band,max <= xi^4/(12v_*).                          (4.5)

The spectral-weight inequality also holds for an empty band, but then the maximum language in (4.5) is inapplicable. This handles the sparse first shells without replacing the sum by an integral.

### Controlled continuum comparison of the static sum

For a sharper comparison when many modes lie in the band, let `delta_L=sqrt(3)pi/L`, the largest distance to the center of a Fourier grid cell. The periodic function s(k) is 1-Lipschitz. Suppose `0<delta_L<xi` and `xi+delta_L<2`. Put

    r=xi-delta_L,  R=2arcsin((xi+delta_L)/2).

A direct cell comparison gives the explicit enclosure

    max(0, r^4-r^6/36-(4/3)delta_L r^3)/(24pi^2)
       <= v_L(xi)
       <= [R^4+(4/3)delta_L R^3]/(24pi^2).               (4.6)

Proof: multiply the sum in (4.2) by the cell volume `(2pi/L)^3`. The eligible cells lie in `s(x)<=xi+delta_L`, with center value at most `s(x)+delta_L`. This domain lies in the Euclidean ball of radius R: each `|x_mu|<=2arcsin((xi+delta_L)/2)` and `|x_mu|/h_mu` is at most its value at that endpoint. Also `s(x)<=|x|`, so the upper integral is at most `pi R^4+(4pi/3)delta_L R^3`.

For the lower bound, every x in the ball `|x|<=r` has an eligible nearest grid center. Its center value is at least `s(x)-delta_L`. The sine remainder gives `s(x)>=|x|-|x|^3/24`. Integrating these terms over the r ball gives `pi r^4-pi r^6/36-(4pi/3)delta_L r^3`. Divide both bounds by `3(2pi)^3` and use positivity for a negative lower expression. The balls in the upper estimate lie inside the representative cube because R<pi.

In particular, for the **static** limit `xi->0`, `L xi->infinity`,

    v_L(xi)=xi^4/(24pi^2)[1+O(xi^2+1/(L xi))].           (4.7)

This is backed by the explicit enclosure, not a continuum density assumption. Define `v_infinity=(3(2pi)^3)^-1 integral s(k) d^3k`. The same Lipschitz-cell argument gives `|v_L-v_infinity|<=delta_L/3`, and v_infinity>0 by (2.5). Thus the sharp static weight fraction is `xi^4/(24pi^2 v_infinity)` to the indicated relative order. Formula (4.7) is not valid as a relative continuum approximation at a fixed first shell, where `L xi` stays bounded.

## 5. A mean-energy ceiling: bounds, exact optimum and surviving tails

Now require only `sum s_r |alpha_r|^2<=m`, equivalently `E_ref(alpha)<=m E_*`. This does not imply support in `s<=m`.

Weighted Cauchy-Schwarz and (2.4) give

    |chi|^2 <= (sum d_r^2/s_r)(sum s_r |alpha_r|^2)
             <= A_L m,
    eta <= min(1, A_L m/v_L)
         = min(1, (1-L^-3)m/(3v_L)).                    (5.1)

The class is empty for `m<s_0`. At `m=s_0` it is exactly the lowest shell, so its optimum is `v_L(s_0)/v_L`, not generally the looser bound (5.1). The bound becomes unity once the unrestricted bright packet is feasible at mean `mu_b=2/v_L`, even though that packet has spectral support well above mu_b.

### Exact finite-volume mean-constrained maximum

There is also an explicit optimizer at every intermediate mean. Write M for the positive diagonal matrix with entries s_r. For `z>-s_0`, set

    A(z)=sum d_r^2/(s_r+z),
    B(z)=sum d_r^2/(s_r+z)^2,
    mu(z)= [sum s_r d_r^2/(s_r+z)^2]/B(z).

For `s_0<m<mu_b`, there is a unique z with `mu(z)=m`, and

    alpha_z=(M+z)^-1 d/sqrt(B(z)),
    eta_mean,max(m)=A(z)^2/[v_L B(z)]
                  =(m+z)A(z)/v_L.                      (5.2)

To prove the upper bound, use the positive matrix M+z:

    |d.alpha|^2 <= A(z) <alpha,(M+z)alpha>
                 <= A(z)(m+z).

The stated alpha_z attains equality and has the required mean. For existence/uniqueness, use probability weights proportional to `d_r^2/(s_r+z)^2`. Differentiation gives `mu'(z)=-2 Cov(s,(s+z)^-1)>0`, because the two functions are oppositely ordered and the local curl has positive weight at more than one frequency. The limits are s_0 as z decreases to -s_0 and mu_b as z tends to infinity. At the endpoints use the lowest-shell matched vector and the full bright vector. This proves the pure-state optimum without importing a semidefinite-optimization theorem.

### Why the fourth-power band law cannot follow from a mean bound

Let u be a normalized lowest-shell oscillator with momentum normal to the xy plaquette. Then `M u=s_0 u` and `d.u=0`. It is a positive-energy dark mode, not a removed harmonic zero mode. The full bright vector `beta=d/sqrt(v_L)` is orthogonal to u and has mean mu_b. For `s_0<=m<=mu_b`, define

    p=(m-s_0)/(mu_b-s_0),
    alpha=sqrt(1-p)u+sqrt(p)beta.

This is a normalized one-particle vector, with no vacuum admixture. The energy cross term vanishes since u is an eigenvector orthogonal to beta. Exactly,

    <M>_alpha=m,  eta_alpha=p.                          (5.3)

For large boxes with `s_0<<m<<1`, its contrast weight is of order m, not m^4. It has a small but nonzero high-energy tail. For example the independent finite check at L=64, m=.2 finds `eta=.0421826672`, whereas the exact hard-band optimum at ceiling .2 is only `7.6534063e-6`. The state satisfies a mean constraint and violates no band theorem: it is outside the band.

The linear coefficient in (5.1) is asymptotically sharp as well. Put `zeta=M^-1 d/sqrt(B_L)`, with mean `mu_zeta=A_L/B_L` and overlap squared `A_L^2/B_L`. Mix zeta with the same u, choosing weight `(m-s_0)/(mu_zeta-s_0)`. For feasible m its exact eta is

    eta_mix=(m-s_0) A_L^2/[v_L(A_L-s_0 B_L)].            (5.4)

The inverse moment B_L is uniformly bounded. With `M_L=L/2`, `H_M=sum_(j=1)^M 1/j`, the chord inequality `s(k)>=4|n|/L` and the cube-shell count `24j^2+2` give

    B_L <= [12 M_L(M_L+1)+2H_(M_L)]/(12L^2).            (5.5)

Thus `s_0 B_L/A_L->0`. Along the static limit `m->0`, `L m->infinity`, (5.4) divided by the upper bound `A_L m/v_L` tends to one. Consequently

    eta_mean,max(m) = m/(3v_infinity) [1+o(1)]          (5.6)

on that static regime. A mean-energy hypothesis supports a linear restriction, and generally no fourth-power replacement. Equations (5.2)–(5.4) also preserve the finite-volume gap edge that a simple O(m) bound would obscure.

## 6. Combining with the same conditional SI ceiling

From (3.2), for either an energy-band ceiling E_o or a mean reference-energy ceiling E_o,

    xi_or_m = E_o/E_* < 6 E_o/E_QG,min.                 (6.1)

When the respective normalized-state class is nonempty and the right side is at most one, the volume-uniform **limiting initial contrast** bounds therefore imply

    C_hard_band <= [6 E_o/E_QG,min]^4/(12v_*),
    C_mean_only <= 2[6 E_o/E_QG,min]/(3v_*).             (6.2)

At E_o=1 eV these upper expressions are respectively about `1.24e-77` and `9.44e-20` using MAGIC, or `6.63e-82` and `8.07e-21` using LHAASO v2 ML/MINOS. They are very different restrictions. The second class allows rare excitations at reference energies of order E_*; calling such a state “an optical-band photon” would erase the hypothesis distinction.

The high-energy tails here are states of the supplied harmonic reference. Assigning them the displayed formal energies does not establish that they are experimentally realized ultraviolet photons. Only the stipulated common energy/clock conversion is used.

The comparison assumes that the lattice spacing and physical clock constrained by the photon interpretation are the same ones used by this local prepared probe. The source parent also requires photon identification, the energy convention E=hbar omega, observed c, proper physical spacing, and the respective source/detector likelihood/systematics. The LHAASO conversion additionally uses the declared constant proper spacing/orientation and FLRW/redshift transport. No new likelihood, orientation marginalization, confidence guarantee or parameter selection is supplied here.

The exact h,c,e definitions are used only for arithmetic. The parent does not derive this physical identification. There is no inference from (6.2) to measured efficiency, observed dark counts, a detector no-go or empirical falsification.

## 7. What transfers to counts, and what does not

At each **fixed finite graph**, fixed parameters, packet class and physical J_- strings, the supplied parent retains `h=K D+delta H4` and every original channel. It proves, for `b=o(tau g^3)`,

    E_n N_j([0,b]) = kappa b g^2(q_n+o(1)),
    q_0=v_L/2, q_1=v_L/2+|chi|^2.

Its factorial estimate makes at-least-one probabilities have the same limiting ratio as these means. Thus at fixed L the hard-band or mean-constrained static optima bound those **limiting** count/probability ratios as well. This uses the imported full-generator theorem; it does not propagate the prepared field by H_ref after the charged preparation. Neither conservation of the reference band under the full Hamiltonian nor the removal of other labels is assumed.

For uniformity over normalized one-particle alpha at one fixed L, the reference span is finite dimensional. The cutoff-tail, initial graph-norm and small-mark-output estimates extend over its unit sphere by finite basis bounds. This is finite-dimensional uniformity with L-dependent constants, not a new thermodynamic bound. In particular, the purely spectral volume bounds (4.5), (4.6) and (5.1) do not control how the full graph's graph-norm constants, total channel norm or microscopic resources grow with L.

The parent's ordered microscopic statement first fixes the graph, g and positive observation window; takes the declared spin/register comparison and refines its grid; then may choose a diagonal making errors smaller than the desired scale before the weak-field/shrinking-window limit. Its bare microscopic initial rate is zero on P, so its time-zero derivative is not the effective rate used in (4.1). No exchange of these limits is inferred here.

Tiny spectral contrast especially requires care: an error `o(1)` at each fixed L need not be small relative to `v_L(xi)` along a changing-volume/low-band family. A result that resolves the O(xi^4) signal would need errors smaller than that signal, including preparation errors, cutoff errors, full dynamics, register errors and the physical clock identification. No finite-g numerical accuracy at optical parameters is established by the present bounds or controls. The time window remains sufficient, not a necessary detector bandwidth, and no fixed laboratory-duration theorem follows.

## 8. Independent finite controls, preserved correction and verification limits

`optical_band_controls.py` was written for this PRE without reading or executing an author or parent runner. It builds the full real integer curl at L=6 and compares its 430 positive oscillator directions against an independently coded Fourier sum. The 218 zero eigenvalues equal V+2, accounting for gauge and three harmonic directions. The maximum squared-frequency discrepancy is `1.25e-14`; local v differs by `1.11e-16`; the inverse-weight identity agrees to displayed floating precision. Three exact mean-optimizer profiles also agree between direct real and Fourier representations within `4.72e-16` in eta.

The retained payload contains seven spectral-volume rows, 56 hard-band rows, 17 explicit cell-enclosure rows, nine mean-optimizer primal/dual rows, three high-tail examples, six SI rows and four small-graph reference-gap rows, plus the direct-matrix record and its three optimizer comparisons. Every stored row was read. These are bounded finite checks, not proofs of the continuum, full dynamics or empirical identification. The analytic arguments above supply the quantifiers.

The first control run completed successfully but exposed a semantic reporting error: ten empty hard-band rows were marked `band_empty=true` while also reporting an `eta_max=0` and ratio one. A zero projected weight is correct; labeling it a realizable optimum over normalized states is not. The complete first script, result, stdout, stderr and receipt are preserved under `attempt01_before_empty_band_label_fix`. The current code uses null optima/ratios for an empty band and an explicit feasibility flag. A genuine second execution completed after this narrow correction. All other scientific fields are exactly equal between the two runs; the comparison record preserves this fact. There was no failed numerical assertion and no hidden discarded run.

Current script SHA-256: `56a189c0d7463c5cf6ae90a72209a0881e8a14d1a3b0100abe5b37f48b34cfb8`.
Current result/stdout SHA-256: `740c8d9cd1e04e58d097d3718ba657cd2768ea6499c97313fdc30bcb23234c57`.
The two own wrapper durations were approximately .2303 s and .2259 s, exit zero with empty stderr. No inherited primary or author control ran. Floating spectra and inequalities are corroboration, not interval enclosures; the SI values are rounded high-precision arithmetic, not new observational precision. The source manifest and verification report bind all evidence and preserved history.

The conditional construction remains open on physical source preparation, stable matter, uptake/heat, realistic clocks, longer-time full-process evolution, simultaneous large-volume errors and empirical parameter selection. No new axiom, universal negative claim, publication action or audit-state mutation is made. This PRE stops before author disclosure.
