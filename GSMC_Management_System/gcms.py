from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bins = AVLTree(compare_function=self.compare_bincap)
        self.objecttree1 = AVLTree(compare_function=self.compare_objectid)# obj id to object
        self.objecttree2 = AVLTree(compare_function=self.compare_assbinid) # assinged bnin id to avl tree
        ##print("Initialized GCMS with empty AVL trees for bins and objects.")

    # Comparison functions
    def compare_bincap(self, bin1, bin2):
        ##print(f"Comparing bin capacities: {bin1} and {bin2}")
        return bin1 - bin2

    def compare_binid(self, bin1, bin2):
        ##print(f"Comparing bin IDs: {bin1} and {bin2}")
        return bin1 - bin2

    def compare_objectid(self, obj1, obj2):
        ##print(f"Comparing object IDs: {obj1} and {obj2}")
        return obj1 - obj2

    def compare_assbinid(self, obj1, obj2):
        ##print(f"Comparing associated bin IDs: {obj1} and {obj2}")
        return obj1 - obj2
    
    # Function to add a new bin
    def add_bin(self, bin_id, capacity):
        ##print(f"Adding new bin with ID: {bin_id} and capacity: {capacity}")
        new_bin = Bin(bin_id, capacity)  # Create a new bin
        ##print(f"Created new bin: {new_bin}")

        # Search for an AVLTree with the same capacity
        found_node = self.bins.search_node(capacity)
        if found_node is not None:
            ##print(f"Found AVL tree for capacity {capacity}.")
            Avltree = found_node.value
            Avltree.insert_node(bin_id, new_bin)
            ##print(f"Inserted bin {bin_id} into the existing AVL tree.")
        else:
            ##print(f"No AVL tree found for capacity {capacity}. Creating new AVL tree.")
            samecapacitytree = AVLTree(compare_function=self.compare_binid)
            samecapacitytree.insert_node(new_bin.bin_id, new_bin)
           # samecapacitytree.key = capacity
            self.bins.insert_node(new_bin.capacity, samecapacitytree)
            ##print("success",self.bins.inorder_traversal(self.bins.root))
            ##print(f"Inserted new AVL tree for bins with capacity {capacity}.")
        avl = AVLTree(compare_function=self.compare_objectid)
        self.objecttree2.insert_node(bin_id,avl)
        node2=self.objecttree2.search_node(bin_id)
        node2.parentbincap=capacity

    def add_object(self, object_id, size, color):
        ##print(self.bins.inorder_traversal(self.bins.root))
        new_object = Object(object_id, size, color)
        compact_capacity = self.bins.find_successor_node(self.bins.root,size)
        best_capacity=self.bins.get_max_value_node(self.bins.root)
        if best_capacity.key < size:
            raise NoBinFoundException()
        # Determine the appropriate algorithm based on color
        if color == Color.RED:  # Largest Fit, Least ID
            best_bin = None
            tree=best_capacity.value # storing small avl tree of bins
            ##print(tree)
            node=tree.get_min_value_node(tree.root) # min id node
            
            ##print(tree.root)
            ##print(node)

            best_bin=node.value # fitting bin
            ##print("nishant")
            ##print(self.bins.inorder_traversal(self.bins.root))
            tree.delete_node(best_bin.bin_id) # delete bin from small avl tree
            ##print("tree",tree.root)
            if(tree.root is None):
                self.bins.delete_node(best_bin.capacity)
            ##print("success",self.bins.inorder_traversal(self.bins.root))


            best_bin.capacity-=size# capacity update 
            new_object.parentbin=best_bin
            ##print(best_bin.capacity)
            
            node1=self.bins.search_node(best_bin.capacity)
            
            ##print(node1)
            
            if node1!=None:
                nodett=node1.value
                nodett.insert_node(best_bin.bin_id, best_bin)
                ##print(nodett.inorder_traversal(nodett.root))
            else: 
                avl = AVLTree(compare_function=self.compare_binid)
                avl.insert_node(best_bin.bin_id, best_bin)
            
                self.bins.insert_node(best_bin.capacity,avl)
            #print("suss",self.bins.inorder_traversal(self.bins.root))#working correctly 

            node2 = self.objecttree2.search_node(best_bin.bin_id)
            #print(node2)
            if node2!=None:
                node2.value.insert_node(object_id,new_object)
                node2.parentbincap=best_bin.capacity
            else: 
                avl = AVLTree(compare_function=self.compare_objectid)
                avl.insert_node(object_id,new_object)
                self.objecttree2.insert_node(best_bin.bin_id,avl)
                node2=self.objecttree2.search_node(best_bin.bin_id)
                node2.parentbincap=best_bin.capacity
                ##print("fuck")
                #avll=(self.objecttree2.search_node(best_bin.bin_id)).value
                ##print(avll.inorder_traversal(avll.root))

            ##print(self.bins.inorder_traversal(self.bins.root))
            self.objecttree1.insert_node(object_id,new_object)
            ##print("sexxxxxxxxxxxxxxxxxxxxxxxx")
            ##print(self.objecttree1.inorder_traversal(self.objecttree1.root))
                
            
        elif color == Color.GREEN:  # Largest Fit, Greatest ID
            best_bin = None
            tree=best_capacity.value # storing small avl tree of bins
            ##print(tree)
            node=tree.get_max_value_node(tree.root) # min id node
            
            ##print(tree.root)
            ##print(node)

            best_bin=node.value # fitting bin
            ##print("nishant")
            ##print(self.bins.inorder_traversal(self.bins.root))
            tree.delete_node(best_bin.bin_id) # delete bin from small avl tree
            ##print("tree",tree.root)
            if(tree.root is None):
                self.bins.delete_node(best_bin.capacity)
            ##print("success",self.bins.inorder_traversal(self.bins.root))


            best_bin.capacity-=size# capacity update 
            new_object.parentbin=best_bin
            ##print(best_bin.capacity)
            
            node1=self.bins.search_node(best_bin.capacity)
            
            ##print(node1)
            
            if node1!=None:
                nodett=node1.value
                nodett.insert_node(best_bin.bin_id, best_bin)
                ##print(nodett.inorder_traversal(nodett.root))
            else: 
                avl = AVLTree(compare_function=self.compare_binid)
                avl.insert_node(best_bin.bin_id, best_bin)
            
                self.bins.insert_node(best_bin.capacity,avl)
            #print("suss",self.bins.inorder_traversal(self.bins.root))#working correctly 

            node2 = self.objecttree2.search_node(best_bin.bin_id)
            #print(node2)
            if node2!=None:
                node2.value.insert_node(object_id,new_object)
                node2.parentbincap=best_bin.capacity
            else: 
                avl = AVLTree(compare_function=self.compare_objectid)
                avl.insert_node(object_id,new_object)
                self.objecttree2.insert_node(best_bin.bin_id,avl)
                node2=self.objecttree2.search_node(best_bin.bin_id)
                node2.parentbincap=best_bin.capacity
                ##print("fuck")
                #avll=(self.objecttree2.search_node(best_bin.bin_id)).value
                ##print(avll.inorder_traversal(avll.root))

            ##print(self.bins.inorder_traversal(self.bins.root))
            self.objecttree1.insert_node(object_id,new_object)
            ##print("sexxxxxxxxxxxxxxxxxxxxxxxx")
            ##print(self.objecttree1.inorder_traversal(self.objecttree1.root))
        elif color == Color.BLUE:  # Compact Fit, Least ID
            best_bin = None
            tree=compact_capacity.value # storing small avl tree of bins
            ##print(tree)
            node=tree.get_min_value_node(tree.root) # min id node
            
            ##print(tree.root)
            ##print(node)

            best_bin=node.value # fitting bin
            ##print("nishant")
            ##print(self.bins.inorder_traversal(self.bins.root))
            tree.delete_node(best_bin.bin_id) # delete bin from small avl tree
            ##print("tree",tree.root)
            if(tree.root is None):
                self.bins.delete_node(best_bin.capacity)
            ##print("success",self.bins.inorder_traversal(self.bins.root))


            best_bin.capacity-=size# capacity update 
            new_object.parentbin=best_bin
            ##print(best_bin.capacity)
            
            node1=self.bins.search_node(best_bin.capacity)
            
            ##print(node1)
            
            if node1!=None:
                nodett=node1.value
                nodett.insert_node(best_bin.bin_id, best_bin)
                ##print(nodett.inorder_traversal(nodett.root))
            else: 
                avl = AVLTree(compare_function=self.compare_binid)
                avl.insert_node(best_bin.bin_id, best_bin)
            
                self.bins.insert_node(best_bin.capacity,avl)
            #print("suss",self.bins.inorder_traversal(self.bins.root))#working correctly 

            node2 = self.objecttree2.search_node(best_bin.bin_id)
            #print(node2)
            if node2!=None:
                node2.value.insert_node(object_id,new_object)
                node2.parentbincap=best_bin.capacity
            else: 
                avl = AVLTree(compare_function=self.compare_objectid)
                avl.insert_node(object_id,new_object)
                self.objecttree2.insert_node(best_bin.bin_id,avl)
                node2=self.objecttree2.search_node(best_bin.bin_id)
                node2.parentbincap=best_bin.capacity
                ##print("fuck")
                #avll=(self.objecttree2.search_node(best_bin.bin_id)).value
                ##print(avll.inorder_traversal(avll.root))

            ##print(self.bins.inorder_traversal(self.bins.root))
            self.objecttree1.insert_node(object_id,new_object)
            ##print("sexxxxxxxxxxxxxxxxxxxxxxxx")
            ##print(self.objecttree1.inorder_traversal(self.objecttree1.root))

        elif color == Color.YELLOW:  # Compact Fit, Greatest ID
            best_bin = None
            tree=compact_capacity.value # storing small avl tree of bins
            ##print(tree)
            node=tree.get_max_value_node(tree.root) # min id node
            
            ##print(tree.root)
            ##print(node)

            best_bin=node.value # fitting bin
            ##print("nishant")
            ##print(self.bins.inorder_traversal(self.bins.root))
            tree.delete_node(best_bin.bin_id) # delete bin from small avl tree
            ##print("tree",tree.root)
            if(tree.root is None):
                self.bins.delete_node(best_bin.capacity)
            ##print("success",self.bins.inorder_traversal(self.bins.root))


            best_bin.capacity-=size# capacity update 
            new_object.parentbin=best_bin
            ##print(best_bin.capacity)
            
            node1=self.bins.search_node(best_bin.capacity)
            
            ##print(node1)
            
            if node1!=None:
                nodett=node1.value
                nodett.insert_node(best_bin.bin_id, best_bin)
                ##print(nodett.inorder_traversal(nodett.root))
            else: 
                avl = AVLTree(compare_function=self.compare_binid)
                avl.insert_node(best_bin.bin_id, best_bin)
            
                self.bins.insert_node(best_bin.capacity,avl)
            #print("suss",self.bins.inorder_traversal(self.bins.root))#working correctly 

            node2 = self.objecttree2.search_node(best_bin.bin_id)
            #print(node2)
            if node2!=None:
                node2.value.insert_node(object_id,new_object)
                node2.parentbincap=best_bin.capacity
            else: 
                avl = AVLTree(compare_function=self.compare_objectid)
                avl.insert_node(object_id,new_object)
                self.objecttree2.insert_node(best_bin.bin_id,avl)
                node2=self.objecttree2.search_node(best_bin.bin_id)
                node2.parentbincap=best_bin.capacity
                ##print("fuck")
                #avll=(self.objecttree2.search_node(best_bin.bin_id)).value
                ##print(avll.inorder_traversal(avll.root))

            ##print(self.bins.inorder_traversal(self.bins.root))
            self.objecttree1.insert_node(object_id,new_object)
            ##print("sexxxxxxxxxxxxxxxxxxxxxxxx")
            ##print(self.objecttree1.inorder_traversal(self.objecttree1.root))
        
    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        # Function to perform in-order traversal of AVL tree
        var=self.objecttree2.search_node(bin_id)
        
            
        node1 = var.value

        bin_cap=var.parentbincap
        extra =node1.inorder_traversal(node1.root)
      
        ans=(bin_cap,extra)
        if extra is None:
            ans=(bin_cap,[])
        return ans       
    
    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        node=self.objecttree1.search_node(object_id)
        if node is None :
            return None
        return node.value.parentbin.bin_id
        pass

    def delete_object(self, object_id):
        
        # Implement logic to remove an object from its bin
        svar2=self.objecttree1.search_node(object_id)
        if svar2 is None :
            return None
        svar=svar2.value
        parentbin1=svar.parentbin # 
        #print(parentbin1.capacity)
        node2=self.bins.search_node(parentbin1.capacity)
        #parentbin_cap=self.objecttree2.search_node(parentbin1.bin_id).parentbincap
        
        objectfi=self.objecttree1.search_node(object_id).value
        object_size=objectfi.size
        var=self.objecttree2.search_node(parentbin1.bin_id)
        avlo=var.value # avl tree 
        #print(avlo.inorder_traversal(avlo.root))
        avlo.delete_node(object_id)
        newc=parentbin1.capacity+object_size
        #print(avlo.inorder_traversal(avlo.root))
        parentbin1.capacity+=object_size
        var.parentbincap=parentbin1.capacity
        
        ##print(node2)
        avltt=node2.value
        #print(avltt.inorder_traversal(avltt.root))
        avltt.delete_node(parentbin1.bin_id)
        #print(avltt.inorder_traversal(avltt.root))

         # delete bin from small avl tree
        ##print("tree",tree.root)
        #print("deletS")
        if(avltt.root is None):
            self.bins.delete_node(parentbin1.capacity-object_size)
        ##print("success",self.bins.inorder_traversal(self.bins.root))
        node3=self.bins.search_node(parentbin1.capacity)
        if node3!=None:
            node3.value.insert_node(parentbin1.bin_id, parentbin1)
        else: 
            avl = AVLTree(compare_function=self.compare_binid)
            avl.insert_node(parentbin1.bin_id, parentbin1)
            self.bins.insert_node(parentbin1.capacity,avl)
        #print("sex")
        self.objecttree1.delete_node(object_id)
        


