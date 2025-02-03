#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sample_data = pd.read_csv('sample_data.csv')
sample_data.column_c.iloc[1]
plt.plot(sample_data.column_a,sample_data.column_b,"o")
plt.title("sample data")
plt.plot()
plt.show()

