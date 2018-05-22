#!/bin/bash

for testScript in `ls lib/tests/test_*py`
do
    python ${testScript} -v
done

