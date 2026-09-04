# Block 187 adversarial check — positivity window characterization

## Scope and exact reconstruction

I rebuilt the `Z_8 x Z_4` matrices from the specification in `b187_exact_check.py`. The only project source read was the permitted dependency script; the reconstruction uses only its `cover_index`, `cover_embedding`, and `block105.shear_hodge` APIs. My independently written index, all 32 embeddings, and symbolic Hodge block agree exactly with those APIs. The reconstructed `D` has 72 nonzero entries and obeys `D = -P D P`. Every decision below uses SymPy integers/rationals; no floating-point value enters a sign, equality, determinant, or bisection decision.

## C1 — mass axis

**Verdict: CONFIRMED.** At `c=5/13`, the exact leading-minor sign vectors are

| `m` | sign vector `(Delta_1,...,Delta_8)` |
|---:|:---|
| `1/10` | `(+,+,+,+,+,+,+,+)` |
| `1/4` | `(+,+,+,+,+,+,+,+)` |
| `1/2` | `(+,+,+,+,+,+,+,+)` |
| `3/5` | `(+,+,+,+,+,+,+,+)` |
| `3/4` | `(+,+,+,+,+,+,+,+)` |
| `1` | `(+,+,+,+,+,+,+,+)` |
| `5/4` | `(+,+,+,+,+,+,+,+)` |
| `3/2` | `(+,+,+,+,+,+,-,-)` |
| `2` | `(+,+,+,+,+,-,+,-)` |

Exact negative witnesses are

- at `m=3/2`, `Delta_7 = -85090229607948729741077107375715753305308272511435659763853597380350349476000039722071097344 / 572960703002653892616167087132755201440169903286762517538700877485657326861128751234870798641374881953125` and `Delta_8 = -55772685855493751416316702326098115089246386029464592895668226720213343145035865283100672 / 409257645001895637582976490809110858171549930919116083956214912489755233472234822310621999029553487109375`;
- at `m=2`, `Delta_6 = -7890231431818882674506063844880003094539586885471536889006112939561800730299477520607415894016 / 74808265874164739714380358730715033870378392220195408647397035293098882634606911082408149805703352125625` and `Delta_8 = -17019757780754929852868756247925151195438833387164842763181606680344607789806367277056 / 1526699303554382443150619565932959874905681473881538951987694597818344543563406348620574485830680655625`.

The Gram matrix was exactly Hermitian at every C1 point.

## C2 — mass boundary

**Verdict: CONFIRMED.** At `c=5/13`, the endpoint vectors are exactly

- `m=2911/2048`: `(+,+,+,+,+,+,+,+)`;
- `m=91/64`: `(+,+,+,+,+,+,+,-)`.

At the upper endpoint the sole failure is

`Delta_8 = -5272182110724018653744537162235884463195365879031413689821274893357388084196927319941971203859717239968536932744192831013257216 / 2852223386432627766189972804014619353218871437883392803720351552108660577540036605807029903777051262643970139899408284331218980830571655192305625`.

My exact bisection from `(5/4,3/2)` took the midpoint path

`11/8 (+), 23/16 (-), 45/32 (+), 91/64 (-), 181/128 (+), 363/256 (+), 727/512 (+), 1455/1024 (+), 2911/2048 (+)`.

Here `+` means all eight minors are positive and `-` means not all are positive. After nine steps this independently reproduces `(2911/2048,91/64)`. A tenth step gives the consistent refinement `(5823/4096,91/64)`, with all minors positive at `5823/4096`.

## C3 — shear axis

**Verdict: CONFIRMED.** At `m=9/20`, the exact vectors are

| `c` | sign vector `(Delta_1,...,Delta_8)` |
|---:|:---|
| `1/5` | `(+,+,+,+,+,+,+,+)` |
| `5/13` | `(+,+,+,+,+,+,+,+)` |
| `3/5` | `(+,+,+,+,+,+,+,+)` |
| `4/5` | `(+,+,+,+,+,-,+,+)` |
| `12/13` | `(+,+,+,+,+,-,+,-)` |
| `1713/2560` | `(+,+,+,+,+,+,+,+)` |
| `857/1280` | `(+,+,+,+,+,+,-,+)` |

Exact endpoint/failure witnesses include

- `Delta_6(9/20,4/5) = -266284252523900433745232911073005552817007835983413760000000000000000 / 29415408186772645015192497240958063260058620461545163952379054230264846961`;
- `Delta_7(9/20,857/1280) = -1598335222229188848331260139735713538793899586253898956125746360485779772825747609028331825177344729361412327257340956309228330917907048340418019474895782167589382115192894752389697512350270857779922509240329882828800000000000000000000 / 938014989242101233823150045262719995750420024879135748599481531431561317455090902457356073907424738459952665704930454884410309281827235552082034266431218759293162023117376658900999782141305020863400544754905318555013844105305274634098782326361`.

The exact bisection path from `(3/5,4/5)` was

`7/10 (-), 13/20 (+), 27/40 (-), 53/80 (+), 107/160 (+), 43/64 (-), 429/640 (-), 857/1280 (-), 1713/2560 (+)`,

which terminates at the claimed bracket `(1713/2560,857/1280)`. The Gram matrix was exactly Hermitian at every C3 point.

## C4 — corners and non-product structure

**Verdict: CONFIRMED.** All four exact vectors match:

| `(m,c)` | sign vector `(Delta_1,...,Delta_8)` |
|:---:|:---|
| `(1,3/5)` | `(+,+,+,+,+,-,+,-)` |
| `(5/4,1/2)` | `(+,+,+,+,+,-,+,-)` |
| `(3/4,7/10)` | `(+,+,+,+,+,-,+,-)` |
| `(1/10,4/5)` | `(+,+,+,+,+,+,-,+)` |

Exact witnesses are `Delta_6(1,3/5) = -52523939070044168716349889558763976641355807318191909636161929216 / 212374950530520124008053860398992737861223502117607259903904181168570081`, `Delta_6(5/4,1/2) = -92442569051078864152895446301447303882342400 / 4725034454698720183431285781738406661962815096625401`, `Delta_6(3/4,7/10) = -210039062259584319496434656025966003560122537067805070817869596856063687095031431168 / 90553709122530283307849375163806890213082846367489919216703295025480788469441212942578125`, and `Delta_7(1/10,4/5) = -196702296481530945521867791523795742855834960937500000 / 13689881409230243144704927919478627765962998376429743510081`.

Each corner combines a mass and a shear certified positive on the two sampled coordinate rays, yet fails jointly. Thus the positive set cannot equal the Cartesian product of those ray intervals. This does not determine the intervening curved boundary. All four corner Gram matrices are exactly Hermitian.

## C5 — openness promotion and its scope

**Verdict: CONFIRMED-WITH-CORRECTION.** The local openness promotion is valid at every claimed positive sample. The correction is that `det Q != 0` is not, by itself, the whole domain hypothesis: the Hodge chart must also be defined, here `c != +/-1`. Equivalently, the statement is made on

`U = {(m,c): c != +/-1 and det Q(m,c) != 0}`.

The exact mass-ray determinant has the compact certificate

`det Q(m,5/13) = F(m)^2 G(m)^2 / 22600569498765673425646382617815399421526202244979382923541986986760398250842873973826153086976`,

where

`F(m) = 299684727885699454242816 m^8 + 1057546650417160380713856 m^6 + 1122356975550987673041509 m^4 + 334202761189083845162330 m^2 + 29915998462435025408400`

and

`G(m) = 1198738911542797816971264 m^8 + 8357584267546985416158720 m^6 + 20746825460109491061517732 m^4 + 21542427261169485079330180 m^2 + 7964480716014734889397129`.

Every coefficient is a positive integer, so this proves exactly that `det Q != 0` at all seven positive C1 masses (indeed, for every real `m`).

For the three positive C3 shear samples, direct exact determinants are

| `c` at `m=9/20` | exact `det Q` |
|---:|:---|
| `1/5` | `13994953333167282846091214369164655514347086607283313719491888103245641918756214364756250082102023321 / 219116140165888394222918920571924360929171991805137640992957634969600000000000000000000000000000000` |
| `5/13` | `434365065623226699761613827521957114917610720141816981156959893930988465451681393063174107141165203868793090542441059790529 / 2392141431138299698729697223684503486672742367036209644060651639608672273328387649857126400000000000000000000000000000000` |
| `3/5` | `167938844184906124102413290784793690729579402712204844409919318025080177141229818816121520485796681 / 41137613933030151053874229563933762624568396640839496583715225600000000000000000000000000000000` |

All numerators and denominators displayed are nonzero positive integers. Thus all ten positive C1/C3 samples are in `U`.

Precisely: on `c != +/-1`, the entries of `H` and `Q` are rational, hence continuous. On `U`, `Q^{-1} = adj(Q)/det Q` is continuous; reflection, restriction, transpose/conjugation, and finite determinants preserve continuity. Each `Delta_k` is therefore continuous. If all eight `Delta_k(p)>0`, continuity supplies eight neighborhoods on which the respective inequalities persist, and their finite intersection is an open positive neighborhood of `p`.

The “denominators are powers of `det Q`” wording is correct only over the coefficient field of rational functions supplied by `Q`: inversion introduces powers of `det Q`. Written over polynomials in `(m,c)`, the Hodge entries also carry chart factors from `1-c^2`; those must not be omitted from the domain statement.

Hermiticity is structural, not a sample accident. Exactly, `P H P=H` and `P D P=-D`, hence `Q^T=P Q P`, `(Q^{-1}P)^T=Q^{-1}P`, and the reflected restricted Gram is real symmetric wherever defined.

What is established: a union of open positive neighborhoods around the ten certified points, the exact one-dimensional sign samples/brackets, and the four non-product witnesses. What is not established: connectivity or simple connectivity of the positive set, uniqueness of a boundary component, monotonicity away from the tested slice, an exact two-dimensional boundary curve, or interpolation between sampled rays.

## C6 — volume dial

**Verdict: CONFIRMED.** I used `shear_hodge(c_t,v)` on the positive half, the same `v` in `P4 shear_hodge(c_thA(t),v) P4^T` on the image half, and exact identity blocks at both zero-shear seam anchors. At `(m,c)=(9/20,5/13)`:

| `v` | Hermitian? | sign vector `(Delta_1,...,Delta_8)` | exact `det Q` |
|---:|:---:|:---|:---|
| `4/5` | yes | `(+,+,+,+,+,+,+,+)` | `14285683622601745390541541674222107411696366222829746178449192238334978522465535938425917614099281941616564421865203844009 / 737135490150174131639534407302747872319099360863783485440000000000000000000000000000000000000000000000000000000000000000` |
| `5/4` | yes | `(+,+,+,+,+,+,+,+)` | `11077683380864810137902501827970746581828643680934720491721644679599099108149160314066197906131262502661377365732525669243126486878365712105363339819840586280769 / 2630187318821282114327219793844976408897894482189862110474316654737414566893413894283944181897782886400000000000000000000000000000000000000000000000000000000` |

Positivity therefore survives one exact volume step in each requested direction. This is a two-point robustness check, not a certified volume interval.

## C7 — boundary order at the mass edge

**Verdict: CONFIRMED-WITH-CORRECTION.** The correction is arithmetic: `1456/1024 = 91/64`, so the suggested first “further” point is exactly the upper endpoint, not beyond it. I evaluated it as requested and added `2913/2048` as a genuinely further adjacent dyadic point.

At `c=5/13`, the exact `Delta_8` data are

| `m` | exact `Delta_8` | sign |
|---:|:---|:---:|
| `2911/2048` | `230206563854760436250197653699817592100084132897488822107268894580294758247343047226593939845567274569110442267330144379860729848130383064702436218183609600844961064121532416 / 84470375364379888995202153499838462070278151522745679063471845246921889331880757846172893203515459824707205603166476717922183719525452599555585553650911039370150092009488934961683571931475625` | `+` |
| `91/64 = 1456/1024` | `-5272182110724018653744537162235884463195365879031413689821274893357388084196927319941971203859717239968536932744192831013257216 / 2852223386432627766189972804014619353218871437883392803720351552108660577540036605807029903777051262643970139899408284331218980830571655192305625` | `-` |
| `2913/2048` | `-422016066763214429627958148553713951050122497858476060262104356617337736324922191826213732992714606027984411744488025479508626317289472413140467867746449348521001821124165632 / 66638349373295193421031204299805176561516462939808994073343377934051072058673869907249145298516936408255382135842281331167152695302266288259751923992468483678751397072440638608381285240214375` | `-` |
| `3/2` | `-55772685855493751416316702326098115089246386029464592895668226720213343145035865283100672 / 409257645001895637582976490809110858171549930919116083956214912489755233472234822310621999029553487109375` | `-` |

Exact cross multiplication gives the strict chain

`Delta_8(2911/2048) > Delta_8(91/64) = Delta_8(1456/1024) > Delta_8(2913/2048) > Delta_8(3/2)`.

Thus the requested finite diagnostic shows one sign transition and decreasing sampled behavior. There is also a stronger exact result. Jacobi's complementary-minor identity gives the numerator of `Delta_8(m,5/13)`, up to a positive rational constant, as

`A(m)^2 B_-(m) B_+(m)`, where

`A(m) = 2338702173616900 m^4 + 5559167172136500 m^2 - 34342504390877071`,

`B_-(m) = 584675543404225 m^4 - 119232179199250 m^3 - 808327810625400 m^2 - 7890304777814160 m - 12314765055708144`,

`B_+(m) = 584675543404225 m^4 + 119232179199250 m^3 - 808327810625400 m^2 + 7890304777814160 m - 12314765055708144`.

Exact Sturm counts on `(2911/2048,91/64)` are `0,0,1` for `A,B_-,B_+`, respectively. Also `gcd(B_+,B_+')=1`; `B_+'` has zero roots in the bracket and has positive endpoint values `27984065518306879605205855/2147483648` and `854440470872410964035/65536`. Since `det Q` never vanishes there by C5, the bracket contains exactly one zero of `Delta_8`, and that zero is simple. This is an exact proof for this bracket, stronger than the requested diagnostic.

## Overall verdict

**CONFIRMED-WITH-CORRECTION.** C1, C2, C3, C4, and C6 are confirmed exactly. C5's openness theorem is valid at every certified positive point but must state the Hodge chart domain `c != +/-1` in addition to `det Q != 0`, and its conclusion is strictly local. C7 confirms a unique simple mass-edge crossing, but `1456/1024` is the same rational as `91/64`, so it cannot serve as a further point.

## Ten-line summary

```text
1. The independent exact reconstruction matches all three permitted dependency APIs.
2. C1 is confirmed: every claimed mass-axis sign vector is exact.
3. C2 is confirmed: the two mass endpoints have the claimed vectors.
4. Exact bisection reproduces the mass bracket and refines its lower endpoint.
5. C3 is confirmed: all shear samples and the shear bracket match exactly.
6. C4 is confirmed: all four corners fail, ruling out a Cartesian-product region.
7. C5 is locally valid at all ten positive samples because every sampled det Q is nonzero.
8. C5 needs the chart-domain caveat c != +/-1 and proves no global boundary topology.
9. C6 is confirmed: both requested volume deformations remain Hermitian and positive.
10. C7 has a unique simple bracketed zero; 1456/1024 duplicates 91/64.
```
