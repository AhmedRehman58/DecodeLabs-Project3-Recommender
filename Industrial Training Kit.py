from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
job_roles = {
    "AI Engineer": "python machine learning deep learning tensorflow pytorch neural networks data",
    "Data Scientist": "python machine learning statistics sql data analysis pandas numpy visualization",
    "Backend Developer": "python java sql apis rest databases nodejs backend server",
    "Frontend Developer": "javascript html css react vuejs typescript ui design responsive",
    "DevOps Engineer": "aws docker kubernetes linux cloud ci cd automation git deployment",
    "Cloud Architect": "aws azure cloud infrastructure devops networking security kubernetes",
    "Cybersecurity Analyst": "networking security penetration testing ethical hacking linux firewall",
    "Data Engineer": "python sql spark hadoop etl data pipelines databases cloud",
    "Full Stack Developer": "javascript python html css react nodejs sql mongodb apis",
    "Mobile Developer": "flutter react native swift kotlin android ios mobile apps",
}
 

print("   Recommendation Kit")
print("   Built by: Ahmed Rehman")
print("   DecodeLabs AI Internship 2026 | Project 3")

 
skill1 = input("Skill 1: ").strip().lower()
skill2 = input("Skill 2: ").strip().lower()
skill3 = input("Skill 3: ").strip().lower()
 
user_profile = skill1 + " " + skill2 + " " + skill3
 
print()
print("Analyzing your profile...")
print()
 
all_docs = list(job_roles.values()) + [user_profile]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_docs)
 
user_vector = tfidf_matrix[-1]
job_vectors = tfidf_matrix[:-1]
 
scores = cosine_similarity(user_vector, job_vectors)[0]
 
results = list(zip(job_roles.keys(), scores))
results.sort(key=lambda x: x[1], reverse=True)
top3 = results[:3]
 
print("=" * 55)
print("   TOP 3 RECOMMENDED JOB ROLES FOR YOU")
print("=" * 55)
for rank, (role, score) in enumerate(top3, 1):
    match = round(score * 100, 1)
    bar = "#" * int(match / 5)
    print(f"  {rank}. {role}")
    print(f"     Match: [{bar:<20}] {match}%")
    print()
 
print("=" * 55)
print("  Skills entered:", skill1, "|", skill2, "|", skill3)
print("  Engineer: Ahmed Rehman | DecodeLabs 2026")
print("=" * 55)