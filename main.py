import os

# set default bentoml home dir
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.environ["BENTOML_HOME"] = f"{SCRIPT_DIR}/bentoml"

from sklearn import svm
from sklearn import datasets

# Load training data
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Model Training
clf = svm.SVC(gamma="scale")
clf.fit(X, y)


# import the IrisClassifier class defined above
from iris_classifier import IrisClassifier

# Create a iris classifier service instance
iris_classifier_service = IrisClassifier()

# Pack the newly trained model artifact
iris_classifier_service.pack("model", clf)

# Save the prediction service to disk for model serving
saved_path = iris_classifier_service.save()

print(f"Service saved in path: {saved_path}")