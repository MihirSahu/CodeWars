fn reverse_seq(n: u32) -> Vec<u32> {

    let mut _arr = Vec::new();

    for i in (1..n+1).rev() {
        _arr.push(i);
    }

    return _arr;
}

fn main() {

    let _n = 5;
    let _arr = reverse_seq(_n);

    for i in 0..5 {
        println!("{}", _arr[i]);
    }

}
