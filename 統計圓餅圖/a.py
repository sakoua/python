import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
# 圓餅圖
labels = '台北', 'B', 'C', 'D', 'E', 'F'
size = [33, 52, 12, 17, 62, 48]
plt.pie(size, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
