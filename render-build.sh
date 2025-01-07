#!/usr/bin/env bash
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
    echo "Installing Chrome..."
    mkdir -p $STORAGE_DIR/chrome
    cd $STORAGE_DIR/chrome
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
    rm ./google-chrome-stable_current_amd64.deb
fi

if [[ ! -d $STORAGE_DIR/chromedriver ]]; then
    echo "Installing Chromedriver..."
    mkdir -p $STORAGE_DIR/chromedriver
    cd $STORAGE_DIR/chromedriver
    CHROMEDRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
    wget -q "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip"
    unzip chromedriver_linux64.zip
    rm chromedriver_linux64.zip
fi
