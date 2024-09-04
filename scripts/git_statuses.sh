#!/bin/bash

for dir in ~/dev/*; do
    if [ -d "$dir" ]; then
        cd "$dir"
        if [ -d ".git" ]; then
            git diff --quiet
            CODE=$?
            if [ $CODE == 1 ]; then
                BASENAME=$(basename "$dir")
                echo -e "Changes in \033[0;31m$BASENAME\033[0m"
            fi
        fi
    fi
done