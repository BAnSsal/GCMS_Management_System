from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException

def print_separator():
    print("\n" + "-"*80 + "\n")
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.key)
        print_tree(node.left, level + 1)
        
if __name__ == "_main_":
    # Initialize GCMS
    gcms = GCMS()
    
    # Adding an initial set of bins with varying capacities
    initial_bin_data = [
        (1001, 50),
        (1002, 30),
        (1003, 40),
        (1004, 25),
        (1005, 35),
        (1006, 60),
        (1007, 45),
        (1008, 55),
        (1009, 20),
        (1010, 70)
    ]
    
    # print("Adding Initial Bins:")
    for bin_id, capacity in initial_bin_data:
        gcms.add_bin(bin_id, capacity)
        # print(f"Added Bin ID: {bin_id}, Capacity: {capacity}")
    

    
    # Adding an initial set of objects with varying sizes and colors
    initial_object_data = [
        (2001, 20, Color.RED),
        (2002, 15, Color.GREEN),
        (2003, 10, Color.GREEN),
        (2004, 25, Color.GREEN),
        (2005, 30, Color.RED),
        (2006, 5, Color.GREEN),
        (2007, 8, Color.GREEN),
        (2008, 22, Color.GREEN),
        (2009, 35, Color.GREEN),
        (2010, 40, Color.RED),
        (2011, 12, Color.GREEN),
        (2012, 18, Color.GREEN),
        (2013, 7, Color.GREEN),
        (2014, 28, Color.RED),
        (2015, 16, Color.GREEN)
    ]
    
    # print("Adding Initial Objects:")
    for obj_id, size, color in initial_object_data:
        # if(obj_id == 2006):
        #     print_tree(gcms.bin_size_avl.root)
        #     print("----------------------------------------------------------------")
        #     break
        try:
            gcms.add_object(obj_id, size, color)
            # print(f"Added Object ID: {obj_id}, Size: {size}, Color: {color.name}")
        except NoBinFoundException:
            pass
            # print(f"Failed to add Object ID: {obj_id}, Size: {size}, Color: {color.name} - No suitable bin found")
    

    
    
    # Adding additional bins after some objects have been placed
    additional_bin_data = [
        (1011, 65),
        (1012, 45),
        (1013, 55)
    ]
    
    # print("Adding Additional Bins:")
    for bin_id, capacity in additional_bin_data:
        gcms.add_bin(bin_id, capacity)
        # print(f"Added Bin ID: {bin_id}, Capacity: {capacity}")
    

    
    # Adding additional objects after new bins have been added
    additional_object_data = [
        (2016, 25, Color.GREEN),
        (2017, 14, Color.GREEN),
        (2018, 9, Color.GREEN),
        (2019, 50, Color.RED),
        (2020, 33, Color.GREEN),
        (2021, 12, Color.GREEN),
        (2022, 7, Color.GREEN),
        (2023, 19, Color.RED),
        (2024, 28, Color.GREEN),
        (2025, 11, Color.GREEN)
    ]
    
    # print("Adding Additional Objects:")
    for obj_id, size, color in additional_object_data:
        try:
            gcms.add_object(obj_id, size, color)
            # print(f"Added Object ID: {obj_id}, Size: {size}, Color: {color.name}")
        except NoBinFoundException:
            pass
            # print(f"Failed to add Object ID: {obj_id}, Size: {size}, Color: {color.name} - No suitable bin found")
    

    
    print("+"*50)
    print_tree(gcms.bins.root)
    print("+"*50)