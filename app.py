import customtkinter as ctk

# Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        # Convert height to meters
        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        # BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.configure(text=f"BMI: {bmi}\nCategory: {category}")
    except ValueError:
        result_label.configure(text="Please enter valid numbers!")

# Main window
app = ctk.CTk()
app.title("BMI Calculator")
app.geometry("350x320")

# Title
title_label = ctk.CTkLabel(app, text="BMI Calculator", font=("Arial", 20, "bold"))
title_label.pack(pady=15)

# Weight input
weight_label = ctk.CTkLabel(app, text="Enter your weight (kg):")
weight_label.pack()
weight_entry = ctk.CTkEntry(app, width=200)
weight_entry.pack(pady=5)

# Height input (in cm)
height_label = ctk.CTkLabel(app, text="Enter your height (cm):")
height_label.pack()
height_entry = ctk.CTkEntry(app, width=200)
height_entry.pack(pady=5)

# Button
calc_button = ctk.CTkButton(app, text="Calculate BMI", command=calculate_bmi)
calc_button.pack(pady=15)

# Result
result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the app
app.mainloop()