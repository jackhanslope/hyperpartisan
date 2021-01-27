#!/usr/bin/env fish
# run the pipeline

set -lx WORK_DIR $PWD
set -lx DATA_FILE $WORK_DIR/$argv[1]
set -lx OUT_DIR $argv[2]
set -lx PICKLE_FILE $WORK_DIR/$argv[3]
mkdir -p $OUT_DIR/tmp

# clean with julia code
cd $WORK_DIR/cleaner
julia src/cleaner.jl $DATA_FILE > $OUT_DIR/tmp/clean.json

# run the python pipeline
cd $WORK_DIR/processing
.venv/bin/python run.py predict $OUT_DIR/tmp/clean.json $PICKLE_FILE > $OUT_DIR/prediction.txt
