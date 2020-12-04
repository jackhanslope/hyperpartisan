module clean
using LightXML
using JSON

struct Article
    id::Integer
    title::AbstractString
    content::AbstractString
    label::Bool
end

function articles_from_xml(article_file, truth_file)
    labels = Dict(
        parse(Int, attribute(c, "id")) => parse(Bool, attribute(c, "hyperpartisan"))
        for c in child_elements(root(parse_file(truth_file)))
    )
    articles = [
        Article(
            parse(Int, attribute(c, "id")),
            attribute(c, "title"),
            content(c),
            labels[parse(Int, attribute(c, "id"))],
        ) for c in child_elements(root(parse_file(article_file)))
    ]
    articles
end

function articles_to_json(articles, file_path)
    open(file_path, "w") do io
        write(io, JSON.json(articles))
    end
end

function run(inp_file, truth_file, out_file)
    articles = articles_from_xml(inp_file, truth_file)
    articles_to_json(articles, out_file)
end

function main()
    if length(ARGS) != 2
        println(stderr, "Incorrect number of arguments given.")
        exit(1)
    end
    run(ARGS[1], ARGS[2])
    println("Clean data written to $(ARGS[2])")
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end

end # module
