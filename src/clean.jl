module clean
using LightXML
using JSON

struct Article
    id::Integer
    title::AbstractString
    content::AbstractString
    label::Bool
end

Article(id::AbstractString, title, content, label::AbstractString) =
    Article(parse(Int, id), title, content, parse(Bool, label))

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

articles_to_json(articles) = JSON.json(articles)

function run(article_file, truth_file)
    articles = articles_from_xml(article_file, truth_file)
    articles_to_json(articles)
end

function main()
    if length(ARGS) != 2
        println(stderr, "Incorrect number of arguments given.")
        exit(1)
    end
    run(ARGS[1], ARGS[2])
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end

end # module
