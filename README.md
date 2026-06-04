DecodeLabs AI Internship — Project 3
Ahmed Rehman | Batch 2026

AI Recommendation Logic
S.P.A.R.K — Skill-based Personalized AI Recommendation Kit
A content-based recommendation system that maps user skills to the most relevant job roles using TF-IDF vectorization and Cosine Similarity.

Features

Takes 3 user skill inputs
TF-IDF vectorization of job role profiles
Cosine Similarity matching
Top 3 job role recommendations with match percentage
Visual match bar display


Tech Stack

Language: Python 3
Libraries: scikit-learn


How to Run
Install library:
bashpip install scikit-learn
Run the project:
bashpython "ahmed_recommender.py"

Sample Input & Output
Input:
Skill 1: python
Skill 2: machine learning
Skill 3: cloud
Output:
TOP 3 RECOMMENDED JOB ROLES FOR YOU
1. AI Engineer        Match: 49.4%
2. Data Scientist     Match: 38.3%
3. Data Engineer      Match: 21.6%

How It Works

User enters 3 skills
TF-IDF converts skills and job roles into vectors
Cosine Similarity calculates match score
Top 3 highest scoring roles are displayed


About

Platform: DecodeLabs AI Internship
Batch: 2026
Engineer: Ahmed Rehman
