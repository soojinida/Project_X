import mglearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

X, y = mglearn.datasets.make_wave(n_samples=40)

X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=0)

for n_neighbors in [1, 3, 9]:
    knn = KNeighborsRegressor(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print(f"n_neighbors={n_neighbors}, R2: {r2:.2f}")
