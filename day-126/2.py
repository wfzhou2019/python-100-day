import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

tips= sns.load_dataset("tips")
print('tips ���ݼ�ǰʮ������:\n', tips.head(5))
print('ÿһ�е���������:\n', tips.dtypes)

# 2.1ʾ��
sns.relplot(x="total_bill", y="tip", data=tips) 

# 2.2ʾ��
sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)  

# 2.3ʾ��
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)  

# 2.4ʾ��
sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)  

# 2.5ʾ��
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)  

# 2.6ʾ��
sns.relplot(x="total_bill", y="tip", size="size", data=tips)  
sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips)

