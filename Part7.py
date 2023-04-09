class my_calculator:

    
    def product(self, *nums):
        pro = 1
        for x in nums:
            print(nums)
            pro = pro * x
        print(pro)


c1 = my_calculator()
c1.product(4)
c1.product(4, 5)
c1.product(4, 5, 6)
c1.product(4, 5, 6, 7)

