class pair_elements:
    def twoSum(self, num, target):
        lookup = {}
        for i,j in enumerate(num):
            if target - j in lookup:
                return (lookup[target - j],i)
            lookup[j]=i
        
values = int(input("enter sum of which sum you want to make it shearch :"))
print("index=%d, index2%d"% pair_elements().twoSum((10,20,30,40,50,60,70),values))
