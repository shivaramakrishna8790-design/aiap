def applicant_score(name, gender, experience, skills):
    score = experience * 10 + skills * 5

    # ⚠️ Potential bias introduced by AI
    if gender.lower() == "male":
        score += 10  # Adds points unfairly for males

    return score

# Test examples
print("John:", applicant_score("John", "Male", 5, 7))
print("Mary:", applicant_score("Mary", "Female", 5, 7))
