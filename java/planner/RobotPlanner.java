import java.util.ArrayList;
import java.util.List;

public class RobotPlanner {
    record Point(int x, int y) {}

    public static List<Point> straightLinePlan(Point start, Point goal) {
        List<Point> path = new ArrayList<>();
        int x = start.x();
        int y = start.y();
        path.add(new Point(x, y));

        while (x != goal.x() || y != goal.y()) {
            if (x < goal.x()) x++;
            else if (x > goal.x()) x--;

            if (y < goal.y()) y++;
            else if (y > goal.y()) y--;

            path.add(new Point(x, y));
        }
        return path;
    }

    public static void main(String[] args) {
        List<Point> path = straightLinePlan(new Point(0, 0), new Point(4, 3));
        path.forEach(System.out::println);
    }
}
