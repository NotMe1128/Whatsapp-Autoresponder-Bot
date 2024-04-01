import random
import psutil
from datetime import datetime, timedelta

def a8ball():
    """
    Simulates the Magic 8-Ball game by generating random answers.

    Returns:
        str: A random Magic 8-Ball answer.
    """
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    msg=f"""*=========🎱=========*
🔮»{random.choice(answers)}
*=========🎱=========*"""
    return msg

def calculate_expression(input_str):
    try:
        # Extract the expression after '!calc'
        expression = input_str[len("!calc"):].strip()
        # Evaluate the expression
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
    
def kinky(h):
    x=random.randrange(0,101)
    z1="▒▒▒▒▒▒▒▒▒▒  😐"
    z2="█▒▒▒▒▒▒▒▒▒  😐"
    z3="██▒▒▒▒▒▒▒▒  😐"
    z4="███▒▒▒▒▒▒▒  😐"
    z5="████▒▒▒▒▒▒  😳"
    z6="█████▒▒▒▒▒  😳"
    z7="██████▒▒▒▒  😳"
    z8="███████▒▒▒  😳"
    z9="████████▒▒  😳"
    z10="█████████▒  😳"
    z11="██████████▒  😳"
    z12="███████████  😳"
    if x==0:
        kinky_bar=z1
    elif x<=10:
        kinky_bar=z2
    elif x<=20:
        kinky_bar=z3
    elif x<=30:
        kinky_bar=z4
    elif x<=40:
        kinky_bar=z5
    elif x<=50:
        kinky_bar=z6
    elif x<=60:
        kinky_bar=z7
    elif x<=70:
        kinky_bar=z8
    elif x<=80:
        kinky_bar=z9
    elif x<=90:
        kinky_bar=z10
    elif x<=99:
        kinky_bar=z11
    else:
        kinky_bar=z12
    me=f"""*🌡️Kinky Meter!🌡️*
*{h}* is {x}% *Kinky*
        
{kinky_bar}
        """
    return(me)

def format_uptime(uptime_seconds):
    uptime = timedelta(seconds=uptime_seconds)
    days, seconds = uptime.days, uptime.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes = remainder // 60
    return f"{days} days, {hours} hours, {minutes} minutes"
def uptime():
    uptime_seconds = psutil.boot_time()
    formatted_uptime = format_uptime(uptime_seconds)
    return f"️♻️*Server Uptime*: {formatted_uptime}"
    

def roll_dice(input_str):
    try:
        # Split the input string into individual numbers
        numbers = list(map(int, input_str.split()))
        if len(numbers) == 1:
            num_sides = numbers[0]
            if num_sides <= 1:
                return "Error: The die must have at least 2 sides."
            return f"🎲Rolled a *{num_sides}*-sided die: {random.randint(1, num_sides)}"
        elif len(numbers) == 2:
            num1, num2 = sorted(numbers)
            return f"🎲Rolled a number between *{num1}* and *{num2}*: {random.randint(num1, num2)}"
        else:
            return "Error: Please provide either 1 or 2 numbers separated by spaces."
    except ValueError:
        return "Error: Invalid input. Please enter valid positive integers."
