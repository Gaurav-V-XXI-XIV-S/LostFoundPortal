import cv2


def orb_similarity(image_a, image_b):
    gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=1200)
    keypoints_a, descriptors_a = orb.detectAndCompute(gray_a, None)
    keypoints_b, descriptors_b = orb.detectAndCompute(gray_b, None)

    if descriptors_a is None or descriptors_b is None:
        return 0.0, 0

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors_a, descriptors_b)
    if not matches:
        return 0.0, 0

    matches = sorted(matches, key=lambda match: match.distance)
    good_matches = [match for match in matches if match.distance < 64]
    max_features = max(len(keypoints_a), len(keypoints_b), 1)
    score = min(len(good_matches) / max_features, 1.0)
    return score, len(good_matches)
