#!/bin/sh
# Run after root preserves/commits the accepted source and supplies its verified HEAD.
# A failed guard retains the slot and all artifacts; never force-clean this pool.
set -eu
: "${1:?Supply the independently verified final HEAD}"
exec python3 /Users/jonBridger/.codex/skills/review-loop/scripts/review_workspace.py release --repo /private/tmp/review-drain-20260915/coordinator --pool /private/tmp/review-drain-20260915/author-pool --slot author-backlog --owner PR8052-8053-8058 --expected-head "$1"
