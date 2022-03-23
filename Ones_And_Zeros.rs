/*
def binary_array_to_number(arr):
	output = 0
	arr.reverse()

	for idx, i in enumerate(arr):
		if i == 1:
			output = output + 2**idx
		else:
			continue
	return output
*/

fn binary_slice_to_number(slice: Vec<u32>) -> u32 {
	
	let mut output: u32 = 0;
	let base: u32 = 2;
	let mut temp = slice.iter().rev();
	let one: u32 = 1;
	let zero: u32 = 0;
	
	for i in 0..temp.len() {
		if *temp.nth(i).unwrap() == zero {
			continue;
		}
		else if *temp.nth(i).unwrap() == one {
			output = output + base.pow(i as u32);
		}
	}

	return output;
}

fn main() {
	
	println!("{}", binary_slice_to_number(vec![0,0,0,1]));
	println!("{}", binary_slice_to_number(vec![0,0,1,0]));
	println!("{}", binary_slice_to_number(vec![1,1,1,1]));
	println!("{}", binary_slice_to_number(vec![0,1,1,0]));
}
