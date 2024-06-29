Animal Health Monitoring and Diagnostics System

README

Abstract

Our system provides a comprehensive and user-friendly method for monitoring and diagnosing animal health issues. By continuously tracking vital signs like heart rate, blood oxygen levels, and temperature, we reduce veterinary costs and prevent serious disorders through early detection and treatment. Accessibility is ensured via an IVR system, a website, and a mobile app. Real-time telehealth integration enables instant veterinary consultations during emergencies, improving overall animal health.

Keywords:

1.Animal healthcare
2.Explainable AI (artificial intelligence)
3.Image classification (disease detection)
4.IoT (Internet of Things)

System Description:

1.Continuously monitors vital signs through wearable IoT sensors.
2.Provides user-friendly interfaces for mobile app, website, and IVR for accessibility.
3.Integrates real-time telehealth for immediate veterinary consultations.
4.Utilizes machine learning models for:
5.Identifying animal species in images.
6.Filtering noise from sensor data for accurate diagnoses.


Main Outcomes:

1.Continuous monitoring of vital signs.
2.Accessible via multiple platforms (mobile app, website, IVR).
3.Real-time telehealth consultations.
4.Machine learning for disease detection and animal identification.

Data:

1.Parameters: Heart rate, blood oxygen, temperature, species classification, disease detection, user access metrics, telehealth logs.
2.Sources: IoT sensors, digital images, user interactions, telehealth service logs.


Methodology:

1.Data Collection: Monitors vital signs and gathers images.
2.Machine Learning:
3.Identifies animal species in images.
4.Detects diseases from images.
5.Analyzes sensor data (e.g., ECG) for abnormalities.
6.Telehealth Integration: Enables real-time consultations with veterinarians.


Components:

1.IoT Device: Wears on the animal to track vital signs.
2.Web Interface: Provides access to system functionalities on a computer.
3.Mobile App: Offers a user-friendly platform for smartphones.
4.Datasets: Collections of data for training machine learning models (e.g., animal images, ECG recordings).
5.Machine Learning Models: Algorithms for specific tasks (e.g., image classification, disease detection, ECG analysis).
6.Convolutional Neural Networks (CNN) and EfficientNetB0 for image classification.
7.Random Forest for disease detection.
8.Gradient Descent for ECG analysis.
9.Telehealth Features: Provides video calls and chat functionality for consultations.

![Screenshot 2024-06-29 131312](https://github.com/supriyo010/funna-care/assets/130129570/a9264b24-1e54-4871-bc7e-78024e1fd2d4)



Accuracy and Results:

1.ECG Analysis: 86% accuracy.
2.Lumpy Skin Cancer Detection: 89% accuracy.
3.Image Classification: Over 80% accuracy.


Validation Strategy:

1.Data Validation: Ensures data quality through cleaning and verification.
2.Model Validation: Uses cross-validation techniques to assess model performance.
3.Telehealth Validation: Simulates consultations and gathers user feedback for improvement.
