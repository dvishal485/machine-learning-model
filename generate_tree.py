# Standard Imports
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz

# Loading csv file to datafrane
data = pd.read_csv("Indian Liver Patient Dataset.csv")

# Making data usable by model
data["gender"] = data["gender"].apply(lambda x: 1 if x == "Female" else 0)
data["alkphos"] = data["alkphos"].fillna(data["alkphos"].mean())
model = RandomForestClassifier(n_estimators=10)

# Training Model
x, y = data.drop(["is_patient"], axis=1), data["is_patient"]
model.fit(x, y)

# Extract a single tree
estimator = model.estimators_[1]

# Export tree as dot file
export_graphviz(estimator, 
                out_file='decision_tree.dot',
                feature_names=data.drop(["is_patient"], axis=1).axes[1],
                rounded = True, proportion = False, 
                precision = 3, filled = True)

# Convert dot file to png
from subprocess import call
call(['dot', '-Tpng', 'decision_tree.dot', '-o', 'decision_tree.png', '-Gdpi=300'])