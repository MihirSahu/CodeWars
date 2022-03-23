use std::io;


fn solution(s: &str) -> Vec<String> {
	let mut v: Vec<String> = Vec::new();

	// This variable changed the functionality between my local rust binary and the code on CodeWars. the '- 1' works on my but not on CodeWars
	let length = s.chars().count() - 1;
	let mut left_bound: usize = 0;
	let mut right_bound: usize = 2;

	if length % 2 == 0 {
		for character in 0..length/2 {
			v.push((&s[left_bound..right_bound]).to_string());
			left_bound = left_bound + 2;
			right_bound = right_bound + 2;
		}
	}
	else {
		for character in 0..(length - 1)/2 {
			v.push((&s[left_bound..right_bound]).to_string());
			left_bound = left_bound + 2;
			right_bound = right_bound + 2;
		}
		v.push((&s[left_bound..right_bound - 1]).to_string() + "_")
	}

	return v;
}

fn main() {
	
	let mut input = String::new();
	io::stdin()
		.read_line(&mut input)
		.expect("Couldn't read input");
	
	for characters in solution(&input) {
		println!("{}", characters);
	}
}
