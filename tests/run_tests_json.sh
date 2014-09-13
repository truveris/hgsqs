#!/bin/sh
#
# This is a shitty regression test that creates two repositories and returns
# the output from hgsqs if successful. If everything works fine, the output
# will be two JSON lines representing the two fake commits made to the local
# repository and pushed to a fake remote repository.
#

test_path=`pwd`
base_path=`dirname $test_path`
hgsqs_path=$base_path/hgsqs

# $1 - msg
die() {
	echo "error: $1"
	exit 1
}

rm -rf test_*

# Create two test repositories.
hg init test_origin > test_hg_init.log || die "hg init failed"
hg clone test_origin test_local > test_hg_clone.log || die "hg clone failed"

# Create a config file that would trigger hgsqs when pushing to "origin".
cat >test_origin/.hg/hgrc<<EOF
[hooks]
incoming.hgsqs = $hgsqs_path --json

[hgsqs]
aws_access_key_id = AK..................
aws_secret_access_key = ............/.........../...............
queues = krokorok-hg
EOF

# Commit things.
{
	echo "Something" > test_local/my_file
	hg -R test_local add test_local/my_file
	hg -R test_local commit -m "added my_file"
	hg -R test_local branch anything-1.2
	echo "Something" > test_local/other_file
	hg -R test_local add test_local/other_file
	hg -R test_local commit -m "added other_file"
} > test_create_repo.log

hg -R test_local push > test_hg_push.log
tail -n 2 test_hg_push.log

rm -rf test_*
