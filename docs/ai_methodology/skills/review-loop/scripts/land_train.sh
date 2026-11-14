#!/usr/bin/env bash
# Land one frozen review-loop train so that every carried PR shows as merged.
#
# Run it from the root of the clean integration worktree, after the combined
# gate and the generated-output cleanup:
#
#   bash land_train.sh <train-file>
#
# <train-file> holds one NAME=value line for each of seven inputs. A value is
# a list of entries separated by single spaces. Blank lines and lines that
# start with "#" are skipped.
#
#   VALIDATED_BASE  the origin/main commit the combined gate ran on
#   VALIDATED_TREE  the tree of the combined candidate
#   COMMITS         the reviewed source-only commits: units in their recorded
#                   order, each unit oldest first, each commit once
#   PR_NUMBERS      every carried PR, all constituents included
#   PR_HEADS        the frozen head commit of each PR
#   PR_HEAD_REFS    the head branch of each PR in this repository
#   PR_TIPS         for each PR, the entry of COMMITS that completes it
#
# The four PR lists are parallel. List the PRs in the order of their PR_TIPS
# entries in COMMITS. The last tip is the last commit, so every landed commit
# belongs to a carried PR. Commits and trees are full object names.
#
# Standard output: RECOVERY_REF <pr> <ref>, LANDED <sha> and
# MERGED <pr> <frozen-head> <landed-head>.
# Standard error: FAILED: <reason> with exit status 1, NOT_RESTORED <pr>: ...,
# NOT_MERGED <pr>: ... and LEAVE_OPEN <pr>: ....
# The exit status is 0 once LANDED is printed, so read every line after it.
# references/LANDING.md says what each line means and what to do next.
#
# Bash reads this whole file before land_train starts, so a train that changes
# this file cannot change the run that lands it.
if [ -z "${BASH_VERSION:-}" ]; then
  echo "FAILED: run the landing loop with bash" >&2
  exit 1
fi

train_file_error() {
  echo "FAILED: train file: $1" >&2
  exit 1
}

is_object_name() {
  case "$1" in
    ''|*[!0123456789abcdef]*) return 1 ;;
  esac
  [ "${#1}" -eq 40 ] || [ "${#1}" -eq 64 ]
}

# The train file is parsed and never executed. Every entry is checked for its
# form here, before the loop runs any other command.
read_train_file() {
  local file line name entry seen number
  local -a entries
  local IFS=' '
  if [ "$#" -ne 1 ]; then
    echo "FAILED: usage: land_train.sh <train-file>" >&2
    exit 1
  fi
  file="$1"
  if [ ! -f "$file" ] || [ ! -r "$file" ]; then
    train_file_error "cannot read $file"
  fi
  seen=""
  number=0
  set -f
  while IFS= read -r line <&3 || [ -n "$line" ]; do
    number=$((number + 1))
    case "$line" in
      ''|'#'*) continue ;;
    esac
    name="${line%%=*}"
    case "$line" in
      VALIDATED_BASE=*|VALIDATED_TREE=*|COMMITS=*) ;;
      PR_NUMBERS=*|PR_HEADS=*|PR_HEAD_REFS=*|PR_TIPS=*) ;;
      *) train_file_error "line $number is not one of the seven NAME=value lines" ;;
    esac
    case " $seen " in
      *" $name "*) train_file_error "line $number sets $name a second time" ;;
    esac
    seen="$seen $name"
    entries=(${line#*=})
    for entry in "${entries[@]}"; do
      case "$name" in
        PR_NUMBERS)
          case "$entry" in
            *[!0123456789]*) train_file_error "$name entry is not a PR number: $entry" ;;
          esac
          ;;
        PR_HEAD_REFS)
          if ! git check-ref-format "refs/heads/$entry"; then
            train_file_error "$name entry is not a branch name: $entry"
          fi
          ;;
        *)
          if ! is_object_name "$entry"; then
            train_file_error "$name entry is not a full object name: $entry"
          fi
          ;;
      esac
    done
    case "$name" in
      VALIDATED_BASE|VALIDATED_TREE)
        if [ "${#entries[@]}" -ne 1 ]; then
          train_file_error "$name needs exactly one entry"
        fi
        ;;
    esac
    case "$name" in
      VALIDATED_BASE) VALIDATED_BASE="${entries[0]}" ;;
      VALIDATED_TREE) VALIDATED_TREE="${entries[0]}" ;;
      COMMITS) COMMITS=("${entries[@]}") ;;
      PR_NUMBERS) PR_NUMBERS=("${entries[@]}") ;;
      PR_HEADS) PR_HEADS=("${entries[@]}") ;;
      PR_HEAD_REFS) PR_HEAD_REFS=("${entries[@]}") ;;
      PR_TIPS) PR_TIPS=("${entries[@]}") ;;
    esac
  done 3< "$file"
  set +f
  for name in VALIDATED_BASE VALIDATED_TREE COMMITS PR_NUMBERS PR_HEADS PR_HEAD_REFS PR_TIPS; do
    case " $seen " in
      *" $name "*) ;;
      *) train_file_error "$name is missing" ;;
    esac
  done
}

land_train() {
   read_train_file "$@"
   if [ "${#PR_NUMBERS[@]}" -eq 0 ] \
      || [ "${#PR_NUMBERS[@]}" -ne "${#PR_HEADS[@]}" ] \
      || [ "${#PR_NUMBERS[@]}" -ne "${#PR_HEAD_REFS[@]}" ] \
      || [ "${#PR_NUMBERS[@]}" -ne "${#PR_TIPS[@]}" ]; then
     echo "FAILED: PR number/head/branch/tip inventory mismatch" >&2
     exit 1
   fi
   # PR_DEPTHS: how many entries of COMMITS the landed head of each PR holds.
   total="${#COMMITS[@]}"
   PR_DEPTHS=()
   previous_depth=0
   for tip in "${PR_TIPS[@]}"; do
     depth=0
     for index in "${!COMMITS[@]}"; do
       if [ "${COMMITS[$index]}" = "$tip" ]; then
         depth=$((index + 1))
       fi
     done
     if [ "$depth" -lt 1 ] || [ "$depth" -lt "$previous_depth" ]; then
       echo "FAILED: PR tip $tip is not in COMMITS in train order" >&2
       exit 1
     fi
     PR_DEPTHS+=("$depth")
     previous_depth="$depth"
   done
   if [ "$previous_depth" -ne "$total" ]; then
     echo "FAILED: the last PR tip is not the last reviewed commit" >&2
     exit 1
   fi
   # A landed commit carries the committer identity of this clone. Without an
   # email git makes one from the host name, and the loop would push it.
   if [ -z "$(git config --get user.email)" ] && [ -z "${GIT_COMMITTER_EMAIL:-}" ]; then
     echo "FAILED: git user.email is not set: a landed commit would carry a committer address made from the host name, in a public repository. Set git config user.name and user.email in this clone." >&2
     exit 1
   fi
   verify_pr_head() {
     local pr="$1" expected="$2" live_ref actual
     case "$pr" in
       ''|*[!0-9]*) return 1 ;;
     esac
     live_ref="refs/tmp/review-loop-train-pr-$pr"
     if ! git fetch -q origin "+pull/$pr/head:$live_ref"; then
       return 1
     fi
     actual="$(git rev-parse --verify "$live_ref")" || return 1
     [ "$actual" = "$expected" ]
   }
   verify_frozen_pr_heads() {
     local index
     for index in "${!PR_NUMBERS[@]}"; do
       if ! verify_pr_head \
            "${PR_NUMBERS[$index]}" "${PR_HEADS[$index]}"; then
         return 1
       fi
     done
   }
   # GitHub marks a PR merged only when its head becomes reachable from its
   # base, and it deletes a merged PR's head branch while automatic deletion
   # is on. So every carried PR must be open, not a draft, from this
   # repository and based on main, with the recorded branch and frozen head,
   # and no open PR may still use a carried head branch as its base.
   verify_pr_github_state() {
     local index pr ref seen
     for index in "${!PR_NUMBERS[@]}"; do
       pr="${PR_NUMBERS[$index]}"
       ref="${PR_HEAD_REFS[$index]}"
       seen="$(gh pr view "$pr" \
         --json state,isDraft,isCrossRepository,baseRefName,headRefName,headRefOid \
         --jq '[.state, .isDraft, .isCrossRepository, .baseRefName, .headRefName, .headRefOid] | map(tostring) | join(" ")')" \
         || return 1
       [ "$seen" = "OPEN false false main ${ref} ${PR_HEADS[$index]}" ] || return 1
       seen="$(gh pr list --state open --base "$ref" --json number --jq length)" \
         || return 1
       [ "$seen" = 0 ] || return 1
     done
   }
   # The frozen head must stay reachable after its branch is rewritten and
   # after GitHub deletes that branch. Record it before any head moves.
   record_recovery_refs() {
     local index ref seen
     local -a specs
     specs=()
     for index in "${!PR_NUMBERS[@]}"; do
       ref="refs/review-loop/recovery/pr-${PR_NUMBERS[$index]}/${PR_HEADS[$index]}"
       specs+=("${PR_HEADS[$index]}:${ref}")
     done
     git push -q origin "${specs[@]}" || return 1
     for index in "${!PR_NUMBERS[@]}"; do
       ref="refs/review-loop/recovery/pr-${PR_NUMBERS[$index]}/${PR_HEADS[$index]}"
       seen="$(git ls-remote origin "$ref")" || return 1
       [ "${seen%%[[:space:]]*}" = "${PR_HEADS[$index]}" ] || return 1
       printf 'RECOVERY_REF %s %s\n' "${PR_NUMBERS[$index]}" "$ref"
     done
   }
   # One atomic push: every head moves, each under an exact lease on its
   # frozen SHA, or none does.
   move_pr_heads() {
     local index
     local -a leases specs
     leases=()
     specs=()
     for index in "${!PR_NUMBERS[@]}"; do
       leases+=("--force-with-lease=refs/heads/${PR_HEAD_REFS[$index]}:${PR_HEADS[$index]}")
       specs+=("${PR_LANDED[$index]}:refs/heads/${PR_HEAD_REFS[$index]}")
     done
     git push -q --atomic "${leases[@]}" origin "${specs[@]}"
   }
   verify_landed_pr_heads() {
     local index
     for index in "${!PR_NUMBERS[@]}"; do
       if ! verify_pr_head \
            "${PR_NUMBERS[$index]}" "${PR_LANDED[$index]}"; then
         return 1
       fi
     done
   }
   # refs/pull/<N>/head follows the head branch a few seconds late. Do not
   # push main until every PR shows the head this loop pushed.
   wait_for_landed_pr_heads() {
     local try
     for try in 1 2 3 4 5 6 7 8 9 10; do
       if verify_landed_pr_heads; then
         return 0
       fi
       sleep 3
     done
     return 1
   }
   # Undo this loop's own head push, each head under an exact lease on the
   # commit the loop pushed, so a head that someone else moved is left alone.
   restore_frozen_pr_heads() {
     local index ref failed
     failed=""
     for index in "${!PR_NUMBERS[@]}"; do
       ref="refs/heads/${PR_HEAD_REFS[$index]}"
       if ! git push -q \
            --force-with-lease="${ref}:${PR_LANDED[$index]}" \
            origin "${PR_HEADS[$index]}:${ref}"; then
         echo "NOT_RESTORED ${PR_NUMBERS[$index]}: ${ref} is off its frozen head, kept at refs/review-loop/recovery/pr-${PR_NUMBERS[$index]}/${PR_HEADS[$index]}" >&2
         failed=1
       fi
     done
     [ -z "$failed" ]
   }
   pr_shows_merged() {
     local pr="$1" try state
     for try in 1 2 3 4 5 6 7 8 9 10; do
       state="$(gh pr view "$pr" --json state --jq .state)" || state=""
       if [ "$state" = MERGED ]; then
         return 0
       fi
       sleep 3
     done
     return 1
   }
   refresh_manifest=""
   for commit in "${COMMITS[@]}"; do
     if git diff-tree --no-commit-id --name-only -r "$commit" -- \
          docs/audit/data/citation_graph_manifest.json \
          | grep -qx docs/audit/data/citation_graph_manifest.json; then
       refresh_manifest=1
       break
     fi
   done
   if ! git diff --quiet || ! git diff --cached --quiet; then
     echo "FAILED: landing worktree has tracked residue before integration" >&2
     exit 1
   fi
   landed=""
   for attempt in 1 2 3 4; do
     git cherry-pick --abort >/dev/null 2>&1 || true
     # A failed generator/write/add/amend may leave only the generated
     # manifest dirty after a completed cherry-pick. Restore exactly that path
     # to the current HEAD before retrying; never reset arbitrary reviewed work.
     if [ "$refresh_manifest" = 1 ] \
        && ! git restore --source=HEAD --staged --worktree -- \
             docs/audit/data/citation_graph_manifest.json; then
       echo "FAILED: could not clear generated manifest retry residue" >&2
       exit 1
     fi
     # Name the destination explicitly: isolated/partial repos may have no
     # remote.origin.fetch refspec, in which case a plain fetch leaves the
     # local origin/main stale and creates fake non-fast-forward "races".
     if ! { git fetch -q origin \
              +refs/heads/main:refs/remotes/origin/main \
            && git switch -q --detach origin/main; }; then
       sleep 3; continue
     fi
     if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then
       echo "FAILED: main moved; rebuild and rerun the combined gate" >&2
       exit 1
     fi
     cherry_pick_complete=""
     last_conflicted_commit=""
     if git cherry-pick "${COMMITS[@]}" >/dev/null 2>&1; then
       cherry_pick_complete=1
     fi
     # Continue the same sequencer through every manifest-only conflict.
     # A failed --continue may have advanced to a different commit; inspect
     # that new failure before deciding whether another repair is allowed.
     while [ -z "$cherry_pick_complete" ]; do
       if ! conflicts="$(git diff --name-only --diff-filter=U)"; then
         echo "FAILED: could not inspect cherry-pick conflicts" >&2
         exit 1
       fi
       if [ "$conflicts" != "docs/audit/data/citation_graph_manifest.json" ]; then
         git cherry-pick --abort >/dev/null 2>&1 || true
         echo "FAILED: source conflict or sequencer failure; return the unit to its worker" >&2
         exit 1
       fi
       if ! conflicted_commit="$(git rev-parse --verify CHERRY_PICK_HEAD)"; then
         echo "FAILED: manifest conflict has no identifiable cherry-pick head" >&2
         exit 1
       fi
       if [ "$conflicted_commit" = "$last_conflicted_commit" ]; then
         echo "FAILED: manifest repair made no sequencer progress" >&2
         exit 1
       fi
       last_conflicted_commit="$conflicted_commit"
       if ! { python3 docs/audit/scripts/run_citation_graph_build.py >/dev/null \
              && python3 docs/audit/scripts/write_citation_graph_manifest.py >/dev/null \
              && git add docs/audit/data/citation_graph_manifest.json; }; then
         echo "FAILED: manifest generation or staging during cherry-pick" >&2
         exit 1
       fi
       if GIT_EDITOR=true git cherry-pick --continue >/dev/null; then
         cherry_pick_complete=1
       fi
     done
     # A conflict-free textual merge can still coalesce independent manifest
     # counts. If this landing carries the manifest, rebuild it from the
     # integrated tree on every retry and amend only generated bytes.
     if [ "$refresh_manifest" = 1 ]; then
       if ! { python3 docs/audit/scripts/run_citation_graph_build.py >/dev/null \
              && python3 docs/audit/scripts/write_citation_graph_manifest.py >/dev/null \
              && git add docs/audit/data/citation_graph_manifest.json; }; then
         echo "FAILED: final manifest generation or staging" >&2
         exit 1
       fi
       if ! git diff --cached --quiet; then
         if ! GIT_EDITOR=true git commit --amend --no-edit >/dev/null; then
           echo "FAILED: could not commit regenerated manifest" >&2
           exit 1
         fi
       fi
     fi
     if [ "$(git rev-parse 'HEAD^{tree}')" != "$VALIDATED_TREE" ]; then
       echo "FAILED: integrated tree differs from the validated candidate" >&2
       exit 1
     fi
     # The candidate is one new commit per reviewed commit on the gated base,
     # so the landed head of each PR is the commit that completes its share.
     if [ "$(git rev-list --count "$VALIDATED_BASE"..HEAD)" != "$total" ]; then
       echo "FAILED: candidate is not one commit per reviewed commit" >&2
       exit 1
     fi
     PR_LANDED=()
     for index in "${!PR_NUMBERS[@]}"; do
       depth="${PR_DEPTHS[$index]}"
       if ! stacked="$(git rev-parse --verify "HEAD~$((total - depth))^{commit}")"; then
         echo "FAILED: could not name the landed head of PR ${PR_NUMBERS[$index]}" >&2
         exit 1
       fi
       PR_LANDED+=("$stacked")
     done
     if ! verify_frozen_pr_heads; then
       echo "FAILED: PR head moved; dissolve the train without pushing" >&2
       exit 1
     fi
     if ! verify_pr_github_state; then
       echo "FAILED: a carried PR is not open on main from its recorded branch, or an open PR is based on a carried head; nothing was pushed" >&2
       exit 1
     fi
     if ! record_recovery_refs; then
       echo "FAILED: could not record every recovery ref; no head was moved" >&2
       exit 1
     fi
     if ! move_pr_heads; then
       echo "FAILED: leased head push refused; no head was moved" >&2
       exit 1
     fi
     if ! wait_for_landed_pr_heads; then
       echo "FAILED: a PR does not show the pushed head; main was not pushed" >&2
       restore_frozen_pr_heads
       exit 1
     fi
     if git push -q origin HEAD:main; then
       landed="$(git rev-parse HEAD)"
       break
     fi
     # The remote may have accepted the push although this client saw an
     # error. Land on containment; otherwise undo the head push and retry.
     if git fetch -q origin +refs/heads/main:refs/remotes/origin/main \
        && git merge-base --is-ancestor HEAD origin/main; then
       landed="$(git rev-parse HEAD)"
       break
     fi
     if ! restore_frozen_pr_heads; then
       echo "FAILED: main was not updated and a PR head could not be restored" >&2
       exit 1
     fi
     sleep 3
   done
   if [ -z "$landed" ]; then
     echo "FAILED: landing did not complete after 4 attempts" >&2
     exit 1
   fi
   if ! git fetch -q origin \
          +refs/heads/main:refs/remotes/origin/main; then
     echo "FAILED: could not refresh origin/main for containment verification" >&2
     exit 1
   fi
   if ! git merge-base --is-ancestor "$landed" origin/main; then
     echo "FAILED: $landed not contained in origin/main" >&2
     exit 1
   fi
   echo "LANDED $landed"
   # Report each PR from a post-push head check. The lander closes nothing
   # and merges nothing: GitHub marks a PR merged once main holds its head.
   for index in "${!PR_NUMBERS[@]}"; do
     pr="${PR_NUMBERS[$index]}"
     expected="${PR_LANDED[$index]}"
     if ! verify_pr_head "$pr" "$expected"; then
       echo "LEAVE_OPEN $pr: PR head moved after landing" >&2
     elif pr_shows_merged "$pr"; then
       printf 'MERGED %s %s %s\n' "$pr" "${PR_HEADS[$index]}" "$expected"
     else
       echo "NOT_MERGED $pr: main holds $expected but GitHub does not show the PR merged" >&2
     fi
   done
}

land_train "$@"; exit
