import PySimpleGUI as sg
import pyttsx3

def calculate_depression_score(answers):
    score = sum(answers.values())  
    return score
sg.theme('DarkPurple')
def categorize_depression_level(score):
    if score <= 20:
         x = "Congratulations you are healthy, atleast mentally, to have a healthy life and a long one, you should till consider following the golden rules"
         engine.say(x)
         engine.runAndWait()
         return "1 - Healthy"
    elif score <= 40:
        x = '''According to this quiz you have Mild Depression, some ways you can feel better are
        Regular exercise can be a great help to get relief from mild depression.
        *Healthy diet-: Eating the right foods can enhance serotonin production in the brain and banish depressive symptoms.
        *Light Therapy it can be done  easily by  purchasing a light box that mimic's the sun's rays without the harmful UV rays. 
        Exposure to this special light for one hour per day can result in a significantly improved mood.
        *spending time with dogs or a pet animal can relief your mind from all the stree that you have.
        '''
        engine.say(x)
        engine.runAndWait()
        return "2 - Mild depression"    
    elif score <= 120:
        x = '''According to this quiz you have Moderate levels of depression, some ways you can feel better are:
        Seeking out social support helps a lot in this type of depression recreational
          activities like picnic etc can help you to get away from all type of depression.
          Light Therapy :it can be done  easily by
            purchasing a light box that mimic's the sun's rays without the harmful UV rays. Exposure to this special light for one hour per day 
            can result in a significantly improved mood.
            Devotion in god and moving blueberry beads can help a lot.
'''
        engine.say(x)
        engine.runAndWait()
        return "3 - Moderate depression"
    elif score <= 160:
        x = '''According to this quiz you have Severe Depression : Cognitive behavioral therapy-: it helps to change negative and distorted thought
          patterns and beliefs from mind of infected person.
        Behavioral activation therapy-: it helps the individual “identify activities they find pleasurable and engaging, 
        help then to enhance it and loosen stress”'''
        engine.say(x)
        engine.runAndWait()
        return "4 - Severe depression"
    else:
        x = '''According to this quiz you have Very Severe Depression, Some ways you can feel better are: 
        Electroconvulsive therapy (ECT): it helps to remove all negativity makes a depressed mind fresh by  delivery of electric currents to 
        the brain to cause a quick seizure. Lifestyle changes Adjustments to your everyday routine — such as with sleep, exercise, and diet — may aid in improving mood
        Cognitive behavioral therapy-: it helps to change negative and distorted thought patterns and beliefs from mind of infected person. 
        Behavioral activation therapy-: it helps the individual “identify activities they find pleasurable and engaging, help then to enhance it and loosen stress”
        '''
        return "5 - Very severe depression"     
    y = '''Apart from all that, there are a few more things you can follow in your day to day life that would help you lead a healthier life, both mentally and physically.
    these are what we like to call the Golden Rules:
    Regular exercise can be a great help to get relief from mild depression 
    Healthy diet-: Eating the right foods can enhance serotonin 
    production in the brain and banish depressive symptoms. 
    Increasing the amount of proteins, healthy fats, zinc and potassium along with fruits while simultaneously cutting processed 
    foods and high sugar beverages will significantly improve your mental and physical health.
    MEDITATION:
    Meditation is a practice which involves trying to train you to be mindful and your thoughts
    to stay in the present moment, because in the present moment there is true peace. 
    it helps to make our mind peace and remove depression
    Cold Showers-: Taking Very cold showers or ice baths can cause spikes in the dopamine levels and serotonin levels that can last 
    longer than more than a few hours giving you more energy throughout the day.
    Journaling:  Journaling at the end of the day is a great way to track your progress and also winding down. Just as the case was with Meditation,
      Journalling also helps you be more mindful throughout the day.

    ''' 
      
engine = pyttsx3.init()

intro_text = '''
Welcome to the Mental Health Quiz!
Mental health is a crucial aspect of overall well-being. It refers to our emotional,
 psychological, and social well-being, 
affecting how we think, feel, and act. Mental health is vital at every stage of life,
 from childhood and adolescence through adulthood.
Maintaining good mental health allows us to handle the challenges and stresses of life,
 have healthy relationships, and make meaningful 
contributions to our communities.
 It is important to prioritize mental health and seek support when needed.
This quiz aims to provide a general assessment of your mental well-being.
 Please answer each question honestly and on a scale of 1 to 10,
 with 1 being the least and 10 being the most severe.
'''
engine.say(intro_text)
engine.runAndWait()
layout = [
    [sg.Text(intro_text)],
    [sg.Button('Start Quiz')],
    [sg.Output(size=(60, 20), key='-OUTPUT-')]
]

window = sg.Window('Mental Health Quiz', layout)


while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Start Quiz':
        window['-OUTPUT-'].update('')

        questions = {
    'question1': "On a scale of 1 to 10, how often have you been feeling down or depressed?",
    'question2': "On a scale of 1 to 10, how often do you get the feeling of being hopeless or worthless?",
    'question3': "On a scale of 1 to 10, how often do you have little interest or pleasure in doing things or find yourself procrastinating?",
    'question4': "On a scale of 1 to 10, how often have you had trouble falling asleep, staying asleep, or sleeping too much?",
    'question5': "On a scale of 1 to 10, how often do you have days when you have very low/no energy?",
    'question6': "On a scale of 1 to 10, how often do you feel anxious or have excessive worry?",
    'question7': "On a scale of 1 to 10, how often do you have difficulty concentrating or making decisions?",
    'question8': "On a scale of 1 to 10, how often do you feel restless or agitated?",
    'question9': "On a scale of 1 to 10, how often do you have thoughts of self-harm or suicide?",
    'question10': "On a scale of 1 to 10, how often do you experience changes in appetite or significant weight loss/gain?",
    'question11': "On a scale of 1 to 10, how often do you feel guilty or blame yourself for things?",
    'question12': "On a scale of 1 to 10, how often do you find it hard to enjoy or have fun with friends or family?",
    'question13': "On a scale of 1 to 10, how often do you have trouble with memory or forget things easily?",
    'question14': "On a scale of 1 to 10, how often do you experience physical symptoms without any underlying medical condition?",
    'question15': "On a scale of 1 to 10, how often do you have difficulty in social situations or fear of being judged?",
     'question16': "On a scale of 1 to 10, how often do you feel lonely or isolated?",
    'question17': "On a scale of 1 to 10, how often do you have difficulty in performing daily tasks or responsibilities?",
    'question18': "On a scale of 1 to 10, how often do you experience irritability or anger outbursts?",
    'question19': "On a scale of 1 to 10, On a scale of 1 to 10, how often do you engage in self-isolating behaviors or withdraw from social interactions?",
    'question20': "On a scale of 1 to 10, how often do you have difficulty in managing stress or coping with life's challenges?",
}

        
        answers = {}
        for question, prompt in questions.items():
            engine.say(prompt)
            engine.runAndWait()
            while True:
                try:
                    answer = int(sg.popup_get_text(prompt + " (Enter a value from 1 to 10): "))
                    if 0 <= answer <= 10:
                        break
                    else:
                        sg.popup_error("Invalid answer. Please enter a value from 1 to 10.")
                except ValueError:
                    sg.popup_error("Invalid answer. Please enter a numeric value.")
            answers[question] = answer

        
        score = calculate_depression_score(answers)      
        depression_level = categorize_depression_level(score)
        
        sg.popup("Quiz Results:",
                 "Depression Score: " + str(score),
                 "Depression Level: " + depression_level)

        engine.say("Quiz Results:")
        engine.say("Depression Score: " + str(score))
        engine.say("Depression Level: " + depression_level)

        
        engine.runAndWait()

# Close the window
window.close()