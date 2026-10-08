# Week 1.2, Session 2: Task 6
# Machine monitoring system



temperature = int(input("Enter the machine temperature in degrees Celsius: "))
pressure = int(input("Enter the machine pressure in PSI: "))
status = int(input("Enter the machine operational status (1 for operating, 0 for stopped): "))

if temperature > 80:
    temperature_status = "Temperature is too high. Shut down the machine."
elif 50 <= temperature <= 80:
    temperature_status = "Temperature is within safe limits."
else:
    temperature_status = "Machine temperature is low. No action is needed."

if pressure > 100:
    pressure_status = "High pressure is detected. Recommend maintenance."
elif 70 <= pressure <= 100:
    pressure_status = "Pressure is stable."
else:
    pressure_status = "Pressure is low. The system is operating normally."

if status == 1:
    if temperature > 80 or pressure > 100:
        machine_status = "Machine is running in unsafe conditions. Shut it down immediately."
    else:
        machine_status = "Machine is running normally."
else:
    machine_status = "Machine is stopped. No immediate action is needed."

print(temperature_status)
print(pressure_status)
print(machine_status)


