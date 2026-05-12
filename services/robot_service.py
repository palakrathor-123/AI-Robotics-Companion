# app/services/robot_service.py
from hardware.controller import robot

def send_robot_command(action_type):
    if action_type == "wave_hand":
        robot.wave_hand()
    elif action_type == "nod":
        robot.move_head(90)
    else:
        print(f"Unknown action: {action_type}")