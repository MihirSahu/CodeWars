fn grow(nums: Vec<i32>) -> i32 {

    let mut output: i32 = 1;

    for i in 0..nums.len() {
        output = nums[i] * output;
    }

    output
}

fn main() {
    println!("{}", grow([1, 2, 3, 4].to_vec()));
}
