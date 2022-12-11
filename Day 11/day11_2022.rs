//== The one with the monkey business ==//
// this is mostly a hack job, I don't understand some of what I've used
// because this is my first Rust program and I just Googled a lot

use std::{io::Error};

#[derive(Debug, Clone,Copy, PartialEq, Eq)]
enum Operation {Multiply,Add,Square}


#[derive(Debug, Clone, PartialEq, Eq)]
struct Monkey{
    items: Vec<i128>,
    operator: Operation,
    operatee: i128,
    test: i128,
    true_dest: usize,
    false_dest: usize
}  


fn main() -> Result<(), Error> {
    let lines = std::fs::read_to_string("input.txt")?;
    let monkeys = lines.split("\n\n").map(read_monkey).collect::<Vec<_>>();
    let part1 = solve(monkeys.clone(), 20, true);
    let part2 = solve(monkeys, 10000, false);

    println!("Part 1: {:?}\nPart 2: {}", part1, part2);
    Ok(())
}

fn solve(mut monkeys: Vec<Monkey>, cycles: usize, part1:bool) -> i128 {
    let mut count = vec![0_i128; monkeys.len()];
    let lcm:i128 = monkeys.iter().map(|m| m.test).product();
    
    for _ in 0.. cycles{
        for i in 0.. monkeys.len() {
            let monkey = monkeys.get(i).unwrap().clone();
            for item in monkey.items {
                count[i] +=1;
                let worry = (match monkey.operator {
                    Operation::Multiply => item * monkey.operatee,
                    Operation::Add => item + monkey.operatee,
                    Operation::Square => item * item,
                } / if part1 {3} else {1}) % lcm;
                if worry % monkey.test == 0 {
                    monkeys.get_mut(monkey.true_dest).unwrap().items.push(worry);
                } else {
                    monkeys.get_mut(monkey.false_dest).unwrap().items.push(worry);
                }

            }
            monkeys[i].items = Vec::new();
        }
    }
    count.sort_by(|a,b| b.cmp(&a));
    count[0] * count[1]
}


fn read_monkey(monkey_str: &str) -> Monkey {
    let mut lines = monkey_str.lines();
    lines.next();
    let initial_items = lines.next().unwrap()[18..].split(", ").map(|x| x.parse::<i128>().unwrap()).collect::<Vec<_>>();
    let op = lines.next().unwrap();
    let operator;
    let operatee;
    if &op[23..] == "* old" {
        operator = Operation::Square;
        operatee = 0;
    } else {
        operator = if op.chars().nth(23).unwrap() == '+' {Operation::Add} else {Operation::Multiply};
        operatee = op[25..].parse::<i128>().unwrap();
    }
    let test = lines.next().unwrap()[21..].parse::<i128>().unwrap();
    let true_dest = lines.next().unwrap()[29..].parse::<usize>().unwrap();
    let false_dest = lines.next().unwrap()[30..].parse::<usize>().unwrap();


    Monkey { items: initial_items, operator, operatee, test, true_dest, false_dest }
}