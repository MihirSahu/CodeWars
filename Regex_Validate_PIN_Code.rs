fn validate_pin(pin: &str) -> bool {
	let mut num_digits = 0;

	for character in pin.chars() {
		if character.is_numeric() {
			num_digits = num_digits + 1;
		}
		else {
			return false;
		}
	}

	if num_digits == 4 || num_digits == 6 {
		return true;
	}

	return false;
}

fn main() {
	println!("{}", validate_pin("1234"));
	println!("{}", validate_pin("12345"));
	println!("{}", validate_pin("a234"));
}
