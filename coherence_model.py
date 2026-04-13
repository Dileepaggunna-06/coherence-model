# coherence_model.py ()

import re
from rst_relations import RST_RELATIONS


def extract_rst_features(text):
    text_lower = text.lower()
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    words = text_lower.split()

    features = {}
    features["num_sentences"] = len(sentences)

    # =====================
    # Avg sentence length
    # =====================
    if sentences:
        avg_len = sum(len(s.split()) for s in sentences) / len(sentences)
        features["avg_sentence_length"] = round(avg_len, 2)
    else:
        features["avg_sentence_length"] = 0

    # =====================
    # RST RELATIONS ()
    # =====================
    relation_counts = {}
    total_relations = 0

    for relation, markers in RST_RELATIONS.items():
        count = 0
        for marker in markers:
            count += len(re.findall(r'\b' + re.escape(marker) + r'\b', text_lower))
        relation_counts[relation] = count
        total_relations += count

    features["relation_counts"] = relation_counts
    features["total_relations"] = total_relations
    features["relation_variety"] = sum(1 for v in relation_counts.values() if v > 0)

    # =====================
    # NUCLEUS vs SATELLITE ()
    # =====================
    nucleus_sentences = []
    satellite_sentences = []

    all_markers = [m for markers in RST_RELATIONS.values() for m in markers]

    for s in sentences:
        s_lower = s.lower()
        is_satellite = any(marker in s_lower for marker in all_markers)

        if is_satellite:
            satellite_sentences.append(s)
        else:
            nucleus_sentences.append(s)

    # ✅ Ensure at least 1 nucleus
    if len(nucleus_sentences) == 0 and sentences:
        nucleus_sentences.append(sentences[0])
        satellite_sentences = sentences[1:]

    features["nucleus_count"] = len(nucleus_sentences)
    features["satellite_count"] = len(satellite_sentences)

    # =====================
    # SENTENCE FLOW (FIXED)
    # =====================
    sentence_pair_score = 0

    for i in range(len(sentences) - 1):
        next_s = sentences[i + 1].lower()

        found = False
        for markers in RST_RELATIONS.values():
            for marker in markers:
                if marker in next_s:
                    sentence_pair_score += 1
                    found = True
                    break
            if found:
                break

    features["sentence_pair_score"] = sentence_pair_score

    # =====================
    # LEXICAL COHESION
    # =====================
    unique_words = set(words)

    if words:
        cohesion = 1 - (len(unique_words) / len(words))
        features["lexical_cohesion"] = round(cohesion, 3)
    else:
        features["lexical_cohesion"] = 0

    return features


def score_document(features):
    score = 0

    # S1: sentence count
    s1 = min(features["num_sentences"] * 2, 20)
    score += s1

    # S2: total RST relations
    s2 = min(features["total_relations"] * 3, 30)
    score += s2

    # S3: relation variety
    s3 = features["relation_variety"] * 3
    score += s3

    # S4: nucleus/satellite balance
    n = features["nucleus_count"]
    s = features["satellite_count"]
    total = n + s

    if total > 0:
        balance = s / total
        s4 = 20 if 0.3 <= balance <= 0.7 else 8
    else:
        s4 = 0

    score += s4

    # S5: sentence connection
    s5 = min(features["sentence_pair_score"] * 2, 10)
    score += s5

    # S6: lexical cohesion
    s6 = int(features["lexical_cohesion"] * 10)
    score += s6

    return min(score, 100)


def compare_groups(good_docs, bad_docs):

    print("\n--- Good Articles ---")
    good_scores = []

    for name, text in good_docs:
        features = extract_rst_features(text)
        score = score_document(features)
        good_scores.append(score)

        print(f"\n{name} → {score}/100")
        print("Features:", features)

    print("\n--- Bad Articles ---")
    bad_scores = []

    for name, text in bad_docs:
        features = extract_rst_features(text)
        score = score_document(features)
        bad_scores.append(score)

        print(f"\n{name} → {score}/100")
        print("Features:", features)

    good_avg = sum(good_scores) / len(good_scores) if good_scores else 0
    bad_avg = sum(bad_scores) / len(bad_scores) if bad_scores else 0

    print(f"\nGood avg : {round(good_avg, 2)}")
    print(f"Bad avg  : {round(bad_avg, 2)}")

    if good_avg > bad_avg:
        print("✔ Model working correctly")
    else:
        print("❌ Improve model")