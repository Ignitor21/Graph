#include <vector>

class graph
{
public:
    graph() = default;
    virtual visualize() const = 0;
    void set_size();
protected:
    std::vector<std::vector<int>> table;

}
