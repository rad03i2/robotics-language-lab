#include <iostream>
#include <vector>

class OccupancyGrid {
public:
    OccupancyGrid(int width, int height) : width_(width), height_(height), cells_(width * height, 0) {}

    void markObstacle(int x, int y) {
        if (inside(x, y)) {
            cells_[index(x, y)] = 1;
        }
    }

    bool isFree(int x, int y) const {
        return inside(x, y) && cells_[index(x, y)] == 0;
    }

    void print() const {
        for (int y = 0; y < height_; ++y) {
            for (int x = 0; x < width_; ++x) {
                std::cout << (cells_[index(x, y)] ? '#' : '.');
            }
            std::cout << '\n';
        }
    }

private:
    int width_;
    int height_;
    std::vector<int> cells_;

    bool inside(int x, int y) const {
        return x >= 0 && y >= 0 && x < width_ && y < height_;
    }

    int index(int x, int y) const {
        return y * width_ + x;
    }
};

int main() {
    OccupancyGrid grid(8, 5);
    grid.markObstacle(2, 1);
    grid.markObstacle(2, 2);
    grid.markObstacle(3, 2);
    grid.print();
}
