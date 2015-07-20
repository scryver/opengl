#!/bin/sh

cd core/build
cmake ..
make
cd ../..

cd game
. ~/.virtualenvs/ctest/bin/activate
python core_build.py
python game.py
