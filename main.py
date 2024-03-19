class Comp:
    def __init__(self,processor,memory,gragh):
        self._processor = processor
        self._memory = memory
        self._gragh = gragh

    def check_data(self):
        return self._processor,self._memory,self._gragh,
    def set_processor(self,new_processor):
        self._processor = new_processor
    def set_memory(self,new_memory):
        self._memory = new_memory
    def set_gragh(self,new_gragh):
        self._gragh = new_gragh

my_comp = Comp('a','b','c')
print(my_comp.check_data())
my_comp.set_gragh('adf')
print(my_comp.check_data())