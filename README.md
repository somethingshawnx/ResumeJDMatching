#  Resume-Job Matcher: AI-Powered Resume Optimization Tool
An intelligent machine learning system that analyzes how well your resume matches any job description and provides actionable recommendations for improvement.

##  Features

- **Semantic Similarity Analysis**: Uses sentence transformers to compute deep semantic similarity between resume and job descriptions
- **Skills Extraction & Matching**: Intelligent skill detection using fuzzy string matching with 80%+ accuracy threshold
- **Comprehensive Scoring**: Combines semantic similarity (50%) and skill overlap (50%) for holistic match assessment
- **Personalized Recommendations**: Generates specific suggestions for resume enhancement based on missing skills
- **Easy-to-Use**: Simple command-line interface with detailed match reports

##  How It Works

```
Resume + Job Description → ML Pipeline → Match Score + Recommendations
```

1. **Text Processing**: Cleans and normalizes input documents
2. **Skill Extraction**: Identifies technical skills using fuzzy matching against comprehensive skills database
3. **Semantic Analysis**: Computes embeddings using sentence-transformers model
4. **Scoring Algorithm**: Combines multiple factors for final match percentage
5. **Recommendation Engine**: Suggests specific improvements based on gap analysis

##  Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/resumematcher.git
cd resumematcher

# Install dependencies
pip install -r requirements.txt
```

### Required Dependencies
```
scikit-learn
sentence-transformers
rapidfuzz
numpy
```

##  Project Structure

```
resumematcher/
│
├── data/
│   ├── resume.txt           # Your resume (plain text)
│   └── job_description.txt  # Target job description
│
├── skills/
│   └── skills_list.txt      # Comprehensive skills database
│
└── app/
    ├── main.py              # Main execution script
    ├── extractor.py         # Text loading and preprocessing
    ├── skills_ner.py        # Skill extraction using fuzzy matching
    ├── scorer.py            # Semantic similarity and scoring
    └── recommender.py       # Recommendation generation
```

##  Quick Start

1. **Prepare Your Data**:
   - Add your resume text to `data/resume.txt`
   - Add target job description to `data/job_description.txt`

2. **Run the Analysis**:
   ```bash
   cd app
   python main.py
   ```

3. **View Results**:
   ```
   === Resume ↔ Job Description Match Report ===
   Semantic similarity: 57.47%
   Skill overlap: 84.0%
   Final match score: 70.74%

   Missing skills: {'databases & querying', 'problem solving', '# programming languages', 'gcp'}

   Suggestions:
   - Add a bullet point showing experience with 'databases & querying'.
   - Add a bullet point showing experience with 'problem solving'.
   - Add a bullet point showing experience with 'gcp'.
   ```

##  Technical Implementation

### Semantic Similarity Engine
- **Model**: `all-MiniLM-L6-v2` sentence transformer
- **Method**: Cosine similarity on document embeddings
- **Accuracy**: Captures contextual meaning beyond keyword matching

### Skills Extraction
- **Algorithm**: Fuzzy string matching with `rapidfuzz`
- **Threshold**: 80% similarity for skill detection
- **Database**: 100+ technical skills across programming, ML, cloud, and soft skills

### Scoring Formula
```python
final_score = 0.5 * semantic_similarity + 0.5 * skill_overlap_percentage
```

##  Example Results

**Test Case: Data Science Position**
- **Semantic Similarity**: 57.47%
- **Skill Overlap**: 84.0%
- **Final Match Score**: 70.74%
- **Key Missing Skills**: GCP, Advanced Database Technologies
- **Recommendations**: 4 specific resume improvements identified

##  Use Cases

- **Job Seekers**: Optimize resumes for specific positions
- **Career Changers**: Identify skill gaps for target roles
- **Students**: Understand industry requirements
- **Recruiters**: Automate initial resume screening
- **Career Counselors**: Provide data-driven guidance

##  Future Enhancements

- [ ] Web-based dashboard interface
- [ ] Industry-specific scoring weights
- [ ] ATS-friendly formatting suggestions
- [ ] Integration with job boards APIs
- [ ] Advanced NLP for experience quantification
- [ ] Multi-language support
- [ ] Real-time skill trend analysis

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
