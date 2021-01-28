#!/usr/bin/env fish
# run the pipeline

set -lx WORK_DIR $PWD
set -lx DATA_FILE $WORK_DIR/$argv[1]
set -lx OUT_DIR $argv[2]
set -lx PICKLE_FILE $WORK_DIR/$argv[3]
mkdir -p $OUT_DIR/tmp

# clean with julia code
cd $WORK_DIR/cleaner
echo Changed dir to $WORK_DIR/cleaner
echo Running cleaning
julia src/cleaner.jl $DATA_FILE > $OUT_DIR/tmp/clean.json
echo Cleaning complete
echo

# run the python pipeline
cd $WORK_DIR/processing
echo Changed dir to $WORK_DIR/processing
echo Running prediction
.venv/bin/python run.py predict $OUT_DIR/tmp/clean.json $PICKLE_FILE > $OUT_DIR/prediction.txt
echo Prediction written to $OUT_DIR/prediction.txt
