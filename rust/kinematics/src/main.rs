fn differential_drive(linear: f64, angular: f64, wheel_base: f64) -> (f64, f64) {
    let left = linear - angular * wheel_base / 2.0;
    let right = linear + angular * wheel_base / 2.0;
    (left, right)
}

fn main() {
    let (left, right) = differential_drive(0.4, 0.8, 0.18);
    println!("left_wheel={:.3} m/s right_wheel={:.3} m/s", left, right);
}
