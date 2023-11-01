#!/usr/bin/env python
# coding: utf-8

# Q1)
# A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.
# 

# In[4]:


import pandas as pd
df=pd.read_csv("Cutlets.csv")
df_UnitA=df['Unit A']
df_UnitB=df["Unit B"]
from scipy import stats
zval, pval=stats.ttest_ind(df_UnitA, df_UnitB)
zval,pval
# Where NULL Hypothesis is : "There is no significant difference in the diameter of the cutlet between two units."
# Where ALTERNATIVE Hypothesis is : "There is significant difference in the diameter of the cutlet between two units."
if pval < 0.05:
    print("Reject NULL Hypothesis and Accept ALTERNATIVE Hypothesis")
else: 
    print("Accept NULL Hypothesis and Reject ALTERNATIVE Hypothesis")


# In[5]:


if pval < 0.05:
    print("There is a significant difference in the diameter of the cutlet between two units.")
else:
    print("There is no significant difference in the diameter of the cutlet between two units.")


# Q2)
# A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch.
# 
# Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.
# 

# In[7]:


import pandas as pd
df=pd.read_csv('LabTAT.csv')
df


# Q$) TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  The manager wants to check whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences

# In[2]:


import pandas as pd
df=pd.read_csv("Costomer+OrderForm.csv")
df


# In[27]:


data_India=pd.DataFrame(df['India'].value_counts())
data_India


# In[28]:


data_Indonesia=pd.DataFrame(df['Indonesia'].value_counts())
data_Indonesia


# In[30]:


data_Phillippines=pd.DataFrame(df['Phillippines'].value_counts())
data_Phillippines


# In[31]:


data_Malta=pd.DataFrame(df['Malta'].value_counts())
data_Malta


# In[46]:


import numpy as np
data=np.array([[280,267,271,269],[20,33,29,31]])
error=data[0]
defective=data[1]


# In[60]:


from scipy import stats
zcal, pval,f,jk=stats.chi2_contingency(data)
zcal, pval
if pval < 0.05:
    print('Reject Null Hypothesis and Accept Alternative Hypothesis')
    print("the defective % varies by error")
else:
    print("Accept Null Hypothesis and Reject Alternative Hypothesis")
    print("the defective % doesn't varies by error")


# Q3)      Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions.

# In[100]:


import pandas as pd
df=pd.read_csv('BuyerRatio.csv')
df


# In[105]:


male=[50,142,131,70]
female=[435,1523,1356,750]
from scipy import stats
zcal,pval=stats.ttest_ind(male, female)
zcal,pval
if pval < 0.05:
    print("Reject Null Hypothesis and Accept Alternative Hypothesis\n All proportions are equal")
else:
    print("Accept Null Hypothesis and Reject Alternative Hypothesis \n All proportions are not equal")


# In[ ]:




