module clean
using LightXML
using JSON

struct Article
    id::Integer
    title::Any
    content::Any
end

function Article(id::AbstractString, title, content)
    Article(parse(Int, id), title, content)
end

function articles_from_xml(file_path)
    xroot = root(parse_file(file_path))
    [
        Article(attribute(c, "id"), attribute(c, "title"), content(c))
        for c in child_elements(xroot)
    ]
end

function articles_to_json(articles, file_path)
    open(file_path, "w") do io
        write(io, JSON.json(articles))
    end
end

function run(inp_file, out_file)
    articles = articles_from_xml(inp_file)
    articles_to_json(articles, out_file)
end

end # module
