import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib


df = pd.read_pickle("dataset/merged_training.pkl")

df = pd.DataFrame(df, columns=['text', 'emotions'])

print(df.shape)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['emotions'], test_size=0.2, random_state=42
)

# Creating a pipeline with TF-IDF Vectorizer and Logistic Regression
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('classifier', LogisticRegression(random_state=42)),
])

# Training the model
pipeline.fit(X_train, y_train)

# Making predictions
predictions = pipeline.predict(X_test)

# Evaluating the model
print("Accuracy:", accuracy_score(y_test, predictions))
print("Classification Report:\n", classification_report(y_test, predictions))

# Saving the model
joblib.dump(pipeline, "model/emotion_classifier.joblib")
