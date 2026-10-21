# Biased phase envelopes: distinct analytical check

Disposition: SUPPORT as an isolated Hilbert-valued oscillatory-integral lemma. All displayed derivative identities, uniform constants, one/two integration-by-parts bounds, discrete-tail estimates and the boundary time integral are supported under the stated hypotheses. No source correction is required. This does not establish an exact scattering packet or any finite-operation result.

## Sources, exposure and coverage

Read the complete new argument and verified SHA256:

- `common_product_biased_phase_envelopes/PROPOSAL.md`: `54e054cbe0238590de69aced0d49a9d162f31c1503e105fe70b6e46047c6d3bc`.

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. Reused the complete immediately preceding stationary-network read and check, refreshing both hashes:

- `common_product_biased_record_network/PROPOSAL.md`: `cdf35dd3f9a8ea32ce0b52745ac00756885dba014d67db7e12f706e58e63b666`.
- `common_product_biased_record_network_check/REVIEW.md`: `1bd4a2878923495df99a219cce1c520cc03674bce2da5ff1d61d64d0940f8d40`.

That check records the exact local-writer ancestry and endpoint correction. The new envelope calculation is self-contained once q and E are specified; no old finite proof is needed to derive its inequalities. The source's statement that the composition check was pending is drafting chronology, not the current status.

ROOT authored this lemma, specified the bounded review and had read the upstream arguments. I had checked its stationary network and component ancestry. This is source-exposed, same-model selective analytical verification, not blind replication, blanket ancestry revalidation or retained audit. Applicable reviewer/workflow instructions previously read in this coherent campaign are reused. Only this report was written; no scientific program, source/W/Git/checkpoint/axiom/editable-prompt/model change, delegation or publication occurred.

## Derivatives and domain

From cos q=cos k+r/2 and sin q>0, differentiation gives sin q q'=sin k. A second differentiation gives sin q q''=cos k-cos q(q')^2. Differentiating this relation once more gives sin q q'''=-sin k+sin q(q')^3-3cos q q'q''. Thus all three formulas have the stated signs and coefficients.

The domain implies |cos k|<=.001 and |cos q|<=.0015. Both sines exceed .99, so .99<q'<1/.99. Explicit conservative ceilings are

    |q''| <= [.001+.0015/(.99)^2]/.99 < .00256 < .003,
    |q'''| <= [1+(1/.99)^3+3*.0015*(1/.99)*.003]/.99 < 2.06 < 3.

These apply uniformly, including r=0, where q=k and the higher derivatives vanish. E'=2j sin k>1.98j, E''=2j cos k and E'''=-2j sin k, giving the stated absolute ceilings 2j. All derivatives are smooth on this open-channel band; no threshold limit is being taken.

## Hilbert-valued integration by parts

Write p=phi', a=p'/p and b=p''/p. Smooth compact support of f and its first derivative removes the boundary terms in both integrations. The first integrand after integration by parts is, up to a unit complex scalar,

    (f'-a f)/p.

After two integrations it is, again up to an irrelevant sign,

    [f''-3a f'+(3a^2-b)f]/p^2.

Taking the Bochner integral norm and using |p|>=g yields exactly the stated F1/F0 and F2/3F1/F0 formulas, including the coefficient 3 multiplying the squared ratio. These manipulations require only the specified compactly supported C2 Hilbert-valued amplitude and the smooth scalar phase. No dimension or component factor arises. The sign of p may be negative; its absolute lower bound is what enters both estimates.

## Spatial phase gaps and discrete sums

Here phi'=nq'+ell+57-tE', phi''=nq''-tE'', and phi'''=nq'''-tE'''. The time restrictions imply 2jt<=1.75ell, while 2jt0=2u0<=.02ell.

For n>=ell and 0<=t<=T,

    phi' >= .99n-.75ell+57 >= .24ell+.99(n-ell).

The ratio of .003n+1.75ell to the latter denominator is maximized at n=ell (its derivative has negative numerator). Its maximum is 1.753/.24<8. The decreasing-function integral comparison for the sum beginning at n=ell+1 gives

    sum g_n^-2 <= integral_0^infinity (.24ell+.99x)^-2 dx
               = 1/(.99*.24ell) < 5/ell.

This sum deliberately excludes n=ell. The one-IBP result therefore bounds the norm of the far-positive sequence by sqrt(5/(2pi)) (F1+8F0)/sqrt(ell), below the claimed factor 2.

For n<=0 and t>=3ell/(4j), the negative phase gap obeys

    -phi' >= .99|n|+.485ell-57 >= .99|n|+.428ell,

where the last step uses ell>=1000, including equality at ell=1000 in this weakened bound. The ratio ceiling is at most 1.75/.428<5; its large-|n| limit is smaller. Because n=0 is included, the appropriate discrete estimate includes the first term:

    sum g_n^-2 <= (.428ell)^-2+1/(.99*.428ell) < 3/ell.

Indeed after multiplication by ell its first term is at most 1/(1000*.428^2), and the resulting total is below 2.37. Thus the claimed factor 2 again exceeds the direct sqrt(3/(2pi)) factor. This is a mathematical full-integer sequence estimate, not a physical negative-site assertion.

At t=t0, n>=0 gives phi'>=.98ell+.99n, with positive57 discarded. The second-derivative ratio is at most max{.02/.98,.003/.99}<1. Including n=0,

    sum g_n^-2 <= (.98ell)^-2+1/(.99*.98ell) < 2/ell.

The early tail bound follows with coefficient sqrt(2/(2pi))<2. The lattice interpretation takes ell to be an integer length, as in its stated intended application. The same integral comparison for the far tail remains valid for a nonintegral cutoff when the sum is over the specified integers n>=ell+1; the formal oscillatory integral also makes sense for real n. No hidden extra endpoint term is needed for any of the stated sums.

## Boundary envelope and its time integral

For n in {ell,ell+1,ell+2},

    phi' >= 1.99ell-2jt >= .24ell > 0.

The uniform ratio ceilings can be checked explicitly at the least favorable endpoint:

    |phi''/phi'| <= [1.753ell+.006]/(.24ell) < 8,
    |phi'''/phi'| <= [4.75ell+6]/(.24ell) < 20,

using ell>=1000. Hence two IBPs give F2+24F1+(20+3*64)F0, exactly F2+24F1+212F0, over sqrt(2pi)(1.99ell-2jt)^2.

The interval is nonempty since t0<=ell/(100j)<T. With qstart=1.99ell-2jt0>0 and qend=.24ell,

    integral_t0^T j/(1.99ell-2jt)^2 dt
      = (1/2)(1/qend-1/qstart)
      <= 1/(.48ell).

This proves the displayed integrated bound for each named level. It is not already a bound for a multi-level boundary operator; its norm and any multiplicity or channel combination must be supplied separately, exactly as the source says.

## Interpretation and remaining obligations

The ideal blank-record incoming column has the checked coefficient phase -i exp(57ik), so absorbing -i into f and retaining shift57 is consistent. The spatial record1 factor uses q(k); its ordinary-amplitude conversion is sqrt(q') with q'=sin k/sin q. A record0 residual must use q=k instead. A physical common scalar c+mu contributes the separate global time phase and does not alter these spatial estimates.

For a concrete packet, C2 regularity and quantitative F0,F1,F2 must be proved for the full amplitude, including derivatives of sqrt(q'), launch coefficients, all scattering/error maps and any cutoff. The lemma does not provide those coefficient bounds. It also does not prove full scattering-packet normalization, spectral completeness, seed matching, finite cut comparison, normalized output, a flag horizon, preparation-temperature improvement or any resource exponent. The verified result is precisely the scalar-phase/Hilbert-amplitude envelope under its explicit hypotheses.
