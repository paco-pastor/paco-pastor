#!/bin/bash

if [ -f ".nvmrc" ]; then
    NODE_VERSION=$(cat .nvmrc)

    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

    if [ -z "$(nvm ls $NODE_VERSION | grep $NODE_VERSION)" ]; then
        nvm install $NODE_VERSION
    fi
    nvm use $NODE_VERSION
fi
