from collections import Counter


def gini(labels):
    """Calculate Gini impurity for a list of labels."""
    total = len(labels)
    if total == 0:
        return 0

    counts = Counter(labels)
    return 1 - sum((count / total) ** 2 for count in counts.values())


def best_split(data):
    """
    Find the best feature and threshold to split the data.

    Each row is [feature_1, feature_2, ..., label].
    """
    number_of_features = len(data[0]) - 1
    best_gain = 0
    best_feature = None
    best_threshold = None

    parent_labels = [row[-1] for row in data]
    parent_gini = gini(parent_labels)

    for feature in range(number_of_features):
        values = sorted(set(row[feature] for row in data))

        for i in range(len(values) - 1):
            threshold = (values[i] + values[i + 1]) / 2

            left = [row for row in data if row[feature] <= threshold]
            right = [row for row in data if row[feature] > threshold]

            if not left or not right:
                continue

            left_gini = gini([row[-1] for row in left])
            right_gini = gini([row[-1] for row in right])

            weighted_gini = (
                len(left) / len(data) * left_gini
                + len(right) / len(data) * right_gini
            )
            gain = parent_gini - weighted_gini

            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold


def majority_class(data):
    """Return the most common label."""
    labels = [row[-1] for row in data]
    return Counter(labels).most_common(1)[0][0]


def build_tree(data, depth=0, max_depth=5):
    """Recursively build a decision tree."""
    labels = [row[-1] for row in data]

    # Stop if all rows have the same label or the depth limit is reached
    if len(set(labels)) == 1 or depth >= max_depth:
        return majority_class(data)

    feature, threshold = best_split(data)

    if feature is None:
        return majority_class(data)

    left = [row for row in data if row[feature] <= threshold]
    right = [row for row in data if row[feature] > threshold]

    return {
        "feature": feature,
        "threshold": threshold,
        "left": build_tree(left, depth + 1, max_depth),
        "right": build_tree(right, depth + 1, max_depth),
        "default": majority_class(data),
    }


def predict(tree, features):
    """Predict a label for one row of feature values."""
    if not isinstance(tree, dict):
        return tree

    if tree["feature"] >= len(features):
        return tree["default"]

    if features[tree["feature"]] <= tree["threshold"]:
        return predict(tree["left"], features)
    return predict(tree["right"], features)


# Example data: [study_hours, attendance_percent, result]
training_data = [
    [1, 50, "Fail"],
    [2, 60, "Fail"],
    [3, 65, "Pass"],
    [4, 70, "Pass"],
    [5, 80, "Pass"],
    [1, 90, "Fail"],
    [6, 55, "Pass"],
    [2, 75, "Fail"],
]

tree = build_tree(training_data, max_depth=3)

student = [3.5, 72]
print("Prediction:", predict(tree, student))
