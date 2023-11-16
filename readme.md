
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

**Potential Impact** 
- Community Impact: Nexa has the potential to have a substantial impact on the Pangea community and beyond. By addressing critical healthcare challenges such as medication adherence, access to medical records, and efficient communication with healthcare providers, Nexa contributes to improved health outcomes and enhanced healthcare experiences for more than 10 million users.
  
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


