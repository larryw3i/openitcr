#!/usr/bin/bash

git_push(){
    echo 'Push to git@gitee.com:larryw3i/openitcr.git'
    git push git@gitee.com:larryw3i/openitcr.git

    echo 'Push to git@github.com:larryw3i/openitcr.git'
    git push git@github.com:larryw3i/openitcr.git
}

test(){
    python3 -c 'from tests import test_0; test_0()'
}

$1