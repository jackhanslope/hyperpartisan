module cleaner
using LightXML
using JSON

"""
    Article(id::Integer, title::AbstractString, content::AbstractString, label::Bool)

Return an `Article` type.

# Examples
```julia-repl
julia> a = cleaner.Article(123, "Title", "Some content.", true)
cleaner.Article(123, "Title", "Some content.", true)
```
"""
struct Article
    id::Integer
    title::AbstractString
    content::AbstractString
    label::Bool
end

"""
    Article(id::AbstractString, title, content, label::AbstractString)

Return an `Article` type with `id` and `label` parsed into the correct types.

# Examples
```julia-repl
julia> a = cleaner.Article("123", "Title", "Some content.", "true")
cleaner.Article(123, "Title", "Some content.", true)
```
"""
Article(id::AbstractString, title, content, label::AbstractString) =
    Article(parse(Int, id), title, content, parse(Bool, label))

"""
    articles_from_xml(article_file, truth_file)

Return an array of `Article`s corresponding to articles in the inputs.

# Arguments
- `from_file`: the path the the xml file containing the articles
- `truth_file`: the path the the xml file containing the ground truth for the articles
"""
function articles_from_xml(article_file, truth_file)
    labels = Dict(
        attribute(c, "id") => attribute(c, "hyperpartisan")
        for c in child_elements(root(parse_file(truth_file)))
    )
    [
        Article(
            attribute(c, "id"),
            attribute(c, "title"),
            content(c),
            labels[attribute(c, "id")],
        ) for c in child_elements(root(parse_file(article_file)))
    ]
end

"""
    articles_to_json(articles)

Return a JSON serialized object of the array of `Article`s.

# Arguments
- `articles`: an array of `Article` objects
"""
articles_to_json(articles) = JSON.json(articles)

"""
    run(article_file, truth_file)

Return a JSON object of the articles from the `article_file` with ground truths from the `truth_file`.
"""
run(article_file, truth_file) =
    articles_to_json(articles_from_xml(article_file, truth_file))

"""
    main()

Execute the `run` funciton with the specified command line arguments.
"""
function main()
    if length(ARGS) != 2
        println(stderr, "Incorrect number of arguments given.")
        exit(1)
    end
    println(run(ARGS[1], ARGS[2]))
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end

end # module
