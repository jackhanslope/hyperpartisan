# cleaner

Julia package for cleaning the data.

## running
- Run `julia src/cleaner.jl <article_file> <truth_file>` to output a json object to stdout
- Run `julia src/cleaner.jl <article_file> <truth_file> > foo.json` to write the json object to the `foo.json` file

## docs
- run `julia docs/make.jl` to build the documentation
- `cd` into `docs/build` and run a http server. For example `python -m http.server 8000`

## tests
- To run the tests, enter the julia REPL and then `] test`
