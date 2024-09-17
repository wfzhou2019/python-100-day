import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
sns.set(color_codes=True)

# 2.1 ʾ��
x = np.random.normal(size=100)
sns.distplot(x)

# 2.2 ʾ��
x = np.random.normal(size=100)
sns.distplot(x, kde=False, rug=True)

# 2.3 ʾ��
x = np.random.normal(size=100)
sns.distplot(x, hist=False, rug=True)

x = np.random.normal(0, 1, size=30)  # ��ʼ��һ�������̬�ֲ��������
bandwidth = 1.06 * x.std() * x.size ** (-1 / 5.)  # ���ݾ��鹫ʽ���� KDE �Ĵ���
support = np.linspace(-4, 4, 200)

kernels = []
for x_i in x:

    kernel = stats.norm(x_i, bandwidth).pdf(support)  # ��ȡÿһ���۲�ֵ�ĺ��ܶȹ���
    kernels.append(kernel)
    plt.plot(support, kernel, color="r") # Ϊÿһ���۲�ֵ���ƺ��ܶȹ�������

sns.rugplot(x, color=".2", linewidth=3)

from scipy.integrate import trapz
density = np.sum(kernels, axis=0)
density /= trapz(density, support)
plt.plot(support, density)

sns.kdeplot(x, shade=True)

sns.kdeplot(x)
sns.kdeplot(x, bw=.2, label="bw: 0.2")
sns.kdeplot(x, bw=2, label="bw: 2")
plt.legend()

sns.kdeplot(x, shade=True, cut=0)
sns.rugplot(x)

# 2.4 ʾ��
x = np.random.gamma(6, size=200)
sns.distplot(x, kde=False, fit=stats.gamma)






