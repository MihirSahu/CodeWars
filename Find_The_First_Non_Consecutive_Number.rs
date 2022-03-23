fn first_non_consecutive(arr: &Vec<i32>) -> Option<i32> {
    for i in 0..arr.len() {
        if i == 0 {
            continue;
        }
        if (arr[i - 1] + 1) != arr[i] {
            return Some(arr[i]);
        }
    }
    return None;
}

fn main() {

    let _arr = vec![1,2,3,4,6,7,8];
    first_non_consecutive(&_arr);

}
