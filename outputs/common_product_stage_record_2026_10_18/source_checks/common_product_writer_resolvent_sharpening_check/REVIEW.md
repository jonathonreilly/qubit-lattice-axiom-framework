# Exact writer resolvent sharpening: selective check

Disposition: supported within the specified local writer and momentum band. No required correction found. The literal positive-block matrix reduces to the two stated chains, a different exact elimination reproduces all row norms and determinants, and the continuum perturbation proves inverse norm below 10. The derivative replacements are valid. This does not certify any downstream finite-device substitution, runtime or completion herald.

## Sources, exposure and execution

Read the complete new proposal, certificate program and complete stored output. The actual writer and its check were read completely in the immediately preceding coherent task and reused at refreshed identical hashes, together with the fully checked packet interface. N denotes `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

- N/`common_product_writer_resolvent_sharpening/PROPOSAL.md`: `22bca57ebcbfb8cfabebbe044cd5302e784e585b503cee28d6172afc72e54cf0`.
- Its `certify_inverse.py`: `f1deb1c3200ca89e287f92ea69acbdf0ac02442ef84795717c795c0aa4b62a7d`.
- Its `certificate.txt`: `218168f4038232b24f2daa861b8adb37fe6eecc9845bf0c30bc4bb1338e58dda`.
- N/`common_product_stage_record_packet/PROPOSAL.md`: `3477197cdf54d18ab538c517726d64f3dbc556f6ddb7a6d4b2608b458d34eeb9`.
- My preceding packet review, N/`common_product_stage_record_packet_check/REVIEW.md`: `17029fa32989bae3869c4ffee81def65201edc0f0b996013ede8996ca8cf1453` (identity from its completed check).
- `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/outputs/attached_record_2026_10_17/source_checks/autonomous_record_route/PROPOSAL.md`: `93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56`.
- Its sibling `autonomous_record_route_check/REVIEW.md`: `c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a`.

ROOT suggested examining the center inverse and supplied the check scope, but reported no full read or preferred verdict at assignment. I read the author's method and certificate before the alternative calculation. This is a source-exposed same-model selective check, not blind verification, retained audit or model independence. The earlier writer/packet checks are explicit reused dependencies, not a new check merely by citation.

Only this report is written. A bounded independent exact SymPy calculation was executed from standard input; no numerical spectral routine, fit, sweep or author's executable was run. The exact algorithm and complete output are preserved below. No source/Git/W/checkpoint/editable-prompt/model change or publication occurred. Previously read applicable reviewer/workflow instructions are reused.

## Actual matrix, boundary sign and port rotation

For an ordinary internal arm head, two Q(-j) occupation contributions give diagonal 2 after division by j. A phase-cell endpoint has one ordinary bond, one sqrt(2) bond and occupation 2-sqrt(2), giving 3. A terminal has one arm bond plus the contact 1+x, giving 2+x. An attachment has its ordinary arm bond plus two junction magnitudes 1/sqrt(2), minus vacancy coefficient sqrt(2)-1, giving 2. Each port likewise has the two junction magnitudes, retained external-bond diagonal 1 and vacancy subtraction, giving 2. The only scalar removed is the four-vacancy scalar c_R. These are the actual block contributions, not an idealized effective writer.

The arm1 coordinate path is indexed from its terminal, so its y=2--3 and y=5--6 bonds are exactly chain edges 2 and 5. The junction in attachment order (A0,A1) and port order (U,F) has entries (-1,-1;-1,+1)/sqrt(2), namely -U. The positive fourth hopping is necessary. The supplied script assembles these entries and occupation contributions correctly. Its phase replacements and vacancy subtraction agree with the physical inventory; no extra terminal compensation is added.

The outgoing lead relation psi_1=z psi_0+(z^-1-z)f gives (H-E/j-zP)q=(z^-1-z)E_P f. Thus the -zP boundary term and -2i sin(k) prefactor are correct. At k=pi/2, relative diagonals are x at terminals, 1 at the four phase sites, 0 at other arm sites and -i at both ports.

T=diag(I_22,U) is real orthogonal, leaves the port block and P invariant, and turns -U into -I because U squared is I. The first rotated port consequently joins arm0 and the second joins arm1. Ordering each arm followed by its port gives precisely the two 12-by-12 chains in the proposal. There are no cross-chain entries. This is unitary equivalence for the actual inverse norm, not a nonunitary change for which an unaccounted condition factor is required.

## Independent exact arithmetic

Instead of rerunning the author's algebraic-field inversion and continuant checks, I used a rational similarity followed by explicit Gauss-Jordan row elimination. For each physical chain J, set d_0=1 and d_(a+1)=d_a/|e_a|, D=diag(d_a), and K=D^-1 J D. Then K has upper off-diagonals -1 and lower off-diagonals -|e_a| squared, all in Q(i). Diagonals are unchanged. The weights w_a=d_a squared equal 1 throughout arm0 and, for arm1, are 1 through index 2, 1/2 through index 5 and 1/4 thereafter. After exact elimination of [K|I] to [I|Z], J^-1=D Z D^-1, so the physical squared row norm is sum_b (w_a/w_b)|Z_ab| squared. This weighting is essential: the nonunitary rational similarity alone does not preserve norms.

The complete executed calculation, with compact formatting, was:

```python
import sympy as s
for x in (1,-1):
    dets=[]
    for phase in (False,True):
        n=12
        diag=[x]+[0]*10+[-s.I]
        if phase:
            for a in (2,3,5,6): diag[a]=1
        edge2=[2 if phase and a in (2,5) else 1 for a in range(11)]
        K=s.diag(*diag); weights=[s.Integer(1)]
        for a,m2 in enumerate(edge2):
            K[a,a+1]=-1; K[a+1,a]=-m2
            weights.append(weights[-1]/m2)
        aug=K.row_join(s.eye(n))
        for col in range(n):
            pivot=next(row for row in range(col,n) if aug[row,col]!=0)
            aug.row_swap(col,pivot); pv=aug[col,col]
            aug.row_op(col,lambda v,j:s.cancel(v/pv))
            for row in range(n):
                if row==col: continue
                factor=aug[row,col]
                if factor:
                    aug.row_op(row,lambda v,j:s.cancel(v-factor*aug[col,j]))
        assert aug[:,:n]==s.eye(n)
        Z=aug[:,n:]
        assert all(s.simplify(v)==0 for v in K*Z-s.eye(n))
        rows=[s.simplify(sum(weights[a]/weights[b]*Z[a,b]*
              s.conjugate(Z[a,b]) for b in range(n))) for a in range(n)]
        det=K.det(method='bareiss'); dets.append(det)
        print('x',x,'phase',phase,'rows',rows,'sum',sum(rows),'det',det)
    print('full determinant',s.expand(s.prod(dets)))
```

Complete successful output:

```text
x 1 phase False rows [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6] sum 72 det 1 + I
x 1 phase True rows [6, 6, 6, 21/2, 5/2, 19/2, 13/2, 13/2, 13/2, 13/2, 13/2, 13/2] sum 159/2 det -2 + 2*I
full determinant -4
x -1 phase False rows [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6] sum 72 det 1 - I
x -1 phase True rows [6, 6, 6, 3/2, 19/2, 5/2, 11/2, 11/2, 11/2, 11/2, 11/2, 11/2] sum 129/2 det 2 + 2*I
full determinant 4
```

The first execution stopped at a raw symbolic `K*Z==I` assertion: SymPy had not simplified equivalent rational expressions. Replacing that assertion with entrywise simplification, without changing matrix entries, elimination or weights, gave the successful result above. This was a checker representation issue, not a nonzero inverse residual; the final residual was checked exactly. No failed scientific counterexample was discarded.

The independently obtained row lists reproduce every entry in the author's table. Their sums give 72,159/2 and 72,129/2. Products of the separately obtained chain determinants give -4 and +4. The full Frobenius squares are therefore 303/2 and 273/2. I also inspected the author's continuant indexing: theta_a is the leading minor before row a, phi_(b+1) the trailing minor after b, the signed edge product gives the off-diagonal cofactor, and theta_12 is the determinant. Its formula and code match these conventions. Its left/right residual checks, rotation checks and stored output are coherent with the alternative calculation. The author's program was read, not rerun or treated as sole evidence.

## Center norm and whole-band extension

The direct-sum operator norm is the maximum of the two block norms. Each is at most its own Frobenius norm, so max is at most sqrt(159/2)<9. Using the full 24-by-24 Frobenius norm instead would not establish this constant; the proved orthogonal chain split is load-bearing. Conserved record-X sectors take another maximum, not a sum.

The only k dependence is -2(1-cos k)I-zP. Hence Delta=2 cos(k)I-(z-i)P and ||Delta||<=3|k-pi/2|. Factoring L=L0(I+L0^-1 Delta) proves the inverse formula in the source with the correct multiplication order. Since ||L0^-1 Delta||<27h, Neumann inversion yields ||L^-1||<9/(1-27h)<=9000/973<10 for h<=10^-3. This is an analytic bound over every real k in the interval, not interpolation from samples. Its denominator is positive. It retains the same physical matrix, scalar, reference planes and record sectors.

## Derivatives and scope of replacement

Both L' and L'' have norm at most 3. With G=L^-1 and B=10, the inverse identities give ||G'||<=3B squared=300 and ||G''||<=18B cubed+3B squared=18300. The scalar -2i sin(k) and its first two derivatives have magnitudes at most 2. Product differentiation therefore gives V<=20, V'<=20+600=620 and V''<=20+1200+36600=37820. Port restriction gives the same first and second derivative ceilings for S_w; the derivative of -I vanishes. These are k derivatives of a dimensionless boundary matrix, so no physical-j factor is missing.

The older packet algebra also accepts the looser direct substitutions 2B=20,8B squared=800 and 56B cubed=56000. Both choices are valid, but a subsequent downstream computation must identify its choice and recompute its feedback/internal constants. This report does not perform or certify that downstream arithmetic. The two writer copies form a head-path direct sum in each shared record-X sector, so their 48-head map has the same local constants without factor 2; a passive reference changes no norm.

This sharpens a mathematical estimate, not the physical apparatus. The old 10^31 bound remains valid and was merely pessimistic. Neither bound asserts optimality or an exact smallest singular value. The result excludes local outgoing singularities on the selected interval but supplies no global completeness, finite-seed bound-state overlap estimate, finite emitter launch, finite output cut, resource exponent, or all-time Record implication. The parent network's feedback margin, propagation, normalization and complete-output obligations retain their own scopes. No runtime or herald theorem is transferred by this check.
