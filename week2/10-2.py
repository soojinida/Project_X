import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X, y = mglearn.datasets.make_wave(n_samples=60)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)

print("가중치 (계수):", lr.coef_)
print("절편:", lr.intercept_)

train_score = lr.score(X_train, y_train)
test_score = lr.score(X_test, y_test)
print("학습 데이터 점수 (R2):", train_score)
print("테스트 데이터 점수 (R2):", test_score)

if abs(train_score - test_score) > 0.1:
    if train_score > test_score:
        print("훈련 데이터 점수가 더 높으므로 모델이 과대적합일 가능성이 높습니다.")
    elif train_score < test_score:
        print("테스트 데이터 점수가 더 높으므로 모델이 과소적합일 가능성이 높습니다.")
else:
    print("훈련 데이터와 테스트 데이터의 점수가 유사하므로 모델이 적절할 가능성이 높습니다.")
