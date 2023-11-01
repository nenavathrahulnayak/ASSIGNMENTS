#!/usr/bin/env python
# coding: utf-8

# Q1) Look at the data given below. Plot the data, find the outliers and find out μ,σ,σ^2 Name of company Measure X Allied Signal 24.23% Bankers Trust 25.53% General Mills 25.41% ITT Industries 24.14% J.P.Morgan & Co. 29.62% Lehman Brothers 28.25% Marriott 25.81% MCI 24.39% Merrill Lynch 40.26% Microsoft 32.95% Morgan Stanley 91.36% Sun Microsystems 25.99% Travelers 39.42% US Airways 26.71% Warner-Lambert 35.00%
# 

# In[45]:


name=['Allied Signal','Bankers Trust','General Mills','ITT Industries','J.P.Morgan & Co.','Lehman Brothers',
      'Marriott','MCI','Merrill Lynch','Microsoft','Morgan Stanley','Sun Microsystems','Travelers','US Airways',
      'Warner-Lambert']


# In[46]:


lis=[24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00]


# In[48]:


import numpy as np
np.mean(lis)# Mean


# In[49]:


np.std(lis)# Standard Deviation


# In[50]:


np.var(lis)#Variance


# In[60]:


import matplotlib.pyplot as plt
plt.boxplot(lis, vert= False)


# Morgan Stanley is the only outlier and it is in the right side.
# 

# Q4)	AT&T was running commercials in 1990 aimed at luring back customers who had switched to one of the other long-distance phone service providers. One such commercial shows a businessman trying to reach Phoenix and mistakenly getting Fiji, where a half-naked native on a beach responds incomprehensibly in Polynesian. When asked about this advertisement, AT&T admitted that the portrayed incident did not actually take place but added that this was an enactment of something that “could happen.” Suppose that one in 200 long-distance telephone calls is misdirected. What is the probability that at least one in five attempted telephone calls reaches the wrong number? (Assume independence of attempts.)

# In[77]:


sample_size=5
probability_of_misdirected_calls=1/200
from scipy.stats import binom
b=binom(sample_size,probability_of_misdirected_calls)
probability=1-b.cdf(0)
print("Probability that at least one in five attempted telephone calls reaches the wrong number is ",probability)


# In[ ]:




