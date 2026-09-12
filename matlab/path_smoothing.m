% Simple path smoothing example for MATLAB or Octave.
points = [0 0; 1 0.8; 2 1.2; 3 1.1; 4 2.0; 5 2.2];
window = 3;
smoothed = points;

for i = 2:size(points, 1)-1
    startIndex = max(1, i - floor(window / 2));
    endIndex = min(size(points, 1), i + floor(window / 2));
    smoothed(i, :) = mean(points(startIndex:endIndex, :), 1);
end

disp('Original path:');
disp(points);
disp('Smoothed path:');
disp(smoothed);
