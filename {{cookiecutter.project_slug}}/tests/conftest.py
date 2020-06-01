"""pytest configuration file"""

import pytest
{% if cookiecutter.use_hypothesis == 'y' -%}
from hypothesis import HealthCheck, Verbosity, settings{% endif %}

{% if cookiecutter.use_hypothesis == 'y' -%}
# register hypothesis search strategy options
settings.register_profile(
    "suppress_deadline",
    deadline=None,
    suppress_health_check=(HealthCheck.too_slow,),
    max_examples=10,
)
settings.register_profile(
    "ci", deadline=None, suppress_health_check=(HealthCheck.too_slow,), max_examples=50
)
settings.register_profile(
    "dev", deadline=None, suppress_health_check=(HealthCheck.too_slow,), max_examples=5
)
settings.register_profile(
    "debug",
    deadline=None,
    suppress_health_check=(HealthCheck.too_slow,),
    max_examples=3,
    verbosity=Verbosity.verbose,
){% endif %}


@pytest.fixture
def unit_test_data():
  "Put your unit test data here..."
    # import numpy as np
    # from sklearn.datasets import make_blobs
    # from sklearn.ensemble import RandomForestClassifier

    # np.random.seed(0)
    # n_clust = 2
    # x, y = make_blobs(
    #     n_samples=12000,
    #     n_features=3,
    #     centers=n_clust,
    #     cluster_std=np.random.rand(n_clust) * 10,
    # )
    # xtrain, ytrain = x[:8000], y[:8000]
    # xtest, ytest = x[8000:], y[8000:]
    # clf = RandomForestClassifier(n_estimators=10, max_depth=2, min_samples_split=3)
    # clf.fit(xtrain, ytrain)
    # probs = clf.predict_proba(xtest)
    # ytest_ = ["class_{}".format(int(i)) for i in ytest]
    # probs_ = {"class_{}".format(i): probs[:, i] for i in range(n_clust)}
    # return {"ytest": ytest_, "probs": probs_}
