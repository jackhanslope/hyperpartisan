module clean
using LightXML

struct Article
    id::Integer
    title::Any
    content::Any
end

function Article(id::AbstractString, title, content)
    Article(parse(Int, id), title, content)
end

function articles_from_file(file_path)
    xroot = root(parse_file(file_path))
    [
        Article(attribute(c, "id"), attribute(c, "title"), content(c))
        for c in child_elements(xroot)
    ]
end

end # module
