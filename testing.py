def finding_small_number(a):
        # import pdb;pdb.set_trace()
        smallest_number = a[0]
        for i in a:
                if smallest_number > i:
                        smallest_number = i
        return smallest_number


def sorting_list(unsortedlist):
        # sortedlist = []
        # for i in range(0,len(unsortedlist)):
        #         sortedlist.append(finding_small_number(unsortedlist))
        #         unsortedlist.remove(finding_small_number(unsortedlist))
        print(set(unsortedlist))

# sorting_list([1,2,7,6,5,9,3,-8,-28,19,29,29,1028])

def setting_list(a):
        no=[]
        for i in a:
                if i not in no:
                        no.append(i)

        print(no)

# setting_list([2,5,1,1,88,9,88])  

def prime_numbers(num):
        for i in range(2,num):
                if num%i == 0:
                        print('Number {} is not prime'.format(num))
                        return

        print(f'Number {num} is prime')

# prime_numbers(3)

def palandrom()





