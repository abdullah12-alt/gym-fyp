from django.shortcuts import render
from django.http import JsonResponse

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message.lower() == 'hi':
            response = 'Hello there, how can I help you?'
        elif message.lower() == 'give me my diet plan':
            response = 'Tell me your weight.'
        else:
            try:
                weight = float(message)
                bmi = calculate_bmi(weight)
                diet_plan = generate_diet_plan(bmi)
                response = f'Here is your diet plan for BMI {bmi}: {diet_plan}'
            except ValueError:
                response = 'Please enter a valid weight.'
        
        return JsonResponse({'message': response})
    
    return render(request, 'chat.html')

def calculate_bmi(weight):
    # BMI calculation logic goes here
    # Implement your own formula or use a library for calculating BMI
    # Example: bmi = weight / (height * height)
    bmi = weight / (1.7 * 1.7)
    return round(bmi, 2)

def generate_diet_plan(bmi):
    # Diet plan generation logic goes here
    # Implement your own logic based on the BMI range
    if bmi < 18.5:
        return 'You are underweight. Consume more calories and focus on gaining weight.'
    elif 18.5 <= bmi < 24.9:
        return 'You have a healthy weight. Maintain a balanced diet and exercise regularly.'
    elif 24.9 <= bmi < 29.9:
        return 'You are overweight. Reduce calorie intake and engage in regular physical activity.'
    else:
        return 'You are obese. Consult a healthcare professional for a personalized diet plan.'
