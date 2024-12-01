#!/bin/bash

SCRIPTPATH="$(
    cd -- "$(dirname "$0")" >/dev/null 2>&1 || exit 1
    pwd -P
)"
export day_number="${1:?Need day number}"
year="${2:-2024}"

touch "${SCRIPTPATH}/../${year}/inputs/${day_number}.txt"
envsubst <"${SCRIPTPATH}/template.py.tpl" >"${SCRIPTPATH}/../${year}/day${day_number}.py"
