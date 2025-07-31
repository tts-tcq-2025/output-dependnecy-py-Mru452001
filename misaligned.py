def get_colour_pairs():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    pairs=[]
    pair_number=1
    for i in enumerate(major_colors):
        for j in enumerate(minor_colors):
            pairs.append((pair_number,i,j))
            pair_number+=1
    return pairs

def print_color_map():
    pairs=get_colour_pairs()
    for number,major,minor in pairs:
        print(f"{number} | {major} | {minor}")
    return len(pairs)
result = print_color_map()
assert(result == 25)
print("All is well (maybe!)")
