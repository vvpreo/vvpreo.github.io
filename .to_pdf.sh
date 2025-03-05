#!/bin/zsh

#brew install basictex pandoc

pandoc --from=gfm --to=pdf -o README.pdf README.md