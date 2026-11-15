lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-16T05:10Z

# Row 1007, `gap-2don-proofs-read-opus`: primary reading of the posted proofs of the 2D O(N) gap

Started 2026-11-15T17:10Z on Mac mini worker 3, at commit f1acd28cb, branch claude/ym4d-hard-route. Reading only: no attack, no new claim.

## Plan (at most eight steps)

1. Read the row's context: FINISH.md rules (Build on published work, efficiency), row 1006, `library/gap-crux-exercise4-check-opus.md` L160-200, lead rule W2 and Corollary S2 in `parts/gap.md`, Lemma PT and Proposition NP of row 1003.
2. Locate and download source A (Ding-Huang-Yang, arXiv:2611.04908) into its own /tmp folder; extract text.
3. Locate source B (OpenAI's 2026-10-06 proof for N = 3): DHY bibliography, Pei arXiv:2611.01532, arXiv listing, OpenAI site, GitHub. Record where looked.
4. Source A, items (1)-(3): theorem, skeleton with pages, where N >= 3 is used.
5. Source A, items (4)-(6): K-one/K-flow, PT and NP, 4D SU(2) analogues, bridge to S(n; 2n) <= 1/20.
6. Source B, items (1)-(6), or NOT FOUND with the places searched.
7. Follow-up preprints (arXiv:2611.01532, arXiv:2610.16824, later ones), one line each.
8. Summary and RESULT line.

## Step log

(sections appended below as each step completes)

## Repo search (FINISH rule "Repo first")

- This folder: the only lane record of the two proofs is `library/gap-crux-exercise4-check-opus.md` L160-200 (row 1006): DHY abstract and pp. 1-6 read, Theorem 1.1 quoted, OpenAI proof described only through DHY Remarks 1.3, 1.5, p. 6; "I did not locate or read it". Its lane grep for 2611.04908, 2611.01532, 2610.16824, "Ding, Huang", "Polyakov", "October 6" found nothing else. The nearest older record: Ursachi, Research Square rs-11440706/v1 (conditional finite seed criterion for 2D O(3) on small tori; `prior/gap-crux-lit-2.md` L309, `prior/gap-seed-lit.md` L20).
- `parts/gap.md` L92: the row 1002 filter is withdrawn as a price; "The 2D model is now a source of mechanisms, not a price. Row 1007 reads both proofs."
- The checkout has one remote ref (origin/claude/ym4d-hard-route); origin/main and the PR branches #10114, #10133, #10134, #10141, #10144 are not fetched here, so they were not searched (this machine has no fetch brief for them). A `git grep` over the one remote ref for the arXiv numbers ran in the background; result recorded below if it differs from the folder grep.

## Step 1. Context: what the row's items (4) and (6) test

- **Lead rule W2** (`parts/gap.md` L90): (K-one) = a property of the measure at one scale, naming a number; (K-flow) = a statement that reads first-passage data and is carried through the band by a step. A (K-flow) step that reads one factor of the state space is bound by Lemma PT (a product with a no-seed factor); one that reads the whole space only through finitely many values of D is bound by Proposition NP.
- **Lemma PT** (`gap-crux-exercise3-max.md` L690-713): for a product model, Z = Z_1 Z_2, D = D_1 + D_2, 1 + S = (1 + S_1)(1 + S_2), m = min(m_1, m_2); a seed of the product is a seed of each factor. So an argument "passes PT" if it does not also prove a gap for a product with a massless (no-seed) factor, i.e. it uses a property the product lacks.
- **Proposition NP** (`gap-crux-exercise4-max.md` L342-437; HOLDS in check 1006): a product (K copies of strong-coupling Wilson SU(2)) x (ordered Ising) contracts D on any prescribed J doublings and has no seed. So an argument "passes NP" if its induction does not read the model only through a finite history of D.
- **The lane's seed for 2D** (`gap-crux-restate.md` L174, L205, Corollary S2): W(a, b) = partition function of the a x b periodic torus, W(a, b) = Tr T_b^a with T_b the transfer operator of the circle of length b; 1 + S(a; b) = W(a, b)/lambda(b)^a. Seed: S(n; 2n) <= 1/20 for one n; then S(2n; 4n) <= 19 S(n; 2n)^2 and the circles of length 2^(k+1) n have gap >= log(1/(19 S(n; 2n)))/n. Scope note (row 698): the transfer setting for O(3) is "plausible ... not proved here". Note for item (6): S(n; 2n) = sum over excited eigenvalues of (lambda_i/lambda_0)^n on the circle of length 2n, so it sees every excited state of T_(2n) (all sectors, all multiplicities), not only the spin channel; it is a periodic-torus free-energy statement, log(1 + S(n; 2n)) = log W(n, 2n) - n log lambda(2n).
- Source A downloaded: arXiv:2611.04908v1 PDF, 74 pages, into `/tmp/row1007-dhy/` (text extracted with PyMuPDF, Python -I; not committed).
