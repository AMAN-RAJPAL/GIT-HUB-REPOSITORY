# Define a dictionary with some example diseases, precautions, and cures
import pyttsx3
engine=pyttsx3.Engine()
disease_info = {
    "cold": {
        "precautions": "Wash hands frequently, cover your mouth and nose when sneezing or coughing, stay hydrated.",
        "cure": "Get plenty of rest, drink fluids, and take over-the-counter cold medication."
    },
    "flu": {
        "precautions": "Get a flu shot, wash hands frequently, avoid close contact with sick people.",
        "cure": "Get plenty of rest, drink fluids, and take over-the-counter flu medication."
    },
    "headache": {
        "precautions": "Stay hydrated, manage stress, get regular sleep.",
        "cure": "Take over-the-counter pain relievers, rest in a quiet, dark room."
    },
    "gastroenteritis": {
        "precautions": "Practice good hand hygiene, avoid contaminated food or water, maintain food safety",
        "cure": "Rehydration with oral rehydration solutions, bland diet.."
    },
    "allergie": {
        "precautions": " Identify and avoid allergens, use air purifiers, follow prescribed allergy management plans.",
        "cure": "Antihistamines, decongestants, or allergy shots (immunotherapy)."
    },
    "cuts and scrapes": {
        "precautions": "Clean the wound, apply an antiseptic, cover with a bandage.",
        "cure": "Keep wounds clean, use protective gear, be cautious to prevent injuries."
    },
    "sunburn": {
        "precautions": "Use sunscreen, wear protective clothing, avoid prolonged sun exposure.",
        "cure": "Apply aloe vera or moisturizing cream, take pain relievers, stay hydrated."
    },
    "acne": {
        "precautions": "Maintain good skin hygiene, avoid squeezing pimples, use non-comedogenic skincare products.",
        "cure": "Topical creams, oral medications, or professional treatments."
    },
    "toothache": {
        "precautions": "Maintain good oral hygiene, including regular brushing and flossing.",
        "cure": "Visit a dentist for diagnosis and treatment, which may include fillings, extractions, or root canals."
    },
    "sprains and strains": {
        "precautions": " Warm-up before physical activity, use proper techniques, wear protective gear.",
        "cure": " R.I.C.E. (Rest, Ice, Compression, Elevation) and physical therapy if needed."
    },
    "asthma": {
        "precautions": " Identify triggers, avoid smoking, and follow an asthma action plan.",
        "cure": "Medications such as bronchodilators and inhaled corticosteroids."
    },
    "diarrhea": {
        "precautions": "Maintain food and water hygiene, avoid contaminated food.",
        "cure": "Rehydration with oral rehydration solutions and identifying and treating the underlying cause."
    },
    "constipation": {
        "precautions": "Maintain a high-fiber diet, stay hydrated, and be physically active",
        "cure": "Dietary changes, increased fluid intake, over-the-counter laxatives."
    },
    "hypertension": {
        "precautions": "Maintain a healthy diet, exercise regularly, limit sodium intake, and manage stress.",
        "cure": "Lifestyle changes, antihypertensive medications."
    },
    "urinary tract infection": {
        "precautions": "Stay hydrated, urinate regularly, wipe front to back.",
        "cure": "Antibiotics by doctor."
    },
    "sinusitis": {
        "precautions": " Use a humidifier, avoid irritants, manage allergies.",
        "cure": " Decongestants, saline nasal rinses, antibiotics (if bacterial)"
    },
    "back pain": {
        "precautions": "Maintain good posture, lift with your legs, exercise core muscles.",
        "cure": "Rest, hot/cold therapy, physical therapy."
    },
    "stress": {
        "precautions": "Practice relaxation techniques, exercise, seek support.",
        "cure": "Practice relaxation techniques, exercise, seek support."
    },
    "insomnia": {
        "precautions": "Maintain a regular sleep schedule, create a calming bedtime routine.",
        "cure": "Maintain a regular sleep schedule, create a calming bedtime routine."
    },
    "ear infections": {
        "precautions": "Avoid inserting objects in the ear, keep ears dry.",
        "cure": "Antibiotics (if bacterial), pain relievers, ear drops."
    },
    "skin rashes": {
        "precautions": " Keep skin clean and dry, avoid irritants, protect from the sun.",
        "cure": "Topical creams, antihistamines, avoiding irritants."
    },
    "acid reflux": {
        "precautions": "Avoid trigger foods, eat smaller meals, raise the head of your bed.",
        "cure": "Medications prescribed by a doctor, lifestyle changes."
    },
    "migraine": {
        "precautions": " Identify triggers, manage stress, maintain a regular schedule.",
        "cure": "Medications prescribed by a doctor, rest in a quiet, dark room."
    },
    "diabetes": {
        "precautions": "Maintain a balanced diet, regular exercise, monitor blood sugar levels, and follow medical advice.",
        "cure": "Lifestyle changes, medications (oral or insulin)."
    },
    "jaundice": {
        "precautions": "taking a lot of fluids like radish juice",
        "cure": "natural sunlight."
    },
    "food poisoning": {
        "precautions": " Practice food safety, proper cooking, and storage.",
        "cure": "Rest, hydration, and, in severe cases, medical attention."
    },
    "heartburn": {
        "precautions": "Avoid trigger foods, maintain a healthy weight.",
        "cure": "Antacids, H2 blockers, lifestyle changes."
    },
    "Insect Bites": {
        "precautions": " Use insect repellent, wear protective clothing.",
        "cure": "Antihistamines,topical ointments."
    },
    "hay fever": {
        "precautions": "Avoid allergens, use antihistamines.",
        "cure": "Antihistamines, decongestants."
    },
    "conjunctivitis": {
        "precautions": "Good hand hygiene, avoid touching your eyes.",
        "cure": "Antibiotic eye drops (if bacterial), antihistamines (if allergic)."
    },
    "athlete's foot": {
        "precautions": "Keep feet clean and dry, wear clean socks and shoes.",
        "cure": "Antifungal creams or powders."
    },
    "cough": {
        "precautions": "Good hygiene practices, avoid irritants.",
        "cure": "Cough drops, expectorants, antitussives."
    },
    "anxiety": {
        "precautions": "Practice stress-reduction techniques, seek therapy",
        "cure": "Therapy, medications (if severe)."
    },
    "depression": {
        "precautions": "Seek support, talk to a mental health professional.",
        "cure": "Therapy, medications."
    },
    "common warts": {
        "precautions": "Avoid contact with warts, keep hands clean.",
        "cure": "Over-the-counter treatments, cryotherapy, laser therapy."
    },
    "eczema": {
        "precautions": "Moisturize skin, avoid trigger irritants.",
        "cure": "Topical corticosteroids, antihistamines, moisturizers"
    },
    "osteoarthritis": {
        "precautions": "Maintain a healthy weight, regular exercise.",
        "cure": " Pain relievers, physical therapy, joint injections."
    },
    "tonsillitis": {
        "precautions": "Good hand hygiene, avoid close contact with infected individuals.",
        "cure": "Antibiotics (for bacterial tonsillitis), rest, pain relievers."
    },
    "bronchitis": {
        "precautions": " Avoid irritants, maintain good hygiene.",
        "cure": "Rest, hydration, cough medicine (if needed)."
    },
    "pneumonia": {
        "precautions": "Get vaccinated, maintain good hygiene.",
        "cure": "Antibiotics, rest, oxygen therapy (in severe cases)."
    },
    "gout": {
        "precautions": "Maintain a healthy diet, avoid trigger foods.",
        "cure": "Medications, lifestyle changes, diet modifications."
    },
    "anemia": {
        "precautions": "Eat a diet rich in iron and vitamins.",
        "cure": "Iron supplements, vitamin supplements, dietary changes."
    },
    "high cholesterol": {
        "precautions": "Maintain a healthy diet, regular exercise",
        "cure": "Medications, lifestyle changes."
    },
    "Sunstroke": {
        "precautions": "Stay hydrated, avoid excessive heat",
        "cure": "Immediate cooling, medical attention."
    },
    "covid-19": {
        "precautions": "Follow public health guidelines, get vaccinated, and practice good hygiene.",
        "cure": " Consult with healthcare professionals for personalized cancer treatment."
    },
    "typhoid": {
        "precautions": "Practice good hygiene, including frequent handwashing and consuming only safe, clean water and food.",
        "cure": "Typhoid can be treated with antibiotics prescribed by a healthcare professional; early diagnosis and treatment are essential."
    },
    "cancer": {
        "precautions": " Maintain a healthy lifestyle with a balanced diet, regular exercise, and avoid exposure to carcinogens.",
        "cure": "Early detection and medical intervention offer the best chance for cancer treatment; consult a healthcare professional for personalized care."
    },
    "frostbite": {
        "precautions": " Dress warmly, avoid prolonged exposure to extreme cold.",
        "cure": "Gradual rewarming, medical attention"
    },
    "dogbite": {
        "precautions": "Avoid approaching unfamiliar dogs, especially when they seem agitated or frightened.",
        "cure": "Clean the wound with soap and water, apply an antiseptic, and seek immediate medical attention to prevent infection."
    },
    "motion sickness": {
        "precautions": " Sit in a forward-facing seat while traveling to reduce motion sickness.",
        "cure": "Close your eyes, focus on the horizon, and take slow, deep breaths if you start feeling motion sick"
    }
    
}
# Get user input
user_disease = input("Enter the name of the disease: ").lower()
x='''TAKE A GLASS FULL OF HOT WATER, ADD 1 TEASPOON HONEY, ADD TURMERIC POWDER WITH BLACK PEPPER, AND DRINK IT SIP BY SIP.(ALSO YOU CAN ADD GUD IN WINTERS)'''
y='''please do not take medicines prescribed on google, as medicines contain chemicals and it may not suit your body; also if taken more doses can effect your body may lead to bad health'''
# Check if the disease is in the dictionary

if user_disease in disease_info:
    precautions = disease_info[user_disease]["precautions"]
    cure = disease_info[user_disease]["cure"]
    
    print(f"Information for {user_disease.capitalize()}:")
    print(f"Precautions: {precautions}")
    print(f"Cure: {cure}")
    print(x)
else:
    print("Disease not found in the database. Please enter a valid disease.")

engine.say(f"Information for {user_disease.capitalize()}:")
engine.say(f"Precautions: {precautions}")
engine.say(f"Cure: {cure}")
engine.say(x)
engine.say(y)
engine.say("Disease not found in the database. Please enter a valid disease.")
engine.runAndWait()

print("Execution complete. Press Enter to exit.")
input()