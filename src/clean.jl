module clean

struct Article 
    id::Integer
    title
    content
end

function Article(id::AbstractString, title, content)
    Article(
        parse(Int, id),
        title,
        content,
    )
end

end # module
