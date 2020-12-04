using clean
using Test

@testset "clean.jl" begin
    @test clean.Article(123, "hello", "world") == clean.Article("000123", "hello", "world")

    articles = clean.articles_from_xml("data/articles.xml", "data/truth.xml")
    @test articles[3] == clean.Article(678787, "Jack is good", "As the title says.", true)
    @test articles[1].id == 643
    @test !articles[1].label
    @test articles[2].title ==
          "Hollywood Actors Who Condemn Trump but Were Silent on Weinstein"

    rm("data/tmp.json", force=true)
    clean.articles_to_json(articles, "data/tmp.json")
    tmp, cln = open("data/tmp.json", "r"), open("data/clean.json", "r")
    @test readlines(cln) == readlines(tmp)
    rm("data/tmp.json", force=true)
    close(tmp), close(cln)

    rm("data/tmp.json", force=true)
    clean.run("data/articles.xml", "data/truth.xml", "data/tmp.json")
    tmp, cln = open("data/tmp.json", "r"), open("data/clean.json", "r")
    @test readlines(cln) == readlines(tmp)
    rm("data/tmp.json", force=true)
    close(tmp), close(cln)
end
