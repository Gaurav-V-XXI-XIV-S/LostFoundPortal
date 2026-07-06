import numpy as np

from ai.image_match import histogram_similarity, preprocess
from ai.orb_match import orb_similarity


def test_histogram_similarity_identical_images():
    image = np.zeros((120, 120, 3), dtype=np.uint8)
    image[:, :] = (20, 120, 220)
    processed = preprocess(image)

    assert histogram_similarity(processed, processed) > 0.99


def test_orb_similarity_handles_blank_images():
    image = np.zeros((120, 120, 3), dtype=np.uint8)
    processed = preprocess(image)

    score, good_matches = orb_similarity(processed, processed)

    assert score == 0
    assert good_matches == 0
