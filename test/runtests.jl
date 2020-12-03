using clean
using Test

@testset "clean.jl" begin
    @test clean.Article(123, "hello", "world") == clean.Article("000123", "hello", "world")
end
