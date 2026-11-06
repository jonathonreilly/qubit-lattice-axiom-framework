lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T16:05Z

# P10 stability port: one line-by-line check

Status: in progress (written section by section).

Target: `library/port/p10-stability.md` (1,686 lines), Codex port of CA-I rows A10, A15, A17, A19, A20 of `library/chain-ca.md`. Source: CA-I `theorem_0_complete_account_raw_I.tex` at `31a47c543775` (166,711 lines), fetched by raw URL into a scratch folder. Pinned at branch commit `2bb183fd0`. One reading, not a hostile review, not an audit.

## A10 — 4.18:thm-preparatory-boundary (port L43–278; CA-I 54985–55192)

- Statement (L106–158): matches CA-I 54985–55052 clause by clause: (a)–(f), the rates (A10.2), the constant `C_0=c_G(d,L,M)+1`, and the last assertion. The `X∈𝔻_m` of (A10.3) is to be read with `m=m(X)`, as at CA-I 54355–54358. That is the source's reading too.
- Hypotheses (L50–86): H-STAGE and H-PROFILE-CLASS are the first two bullets of 54989–55003. H-RECURSION is (α), (β) of `4.18:prop-profile-independence` (54497–54505), plus the setting of that proposition (same stage-0 action, same members, couplings and measures). H-INDICATOR is lemma hypothesis (ii) (54694–54698). The port's added H-WEIGHT (lemma premises (i), (iii)–(viii), 54692–54715) is correct and worth keeping. The source proof uses the lemma's conclusions (a) and (d) at 55115, 55126 and 55186–55191, but the theorem names only premise (ii). The port lists the premises correctly.
- (A10.1) (L88–103): matches the weighted norm and filing rule at 54339–54353.
- Compensation step (L167–193): this is the induction of `4.18:prop-profile-independence` (54545–54600), in the right order. I checked the signs. Proposition (c) and (d), with `Π` the family and `Π'` the companion, give family − companion = `A(e_n,·)` for the non-Wilson parts and `A(e_{n+1}−e_n,U)` for the stage terms. These agree with (A10.6) and with the corollary's display 54634. The logarithm-branch remark (L174–176) is a correct fill. One series defines the logarithm for both systems, so equal integrals give equal logarithms.
- (a) (L195–206): see finding F1. This is a small gap, shared with the source, that can be repaired.
- (b) (L208–213): matches 55116–55122.
- (c) (L215–243): (A10.7) is 55134–55138, and its last inequality is correctly marked as an H-STAGE input. The filled norm step (L226–231) is correct. For `□∈π_{j+1}`, the only cube term `X∋□` with `X∈π_{j+1}` is `X=□`, and `d_{j+1}=0`. So the cube family has norm at most `sup_C‖A(w_{n+1}1_C,·)‖_∞`, and subadditivity gives (A10.8) = 55142–55153.
- (d) (L245–248): correct. Take `□⊂X` with `□∈π_{m(X)}`. One term of the nonnegative sum is then at most `‖ℂ‖≤C_0`.
- (e) (L250–255) and (f) (L257–264): these match 55163–55182. In (f), "these are unchanged" is slightly too strong, but containment is true and is all that is needed. Since `φ°≥φ≥0` (54135 and lemma (a)) and `φ_{Z_{j+1}}=0` on `Z_{j+1}⊃D_{j+1}`, one has `w°_{n+1}=−β_{j+1}φ°_{Z''_{j+1}}≠0` at every point of `D_{j+1}` (when `β_{j+1}>0`). So the prepared cube family's support lies in the companion's.
- Last assertion (L266–270): `j+1≤k_0 ⟺ n+1≤N−N_0`, since `N=k−h` and `k_0=k−N_0`. Correct.
- **F1 (L203–206; also CA-I 55107–55114). Repairable, not fatal.** Statement (a) requires each new cube to meet the conditions of (1.63), and the port's own L101–103 lists `X∩Ω_m≠∅` among them. H-WEIGHT (lemma (d) with premise (viii)) gives `m(C)=j+1`, `C∈𝔻_{j+1}` and `C∩R_n≠∅`. It does not give `C∩Ω_{j+1}≠∅`, and `R_n⊂Z_{j+1}=Λ_{j+1}^c` (53808) does not imply it. The source proof has the same omission. Repair (unproved here beyond these lines): a cube term with non-zero excess has a base point `x∈C∩D_{j+1}`. By the support remark under (f), the companion's cube term at the same `C` has `w°_{n+1}(x)≠0`. So H-STAGE (a) has already filed `C` under (1.63), and the prepared family can take the companion's filing.
- Verdict A10: faithful. Proved as an implication from H-STAGE, H-PROFILE-CLASS, H-RECURSION, H-INDICATOR, H-WEIGHT and H-PREPARED, with F1 repaired as above. CMP 122a (1.60)–(1.70) stays assumed, as the port says (L272–275).

## A15 — 4.38:cor-step-count (port L280–442; CA-I 60810–60878)

- Statement (L354–379): matches 60810–60838 in parts (a)–(f). In (e), the port reads "the last member of clause (0)" as the torus-identification sentence. That is right: in Theorem 0 itself (CA-I 2542) the last member is "The K renormalization steps on T_m produce exactly these couplings", and fixed-depth windows comes after it as a separate item. In `4.1:thm-clause-zero` it is item 5 (3553). The H-AUX qualifier in (f) is an addition. It is conservative and correct.
- Hypotheses (L288–352): H-TORUS lists the seven A14 hypotheses of 58188–58216 faithfully. (A15.1) agrees with `1.2:def-flow-constants` (657–666) and `4.38:def-admissible-sites` (57036–57065). H-CELL is the pair "taken by statement" at 57122–57126, and H-HOM is 57047–57053.
- H-FLOW (L310–318) is an input the source does not name. The source's (a) uses clause (β_j) of 𝔦(j) for `x_j>0` (60852). The source's (e) does not show that the first-passage set is nonempty: 60866–60872 shows only that `K` is site-free. So the port is right to carry the drift bound as a named input.
- (a) proof (L385–394): matches 60843–60857.
- No-circle fill (L396–402): matches property (i) and (iii) at 57067–57090 and 57095–57115. `𝒮_j^♭=𝒮_{j−1}∩{K'≥j}` is defined from earlier data, and each condition is a lower bound on `m`.
- First-passage fill (L407–422): checked step by step. With `T=g^{-2}+B_♯`, `g_0≤g_-(g)` gives `x_0≥T`, so `x_0≤T` forces `K=0`. If no passage occurs, an `n>(x_0−T+c_5)/λ_♯` gives `x_n≤x_0−λ_♯n+c_5<T`, which is a contradiction. At `K>0`, `x_K≥x_{K−1}−B_♯>g^{-2}≥γ_H^{-2}>γ^{-2}`, using `γ_H^{-2}≥γ^{-2}+c_5+1`. Correct, and it uses only H-FLOW.
- (c) (L424–433): the display is word for word the proof of property (ii) at 57116–57132. Correct.
- (d) (L435–440): the homogeneity argument `(RT)(aρ)=a(RTρ)` follows from H-HOM as stated (T linear, R of degree one, no term contains E). It is a correct fill of 60862–60865.
- (f) (L442–443): correct as an implication from P7 and H-AUX.
- Verdict A15: faithful. Proved as an implication from H-TORUS, H-FLOW, H-CELL, H-HOM and H-AUX. No failing step.

## A17 — 4.20:thm-representation (port L444–1008; CA-I 61095–61206)

- Kind: the source gives no proof at the theorem. The proof is "the induction ... in the sections that follow" (61208–61210). The port is a conditional assembly from named inputs, and it says so (L450–452, L797–799). It is checked as that.
- Statement (L453–599): (a), (b) with (A17.3), and (c) with (A17.4)–(A17.5) match 61095–61206. That includes the CMP 119 exceptions ((2.47) dropped, the integrated upper member in place of (2.50)), the hereditary-class reading, the two weaker cases of (b), and "no reverse comparison". (A17.1)–(A17.2) match `4.20:not-representation` (60940–61063). The constant `E_k[𝒮]` depends on the label. The source writes `E_k` inside `A_{k,𝒮}`, so this reading is allowed.
- REP-PARAM (L459–494): agrees with (H1)–(H6) at 1126–1182. That includes the two unproved rank-`N≥3` statements and the separation of (H7). `2.4:prop-m-freeness` is incomplete at (∗) (1202–1205). Correct.
- Antecedent table and frontier (L604–797): I spot-checked these status loci, and all are correct: `4.4:prop-local-real-base`, outstanding (8110, 8373); `4.13:lem-minimizer-unique` and `lem-own-constant`, outstanding (45163, 45204); `4.21:prop-relative-machine`, outstanding (61325), with the two unproved inputs at 61304–61310 and 61345–61349; the arrest theorem incomplete (137628); A18 outstanding (156837, 156953); core-freezing (146051); cubewise analysis (151575); frames-instance (153174); and `4.26:thm-inherited-expansion` (119813–119900), where the three hypotheses and (A17.6) match. The REP-RF expansion (f0)–(f4) matches 61243–61298. The published-input table and both open lists match 166563–166692 entry by entry. The Combes–Thomas entry is indeed "not used in the proof of clause (i)" (105192–105194). The port is right that the summary lists omit the local real base, near-group persistence and stored orbit supply.
- Induction order (L807–816): matches 3593–3613.
- Induction-object fill (L818–828): correct. The structural part of A17 at level `k` comes first. A19 at `k` follows from it with (h1)–(h11), and only then is the integrated member of A17(a) available. No integrated bound at `k` enters the structural step at `k`. This is the order 166702–166709 states.
- Position-dependent coupling fill (L908–920): the same computation as 61066–61077. Correct.
- Skeleton-entropy fill and (A17.7) (L922–971): this is `4.21:lem-skeleton` (c) (63275–63371) and `4.21:prop-birth-site` (c) (77510–77528), step for step. `d^θ(X)=d_j(sk(X))` is the definition at 975–978. `λ_θ=(1+3^d)𝖼_d\log2` is fixed exactly at 960, so the count `2^{(1+3^d)N_j(A)}≤e^{λ_θ(d_j(A)+1)}` holds with `N_j(A)≤𝖼_d(d_j(A)+1)`. The last line of (A17.7) uses `λ_θ≤β_sκ/4`. Correct. The port leaves implicit one condition the count needs: `X∩W` must be a union of whole strips (clause (u2), 77511). It is part of H-BIRTH.
- Ratio fill (L983–991): with `t=x_j/x_n>1/2`, `max(1,t^2)≤4t^2` and `g_j^{κ_0}t^2=g_j^{κ_0−4}g_n^4`. Correct, and it handles steps where the coupling moves backward.
- Verdict A17: faithful. It is a conditional assembly of 4.20 from REP-PARAM … REP-STABILITY, the published inputs, the PRINT-* inputs and the open inputs O-*, all named. REP-RF, REP-ARREST, REP-CORE, REP-POS and others stay open, as their own sources say. No failing step.

## A19 — 4.33:thm-stability (port L1010–1360; CA-I 157000–157241)

- Hypotheses (L1017–1137): (h1)–(h11) match 157028–157075 one by one. The port is right that the source has eleven hypotheses, not the "(h1)–(h8)" of `chain-ca.md` row A19. The conventions (L1020–1033: `N_k`, `ℓ_j`, `Z_j`, `Z_j^+`, `Γ_n`, the disintegration) match 157000–157026. The (h6) remark (L1095–1098) is right: 157243–157249 sketches a route and proves nothing.
- §5.2 correction (L1139–1205): **correct.** I checked its premises and its algebra.
  - Chapter 1's bare density has no vacuum constant: `ρ_0(U)=exp[−g_0^{-2}A(U)]` (CA-I 479). During the induction `E=0` (57047–57053).
  - The vacuum theorem's label energy does include it: `E=Σ_{j<K}E^{(j)}(T,T)` and `E_k[𝒮]=E−Σ_{j<k}E^{(j)}(Ω_{j+1},Λ_{j+1})` (159153–159160). Its (a) is `𝔈_k=Σ_{j=k}^{K−1}E^{(j)}(T,T)=−𝔩_k+𝔯_k` (159321–159327).
  - So (h4)(a) holds for `ρ̂=e^{−E_vac}ρ^{bare}` and not for the bare density. (A19.6)–(A19.7) follow at once.
  - (A19.8) is 159414–159426 with `d=4` and `D=N^2−1`. `C_log=\tfrac92(N^2−1)L^4` at 159314 fixes `D`.
  - (A19.9) is right: `Σ_{t=0}^{n−1}L^{−4(t+1)}=(1−L^{−4n})/(L^4−1)`, and `D_0/(L^4−1)=c_G^♯+K_*(E_0+1)/(L^4−1)=C_𝔯` (159312).
  - The bare-variable restatements (L1254–1259) have the factor `e^{E_vac}` on the correct side.
  - The source intends E-fixed densities at the Theorem 0 sites (57047–57053, 60862). So this is a needed precision of convention, not an error in 4.33's internal deduction. `gates/nrm-check.md` §5 reached the same finding first.
- Conclusions (L1207–1259): match (i-b)(1)–(3) and (i-c) at 157077–157111.
- Proof (L1262–1358): it follows 157114–157241 step by step. Lower member: keep the never-large term, then apply (h2) and (h3)+(h4)(a). Upper member: disintegrate, apply (h5), then (h4)(c), split off `n=k`, use `|Γ_k|≤N_k` with a nonnegative coefficient, then (h6). Next come mass preservation for T, the partition, R, (h9) and (h10), and finally the last-level constant. Each filled step is correct: the measure comparison, the sign for the volume swap, `E_+≤\max(a,b)(1+ℓ_k)`, and the kernel reading of the T step.
- Verdict A19: faithful. Proved as an implication from (h1)–(h11), read in the vacuum-normalised convention of §5.2. REP-POS (A18) and (h6) stay assumed. No failing step.
