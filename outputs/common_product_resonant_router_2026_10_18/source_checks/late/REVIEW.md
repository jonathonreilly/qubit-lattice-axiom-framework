# Late negative-gap half-line tails: distinct check

Disposition: SUPPORT for the abstract negative-gap bound and the two specified late physical interfaces. No required correction found. The low/high auxiliary split, full sequence norms, channel Jacobian, origin enumeration and fixed phases are supported. No complete finite budget or resource exponent is established.

## Evidence and exposure

Read the complete `common_product_resonant_late_tails/PROPOSAL.md` and verified SHA256 `a03139261c649546c00b7a15bef01c4a7387dfa6cc267f5c20e82f88b65f02d9`. Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

Reused the immediately preceding complete half-line read and check: source `43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1`, own review `1fa285544e38728389fb6bb9928b8bbd1e6a9612beb12cfde7532439b0935f9b`, refreshed here. Also reused the full reads of outgoing source `b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80` and its distinct review `0071e81532263d56c37690be97aa25e30ed56a7fa6c394dbfc9243a646e62d00`. Their pending labels in the new source are historical; neither is treated as an already proved late-tail theorem.

Exact packet `cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf` / own review `315a618f389598fe8443a8ed3cdf8c39180b65ba223c4de2a359be4e218ea916`, finite `532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123` / own review `5ef953f745c598888b329aa8fafa94d226a18f2cc01fa57f09b165e0e7a1a936`, and standalone launcher `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4` retain their complete recent reads and scoped phase/measure/geometry premises. The two concrete applications need only a constant injection and sqrt(q'), not a new matrix inverse proof.

ROOT proposed the late-gap and channel-measure route. The author wrote upstream packet/tail work; I checked the exposed preceding interfaces. This is same-model selective analytical verification, not blind replication or retained audit. Applicable previously read reviewer/workflow instructions are reused. Only this report was written; no source/W/Git/checkpoint/axiom/editable-prompt/model change, scientific executable, delegation or publication occurred.

## 1. Coefficient regularity and negative phase gap

The exact source pole representation gives auxiliary phase +vx for F, with prefactor rho/(pi A sqrt(p_chi))<=rho and amplitude chi(k(x)) exp(ik(x))k'(x)M(k(x)). The preceding checked cutoff/chain calculations apply unchanged: the specified quintic is W^{3,1}, continuous through its second derivative, and has the displayed derivative L1 ceilings. Ordered Leibniz therefore gives D_s/h^2 without dropping source phase, Jacobian or positive normalization. No arbitrary C2 or analytic cutoff is substituted.

In k coordinates, sin k>.99 and k_a'>=.99 give phase'<=-.99n-(1.98u-L)=-.99n-Q. Multiplication by k'(x)>=.999 preserves a negative bound. On 0<=v<=Q/2,

    (phi+vx)'<=-.98901n-.499Q<=-.23(n+Q).

Thus this split is tied to the actual negative gap Q, not simply to elapsed time. With L+u<=Cgap Q, the absolute first k derivative is <=2Cgap(n+Q). Orders two, three and four have bounds 2,3,10 times that same quantity. The atan chain yields 4,32,128 times Cgap(n+Q), as in (4). Adding vx changes no higher derivative. The real q'''' formula and safe <.04 ceiling were explicitly reconstructed in review1fa285; the loose bound10 suffices here.

## 2. Low-v whole-half-line estimate

Three integrations by parts have the seven coefficients 1,6,4,15,1,10,15 and the stated powers of the phase derivative. Substituting the preceding gap and higher-derivative ceilings gives exactly P_late/(h^2(n+Q)^3). The weak third derivative and vanishing compact-support traces justify these integrations across the quintic joins.

Integration over the low-v interval has length Q/2 and costs at most rho Q P_late/[2h^2(n+Q)^3]. The full endpoint-inclusive sum is

    sum_(n>=0)(n+Q)^-6<=Q^-6+Q^-5/5<=6/(5Q^5),

using Q>=1. Consequently the low sequence norm has coefficient sqrt(6/5)/2<1 multiplying rho P_late/(h^2 Q^(3/2)). This verifies the first term of (5) as an entire half-line/operator norm, not a pointwise estimate extrapolated to infinitely many sites.

## 3. High-v physical momentum measure

For fixed v return to k, then put p=k_a(k). The phase factors have unit modulus. The transformed Fourier coefficient divides by d_a=k_a', not its square root, because dk=dp/d_a. For every unit input vector its squared p-space norm is therefore

    integral |chi(k)|^2 ||M(k)xi||^2 / d_a(k) dk.

The map is monotone, d_a>=.99, and its compact image lies in a Fourier period; extension by zero is legitimate. This gives the bound 2h M0^2/.99. Full-integer Parseval applies with either Fourier-kernel sign, and restriction to n>=0 contracts it. The resulting vector estimate is uniform in xi and hence an operator norm estimate, also after tensoring passive references.

Minkowski is used on this COMPLETE sequence before integrating v>=Q/2. Since Ab=rho^2, the coefficient after auxiliary integration is at most

    2 sqrt(2/(.99pi)) M0 sqrt(h)/rho,

which is below 2M0 sqrt(h)/rho and therefore below the stated factor4. The exponential is exactly exp(-bQ/2)=exp[-rho^2 Q/(2(2-rho^2))]. For each fixed rho>0, the original double integral is absolutely bounded by the compact amplitude norm divided by b, so Fubini is justified. Uniform bounds are derived afterward. This proves the high contribution without using an incorrect unweighted k Parseval norm for the q channel.

## 4. Concrete incoming and nonpositive-F tails

For the actual late incoming packet, k_a=k, L=ell and M=V_0 give exactly its ordinary record0 incoming field. The injection has ceilings (1,0,0,0). In u in [3ell/4,7ell/8], Q>=.485ell and L+u<=1.875ell; Cgap=16 is safe and Q>=1 under the finite geometry's ell>=1000. Both I ports, their origins and arbitrary coherent input/reference data remain in this bound.

For the ideal F tail, substituting its physical radius m=-n with n>=0 covers EXACTLY all m<=0, including zero. The phase becomes -nq+(ell+57)k-ue(k), and M=-i sqrt(q') retains the fixed comparator phase. At ell>=1000,

    Q>=.485ell-57>=.428ell>=1,
    L+u<=1.875ell+57<=1.932ell<16Q.

The stated derivative formulas for sqrt(q') through order three are correct. The real bounds on q',q'',q''',q'''' give the sufficient ceilings (2,1,10,100); multiplication by -i changes no norm. Keeping this square-root factor inside M and then using the 1/q' measure in the high-v norm is consistent: for the ideal scalar coefficient these factors cancel exactly in the squared integral. The source's larger general coefficient bound remains valid.

The two separate origin estimates do not change the physical packet convention: its incoming and outgoing pieces add at a single physical origin, while the retained target starts at F radius1. No extra record time phase is introduced; E(k)=E_0(q)+kappa already fixes that energy convention. The physical exp(-ict), and any separately supplied exact common one-head scalar phase, have unit modulus and are retained in the compared fields.

## Scope

The abstract result assumes the stated coefficient derivatives and explicit Q/Cgap domain. Its two concrete applications are supported without invoking new network third derivatives. The accepted b262/0071 interface can supply such derivatives for another correctly identified full network coefficient, but it does not automatically verify its phase geometry or a finite budget.

These bounds concern complete half-line norms and include radius zero. They do not establish internal-map decay, source survival, early matching, integrated cut errors, positive outgoing tails, target normalization or a new simultaneous finite family. No runtime exponent, thermal/preparation improvement, normalized rare-branch guarantee, native supplier, readout/capture/reset or permanent halt is inferred.
