<!-- Original PR9797 source SHA256 96e58cecd87f372bc53c79bdf20c6319631713c6c2294694dc9f3ed7d145a698. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Native energetic limit on the particle-relative flat environment

Status: bounded-support. Supplied microscopic Hamiltonian and weak anisotropy remain conditional. No empirical identification.

Use periodic R×R four-layer coefficient K=-4 sum P-5 sum E, E=XX edge, P=ZZZZ plaquette; R>m+2, m>=3. S is an m×m square of column sites. K_S contains its (m-1)^2 internal plaquettes and 2m(m-1) internal edges. K_out contains terms wholly outside S; B contains remaining terms. Let Q_S project all internal plaquettes to+1. Every internal edge anticommutes with at least one internal plaquette for m>=3, including boundary edges (use a plaquette at one endpoint rather than the plaquette containing both endpoints). Hence Q_S E Q_S=0. On Q_S, K_S=-4(m-1)^2. Trial all X+ in S gives e_S<=-10m(m-1). Thus flat-sector energy above e_S >=D_m=6m²-2m-4.

Boundary terms: 4m crossing edges and 4m plaquettes intersecting S but not contained (total intersecting (m+1)^2 minus internal(m-1)^2=4m). Therefore ||B||<=36m. Let e be global ground. Product of separate ground states gives e<=e_S+e_out+||B||. Any flat state has <K>>=e+D_m-72m. No gap, clustering, phase identification or local vacuum state is assumed.

For general state with epsilon=<1-Q_S>, each internal E has QEQ=0. Decompose into Q and 1-Q: |<E>|<=2sqrt(epsilon)+epsilon. Since -4sumP>=-4(m-1)^2, <K_S>>=-4(m-1)^2-10m(m-1)[2sqrt(epsilon)+epsilon]. Therefore

<K>-e >= D_m-72m-10m(m-1)(2sqrt(epsilon)+epsilon).

For particle-background vector sum_i |i>psi_i, shift S to i+S and use conditional normalized states, epsilon_i. Hb/K expectation decomposes over i. Jensen sum p_i sqrt(eps_i)<=sqrt(sum p_i eps_i). Same lower bound holds with epsilon the particle-relative flat-patch failure probability. This does not assume a classical environment or factorization.

This coefficient theorem cannot automatically be transferred to the native heavy band at growing m,R using an extensive uncontrolled remainder. At height4 finite-order local expansion: Hb=scalar+Jlambda4K/128+ O(Jlambda5 R²). Existing growing-box R~lambda^-1 gives O(Jlambda³), below heavy excess O(Jlambda^2.5). Singleton heavy H=4J+Hb+JlambdaT+Jlambda²D2+O(Jlambda³), with lambdaT+lambda²D2>=-4lambda. Thus for actual near-ground heavy states in the exact odd physical-Z sector, <Hb>-Eg<=C Jlambda^2.5, so <K>-e<=C lambda^-1.5 plusO(lambda^-1) under same expansion/dressing. Combining bound yields that an almost surely flat particle-relative m-square cannot have m much larger than lambda^-3/4 (and within R~lambda^-1), since D_m asymptotic6m² and epsilon=o(1). This is an upper bound on a high-probability flat-environment radius, not a selected radius, lower bound or COM extent. Earlier proven guaranteed radiusq<3/8 remains weaker than this upper boundq<=3/4.


## Actual-state qualification
Restrict to a state supported in the actual isolated two-wall spectral cluster, in the odd physical-Z sector, whose energy is within O(Jlambda^(5/2)) of the odd-sector minimum. Apply the inherited local normal-form unitary and project/normalize in N2. Odd parity excludes the half-column block exactly; the dressed state is a singleton-background vector. The inherited cluster separation bounds projection leakage by O(lambda³). A low mean energy without spectral support is insufficient. The statement concerns this dressed particle-relative observable, not a bare spin measurement.

For R comparable to lambda^-1, the expansion of the vacuum block through order four has norm error O(Jlambda5 R²)=O(Jlambda³). The previous heavy-band bound and positivity of lambda T+lambda²D2+4lambda imply <Hb>-min Hb=O(Jlambda^(5/2)). Consequently <K>-min K=O(lambda^-3/2). This is an expectation estimate and needs no internal vacuum spectral gap.

If epsilon(lambda) tends to zero and m>=3 with m+2<R, the exact cost inequality has positive leading coefficient 6m². Thus m=O(lambda^-3/4). In particular m asymptotic lambda^-q with q>3/4 cannot be almost surely flat. The earlier constructive correlation theorem guarantees joint flat patches only for q<3/8; the gap between these bounds is unresolved. Neither bound proves a preferred radius, a center-of-mass localization length, a universal scalar profile or an observed coupling.

## Check scope
The replay checks crossing counts and anticommutation on nonaliased periodic grids for m=3,...,20, exact D_m, and an independent dense three-by-three local spectrum/control. The general proof is the operator decomposition above, not extrapolation of that finite enumeration. All inputs and outputs are exposed model development. Native interactions alone supply the cost; no phenomenological surface tension is added.


## Native kinetic/environment balance

Let delta=<T+4>, F<=8delta, and S_d<=2F+2|d|1²delta for normalized dressed singleton-background state. For each internal edge e of relative m-square select an internal plaquette p(e) intersecting exactly one endpoint; its anchor has |d|1<=2m. The operators E_e and P_p anticommute. In any conditional normalized background state, |<E_e>|<=2sqrt(p_bad), by <E>²+<P>²<=1 and p_bad=(1-<P>)/2. Jensen across particle positions gives averaged |<E_e>|<=2sqrt((16+8m²)delta). All conditional offsets use the same relative patch and no factorization is assumed.

Repeating the energy cut with this edge bound rather than the joint-flat projector yields

<K>-e >= 6m²-74m-4 -20m(m-1)sqrt((16+8m²)delta).

For m>=3, sqrt(16+8m²)<=sqrt10 m. Choose a=1/(20sqrt10), m=min(floor(a/sqrtdelta),floor(R/4)), delta=0 interpreted as second choice. Then m sqrtdelta<=a. For m>=32 the cost is >=5m²-74m-4>=2m². Existing upperdelta=O(lambda1.5) implies m diverges. For unsaturated choice, m>=a/(2sqrtdelta), so cost>=a²/(2delta)=1/(8000delta).

Use actual isolated odd-heavy states, R comparablelambda^-1, and inherited energy upper gap4J-4Jlambda+CJlambda2.5. The local normal-form transfer errors are O(Jlambda³). Define excessD=Eheavy-Eg-4J+4Jlambda. Positivity/form bound gives

D/J >= lambda(1-lambda)delta + lambda4/(128)(<K>-e) - C lambda³.

The saturated choice m=floor(R/4) has cost>=R²/32 for largeR and gives D/J>=c lambda²-C lambda³, contradicting D/J<=C lambda2.5 at sufficiently smalllambda. Thus saturation is impossible for the stated near-minimizers. In the unsaturated branch,

D/J >= lambda(1-lambda)delta + lambda4/(1024000delta)-C lambda³.

AMGM yields D/J >= [2sqrt(1-lambda)/sqrt1024000]lambda2.5-C lambda³. Thus the actual odd-heavy minimum obeys

Eheavy-Eg=4J-4Jlambda+Theta(Jlambda2.5).

The two positive terms and the existing upper imply delta=Theta(lambda1.5), and <Hb>-minHb=Theta(Jlambda2.5) (upper already proved, lowercostnow). The length delta^-1/2 is Theta(lambda^-3/4), a defined kinetic/transport scale, not an identified sharp flat radius or COM localization length. Joint-flat guarantee still q<3/8; high-probabilityflat upperq<=3/4 remains. No coefficient, shape, relativistic scalar or empirical scale is derived.


Prior-art context: White and Affleck, On the Nagaoka polaron in the t-J model, https://arxiv.org/abs/cond-mat/0011098, discusses the known kinetic/environment size balance in a different Hamiltonian. That mechanism is not claimed as new. No t-J interaction, numerical radius coefficient or empirical value is imported here; the native bounds above are independently derived.
