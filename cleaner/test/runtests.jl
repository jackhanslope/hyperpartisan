using cleaner
using Test

@testset "cleaner.jl" begin
    @testset "two argument" begin
        articles = cleaner.articles_from_xml("data/articles.xml", "data/truth.xml")
        @test articles[3] == cleaner.Article(678787, "Jack is good", "As the title says.", true)
        @test articles[1].id == 643
        @test !articles[1].label
        @test articles[2].title ==
              "Hollywood Actors Who Condemn Trump but Were Silent on Weinstein"

        open("data/clean.json", "r") do io
            @test readlines(io)[1] == cleaner.articles_to_json(articles)
        end

        open("data/clean.json", "r") do io
            @test readlines(io)[1] == cleaner.run("data/articles.xml", "data/truth.xml")
        end
    end # "two argument"

    @testset "one argument" begin
        articles = cleaner.articles_from_xml("data/articles.xml")
        @test articles[3] == cleaner.Article(678787, "Jack is good", "As the title says.", nothing)
        @test articles[1].id == 643
        @test isnothing(articles[1].label)
        @test articles[2].title ==
              "Hollywood Actors Who Condemn Trump but Were Silent on Weinstein"
    end # "one argument"

end # cleaner.jl
