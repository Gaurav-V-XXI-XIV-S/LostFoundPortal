import os

from flask import current_app

from ai.image_match import histogram_similarity, load_image
from ai.orb_match import orb_similarity


def static_path(relative_path):
    return os.path.join(current_app.static_folder, relative_path.replace("/", os.sep))


def compare_images(lost_relative_path, found_relative_path):
    lost_image = load_image(static_path(lost_relative_path))
    found_image = load_image(static_path(found_relative_path))

    orb_score, good_matches = orb_similarity(lost_image, found_image)
    histogram_score = histogram_similarity(lost_image, found_image)
    combined = (orb_score * 0.62) + (histogram_score * 0.38)

    return {
        "orb_score": round(orb_score * 100, 2),
        "histogram_score": round(histogram_score * 100, 2),
        "similarity": round(combined * 100, 2),
        "good_matches": good_matches,
    }


def find_matches(lost_item, found_items, threshold=35):
    matches = []
    for found in found_items:
        try:
            scores = compare_images(lost_item["image_path"], found["image_path"])
        except Exception:
            continue
        if scores["similarity"] >= threshold:
            matches.append({"found": found, "scores": scores})
    return sorted(matches, key=lambda item: item["scores"]["similarity"], reverse=True)
