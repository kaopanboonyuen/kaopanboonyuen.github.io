#!/bin/bash

# Ensure Hugo 0.119.0 is used
HUGO_VERSION="0.119.0"

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "Hugo could not be found, please install Hugo version $HUGO_VERSION"
    exit
fi

# Check if the installed version is the required version
INSTALLED_HUGO_VERSION=$(hugo version | awk '{print $5}' | sed 's/v//g')

if [ "$INSTALLED_HUGO_VERSION" != "$HUGO_VERSION" ]; then
    echo "Installed Hugo version ($INSTALLED_HUGO_VERSION) does not match required version ($HUGO_VERSION)"
    exit
fi

echo "Using Hugo version $HUGO_VERSION"

# Clean the public directory
rm -rf public

# Build the project.
hugo -D

# Go to the public directory and create a git repository.
cd public
git init

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
    msg="$*"
fi
git commit -m "$msg"

# Set up the remote repository and push to gh-pages branch.
git remote add origin git@github.com:kaopanboonyuen/kaopanboonyuen.github.io.git
git branch -M gh-pages
git push -f origin gh-pages

# Come back to the root of the project.
cd ..