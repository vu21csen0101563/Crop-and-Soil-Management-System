# Example datasets for crops, soil management, and diseases
crops = {
    "wheat": {"soil_type": "loamy", "weather": "temperate", "nutrition": "high"},
    "rice": {"soil_type": "clay", "weather": "tropical", "nutrition": "moderate"},
    "corn": {"soil_type": "sandy", "weather": "subtropical", "nutrition": "high"},
    "millet": {"soil_type": "sandy", "weather": "arid", "nutrition": "high"},
    "sweet_potato": {"soil_type": "loamy", "weather": "tropical", "nutrition": "high"}
}

soil_recommendations = {
    "loamy": "Add organic compost and maintain pH between 6 and 7. Practice crop rotation to maintain soil health.",
    "clay": "Ensure good drainage and consider gypsum to improve structure. Use cover crops to prevent soil erosion.",
    "sandy": "Use organic matter to improve water retention. Mulching can help conserve soil moisture."
}

disease_data = {
    "leaf_spot": {
        "symptoms": ["small round dark spots", "yellow halo"],
        "solution": "Use a natural fungicide, such as neem oil, and remove affected leaves. Practice crop rotation."
    },
    "blight": {
        "symptoms": ["brown patches", "wilting", "leaf drop"],
        "solution": "Improve air circulation, use copper-based sprays if necessary, and avoid overwatering."
    },
    "powdery_mildew": {
        "symptoms": ["white powdery growth", "curling leaves"],
        "solution": "Use sulfur-based fungicide and remove infected plants. Ensure plants are not overcrowded."
    }
}

# Function to recommend crops based on soil type, weather, and nutrition contribution
def recommend_crop(soil_type, weather_conditions):
    suitable_crops = [crop for crop, conditions in crops.items()
                      if conditions["soil_type"] == soil_type and conditions["weather"] == weather_conditions]
    
    if suitable_crops:
        # Sort crops by their nutritional value to align with Zero Hunger
        suitable_crops.sort(key=lambda crop: crops[crop]["nutrition"], reverse=True)
        return suitable_crops
    else:
        return ["No suitable crops found for the given conditions."]

# Function to provide soil management recommendations focused on sustainability
def soil_management(soil_type):
    return soil_recommendations.get(soil_type, "No recommendations available for this soil type.")

# Function to identify diseases and recommend sustainable solutions
def identify_disease(symptoms):
    symptoms = symptoms.lower()
    for disease, details in disease_data.items():
        if all(symptom in symptoms for symptom in details["symptoms"]):
            return {"disease": disease.replace('_', ' ').title(), "solution": details["solution"]}
    return {"disease": "Unknown Disease", "solution": "No solution available for the given symptoms."}

# Main function to run the application
def main():
    while True:
        print("\nWelcome to the Crop and Soil Management System (Zero Hunger Focus)")
        print("1. Recommend a Crop")
        print("2. Soil Management")
        print("3. Identify Plant Disease")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            soil_type = input("Enter soil type (loamy, clay, sandy): ").lower()
            weather_conditions = input("Enter weather conditions (temperate, tropical, subtropical, arid): ").lower()
            recommended_crops = recommend_crop(soil_type, weather_conditions)
            print(f"Recommended Crops (with focus on nutrition and sustainability): {', '.join(recommended_crops)}")
        
        elif choice == '2':
            soil_type = input("Enter soil type (loamy, clay, sandy): ").lower()
            recommendations = soil_management(soil_type)
            print(f"Sustainable Soil Management Recommendations: {recommendations}")
        
        elif choice == '3':
            symptoms = input("Enter the symptoms of the plant (e.g., small round dark spots, yellow halo): ").lower()
            disease_info = identify_disease(symptoms)
            print(f"Disease Identified: {disease_info['disease']}")
            print(f"Sustainable Solution: {disease_info['solution']}")
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
