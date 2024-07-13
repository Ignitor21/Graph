#include <iostream>
#include <string>
#include <string_view>

struct graph_generator
{
    std::string command;
    std::string graph_file{"../graphics/graph.dot"};
    graph_generator() = default;
    graph_generator(std::string_view str) : command(str) {}

};
