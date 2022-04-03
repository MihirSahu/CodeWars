fn count_sheep(sheepL: &[bool]) -> u8 {
    let mut count: u8 = 0;
    for i in sheepL {
        if *i == true {
            count = count + 1;
        }
        else {
            continue;
        }
    }
    return count;
}

fn main() {

    println!("{}", count_sheep(&[true,  true,  true,  false, true,  true,  true,  true , true,  false, true,  false, true,  false, false, true , true,  true,  true,  true ,false, false, true,  true]));
}
