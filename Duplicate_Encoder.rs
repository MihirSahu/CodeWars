fn duplicate_encode(word:&str)->String {

    let mut duplicate: Vec<char> = Vec::new();
    let mut output = String::new();

    for i in 0..word.chars().count() {
        if duplicate.contains(&(word.chars().nth(i).unwrap())) != true {
            duplicate.push(word.chars().nth(i).unwrap());
            println!("Pushed {}", word.chars().nth(i).unwrap());
        }
    }

    for i in 0..duplicate.len() {
        println!("{}", duplicate[i]);
    }

    for i in 0..word.chars().count() {
        if duplicate.contains(&(word.chars().nth(i).unwrap())) == true {
            output = format!("{})", output);
            println!("Appended {}", word.chars().nth(i).unwrap());
        }
        else {
            output = format!("{}(", output);
        }
    }

    return output;
}

fn main() {
    println!("{}", duplicate_encode("recede"));
}
