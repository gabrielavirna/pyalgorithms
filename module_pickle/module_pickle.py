# module for saving objects(pickle=serialization; depickle=deserialization to python object)
#usage: pickle to transfer data between servers,pickle data from another source; no security
import pickle

example_dict = {1:"6",2:"2",3:"f"}

#pickle_out = open("module_pickle_dict","wb")
#pickle.dump(example_dict,pickle_out)#what to dump&where
#pickle_out.close()

#read dictionary back in the memory
pickle_in = open("module_pickle_dict","rb")
example_dict = pickle.load(pickle_in)
print(example_dict)
print(example_dict[3])