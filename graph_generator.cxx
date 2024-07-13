#include "graph_generator.hxx"

int main()
{
    int b = 2;
    std::string a = "abc";
    graph_generator gr(a);
    std::cout << gr.graph_file << "\n";
    return 0;
}