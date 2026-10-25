# J:derive:review-20261012-box-domain-interactions:a1 — interacting box-domain construction

Worker: Claude Sonnet 5.5, same family as the source workers. Unrefereed. Nothing in the repository was edited. Everything is in this folder; `check.py` is the executable record (56 PASS, 0 FAIL, about 30 s, about 120 MB).

**Read before concluding (stated as required):** `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 130 lines), on current main `a77a3449c91a753b06ce2a63876cd460b62cb4cf`. Also read in full: `C5_R8-1_report.md`, `C5_R8-1_referee_verdict.md`, `r81_common.py`, `r81_d2_lattice_algebra.py`, and the R7-1 report lines 60-175 plus the R7-6 report header and section 0 (overlap check).

## Plain language

The source (R8-1) built a two-body "Bakamjian-Thomas" law on a lattice whose one-body band is exactly relativistic inside a momentum box. It claims the full relativistic symmetry algebra closes exactly on a small set of smooth wavefunctions (a "common core") in 1+1 and 2+1 dimensions, and that boosting beyond the box leaks by a bounded amount.

What I did, in order of value:

1. I closed the commutator list. The 2+1 algebra has 15 relations, not 12. The d=2 runners tested 11 (plus an internal-spin check), so four were never tested. All 15 now close exactly (symbolic, not numerical), and the same method gives all 45 relations in 3+1 for the p-wave triplet channel. Each wrong variant (printed boost sign, wrong spin coefficient) fails on exactly the relations it should.
2. I checked the "chart" identities that tie the lattice operators to the Bakamjian-Thomas operators at 60 digits, with no grid and no finite differences, in d=2 and d=3. This exposed one defect for d=3. The lattice-native spin formula that works in d=2 is wrong by a helicity term in d=3, and I give the corrected form. Only P x S enters the boost, so the boost formula survives.
3. I proved what the common-core algebra does not give you. The boost restricted to the core is not essentially self-adjoint, with deficiency (1,1) per mass fibre. No bounded box of momenta is boost-invariant. Because the lattice Hamiltonian is bounded, the integrated boost relation cannot hold for large rapidity. This fixes the word "exponentiation" in the three-way distinction the task asks for.
4. I gave the safe rapidity range in closed form, with the worst case identified and the leg-in-box condition written as an explicit inequality.
5. For three bodies I derived the exact leftover when pair terms are simply added, checked it exactly in a solvable model, and showed that the model's lowest three-body mass depends on the total momentum. That excludes any boost that generates a local unitary group across P-intervals containing both P=0 and P=2.

What I did **not** do: a precision lattice closure of the interacting d=2 algebra. The source's direct lattice run (residuals 7e-3 to 0.35) is untouched, and none of my numbers replace it. My chart and fibre checks are identities of the chart and of the abstract fibre algebra.

## Setting and premises (every one is an assumption)

- A0 (ASSUMED). The axioms supply no dynamics: Admissibility "does not choose a Hamiltonian or transfer operator" (`MINIMAL_AXIOMS_2026-06-29.md:114-130`). Everything below is conditional on the lane's supplied model. Nothing here is derived from the four axioms.
- A1 (ASSUMED, imports). Graded CAR composition of site modes, continuous time, mass m>0, and the unit c=1. The approved `kinetic_isotropy_primitive` supplies only c_t=c_s (`PRIMITIVE_REGISTRY_CHECK.md:58-96`), not continuous time or a Hamiltonian. READING: c=1 is compatible with it.
- A2 (ASSUMED, lane-supplied). One-body box law s(k)=k on |k_a|≤B and a C^inf, non-quasi-analytic periodic continuation (`r81_common.py:25-33`; B=2.6 there). ε=sqrt(m^2+|s|^2).
- A3 (ASSUMED, lane-supplied). Mass operator M=M0+V with V=λ Σ_a |g_a><g_a|, a rotation-invariant odd multiplet g_a=q_a b(|q|^2), plus the plateau c(P)=1 for |P|≤Π1 (`C5_R8-1_report.md:56-60`).
- A4 (taken from R8-1, not re-proved). The Woodbury formula gives a C^inf kernel W(P;q',q) supported in supp g x supp g, and f(M)-f(M0) has the same support property (`C5_R8-1_report.md:104-108`, `referee_verdict.md:28-30`).
- A5 (taken from R8-1 plus referee corrections, used only in step 8). Theorem L: the leakage bound ||e^{-iηK}ψ - U_BT ψ|| ≤ 2||(1-E)ψ|| under the orbit condition (`C5_R8-1_report.md:232-243`; referee sharpening `referee_verdict.md:25-30`).
- Notation: 𝒟₂ is the common core of C_c^inf antisymmetric functions supported in {|P|<Π1, |q|<κ'} (`C5_R8-1_report.md:64`). X = i∂_P at fixed q; S = internal angular momentum of the pair in the canonical frame.

## Steps

1. **RETRIEVAL (CHECKED).** All six source objects at `02b443faa6d9a2331fb04d648c578c6b85e1900a` match their sha256 (`RECOVERY_STATUS.json`; `check.py` re-verifies them when the read-only checkout is present). No earlier derive attempt exists for this task id under `probes/work/derive`, and no open PR matched "box domain / Bakamjian / two-body box". I did not run `claim.py`, because it writes. The supervisor should check claim ownership.

2. **Counting (CHECKED, exact).** The 2+1 algebra has C(6,2)=15 pairs. `r81_d2_lattice_algebra.py:146-156` lists 11, and the chart runner has the same list (referee noted this at `referee_verdict.md:32-33`). Omitted: [Ky,Px], [J,Py], [Py,H], [Px,Py]. R8-1's "all 12 relations" (`report.md:28`) is 11 plus the check [S,M]. The omission was already known to the referee, so it is not a new defect, but step 3 closes it.

3. **Fibre closure (PROVED by reduction; CHECKED symbolically).**
   - *Statement.* Define H=sqrt(μ²+P²), P, J=X×P+S, K_a=½{H,X_a}+α(P×S)_a/(μ+H) with α=+1. The Lie brackets of these generators are as follows.
     - d=2 (S=s a real number): [Kx,Ky]=-iJ, [J,K_a]=iε_ab K_b, [J,P_a]=iε_ab P_b, [K_a,P_b]=iδ_ab H, [K_a,H]=iP_a, and [H,P]=[H,J]=[P,P]=0. This is all 15 relations.
     - d=3 (S su(2) matrices): the standard relations, all 45 pairs.
   - *Proof of the reduction.*
     - On 𝒟₂ with c=1, the BT generators are first-order differential operators in P whose coefficients are functions of P and of the commuting operators (M,S). M and S commute with P, X and each other (d=2).
     - Any commutator is again a first-order operator c0(P;M,S)+c^a(P;M,S)∂_a. If c0 and c^a vanish identically as functions of the parameters, they vanish by functional calculus, and Rψ=0 on 𝒟₂.
     - So it suffices to verify the identities with M→μ and S→s symbolic. `check.py` does this on plane-wave coefficients and reduces modulo H²=μ²+P² (sympy `rem`).
     - For d=3, S_a are su(2) generators commuting with M. Every commutator is at most quadratic in S, and an element of degree ≤2 in U(su(2)) that vanishes on spin 1 and spin 2 is zero (the traceless symmetric part and S_a are faithful on spin ≥1; the Casimir values 2 and 6 fix the scalar part). `check.py` verifies spin 1/2, 1 and 2.
   - *Exact results.*
     - d=2: all 15 close. [Kx,Ky]+iJ = i(1-α)s exactly, so the spin coefficient enters only [Kx,Ky]. α=2, α=0 and the flipped spin sign fail exactly {[Kx,Ky]}.
     - The printed R7-1 boost sign fails exactly {[H,K_a],[P_a,K_a],[Kx,Ky]}.
     - d=3: all 45 close for spin 1/2, 1, 2. Flipped or dropped spin term fails exactly the three [K_a,K_b].
   - *Scope.* This is the algebra of the chart/fibre operators on the core. It is not a lattice grid result and is not a statement about the full lattice Hilbert space.
   - Also CHECKED: ½{H,X}=H^{1/2} X H^{1/2} exactly in the fibre, because [H^{1/2},[H^{1/2},X]]=0 there.

4. **Chart identities at 60 digits (CHECKED, d=2 and d=3).** In the (P,k1) coordinates with half-density √Jq, with Jq=ωH0/(2ε1ε2) (the closed form also verified for d=3, and the chart round trip), the lattice free generators K0=Σ½{ε_i,X_i}, J0 (symmetrised lattice rotation) and the lattice-native X_NW=X_E-(P×S)/(H0(M0+H0)) equal the BT chart operators X=i∂_P|_q, S=-i q×∇_q, K=½{H0,X}+(P×S)/(M0+H0), J=X×P+S. Worst relative difference over 3 random points x 2 dimensions: 2.3e-60, using mpmath derivatives on an analytic complex test function, with no grid and no finite differences. Controls with the opposite spin sign differ at 1e-2.
   - **NEW (d=3 defect).** The direct d=3 analogue of R8-1's lattice-native spin, S=(H0/M0)(J0-X_E×P) (`report.md:130`, stated there for d=2), is not the chart S. It equals the transverse part correctly but multiplies the component along P by H0/M0. The corrected form is S=(H0/M0)(J0-X_E×P)-P(P·J0)/(M0(H0+M0)), checked at 60 digits. Since only P×S enters X_NW and K, `K` and `X_NW` are unaffected, and uncorrected S differs from chart S by 0.63 at the worst sampled point. R8-1 gave no d=3 spin formula (d=3 was "suggested, not checked", `report.md:279`).

5. **Lattice K in terms of H (PROVED, algebra on 𝒟₂ given steps 3-4).** The R8-1 form K=K0+½{cW,X_NW}+(P×½{S,cF}) with F=f(M)-f(M0), f=1/(M+H) (`report.md:134`) equals ½{H,X_NW}+(P×S)/(M+H) when c=1, because K0=½{H0,X_NW}+(P×S)/(M0+H0) (step 4), W=H-H0, and ½{S,F}=SF since [S,M]=0. Only the commutation of M and S with P, X_NW and each other is used.

6. **Common-core domain lemma (PROVED with an explicit inequality; CHECKED).**
   - *Lemma D (leg margin, any d).* If |P|≤Π, |q|≤κ, then each leg satisfies |k_i| ≤ κ + Π(½ + Πκ/(8m²)).
   - *Proof.* The inverse chart is k1=q+P[(P·q)/(M0(H0+M0))+ω/M0], and k2 is the same with q→-q. Here M0=2ω gives ω/M0=½. Also M0(H0+M0) ≥ 2M0² ≥ 8m², and |P·q| ≤ Πκ.
   - *Numbers.* For m=½, κ=0.8, Π1=0.6 the bound is 311/250=1.244, less than the flat region B=2.6; sampled supremum 1.139 in both d=2 and d=3. For κ=1, Π1=1 the bound is 2.0 (direct-run parameters).
   - *Leg capacity.* Taking b=2.6 and Π1=0.6, legs stay in the flat region for all internal masses up to μmax=2·sqrt(m²+κmax²)=4.0245, with κmax=115/59.
   - *Consequence.* Given A3-A4, 𝒟₂ is invariant under H, P, J, K and the 15 (45) relations hold on it. The invariance reasons are: W and F output |q|<κ at the same P; X, S and multiplications preserve supports; and no umklapp holds because |P|<Π1<π (this was a parameter choice in R8-1; here it is an explicit inequality).

7. **Three notions kept apart: Lie algebra on a core, global exponentiation, invariant box.**
   - (a) *Lie algebra on a common core.* Steps 3-6. Conditional on A1-A4.
   - (b) *Global self-adjoint K on the lattice.* R8-1 §3.3 with the referee's completion (`referee_verdict.md:22-23`). Not re-proved here. READING: consistent with (c) below, since this K lives on the larger space ℓ², not on a box sector.
   - (c) **No invariant box (PROVED).** Per mass fibre μ in d=1, K=½{H,i∂_P} is unitarily equivalent to i d/dθ with P=μ sinhθ (exact, checked). On the box sector this is the operator i d/dθ on the interval (-θ1,θ1) with θ1=asinh(Π1/μ).
     - Its adjoint has the L² solutions e^{∓θ} of K*u=∓iu, so the deficiency indices are (1,1) per fibre.
     - The boundary form on e^{θ} is -2i sinh(2θ1)≠0.
     - So K restricted to the core is symmetric but not essentially self-adjoint on L²(R'). In d=2 the same conclusion holds on each chord, with the explicit solution u=φ(Py)H^{-1/2}exp(∓θx+iΦ), which includes the spin term (symbolic check).
     - The boost orbit of any P leaves |P|<Π1 in finite rapidity asinh(Π1/μ)+asinh(P/μ), so no bounded box is boost-invariant. Self-adjoint extensions on the box therefore cannot implement the boost.
   - (d) **Bounded-H ceiling (PROVED, elementary).** On the lattice H is bounded. If the integrated relation e^{-iηK} H e^{iηK}=H coshη+P sinhη held for all η, then ⟨H⟩coshη+⟨P⟩sinhη ≤ ||H|| for all η. This is false because H>|P| strictly (m>0). So the continuum boost law can be followed only up to a finite η. For the free R8-1 box law, 2max ε=5.395, giving a ceiling η ≤ arccosh(5.395/0.85)=2.535 for a rest state of mass 0.85. (||W|| would raise Hmax slightly.) Theorem L's η* is far below this ceiling.

8. **Explicit finite-rapidity range (PROVED; CHECKED).** For a boost by rapidity s along unit n, H'=H coshs - (P·n) sinhs, and |Φ_s(P)|²=H'²-μ². Over the ball |P|≤ρ the maximum of H' at each s is attained at P=-ρn and equals μ cosh(r+s) with r=asinh(ρ/μ), because H' is increasing in |P| and linear in P·n. Hence the orbit stays in |P|<Π1 for all s<η*(ρ,μ)=asinh(Π1/μ)-asinh(ρ/μ), which is sharp. For a set Σ of internal masses take min over Σ. Together with Lemma D (κΣ=max(κ, sqrt(μmax²/4-m²))) and A5, the leakage bound 2||(1-E)ψ|| holds for η<min_Σ η*. In d=1 this reproduces R8-1's η*=0.367 (0.3674); `check.py` also checks the closed-form exit rapidity against direct boosts (d=2,3, 7200 sampled orbits, floating point). This is a corollary of the cited Theorem L, not an independent proof of it.

9. **Ordered-pair ½ normalisation (CHECKED, exact).** On 4 modes with Jordan-Wigner CAR and random rational exchange-symmetric kernels, the Fock operator ½ΣW a†a†aa equals Σ_{x<y} W^{(xy)} exactly in the N=2 and N=3 sectors (all matrix elements, Fractions). Prefactor ¼ does not. For a kernel odd in each pair index the Fock matrix element on normalised pair states is 2W(k',k), the origin of the spurious factor 2 attributed to the earlier referee in R8-1. The N=3 sector confirms the pairwise lift used in step 10.

10. **Three bodies: exact leftover and what is needed (PROVED derivation; CHECKED in a solvable model).**
    - *Derivation.* Let the pair lifts be K_ij=K0^{ij}+½{W_ij,X_ij} and H_ij=H0^{ij}+W_ij, with pair closure [K_ij,H_ij]=iP_ij, and let X_ij be the pair centre-of-energy position (fixed q), so [X_ij,W_kl]=i u_ij(W_kl) for the vector field u_ij=Σ_{a∈ij}(ε_a/H0^{ij})∂_a.
      - For the pairwise sum K=K0+Σ½{W_ij,X_ij}, H=H0+ΣW_ij, spectator terms commute, so [K,H]-iP = Σ_{(ij)≠(kl)}[½{W_ij,X_ij},W_kl].
      - When the W's are multiplication operators this equals C=Σ_{(ij)≠(kl)} i W_ij u_ij(W_kl).
      - Only pairs sharing a particle contribute.
    - *Check.* In the solvable model W_ij=sqrt(H0_ij²+a)-H0_ij (pair mass shift M²=M0²+a, a diagonal operator), the pair closure holds to 4e-174 and [K,H]-iP-Cf=0 to 1.6e-173 at 40 digits. |Cf|=3.6e-3, nonzero, and scales as a² (ratio 3.997 for a→a/2).
    - *Infimum-mass obstruction (CHECKED, floating-point global search).* In that model the lowest three-body invariant mass is 3.70820393 at P=0 (equal to 3+3(sqrt5-2)), 3.69857927 at P=2 and 3.68740219 at P=4. A boost generating a (local) unitary group across a P-interval containing 0 and 2 would map the mass-3.6986 level at P=2 to P=0, where it does not exist. So no such K exists for the pairwise H. SCOPE: this excludes local exponentiation, not a Lie-algebra-only K on a smaller domain (levels below the P=0 infimum are not constrained by it). R7-6's wording "no boost operator of any form" (`C5_R7-6_report.md:38`) therefore needs the integrability qualifier, at least in this solvable model.
    - *What is needed for cluster-separable closure (SUGGESTED, from the derivation).* Three-body terms (V3,Y3) such that H=H0+ΣW+V3, K=K0+Σ½{W,X}+Y3 satisfy [K,H]=iP, with [V3,P]=0, [Y3,P]=iV3, V3 and Y3 vanishing when any particle is removed far away, and (d≥2) also the [K_a,K_b] and rotation relations. At order a² this is the inhomogeneous equation [K0,V3]+[Y3,H0]=-C₂ for explicit C₂, and the same for [K,K]. The known solutions (BT three-body mass operator, Sokolov/Coester-Polyzou packing, R7-6 Prop. BT0) are imports (RECALLED/unverified here). Whether they preserve the common core on the lattice is R7-6's suggested item; I did not check it.

11. **d=3 requirements (CHECKED where stated).**
    - CHECKED: the fibre algebra (45 relations, spin 1/2, 1, 2); the free chart identity K0, J0, X_NW at 60 digits; the corrected spin formula (step 4); the Jacobian Jq=ωH0/(2ε1ε2) holds in d=3; the leg bound (step 6) is dimension-free and the sampled supremum agrees.
    - CHECKED (exact symbolic): the triplet kernel Σ_a g_a(q)g_a(q') is rotation invariant and odd, so [S,V]=0 and [S,M]=0 in d=2 and d=3 (the d=3 condition used in step 3).
    - NOT checked: the rank-3 Woodbury kernel for W in d=3, the d=3 lattice run, the d=3 leakage numerics, and the d=3 Ward/stress-tensor questions.

## What is new, and what is not

Not new: retrieval of R7-1/R8-1 results; the d=2 chart algebra at 6e-13; ½ versus ¼ at one level (R8-1 §4.1); the leakage statement (Theorem L); the omission of four commutators (already in the referee verdict); the existence of N≥3 cluster trouble (R7-1, R7-6, Keister-Polyzou as cited there).

New (all same-family, unrefereed):
- N1. The complete 15 (d=2) and 45 (d=3) Lie relations close exactly on the fibre algebra, with exact failure patterns for each wrong variant and the exact [Kx,Ky] residual i(1-α)s (step 3).
- N2. 60-digit grid-free chart identities in d=2 and d=3, and the d=3 helicity defect in the lattice-native spin (step 4).
- N3. Non-essential self-adjointness (deficiency (1,1) per fibre, explicit solutions in d=1 and d=2), no boost-invariant box, and the bounded-H ceiling (step 7).
- N4. Closed-form sharp η*(ρ,μ) in any d, with the explicit leg-capacity inequality (steps 6 and 8).
- N5. Exact pairwise-lift leftover C with an exactly checked solvable model, the P-dependent infimum mass, and the qualification of R7-6's "any boost" statement (step 10).
- N6. The N=3 sector check of the ½ prefactor (step 9).

## First unresolved step

**Step U (unresolved, not attempted to closure).** A direct lattice-native evaluation of the interacting d=2 relations with demonstrated convergence. Everything above shows that the chart/fibre algebra is exact and that the lattice free generators equal the chart ones; what is missing is a lattice computation of the interacting kernels W and F whose residuals decrease with L and the P-grid. R8-1's direct run stalls at 7e-3 to 0.35 because the relative-momentum torus does not resolve the form-factor shoulder (`C5_R8-1_report.md:258-272`). My 1e-60 numbers are analytic identities of the free part and cannot stand in for it.

Behind it:
- Step V. Three-body (V3,Y3) cluster-separable closure on the lattice box (step 10 states the equations; neither solved nor checked).
- Step W. d=3 interacting kernel and leakage (step 11).

## Honesty notes

- The infimum-mass search and the orbit sampling are floating-point; all other finite claims are exact (sympy, Fractions) or 40-60 digit mpmath.
- "PROVED" claims in steps 3, 5, 6, 7, 8 and 10 rest on A1-A5 and on standard facts (functional calculus, deficiency indices of i d/dθ on an interval).
- Spin-1/2, 1, 2 matrices and plane-wave coefficients are the test objects in step 3; the reduction argument is what turns them into an operator identity on 𝒟₂.
- No claim here changes any status, and none is a statement about the four axioms.
