from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np

font_location = 'LG PC.ttf' 

font_name = fm.FontProperties(fname=font_location, size=10)


X, y = make_blobs(centers=4, random_state=8)
y = y % 2

markers=['o','^']
colors=['blue','red']

for i in range(2):
  #plt.scatter(x[:,0],x[:,1],c=y,marker=mkr_dict[kind])
  plt.scatter(X[y==i,0],X[y==i,1],c=colors[i],marker=markers[i],edgecolor="k",s=100)
plt.xlabel('특성 0',fontproperties=font_name)
plt.ylabel('특성 1',fontproperties=font_name)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
C_values = [-1, 0, 3]
#gamma_values = [-1, -0.5, 0, 0.5, 1, 1.5, 2]
gamma_values = np.logspace(start=-1, stop=2, num=100)
train_scores=[]
test_scores=[]

best_score = 0
best_train_score=0
best_C = None
best_gamma = None

for C in C_values:
    for gamma in gamma_values:
        svc = SVC(C=10**C, gamma=gamma)
        svc.fit(X_train, y_train)
        train_score=svc.score(X_train, y_train)
        test_score = svc.score(X_test, y_test)
        if test_score > best_score:
            best_score = test_score
            best_train_score=train_score
            best_C = C
            best_gamma = gamma

print(f"최적의 C: {best_C}, 최적의 gamma: {best_gamma}, 학습 정확도: {best_train_score: .2f}, 테스트 정확도: {best_score:.2f}")


