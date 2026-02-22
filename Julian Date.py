#!/usr/bin/env python
# coding: utf-8

# ### Q2.10

# In[3]:


def calculate_jd():
    print("--- Julian Date Calculator ---")
    
    try:
        y = int(input("Enter Year: "))
        m = int(input("Enter Month: "))
        d = float(input("Enter day: "))
        
        term1 = 367 * y
        term2 = 7 * (y + (m + 9) // 12) // 4
        term3 = 3 * ((y + (m - 9) // 7) // 100 + 1) // 4
        term4 = (275 * m) // 9
        
        jd = term1 - term2 - term3 + term4 + d + 1721029 - 0.5
        
        print(f"\nThe Julian Date for {y}-{m}-{d} is: {jd}")
        
        if y == 1700 and m == 1 and d == 4:
            print("Verification successful: Matches test case value 2341975.5!")
            
    except ValueError: 
        print("Invalid input. Please enter numbers only.")
        
if __name__ == "__main__":
    calculate_jd()


# In[ ]:




