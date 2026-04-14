import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

class CareerModel:

    def __init__(self):
        
        self.rf_model = RandomForestClassifier(n_estimators=200)
        self.knn_model = KNeighborsClassifier(n_neighbors=5)

    def train(self, csv_path):
        df = pd.read_csv(csv_path)
        X = df.drop("career", axis=1)
        y = df["career"]

    
        self.rf_model.fit(X, y)
        self.knn_model.fit(X, y)

        print("Models trained successfully!")
        print("Random Forest Accuracy:", self.rf_model.score(X, y))
        print("KNN Accuracy:", self.knn_model.score(X, y))

    def predict(self, answers):
        
      cols = [f"Q{i}" for i in range(1, len(answers)+1)]
      input_df = pd.DataFrame([answers], columns=cols)

    
      rf_result = self.rf_model.predict(input_df)[0]
      rf_proba = max(self.rf_model.predict_proba(input_df)[0])

    
      knn_result = self.knn_model.predict(input_df)[0]
      knn_proba = max(self.knn_model.predict_proba(input_df)[0])

      return (rf_result, round(rf_proba, 2)), (knn_result, round(knn_proba, 2))