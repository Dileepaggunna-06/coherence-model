RST-Based Document Coherence Model

##📌 Project Overview

This project analyzes the coherence of a document using Rhetorical Structure Theory (RST). It evaluates how well sentences are logically connected and generates a coherence score out of 100.

⸻

⚙️ Features
	•	Sentence segmentation
	•	RST relation detection (contrast, cause, result, etc.)
	•	Nucleus vs Satellite classification
	•	Sentence-to-sentence flow analysis
	•	Lexical cohesion calculation
	•	Final scoring system

⸻

🧠 How It Works
	1.	The input text is converted to lowercase.
	2.	The document is split into sentences.
	3.	Words are extracted from the text.
	4.	RST relations are detected using keywords like “however”, “because”, “as a result”.
	5.	Sentences are classified into:
	•	Nucleus (main idea)
	•	Satellite (supporting information)
	6.	Sentence flow is measured using relation connections.
	7.	Lexical cohesion is calculated based on word repetition.
	8.	A final score is generated out of 100.

⸻

📊 Example Output

Score: 64/100

Features:
	•	Sentences: 6
	•	Relations: 6
	•	Variety: 5
	•	Balance: 0.83
	•	Flow: 5
	•	Cohesion: 0.15

⸻

📁 Project Files
	•	main.py → Runs the program
	•	coherence_model.py → Feature extraction and scoring
	•	rst_relations.py → RST relation keywords

⸻

🚀 How to Run
	1.	Install Python
	2.	Open terminal in the project folder
	3.	Run: 
              python main.py 

🎯 Key Concepts
	•	RST Relations → Logical connections between sentences
	•	Variety → Diversity of relation types
	•	Cohesion → Word repetition
	•	Flow → Sentence connectivity

⸻

👨‍💻 Author

Dileep

⸻

⭐ Note

This is an unsupervised rule-based model designed for interpretability. It may slightly overestimate relations but provides clear and explainable results.