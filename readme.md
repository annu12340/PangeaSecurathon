# Nexa

## 💡 Inspiration
In our current healthcare system, there exist numerous inefficiencies that adversely affect both patients and medical professionals. 

1. Long paper work:-  One prominent issue is the cumbersome paper work process patients encounter when visiting a healthcare facility. Each time a user steps into a hospital, they are compelled to **complete extensive, monotonous, and repetitive forms**. Regrettably, this bureaucratic ritual often leads to critical information being overlooked or omitted. Moreover, in **dire circumstances such as accidents or emergencies, medical practitioners are often left without fundamental patient data**, including blood type, ongoing medication, and family medical history. This conspicuous lack of crucial information contributes significantly to the inefficiency and suboptimal treatment outcomes within our healthcare system.

2. Medical errors:- The World Health Organization (WHO) has shed light on the severity of this predicament by reporting that more than **138 million patients suffer harm annually as a result of medical errors**. This alarming statistic serves as a stark reminder of the dire consequences of these inefficiencies and underscores the urgent need for improvement. 
Additionally, the current challenge with existing AI assistants in healthcare is their heavy reliance on personally identifiable data, which raises critical privacy and security issues. **The very technology meant to heal is, at times, inadvertently jeopardizing patient data.**

3. Medication mismanagement:- Furthermore, even when patients receive the correct treatment, there remains a persistent challenge: medication adherence. P**atients frequently forget to take their prescribed medications at the designated times**, leading to a continuous deterioration in their health. This cascading effect not only compromises individual well-being but also places an ever-increasing burden on healthcare systems, exacerbating the strain on resources and diminishing the overall quality of care.

## 🚀What it does
Nexa emerges as the beacon of hope, addressing these pressing healthcare challenges with groundbreaking solutions that hold the potential to revolutionize the entire healthcare journey:

1. QR Coded Health Card: In the era of Nexa, patients will embrace a paradigm shift as they carry a QR coded health card brimming with their comprehensive medical history, family medical lineage, meticulously cataloged medical reports, and other pivotal health-related details. Gone are the days of grappling with voluminous forms or battling memory lapses during life-threatening emergencies. **With a swift scan, this digital key unlocks a treasure trove of essential information**, offering immediate access to crucial insights that can be life-saving.

2. AI Diagnostic Assistant: Nexa has an AI diagnostic assistant that transcends the boundaries of traditional AI solutions. **What sets Nexa apart is its unwavering commitment to safeguarding user privacy**. Prior to invoking the AI model, Nexa employs a data protection mechanism using Pangea APPI that conceals all personally identifiable data, ensuring that sensitive health information remains confidential and secure. This groundbreaking approach redefines the boundaries of AI-powered healthcare, setting a new standard for privacy-conscious medical solutions.

3. Medication Reminder App: Nexa's multifaceted approach extends to the realm of medication management, where our dedicated app takes the reins in combating medication mismanagement. Through this user-friendly application, **patients can effortlessly configure personalized medication reminders, leaving no room for missed doses or scheduling errors.**

## ⭐Where Pangea API is used
#### Compliance
- Secure Audit Log: All important events are captured in the audit logs
- Redact: Redact is used to remove all PII before sending the data to the AI model to safe guard user privacy
- Embargo: When a user logs in, the app gets the user's IP address and checks whether the IP address is sanctioned

#### Intelligence
- Domain Intel: This is for blocking a user signing up into the app with an email that has a malicious domain 
- User Intel: When a user registers into the platform, the user intel is used to check if 
    i an email address
   ii.  username,
   iii. phone number etc was exposed in a security breach.

#### Data Protection
- Vault: Critical secrets like openai key, twilio ket etc are stored in vault and programmatically fetched from it

#### Detect
-  File Scan: When the user uploads any medical report pdf, we detect whether it is malicious or not

## 🏆 How Nexa satisfies the judgment criteria
 1. **Technological Implementation**: 
- Nexa seamlessly interacts with the pangea 10+ API to provide users with valuable healthcare solutions, showcasing well-structured and robust coding practices. 
- It also uses Twilio to make phone calls and celery to create a cron that constantly monitors the time and alert when it is time to consume the medicine
- It also has a speech to text convertor  and an openai assistant to help diagnose disease 
 
 2. **Design**
- User-Centric Design: Nexa places a strong emphasis on user-centric design. Every feature and interface element has been designed with the user's needs and preferences in mind. The QR-coded health card, AI diagnostic assistant, and medication reminder app are all designed to streamline the user's healthcare journey.
- Privacy Focus: The design also prioritizes user privacy. By concealing personally identifiable data before invoking the AI model, Nexa ensures that sensitive health information remains protected and compliant with privacy regulations.

 3. **Potential Impact** 
- Community Impact: Nexa has the potential to have a substantial impact on the Pangea community and beyond. By addressing critical healthcare challenges such as medication adherence, access to medical records, and efficient communication with healthcare providers, Nexa contributes to improved health outcomes and enhanced healthcare experiences for more than 10 million users.
- Data Privacy: By placing a strong focus on user data privacy, Nexa not only improves healthcare but also sets a precedent for secure and ethical data handling in healthcare technology.

## 🚧 Challenges we ran into
During the design and development process of Nexa, I encountered a series of intricate challenges. I ran into a lot of bugs while implementing the code for the project, especially the backend section. With the clock ticking down, prioritizing various tasks and managing deadlines was a challenge. Also because of lack of time, I couldn't properly do the demo as well
 Also doing everything solo and completing the project on time was very difficult

## 🎉 Accomplishments that we're proud of
I embraced the task of single-handedly developing Nexa, handling both the intricate backend technical aspects and crafting the appealing frontend interface you interact with. I am very pride of it

## 🌿 What's next for Nexa
- Due to lack of time, I couldn't implement all features in a proper manner
- Integration with blockchain
- Create a space for users to connect, share experiences, and provide support to one another 
- Integration with Wearable Devices
- Integrate a tool that helps users compare medication prices and find cost-effective options or prescription assistance programs.

