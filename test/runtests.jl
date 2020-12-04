using cleaner
using Test

@testset "clean.jl" begin
    articles = clean.articles_from_xml("data/articles.xml", "data/truth.xml")
    @test articles[3] == clean.Article(678787, "Jack is good", "As the title says.", true)
    @test articles[1].id == 643
    @test !articles[1].label
    @test articles[2].title ==
          "Hollywood Actors Who Condemn Trump but Were Silent on Weinstein"

    open("data/clean.json", "r") do io
        @test readlines(io)[1] == clean.articles_to_json(articles)
    end

    open("data/clean.json", "r") do io
        @test readlines(io)[1] == clean.run("data/articles.xml", "data/truth.xml")
    end

end # testcase
