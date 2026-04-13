# main.py

from coherence_model import extract_rst_features, score_document, compare_groups


def rank_all_documents(documents):
    results = []

    for name, text in documents:
        features = extract_rst_features(text)
        score = score_document(features)
        results.append((name, score))

    results.sort(key=lambda x: x[1], reverse=True)

    for rank, (name, score) in enumerate(results, 1):
        print(f"{rank}. {name} → {score}/100")


# =======================
# GOOD DOCUMENTS (10)
# =======================
good_docs = [

("Iran-Pakistan Diplomacy", """Iran's Foreign Ministry thanked Pakistan for supporting diplomatic talks. 
However, tensions in the region remain high. Because of continued negotiations, both sides are considering peace options. 
As a result, the chances of conflict have reduced. In conclusion, diplomacy played a key role."""),

("India-US Trade Talks", """India and the U.S. are discussing a new trade deal. 
However, legal challenges have delayed progress. Because of these issues, negotiations are still ongoing. 
As a result, both countries are working to find a solution. In conclusion, cooperation remains strong."""),

("Assam Election Update", """Voting has started in multiple states across India. 
However, voter turnout varies between regions. Because of strong campaigns, participation is expected to increase. 
As a result, elections are becoming more competitive. In conclusion, democracy is active."""),

("IPL Final Victory", """Royal Challengers Bengaluru won the IPL title after many years of struggle. 
The team performed consistently throughout the tournament and showed strong teamwork. 
However, the final match was very challenging. Because of excellent batting and disciplined bowling, RCB secured victory. 
As a result, fans celebrated across the country. In conclusion, teamwork was the key."""),

("AI Revolution in Industry", """Artificial Intelligence is growing rapidly in modern industries. 
For example, it is used in healthcare and finance. Because of its efficiency, companies are adopting it widely. 
As a result, productivity has increased. In conclusion, AI is transforming the world."""),

("Digital Education Growth", """Online education has become popular in recent years. 
However, challenges like internet access still exist. Because of digital tools, learning has improved. 
As a result, students can learn from anywhere. In conclusion, technology is shaping education."""),

("Economic Recovery Trends", """The country's economy is recovering after the pandemic. 
However, inflation remains a concern. Because of government policies, growth has improved. 
As a result, employment opportunities are increasing. In conclusion, recovery is ongoing."""),

("Public Health Awareness", """Doctors are warning about rising health issues. 
For example, lifestyle diseases are increasing. Because of poor habits, many people are affected. 
As a result, awareness campaigns are being conducted. In conclusion, prevention is important."""),

("Climate Change Impact", """Climate change is affecting global weather patterns. 
However, efforts are being made to reduce pollution. Because of awareness, people are adopting eco-friendly practices. 
As a result, environmental protection is improving. In conclusion, action is necessary."""),

("Business Innovation Strategy", """Companies are investing in new technologies. 
However, risks are involved in innovation. Because of competition, businesses are evolving quickly. 
As a result, markets are changing rapidly. In conclusion, adaptability is key."""),

("online education" , """Online education is growing rapidly in recent years. 
For example, many students use digital platforms for learning. 
However, internet connectivity issues still exist in rural areas. 
Because of these challenges, governments are improving infrastructure. 
As a result, access to education is increasing. 
In conclusion, online learning is shaping the future of education."""),

("edge" , """However, the match was difficult, but the team won. 
Because of rain, the match was delayed, and because of poor lighting, it was stopped."""),

("cricket" , """India won the match. However, the match was difficult.
Because of strong batting, India succeeded.
As a result, fans celebrated. In conclusion, it was a great victory."""),
]


bad_docs = [

("Random Daily Thoughts", "Dog is running. Sky is blue. I like pizza. Table is wooden. Nothing connects here."),
("random", "Dog is running. Sky is blue. Pizza is tasty. Table is wooden. Phone is ringing."),
("Unrelated Ideas Mix", "The car is fast. Banana is yellow. I am happy today. Window is open. No relation exists."),
("Disconnected Story", "Apple is tasty. Ball is round. Cat is sleeping. Sun is hot. Random ideas here."),
("Mixed Objects Description", "Tree is green. Water is cold. Laptop is new. Music is loud. No connection between them."),
("Household Items List", "Chair is broken. Table is big. Fan is rotating. Light is bright. Words are unrelated."),
("Stationery Random Text", "Pen is blue. Pencil is sharp. Eraser is small. Scale is long. These are random items."),
("Electronic Confusion", "Phone is ringing. Charger is missing. Cable is short. Switch is off. No logical flow."),
("Transport Random Info", "Car is parked. Bus is late. Bike is fast. Train is long. No meaningful relation."),
("Weather Mixed Signals", "Rain is falling. Sun is hot. Cloud is white. Wind is strong. Mixed random thoughts."),
("Emotion Without Flow", "I am happy. I am sad. I am angry. I am excited. No proper structure or flow."),
]


# =======================
# RUN
# =======================
print("=== Ranking ===")
rank_all_documents(good_docs + bad_docs)

print("\n=== Group Comparison ===")
compare_groups(good_docs, bad_docs)