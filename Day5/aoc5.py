def part1():
    blocks_dict= {
        "list_1": ["D", "L", "V", "T", "M", "H", "F"],
        "list_2": ["H", "Q", "G", "J", "C", "T", "N", "P"],
        "list_3": ["R", "S", "D", "M", "P", "H"],
        "list_4": ["L", "B", "V", "F"],
        "list_5": ["N", "H", "G", "L", "Q"],
        "list_6": ["W", "B", "D", "G", "R", "M", "P"],
        "list_7": ["G", "M", "N", "R", "C", "H", "L", "Q"],
        "list_8": ["C", "L", "W"],
        "list_9": ["R", "D", "L", "Q", "J", "Z", "M", "T"]
    }

    with open("input.txt") as file:
        for line in file:
            numbers = line.split('move')[1].strip()
            number_of_blocks = int(numbers.split("from")[0].strip())
            print(number_of_blocks)
            beginning_list = int(line.split("from")[1].split("to")[0])
            ending_list = int(line.split("from")[1].split("to")[1])
            blocks = blocks_dict[f"list_{beginning_list}"][-number_of_blocks:]
            blocks_list = blocks[::-1]
            for block in blocks_list:
                blocks_dict[f"list_{beginning_list}"].pop()
                blocks_dict[f"list_{ending_list}"].append(block)

    for list in blocks_dict:
        print(blocks_dict[list][-1])


def part2():
    blocks_dict= {
        "list_1": ["D", "L", "V", "T", "M", "H", "F"],
        "list_2": ["H", "Q", "G", "J", "C", "T", "N", "P"],
        "list_3": ["R", "S", "D", "M", "P", "H"],
        "list_4": ["L", "B", "V", "F"],
        "list_5": ["N", "H", "G", "L", "Q"],
        "list_6": ["W", "B", "D", "G", "R", "M", "P"],
        "list_7": ["G", "M", "N", "R", "C", "H", "L", "Q"],
        "list_8": ["C", "L", "W"],
        "list_9": ["R", "D", "L", "Q", "J", "Z", "M", "T"]
    }

    with open("input.txt") as file:
        for line in file:
            numbers = line.split('move')[1].strip()
            number_of_blocks = int(numbers.split("from")[0].strip())
            beginning_list = int(line.split("from")[1].split("to")[0])
            ending_list = int(line.split("from")[1].split("to")[1])
            blocks = blocks_dict[f"list_{beginning_list}"][-number_of_blocks:]
            for block in blocks:
                blocks_dict[f"list_{beginning_list}"].pop()
                blocks_dict[f"list_{ending_list}"].append(block)

    for list in blocks_dict:
        print(blocks_dict[list][-1])
        

print("Part 1: \n")      
part1()

print("Part 2: \n")
part2()