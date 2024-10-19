from exceptions import NoBinFoundException
from avl import AVLTree

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        if object.size > self.remcap:
            raise NoBinFoundException()
        self.objects.insert(object.object_id, object)
        self.remaining_capacity -= object.size
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        removed_object = self.objects.get(object_id)
        if removed_object:
            self.remaining_capacity += removed_object.size
            self.objects.delete(object_id)
        else:
            raise ValueError(f"Object with ID {object_id} not found")
            pass
